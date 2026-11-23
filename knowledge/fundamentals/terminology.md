# Terminology

| Term | Meaning in this extracted project | Evidence / caveat |
|---|---|---|
| Craftland FC | Source language/files in `.fcg`; generated symbol/header files use `.fcc`. | Project instructions and `04_SCRIPT_DOCUMENTATION.md`; generated `Temp/UGCLanguage/editorGen/` files are read-only. |
| `Mob` / pet | Project code, CSV, and component terminology uses `Mob`; player-facing tutorials often call these pets. | Preserve exact source name in code-facing references. |
| mutation | Configured values include Normal, Golden, Frozen, Magma in the current mutation table; mutation content spans config, enum, material/effect, prefab/component and HUD presentation. | Tutorials document authoring workflow; current table and source are separately inspected. |
| rebirth | Progression represented in `rebirth.csv`, `RebirthConfig.fcg` and `RebirthManager.fcg`. | Runtime progression was not tested. |
| Base | Player-associated build/display/collect/lock structure; `Base` custom component properties are recorded in project knowledge. | See prefab and component reference. |
| ECA | Editor-owned event graph. One read-only built-in `Spawn Point Auto Closer` graph was inspected. | Do not generalize from the single graph. |
| CSV row index | `CSVData` reader and enum code use numeric row/column indexing. | Mismatch between `MutationConfigEnum.Tier=7` and the six-column CSV is recorded as a static concern. |
| local leaderboard | `GlobalLeaderboard.fcg` sends a live match ranking; `LeaderboardManager.fcg` uses persistent Data Storage rank calls. | They are distinct systems. Neither implies an external website. |
| `aiPrompt` | Editor entity field that was searched in scene/prefabs/UIs; no populated values found. | Does not mean Craftland always lacks prompts elsewhere. |

Project naming inconsistency: tutorials call the template “Steal A Pet Template”; localization calls the game “Steal A Shape.” Explanation unknown.

## Sources

- `Craftland-Extraction/03_PROMPT_LIBRARY.md`
- `Craftland-Extraction/04_SCRIPT_DOCUMENTATION.md`
- `Craftland-Extraction/05_CRAFTLAND_KNOWLEDGE.md`
- `Craftland-Extraction/08_API_AND_INTEGRATIONS.md`
