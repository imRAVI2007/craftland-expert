# Project comparison: Steal A Pet Template and Hungry Fish 2.0

This comparison is evidence-limited to two different extracted projects. A shared pattern across two samples is not automatically a universal Craftland rule. Keep each project's scripts, configs, IDs, and editor observations separate.

| Area | Project 5: Steal A Pet Template (`D:\My project (5)`) | Project 6: Hungry Fish 2.0 (`D:\My project (6)`) |
|---|---|---|
| Feature loop | Bases, pet/mob collection and display, stealing, wallet, rebirth, parade. | Fish selection/survival, food/coin pickups, combat/skills, levels, login rewards, scores/results. |
| FC source | 63 scripts under `Assets/Scripts/`; its own [index](../scripting/fc-script-index.md). | 93 scripts under `Assets/_Scripts/`; [separate index](../scripting/hungry-fish-2.0-script-reference.md). |
| CSV/config | `globalConfig.csv`, `mob.csv`, `mutation.csv`, `rebirth.csv`, `Localization/key.csv`; static mutation column mismatch recorded. | `Assets/Config/fish_config.csv` and `Assets/Localization/key.csv`; additional prices/reward/class values are described in FC config modules, not inferred CSVs. |
| Scene/map | One `MainScene.scene`; active map ID 10, flat 100m×100m ground at Y=0, six base groups. | One main scene; eight observed spawn boxes and ground collider settings. Selected map ID/full map profile not established in reviewed summary. |
| Prefabs | 27 local prefab trees; base/pet/display/laser-wall roles. | 70 project prefabs grouped as Currency, Effect, Fishes, Food, Mouth, Weapon. |
| UI | 10 local UI trees; pet interaction, rebirth, wallet, leaderboard, prompt/menu. | 20 local UI trees; fish selection, abilities, daily rewards, kill/score rankings, match/result displays. |
| Player data / persistence | Project controllers and DataStorage abstractions for wallet, pet inventory/state, rebirth and leaderboard. `DatabaseController` coordinates database-ready/saved lifecycle events for other modules. | 27 PlayerData entity definitions plus separate DataStorage sheets `Wallet`, `Inventory`, `Login`, `Score`; feature-specific data graphs make reads/writes and retries. Do not confuse entity archetypes with stored player records. |
| Leaderboards | Persistent `LeaderboardManager` plus live `GlobalLeaderboard` path, with different interfaces/flows. | Persistent kill/score ranking in `PlayerRankingData` plus match score/ranking and result upload paths. |
| ECA | One read-only built-in `Spawn Point Auto Closer` graph in the extraction. | Three project ECA graphs (`NumberUtils`, `Test`, `TestServer`) observed through Studio; utility/test-like, runtime not tested. |
| Instruction archive | 17 historical sources in original project extraction, including two human tutorials; no saved AI prompts. | 14 local instruction copies / 13 unique texts, including a duplicated asset rule; no saved user prompt templates identified. |

## Reusable techniques vs project-specific implementations

**Repeated evidence in both projects:** Craftland FC `.fcg` source imports `.fcc` libraries; editor-owned serialized assets are inspected through Craftland Studio; project behavior is cross-linked across script, data, prefab/UI, and scene records; DataStorage calls are Craftland platform usage, not proof of a custom web/database backend. Treat these as observed patterns in two projects only.

**Keep project-specific:** game mechanics, FC event names, data sheet schemas, CSV columns, player-state logic, ranking calculations, asset counts, UI layouts, component definitions, spawn placement, and editor observations. A script with a matching filename/name is not evidence of equivalent behavior.

## Contradictions and age/version boundaries

- Project 5 has a likely static mutation CSV/enum access mismatch; it is not evidence about Project 6.
- Project 6 has `GameStart.ui` 30-second text vs five-second workflow data and conflicting values across workflow/mod settings; precedence/runtime effect are unknown. These do not imply a Project 5 issue.
- Project 5 is based on an extraction with a different gameplay template and asset inventory. Project 6 records version `1.19.4689915` and managed instruction package `0.5.3`; this does not establish Project 5's editor version.

## Sources

- Project 5: `Craftland-Extraction/01_PROJECT_OVERVIEW.md`, `04_SCRIPT_DOCUMENTATION.md`, `05_CRAFTLAND_KNOWLEDGE.md`, `14_UNKNOWN_INFORMATION.md`.
- Project 6: `D:\My project (6)\Craftland-Extraction\01_PROJECT_OVERVIEW.md`, `04_SCRIPT_DOCUMENTATION.md`, `05_CRAFTLAND_KNOWLEDGE.md`, `08_API_AND_INTEGRATIONS.md`, `14_UNKNOWN_INFORMATION.md`.
