# Gameplay systems

**Evidence scope:** source review summarized by the extraction; no gameplay runtime/playtest validation was run.

## Player/base lifecycle and spawn

`GlobalBase.InitBaseList` reads the registered `EResSceneMainScene.BaseList`, and takes each base group's first child as a base. `GlobalBase.SetBasePlayer` assigns an available base; `PlayerBase` binds it, sets floor/name/display zones, exposes the base `Spawn`, and computes income. The call in `GlobalBase.OnPlayerJoin` is commented out; the active documented assignment path is `RebirthManager.LoadRebirthData` after player data loads. `PlayerTeleport.TeleportToHome` uses the base spawn with a one-unit vertical offset. Exact runtime ordering is not playtested.

## Pet data, display, and economy

`PetsManager` tracks pet IDs, mutations, accumulated balances, interactability, capacity and held/awaiting counts; creates visuals from the registered Mob prefab; and persists pet fields through Craftland Data Storage. The source summary reports balance accrual every second, capped to one hour; offline accrual applies five elapsed seconds as one online second. Collection transfers balance to wallet; selling pays half the configured mob price. `PlayerBase.GetBaseIncome` combines pet production with mutation and rebirth multipliers.

## Parade and weighted selection

`PetParadeManager` manages parade pet spawning/movement, pool returns, purchase requests, purchase condition checks and processing. The source references spawn timing as `GlobalConfig._MobSpawnInterval / 2`. `WeightedRandom` exposes weighted pet/mutation/rarity selection and queue helpers. Do not infer distribution properties or runtime rates beyond source statements.

## Stealing and state controls

`StealManager` validates requests, player/pet state and eligibility, coordinates pet-state locking/transfer, changes visuals and prompts, and handles success/failure/disconnect/teleport paths. Related modules include `PetMutex`, `PetStateController`, `PlayerStateController`, `ValidationController`, `PetsManager`, and interaction HUD/controller scripts. Static concerns are in [known-issues.md](../troubleshooting/known-issues.md); this is not a security or exploit test.

## Wallet, rebirth, and ranking

`WalletManager` holds balance/multiplier operations, large values use `List<int>` and `BigNumberHandler`, and `HudWallet` presents changes. `RebirthManager` loads/stores levels, validates conditions, resets progression-related state and applies configured base/capacity/floor/lock/name/multiplier state. Its declared unlock/eligibility helpers include swaps, hatching, dust, fusion, gift code, portals, pet following, and rarity-gated stealing; conditions are source-defined and not playtested.

There are two leaderboard paths: `LeaderboardManager` reads/writes persistent `IncomeRank` and `WealthRank`; `GlobalLeaderboard` builds a live match ranking every 10 seconds during the in-progress phase, scoring wallet balance plus configured mob price for held pets and dispatching formatted rows to clients.

## Player movement and interaction

`PlayerEntity` applies configured run speed, equips a baseball bat, sets hit-fly response and temporary immunity, and revives after five seconds following elimination. `PlayerTeleport` uses three-second transition/cooldown intervals according to the source summary. `PlayerInteract`, trigger scripts and HUD controllers coordinate proximity/interaction.

## Script relationships

See [script-relationships.md](../scripting/script-relationships.md) and [fc-script-index.md](../scripting/fc-script-index.md).

## Sources

- `Craftland-Extraction/04_SCRIPT_DOCUMENTATION.md` (flow summaries and script declarations)
- `Craftland-Extraction/05_CRAFTLAND_KNOWLEDGE.md`
- `Craftland-Extraction/08_API_AND_INTEGRATIONS.md`
