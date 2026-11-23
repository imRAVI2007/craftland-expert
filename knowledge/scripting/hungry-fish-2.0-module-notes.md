# Hungry Fish 2.0: detailed notes for 18 important modules

These summaries paraphrase source review recorded in `D:\My project (6)\Craftland-Extraction\04_SCRIPT_DOCUMENTATION.md`. They are not runtime validation. Exact signatures/imports for the 93 scripts are in the [script index CSV](../../sources/hungry-fish-2.0/indexes/SCRIPT_INDEX.csv). Original source paths are relative to `D:\My project (6)`.

## `Assets/_Scripts/Player/AttackController.fcg`

Server graph stores spawn positions registered by `Components/SpawnManager.fcg`. On revive it dispatches revive events, teleports to `GetSpawnPosition`, resets model/shield state, and queues a defeat-reason tip. Spawn selection chooses the point whose nearest-other-player distance is greatest. No explicit empty-list fallback is present in the reviewed source; runtime consequence unknown.

## `Assets/_Scripts/Player/PlayerAttack.fcg`

Client graph handles attack completion for the local player, updating streak, score, kill score, experience, sound, speed/energy, shield checks, possible bonus coins, and water VFX. Random calls include `(10,31)` for coin amount and `(0,101)` for chance. `RandomInt` endpoint semantics and runtime distribution are unverified. A missed-attempt counter can grant a later coin when it reaches `Round(100 / killCoinRate)`.

## `Assets/_Scripts/Global/FoodManager.fcg`

Client graph creates 70 food entries on round start at random x/z positions in `[-50,50]`, y=6, with a frame yielded between creations. Hidden pickups are deactivated, wait the reset duration, relocate and reactivate. Pickup flow grants configured energy modified by `manaFood`, experience adjusted by `expFood`, score, and possible coins. Entries are destroyed at result phase. Runtime random endpoints are unverified.

## `Assets/_Scripts/Global/CoinManager.fcg`

Client graph creates 30 coin entries on round start using the same documented coordinate range and height. Hidden coins are disabled, wait, relocate, and reactivate. Collection grants configured currency and tracks earned coin; tracked entries are destroyed at result phase. Runtime random endpoints are unverified.

## `Assets/_Scripts/Player/PlayerLevel.fcg`

Client graph initializes level/experience from `PlayerController` configuration at `OnSetPlayerConfig`. Level-up increments level, updates threshold/UI, scales the player and mouth/hole, calls the wallet randomized-fish bonus, and updates the level title. The extracted loop description gives threshold terms as rounded `60 * 1.4^i`, for `i=0..level-1`, using the project's documented half-open loop convention.

## `Assets/_Scripts/Player/PlayerScore.fcg`

Client graph stores per-player round score, sorts ranking data, updates match/global ranking interfaces, and awards rank coins. The extracted formula is `(player count - rank index) * 50 + round(score / 10)`; configured score rate also applies. `KillStreakGoldFish` receives 10 coins every fifth kill-score increment according to the source summary. Ordering and runtime values were not tested.

## `Assets/_Scripts/Global/ScoreManager.fcg`

Server graph receives score-sync events, removes players on quit, waits five seconds after result phase begins, sends the score map to clients, then calls final upload using `GameResultType.Booyah`. No result upload was exercised.

## `Assets/_Scripts/Player/PlayerWallet.fcg`

Client graph tracks `coin` and match `earnedCoin`, updates wallet UI, rejects subtraction when balance is insufficient, and writes coin state at End phase. Persistence is handled by `PlayerWalletData.fcg`.

## `Assets/_Scripts/Player/PlayerWalletData.fcg`

Reads DataStorage sheet `Wallet`, key `Coin`, retries reads up to ten times while the result is `-1`, initializes absent balance to zero, dispatches loaded balance, then writes. Writes retry `DataStorageTimeout` up to ten times. Final non-timeout error handling is not described as comprehensive and runtime behavior is untested.

## `Assets/_Scripts/Player/PlayerInventoryData.fcg`

Server graph reads sheet `Inventory`, keys `Fish` and `Effect`; retries nil reads up to ten times; defaults to one unlocked item followed by 27 locked fish slots and one unlocked item followed by 10 locked effect slots. It dispatches data to the client and writes; sync events replace lists and persist them. Exact table-length alignment remains a check for source/editor work.

## `Assets/_Scripts/Player/PlayerScoreData.fcg`

Server graph reads lifetime elimination/score values from sheet `Score`, keys `Elimination` and `Score`, retrying zero values up to ten times before sending results and requesting ranking data. Sync writes both values with timeout retries. Because zero may be a valid value, retry consequences are unverified.

## `Assets/_Scripts/Player/PlayerRankingData.fcg`

Server graph reads ranks 1–120 from `KillRanking` and `ScoreRanking`, retries nil values up to ten times, finds the player's rank by stored-name comparison, and uses `120+` if absent. Writes use the built-in leaderboard write for current kill and score totals. Ordering/schema/runtime behavior were not tested.

## `Assets/_Scripts/Player/PlayerLogin.fcg`

Login data is sent to the client. The graph compares day-of-month, advances/wraps a seven-day reward cycle, updates reward states, refreshes reward UI, and sets a red point for any `NotClaimed` entry. At End it syncs state to server. Calendar boundary behavior is untested.

## `Assets/_Scripts/HUD/RewardUI.fcg`

On a valid unlocked, unclaimed reward interaction, the graph marks it claimed, updates persistence, grants its `Amount` as wallet coins, increments match-earned coins, plays coin sound, and sends wallet balance to server. Adjacent TODO comments in this module and `PlayerLogin` do not by themselves prove missing functionality because the summarized calls exist nearby.

## `Assets/_Scripts/Config/FishConfigReader.fcg`

For the local player at round start, reads the selected fish ID, computes a row using `StringUtils.GetFishNumber(fishID) + 1`, casts row values to `List<int>`, sets controller configuration, and dispatches `OnSetPlayerConfig`. Verify the column mapping against `Assets/Config/fish_config.csv` before changing it.

## `Assets/_Scripts/Global/GlobalManager.fcg`

Server graph handles skip-phase and reconnect; a reconnect during Selection sends UI recreation. Exact event ordering and runtime effects are untested.

## `Assets/_Scripts/Components/SpawnManager.fcg`

Server spawn marker registers its position on `OnAwake` and disables itself when the round starts. `AttackController` consumes registered positions; their relationship is source-described, not playtested.

## `Assets/_Scripts/HUD/MatchResultUI.fcg`

Server graph creates a built-in multi-team result HUD at End, sorts players by score, fills score/player/team arrays, and uses `GameResultType.Booyah`. A `JoinNewTeam` call is commented out; there is no evidence it is active.

## Shared limits

Inputs include Craftland phase/player/entity events, component values, project configuration, CSV rows, and DataStorage values. Outputs described include entity state, UI/prefab changes, cross-platform event dispatch, visuals/audio, DataStorage writes, and result uploads. No external web endpoint is established. No builds, playtests, runtime tests, or uploads were performed.
