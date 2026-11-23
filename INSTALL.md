# Installation

## Global Craftland core

The global skill is installed at `%USERPROFILE%\.agents\skills\craftland-core\` (on this machine, `C:\Users\dell\.agents\skills\craftland-core\`). The installed copy contains `SKILL.md` plus the knowledge, research, extraction, and source-reference files needed by its instructions. The combined skill is backed by both projects, with project references kept distinct.

To install into a new profile, inspect the destination first and stop if it exists:

```powershell
$repo = 'C:\Users\dell\Desktop\craftland-expert'
$destination = Join-Path $env:USERPROFILE '.agents\skills\craftland-core'
if (Test-Path -LiteralPath $destination) {
  throw "Destination exists; review and back it up before updating: $destination"
}
New-Item -ItemType Directory -Force -Path $destination | Out-Null
Copy-Item -LiteralPath (Join-Path $repo 'skills\craftland-core\SKILL.md') -Destination $destination
foreach ($reference in @('knowledge','research','Craftland-Extraction','sources\hungry-fish-2.0')) {
  Copy-Item -LiteralPath (Join-Path $repo $reference) -Destination $destination -Recurse
}
```

### Updating an existing install

Read the repository and installed skill first. Before replacing any installed file, copy the entire current skill folder to a new, non-existing timestamped backup path. Confirm the backup hash/file count, then update `SKILL.md` and its referenced `knowledge/`, `research/`, `Craftland-Extraction/`, and `sources/hungry-fish-2.0/` files. Do not overwrite unrelated files or an existing backup. Verify installed relative links and hashes against the reviewed repository source.

## Project skill

The repo-discoverable skill is [.agents/skills/craftland-project/SKILL.md](.agents/skills/craftland-project/SKILL.md). Its packaged mirror is [skills/craftland-project/SKILL.md](skills/craftland-project/SKILL.md); keep both byte-identical. It governs maintenance here and delegates Craftland assistance to `craftland-core`.

## Discovery and use

Codex discovers a skill when its `SKILL.md` is in a configured skill search location and the active agent loads it. Load `craftland-core` for Craftland tasks. When maintaining this repository, also load `craftland-project`, read root [AGENTS.md](AGENTS.md), identify the relevant project in [project-sources.md](research/project-sources.md), and open its project-specific references.

The `knowledge/` library and source references are required context; the skill file is intentionally concise. Do not assume either project's details apply to another project without independent evidence.

## Updating knowledge

Follow [CONTRIBUTING.md](CONTRIBUTING.md): preserve source provenance, edit the canonical reference, update affected cross-links/indexes, record material decisions in [CHANGELOG.md](CHANGELOG.md), and run documentation audits. Keep both original Craftland projects read-only unless a separate task authorizes source changes.
