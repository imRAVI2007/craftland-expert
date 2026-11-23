# Prefab reference

All paths are relative to the original project (`D:\My project (5)`), not this knowledge repository. Entity counts and bound roles are editor-observed. `none` means no bound script role was listed in the extraction, not proof of no behavior through other mechanisms.

| Prefab | Entities | Bound script roles |
|---|---:|---|
| `Assets/Prefabs/Base/Base.prefab` | 195 | CollectZoneTrigger, Floor1Handler, MobDisplayHandler, MobBaseTrigger, LaserWallHandler, UnlockBaseTrigger, KickTrigger, LaserWallSwitchTrigger |
| `Assets/Prefabs/Base/BaseName.prefab` | 3 | Floor1Handler |
| `Assets/Prefabs/Base/CollectZone.prefab` | 3 | CollectZoneTrigger |
| `Assets/Prefabs/Base/DisplayZone.prefab` | 127 | MobDisplayHandler, MobBaseTrigger |
| `Assets/Prefabs/Base/Floor1.prefab` | 23 | none listed |
| `Assets/Prefabs/Base/Floor2.prefab` | 27 | none listed |
| `Assets/Prefabs/Base/Floor3.prefab` | 55 | none listed |
| `Assets/Prefabs/Base/InvisibleLaserWall.prefab` | 2 | none listed |
| `Assets/Prefabs/Base/LaserWall.prefab` | 36 | LaserWallHandler, UnlockBaseTrigger, KickTrigger, LaserWallSwitchTrigger |
| `Assets/Prefabs/Base/Single.prefab` | 7 | MobDisplayHandler, MobBaseTrigger |
| `Assets/Prefabs/Base/SingleTest.prefab` | 11 | MobBaseTrigger |
| `Assets/Prefabs/Base/Stair.prefab` | 4 | none listed |
| `Assets/Prefabs/Hint.prefab` | 1 | Hint |
| `Assets/Prefabs/Mob/Mob.prefab` | 9 | MobHandler, PetMutex, MobModelHandler, MobDescriptionHandler, MobRarityRingHandler |
| `Assets/Prefabs/Mob/MobDescription.prefab` | 1 | MobDescriptionHandler |
| `Assets/Prefabs/Mob/MobFollow.prefab` | 14 | MobHandler, MobModelHandler, MobDescriptionHandler, unresolved reference `emjscp8lpru-mno4xs1s-ucomtm2qgx8` |
| `Assets/Prefabs/Mob/MobFollowing.prefab` | 15 | MobHandler, MobModelHandler, MobDescriptionHandler, unresolved reference `emjscp8lpru-mno4xs1s-ucomtm2qgx8` |
| `Assets/Prefabs/Mob/MobModel.prefab` | 2 | MobModelHandler |
| `Assets/Prefabs/Mob/MobParade.prefab` | 11 | MobParadeHandler, MobParadeTrigger, MobHandler, PetMutex, MobModelHandler, MobRarityRingHandler, MobDescriptionHandler |
| `Assets/Prefabs/Mob/MobRarityRing.prefab` | 2 | MobRarityRingHandler |
| `Assets/Prefabs/Mob/NewMobDescription.prefab` | 4 | MobDescriptionHandler |
| `Assets/Prefabs/MutationEffects/FronzenEffect.prefab` | 1 | none listed |
| `Assets/Prefabs/MutationEffects/GoldenEffect.prefab` | 1 | none listed |
| `Assets/Prefabs/MutationEffects/MagmaEffect.prefab` | 1 | none listed |
| `Assets/Prefabs/PlayerTrigger.prefab` | 1 | PlayerTrigger |
| `Assets/Prefabs/TeleportEffect.prefab` | 2 | TeleportEffect |
| `Assets/Prefabs/TextOverHead.prefab` | 3 | none listed |

`ChristmasTree.prefab.meta` exists but the extraction's 27-local-prefab catalog/tree list does not include a `ChristmasTree.prefab` source file. Do not count the metadata sidecar as a prefab tree.

## Component definitions

The editor reported 18 complete project-owned custom component definitions, seven partial/editor-provided definitions, 17 project-owned enums, and no project-owned custom events. Property lists and caveats are in [UI components and definitions](../ui/ui-components.md).

## Sources

- `Craftland-Extraction/05_CRAFTLAND_KNOWLEDGE.md`
- `Craftland-Extraction/02_COMPLETE_FILE_INDEX.md`
