# Hungry Fish 2.0 scene, UI, and prefab observations

**Status:** Craftland Studio observations recorded by the extraction. They describe captured structure, not runtime behavior.

## Main scene and map

The extraction reports 66 scene objects plus a synthetic root: one weather object, one photo filter, 51 mesh entities, eight preset SpawnBox entities, and five group/empty entities. The eight spawn boxes use x/z values from `-40`, `0`, and `40`, y approximately `5.42`, and scale `10×1×10`. The ground is reported as a collidable mesh with a box collider; its entity scale is `3.25×1×3.25`, collider size `44×6×44`, and local y offset `3`. `SpawnManager.fcg` registers spawn positions on server `OnAwake`.

The inspected extraction does not establish the selected map ID or a complete map-size/terrain profile for this project. Do not infer those from the scene extents. The complete scene/entity settings and all serialized properties were not semantically audited.

## UI

20 `.ui` assets were queried through Craftland Studio. The extracted catalog reports a 1500×750 canvas for inspected roots and counts that exclude roots: `FishSelection` 148, `Test` 75, `KillRanking` 62, `ScoreRanking` 62, `Ranking` 57, `DailyReward` 44, `SpecialSkill` 14, `MatchRanking` 14, `GameStart` 8, `Debug` 6, `Level` 5, `GodState` 5, `Ability` 5, `Energy` 4, `Detail` 4, `Score` 4, `Wallet` 4, `Tip` 3, `Broadcast` 2, and `KillStreak` 2. Names and control notes are from `04_SCRIPT_DOCUMENTATION.md`; current bindings must be confirmed in the editor.

`GameStart.ui` contains a 30-second start message while `ProjectSettings/Workflow.wfl` has five-second game-start phase data. This is an observed discrepancy; precedence and runtime meaning are unknown, so it is not labeled a defect.

## Prefabs and PlayerData

70 project prefabs were structurally queried, grouped as Currency (3), Effect (11), Fishes (35), Food (13), Mouth (3), and Weapon (5). Extraction notes describe fish roots with avatar/animation-controller/collider structures and food/currency with mesh, collider, and rigidbody components. Attachments recorded include `HoleTrigger.prefab` → `Components/HoleTrigger.fcg`, `MouthTrigger.prefab` → `Components/MouthTrigger.fcg`, `Mine.prefab` → `Components/Mine.fcg`, `PosionField.prefab` → `Components/Posion.fcg`, `Rocket.prefab` and `WaterRocket.prefab` → `Components/Rocket.fcg`, `Snow.prefab` → `Components/Snow.fcg`, and `WaterRocket.prefab` → `Components/WarningTrigger.fcg`.

27 `Assets/PlayerData/**/*.playerdata` definitions were read through Craftland Studio. All are reported as `UGCPlayerEntity` with gender value 0 and scale 1.5; 26 point at fish prefabs and use three named action maps, while the fishbone entry differs. These are player-entity archetype definitions, not proof of per-user persistence. Specific animation/resource details remain source-project-specific.

**Sources:** `D:\My project (6)\Craftland-Extraction\04_SCRIPT_DOCUMENTATION.md`, `05_CRAFTLAND_KNOWLEDGE.md`, and `14_UNKNOWN_INFORMATION.md`.
