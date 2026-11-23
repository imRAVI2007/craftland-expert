# Map and game-mode settings

## Current project state

- `Assets/Scenes/MainScene.scene` is the one local scene. Editor scene grounding reports current map ID **10**, a flat map with ground at world Y=0, surrounded by sea, with ground and no terrain. The map list reports 100 m × 100 m.
- The scene contains six named base groups (`Base1`…`Base6`) and named/repeated objects including `Spawn`, `BaseName`, and `UnlockBaseTrigger`.
- `ProjectSettings/PlayerSetting.asset` reports `custom_game_mode=0`, map-bound size 25–100 and circle size 90–180. The numeric mode enum was not decoded; do not assign a mode name.
- `WorkflowMod.asset` has game phases; `GlobalMod.asset` has match configuration. Numeric/raw fields are not described beyond the extraction evidence.
- Other editor map choices are not the active scene: map 25 is 50 m flat at Y=-0.3; map 32 is 200 m empty/no ground; other selectable maps have varying terrain. Never transfer current-map Y=0 to another map.
- `GlobalBase` uses registered base-list data and `PlayerBase` uses each assigned base's `Spawn`. See gameplay lifecycle notes for assignment timing.

## Validation boundary

Map metadata and hierarchy were editor-observed, but no gameplay launch or spawn playtest occurred. No game mode name is inferred from `custom_game_mode=0`. See [scene structure](../maps/scene-structure.md).

## Sources

- `Craftland-Extraction/05_CRAFTLAND_KNOWLEDGE.md`
- `Craftland-Extraction/08_API_AND_INTEGRATIONS.md`
- Original project-relative: `Assets/Scenes/MainScene.scene`, `ProjectSettings/PlayerSetting.asset`, `ProjectSettings/WorkflowMod.asset`, `ProjectSettings/GlobalMod.asset`
