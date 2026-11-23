# Script Documentation and Search Index

FC source files inspected by reading their complete text: **63**. In addition, one read-only built-in ECA script was expanded through Craftland Studio MCP. No FC/ECA code was executed or compiled. Original project-relative FC source paths are provided as text; this index documents declarations, imports, entry points and naming-level behavior. It does not replace statement-by-statement review before making changes.

There are **13 additional `.fcg.meta` files** under `Assets/Scripts/` whose matching `.fcg` source files are absent. They are listed in [14_UNKNOWN_INFORMATION.md](../../Craftland-Extraction/14_UNKNOWN_INFORMATION.md). The editor asset catalog confirms 63 actual FC scripts. No HTML/CSS/JavaScript/TypeScript/Python/shell script files are present in the full inventory.

## Search by folder

> Original FC sources are not included in this repository. Paths shown as `Assets/...` refer to the old project tree. The extraction records that their complete text was inspected; this index is the available technical summary.

### `Assets/Scripts`

#### `Assets/Scripts/TeleportEffect.fcg`

- **Location / full source:** `Assets/Scripts/TeleportEffect.fcg`; `Assets/Scripts/TeleportEffect.fcg`; 236 bytes, 11 lines.
- **Purpose:** Implements `TeleportEffect` behavior; module context is `Assets/Scripts`.
- **Graph:** `TeleportEffect`.
- **Graph fields (direct source):** `TELEPORT_TIME: int = 3500`
- **Event signatures (direct source):** `event OnAwake()`
- **Working logic (declaration-level):** No function declaration parsed.
- **Functions, inputs and outputs (direct source signatures):** none
- **Dependencies:** `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`
- **Observed API/engine calls:** `WaitForMillisecond`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

## Verified feature-flow summaries from source review

### Configuration readers

- `Assets/Scripts/Configs/GlobalConfig.fcg`: static graph reads the third CSV data row using named column lookup at `OnAwake`; caches mob spawn interval, player move speed, steal speed and hit invulnerability time. Public getters visible in the source expose move and steal speed. The values have no unit labels in the CSV; call sites determine interpretation.
- `MobConfig.fcg`: reads `Mob.csv` starting at row index 2, builds ID-keyed maps for name, rarity, value, price, weight, mesh, material and sprite. Big-number fields are converted through `BigNumberHandler`. Exposes lookup/localization, rarity color, filtering, top-tier selection and mutation-adjusted value. `IsValidPetId` assumes positive IDs do not exceed row count.
- `MutationConfig.fcg`: reads mutation rows into maps; parses multiplier strings, exposes material/effect/value/weight/tier access, maps enum IDs to localization, and applies hard-coded display colors for Golden/Frozen/Magma. Static mismatch with current CSV Tier column is recorded in 09.
- `RebirthConfig.fcg`: reads rows into maps for lock duration, initial cash, multiplier, base level, pet quantity, next-level cash/pet requirements and money cap. Big-number strings become integer lists.

### Persistence and leaderboard

- `DatabaseController.fcg`: systems register database types. Player join dispatches `OnDatabaseLoad` on the server for each registered type; feature managers load their portion and mark it ready. Quit/match-end dispatches `OnDatabaseSave` for ready databases. `RetryLoadData` retries up to five times; timeout waits 1 second and data-store-limit waits 10 seconds. The saved-status initialization guard mismatch is documented in 09.
- `PlayersManager.fcg`: registers player DB; tracks current player entities and last-log timestamps; loads `PlayerSave/LAST_LOG_TIME` via a batch read, retries failures, computes elapsed offline time, marks ready, and writes the latest timestamp on save. Reconnect handling waits 5 seconds before restoring the current entity mapping.
- `LeaderboardManager.fcg`: reads persistent `IncomeRank` and `WealthRank` by ranks 1–120 using Craftland Data Storage leaderboard calls; persists each player's current income/wealth score on quit/match end. Income comes from base income; wealth comes from wallet balance. The configured map code is the empty string.
- `GlobalLeaderboard.fcg`: independently builds a live match ranking every 10 seconds while the phase is in progress. It sorts current players by wallet balance plus the configured mob **price** for each held pet, formats rank/name/value lines, and dispatches them to clients. This is distinct from the persistent leaderboard manager.

### Base/spawn and player lifecycle

- `GlobalBase.fcg`: obtains base groups under the registered `MainScene.BaseList` asset, stores each group's first child as a base, assigns the first available base to a player, and returns released bases on leave. Player proximity within 8 units can trigger another player's return-to-base request. `OnPlayerJoin` itself has the `SetBasePlayer` call commented out; the active source path to base assignment is `RebirthManager.LoadRebirthData` after player data loads.
- `PlayerBase.fcg`: binds the assigned base to the player, sets up the floor/name banner and display zones, teleports home, exposes the base's `Spawn`, pet display and collect-zone handles, and computes income from pet values × mutation multipliers × rebirth multiplier.
- `PlayerTeleport.fcg`: protects teleport events with immunity and existing-player checks. A requested return checks stealing/cooldown/teleport state, sets the teleporting state, waits 3,000 ms, sends the player to the base spawn with a 1-unit vertical offset, then applies a 3,000 ms cooldown. `TeleportToHome` uses the base spawn rotation rule.
- `PlayerEntity.fcg`: equips a baseball bat, disables item/fall-drop behavior, applies configured run speed, attaches a trigger, handles non-self bullet hits with configurable hit-fly values and temporary immunity, and revives after a 5,000 ms delay after elimination.

### Pet state/economy

- `PetsManager.fcg`: stores per-player pet IDs, mutations, accumulated balances, interactability, capacity and held/awaiting counts. It restores pet visuals after player/rebirth data is ready, saves pet fields to Craftland Data Storage, and creates pets from the registered Mob prefab. Pet balances update once per second; offline time is applied at one online second per five elapsed seconds and capped at 3,600 seconds of earnings. Collection transfers balance to wallet; selling a pet pays half the configured mob price. Cross-player stealing and other actions are coordinated by `StealManager`, `PetMutex`, `PetStateController`, and UI event handlers; inspect their linked source entries for branch details.

## Accuracy boundary

The summaries above were checked against the named source files. The per-file index for all 63 scripts gives exact declarations/imports and describes module behavior at the declaration level. A full line-by-line narrative of every branch in every script is not duplicated here; use the linked source as canonical. Unknown method behavior is not inferred solely from an API name.

### Additional central module summaries

- `StealManager.fcg`: server-side request flow validates player states, base/pet slot, existing pet interaction locks and rarity restrictions; it transfers the pet's ID/mutation/index state between owner and snatcher, toggles interactability, changes visuals, updates state controllers, and dispatches prompts. It also handles disconnect/teleport-related failure paths. Exact branches remain in source.
- `WalletManager.fcg`: stores and exposes per-player balances/multipliers and provides earn/spend/transfer operations. Large currency values use `List<int>` and `BigNumberHandler`; HUD updates and purchase checks are routed through manager functions.
- `RebirthManager.fcg`: persistent rebirth level is loaded from `PlayerSave`; request validation rejects pending pets, being-stolen state, stealing state, insufficient money, missing required pets and egg-related conditions. Successful rebirth resets money/pets, increments/clamps the level, reloads capacity/base/floor/lock time/name banner/multiplier and updates the player.
- `PetParadeManager.fcg`: coordinates parade pets and purchases/interaction with purchase queue/state; mob spawn timing references `GlobalConfig._MobSpawnInterval / 2`. The parade interacts with `MobHandler`, wallet, pets and prompt events.
- `HudLeaderboard.fcg`: initializes and switches leaderboard tabs, populates rank rows/current player details and requests leaderboard type data from `LeaderboardManager`. The corresponding UI includes global/region tabs, top-rank profile rows and a current-rank section.
- `HudPetInteract.fcg`: controls buy/sell/steal interaction UI and confirmation flows; signals are connected to pet, wallet, rebirth, state and teleport managers.
- `HudRebirth.fcg`: builds reward and requirement widgets from the rebirth configuration, checks max level and confirms/cancels the action.
- `HudLaserWallInteract.fcg`: presents unlock cost/confirmation and reports insufficient funds, cooldown, unlock success and owner notifications.
- `WeightedRandom.fcg`: weighted selection for mob IDs, mutation IDs and rarity-filtered mobs, with queue helpers. It contains four `DEBUG` comments; no execution was performed to determine whether any commented debugging code can be activated.

### Current source/config mismatch: mutation table

`MutationConfigEnum` from generated symbols has columns ID=0, Name=1, MaterialKey=2, EffectKey=3, Multiplier=4, Weight=5, FusionWeight=6 and Tier=7. Current `mutation.csv` has only six columns (`ID,Name,MaterialKey,EffectKey,Multiplier,Weight`). `MutationConfig.fcg` reads `FusionWeight` nowhere but reads `Tier` at index 7. The tier access is likely invalid for every current row; the current source's `MUTATIONS_NAME` and color mapping use enum IDs directly. This is static cross-file evidence, not runtime reproduction.

### Current script attachment anomaly

The `MobFollow.prefab` and `MobFollowing.prefab` assets each have a script reference ID `emjscp8lpru-mno4xs1s-ucomtm2qgx8`; it is not among the 63 project FCG IDs. `asset-list(fcg)` and the project source catalog do not map it to a local file. It may be a package-provided script; not confirmed missing at runtime.

### Read-only ECA script

`Spawn Point Auto Closer.eca` is a built-in, read-only package asset (`OwnerType=Entity`, `ComponentTypes=SpawnPos`, server platform). Its one top-level event is `OnPhaseEnd(Phase)`, followed by `SetActive(this_entity, false)`. This behavior comes from `eca-graph-get(depth=-1)`; the raw serialized `.eca` file was not hand-edited or copied.

### `Assets/Scripts/_SharedLibs/CoreLib`

#### `Assets/Scripts/_SharedLibs/CoreLib/ActionController.fcg`

- **Location / full source:** `Assets/Scripts/_SharedLibs/CoreLib/ActionController.fcg`; `Assets/Scripts/_SharedLibs/CoreLib/ActionController.fcg`; 1572 bytes, 54 lines.
- **Purpose:** Provides shared state/controller behavior for `ActionController`.
- **Graph:** `ActionController`.
- **Graph fields (direct source):** `PROCESS_ACTION_COOLDOWN: int = 1`; `_RegisteredActions: Map<string, bool> = Map<string, bool>{}`; `_LastActionTimestamp: Map<UUID, int> = Map<UUID, int>{}`
- **Event signatures (direct source):** none
- **Working logic (declaration-level):** Declared helper flow: RegisterAction, IsActionRegistered, RequestAction, IsProcressSoFast.
- **Functions, inputs and outputs (direct source signatures):** `func RegisterAction(actionType string)`; `func IsActionRegistered(actionType string) bool`; `func RequestAction(playerUID UUID, actionType string, payload Map<object, object>)`; `func IsProcressSoFast(playerUID UUID) bool`
- **Dependencies:** `import "Map.fcc" as Map`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "./DatabaseController.fcg" as DatabaseController`
- **Observed API/engine calls:** `DispatchEventToEntity`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/_SharedLibs/CoreLib/DatabaseController.fcg`

- **Location / full source:** `Assets/Scripts/_SharedLibs/CoreLib/DatabaseController.fcg`; `Assets/Scripts/_SharedLibs/CoreLib/DatabaseController.fcg`; 4702 bytes, 149 lines.
- **Purpose:** Provides shared state/controller behavior for `DatabaseController`.
- **Graph:** `DatabaseController`.
- **Graph fields (direct source):** `MAX_LOOP_READ_DATA (inferred) = 5`; `WAIT_TIME_DATA_STORAGE_TIMEOUT (inferred) = 1000`; `WAIT_TIME_DATA_STORAGE_LIMIT_EXCEEDED (inferred) = 10000`; `_RegisteredDBs: Map<string, bool> = Map<string, bool>{}`; `_DBReadyStatus: Map<UUID, Map<string, bool>> = Map<UUID, Map<string, bool>>{}`; `_DBSavedStatus: Map<UUID, Map<string, bool>> = Map<UUID, Map<string, bool>>{}`
- **Event signatures (direct source):** `event OnPlayerJoin(player entity<Player>)`; `event OnUserQuitOrUserMatchEnd(player entity<Player>)`
- **Working logic (declaration-level):** Declared helper flow: RegisterDatabase, LoadAllDatabases, RetryLoadData, SetDatabaseReady, IsDatabaseReady, SaveAllDatabases, SetDatabaseSaved, IsDatabaseSaved.
- **Functions, inputs and outputs (direct source signatures):** `func RegisterDatabase(dbType string)`; `func LoadAllDatabases(playerUID UUID)`; `async func RetryLoadData(sheetName string, playerUID UUID, key string, out var result object, mapCode string, out var statusCode StatusCode)`; `func SetDatabaseReady(playerUID UUID, dbType string, isReady bool)`; `func IsDatabaseReady(playerUID UUID, dbType string) bool`; `func AreAllDatabasesReady(playerUID UUID) bool`; `func SaveAllDatabases(playerUID UUID)`; `func SetDatabaseSaved(playerUID UUID, dbType string, isSaved bool)`; `func IsDatabaseSaved(playerUID UUID, dbType string) bool`; `func AreAllDatabasesSaved(playerUID UUID) bool`
- **Dependencies:** `import "Map.fcc" as Map`; `import "Player.fcc" as Player`; `import "Database.fcc" as Database`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`
- **Observed API/engine calls:** `DispatchEventToEntity`, `ReadFromDataStoreSteady`, `WaitForMillisecond`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

### `Assets/Scripts/_SharedLibs/PetLib`

#### `Assets/Scripts/_SharedLibs/PetLib/PetStateController.fcg`

- **Location / full source:** `Assets/Scripts/_SharedLibs/PetLib/PetStateController.fcg`; `Assets/Scripts/_SharedLibs/PetLib/PetStateController.fcg`; 3295 bytes, 123 lines.
- **Purpose:** Provides shared state/controller behavior for `PetStateController`.
- **Graph:** `PetStateController`.
- **Graph fields (direct source):** `_ParadePetState: Map<int, PetState>`; `_BasePetState: Map<UUID, Map<int, PetState>>`
- **Event signatures (direct source):** `event OnAwake()`; `event OnPlayerJoin(player entity<Player>)`
- **Working logic (declaration-level):** Declared helper flow: InitPetStateController, InitPetState, GetPetState, UpdatePetState, CanUpdateState, GetParadePetState, UpdateParadePetState, CanUpdateParadeState.
- **Functions, inputs and outputs (direct source signatures):** `func InitPetStateController()`; `func InitPetState(playerUID UUID)`; `func GetPetState(playerUID UUID, petSlot int) PetState`; `func UpdatePetState(playerUID UUID, petSlot int, newState PetState)`; `func CanUpdateState(playerUID UUID, petSlot int, newState PetState) bool`; `func GetParadePetState(petIndex int) PetState`; `func UpdateParadePetState(petIndex int, newState PetState)`; `func CanUpdateParadeState(petIndex int, newState PetState) bool`
- **Dependencies:** `import "Map.fcc" as Map`; `import "Player.fcc" as Player`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/_SharedLibs/PetLib/PlayerStateController.fcg`

- **Location / full source:** `Assets/Scripts/_SharedLibs/PetLib/PlayerStateController.fcg`; `Assets/Scripts/_SharedLibs/PetLib/PlayerStateController.fcg`; 1892 bytes, 71 lines.
- **Purpose:** Provides shared state/controller behavior for `PlayerStateController`.
- **Graph:** `PlayerStateController`.
- **Graph fields (direct source):** `RESET_STATE_DURATION: Map<PlayerState, int> = Map<PlayerState, int>{`; `_PlayerState: Map<UUID, PlayerState>`
- **Event signatures (direct source):** `event OnAwake()`
- **Working logic (declaration-level):** Declared helper flow: InitPlayerStateController, InitPlayerState, GetPlayerState, UpdatePlayerState, CanUpdateState.
- **Functions, inputs and outputs (direct source signatures):** `func InitPlayerStateController()`; `func InitPlayerState(playerUID UUID)`; `func GetPlayerState(playerUID UUID) PlayerState`; `async func UpdatePlayerState(playerUID UUID, newState PlayerState)`; `func CanUpdateState(playerUID UUID, newState PlayerState) bool`
- **Dependencies:** `import "Map.fcc" as Map`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`
- **Observed API/engine calls:** `WaitForMillisecond`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/_SharedLibs/PetLib/ValidationController.fcg`

