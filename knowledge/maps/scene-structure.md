# Scene structure

## MainScene

The only local scene is `Assets/Scenes/MainScene.scene`. Editor reports 1,186 child entities. Six 200-row pages returned 1,187 unique entity IDs because the rows included a synthetic `Scene` root plus those children. Composition including root: 379 `MeshEntity`, 673 `EmptyEntity`, 132 `PresetItem`, and one each of `Scene`, `WeatherEntity`, `PhotoFilterEntity` (1,187 total).

The editor tree includes six base groups `Base1`–`Base6` and repeated children such as `Base`, `Spawn`, `BaseName`, and `UnlockBaseTrigger`. These names/tree observations do not by themselves establish player assignment/spawn semantics; see [map settings](../gameplay/map-settings.md) and gameplay sources.

## Serialized content boundary

The scene tree was read via Craftland Studio. Every one of its 1,186 children and every serialized property were not semantically reviewed. No `aiPrompt` values were found in the scene, 27 local prefab trees, or 10 UI trees using the editor search recorded in the extraction. That result is scoped to this snapshot.

## Sources

- `Craftland-Extraction/05_CRAFTLAND_KNOWLEDGE.md`
- `Craftland-Extraction/08_API_AND_INTEGRATIONS.md`
- `Craftland-Extraction/14_UNKNOWN_INFORMATION.md`
