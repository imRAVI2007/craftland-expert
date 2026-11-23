# Hungry Fish 2.0 player data

Distinguish **PlayerData asset definitions** from **persistent player records**:

- 27 local `.playerdata` assets under `Assets/PlayerData/` define `UGCPlayerEntity` archetypes. Craftland Studio reported gender value 0 and scale 1.5; most use fish prefab/action-map references. These definitions are not themselves evidence of stored per-user state.
- FC persistence is handled separately through Craftland DataStorage calls. See [persistence](../persistence/hungry-fish-2.0.md).

## Source-described player state

The project groups data by feature: wallet (`Wallet` / `Coin`), inventory (`Inventory` / `Fish`, `Effect`), login (`Login` / `LastTimestamp`, `Reward`, `LastLoginDay`), and score (`Score` / `Elimination`, `Score`). The exact key names are copied from source summaries; no account IDs, map codes tied to a user, or private values are included here.

`PlayerInventoryData.fcg` seeds a default unlocked fish/effect and locked slots. `PlayerScoreData.fcg` reads/writes lifetime elimination and score values. `PlayerLoginData` and `PlayerLogin` handle a seven-day reward state. Module references and caveats are in the [FC module notes](../scripting/hungry-fish-2.0-module-notes.md).

The extraction found the editor `playerdata` listing returned zero despite 27 files being present; individual files were then queried through the raw asset reader. That discrepancy remains unexplained. No DataStorage behavior was executed or validated.

**Sources:** `D:\My project (6)\Craftland-Extraction\04_SCRIPT_DOCUMENTATION.md`, `05_CRAFTLAND_KNOWLEDGE.md`, `14_UNKNOWN_INFORMATION.md`.
