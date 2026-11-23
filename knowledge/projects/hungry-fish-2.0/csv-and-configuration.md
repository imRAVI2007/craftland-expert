# Hungry Fish 2.0 CSV and configuration

## CSV files found in the baseline inventory

| Original path | Extracted role | Evidence boundary |
|---|---|---|
| `Assets/Config/fish_config.csv` | Fish/player configuration read by `Config/FishConfigReader.fcg`. | The narrative says the reader maps the selected fish ID to a row and casts values to `List<int>`; column semantics must be checked in source before editing. |
| `Assets/Localization/key.csv` | Localization keys and translations. | Inventory confirms file path/size. The extraction does not report a full translation-quality or row-by-row semantic audit. |

`ProjectSettings/Workflow.wfl`, `WorkflowMod.asset`, `GlobalMod.asset`, `PlayerSetting.asset`, and other settings are separate editor/configuration sources, not CSV tables. Project-setting serialized coverage is incomplete.

## Code-defined configuration described in the extraction

The extraction documents `DailyRewardConfig` values 50, 75, 100, 125, 150, 200, 300; `FishPriceConfig` for `F_01`…`F_26`; `EffectPriceConfig` for `E001`…`E009`; `FishClass` mappings; `FoodConfig` with 12 food prefab IDs; and `KillStreakConfig`. These are reported as FC source declarations/records, not rows in the two CSV files above. Consult the exact `.fcg` and generated-symbol source paths before changing any mapping.

## Maintenance guidance

Keep fish table columns aligned with `FishConfigReader` and the controller values it sets. Preserve source spelling and exact IDs. Validate selected fish IDs, list lengths, resource registrations, and UI bindings against the current project. This extraction did not compile or run the project after any change.

**Sources:** `D:\My project (6)\Craftland-Extraction\02_COMPLETE_FILE_INDEX.md`, `04_SCRIPT_DOCUMENTATION.md`, `05_CRAFTLAND_KNOWLEDGE.md`; inventory copy at [FILE_INVENTORY.csv](../../../sources/hungry-fish-2.0/indexes/FILE_INVENTORY.csv); script index at [SCRIPT_INDEX.csv](../../../sources/hungry-fish-2.0/indexes/SCRIPT_INDEX.csv).
