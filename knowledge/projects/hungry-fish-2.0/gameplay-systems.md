# Hungry Fish 2.0 gameplay systems

**Evidence label:** source-described and editor-observed project implementation; runtime behavior is unverified.

## Fish selection, configuration, and abilities

`Config/FishConfigReader.fcg` reads the selected fish ID, derives a row from `Assets/Config/fish_config.csv`, casts the row values to `List<int>`, configures the player controller, and dispatches `OnSetPlayerConfig` for the local player at round start. `PlayerController` has defaults for run/dash speed, mana, regen, score rate, shield/dash durations, mine and rocket costs; fish configuration can override controller values. See the indexed imports and declarations in the project's [FC index](../../scripting/hungry-fish-2.0-script-reference.md). The meaning of each CSV column must be confirmed against the source and current editor data before editing.

## Food, coins, combat, and progression

- `Global/FoodManager.fcg` and `Global/CoinManager.fcg` create 70 and 30 pickup entries on round start, respectively, at random x/z positions in `[-50,50]`, y=6. Hidden pickups are disabled, wait their configured reset interval, relocate, and reactivate. Pickup outcomes update energy, experience, score, or coins through related player modules.
- `Player/PlayerAttack.fcg` handles the local player's attack completion path: streak/score/experience updates, death sound, speed/energy changes, fish shield checks, possible coin rewards, and water effects. Random endpoint semantics are not verified.
- `Player/PlayerLevel.fcg` increments levels, updates its threshold and UI, scales the player/mouth/hole, invokes a wallet randomized-fish bonus, and updates the level title. The extracted source note describes its threshold as the sum of rounded `60 * 1.4^i` terms for `i=0..level-1` using the project's documented half-open loop syntax.
- Kill-streak display/configuration covers streaks 2–7; higher streaks reuse the “unstoppable” label according to the source summary.

## Rewards and match results

`Player/PlayerLogin.fcg` compares day-of-month values, advances/wraps a seven-day reward cycle, synchronizes login state, and drives reward UI refresh. `HUD/RewardUI.fcg` handles a claimed unclaimed reward, wallet updates, sound, and persistence synchronization. `DailyRewardConfig.fcg` lists configured values 50, 75, 100, 125, 150, 200, 300. These are source descriptions; calendar edge cases and runtime rewards were not tested.

`Player/PlayerScore.fcg` tracks round scores and rankings, updates match/global ranking interfaces, and computes a rank reward using `(player count - rank index) * 50 + round(score / 10)` in the extracted narrative. `Global/ScoreManager.fcg` receives score synchronization, removes departing players, waits five seconds after the result phase begins, sends the score map to clients, and calls the built-in `GameResultType.Booyah` result upload. No result upload was exercised. See the separate [leaderboard reference](../../leaderboards/hungry-fish-2.0.md).

## Spawn and reconnect

`Components/SpawnManager.fcg` registers spawn positions on server `OnAwake` and disables its marker at round start. `Player/AttackController.fcg` selects a spawn point maximizing distance to the nearest other player, then revives/teleports and resets player state. There is no explicit empty-spawn-list fallback in the reviewed source. `Global/GlobalManager.fcg` handles skip-phase and reconnect behavior; a reconnect during Selection sends UI recreation.

## Practical use and limits

For changes, trace the relevant `.fcg` module with its CSV/config, UI or prefab bindings, and current project/editor schema. Do not transfer the fish game’s constants, events, folder layout, or UI wiring to the `Steal A Pet Template` project. The detailed notes for 18 modules are in [hungry-fish-2.0-module-notes.md](../../scripting/hungry-fish-2.0-module-notes.md). Source: `D:\My project (6)\Craftland-Extraction\04_SCRIPT_DOCUMENTATION.md` and `05_CRAFTLAND_KNOWLEDGE.md`.
