#!/usr/bin/env python3
"""Refresh declaration details in the Craftland Expert FC script index.

Reads original Assets/Scripts/**/*.fcg files without changing them. It updates
the source declaration sections in knowledge/scripting/fc-script-index.md while
leaving the extraction-authored behavior/dependency/caveat summaries intact.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


GRAPH_RE = re.compile(r"^\s*(?:static\s+)?graph\s+[A-Za-z_]\w*\s*\{")
FUNC_RE = re.compile(r"^\s*(?:async\s+)?func\s+[A-Za-z_]\w*\s*\(")
EVENT_RE = re.compile(r"^\s*event\s+[A-Za-z_]\w*\s*\(")
FIELD_RE = re.compile(r"^\s*(?P<name>[A-Za-z_]\w*)\s+(?P<type>[^=]+?)(?:\s*=\s*(?P<init>.*))?\s*$")
INFERRED_RE = re.compile(r"^\s*(?P<name>[A-Za-z_]\w*)\s*=\s*(?P<init>.*)$")


def brace_delta(line: str) -> int:
    # The project source's top-level declarations use ordinary FC braces.
    # Braces in strings/comments can make this approximate; field extraction is
    # restricted to graph depth 1 and is checked against the 63-file inventory.
    return line.count("{") - line.count("}")


def declaration(lines: list[str], start: int) -> tuple[str, int]:
    parts = [lines[start].strip()]
    balance = parts[0].count("(") - parts[0].count(")")
    end = start
    while balance > 0 and end + 1 < len(lines):
        end += 1
        part = lines[end].strip()
        parts.append(part)
        balance += part.count("(") - part.count(")")
    value = " ".join(parts).split("//", 1)[0].strip()
    value = re.split(r"\s*\{", value, maxsplit=1)[0].rstrip("; ")
    return value, end


def source_declarations(path: Path) -> tuple[list[str], list[str], list[str]]:
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    functions: list[str] = []
    events: list[str] = []
    fields: list[str] = []
    depth = 0
    in_graph = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if not in_graph and GRAPH_RE.match(line):
            in_graph = True
            depth = 1
            i += 1
            continue
        if in_graph and depth == 1:
            if FUNC_RE.match(line) or EVENT_RE.match(line):
                value, end = declaration(lines, i)
                (functions if FUNC_RE.match(line) else events).append(value)
                # Count braces for the entire signature/body-opening range.
                depth += sum(brace_delta(item) for item in lines[i : end + 1])
                i = end + 1
                if depth <= 0:
                    in_graph = False
                continue
            if not re.match(r"^\s*(?://|/\*|\*|\[|$|\}|import\b)", line):
                match = FIELD_RE.match(line)
                if match and match.group("type").strip() and not re.match(
                    r"^(?:func|async|event|graph|enum|component|tuple|alias|define)\b",
                    line.strip(),
                ):
                    item = f"{match.group('name')}: {match.group('type').strip()}"
                    if match.group("init") is not None:
                        item += f" = {match.group('init').strip()}"
                    fields.append(item)
                else:
                    inferred = INFERRED_RE.match(line)
                    if inferred:
                        fields.append(
                            f"{inferred.group('name')} (inferred) = {inferred.group('init').strip()}"
                        )
        depth += brace_delta(line)
        if in_graph and depth <= 0:
            in_graph = False
        i += 1
    return functions, events, fields


def inline(values: list[str]) -> str:
    tick = "`"
    return "; ".join(f"{tick}{value}{tick}" for value in values) if values else "none"


def refresh(repo: Path, project: Path) -> tuple[int, int]:
    index_path = repo / "knowledge/scripting/fc-script-index.md"
    text = index_path.read_text(encoding="utf-8-sig")
    script_root = project / "Assets/Scripts"
    source_files = sorted(script_root.rglob("*.fcg"))
    source_map = {
        path.relative_to(project).as_posix(): source_declarations(path)
        for path in source_files
    }
    heading_re = re.compile(r"(?m)^#### `(?P<path>Assets/Scripts/[^`]+\.fcg)`$")
    headings = list(heading_re.finditer(text))
    updated = 0
    for pos, heading in reversed(list(enumerate(headings))):
        source_path = heading.group("path")
        if source_path not in source_map:
            continue
        functions, events, fields = source_map[source_path]
        start = heading.start()
        end = headings[pos + 1].start() if pos + 1 < len(headings) else len(text)
        section = text[start:end]
        section = re.sub(
            r"(?m)^- \*\*Functions, inputs and outputs(?: \(direct source signatures\))?:\*\*.*$",
            "- **Functions, inputs and outputs (direct source signatures):** " + inline(functions),
            section,
        )
        section = re.sub(
            r"(?m)^- \*\*Entry points:\*\*.*$",
            "- **Event signatures (direct source):** " + inline(events),
            section,
        )
        section = re.sub(
            r"(?m)^- \*\*Graph fields \(direct source\):\*\*.*$",
            "",
            section,
        )
        section = re.sub(
            r"(?m)^- \*\*Graph:\*\*.*$",
            lambda match: match.group(0)
            + "\n- **Graph fields (direct source):** "
            + inline(fields),
            section,
            count=1,
        )
        text = text[:start] + section + text[end:]
        updated += 1
    index_path.write_text(text, encoding="utf-8")
    return len(source_files), updated


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    count, updated = refresh(args.repo_root.resolve(), args.project_root.resolve())
    print(f"Read {count} FC source files; refreshed {updated} indexed entries.")
    if count != 63 or updated != 63:
        raise SystemExit("Expected exactly 63 source files and 63 indexed entries; review the paths.")


if __name__ == "__main__":
    main()
