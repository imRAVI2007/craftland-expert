# FC script overview

The extracted project contains 63 `.fcg` source files under `Assets/Scripts/`; there were no user `.fcc` sources listed. `Temp/UGCLanguage/editorGen/*.fcc` are generated symbol libraries and read-only. Full declaration-level source index: [fc-script-index.md](fc-script-index.md).

## Script categories

| Source folder | Count | Typical responsibility |
|---|---:|---|
| Root | 1 | Teleport effect |
| `_SharedLibs/CoreLib` | 2 | Action coordination, DB lifecycle |
| `_SharedLibs/PetLib` | 3 | Pet/player state and validation |
| `Base` (including `Collect`, `LaserWall`) | 7 | Base display, collect and lock triggers |
| `Configs` | 4 | Global, mob, mutation and rebirth config readers |
| `HUDs` | 11 | Player-facing HUD controllers |
| `Manager` | 9 | Base, leaderboard, parade, pet, player, rebirth, steal and wallet managers |
| `Mobs` | 8 | Mob/pet behavior and triggers |
| `Player` | 9 | Player base, movement, interaction, equipment, effects and teleport |
| `Utils` | 9 | Number/data/UI/hint/weighted-random helpers |
| **Total** | **63** | Matches extraction/editor catalog |

The exact names and original source-relative path are in the complete index. These counts were checked against the 63 script entries (63 source files, not the 13 extra `.fcg.meta` sidecars without source).

## Reading and editing guidance

The index records module graph, entry points, declarations/signatures, imports, observed calls and caveats as documented in the extraction. Do not treat an API name as proof of semantics. Consult current project source and generated symbols before coding. FC examples in archived instructions may be context-specific; verify current declarations. The extraction did not compile, run or test the scripts.

## Sources

- `Craftland-Extraction/04_SCRIPT_DOCUMENTATION.md`
- `Craftland-Extraction/02_COMPLETE_FILE_INDEX.md`
- `Craftland-Extraction/01_PROJECT_OVERVIEW.md`