- **Location / full source:** `Assets/Scripts/_SharedLibs/PetLib/ValidationController.fcg`; `Assets/Scripts/_SharedLibs/PetLib/ValidationController.fcg`; 2810 bytes, 70 lines.
- **Purpose:** Provides shared state/controller behavior for `ValidationController`.
- **Graph:** `ValidationController`.
- **Graph fields (direct source):** none
- **Event signatures (direct source):** `event OnRequestAction(playerUID UUID, actionType string, payload Map<object, object>)`
- **Working logic (declaration-level):** Declared helper flow: .
- **Functions, inputs and outputs (direct source signatures):** `func ValidateRequestAction(playerUID UUID, actionType string, payload Map<object, object>, out var statusCode int)`; `func ValidatePlayerState(playerUID UUID, actionType string, out var statusCode CustomStatusCode)`; `func ValidatePetState(ownerUID UUID, petSlot int, actionType string, out var statusCode CustomStatusCode)`
- **Dependencies:** `import "Map.fcc" as Map`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "./PetStateController.fcg" as PetStateController`; `import "./PlayerStateController.fcg" as PlayerStateController`
- **Observed API/engine calls:** `DispatchEventToEntity`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

### `Assets/Scripts/Base`

#### `Assets/Scripts/Base/Floor1Handler.fcg`

- **Location / full source:** `Assets/Scripts/Base/Floor1Handler.fcg`; `Assets/Scripts/Base/Floor1Handler.fcg`; 744 bytes, 34 lines.
- **Purpose:** Implements `Floor1Handler` behavior; module context is `Assets/Scripts/Base`.
- **Graph:** `Floor1Handler`.
- **Graph fields (direct source):** `_NameBanner: entity<Entity>`
- **Event signatures (direct source):** none
- **Working logic (declaration-level):** Declared helper flow: InitNameBanner, SetUpNameBanner, ClearNameBanner.
- **Functions, inputs and outputs (direct source signatures):** `func InitNameBanner()`; `func F1Setup()`; `func F1CleanUp()`; `func SetUpNameBanner(playerName string)`; `func ClearNameBanner()`
- **Dependencies:** `import "Math.fcc" as Math`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Base/MobDisplayHandler.fcg`

- **Location / full source:** `Assets/Scripts/Base/MobDisplayHandler.fcg`; `Assets/Scripts/Base/MobDisplayHandler.fcg`; 439 bytes, 16 lines.
- **Purpose:** Implements `MobDisplayHandler` behavior; module context is `Assets/Scripts/Base`.
- **Graph:** `MobDisplayHandler`.
- **Graph fields (direct source):** none
- **Event signatures (direct source):** none
- **Working logic (declaration-level):** Declared helper flow: EnableDisplay, DisableDisplay.
- **Functions, inputs and outputs (direct source signatures):** `func EnableDisplay()`; `func DisableDisplay()`
- **Dependencies:** `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

### `Assets/Scripts/Base/Collect`

#### `Assets/Scripts/Base/Collect/CollectZoneTrigger.fcg`

- **Location / full source:** `Assets/Scripts/Base/Collect/CollectZoneTrigger.fcg`; `Assets/Scripts/Base/Collect/CollectZoneTrigger.fcg`; 821 bytes, 21 lines.
- **Purpose:** Implements base/trigger behavior for `CollectZoneTrigger`.
- **Graph:** `CollectZoneTrigger`.
- **Graph fields (direct source):** none
- **Event signatures (direct source):** `event OnTriggerEnter(target entity<Entity>)`
- **Working logic (declaration-level):** No function declaration parsed.
- **Functions, inputs and outputs (direct source signatures):** none
- **Dependencies:** `import "Physics.fcc" as Physics`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../../Manager/StealManager.fcg" as StealManager`; `import "../../_SharedLibs/CoreLib/ActionController.fcg" as ActionController`; `import "../../_SharedLibs/PetLib/PlayerStateController.fcg" as PlayerStateController`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

### `Assets/Scripts/Base/LaserWall`

#### `Assets/Scripts/Base/LaserWall/KickTrigger.fcg`

- **Location / full source:** `Assets/Scripts/Base/LaserWall/KickTrigger.fcg`; `Assets/Scripts/Base/LaserWall/KickTrigger.fcg`; 1641 bytes, 46 lines.
- **Purpose:** Implements base/trigger behavior for `KickTrigger`.
- **Graph:** `KickTrigger`.
- **Graph fields (direct source):** `_PlayerList: List<entity<Player>> = List<entity<Player>>{}`; `_KickDirectionBlock: entity<Entity>`; `_KickDirection: Vector3`
- **Event signatures (direct source):** `event OnAwake()`; `event OnTriggerEnter(target entity<Entity>)`; `event OnTriggerLeave(target entity<Entity>)`
- **Working logic (declaration-level):** No function declaration parsed.
- **Functions, inputs and outputs (direct source signatures):** none
- **Dependencies:** `import "List.fcc" as List`; `import "Player.fcc" as Player`; `import "Physics.fcc" as Physics`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "./LaserWallHandler.fcg" as LaserWallHandler`; `import "../../Player/PlayerEntity.fcg" as PlayerEntity`
- **Observed API/engine calls:** `WaitForNextFrame`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Base/LaserWall/LaserWallHandler.fcg`

- **Location / full source:** `Assets/Scripts/Base/LaserWall/LaserWallHandler.fcg`; `Assets/Scripts/Base/LaserWall/LaserWallHandler.fcg`; 4753 bytes, 148 lines.
- **Purpose:** Implements base/trigger behavior for `LaserWallHandler`.
- **Graph:** `LaserWallHandler`.
- **Graph fields (direct source):** `UNLOCK_PRICE_MULTIPLIER: float = 3`; `_IsLaserWallOn: bool`; `_OnKey: int`
- **Event signatures (direct source):** `event OnPlayerJoin(player entity<Player>)`
- **Working logic (declaration-level):** Declared helper flow: IsLaserWallOn, TurnOnLaserWallTimeLevel, TurnOnLaserWall, TurnOffLaserWall, UpdateSwitchText, CheckCorrectOwner, GetOwner, GetUnlockPrice, GetUnlockPricePetCoins.
- **Functions, inputs and outputs (direct source signatures):** `func IsLaserWallOn() bool`; `func TurnOnLaserWallTimeLevel()`; `async func TurnOnLaserWall(time int)`; `func TurnOffLaserWall()`; `func UpdateSwitchText(content StringOrLocString)`; `func CheckCorrectOwner(player entity<Player>) bool`; `func GetOwner() entity<Player>`; `func GetUnlockPrice() List<int>`; `func GetUnlockPricePetCoins() List<int>`
- **Dependencies:** `import "List.fcc" as List`; `import "Math.fcc" as Math`; `import "Items.fcc" as Items`; `import "Player.fcc" as Player`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "./UnlockBaseTrigger.fcg" as UnlockBaseTrigger`; `import "../../Configs/MobConfig.fcg" as MobConfig`; `import "../../Player/PlayerBase.fcg" as PlayerBase`; `import "../../Manager/PetsManager.fcg" as PetsManager`; `import "../../Player/PlayerEntity.fcg" as PlayerEntity`; `import "../../Manager/RebirthManager.fcg" as RebirthManager`; `import "../../Utils/BigNumberHandler.fcg" as BigNumberHandler`
- **Observed API/engine calls:** `DispatchEventToEntity`, `GetAllPlayers`, `WaitForMillisecond`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Base/LaserWall/LaserWallSwitchTrigger.fcg`

- **Location / full source:** `Assets/Scripts/Base/LaserWall/LaserWallSwitchTrigger.fcg`; `Assets/Scripts/Base/LaserWall/LaserWallSwitchTrigger.fcg`; 744 bytes, 20 lines.
- **Purpose:** Implements base/trigger behavior for `LaserWallSwitchTrigger`.
- **Graph:** `LaserWallSwitchTrigger`.
- **Graph fields (direct source):** none
- **Event signatures (direct source):** `event OnTriggerEnter(target entity<Entity>)`
- **Working logic (declaration-level):** No function declaration parsed.
- **Functions, inputs and outputs (direct source signatures):** none
- **Dependencies:** `import "Physics.fcc" as Physics`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "./LaserWallHandler.fcg" as LaserWallHandler`
- **Observed API/engine calls:** `DispatchEventToEntity`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Base/LaserWall/UnlockBaseTrigger.fcg`

