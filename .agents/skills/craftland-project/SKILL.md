---
name: craftland-project
description: Maintain the Craftland Expert knowledge repository, source archive, script index, prompts, documentation and verification records.
---

# Craftland Project

Use `craftland-core` for general Craftland expertise whenever both skills are available. This skill governs only the Craftland Expert repository at the active project root.

## Repository workflow

1. Read root `AGENTS.md`, `REPOSITORY.md`, the relevant knowledge page, and `CONTRIBUTING.md`.
2. Keep the original Project 5 `Craftland-Extraction/` immutable. Project 6's source extraction remains read-only at `D:\My project (6)\Craftland-Extraction\`; repository-preserved indexes and its 14 instruction files are under `sources/hungry-fish-2.0/`. Add future evidence separately; never overwrite a source archive silently.
3. Search before editing. Update the canonical topic page and only affected indexes/references. Keep detailed technical material in `knowledge/`, not duplicated in this skill.
4. Maintain the two separate FC indexes: 63 Project 5 scripts in `knowledge/scripting/fc-script-index.md` and 93 Project 6 scripts in `knowledge/scripting/hungry-fish-2.0-script-reference.md` plus the linked CSV. Preserve project-specific paths, graph names, imports, declarations, terminology, and limits. Do not merge or deduplicate by name alone.
5. Keep project-specific mechanics in `knowledge/projects/` and comparisons in `knowledge/project-comparisons/`. Promote a pattern to general guidance only with explicit supporting evidence and retain its scope.
6. Add script source copies only when purpose/behavior/dependencies/limitations are understood and redistribution is appropriate. Keep original projects read-only by default; current policy has no approved FC copies.
7. Preserve the 14 Project 6 instruction copies as historical text under `sources/`; they are 13 unique texts and are not prompts. New prompt files remain labelled `NEW REUSABLE PROMPT` and cite documented workflows.
8. Record facts with `VERIFIED`, `OBSERVED`, `INFERRED`, `UNVERIFIED`, or `UNKNOWN`; never upgrade evidence without a source or actual validation.
9. Record important decisions in repository documentation and add a dated `CHANGELOG.md` entry.
10. Audit both script counts, ECA records, internal links, duplicate material, source hashes, and secret patterns. Report exactly what checks ran. Do not claim runtime/build validation unless it occurred.

## Installation and release boundaries

Global installation target is `~/.agents/skills/craftland-core/`; inspect and back up an existing installation before any authorized update. Do not upload or publish this repository without the user's instruction. Do not choose a license; `LICENSE` remains a placeholder.
