# Components and enums

**Observed by read-only Craftland Studio definition catalog.** This is not a complete description of built-in engine components.

## Complete project-owned custom components (18)

| Component | Editor-label properties |
|---|---|
| `Floor1` | `NameBanner: Entity` |
| `Base` | `Floor1`, `CollectZone`, `DisplayZone`, `LaserWall`, `Spawn`, `Multiplier`, `ProtectSlot`: Entity; `Owner: Player` |
| `Mob` | `MobModel`, `MobDescription`, `MobRarityRing`: Entity |
| `MobParade` | `trigger`, `mobPlace`: Entity |
| `MobDisplay` | `MobDisplayModelHolder`, `MobDisplayTriggerHolder`, `MobDisplayModelEntity`: Entity; `Decoration: ListT_Entity` |
| `MobModelPlace` | `modelEntity: Entity` |
| `MobDescriptionPlace` | `descriptionEntity: Entity` |
| `MobPlace` | `mobEntity: Entity` |
| `LaserWall` | `WallPhysicalBlock`, `SwitchTrigger`, `SwitchTimerText`, `WallPhysicalBlock2`, `WallPhysicalBlock3`, `Wall1`, `Wall2`, `Wall3`: Entity; `UnlockTrigger: ListT_Entity` |
| `ParentEntity` | `parentEntity: Entity` |
| `MobStealing` | `modelPlace: Entity` |
| `NewMobDescription` | `Mutation`, `Rarity`, `General: Entity` |
| `ConfirmYesBtn` | no properties listed |
| `ConfirmNoBtn` | `entity: Entity`; one attached ECA script record |
| `MobRarityRing` | `RingEffect: Entity` |
| `MobMutation` | `GoldenEffect`, `FrozenEffect`, `MagmaEffect: Entity` |
| `PlayerCustomTrigger` | `owner: Player`; one attached ECA script record |
| `CollectTriggerHolder` | `trigger`, `displayText`, `decorateBtn: Entity` |

## Partial/editor definitions (7)

`CustomLevelObject`, `Component`, `Collider`, `CustomHud`, `HudButtonWidget`, `HudEmptyWidget`, `AimableEntity`. Extraction classifies them as partial editor extensions/definitions, not complete project-authored schemas.

## Project-owned enums (17)

`MobConfigEnum`, `MutationConfigEnum`, `RebirthConfigEnum`, `RarityEnum`, `MutationEnum`, `DataType`, `HudDepth`, `LeaderboardType`, `RebirthRewardType`, `CurrencyType`, `CustomStatusCode`, `DatabaseType`, `ActionType`, `PlayerState`, `PetState`, `RequestParameter`, `ButtonEnum`.

The extraction reports underlying type `Int` except `RarityEnum`, `DatabaseType`, and `ActionType`, which use `String`. Exact enum members should be taken from the original source/generated symbols, not reconstructed from these names. No project-owned custom events were returned. Names/properties are catalog metadata, not proof of runtime attachment/behavior.

## Sources

- `Craftland-Extraction/05_CRAFTLAND_KNOWLEDGE.md`
- `Craftland-Extraction/08_API_AND_INTEGRATIONS.md`
