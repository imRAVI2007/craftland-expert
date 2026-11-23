# Prefab overview

The editor catalog reported 32 prefab assets: 27 project prefabs plus five built-in/library read-only resources. Each of the 27 local prefab entity trees was read through Craftland Studio. Reported counts include the returned root, consistent with editor entity-count behavior described in the extraction. Structure/bindings were observed; runtime behavior and every serialized property were not validated.

The largest local trees are `Base.prefab` (195 entities), `DisplayZone.prefab` (127), `Floor3.prefab` (55), `LaserWall.prefab` (36), `Floor2.prefab` (27), and `Floor1.prefab` (23). `Base.prefab` binds collect/floor/display/base-trigger/laser-wall/unlock/kick/switch roles. `Mob.prefab` binds mob, mutex, model, description and rarity-ring behavior. The complete list and script bindings are in [prefab-reference.md](prefab-reference.md).

One project concern: `MobFollow.prefab` and `MobFollowing.prefab` each have an unresolved script reference ID in the editor catalog; its origin/runtime resolution is unknown. See [known issues](../troubleshooting/known-issues.md).

## Sources

- `Craftland-Extraction/05_CRAFTLAND_KNOWLEDGE.md`
- `Craftland-Extraction/08_API_AND_INTEGRATIONS.md`
- `Craftland-Extraction/02_COMPLETE_FILE_INDEX.md`