- **Location / full source:** `Assets/Scripts/Base/LaserWall/UnlockBaseTrigger.fcg`; `Assets/Scripts/Base/LaserWall/UnlockBaseTrigger.fcg`; 877 bytes, 24 lines.
- **Purpose:** Implements base/trigger behavior for `UnlockBaseTrigger`.
- **Graph:** `UnlockBaseTrigger`.
- **Graph fields (direct source):** `_PlayerList: List<entity<Player>> = List<entity<Player>>{}`
- **Event signatures (direct source):** `event OnTriggerEnter(target entity<Entity>)`; `event OnTriggerLeave(target entity<Entity>)`
- **Working logic (declaration-level):** No function declaration parsed.
- **Functions, inputs and outputs (direct source signatures):** none
- **Dependencies:** `import "List.fcc" as List`; `import "Physics.fcc" as Physics`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "./LaserWallHandler.fcg" as LaserWallHandler`; `import "../../Player/PlayerInteract.fcg" as PlayerInteract`
- **Observed API/engine calls:** `DispatchEventToEntity`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

### `Assets/Scripts/Configs`

#### `Assets/Scripts/Configs/GlobalConfig.fcg`

- **Location / full source:** `Assets/Scripts/Configs/GlobalConfig.fcg`; `Assets/Scripts/Configs/GlobalConfig.fcg`; 1219 bytes, 39 lines.
- **Purpose:** Loads and exposes game balance/content configuration for `GlobalConfig`.
- **Graph:** `GlobalConfig`.
- **Graph fields (direct source):** `VALUE_ROW: int = 3`; `_MobSpawnInterval: int`; `_PlayerMoveSpeed: float`; `_PlayerStealSpeed: float`; `_PlayerHitInvulnerableTime: int`
- **Event signatures (direct source):** `event OnAwake()`
- **Working logic (declaration-level):** Declared helper flow: GetDefaultConfig, GetPlayerMoveSpeed, GetStealSpeed.
- **Functions, inputs and outputs (direct source signatures):** `func GetDefaultConfig()`; `func GetPlayerMoveSpeed() float`; `func GetStealSpeed() float`
- **Dependencies:** `import "Map.fcc" as Map`; `import "List.fcc" as List`; `import "Convert.fcc" as Convert`; `import "CSVData.fcc" as CSVData`; `import "Strings.fcc" as Strings`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Utils/DataUtils.fcg" as DataUtils`; `import "../Utils/BigNumberHandler.fcg" as BigNumberHandler`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Configs/MobConfig.fcg`

- **Location / full source:** `Assets/Scripts/Configs/MobConfig.fcg`; `Assets/Scripts/Configs/MobConfig.fcg`; 9073 bytes, 270 lines.
- **Purpose:** Loads and exposes game balance/content configuration for `MobConfig`.
- **Graph:** `MobConfig`.
- **Graph fields (direct source):** `RARITY_INDEX: Map<RarityEnum, int> = Map<RarityEnum, int>{`; `RARITIES_NAME: Map<RarityEnum, StringOrLocString> = Map<RarityEnum, StringOrLocString>{`; `RARITY_COLOR: Map<RarityEnum, Color> = Map<RarityEnum, Color>{`; `_MobCount: int`; `_MobId2Name: Map<int, string>`; `_MobId2Rarity: Map<int, string>`; `_MobId2Value: Map<int, List<int>>`; `_MobId2Price: Map<int, List<int>>`; `_MobId2Weight: Map<int, float>`; `_MobId2Mesh: Map<int, string>`; `_MobId2Material: Map<int, string>`; `_MobId2Sprite: Map<int, string>`
- **Event signatures (direct source):** `event OnAwake()`
- **Working logic (declaration-level):** Declared helper flow: GetMobConfigFromCSV, SortPetIdsByRank, GetMobCount, GetMobCountByRarity, GetMobId2Name, GetMobName, GetMobNameLocalization, GetMobNameLocalizationColor, GetMobRarityIndex, GetMobRarity, GetMobRarityLocalization, GetMobValue, GetMobPrice, GetMobWeight, GetMobMeshKey, GetMobMaterialKey, GetMobThumbnailKey, IsValidPetId, GetMobsByRarity, GetTopTierPetsOnRoad, GetMobValueWithMutation, GetRarityCount, GetRarities, GetRarityIndex, GetRarityByIndex, GetRarityColor, GetRarityLocalization, GetRarityLocalizationColor.
- **Functions, inputs and outputs (direct source signatures):** `func GetMobConfigFromCSV()`; `func SortPetIdsByRank(originList List<int>, ranks List<int>) List<int>`; `func GetMobCount() int`; `func GetMobCountByRarity(rarity string) int`; `func GetMobId2Name() Map<int, string>`; `func GetMobName(mobId int) string`; `func GetMobNameLocalization(mobId int) StringOrLocString`; `func GetMobNameLocalizationColor(mobId int) StringOrLocString`; `func GetMobRarityIndex(mobId int) int`; `func GetMobRarity(mobId int) RarityEnum`; `func GetMobRarityLocalization(mobId int) StringOrLocString`; `func GetMobValue(mobId int) List<int>`; `func GetMobPrice(mobId int) List<int>`; `func GetMobWeight(mobId int) float`; `func GetMobMeshKey(mobId int) string`; `func GetMobMaterialKey(mobId int) string`; `func GetMobThumbnailKey(mobId int) string`; `func IsValidPetId(petId int) bool`; `func GetMobsByRarity(rarity string) List<int>`; `func GetTopTierPetsOnRoad(rarity RarityEnum, topTier int) List<int>`; `func GetMobValueWithMutation(mobId int, mutationId int) List<int>`; `func GetRarityCount() int`; `func GetRarities() List<RarityEnum>`; `func GetRarityIndex(rarity RarityEnum) int`; `func GetRarityByIndex(rarityIndex int) RarityEnum`; `func GetRarityColor(rarity RarityEnum) Color`; `func GetRarityLocalization(rarity RarityEnum) StringOrLocString`; `func GetRarityLocalizationColor(rarity RarityEnum) StringOrLocString`
- **Dependencies:** `import "Map.fcc" as Map`; `import "List.fcc" as List`; `import "Convert.fcc" as Convert`; `import "CSVData.fcc" as CSVData`; `import "Strings.fcc" as Strings`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "./MutationConfig.fcg" as MutationConfig`; `import "../Utils/BigNumberHandler.fcg" as BigNumberHandler`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Configs/MutationConfig.fcg`

- **Location / full source:** `Assets/Scripts/Configs/MutationConfig.fcg`; `Assets/Scripts/Configs/MutationConfig.fcg`; 4465 bytes, 125 lines.
- **Purpose:** Loads and exposes game balance/content configuration for `MutationConfig`.
- **Graph:** `MutationConfig`.
- **Graph fields (direct source):** `MUTATIONS_NAME: Map<MutationEnum, StringOrLocString> = Map<MutationEnum, StringOrLocString>{`; `_MutationCount: int`; `_MutationId2Name: Map<int, string>`; `_MutationId2MaterialKey: Map<int, string>`; `_MutationId2EffectKey: Map<int, string>`; `_MutationId2Multiplier: Map<int, float>`; `_MutationId2Weight: Map<int, float>`; `_MutationId2Tier: Map<int, int>`
- **Event signatures (direct source):** `event OnAwake()`
- **Working logic (declaration-level):** Declared helper flow: GetMutationConfigFromCSV, GetMutationCount, GetMutationId2Name, GetMutationName, GetMutationNameLocalization, GetMutationNameLocalizationColor, GetMutationMaterialKey, GetMutationEffectKey, GetMutationMultiplier, GetMutationWeight, GetMutationTier, GetMutationIconKey, IsAvailableMutation.
- **Functions, inputs and outputs (direct source signatures):** `func GetMutationConfigFromCSV()`; `func GetMutationCount() int`; `func GetMutationId2Name() Map<int, string>`; `func GetMutationName(mutationId int) string`; `func GetMutationNameLocalization(mutationId int) StringOrLocString`; `func GetMutationNameLocalizationColor(mutationId int) StringOrLocString`; `func GetMutationMaterialKey(mobId int, mutationId int) string`; `func GetMutationEffectKey(mutationId int) string`; `func GetMutationMultiplier(mutationId int) float`; `func GetMutationWeight(mutationId int) float`; `func GetMutationTier(mutationId int) int`; `func GetMutationIconKey(mutationId int) string`; `func IsAvailableMutation(mutationId int) bool`
- **Dependencies:** `import "Map.fcc" as Map`; `import "List.fcc" as List`; `import "Convert.fcc" as Convert`; `import "CSVData.fcc" as CSVData`; `import "Strings.fcc" as Strings`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "./MobConfig.fcg" as MobConfig`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Configs/RebirthConfig.fcg`

- **Location / full source:** `Assets/Scripts/Configs/RebirthConfig.fcg`; `Assets/Scripts/Configs/RebirthConfig.fcg`; 3844 bytes, 101 lines.
- **Purpose:** Loads and exposes game balance/content configuration for `RebirthConfig`.
- **Graph:** `RebirthConfig`.
- **Graph fields (direct source):** `_RebirthCount: int`; `_RebirthId2BaseLockTime: Map<int, int>`; `_RebirthId2StartingMoney: Map<int, List<int>>`; `_RebirthId2MoneyMultiplier: Map<int, float>`; `_RebirthId2BaseLevel: Map<int, int>`; `_RebirthId2MobAmount: Map<int, int>`; `_RebirthId2NextLevelMoney: Map<int, List<int>>`; `_RebirthId2NextLevelMob: Map<int, List<int>>`; `_RebirthId2MaxMoney: Map<int, List<int>>`
- **Event signatures (direct source):** `event OnAwake()`
- **Working logic (declaration-level):** Declared helper flow: GetRebirthConfigFromCSV, GetRebirthCount, GetRebirthBaseLockTime, GetRebirthStartingMoney, GetRebirthMoneyMultiplier, GetRebirthBaseLevel, GetRebirthMobAmount, GetRebirthNextLevelMoney, GetRebirthNextLevelMob, GetRebirthMaxMoneyRank, GetRebirthMaxMoney.
- **Functions, inputs and outputs (direct source signatures):** `func GetRebirthConfigFromCSV()`; `func GetRebirthCount() int`; `func GetRebirthBaseLockTime(rebirthId int) int`; `func GetRebirthStartingMoney(rebirthId int) List<int>`; `func GetRebirthMoneyMultiplier(rebirthId int) float`; `func GetRebirthBaseLevel(rebirthId int) int`; `func GetRebirthMobAmount(rebirthId int) int`; `func GetRebirthNextLevelMoney(rebirthId int) List<int>`; `func GetRebirthNextLevelMob(rebirthId int) List<int>`; `func GetRebirthMaxMoneyRank(rebirthId int) List<int>`; `func GetRebirthMaxMoney(rebirthId int) List<int>`
- **Dependencies:** `import "Map.fcc" as Map`; `import "List.fcc" as List`; `import "Convert.fcc" as Convert`; `import "CSVData.fcc" as CSVData`; `import "Strings.fcc" as Strings`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Utils/DataUtils.fcg" as DataUtils`; `import "../Utils/BigNumberHandler.fcg" as BigNumberHandler`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

### `Assets/Scripts/HUDs`

#### `Assets/Scripts/HUDs/HudControls.fcg`

- **Location / full source:** `Assets/Scripts/HUDs/HudControls.fcg`; `Assets/Scripts/HUDs/HudControls.fcg`; 1891 bytes, 63 lines.
- **Purpose:** Controls player-facing HUD state and interaction presentation for `HudControls`.
- **Graph:** `HudControls`.
- **Graph fields (direct source):** `PLAYER_UI_SWITCH_TYPE_COUNT (inferred) = 32`; `DEFAULT_UI_ON (inferred) = List<PlayerUISwitchType>{`
- **Event signatures (direct source):** `event OnAwake()`; `event OnStealPet(snatcher entity<Player>, owner entity<Player>, petSlot int)`; `event OnStolenSuccess(snatcher entity<Player>, owner entity<Player>, petSlot int)`; `event OnStolenFail(snatcher entity<Player>, owner entity<Player>, petSlot int)`
- **Working logic (declaration-level):** Declared helper flow: TurnOffDefaultUI, TurnOnNeedUI, DisableAttack, EnableAttack.
- **Functions, inputs and outputs (direct source signatures):** `func TurnOffDefaultUI()`; `func TurnOnNeedUI()`; `func DisableAttack()`; `func EnableAttack()`
- **Dependencies:** `import "Player.fcc" as Player`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/HUDs/HudDebug.fcg`

- **Location / full source:** `Assets/Scripts/HUDs/HudDebug.fcg`; `Assets/Scripts/HUDs/HudDebug.fcg`; 457 bytes, 22 lines.
- **Purpose:** Controls player-facing HUD state and interaction presentation for `HudDebug`.
- **Graph:** `HudDebug`.
- **Graph fields (direct source):** `_DebugHUD: entity<CustomUI>`
- **Event signatures (direct source):** `event OnAwake()`
- **Working logic (declaration-level):** Declared helper flow: InitDebugHUD.
- **Functions, inputs and outputs (direct source signatures):** `func InitDebugHUD()`
- **Dependencies:** `import "Hud.fcc" as Hud`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`
- **Observed API/engine calls:** `CreateCustomUI`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/HUDs/HudLaserWallInteract.fcg`

- **Location / full source:** `Assets/Scripts/HUDs/HudLaserWallInteract.fcg`; `Assets/Scripts/HUDs/HudLaserWallInteract.fcg`; 5700 bytes, 147 lines.
- **Purpose:** Controls player-facing HUD state and interaction presentation for `HudLaserWallInteract`.
- **Graph:** `HudLaserWallInteract`.
- **Graph fields (direct source):** `COOLDOWN_DURATION: int = 30`; `_CoolDownTime: Map<entity<Player>, int>`; `_LaserWallOwner: entity<Player>`; `_CurrentLaserWall: entity<Entity>`; `_LaserWallInteractHUD: entity<CustomUI>`; `_UnlockButton: entity<UIWidgetButton>`; `_ConfirmWidget: entity<UIWidget>`; `_DetailsLabel: entity<UIWidgetLabel>`; `_MoneyAmountLabel: entity<UIWidgetLabel>`
- **Event signatures (direct source):** `event OnAwake()`; `event OnNearLaserWall(player entity<Player>, laserWall entity<Entity>)`; `event OnFarLaserWall(player entity<Player>)`; `event OnLaserWallOn(owner entity<Player>, player entity<Player>, laserWall entity<Entity>)`; `event OnLaserWallOff(owner entity<Player>, laserWall entity<Entity>)`
- **Working logic (declaration-level):** Declared helper flow: InitLaserWallInteractHUD, ShowLaserWallInteractHUD, HideLaserWallInteractHUD, ShowConfirmWidget, HideConfirmWidget, UpdateDetails, ConfirmUnlock, CancelUnlock.
- **Functions, inputs and outputs (direct source signatures):** `func InitLaserWallInteractHUD()`; `func ShowLaserWallInteractHUD()`; `func HideLaserWallInteractHUD()`; `func ShowConfirmWidget()`; `func HideConfirmWidget()`; `func UpdateDetails()`; `func ConfirmUnlock()`; `func CancelUnlock()`; `async func CoolDownUnlockBase(player entity<Player>)`
- **Dependencies:** `import "Hud.fcc" as Hud`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import Res from "EditorGenLib.fcc"`; `import "../Manager/WalletManager.fcg" as WalletManager`; `import "../Base/LaserWall/LaserWallHandler.fcg" as LaserWallHandler`; `import "../Utils/UIUtils.fcg" as UIUtils`; `import "../Utils/BigNumberHandler.fcg" as BigNumberHandler`
- **Observed API/engine calls:** `CreateCustomUI`, `DispatchEventToEntity`, `WaitForMillisecond`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/HUDs/HudLeaderboard.fcg`

- **Location / full source:** `Assets/Scripts/HUDs/HudLeaderboard.fcg`; `Assets/Scripts/HUDs/HudLeaderboard.fcg`; 8255 bytes, 196 lines.
- **Purpose:** Controls player-facing HUD state and interaction presentation for `HudLeaderboard`.
- **Graph:** `HudLeaderboard`.
- **Graph fields (direct source):** `ACTIVE_TAB_TOP (inferred) = #216ABD`; `ACTIVE_TAB_BOTTOM (inferred) = #457FDF`; `ACTIVE_TEXT_COLOR (inferred) = #E5FAFE`; `DEFAULT_TAB_TOP (inferred) = #B9DCF2`; `DEFAULT_TAB_BOTTOM (inferred) = #B9DCF2`; `DEFAULT_TEXT_COLOR (inferred) = #1F64C4`; `MONEY_SUFFIX: Map<int, string> = Map<int, string>{`; `_CurrentLeaderboardType: LeaderboardType`; `_LeaderboardHUD: entity<CustomUI>`; `_TabButtons: Map<LeaderboardType, entity<UIWidgetButton>>`; `_LoadingLabel: entity<UIWidgetLabel>`; `_DetailsWidget: entity<UIWidget>`; `_RankWidgets: List<entity<UIWidget>>`; `_PlayerRankWidget: entity<UIWidget>`
- **Event signatures (direct source):** `event OnAwake()`
- **Working logic (declaration-level):** Declared helper flow: InitLeaderboardHUD, ShowLeaderboardHUD, HideLeaderboardHUD, UpdateLeaderboardLayout, UpdateRankWidget, ConvertMoneyRankScore.
- **Functions, inputs and outputs (direct source signatures):** `func InitLeaderboardHUD()`; `func ShowLeaderboardHUD()`; `func HideLeaderboardHUD()`; `async func UpdateLeaderboardLayout(leaderboardType LeaderboardType)`; `func UpdateRankWidget(rankWidget entity<UIWidget>, rankDetails List<object>, isCurrentPlayer bool)`; `func ConvertMoneyRankScore(moneyRankScore int) string`; `func SwitchLeaderboardTab(leaderboardType LeaderboardType)`
- **Dependencies:** `import "Hud.fcc" as Hud`; `import "Map.fcc" as Map`; `import "List.fcc" as List`; `import "Convert.fcc" as Convert`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import Res from "EditorGenLib.fcc"`; `import "../Manager/LeaderboardManager.fcg" as LeaderboardManager`; `import "../Utils/UIUtils.fcg" as UIUtils`; `import "../Utils/BigNumberHandler.fcg" as BigNumberHandler`
- **Observed API/engine calls:** `CreateCustomUI`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/HUDs/HudMail.fcg`

- **Location / full source:** `Assets/Scripts/HUDs/HudMail.fcg`; `Assets/Scripts/HUDs/HudMail.fcg`; 867 bytes, 36 lines.
- **Purpose:** Controls player-facing HUD state and interaction presentation for `HudMail`.
- **Graph:** `HudMail`.
- **Graph fields (direct source):** `_MailHUD: entity<CustomUI>`; `_MailContent: entity<UIWidgetLabel>`
- **Event signatures (direct source):** none
- **Working logic (declaration-level):** Declared helper flow: InitMailHUD, ShowMailHUD, HideMailHUD.
- **Functions, inputs and outputs (direct source signatures):** `func InitMailHUD()`; `func ShowMailHUD()`; `func HideMailHUD()`
- **Dependencies:** `import "Hud.fcc" as Hud`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import Res from "EditorGenLib.fcc"`; `import "../Utils/UIUtils.fcg" as UIUtils`
- **Observed API/engine calls:** `CreateCustomUI`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/HUDs/HudMenu.fcg`

- **Location / full source:** `Assets/Scripts/HUDs/HudMenu.fcg`; `Assets/Scripts/HUDs/HudMenu.fcg`; 4762 bytes, 128 lines.
- **Purpose:** Controls player-facing HUD state and interaction presentation for `HudMenu`.
- **Graph:** `HudMenu`.
- **Graph fields (direct source):** `UPDATE_REBIRTH_ALERT_INTERVAL (inferred) = 3000`; `EXPAND_ICON_NO_FLIP (inferred) = 2`; `EXPAND_ICON_FLIP (inferred) = 1`; `_CanUpdateRebirthAlert: bool`; `_MenuHUD: entity<CustomUI>`; `_ExpandToolsWidget: entity<UIWidget>`; `_ExpandIcon: entity<UIWidgetImage>`; `_AlertMenuIcon: entity<UIWidgetImage>`; `_AlertNewsIcon: entity<UIWidgetImage>`; `_AlertRebirthIcon: entity<UIWidgetImage>`; `_AlertDecorationIcon: entity<UIWidgetImage>`; `_DecorationButton: entity<UIWidgetButton>`; `_RearrangePetsButton: entity<UIWidgetButton>`; `_GiftCodeButton: entity<UIWidgetButton>`
- **Event signatures (direct source):** `event OnAwake()`; `event OnNearPetInHouse(player entity<Player>, owner entity<Player>, petSlot int)`; `event OnOwnNewPet(player entity<Player>, petId int, mutationId int)`; `event OnLaserWallOn(owner entity<Player>, player entity<Player>, laserWall entity<Entity>)`; `event OnLaserWallOff(owner entity<Player>, laserWall entity<Entity>)`
- **Working logic (declaration-level):** Declared helper flow: InitMenuHUD, ShowMenuHUD, HideMenuHUD, ShowExtraTools, HideExtraTools, UpdateExtraTools, UpdateRebirthAlert, UpdateDecorationAlert.
- **Functions, inputs and outputs (direct source signatures):** `func InitMenuHUD()`; `func ShowMenuHUD()`; `func HideMenuHUD()`; `func ShowExtraTools()`; `func HideExtraTools()`; `func UpdateExtraTools()`; `async func UpdateRebirthAlert()`; `func UpdateDecorationAlert(iShow bool)`
- **Dependencies:** `import "Hud.fcc" as Hud`; `import "Map.fcc" as Map`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import Res from "EditorGenLib.fcc"`; `import "../Manager/PlayersManager.fcg" as PlayersManager`; `import "../Manager/RebirthManager.fcg" as RebirthManager`; `import "../Utils/UIUtils.fcg" as UIUtils`; `import "../_SharedLibs/CoreLib/DatabaseController.fcg" as DatabaseController`
- **Observed API/engine calls:** `CreateCustomUI`, `WaitForMillisecond`, `WaitForNextFrame`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/HUDs/HudPetInteract.fcg`

- **Location / full source:** `Assets/Scripts/HUDs/HudPetInteract.fcg`; `Assets/Scripts/HUDs/HudPetInteract.fcg`; 9337 bytes, 285 lines.
- **Purpose:** Controls player-facing HUD state and interaction presentation for `HudPetInteract`.
- **Graph:** `HudPetInteract`.
- **Graph fields (direct source):** `PET_COIN_TO_SKIP_HATCH: List<int> = List<int>{1}`; `PET_COIN_TO_HATCH_OTHER_EGG: List<int> = List<int>{10}`; `_CurrentPetSlot: int`; `_IsConfirmingSellPet: bool`; `_DisconnectedPlayers: List<entity<Player>>`; `_PetInteractHUD: entity<CustomUI>`; `_BuyButton: entity<UIWidgetButton>`; `_SellButton: entity<UIWidgetButton>`; `_StealButton: entity<UIWidgetButton>`; `_ConfirmWidget: entity<UIWidget>`; `_DetailsLabel: entity<UIWidgetLabel>`
- **Event signatures (direct source):** `event OnAwake()`; `event OnNearPetInHouse(player entity<Player>, owner entity<Player>, petSlot int)`; `event OnNearPetParade(player entity<Player>, pet entity<Entity>)`; `event OnFarPetInHouse(player entity<Player>)`; `event OnFarPetParade(player entity<Player>, pet entity<Entity>)`; `event OnStealPet(snatcher entity<Player>, owner entity<Player>, petSlot int)`; `event OnReconnect(player entity<Player>)`; `event OnDisconnect(player entity<Player>)`
- **Working logic (declaration-level):** Declared helper flow: InitPetInteractHUD, ShowPetInteractHUD, HidePetInteractHUD, ResetPetInteractHUD, ShowBuyButton, HideBuyButton, ShowSellButton, HideSellButton, ShowStealButton, HideStealButton, ShowConfirmWidget, HideConfirmWidget, HandleInteractPetInHouse, HandleInteractPetParade, HandleBuyPet, HandleSellPet, HandleStealPet, HandleConfirmSellPet, HandleCancelSellPet.
- **Functions, inputs and outputs (direct source signatures):** `func InitPetInteractHUD()`; `func ShowPetInteractHUD()`; `func HidePetInteractHUD()`; `func ResetPetInteractHUD()`; `func ShowBuyButton()`; `func HideBuyButton()`; `func ShowSellButton()`; `func HideSellButton()`; `func ShowStealButton()`; `func HideStealButton()`; `func ShowConfirmWidget()`; `func HideConfirmWidget()`; `func HandleInteractPetInHouse(owner entity<Player>, petSlot int)`; `func HandleInteractPetParade(pet entity<Entity>)`; `func HandleBuyPet()`; `func HandleSellPet()`; `func HandleStealPet()`; `func HandleConfirmSellPet()`; `func HandleCancelSellPet()`
- **Dependencies:** `import "Hud.fcc" as Hud`; `import "List.fcc" as List`; `import "Player.fcc" as Player`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import Res from "EditorGenLib.fcc"`; `import "../Configs/MobConfig.fcg" as MobConfig`; `import "../Manager/PetsManager.fcg" as PetsManager`; `import "../Manager/WalletManager.fcg" as WalletManager`; `import "../Manager/RebirthManager.fcg" as RebirthManager`; `import "../Player/PlayerBase.fcg" as PlayerBase`; `import "../Player/PlayerInteract.fcg" as PlayerInteract`; `import "../Player/PlayerTeleport.fcg" as PlayerTeleport`; `import "../Mobs/MobHandler.fcg" as MobHandler`; `import "../Utils/UIUtils.fcg" as UIUtils`; `import "../Utils/BigNumberHandler.fcg" as BigNumberHandler`; `import "../_SharedLibs/CoreLib/ActionController.fcg" as ActionController`; `import "../_SharedLibs/PetLib/PlayerStateController.fcg" as PlayerStateController`
- **Observed API/engine calls:** `CreateCustomUI`, `WaitForMillisecond`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/HUDs/HudPrompt.fcg`

- **Location / full source:** `Assets/Scripts/HUDs/HudPrompt.fcg`; `Assets/Scripts/HUDs/HudPrompt.fcg`; 6202 bytes, 158 lines.
- **Purpose:** Controls player-facing HUD state and interaction presentation for `HudPrompt`.
- **Graph:** `HudPrompt`.
- **Graph fields (direct source):** `PROMPT_DURATION (inferred) = 5000`; `PROMPT_PREVENT_SPAM_DURATION (inferred) = 15`; `PROMPTS: Map<string, StringOrLocString> = Map<string, StringOrLocString>{`; `PROMPTS_HAVE_PARAMS: List<string> = List<string>{`; `PROMPT_HAVE_DELAY_SPAM: List<string> = List<string>{`; `CONTINUOUS_PROMPTS: List<string> = List<string>{`; `_CurrentPrompt: string`; `_CurrentParams: List<object>`; `_CountPrompt: int`; `_LastPromptTime: int`; `_PromptHUD: entity<CustomUI>`; `_ContentLabel: entity<UIWidgetLabel>`
- **Event signatures (direct source):** `event OnAwake()`; `event OnShowPrompt(prompt string, params List<object>)`; `event OnPhaseStart(phase entity<Phase>)`
- **Working logic (declaration-level):** Declared helper flow: InitPromptHUD, ShowPromptHUD, HidePromptHUD, UpdatePromptHUD, UpdatePromptHasParams.
- **Functions, inputs and outputs (direct source signatures):** `func InitPromptHUD()`; `async func ShowPromptHUD()`; `func HidePromptHUD()`; `func UpdatePromptHUD()`; `func UpdatePromptHasParams()`
- **Dependencies:** `import "Hud.fcc" as Hud`; `import "Map.fcc" as Map`; `import "List.fcc" as List`; `import "Workflow.fcc" as Workflow`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import Res from "EditorGenLib.fcc"`; `import "../Utils/UIUtils.fcg" as UIUtils`
- **Observed API/engine calls:** `CreateCustomUI`, `WaitForMillisecond`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/HUDs/HudRanking.fcg`

- **Location / full source:** `Assets/Scripts/HUDs/HudRanking.fcg`; `Assets/Scripts/HUDs/HudRanking.fcg`; 1885 bytes, 55 lines.
- **Purpose:** Controls player-facing HUD state and interaction presentation for `HudRanking`.
- **Graph:** `HudRanking`.
- **Graph fields (direct source):** `_RankingHUD: entity<CustomUI>`; `_RankLabel: entity<UIWidgetLabel>`; `_NameLabel: entity<UIWidgetLabel>`; `_ValueLabel: entity<UIWidgetLabel>`
- **Event signatures (direct source):** `event OnUpdateRanking(ranks string, names string, values string)`
- **Working logic (declaration-level):** Declared helper flow: InitRankingHUD, ShowRankingHUD, HideRankingHUD, UpdateRankingHUD.
- **Functions, inputs and outputs (direct source signatures):** `func InitRankingHUD()`; `func ShowRankingHUD()`; `func HideRankingHUD()`; `func UpdateRankingHUD(ranks string, names string, values string)`
- **Dependencies:** `import "Hud.fcc" as Hud`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import Res from "EditorGenLib.fcc"`; `import "../Utils/UIUtilsClient.fcg" as UIUtilsClient`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/HUDs/HudRebirth.fcg`

- **Location / full source:** `Assets/Scripts/HUDs/HudRebirth.fcg`; `Assets/Scripts/HUDs/HudRebirth.fcg`; 13931 bytes, 322 lines.
- **Purpose:** Controls player-facing HUD state and interaction presentation for `HudRebirth`.
- **Graph:** `HudRebirth`.
- **Graph fields (direct source):** `LAYOUT_SIZE: int = 100`; `LAYOUT_DISTANCE: int = 25`; `REWARD_MAX_PRIORITY: int = 10`; `REWARD_ICON: Map<RebirthRewardType, EResSprite> = Map<RebirthRewardType, EResSprite>{`; `REWARD_LABEL: Map<RebirthRewardType, StringOrLocString> = Map<RebirthRewardType, StringOrLocString>{`; `_CurrentRebirthID: int`; `_RebirthHUD: entity<CustomUI>`; `_RebirthWidget: entity<UIWidget>`; `_ConfirmWidget: entity<UIWidget>`; `_RewardsLayout: entity<UIWidgetLayout>`; `_MultiLabel: entity<UIWidgetLabel>`; `_CashLabel: entity<UIWidgetLabel>`; `_LockTimeLabel: entity<UIWidgetLabel>`; `_SlotLabel: entity<UIWidgetLabel>`; `_ReqMoneyLabel: entity<UIWidgetLabel>`; `_ReqMoneyProgress: entity<UIWidgetImage>`; `_ReqPetsLayout: entity<UIWidgetLayout>`; `_WarningLabel: entity<UIWidgetLabel>`; `_RebirthButton: entity<UIWidgetButton>`; `_WarningPetsLayout: entity<UIWidgetLayout>`
- **Event signatures (direct source):** `event OnAwake()`
- **Working logic (declaration-level):** Declared helper flow: InitRebirthHUD, ShowRebirthHUD, HideRebirthHUD, IsShowing, ShowRebirthWidget, HideRebirthWidget, ShowConfirmWidget, HideConfirmWidget, UpdateRebirthDetails, UpdateRebirthRewards, ResetRewardsLayout, UpdateRewardWidget, UpdateRebirthRequirements, UpdateRequireMoney, UpdateRequirePetsLayout, UpdateRequirePetWidget, ResetRequirePetsLayout, CheckMaxLevel, ConfirmRebirth, CancelRebirth, IsOpenRebirthWidget.
- **Functions, inputs and outputs (direct source signatures):** `func InitRebirthHUD()`; `func ShowRebirthHUD()`; `func HideRebirthHUD()`; `func IsShowing() bool`; `func ShowRebirthWidget()`; `func HideRebirthWidget()`; `func ShowConfirmWidget()`; `func HideConfirmWidget()`; `func UpdateRebirthDetails()`; `func UpdateRebirthRewards()`; `func ResetRewardsLayout(rewardsCount int)`; `func UpdateRewardWidget(rewardWidget entity<UIWidget>, rewardType RebirthRewardType, rewardValue object)`; `func UpdateRebirthRequirements()`; `func UpdateRequireMoney()`; `func UpdateRequirePetsLayout()`; `func UpdateRequirePetWidget(petWidget entity<UIWidget>, petId int)`; `func ResetRequirePetsLayout()`; `func CheckMaxLevel()`; `func ConfirmRebirth()`; `func CancelRebirth()`; `func IsOpenRebirthWidget() bool`
- **Dependencies:** `import "Hud.fcc" as Hud`; `import "Map.fcc" as Map`; `import "List.fcc" as List`; `import "Strings.fcc" as Strings`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import Res from "EditorGenLib.fcc"`; `import "../Configs/RebirthConfig.fcg" as RebirthConfig`; `import "../Manager/PetsManager.fcg" as PetsManager`; `import "../Manager/WalletManager.fcg" as WalletManager`; `import "../Manager/RebirthManager.fcg" as RebirthManager`; `import "../Utils/UIUtils.fcg" as UIUtils`; `import "../Utils/BigNumberHandler.fcg" as BigNumberHandler`; `import "../_SharedLibs/CoreLib/ActionController.fcg" as ActionController`
- **Observed API/engine calls:** `CreateCustomUI`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/HUDs/HudWallet.fcg`

- **Location / full source:** `Assets/Scripts/HUDs/HudWallet.fcg`; `Assets/Scripts/HUDs/HudWallet.fcg`; 4729 bytes, 122 lines.
- **Purpose:** Controls player-facing HUD state and interaction presentation for `HudWallet`.
- **Graph:** `HudMoney`.
- **Graph fields (direct source):** `EXCHANGE_MONEY_DURATION: int = 3000`; `CURRENCY_ICON: Map<CurrencyType, EResSprite> = Map<CurrencyType, EResSprite>{`; `CURRENCY_EXCHANGE_POS: Map<CurrencyType, Vector3> = Map<CurrencyType, Vector3>{`; `_WalletHUD: entity<CustomUI>`; `_MoneyLabel: entity<UIWidgetLabel>`; `_PetCoinsLabel: entity<UIWidgetLabel>`; `_DustLabel: entity<UIWidgetLabel>`; `_GemstoneLabel: entity<UIWidgetLabel>`; `_PetCoinsBG: entity<UIWidget>`; `_DustBG: entity<UIWidget>`; `_GemstoneBG: entity<UIWidget>`; `_MoneyBG: entity<UIWidget>`; `_ExchangeWidget: entity<UIWidget>`; `_TransferButton: entity<UIWidgetButton>`
- **Event signatures (direct source):** `event OnWalletUpdate(currencyType int, exchangeAmount string, isIncrease bool)`
- **Working logic (declaration-level):** Declared helper flow: InitWalletHud, UpdateWalletHud.
- **Functions, inputs and outputs (direct source signatures):** `func InitWalletHud()`; `func UpdateWalletHud(currencyType CurrencyType, exchangeAmount string, isIncrease bool)`; `async func NotifyExchangeWallet(amount string, currencyType CurrencyType, isIncrease bool)`; `func ActiveNewCurrency(isActive bool)`
- **Dependencies:** `import "Hud.fcc" as Hud`; `import "List.fcc" as List`; `import "Playable.fcc" as Playable`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import Res from "EditorGenLib.fcc"`; `import "../Configs/RebirthConfig.fcg" as RebirthConfig`; `import "../Manager/WalletManager.fcg" as WalletManager`; `import "../Manager/RebirthManager.fcg" as RebirthManager`; `import "../Utils/UIUtils.fcg" as UIUtils`; `import "../Utils/BigNumberHandler.fcg" as BigNumberHandler`
- **Observed API/engine calls:** `CreateCustomUI`, `WaitForMillisecond`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

### `Assets/Scripts/Manager`

#### `Assets/Scripts/Manager/GlobalBase.fcg`

- **Location / full source:** `Assets/Scripts/Manager/GlobalBase.fcg`; `Assets/Scripts/Manager/GlobalBase.fcg`; 2849 bytes, 87 lines.
- **Purpose:** Coordinates shared game state and player-facing rules for `GlobalBase`.
- **Graph:** `GlobalBase`.
- **Graph fields (direct source):** `BASE_DISTANCE (inferred) = 8`; `_NumberPlayers: int`; `_BaseList: List<entity<Entity>>`; `_AvailableBaseList: List<entity<Entity>>`
- **Event signatures (direct source):** `event OnAwake()`; `event OnPlayerJoin(player entity<Player>)`; `event OnUserQuitOrUserMatchEnd(player entity<Player>)`
- **Working logic (declaration-level):** Declared helper flow: InitBaseList, SetBasePlayer.
- **Functions, inputs and outputs (direct source signatures):** `func InitBaseList()`; `func SetBasePlayer(player entity<Player>)`
- **Dependencies:** `import "List.fcc" as List`; `import "Math.fcc" as Math`; `import "Player.fcc" as Player`; `import "StdLibrary.fcc" as StdLib`; `import "LevelObject.fcc" as LevelObject`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Player/PlayerBase.fcg" as PlayerBase`; `import "../Player/PlayerTeleport.fcg" as PlayerTeleport`; `import "../Base/LaserWall/LaserWallHandler.fcg" as LaserWallHandler`
- **Observed API/engine calls:** `GetAllPlayers`, `WaitForMillisecond`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Manager/GlobalLeaderboard.fcg`

- **Location / full source:** `Assets/Scripts/Manager/GlobalLeaderboard.fcg`; `Assets/Scripts/Manager/GlobalLeaderboard.fcg`; 5016 bytes, 147 lines.
- **Purpose:** Coordinates shared game state and player-facing rules for `GlobalLeaderboard`.
- **Graph:** `RankingManager`.
- **Graph fields (direct source):** `UPDATE_RANKING_DURATION: int = 10000`; `_CurrentPlayerList: List<entity<Player>>`; `_MapRankPlayer: Map<int, entity<Player>>`; `_PlayerTotalValueMap: Map<entity<Player>, List<int>>`; `_PlayerStealCountMap: Map<entity<Player>, int>`
- **Event signatures (direct source):** `event OnAwake()`; `event OnPlayerJoin(player entity<Player>)`; `event OnUserQuitOrUserMatchEnd(player entity<Player>)`; `event OnPhaseStart(phase entity<Phase>)`
- **Working logic (declaration-level):** Declared helper flow: UpdateRanking, CalculateRanking, CalculateAllPlayersTotalValue, CalculatePlayerTotalValue, GetRanks, GetNames, GetValues.
- **Functions, inputs and outputs (direct source signatures):** `func UpdateRanking()`; `func CalculateRanking()`; `func CalculateAllPlayersTotalValue()`; `func CalculatePlayerTotalValue(player entity<Player>) List<int>`; `func GetRanks() string`; `func GetNames() string`; `func GetValues() string`
- **Dependencies:** `import "List.fcc" as List`; `import "Player.fcc" as Player`; `import "Workflow.fcc" as Workflow`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Configs/MobConfig.fcg" as MobConfig`; `import "../Manager/PetsManager.fcg" as PetsManager`; `import "../Manager/WalletManager.fcg" as WalletManager`; `import "../Utils/BigNumberHandler.fcg" as BigNumberHandler`
- **Observed API/engine calls:** `DispatchEventToEntity`, `WaitForMillisecond`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Manager/LeaderboardManager.fcg`

- **Location / full source:** `Assets/Scripts/Manager/LeaderboardManager.fcg`; `Assets/Scripts/Manager/LeaderboardManager.fcg`; 4589 bytes, 143 lines.
- **Purpose:** Coordinates shared game state and player-facing rules for `LeaderboardManager`.
- **Graph:** `LeaderboardManager`.
- **Graph fields (direct source):** `SHEETS_RANK: Map<LeaderboardType, string> = Map<LeaderboardType, string>{`; `MAP_CODE (inferred) = ""`; `START_RANK (inferred) = 1`; `END_RANK (inferred) = 120`; `_LeaderboardDetails: Map<LeaderboardType, List<List<object>>>`; `_LoadedLeaderboard: Map<LeaderboardType, bool>`
- **Event signatures (direct source):** `event OnAwake()`; `event OnUserQuitOrUserMatchEnd(player entity<Player>)`
- **Working logic (declaration-level):** Declared helper flow: InitLeaderboardManager, GetLeaderboardType, LoadLeaderboard, SaveLeaderboardDatabase, SavePlayerLeaderboard, GetPlayerRankScore, GetPlayerIncomeRank, GetPlayerWealthRank.
- **Functions, inputs and outputs (direct source signatures):** `func InitLeaderboardManager()`; `async func GetLeaderboardType(type LeaderboardType, out var leaderboardDetails List<List<object>>, player entity<Player>, out var playerRankDetails List<int>)`; `async func LoadLeaderboard(leaderboardType LeaderboardType, startRank int, endRank int)`; `func SaveLeaderboardDatabase(player entity<Player>)`; `async func SavePlayerLeaderboard(playerUID UUID, leaderboardType LeaderboardType, leaderboardScore int)`; `func GetPlayerRankScore(type LeaderboardType, player entity<Player>) int`; `func GetPlayerIncomeRank(player entity<Player>) int`; `func GetPlayerWealthRank(playerUID UUID) int`
- **Dependencies:** `import "Map.fcc" as Map`; `import "List.fcc" as List`; `import "Player.fcc" as Player`; `import "Convert.fcc" as Convert`; `import "Database.fcc" as Database`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Manager/WalletManager.fcg" as WalletManager`; `import "../Player/PlayerBase.fcg" as PlayerBase`; `import "../_SharedLibs/CoreLib/DatabaseController.fcg" as DatabaseController`
- **Observed API/engine calls:** `ReadFromLeaderboardByRank`, `WriteToLeaderboard`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Manager/PetParadeManager.fcg`

- **Location / full source:** `Assets/Scripts/Manager/PetParadeManager.fcg`; `Assets/Scripts/Manager/PetParadeManager.fcg`; 11570 bytes, 312 lines.
- **Purpose:** Coordinates shared game state and player-facing rules for `PetParadeManager`.
- **Graph:** `PetsParadeManager`.
- **Graph fields (direct source):** `PET_SPAWN_INTERVAL: int = 6000`; `_PetsParadePool: List<entity<Entity>>`; `_PetParadeIndex: int`; `_StartPos1: Vector3`; `_EndPos1: Vector3`; `_StartPos2: Vector3`; `_EndPos2: Vector3`; `_TweenCurveLinear: BezierCurve`
- **Event signatures (direct source):** `event OnAwake()`; `event OnPhaseStart(phase entity<Phase>)`; `event OnProcessAction(playerUID UUID, actionType string, payload Map<object, object>)`
- **Working logic (declaration-level):** Declared helper flow: InitPetsParadeManager, GetDistance, GetMoveDuration, GetRotationAngle, GetPetFromParadePool, CreateNewPetToParadePool, MovePetParade, CheckReturnPetToParadePool, RequestBuyPet, CheckConditionBuyPet.
- **Functions, inputs and outputs (direct source signatures):** `func InitPetsParadeManager()`; `func GetDistance(x1 float, z1 float, x2 float, z2 float) float`; `func GetMoveDuration(moveDistance float) int`; `func GetRotationAngle(x1 float, z1 float, x2 float, z2 float) Vector3`; `async func SpawnPetsParade()`; `func SpawnPetParade()`; `func GetPetFromParadePool() entity`; `func CreateNewPetToParadePool()`; `async func MovePetParade(petParade entity<Entity>, startPos Vector3, endPos Vector3)`; `async func DestroyPetParade(petParade entity<Entity>, duration int, tweenIndex int)`; `func ReturnPetToParadePool(petParade entity<Entity>)`; `func CheckReturnPetToParadePool(petIndex int, out var statusCode CustomStatusCode)`; `func RequestBuyPet(player entity<Player>, pet entity<Entity>)`; `func CheckConditionBuyPet(player entity<Player>, pet entity<Entity>, out var statusCode CustomStatusCode)`; `async func ProcessBuyPet(player entity<Player>, petParade entity<Entity>)`
- **Dependencies:** `import "List.fcc" as List`; `import "Math.fcc" as Math`; `import "Playable.fcc" as Playable`; `import "Workflow.fcc" as Workflow`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import Res from "EditorGenLib.fcc"`; `import "../Configs/MobConfig.fcg" as MobConfig`; `import "../Configs/GlobalConfig.fcg" as GlobalConfig`; `import "../Configs/MutationConfig.fcg" as MutationConfig`; `import "../Manager/PetsManager.fcg" as PetsManager`; `import "../Manager/WalletManager.fcg" as WalletManager`; `import "../Manager/PlayersManager.fcg" as PlayersManager`; `import "../Player/PlayerBase.fcg" as PlayerBase`; `import "../Player/PlayerSFXHandler.fcg" as PlayerSFXHandler`; `import "../Mobs/MobHandler.fcg" as MobHandler`; `import "../Mobs/MobModelHandler.fcg" as MobModelHandler`; `import "../Mobs/MobParadeHandler.fcg" as MobParadeHandler`; `import "../Utils/WeightedRandom.fcg" as WeightedRandom`; `import "../Utils/BigNumberHandler.fcg" as BigNumberHandler`; `import "../_SharedLibs/CoreLib/ActionController.fcg" as ActionController`; `import "../_SharedLibs/PetLib/PetStateController.fcg" as PetStateController`; `import "../_SharedLibs/PetLib/ValidationController.fcg" as ValidationController`
- **Observed API/engine calls:** `CreateFromPrefab`, `DispatchEventToEntity`, `WaitForMillisecond`, `WaitForNextFrame`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Manager/PetsManager.fcg`

- **Location / full source:** `Assets/Scripts/Manager/PetsManager.fcg`; `Assets/Scripts/Manager/PetsManager.fcg`; 26742 bytes, 736 lines.
- **Purpose:** Coordinates shared game state and player-facing rules for `PetsManager`.
- **Graph:** `PetsManager`.
- **Graph fields (direct source):** `SHEET_PETS (inferred) = "PlayerSave"`; `KEY_PETS: Map<DataType, string> = Map<DataType, string>{`; `MAP_CODE (inferred) = ""`; `MAX_CAPACITY (inferred) = 18`; `DEFAULT_PETS: Map<DataType, object> = Map<DataType, object>{`; `_CurrentPetIndex: int`; `_BasePetIndices: List<int> // Pet Indices in bases`; `_HandPetIndices: List<int> // Pet Indices on hands // Stealing or Selecting`; `_DebugLog: string`; `_PetIndexMutexLocked: bool`; `_PetIndexMutexThreadId: string`; `_AllowInteractPet: Map<UUID, bool>`; `_PlayerPetIds: Map<UUID, List<int>>`; `_PlayerPetMutations: Map<UUID, List<int>>`; `_PlayerPetBalances: Map<UUID, List<List<int>>>`; `_PlayerPetsInteractable: Map<UUID, List<bool>>`; `_PlayerMaxQuantity: Map<UUID, int>`; `_PlayerCurrentHold: Map<UUID, int>`; `_PlayerCurrentAwait: Map<UUID, int>`
- **Event signatures (direct source):** `event OnAwake()`; `event OnDatabaseLoad(playerUID UUID, databaseType string)`; `event OnDatabaseSave(playerUID UUID, databaseType string)`
- **Working logic (declaration-level):** Declared helper flow: InitPetsManager, InitPlayerPet, LoadPetsDatabase, LoadPlayerPets, SavePetsDatabase, SavePlayerPets, GetBasePetIndices, GetHandPetIndices, IsExistingBasePet, AddBasePetIndex, RemoveBasePetIndex, IsExistingHandPet, AddHandPetIndex, RemoveHandPetIndex, SetAllowInteractPet, CanInteractPlayerPet, GetPlayerPetIdsList, GetPlayerPetIdBySlot, SetPlayerPetIdAt, GetPlayerPetMutationsList, GetPlayerPetMutationsBySlot, SetPlayerPetMutationsBySlot, GetPlayerPetBalancesList, GetPlayerPetBalanceBySlot, SetPlayerPetBalanceBySlot, GetPlayerInteractablePets, CanInteractPlayerPetAt, SetPlayerPetInteractableAt, GetPlayerOwnPetsValue, UpdatePetBalanceOffline, InitPlayerPetIDs, ResetAllPlayerPets, AddPlayerPet, AddPlayerPetAt, CreatePet, RemovePlayerPet, RemovePlayerPetVisual, GetAvailableSlot, GetInteractiveSlot, CheckSlotAvailable, GetNumberSlotAvailable, HandleCollectPetBalance, HandleSellPet, GetPlayerMaxQuantity, SetPlayerExtraSlot, GetPlayerCurrentAwait, SetPlayerCurrentAwait, GetPlayerCurrentHold, SetPlayerCurrentHold.
- **Functions, inputs and outputs (direct source signatures):** `func InitPetsManager()`; `func InitPlayerPet(playerUID UUID)`; `async func LoadPetsDatabase(playerUID UUID)`; `async func LoadPlayerPets( playerUID UUID, dataType DataType, rawPets object, needRetry bool, out var result List<object>, out var isSuccess bool)`; `async func SavePetsDatabase(playerUID UUID)`; `async func SavePlayerPets(playerUID UUID, dataType DataType, petValue List<object>)`; `func GetBasePetIndices() List<int>`; `func GetHandPetIndices() List<int>`; `func IsExistingBasePet(petIndex int) bool`; `func AddBasePetIndex(petIndex int)`; `func RemoveBasePetIndex(petIndex int)`; `func IsExistingHandPet(petIndex int) bool`; `func AddHandPetIndex(petIndex int)`; `func RemoveHandPetIndex(petIndex int)`; `func SetAllowInteractPet(player entity<Player>, allowInteract bool)`; `func CanInteractPlayerPet(playerUID UUID) bool`; `func GetPlayerPetIdsList(playerUID UUID) List<int>`; `func GetPlayerPetIdBySlot(playerUID UUID, slot int) int`; `func SetPlayerPetIdAt(playerUID UUID, slot int, petId int)`; `func GetPlayerPetMutationsList(playerUID UUID) List<int>`; `func GetPlayerPetMutationsBySlot(playerUID UUID, slot int) int`; `func SetPlayerPetMutationsBySlot(playerUID UUID, slot int, mutationId int)`; `func GetPlayerPetBalancesList(playerUID UUID) List<List<int>>`; `func GetPlayerPetBalanceBySlot(playerUID UUID, slot int) List<int>`; `func SetPlayerPetBalanceBySlot(playerUID UUID, slot int, balance List<int>)`; `func GetPlayerInteractablePets(playerUID UUID) List<bool>`; `func CanInteractPlayerPetAt(playerUID UUID, slot int) bool`; `func SetPlayerPetInteractableAt(playerUID UUID, slot int, interactable bool)`; `func HasNonInteractablePet(playerUID UUID) bool`; `func GetPlayerOwnPetsValue(player entity<Player>) int`; `func HasPetAt(playerUID UUID, slot int) bool`; `func HasPet(playerUID UUID, petId int) bool`; `async func UpdatePetBalanceOffline(player entity<Player>, deltaTime int)`; `async func PetBalanceUpdateLoop(player entity<Player>)`; `func PetBalanceUpdate(player entity<Player>, petIndex int, deltaTime int)`; `async func InitPlayerPetIDs(playerUID UUID)`; `func ResetAllPlayerPets(player entity<Player>)`; `func AddPlayerPet(player entity<Player>, petId int, mutationId int, petIndex int, isDecAwait bool)`; `func AddPlayerPetAt(player entity<Player>, petId int, mutationId int, slotIndex int, petIndex int)`; `func PolishWeatherIds(weatherIds List<int>) List<int>`; `func CreatePet(player entity<Player>, petId int, mutationId int, petIndex int) entity<Entity>`; `func RemovePlayerPet(player entity<Player>, slot int, isRemovePetIndex bool)`; `func RemovePlayerPetVisual(player entity<Player>, slot int, isRemovePetIndex bool)`; `func GetAvailableSlot(player entity<Player>) int`; `func GetInteractiveSlot(player entity<Player>) int`; `func FindPetSlotByIndex(player entity<Player>, petIndex int) int`; `func CheckSlotAvailable(player entity<Player>) bool`; `func GetNumberSlotAvailable(player entity<Player>)int`; `func HandleCollectPetBalance(player entity<Player>, slot int)`; `func HandleSellPet(player entity<Player>)`; `func GetPlayerMaxQuantity(player entity<Player>) int`; `func SetPlayerExtraSlot(player entity<Player>, maxNew int)`; `func GetPlayerCurrentAwait(player entity<Player>) int`; `func SetPlayerCurrentAwait(player entity<Player>, currentAwait int)`; `func IncPlayerCurrentAwait(player entity<Player>)`; `func DecPlayerCurrentAwait(player entity<Player>)`; `func GetPlayerCurrentHold(player entity<Player>) int`; `func SetPlayerCurrentHold(player entity<Player>, currentHold int)`; `func IncPlayerCurrentHold(player entity<Player>)`; `func DecPlayerCurrentHold(player entity<Player>)`
- **Dependencies:** `import "Map.fcc" as Map`; `import "List.fcc" as List`; `import "Math.fcc" as Math`; `import "Player.fcc" as Player`; `import "Database.fcc" as Database`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Configs/MobConfig.fcg" as MobConfig`; `import "../Manager/StealManager.fcg" as StealManager`; `import "../Manager/WalletManager.fcg" as WalletManager`; `import "../Manager/PlayersManager.fcg" as PlayersManager`; `import "../Player/PlayerBase.fcg" as PlayerBase`; `import "../Player/PlayerInteract.fcg" as PlayerInteract`; `import "../Mobs/PetMutex.fcg" as PetMutex`; `import "../Mobs/MobHandler.fcg" as MobHandler`; `import "../Mobs/MobParadeHandler.fcg" as MobParadeHandler`; `import "../HUDs/HudMenu.fcg" as HudMenu`; `import "../Utils/DataUtils.fcg" as DataUtils`; `import "../Utils/BigNumberHandler.fcg" as BigNumberHandler`; `import "../_SharedLibs/CoreLib/DatabaseController.fcg" as DatabaseController`; `import "../_SharedLibs/PetLib/PlayerStateController.fcg" as PlayerStateController`
- **Observed API/engine calls:** `CreateFromPrefab`, `DispatchEventToEntity`, `GetAllPlayers`, `WaitForMillisecond`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Manager/PlayersManager.fcg`

- **Location / full source:** `Assets/Scripts/Manager/PlayersManager.fcg`; `Assets/Scripts/Manager/PlayersManager.fcg`; 5346 bytes, 185 lines.
- **Purpose:** Coordinates shared game state and player-facing rules for `PlayersManager`.
- **Graph:** `PlayersManager`.
- **Graph fields (direct source):** `SHEET_PLAYERS (inferred) = "PlayerSave"`; `KEY_PLAYERS: Map<DataType, string> = Map<DataType, string>{`; `MAP_CODE (inferred) = ""`; `RECONNECT_DELAY (inferred) = 5000`; `_ExistingPlayers: Map<UUID, entity<Player>>`; `_PlayerLastLogTime: Map<UUID, int>`; `_PlayerDeltaLastLogTime: Map<UUID, int>`
- **Event signatures (direct source):** `event OnAwake()`; `event OnPlayerJoin(player entity<Player>)`; `event OnDatabaseLoad(playerUID UUID, databaseType string)`; `event OnDatabaseSave(playerUID UUID, databaseType string)`; `event OnDisconnect(player entity<Player>)`; `event OnReconnect(player entity<Player>)`
- **Working logic (declaration-level):** Declared helper flow: InitPlayerManager, InitPlayer, LoadPlayersDatabase, LoadPlayerLastLogTime, SavePlayersDatabase, SavePlayerLastLogTime, IsExistingPlayer, GetExistingPlayersByUID, GetPlayerLastLogTime, GetPlayerDeltaLastLogTime.
- **Functions, inputs and outputs (direct source signatures):** `func InitPlayerManager()`; `func InitPlayer(player entity<Player>)`; `async func LoadPlayersDatabase(playerUID UUID)`; `async func LoadPlayerLastLogTime(playerUID UUID, lastLogTime string, needRetry bool, out var result int, out var isSuccess bool)`; `async func SavePlayersDatabase(playerUID UUID)`; `async func SavePlayerLastLogTime(playerUID UUID)`; `func IsExistingPlayer(playerUID UUID) bool`; `func GetExistingPlayersByUID(playerUID UUID) entity<Player>`; `func GetPlayerLastLogTime(playerUID UUID) int`; `func GetPlayerDeltaLastLogTime(playerUID UUID) int`
- **Dependencies:** `import "Map.fcc" as Map`; `import "List.fcc" as List`; `import "Math.fcc" as Math`; `import "Player.fcc" as Player`; `import "Convert.fcc" as Convert`; `import "Database.fcc" as Database`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Utils/DataUtils.fcg" as DataUtils`; `import "../_SharedLibs/CoreLib/DatabaseController.fcg" as DatabaseController`
- **Observed API/engine calls:** `WaitForMillisecond`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Manager/RebirthManager.fcg`

- **Location / full source:** `Assets/Scripts/Manager/RebirthManager.fcg`; `Assets/Scripts/Manager/RebirthManager.fcg`; 17734 bytes, 515 lines.
- **Purpose:** Coordinates shared game state and player-facing rules for `RebirthManager`.
- **Graph:** `RebirthManager`.
- **Graph fields (direct source):** `SHEET_REBIRTH (inferred) = "PlayerSave"`; `KEY_REBIRTH: Map<DataType, string> = Map<DataType, string>{`; `MAP_CODE (inferred) = ""`; `DEFAULT_REBIRTH_LEVEL (inferred) = 1`; `UNLOCK_PET_SLOTS_MAX_LEVEL: int = 13`; `UNLOCK_SWAP_LEVEL: int = 2`; `UNLOCK_HATCH_OTHER_EGG_LEVEL: int = 2`; `UNLOCK_DUST_LEVEL: int = 3`; `UNLOCK_FUSION_LEVEL: int = 3`; `UNLOCK_GIFTCODE_LEVEL: int = 7`; `UNLOCK_PORTALS_LEVEL: int = 14`; `UNLOCK_PET_FOLLOWING_LEVEL: int = 18`; `ALLOW_STEAL_EPIC_LEVEL: int = 2`; `ALLOW_STEAL_LEGENDARY_LEVEL: int = 4`; `ALLOW_STEAL_MYTHIC_LEVEL: int = 6`; `ALLOW_STEAL_DIVINE_LEVEL: int = 10`; `_PlayerRebirthLevel: Map<UUID, int>`; `_DebugLog: string`
- **Event signatures (direct source):** `event OnAwake()`; `event OnDatabaseLoad(playerUID UUID, databaseType string)`; `event OnDatabaseSave(playerUID UUID, databaseType string)`; `event OnProcessAction(playerUID UUID, actionType string, payload Map<object, object>)`
- **Working logic (declaration-level):** Declared helper flow: InitRebirthManager, InitPlayerRebirth, LoadRebirthDatabase, LoadPlayerRebirth, SaveRebirthDatabase, SavePlayerRebirth, RequestRebirth, CheckConditionForRebirth, LoadRebirthData, ResetRebirthStats, GetPlayerRebirthLevel, SetPlayerRebirthLevel, GetNextRebirthRewards, GetUnlockedSwapLevel, IsUnlockedSwap, GetUnlockedHatchOtherEggLevel, IsUnlockedHatchOtherEgg, GetUnlockedDustLevel, IsUnlockedDust, GetUnlockedFusionLevel, IsUnlockedFusion, GetUnlockedGiftcodeLevel, CanUseGiftcode, GetUnlockedPortalsLevel, IsUnlockedPortals, GetUnlockedPetFollowingLevel, IsUnlockedPetFollowing, GetAllowedStealEpicLevel, IsAllowedStealEpic, GetAllowedStealLegendaryLevel, IsAllowedStealLegendary, GetAllowedStealMythicLevel, IsAllowedStealMythic, GetAllowedStealDivineLevel, IsAllowedStealDivine, GetAllowedStealRarityLevel, IsAllowedStealRarity.
- **Functions, inputs and outputs (direct source signatures):** `func InitRebirthManager()`; `func InitPlayerRebirth(playerUID UUID)`; `async func LoadRebirthDatabase(playerUID UUID)`; `async func LoadPlayerRebirth(playerUID UUID, rawRebirthLevel object, needRetry bool, out var result int, out var isSuccess bool)`; `async func SaveRebirthDatabase(playerUID UUID)`; `async func SavePlayerRebirth(playerUID UUID)`; `func RequestRebirth(player entity<Player>)`; `func CheckConditionForRebirth(player entity<Player>, out var statusCode CustomStatusCode)`; `async func DoRebirth(player entity<Player>)`; `async func LoadRebirthData(playerUID UUID, rebirthLevel int)`; `func ResetRebirthStats(player entity<Player>)`; `func GetPlayerRebirthLevel(playerUID UUID) int`; `func SetPlayerRebirthLevel(playerUID UUID, rebirthLevel int)`; `func GetNextRebirthRewards(playerUID UUID) Map<RebirthRewardType, object>`; `func GetUnlockedSwapLevel() int`; `func IsUnlockedSwap(playerUID UUID) bool`; `func GetUnlockedHatchOtherEggLevel() int`; `func IsUnlockedHatchOtherEgg(playerUID UUID) bool`; `func GetUnlockedDustLevel() int`; `func IsUnlockedDust(playerUID UUID) bool`; `func GetUnlockedFusionLevel() int`; `func IsUnlockedFusion(playerUID UUID) bool`; `func GetUnlockedGiftcodeLevel() int`; `func CanUseGiftcode(playerUID UUID, requireRebirth int) bool`; `func GetUnlockedPortalsLevel() int`; `func IsUnlockedPortals(playerUID UUID) bool`; `func GetUnlockedPetFollowingLevel() int`; `func IsUnlockedPetFollowing(playerUID UUID) bool`; `func GetAllowedStealEpicLevel() int`; `func IsAllowedStealEpic(playerUID UUID) bool`; `func GetAllowedStealLegendaryLevel() int`; `func IsAllowedStealLegendary(playerUID UUID) bool`; `func GetAllowedStealMythicLevel() int`; `func IsAllowedStealMythic(playerUID UUID) bool`; `func GetAllowedStealDivineLevel() int`; `func IsAllowedStealDivine(playerUID UUID) bool`; `func GetAllowedStealRarityLevel(rarity RarityEnum) int`; `func IsAllowedStealRarity(playerUID UUID, rarity RarityEnum) bool`
- **Dependencies:** `import "Convert.fcc" as Convert`; `import "Strings.fcc" as Strings`; `import "Database.fcc" as Database`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Configs/MobConfig.fcg" as MobConfig`; `import "../Configs/RebirthConfig.fcg" as RebirthConfig`; `import "../Manager/GlobalBase.fcg" as GlobalBase`; `import "../Manager/PetsManager.fcg" as PetsManager`; `import "../Manager/WalletManager.fcg" as WalletManager`; `import "../Manager/PlayersManager.fcg" as PlayersManager`; `import "../Player/PlayerBase.fcg" as PlayerBase`; `import "../Player/PlayerTeleport.fcg" as PlayerTeleport`; `import "../Base/LaserWall/LaserWallHandler.fcg" as LaserWallHandler`; `import "../HUDs/HudWallet.fcg" as HudWallet`; `import "../Utils/BigNumberHandler.fcg" as BigNumberHandler`; `import "../_SharedLibs/CoreLib/ActionController.fcg" as ActionController`; `import "../_SharedLibs/CoreLib/DatabaseController.fcg" as DatabaseController`; `import "../_SharedLibs/PetLib/PlayerStateController.fcg" as PlayerStateController`
- **Observed API/engine calls:** `DispatchEventToEntity`, `WaitForMillisecond`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Manager/StealManager.fcg`

- **Location / full source:** `Assets/Scripts/Manager/StealManager.fcg`; `Assets/Scripts/Manager/StealManager.fcg`; 16776 bytes, 425 lines.
- **Purpose:** Coordinates shared game state and player-facing rules for `StealManager`.
- **Graph:** `StealManager`.
- **Graph fields (direct source):** `MAX_STEAL_DISTANCE: float = 5`; `MAX_STEAL_TIME: int = 3 // seconds`; `_DebugLog: string`; `_PlayerStealingPayload: Map<entity<Player>, Map<RequestParameter, object>>`; `_PlayerStolenPetSlots: Map<entity<Player>, List<int>>`
- **Event signatures (direct source):** `event OnAwake()`; `event OnPlayerJoin(player entity<Player>)`; `event OnProcessAction(playerUID UUID, actionType string, payload Map<object, object>)`; `event OnUserQuitOrUserMatchEnd(player entity<Player>)`
- **Working logic (declaration-level):** Declared helper flow: InitStealManager, InitPlayer, RequestStealPet, CheckConditionStealPet, CheckHackStealingWithDistance, CheckHackStealingWithTime, RequestStolenPetSuccess, CheckConditionStolenPetSuccess, ResetStealStatuses, RequestStolenPetFail, CheckConditionStolenPetFail, GetPlayerStealingPayload, SetPlayerStealingPayload, GetPlayerStolenPets, IsPlayerStolenPet, UpdateStolenPets.
- **Functions, inputs and outputs (direct source signatures):** `func InitStealManager()`; `func InitPlayer(player entity<Player>)`; `func RequestStealPet(snatcherUID UUID, payload Map<object, object>)`; `func CheckConditionStealPet(snatcherUID UUID, payload Map<object, object>, out var statusCode CustomStatusCode)`; `func CheckHackStealingWithDistance(snatcher entity<Player>, owner entity<Player>, petSlotId int) bool`; `func CheckHackStealingWithTime(snatcher entity<Player>) bool`; `func ProcessStealPet(snatcherUID UUID, payload Map<object, object>)`; `func RequestStolenPetSuccess(snatcherUID UUID)`; `func CheckConditionStolenPetSuccess(snatcherUID UUID, out var statusCode CustomStatusCode)`; `func ProcessStolenSuccess(snatcher entity<Player>)`; `func ResetStealStatuses(snatcher entity<Player>)`; `func RequestStolenPetFail(snatcherUID UUID)`; `func CheckConditionStolenPetFail(snatcherUID UUID, out var statusCode CustomStatusCode)`; `func ProcessStolenFail(snatcher entity<Player>)`; `func GetPlayerStealingPayload(player entity<Player>) Map<RequestParameter, object>`; `func SetPlayerStealingPayload(player entity<Player>, payload Map<RequestParameter, object>)`; `func GetPlayerStolenPets(player entity<Player>) List<int>`; `func IsPlayerStolenPet(player entity<Player>, petSlot int) bool`; `func UpdateStolenPets(owner entity<Player>, petSlot int, isAdded bool)`
- **Dependencies:** `import "Map.fcc" as Map`; `import "List.fcc" as List`; `import "Math.fcc" as Math`; `import "Items.fcc" as Items`; `import "Player.fcc" as Player`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Configs/MobConfig.fcg" as MobConfig`; `import "../Configs/GlobalConfig.fcg" as GlobalConfig`; `import "../Configs/MutationConfig.fcg" as MutationConfig`; `import "../Manager/PetsManager.fcg" as PetsManager`; `import "../Manager/PlayersManager.fcg" as PlayersManager`; `import "../Manager/RebirthManager.fcg" as RebirthManager`; `import "../Player/PlayerBase.fcg" as PlayerBase`; `import "../Mobs/PetMutex.fcg" as PetMutex`; `import "../Mobs/MobHandler.fcg" as MobHandler`; `import "../_SharedLibs/CoreLib/ActionController.fcg" as ActionController`; `import "../_SharedLibs/PetLib/PlayerStateController.fcg" as PlayerStateController`
- **Observed API/engine calls:** `DispatchEventToEntity`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Manager/WalletManager.fcg`

- **Location / full source:** `Assets/Scripts/Manager/WalletManager.fcg`; `Assets/Scripts/Manager/WalletManager.fcg`; 9485 bytes, 281 lines.
- **Purpose:** Coordinates shared game state and player-facing rules for `WalletManager`.
- **Graph:** `WalletManager`.
- **Graph fields (direct source):** `SHEET_WALLET (inferred) = "PlayerSave"`; `KEY_WALLET: Map<DataType, string> = Map<DataType, string>{`; `MAP_CODE (inferred) = ""`; `DEFAULT_WALLET: Map<DataType, List<int>> = Map<DataType, List<int>>{`; `_PlayerBalance: Map<UUID, List<int>>`; `_MultiplyRate: Map<UUID, float>`; `_DebugLog: string`
- **Event signatures (direct source):** `event OnAwake()`; `event OnPlayerJoin(player entity<Player>)`; `event OnDatabaseLoad(playerUID UUID, databaseType string)`; `event OnDatabaseSave(playerUID UUID, databaseType string)`
- **Working logic (declaration-level):** Declared helper flow: InitWalletManager, InitPlayerWallet, LoadWalletDatabase, LoadPlayerWallet, SaveWalletDatabase, SavePlayerWallet, GetPlayerBalance, SetPlayerBalance, GetBalanceRankScore, GetPlayerMultiplyRate, SetPlayerMultiplyRate.
- **Functions, inputs and outputs (direct source signatures):** `func InitWalletManager()`; `func InitPlayerWallet(playerUID UUID)`; `async func LoadWalletDatabase(playerUID UUID)`; `async func LoadPlayerWallet( playerUID UUID, walletType DataType, rawWallet object, needRetry bool, out var result List<int>, out var isSuccess bool)`; `async func SaveWalletDatabase(playerUID UUID)`; `async func SavePlayerWallet(playerUID UUID, walletType DataType, walletValue List<int>)`; `async func ProcessIdleIncomeGain(playerUID UUID)`; `func EarnNewIncome(currentIncome List<int>, maxCapIncome List<int>, earnAmount List<int>) List<int>`; `func HasEnoughWallet(currentWallet List<int>, amount List<int>) bool`; `func GetPlayerBalance(playerUID UUID) List<int>`; `func SetPlayerBalance(playerUID UUID, balance List<int>)`; `func EarnBalance(player entity<Player>, amount List<int>)`; `func SpendBalance(player entity<Player>, amount List<int>)`; `func HasEnoughBalance(player entity<Player>, amount List<int>) bool`; `func GetBalanceRankScore(balance List<int>) int`; `func GetPlayerMultiplyRate(playerUID UUID) float`; `func SetPlayerMultiplyRate(playerUID UUID, multiplyRate float)`
- **Dependencies:** `import "Map.fcc" as Map`; `import "List.fcc" as List`; `import "Math.fcc" as Math`; `import "Player.fcc" as Player`; `import "Database.fcc" as Database`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Configs/RebirthConfig.fcg" as RebirthConfig`; `import "../Manager/PlayersManager.fcg" as PlayersManager`; `import "../Manager/RebirthManager.fcg" as RebirthManager`; `import "../Player/PlayerSFXHandler.fcg" as PlayerSFXHandler`; `import "../Utils/BigNumberHandler.fcg" as BigNumberHandler`; `import "../_SharedLibs/CoreLib/DatabaseController.fcg" as DatabaseController`
- **Observed API/engine calls:** `DispatchEventToEntity`, `WaitForMillisecond`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

### `Assets/Scripts/Mobs`

#### `Assets/Scripts/Mobs/MobBaseTrigger.fcg`

- **Location / full source:** `Assets/Scripts/Mobs/MobBaseTrigger.fcg`; `Assets/Scripts/Mobs/MobBaseTrigger.fcg`; 1358 bytes, 44 lines.
- **Purpose:** Implements pet/mob entity behavior for `MobBaseTrigger`.
- **Graph:** `MobBaseTrigger`.
- **Graph fields (direct source):** `_BaseEntity: entity<Entity>`; `_BaseOwner: entity<Player>`; `_ParentEntity: entity<Entity>`; `_SlotInBase: int`
- **Event signatures (direct source):** `event OnTriggerEnter(target entity<Entity>)`; `event OnTriggerLeave(target entity<Entity>)`
- **Working logic (declaration-level):** Declared helper flow: InitParams, InitProtectParams.
- **Functions, inputs and outputs (direct source signatures):** `func InitParams()`; `func InitProtectParams()`
- **Dependencies:** `import "List.fcc" as List`; `import "Physics.fcc" as Physics`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Player/PlayerBase.fcg" as PlayerBase`; `import "../Player/PlayerInteract.fcg" as PlayerInteract`; `import "../Utils/BigNumberHandler.fcg" as BigNumberHandler`
- **Observed API/engine calls:** `DispatchEventToEntity`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Mobs/MobDescriptionHandler.fcg`

- **Location / full source:** `Assets/Scripts/Mobs/MobDescriptionHandler.fcg`; `Assets/Scripts/Mobs/MobDescriptionHandler.fcg`; 1834 bytes, 46 lines.
- **Purpose:** Implements pet/mob entity behavior for `MobDescriptionHandler`.
- **Graph:** `MobDescriptionHandler`.
- **Graph fields (direct source):** none
- **Event signatures (direct source):** none
- **Working logic (declaration-level):** Declared helper flow: SetMobDescription, SetMobDescriptionFollowing, GetMutationText.
- **Functions, inputs and outputs (direct source signatures):** `func SetMobDescription(mobId int, mutationId int)`; `func SetMobDescriptionFollowing(player entity<Player>)`; `func GetMutationText(mutationId int) StringOrLocString`
- **Dependencies:** `import "List.fcc" as List`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Configs/MobConfig.fcg" as MobConfig`; `import "../Configs/MutationConfig.fcg" as MutationConfig`; `import "../Utils/BigNumberHandler.fcg" as BigNumberHandler`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Mobs/MobHandler.fcg`

- **Location / full source:** `Assets/Scripts/Mobs/MobHandler.fcg`; `Assets/Scripts/Mobs/MobHandler.fcg`; 2070 bytes, 68 lines.
- **Purpose:** Implements pet/mob entity behavior for `MobHandler`.
- **Graph:** `MobHandler`.
- **Graph fields (direct source):** `_MobIndex: int`; `_MobID: int`; `_MutationID: int`; `_MobModel: entity<Entity>`; `_MobDescription: entity<Entity>`; `_MobRarityRing: entity<Entity>`; `_MobMutationEffects: Map<MutationEnum, entity<Entity>>`
- **Event signatures (direct source):** `event OnAwake()`
- **Working logic (declaration-level):** Declared helper flow: GetMobID, GetMutationID, GetMobIndex, SetMobIndex, SetMobWithID.
- **Functions, inputs and outputs (direct source signatures):** `func GetMobID() int`; `func GetMutationID() int`; `func GetMobIndex() int`; `func SetMobIndex(index int)`; `func SetMobWithID(mobId int, mutationId int)`
- **Dependencies:** `import "List.fcc" as List`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import Res from "EditorGenLib.fcc"`; `import "./MobModelHandler.fcg" as MobModelHandler`; `import "./MobRarityRingHandler.fcg" as MobRarityRingHandler`; `import "./MobDescriptionHandler.fcg" as MobDescriptionHandler`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Mobs/MobModelHandler.fcg`

- **Location / full source:** `Assets/Scripts/Mobs/MobModelHandler.fcg`; `Assets/Scripts/Mobs/MobModelHandler.fcg`; 1813 bytes, 53 lines.
- **Purpose:** Implements pet/mob entity behavior for `MobModelHandler`.
- **Graph:** `MobModelHandler`.
- **Graph fields (direct source):** `_DefaultRenderMaterial: MaterialID`; `_StealRenderMaterial: MaterialID = EResMaterial.StealMat`
- **Event signatures (direct source):** none
- **Working logic (declaration-level):** Declared helper flow: ResetDefaultRender.
- **Functions, inputs and outputs (direct source signatures):** `func ResetDefaultRender()`; `func SwitchModelMesh(meshKey string)`; `func SwitchModelMeshWithID(id int)`; `func SwitchToSteal()`; `func SwitchToDefault()`; `func SwitchRenderMutation(mobId int, mutationID int)`
- **Dependencies:** `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import Res from "EditorGenLib.fcc"`; `import "../Configs/MobConfig.fcg" as MobConfig`; `import "../Configs/MutationConfig.fcg" as MutationConfig`; `import "../Mobs/MobHandler.fcg" as MobHandler`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Mobs/MobParadeHandler.fcg`

- **Location / full source:** `Assets/Scripts/Mobs/MobParadeHandler.fcg`; `Assets/Scripts/Mobs/MobParadeHandler.fcg`; 1829 bytes, 67 lines.
- **Purpose:** Implements pet/mob entity behavior for `MobParadeHandler`.
- **Graph:** `MobParadeHandler`.
- **Graph fields (direct source):** `_PlayerBuy: entity<Player>`; `_MoveTween: entity<Tween>`; `_CurrentTweenIndex: int`; `_TransactionIndex: string`
- **Event signatures (direct source):** `event OnAwake()`
- **Working logic (declaration-level):** Declared helper flow: GetPlayerBuy, SetPlayerBuy, GetTransactionIndex, SetTransactionIndex, GetMoveTween, SetMoveTween.
- **Functions, inputs and outputs (direct source signatures):** `func GetPlayerBuy() entity<Player>`; `func SetPlayerBuy(player entity<Player>)`; `func GetTransactionIndex() string`; `func SetTransactionIndex(transactionIndex string)`; `func GetMoveTween() entity<Tween>`; `func SetMoveTween(tween entity<Tween>, out var tweenIndex int)`; `async func DestroyMoveTween(tweenIndex int, out var wasCurrentTween bool)`
- **Dependencies:** `import "List.fcc" as List`; `import "Math.fcc" as Math`; `import "Playable.fcc" as Playable`; `import "Animation.fcc" as Animation`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Manager/PetsManager.fcg" as PetsManager`; `import "../Manager/PetParadeManager.fcg" as PetParadeManager`; `import "../Player/PlayerBase.fcg" as PlayerBase`; `import "../Player/PlayerSFXHandler.fcg" as PlayerSFXHandler`; `import "../Mobs/MobHandler.fcg" as MobHandler`; `import "../Mobs/MobParadeTrigger.fcg" as MobParadeTrigger`; `import "../Utils/BigNumberHandler.fcg" as BigNumberHandler`
- **Observed API/engine calls:** `WaitForNextFrame`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Mobs/MobParadeTrigger.fcg`

- **Location / full source:** `Assets/Scripts/Mobs/MobParadeTrigger.fcg`; `Assets/Scripts/Mobs/MobParadeTrigger.fcg`; 647 bytes, 19 lines.
- **Purpose:** Implements pet/mob entity behavior for `MobParadeTrigger`.
- **Graph:** `MobParadeTrigger`.
- **Graph fields (direct source):** none
- **Event signatures (direct source):** `event OnTriggerEnter(target entity<Entity>)`; `event OnTriggerLeave(target entity<Entity>)`
- **Working logic (declaration-level):** No function declaration parsed.
- **Functions, inputs and outputs (direct source signatures):** none
- **Dependencies:** `import "List.fcc" as List`; `import "Physics.fcc" as Physics`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Player/PlayerInteract.fcg" as PlayerInteract`; `import "../Mobs/MobParadeHandler.fcg" as MobParadeHandler`
- **Observed API/engine calls:** `DispatchEventToEntity`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Mobs/MobRarityRingHandler.fcg`

- **Location / full source:** `Assets/Scripts/Mobs/MobRarityRingHandler.fcg`; `Assets/Scripts/Mobs/MobRarityRingHandler.fcg`; 893 bytes, 29 lines.
- **Purpose:** Implements pet/mob entity behavior for `MobRarityRingHandler`.
- **Graph:** `MobRarityRingHandler`.
- **Graph fields (direct source):** `_RarityRing: entity<Entity>`
- **Event signatures (direct source):** `event OnAwake()`
- **Working logic (declaration-level):** Declared helper flow: SetMobRarityRing.
- **Functions, inputs and outputs (direct source signatures):** `func SetMobRarityRing(id int)`
- **Dependencies:** `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Configs/MobConfig.fcg" as MobConfig`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Mobs/PetMutex.fcg`

- **Location / full source:** `Assets/Scripts/Mobs/PetMutex.fcg`; `Assets/Scripts/Mobs/PetMutex.fcg`; 1050 bytes, 41 lines.
- **Purpose:** Implements pet/mob entity behavior for `PetMutex`.
- **Graph:** `PetMutex`.
- **Graph fields (direct source):** `_Locked: bool`; `_ThreadId: string`
- **Event signatures (direct source):** none
- **Working logic (declaration-level):** Declared helper flow: CreateThreadId, GetCurrentThreadId.
- **Functions, inputs and outputs (direct source signatures):** `func MutexLock(player entity<Player>, out var threadId string, out var isSuccess bool)`; `func MutexUnlock(threadId string)`; `func CreateThreadId(player entity<Player>) string`; `func GetCurrentThreadId() string`
- **Dependencies:** `import "Math.fcc" as Math`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

### `Assets/Scripts/Player`

#### `Assets/Scripts/Player/PlayerBase.fcg`

- **Location / full source:** `Assets/Scripts/Player/PlayerBase.fcg`; `Assets/Scripts/Player/PlayerBase.fcg`; 9451 bytes, 284 lines.
- **Purpose:** Implements player lifecycle or interaction behavior for `PlayerBase`.
- **Graph:** `PlayerBase`.
- **Graph fields (direct source):** `_BaseExtraLevel: int`; `_ExtraFloors: entity<Entity>`; `_Base: entity<Entity>`; `_DisplayZones: List<entity<Entity>>`; `_LaserWallDuration: int`
- **Event signatures (direct source):** `event OnAwake()`; `event OnCollectMoney(player entity<Player>, slot int, amount List<int>)`
- **Working logic (declaration-level):** Declared helper flow: SetUpBase, SetMultiplierBanner, SetPlayerExtraBase, SetMobDisplayExtra, SetNameBanner, ClearBase, ClearMultiplierBanner, ClearExtraPart, ClearExtraPetDisplayZones, GetBase, GetBasePosition, GetBaseDirection, GetBaseExtraLevel, GetSpawnLocation, GetSpawnRotation, GetLaserWall, GetLaserWallSwitchTrigger, GetDisplayZones, GetDisplayZone, GetPetDisplaySlot, GetPetDisplayText, GetPetAtSlot, AddPetAtDisplaySlot, RemovePetAtDisplaySlot, SetMobAtDisplaySlotRenderSteal, SetMobAtDisplaySlotRenderDefault, GetCollectZonePosition, GetBaseIncome.
- **Functions, inputs and outputs (direct source signatures):** `func SetUpBase(base entity<Entity>)`; `func SetMultiplierBanner(content StringOrLocString)`; `async func SetPlayerExtraBase(level int)`; `async func SetMobDisplayExtra(oldCount int, newCount int)`; `func SetNameBanner(name StringOrLocString)`; `func ClearBase()`; `func ClearMultiplierBanner()`; `func ClearExtraPart()`; `func ClearExtraPetDisplayZones()`; `func GetBase() entity<Entity>`; `func GetBasePosition() Vector3`; `func GetBaseDirection() Vector3`; `func GetBaseExtraLevel() int`; `func GetSpawnLocation() Vector3`; `func GetSpawnRotation() Vector3`; `func GetLaserWall() entity<Entity>`; `func GetLaserWallSwitchTrigger() entity<Entity>`; `func GetDisplayZones() List<entity<Entity>>`; `func GetDisplayZone(slot int) entity<Entity>`; `func GetPetDisplaySlot(slot int) entity<MobDisplay>`; `func GetPetDisplayText(slot int) entity<Text>`; `func GetPetAtSlot(slot int) entity<Entity>`; `func AddPetAtDisplaySlot(mobEntity entity<Entity>, slot int)`; `func RemovePetAtDisplaySlot(slot int)`; `func SetMobAtDisplaySlotRenderSteal(slot int)`; `func SetMobAtDisplaySlotRenderDefault(slot int)`; `func BalanceDisplayUpdateAt(id int, content StringOrLocString)`; `func GetCollectZonePosition() Vector3`; `func GetBaseIncome() List<int>`
- **Dependencies:** `import "AI.fcc" as AI`; `import "Map.fcc" as Map`; `import "List.fcc" as List`; `import "Math.fcc" as Math`; `import "Player.fcc" as Player`; `import "Convert.fcc" as Convert`; `import "Playable.fcc" as Playable`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import Res from "EditorGenLib.fcc"`; `import "../Configs/MobConfig.fcg" as MobConfig`; `import "../Configs/RebirthConfig.fcg" as RebirthConfig`; `import "../Manager/PetsManager.fcg" as PetsManager`; `import "../Manager/RebirthManager.fcg" as RebirthManager`; `import "../Manager/GlobalLeaderboard.fcg" as GlobalLeaderboard`; `import "../Player/PlayerTeleport.fcg" as PlayerTeleport`; `import "../Base/Floor1Handler.fcg" as Floor1Handler`; `import "../Base/LaserWall/LaserWallHandler.fcg" as LaserWallHandler`; `import "../Base/MobDisplayHandler.fcg" as MobDisplayHandler`; `import "../Mobs/MobHandler.fcg" as MobHandler`; `import "../Mobs/MobBaseTrigger.fcg" as MobBaseTrigger`; `import "../Mobs/MobModelHandler.fcg" as MobModelHandler`; `import "../Utils/BigNumberHandler.fcg" as BigNumberHandler`; `import "../_SharedLibs/CoreLib/DatabaseController.fcg" as DatabaseController`
- **Observed API/engine calls:** `CreateFromPrefab`, `WaitForMillisecond`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Player/PlayerClientHandEquip.fcg`

- **Location / full source:** `Assets/Scripts/Player/PlayerClientHandEquip.fcg`; `Assets/Scripts/Player/PlayerClientHandEquip.fcg`; 1628 bytes, 45 lines.
- **Purpose:** Implements player lifecycle or interaction behavior for `PlayerClientHandEquip`.
- **Graph:** `PlayerClientHandEquip`.
- **Graph fields (direct source):** `WEATHER_DURATION: int = 5000`; `_CurrentMob: entity`
- **Event signatures (direct source):** `event EquipItemClient(eresMeshKey string, renderMaterial string)`; `event RemoveEquipItemClient()`
- **Working logic (declaration-level):** No function declaration parsed.
- **Functions, inputs and outputs (direct source signatures):** none
- **Dependencies:** `import "List.fcc" as List`; `import "Avatar.fcc" as Avatar`; `import "Player.fcc" as Player`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import Res from "EditorGenLib.fcc"`
- **Observed API/engine calls:** `CreateFromPrefab`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Player/PlayerEntity.fcg`

- **Location / full source:** `Assets/Scripts/Player/PlayerEntity.fcg`; `Assets/Scripts/Player/PlayerEntity.fcg`; 4188 bytes, 128 lines.
- **Purpose:** Implements player lifecycle or interaction behavior for `PlayerEntity`.
- **Graph:** `PlayerEntity`.
- **Graph fields (direct source):** `_IsImmune: bool`; `_DurationHitFly: float`; `_VelocityXZ: float`; `_VelocityY: float`; `_BuffDoubleCost: bool`
- **Event signatures (direct source):** `event OnAwake()`; `event OnHitByBullet(weapon entity<Weapon>, hitPosition Vector3)`; `event OnEliminated(attacker entity<Entity>, damageType DamageType, damagedBodyPart DamagedBodyPartType)`
- **Working logic (declaration-level):** Declared helper flow: AddBat, AddPickaxe, IsImmune, PlayerGetImmunity, AddPlayerTrigger, SetHitFly, GetDurationHitFly, GetVelocityXZ, GetVelocityY, GetBuffDoubleCost, SetBuffDoubleCost.
- **Functions, inputs and outputs (direct source signatures):** `func AddBat()`; `func AddPickaxe()`; `func DestroyPickaxe()`; `func DestroyBat()`; `func IsImmune() bool`; `async func PlayerGetImmunity(time int)`; `func AddPlayerTrigger()`; `func SetHitFly(duration float, xz float, y float)`; `func GetDurationHitFly() float`; `func GetVelocityXZ() float`; `func GetVelocityY() float`; `func GetBuffDoubleCost() bool`; `func SetBuffDoubleCost(buff bool)`
- **Dependencies:** `import "Items.fcc" as Items`; `import "Combat.fcc" as Combat`; `import "Player.fcc" as Player`; `import "Playable.fcc" as Playable`; `import "Hostility.fcc" as Hostility`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "./PlayerEntity.fcg" as OtherPlayerEntity`; `import "./PlayerTrigger.fcg" as PlayerTrigger`; `import "../Configs/GlobalConfig.fcg" as GlobalConfig`; `import "../_SharedLibs/CoreLib/ActionController.fcg" as ActionController`; `import "../_SharedLibs/PetLib/PlayerStateController.fcg" as PlayerStateController`
- **Observed API/engine calls:** `CreateFromPrefab`, `WaitForMillisecond`, `WaitForNextFrame`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Player/PlayerHintHandler.fcg`

- **Location / full source:** `Assets/Scripts/Player/PlayerHintHandler.fcg`; `Assets/Scripts/Player/PlayerHintHandler.fcg`; 1728 bytes, 59 lines.
- **Purpose:** Implements player lifecycle or interaction behavior for `PlayerHintHandler`.
- **Graph:** `PlayerHintHandler`.
- **Graph fields (direct source):** `_HintEntity: entity<Entity>`
- **Event signatures (direct source):** `event OnStealPet(snatcher entity<Player>, owner entity<Player>, petSlot int)`; `event OnStolenSuccess(snatcher entity<Player>, owner entity<Player>, petSlot int)`; `event OnStolenFail(snatcher entity<Player>, owner entity<Player>, petSlot int)`
- **Working logic (declaration-level):** Declared helper flow: InitHint, ShowHintAt.
- **Functions, inputs and outputs (direct source signatures):** `func InitHint()`; `func ShowHintAt(x float, z float)`; `func OffHint()`
- **Dependencies:** `import "Playable.fcc" as Playable`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Player/PlayerBase.fcg" as PlayerBase`; `import "../Utils/Hint.fcg" as Hint`
- **Observed API/engine calls:** `CreateFromPrefab`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Player/PlayerInteract.fcg`

- **Location / full source:** `Assets/Scripts/Player/PlayerInteract.fcg`; `Assets/Scripts/Player/PlayerInteract.fcg`; 2483 bytes, 90 lines.
- **Purpose:** Implements player lifecycle or interaction behavior for `PlayerInteract`.
- **Graph:** `PlayerInteract`.
- **Graph fields (direct source):** `_InteractSlotKey: int`; `_InteractPlayer: entity<Player>`; `_InteractLaserWall: entity<Entity>`; `_ListInteractEntity: List<entity<Entity>>`
- **Event signatures (direct source):** `event OnAwake()`; `event OnNearLaserWall(player entity<Player>, laserWall entity<Entity>)`; `event OnNearPetInHouse(player entity<Player>, owner entity<Player>, petSlot int)`; `event OnFarPetInHouse(player entity<Player>)`; `event OnNearPetParade(player entity<Player>, pet entity<Entity>)`; `event OnFarPetParade(player entity<Player>, pet entity<Entity>)`
- **Working logic (declaration-level):** Declared helper flow: SetInteractLaserWall, GetInteractLaserWall, HandleInteractPetInHouse, SetMobBaseInteract, ClearMobDisplayInteract, GetInteractSlotKey, GetInteractPlayer, AddListInteract, RemoveListInteract, GetListInteractEntity.
- **Functions, inputs and outputs (direct source signatures):** `func SetInteractLaserWall(laserWall entity<Entity>)`; `func GetInteractLaserWall() entity<Entity>`; `func HandleInteractPetInHouse(owner entity<Player>, petSlot int)`; `func SetMobBaseInteract(interactPlayer entity<Player>, interactSlotKey int)`; `func ClearMobDisplayInteract()`; `func GetInteractSlotKey() int`; `func GetInteractPlayer() entity<Player>`; `func AddListInteract(ent entity<Entity>)`; `func RemoveListInteract(ent entity<Entity>)`; `func GetListInteractEntity() List<entity<Entity>>`
- **Dependencies:** `import "List.fcc" as List`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Manager/PetsManager.fcg" as PetsManager`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Player/PlayerLaserWall.fcg`

- **Location / full source:** `Assets/Scripts/Player/PlayerLaserWall.fcg`; `Assets/Scripts/Player/PlayerLaserWall.fcg`; 4217 bytes, 111 lines.
- **Purpose:** Implements player lifecycle or interaction behavior for `PlayerLaserWall`.
- **Graph:** `PlayerLaserWall`.
- **Graph fields (direct source):** `WALL_ROTATION: List<Vector3> = List<Vector3>{`; `WALL_POSITION: Vector3 = Vector3 {0, 2.5, 0}`; `_LaserWall1: Map<entity<Player>, entity<Entity>>`; `_LaserWall2: Map<entity<Player>, entity<Entity>>`; `_LaserWall3: Map<entity<Player>, entity<Entity>>`
- **Event signatures (direct source):** `event OnAwake()`; `event OnLaserWallOn(owner entity<Player>, player entity<Player>, laserWall entity<Entity>)`; `event OnLaserWallOff(owner entity<Player>, laserWall entity<Entity>)`; `event OnPlayerQuit(player entity<Player>)`
- **Working logic (declaration-level):** Declared helper flow: CreateHiddenLaserWalls.
- **Functions, inputs and outputs (direct source signatures):** `func CreateHiddenLaserWalls(owner entity<Player>, laserWall entity<Entity>)`; `func ChangeLaserWallOwnColor(laserWall entity<Entity>)`
- **Dependencies:** `import "Player.fcc" as Player`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import Res from "EditorGenLib.fcc"`
- **Observed API/engine calls:** `CreateFromPrefab`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Player/PlayerSFXHandler.fcg`

- **Location / full source:** `Assets/Scripts/Player/PlayerSFXHandler.fcg`; `Assets/Scripts/Player/PlayerSFXHandler.fcg`; 1671 bytes, 55 lines.
- **Purpose:** Implements player lifecycle or interaction behavior for `PlayerSFXHandler`.
- **Graph:** `PlayerSFXHandler`.
- **Graph fields (direct source):** `_CanPlayWeatherBGM: bool`; `_CurrentBGM: entity<SoundEffect>`
- **Event signatures (direct source):** `event OnAwake()`; `event OnLaserWallOn(owner entity<Player>, player entity<Player>, laserWall entity<Entity>)`; `event OnLaserWallOff(owner entity<Player>, laserWall entity<Entity>)`; `event OnCollectMoney(player entity<Player>, slot int, amount List<int>)`; `event OnStealPet(snatcher entity<Player>, owner entity<Player>, petSlot int)`
- **Working logic (declaration-level):** Declared helper flow: PlaySFX, HandlePlayCashSound.
- **Functions, inputs and outputs (direct source signatures):** `func PlaySFX(ereskey object)`; `func HandlePlayCashSound(withdrawAmount List<int>)`
- **Dependencies:** `import "Map.fcc" as Map`; `import "List.fcc" as List`; `import "Playable.fcc" as Playable`; `import "Animation.fcc" as Animation`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import Res from "EditorGenLib.fcc"`; `import "../Base/LaserWall/LaserWallHandler.fcg" as LaserWallHandler`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Player/PlayerTeleport.fcg`

- **Location / full source:** `Assets/Scripts/Player/PlayerTeleport.fcg`; `Assets/Scripts/Player/PlayerTeleport.fcg`; 3256 bytes, 84 lines.
- **Purpose:** Implements player lifecycle or interaction behavior for `PlayerTeleport`.
- **Graph:** `PlayerTeleport`.
- **Graph fields (direct source):** `TELEPORT_TIME: int = 3000`; `TELEPORT_COOLDOWN: int = 3000`; `_IsTeleporting: bool`; `_IsTeleportCooldown: bool`
- **Event signatures (direct source):** `event OnAwake()`; `event OnPlayerTeleport(player entity<Player>, position Vector3, rotation Vector3)`
- **Working logic (declaration-level):** Declared helper flow: IsTeleporting, RequestTeleportToBase, TeleportToHome, CreateTeleportEffect.
- **Functions, inputs and outputs (direct source signatures):** `func IsTeleporting() bool`; `async func RequestTeleportToBase(isShowPrompt bool)`; `func TeleportToHome()`; `async func CreateTeleportEffect()`
- **Dependencies:** `import "Player.fcc" as Player`; `import "Playable.fcc" as Playable`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Manager/PlayersManager.fcg" as PlayersManager`; `import "../Player/PlayerBase.fcg" as PlayerBase`; `import "../Player/PlayerEntity.fcg" as PlayerEntity`; `import "../_SharedLibs/PetLib/PlayerStateController.fcg" as PlayerStateController`
- **Observed API/engine calls:** `CreateFromPrefab`, `DispatchEventToEntity`, `Teleport`, `WaitForMillisecond`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Player/PlayerTrigger.fcg`

- **Location / full source:** `Assets/Scripts/Player/PlayerTrigger.fcg`; `Assets/Scripts/Player/PlayerTrigger.fcg`; 903 bytes, 27 lines.
- **Purpose:** Implements player lifecycle or interaction behavior for `PlayerTrigger`.
- **Graph:** `PlayerTrigger`.
- **Graph fields (direct source):** `_Owner: entity<Player>`
- **Event signatures (direct source):** `event OnTriggerEnter(target entity<Entity>)`; `event OnTriggerLeave(target entity<Entity>)`
- **Working logic (declaration-level):** Declared helper flow: SetOwner.
- **Functions, inputs and outputs (direct source signatures):** `func SetOwner(owner entity<Player>)`
- **Dependencies:** `import "List.fcc" as List`; `import "Physics.fcc" as Physics`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`
- **Observed API/engine calls:** `DispatchEventToEntity`, `GetAllPlayers`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

### `Assets/Scripts/Utils`

#### `Assets/Scripts/Utils/BigNumberHandler.fcg`

- **Location / full source:** `Assets/Scripts/Utils/BigNumberHandler.fcg`; `Assets/Scripts/Utils/BigNumberHandler.fcg`; 17447 bytes, 524 lines.
- **Purpose:** Provides shared helper behavior for `BigNumberHandler`.
- **Graph:** `BigNumberHandler`.
- **Graph fields (direct source):** `MONEY_SUFFIX: Map<int, string> = Map<int, string>{`
- **Event signatures (direct source):** none
- **Working logic (declaration-level):** Declared helper flow: ConvertIntToList, ConvertFloatToList, AddNumber, GetMaxLength2Num, ConvertStringToListNum, ConvertListNumToString, ConvertStringLikeToFormatString, ConvertMoneyRankValueToMoneyFormat, ConvertMoneyRankValueToListNum.
- **Functions, inputs and outputs (direct source signatures):** `func MultiplyListIntByFloat(num List<int>, multiplier float) List<int>`; `func ConvertIntToList(num int) List<int>`; `func ConvertFloatToList(num float) List<int>`; `func ShortenNumber(num List<int>)`; `func CleanNumber(num List<int>)`; `func AddNumber(num1 List<int>, num2 List<int>) List<int>`; `func SubtractNumber(num1 List<int>, num2 List<int>) List<int>`; `func MultiplyNumber(num1 List<int>, num2 List<int>) List<int>`; `func MultiplierNumber(num1 List<int>, multiplier float)`; `func FixBlankList(num List<int>)`; `func GetMaxLength2Num(num1 List<int>, num2 List<int>) int`; `func CompareListNum(a List<int>, b List<int>) int`; `func ConvertStringToListNum(s string) List<int>`; `func ConvertListNumToString(num List<int>) string`; `func ToDisplayFormat(num List<int>) string`; `func ToDisplayFormatHasComma(num List<int>) string`; `func DivideListNumToFloat(num1 List<int>, num2 List<int>) float`; `func MultiplyListIntByFloatV2(bigNum List<int>, multiplier float) List<int>`; `func ConvertStringLikeToFormatString(like string) string`; `func ConvertMoneyRankValueToMoneyFormat(moneyRankScore int) string`; `func ConvertMoneyRankValueToListNum(moneyRankScore int) List<int>`
- **Dependencies:** `import "Map.fcc" as Map`; `import "List.fcc" as List`; `import "Math.fcc" as Math`; `import "Player.fcc" as Player`; `import "Convert.fcc" as Convert`; `import "Strings.fcc" as Strings`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Utils/CustomUIUtils.fcg`

- **Location / full source:** `Assets/Scripts/Utils/CustomUIUtils.fcg`; `Assets/Scripts/Utils/CustomUIUtils.fcg`; 5946 bytes, 158 lines.
- **Purpose:** Provides shared helper behavior for `CustomUIUtils`.
- **Graph:** `CustomUIUtils`.
- **Graph fields (direct source):** none
- **Event signatures (direct source):** `event OnTapButton(player entity<Player>, button entity<UIWidgetButton>)`
- **Working logic (declaration-level):** Declared helper flow: HandleTapButton, IsContainButton, HideAllHUDs.
- **Functions, inputs and outputs (direct source signatures):** `async func HandleTapButton(player entity<Player>, button entity<UIWidgetButton>)`; `func IsContainButton(button entity<UIWidget>, player entity<Player>, buttonIdsList List<CustomHudWidgetID>) bool`; `func HideAllHUDs(player entity<Player>)`
- **Dependencies:** `import "Hud.fcc" as Hud`; `import "List.fcc" as List`; `import "Player.fcc" as Player`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Manager/WalletManager.fcg" as WalletManager`; `import "../Player/PlayerTeleport.fcg" as PlayerTeleport`; `import "../Player/PlayerSFXHandler.fcg" as PlayerSFXHandler`; `import "../HUDs/HudMail.fcg" as HudMail`; `import "../HUDs/HudMenu.fcg" as HudMenu`; `import "../HUDs/HudRebirth.fcg" as HudRebirth`; `import "../HUDs/HudLeaderboard.fcg" as HudLeaderboard`; `import "../HUDs/HudPetInteract.fcg" as HudPetInteract`; `import "../HUDs/HudLaserWallInteract.fcg" as HudLaserWallInteract`; `import "../_SharedLibs/CoreLib/DatabaseController.fcg" as DatabaseController`
- **Observed API/engine calls:** `DispatchEventToEntity`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Utils/DataUtils.fcg`

- **Location / full source:** `Assets/Scripts/Utils/DataUtils.fcg`; `Assets/Scripts/Utils/DataUtils.fcg`; 7520 bytes, 224 lines.
- **Purpose:** Provides shared helper behavior for `DataUtils`.
- **Graph:** `DataUtils`.
- **Graph fields (direct source):** none
- **Event signatures (direct source):** none
- **Working logic (declaration-level):** Declared helper flow: .
- **Functions, inputs and outputs (direct source signatures):** `func ListIntToString(list List<int>) string`; `func StringToListInt(s string) List<int>`; `func ListListIntToString(list List<List<int>>) string`; `func StringToListListInt(s string) List<List<int>>`; `func StringToListString(s string) List<string>`; `func ListIntToStringUseComma(list List<int>, comma string) string`; `func StringToListStringV2(s string, comma string) List<string>`; `func StringToListIntV2(data string, comma string) List<int>`; `func StringToKeyValue(data string) List<string>`; `func StringToIntValue(data string, out var isSuccess bool) int`; `func KeyValueToString(key string, value string)string`; `func ListStringToStringUseComma(list List<string>, comma string)string`; `func JsonStringToKeyValue(json string) Map<string, string>`; `func JsonStringToListKeyValue(json string) List<Map<string, string>>`; `func ListKeyValueToJsonString(listKeyValue List<Map<string, string>>) string`
- **Dependencies:** `import "List.fcc" as List`; `import "Convert.fcc" as Convert`; `import "Strings.fcc" as Strings`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Utils/Hint.fcg`

- **Location / full source:** `Assets/Scripts/Utils/Hint.fcg`; `Assets/Scripts/Utils/Hint.fcg`; 865 bytes, 31 lines.
- **Purpose:** Provides shared helper behavior for `Hint`.
- **Graph:** `Hint`.
- **Graph fields (direct source):** `_TargetX: float`; `_TargetZ: float`; `_FollowEntity: entity`; `_Owner: entity<Player>`
- **Event signatures (direct source):** `event OnAwake()`; `event OnUpdate()`
- **Working logic (declaration-level):** Declared helper flow: SetHintTarget.
- **Functions, inputs and outputs (direct source signatures):** `func SetHintTarget(x float, z float)`
- **Dependencies:** `import "Math.fcc" as Math`; `import "Playable.fcc" as Playable`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Utils/UIUtils.fcg`

- **Location / full source:** `Assets/Scripts/Utils/UIUtils.fcg`; `Assets/Scripts/Utils/UIUtils.fcg`; 4772 bytes, 110 lines.
- **Purpose:** Provides shared helper behavior for `UIUtils`.
- **Graph:** `UIUtils`.
- **Graph fields (direct source):** `ACTIVE_COLOR (inferred) = #FFFFFF`; `DEFAULT_COLOR (inferred) = #111111`
- **Event signatures (direct source):** none
- **Working logic (declaration-level):** Declared helper flow: GetHUDWidget, UpdatePetWidget, UpdatePetWidgetV2.
- **Functions, inputs and outputs (direct source signatures):** `func GetHUDWidget(player entity<Player>, customHud entity<CustomUI>, customUIWidgetId CustomUIWidgetID) entity<UIWidget>`; `func UpdatePetWidget(player entity<Player>, petWidget entity<UIWidget>, petId int, mutationId int, isShowOwned bool, isShowName bool, isShowMutation bool)`; `func UpdatePetWidgetV2(player entity<Player>, petWidget entity<UIWidget>, petId int, mutationId int, isShowOwned bool, isShowRarity bool, isShowName bool, isShowMutation bool)`; `func FormatTime(time int) string`
- **Dependencies:** `import "Hud.fcc" as Hud`; `import "List.fcc" as List`; `import "Convert.fcc" as Convert`; `import "Strings.fcc" as Strings`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import Res from "EditorGenLib.fcc"`; `import "./BigNumberHandler.fcg" as BigNumberHandler`; `import "../Configs/MobConfig.fcg" as MobConfig`; `import "../Configs/MutationConfig.fcg" as MutationConfig`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Utils/UIUtilsClient.fcg`

- **Location / full source:** `Assets/Scripts/Utils/UIUtilsClient.fcg`; `Assets/Scripts/Utils/UIUtilsClient.fcg`; 2068 bytes, 73 lines.
- **Purpose:** Provides shared helper behavior for `UIUtilsClient`.
- **Graph:** `UIUtilsClient`.
- **Graph fields (direct source):** `DEFAULT_LANGUAGE: int = 1`; `CHARACTER_WIDTH: Map<int, float> = Map<int, float>{`
- **Event signatures (direct source):** none
- **Working logic (declaration-level):** Declared helper flow: GetHUDWidget, GetWidgetLabelScale.
- **Functions, inputs and outputs (direct source signatures):** `func GetHUDWidget(customHud entity<CustomUI>, customUIWidgetId CustomUIWidgetID) entity<UIWidget>`; `func GetWidgetLabelScale(textLength int, out var width int, out var height int)`
- **Dependencies:** `import "Hud.fcc" as Hud`; `import "Map.fcc" as Map`; `import "Math.fcc" as Math`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`
- **Observed API/engine calls:** none from compact call list; inspect full source for others
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Utils/UIWidgetButtonUtils.fcg`

- **Location / full source:** `Assets/Scripts/Utils/UIWidgetButtonUtils.fcg`; `Assets/Scripts/Utils/UIWidgetButtonUtils.fcg`; 317 bytes, 11 lines.
- **Purpose:** Provides shared helper behavior for `UIWidgetButtonUtils`.
- **Graph:** `UIWidgetButtonUtils`.
- **Graph fields (direct source):** none
- **Event signatures (direct source):** `event OnTapped(player entity<Player>)`
- **Working logic (declaration-level):** No function declaration parsed.
- **Functions, inputs and outputs (direct source signatures):** none
- **Dependencies:** `import "Hud.fcc" as Hud`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`
- **Observed API/engine calls:** `DispatchEventToEntity`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Utils/UIWidgetButtonUtilsClient.fcg`

- **Location / full source:** `Assets/Scripts/Utils/UIWidgetButtonUtilsClient.fcg`; `Assets/Scripts/Utils/UIWidgetButtonUtilsClient.fcg`; 336 bytes, 12 lines.
- **Purpose:** Provides shared helper behavior for `UIWidgetButtonUtilsClient`.
- **Graph:** `UIWidgetButtonUtils`.
- **Graph fields (direct source):** none
- **Event signatures (direct source):** `event OnTapped(player entity<Player>)`
- **Working logic (declaration-level):** No function declaration parsed.
- **Functions, inputs and outputs (direct source signatures):** none
- **Dependencies:** `import "Hud.fcc" as Hud`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`
- **Observed API/engine calls:** `DispatchEventToEntity`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).

#### `Assets/Scripts/Utils/WeightedRandom.fcg`

- **Location / full source:** `Assets/Scripts/Utils/WeightedRandom.fcg`; `Assets/Scripts/Utils/WeightedRandom.fcg`; 7067 bytes, 223 lines.
- **Purpose:** Provides shared helper behavior for `WeightedRandom`.
- **Graph:** `WeightedRandom`.
- **Graph fields (direct source):** `FLOAT_TOLERANCE: float = 0.001`; `MAX_POOL_PET_COUNT: int = 1200`; `MYTHIC_SPAWN_START: int = 300`; `MYTHIC_SPAWN_END: int = 400`; `DIVINE_SPAWN_START: int = 900`; `DIVINE_SPAWN_END: int = 1000`; `_PetWeight: List<float>`; `_RarityWeight: Map<RarityEnum, Map<int, float>>`; `_TopTierRarityWeight: Map<RarityEnum, Map<int, float>>`; `_MutationWeight: List<float>`; `_IsInit: bool`; `_QueuePetIds: List<int>`; `_QueueMutationIds: List<int>`
- **Event signatures (direct source):** `event OnAwake()`
- **Working logic (declaration-level):** Declared helper flow: GetRandomWeightedIndex, GetPetRandomID, CalculatePetWeight, GetMutationRandomID, CalculateMutationWeight, GetPetRandomIDByRarity, CalculateRarityWeight.
- **Functions, inputs and outputs (direct source signatures):** `func EnqueuePetID(petId int)`; `func EnqueueMutationID(mutationId int)`; `func GetRandomWeightedIndex(weights List<float>) int`; `func GetPetRandomID() int`; `func CalculatePetWeight(petCount int)`; `func GetMutationRandomID() int`; `func CalculateMutationWeight(mutationCount int)`; `func GetPetRandomIDByRarity(rarity RarityEnum) int`; `func CalculateRarityWeight(petCount int)`
- **Dependencies:** `import "Map.fcc" as Map`; `import "List.fcc" as List`; `import "Math.fcc" as Math`; `import "Convert.fcc" as Convert`; `import "CSVData.fcc" as CSVData`; `import "StdLibrary.fcc" as StdLib`; `import "EditorGenLib.fcc" as EditorLib`; `import "../Configs/MobConfig.fcg" as MobConfig`; `import "../Configs/MutationConfig.fcg" as MutationConfig`
- **Observed API/engine calls:** `LogError`
- **Outputs / side effects:** See each function/event body in the full source link; this index does not paraphrase every branch.
- **Limitations / possible errors:** No runtime, build or tests were run. Null/empty-state handling, remote result status handling, bounds assumptions and platform behavior require source review; any verified concern is listed in [known issues](../troubleshooting/known-issues.md).


