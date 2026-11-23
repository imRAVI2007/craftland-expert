# Hungry Fish 2.0 files not semantically inspected

The captured baseline has 2,840 files. The extraction reports 252 files received content/structure inspection and 2,588 remaining with inventory coverage only, plus targeted keyword scans for some text files. This is not a claim that all 252 were semantically analyzed; several groups were signature-indexed or editor-queried.

## Inspection groups named in the extraction

- 93 `.fcg` files: source signatures/imports indexed; 18 receive narrative logic notes. No script execution or compilation.
- 14 local instruction/rule/reference files: preserved verbatim; 13 unique texts because two asset-rule copies are exact duplicates.
- 137 editor records: one main scene, three project ECA graphs, 20 UI assets, 70 project prefabs, 27 player-data definitions, and 16 project-setting modification modules queried through Craftland Studio.
- Eight additional project/config/support files were read, but the extraction overview does not identify those eight paths individually. Their exact classification cannot be reconstructed without more evidence.

The counts sum to 252 when the 18 narrative module notes are treated as a subset of the 93 scripts, not an additional group.

## Remaining uninspected or partial-review areas

The full path/size list is the [baseline FILE_INVENTORY.csv](../sources/hungry-fish-2.0/indexes/FILE_INVENTORY.csv). The extraction does not include a per-file inspected/uninspected manifest, so it would be misleading to label an exact 2,588-row subset as known. Treat all inventory paths outside the named inspection groups below as **inspection status not recorded**; some text files received targeted keyword scans, not complete review.

- Visual meaning and settings of models/meshes, textures, sprite sheets, animations, materials, particles, and audio.
- Serialized settings not among the 16 queried project-setting modification modules; detailed editor properties not covered by the captured MCP queries.
- Libraries, generated symbols, cache/build/timeline files, sidecars, and support files not individually named as inspected.
- The 2,588 inventory-only/targeted-scan files as a group; use the inventory for their exact original paths and byte sizes.

## Questions that need new evidence

- Which exact eight project/config/support paths were the additional inspected files?
- Which project-setting modules and all other setting assets control the conflicting workflow values?
- What is the selected map ID and complete terrain profile for the main scene?
- What are runtime results for DataStorage failure paths, zero score reads, spawn selection, match results, and leaderboard calls?
- What do unreviewed visual/audio assets represent, and how are remaining asset properties configured?

**Sources:** `D:\My project (6)\Craftland-Extraction\01_PROJECT_OVERVIEW.md`, `02_COMPLETE_FILE_INDEX.md`, `14_UNKNOWN_INFORMATION.md`.
