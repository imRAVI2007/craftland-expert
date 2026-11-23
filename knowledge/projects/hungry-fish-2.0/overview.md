# Hungry Fish 2.0 project overview

**Project identity:** this is the separate `hungry-fish-2.0` / `PUGC - Hungry Fish 2.0` Craftland project at `D:\My project (6)`. The extraction is an inventory snapshot with targeted semantic inspection, not a complete review of every file.

## Verified scope

- Baseline inventory: 2,840 project files across 772 directories. The repository copy of the inventory is [FILE_INVENTORY.csv](../../../sources/hungry-fish-2.0/indexes/FILE_INVENTORY.csv).
- 93 `.fcg` files under `Assets/_Scripts/`, each represented in the [searchable script index](../../scripting/hungry-fish-2.0-script-reference.md) and the original [SCRIPT_INDEX.csv](../../../sources/hungry-fish-2.0/indexes/SCRIPT_INDEX.csv).
- 18 important modules have narrative source-flow notes in [module notes](../../scripting/hungry-fish-2.0-module-notes.md).
- Studio inspection covered one main scene, three project ECA graphs, 20 UI assets, 70 project prefabs, 27 PlayerData definitions, and 16 project-setting modification modules. The separate extraction overview gives the query scope.
- 14 instruction-file copies representing 13 unique texts are preserved byte-for-byte under [sources/hungry-fish-2.0/instructions](../../../sources/hungry-fish-2.0/instructions/). Two asset-rule copies are an exact duplicate pair. They are historical project guidance, not prompts for execution in this repository.

## Implemented feature surface

The source supports a fish-survival game loop with fish selection, food/coin pickups, movement and combat abilities, level and score progression, kill streaks, daily rewards, match results, and rankings. Detailed paths and evidence are in [gameplay systems](gameplay-systems.md), [player data](../../player-data/hungry-fish-2.0.md), [persistence](../../persistence/hungry-fish-2.0.md), and [leaderboards](../../leaderboards/hungry-fish-2.0.md).

## Provenance and boundaries

Primary extraction location: `D:\My project (6)\Craftland-Extraction\`. The full 15-document extraction remains there and was not modified. Selected index CSVs and the 14 source instruction files are copied into this repository for searchability and preservation. Paths such as `Assets/_Scripts/Player/PlayerAttack.fcg` refer to the read-only original project root `D:\My project (6)`, not a code copy in this repository.

The extraction reports 252 files inspected for content or structure. It explicitly says 2,588 baseline files have inventory coverage only, with targeted keyword scans for some text. No scripts were executed; no build, playtest, or runtime validation was performed. Consult [limitations](limitations-and-unknowns.md) before treating implementation descriptions as behavior.

## Primary source documents

- `D:\My project (6)\Craftland-Extraction\01_PROJECT_OVERVIEW.md`
- `D:\My project (6)\Craftland-Extraction\02_COMPLETE_FILE_INDEX.md`
- `D:\My project (6)\Craftland-Extraction\04_SCRIPT_DOCUMENTATION.md`
- `D:\My project (6)\Craftland-Extraction\05_CRAFTLAND_KNOWLEDGE.md`
- `D:\My project (6)\Craftland-Extraction\14_UNKNOWN_INFORMATION.md`
