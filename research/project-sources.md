# Project source register

Audit date: 2026-11-23 (Asia/Calcutta). The register keeps the two Craftland projects distinct.

## Project 5 — Steal A Pet Template

- **Original project:** `D:\My project (5)` (read-only during its extraction; not modified during this merge).
- **Extraction source:** `Craftland-Extraction/` in this repository, copied from `D:\My project (5)\Craftland-Extraction\`.
- **Coverage:** 15 Markdown docs; 63 FC scripts; 17 archived tutorial/instruction sources; 27 prefab trees; 10 UI trees; component/enum records; one read-only built-in ECA graph; CSV, scene, map, and gameplay summaries.
- **Limitations:** no runtime/build/playtest; source summary warns of incomplete semantic review for serialized details. See [status register](knowledge-status.md) and [unknowns](../knowledge/troubleshooting/known-issues.md).

## Project 6 — Hungry Fish 2.0

- **Original project:** `D:\My project (6)` (read-only for this work; no source asset changed).
- **Extraction source:** `D:\My project (6)\Craftland-Extraction\` (15 Markdown documents, `FILE_INVENTORY.csv`, `SCRIPT_INDEX.csv`). The original extraction files remain there, unmodified.
- **Repository-preserved artifacts:** the two CSVs and 14 instruction-file copies under [sources/hungry-fish-2.0](../sources/hungry-fish-2.0/). The instruction copies were hash-checked against original files. No original game scripts/assets were copied.
- **Coverage:** inventory baseline 2,840 paths across 772 directories; all 93 `.fcg` entries indexed; 18 modules with narrative logic notes; three local ECA graphs; 20 UI trees; 70 project prefabs; 27 playerdata definitions; 14 local instruction copies / 13 unique texts; selected scene, config, and project-setting records. The extraction reports 252 files inspected for content/structure and 2,588 with inventory-only or targeted-scan coverage.
- **Validation:** inventory paths and sizes exactly match the 2,840-file baseline; 93 source paths equal the 93 script-index paths; 14 instruction copies correspond to original files; 0 credential-pattern matches in the extraction docs/indexes or instruction sources.
- **Limitations:** no runtime/build/playtest, no code execution, no Git history, and no complete semantic review of all files/assets. Website, Discord, auth, and external API systems were not established in the inspected local project. Selected map ID and some serialized setting precedence remain unknown.
- **Uninspected-file register:** [inspection gaps](project-6-inspection-gaps.md) describes the named review groups and clearly marks the eight additional paths that the extraction did not enumerate; the complete inventory remains the path authority.

## Evidence terms

Use `VERIFIED`, `OBSERVED`, `INFERRED`, `UNVERIFIED`, and `UNKNOWN` as defined in [knowledge-status.md](knowledge-status.md). “Verified” means supported by the cited local artifact; it does not mean runtime validated. A common pattern in both projects is not an editor-wide guarantee.
