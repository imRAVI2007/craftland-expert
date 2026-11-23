# Script relationships

## Data/config path

`GlobalConfig`, `MobConfig`, `MutationConfig`, and `RebirthConfig` read the project CSVs. `MobConfig` imports `MutationConfig`; `RebirthConfig` exposes progression values used by `RebirthManager`, `WalletManager`, `PlayerBase`, HUDs and base unlock logic. `BigNumberHandler` and `DataUtils` support numeric/data serialization.

## Player persistence path

`DatabaseController` provides registered database load/save orchestration and retries. `PlayersManager`, `PetsManager`, `WalletManager`, `RebirthManager`, and `LeaderboardManager` subscribe to database lifecycle events for their own state. A static state-map guard mismatch in `DatabaseController.SetDatabaseSaved` is recorded as unverified.

## Base and pet path

`GlobalBase` selects/assigns base groups; `PlayerBase` maps base entities, display slots, collect zone, spawn, and income. `MobHandler` coordinates model, description, rarity-ring helpers. Base, mob, collect, player, and parade triggers signal interaction/UI/manager modules. `PetsManager` persists/creates pets and manages balances; `PetMutex`, `PetStateController`, `PlayerStateController`, `ValidationController`, `ActionController`, and `StealManager` are connected in action/state flows.

## Parade and selection

`PetParadeManager` depends on mob/pet/config/wallet/player systems and `WeightedRandom`; `MobParadeHandler`/`MobParadeTrigger` hold per-pet parade interaction/movement details.

## UI path

`HudPetInteract`, `HudLaserWallInteract`, `HudRebirth`, `HudWallet`, menu, prompt, leaderboard and ranking controllers call managers/configs and utilities. `CustomUIUtils`, `UIUtils`, `UIUtilsClient`, and button helper graphs provide shared widget access/update behavior. Exact callbacks and bindings must be checked against the corresponding `.ui` tree/current editor.

## Two leaderboards

- Persistent: `LeaderboardManager` uses Data Storage `IncomeRank` / `WealthRank`; `HudLeaderboard` requests and shows the tabular result.
- Live match: `GlobalLeaderboard` periodically dispatches match rankings; `HudRanking` displays ranks/names/values.

## Evidence boundary

These relations summarize imports/event signatures and feature-flow reviews, not a complete execution graph or proven event ordering. See the per-script index and source.

## Sources

- `Craftland-Extraction/04_SCRIPT_DOCUMENTATION.md`
- `Craftland-Extraction/05_CRAFTLAND_KNOWLEDGE.md`
- `Craftland-Extraction/08_API_AND_INTEGRATIONS.md`
