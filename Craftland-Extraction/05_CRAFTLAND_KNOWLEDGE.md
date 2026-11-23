# Craftland Project Knowledge

## Evidence classes

- **Project-authored**: `Tutorial (EN).md`, its Vietnamese counterpart, `AGENTS.md`, `.craftland/agents/`, `.github/instructions/`, FC source/CSV/config.
- **Editor-observed**: read-only Craftland Studio MCP catalog and entity metadata.
- **Assumption**: anything inferred without a source or editor record; explicitly marked below.

## Verified project-specific facts

- The project is a Craftland UGC game template named **Steal A Pet Template** in both tutorials.
- A single local scene, `Assets/Scenes/MainScene.scene`, is present. Craftland Studio's `entityCount` reports 1,186; reading all pages returned 1,187 unique IDs because the returned rows include the scene root plus the 1,186 children.
- Scene composition including root: 379 `MeshEntity`, 673 `EmptyEntity`, 132 `PresetItem`, plus one each of `Scene`, `WeatherEntity`, and `PhotoFilterEntity` (1,187 rows). The root explains the one-row difference from `entityCount`.
- Project source implements pet collection/display, base ownership/locks, interaction, stealing, wallet/economy, rebirth, mutations, pet parade, player movement/interactions/teleport, and HUDs. This list is supported by file names and FC declarations; per-feature flow is documented in 04.
- Data authoring is organized around CSV files: `Assets/CSV/globalConfig.csv`, `mob.csv`, `mutation.csv`, `rebirth.csv`; localization is in `Assets/Localization/key.csv`.
- Current table contents: `globalConfig.csv` has one configuration row (`MobSpawnInterval=6000`, `PlayerMoveSpeed=1.0`, `PlayerStealSpeed=0.35`, `PlayerHitInvulnerableTime=3000`, `DurationRiseSpeed=30000`, `SpeedRiseItem=0.1`, `DurationSuperWeapon=30000`); `mob.csv` contains 20 pet/mob rows across COMMON, RARE, EPIC, LEGENDARY, MYTHIC; `mutation.csv` has Normal, Golden, Frozen and Magma; `rebirth.csv` has 10 rows. Values and column names are preserved in source CSVs; units are not stated consistently in the table. `GlobalConfig.fcg` reads only the first four configuration values; no references to `DurationRiseSpeed`, `SpeedRiseItem` or `DurationSuperWeapon` were found in FC source.
- `key.csv` contains a 15-language header and identifies the game as “Steal A Shape”; the tutorials call the template “Steal A Pet Template.” This naming difference is observed, but its meaning is unknown.
- Tutorials say mob names and rarity values should be uppercase; mob IDs should be unique and sequentially increasing; localization key equals mob name. Tutorials describe adding a mutation through `MutationEnum`, materials/effects, `MobMutation`, `Mob.prefab`, localization, `MutationConfig.fcg`, and a color warning search. These are project instructions, not verified current editor behavior.
- Craftland workflow says FC symbols and asset registrations must be verified; `.fcg` and `.fcc` are the only directly editable text game assets; generated editor symbol files are read-only; FC edits require full validation. No code changes/builds were made in this extraction.

## Generic editor guidance sourced from MCP

The editor's `instructions://entities-assets` guide states that entity properties are merged from static type schema, component schema, and instance `dynamicDefine`; scene grounding varies by map; custom mesh entities do not automatically receive collision; and materials must match mesh submesh count for complete rendering. These are editor-wide instructions, not findings that every project object follows those conditions. Full resource list and relevant guidance are in 08.

## Not established

No map-design brief, map-settings document, player-spawn implementation description, playtest results, performance measurements, or editor build results were yet established. The project has a scene and editor settings but no map author narrative found in the initial pass. Do not extrapolate settings from file names alone.

## Gameplay source facts

## Project-owned custom components and enums (Craftland Studio)

Read-only `definition-list` returned 25 custom component definitions: 18 complete project-owned definitions plus 7 partial/editor-provided entries. The 18 complete project definitions and property labels are:

| Component | Properties (editor label : type) |
|---|---|
| Floor1 | NameBanner: Entity |
| Base | Floor1: Entity; CollectZone: Entity; DisplayZone: Entity; LaserWall: Entity; Spawn: Entity; Multiplier: Entity; ProtectSlot: Entity; Owner: Player |
| Mob | MobModel: Entity; MobDescription: Entity; MobRarityRing: Entity |
| MobParade | trigger: Entity; mobPlace: Entity |
| MobDisplay | MobDisplayModelHolder: Entity; MobDisplayTriggerHolder: Entity; MobDisplayModelEntity: Entity; Decoration: ListT_Entity |
| MobModelPlace | modelEntity: Entity |
| MobDescriptionPlace | descriptionEntity: Entity |
| MobPlace | mobEntity: Entity |
| LaserWall | WallPhysicalBlock, SwitchTrigger, SwitchTimerText, WallPhysicalBlock2, WallPhysicalBlock3, Wall1, Wall2, Wall3: Entity; UnlockTrigger: ListT_Entity |
| ParentEntity | parentEntity: Entity |
| MobStealing | modelPlace: Entity |
| NewMobDescription | Mutation, Rarity, General: Entity |
| ConfirmYesBtn | no properties |
| ConfirmNoBtn | entity: Entity; one attached ECA script record |
| MobRarityRing | RingEffect: Entity |
| MobMutation | GoldenEffect, FrozenEffect, MagmaEffect: Entity |
| PlayerCustomTrigger | owner: Player; one attached ECA script record |
| CollectTriggerHolder | trigger, displayText, decorateBtn: Entity |

The seven partial definitions reported by the editor are `CustomLevelObject`, `Component`, `Collider`, `CustomHud`, `HudButtonWidget`, `HudEmptyWidget`, and `AimableEntity`; these are partial extensions/editor definitions, not complete project-authored component schemas. The editor also returned 17 project-owned custom enums: `MobConfigEnum`, `MutationConfigEnum`, `RebirthConfigEnum`, `RarityEnum`, `MutationEnum`, `DataType`, `HudDepth`, `LeaderboardType`, `RebirthRewardType`, `CurrencyType`, `CustomStatusCode`, `DatabaseType`, `ActionType`, `PlayerState`, `PetState`, `RequestParameter`, and `ButtonEnum`. Their underlying type is `Int`, except `RarityEnum`, `DatabaseType`, and `ActionType`, which use `String`. No custom events were returned. These are names and schema metadata from the connected editor; see source/enum values in the script documentation and generated symbol references. This list does not describe every built-in engine component.

- **Spawning and base assignment:** Scene has six bases and named `Spawn` objects. `GlobalBase.InitBaseList` reads the registered `EResSceneMainScene.BaseList` and takes each base group's first child. `RebirthManager.LoadRebirthData` assigns a base after data loading. `PlayerBase.GetSpawnLocation` returns the base's `Spawn` transform; `PlayerTeleport.TeleportToHome` uses it plus one world Y unit. `GlobalBase.OnPlayerJoin` has base setup commented out, so the data-load path is significant.
- **Pet economy:** `PetsManager` loads/saves pet IDs, mutations, pet balances and current state through Data Storage. Pet balance accrues once per second and is capped to one hour; offline accrual converts five elapsed seconds to one online second. `PlayerBase.GetBaseIncome` combines pet production with mutation and rebirth multipliers. Selling gives half of configured pet price. The live ranking value is wallet balance plus owned pet price.
- **Stealing and lock system:** `StealManager` validates eligibility and coordinates pet state/mutex, transfer, display, prompts and failures. `LaserWallHandler` manages base wall state and unlock values; trigger scripts handle passage and interaction. Exact thresholds and edge cases are in source, not independently playtested.
- **Rebirth:** Ten CSV rows define starting money, multiplier, base lock duration/level, pet capacity, next-level money/pet requirements and money cap. Source declares unlock thresholds for swaps, hatching, dust, fusion, gift code, portals and pet following, plus minimum rebirth levels for stealing progressively rarer pets.
- **Movement/combat:** `PlayerEntity` sets configured run speed, baseball bat, hit-fly response and temporary immunity; player elimination revives after five seconds. `PlayerTeleport` uses three-second transition and cooldown intervals. `WaitForMillisecond` values are milliseconds in the source calls.

## Game modes and map settings

The current project's `PlayerSetting.asset` contains built-in/custom mode records, with `custom_game_mode=0`, map bounds values, and mode-specific round/team/safe-zone/revive properties. The enum is not decoded here. The current scene is a custom flat map (map ID 10, size 100 m, ground at y=0). `ProjectSettings/WorkflowMod.asset` has game phases, and `ProjectSettings/GlobalMod.asset` contains match configuration. No gameplay mode name is asserted from numeric settings.

## Serialized scene/UI observations through Craftland Studio

The main scene contains six named base group entities (`Base1` through `Base6`) and repeated child patterns including `Base`, `Spawn`, `BaseName`, and `UnlockBaseTrigger`. The visible scene reads establish object names/structure; gameplay assignment and spawn-selection semantics are implemented in scripts and need source cross-reference.

The connected editor's `current-scene` resolves to `MainScene.scene`. `scene-ground-info` reports map ID **10**, flat ground at world Y=0, surrounded by sea, with ground and no terrain. `scene-map-list` reports map 10 is 100 m × 100 m. Other selectable editor maps include map 25 (50 m flat at Y=-0.3), map 32 (200 m empty/no ground), and terrain maps with varying height; these other map entries are available editor options and are not this project's current scene.

Project `PlayerSetting.asset` reports `custom_game_mode=0` and custom map bounds of size 25–100 and circle size 90–180. These are raw editor settings; the numeric game-mode enum value was not decoded, so no mode name is assigned.

The 10 UI assets and returned entity counts (including each `UIRootEntity`) are: Debug 3, LaserWallInteract 16, Leaderboard 85, Mail 9, Menu 23, PetInteract 20, Prompt 4, Ranking 6, Rebirth 59, Wallet 8. The asset catalog's reported `entityCount` is one less in each case, consistent with excluding the synthetic root. UI types are primarily buttons, images, text, layouts and scroll/profile widgets. All widget entity trees were read through MCP; selected major widget names and relationships are present in the listing here and UI controller summaries in 04.

The editor catalog exposed 27 project prefabs; each entity tree was read. Largest structures are `Base.prefab` (195 entities), `DisplayZone.prefab` (127), `Floor3.prefab` (55), `LaserWall.prefab` (36), `Floor2.prefab` (27), `Floor1.prefab` (23), and `MobFollowing.prefab` (15). Counts and main script bindings:

| Prefab | Entities | Bound script roles |
|---|---:|---|
| Base | 195 | CollectZoneTrigger, Floor1Handler, MobDisplayHandler, MobBaseTrigger, LaserWallHandler, UnlockBaseTrigger, KickTrigger, LaserWallSwitchTrigger |
| BaseName | 3 | Floor1Handler |
| CollectZone | 3 | CollectZoneTrigger |
| DisplayZone | 127 | MobDisplayHandler, MobBaseTrigger |
| Floor1 | 23 | none |
| Floor2 | 27 | none |
| Floor3 | 55 | none |
| InvisibleLaserWall | 2 | none |
| LaserWall | 36 | LaserWallHandler, UnlockBaseTrigger, KickTrigger, LaserWallSwitchTrigger |
| Single | 7 | MobDisplayHandler, MobBaseTrigger |
| SingleTest | 11 | MobBaseTrigger |
| Stair | 4 | none |
| Hint | 1 | Hint |
| Mob | 9 | MobHandler, PetMutex, MobModelHandler, MobDescriptionHandler, MobRarityRingHandler |
| MobDescription | 1 | MobDescriptionHandler |
| MobFollow | 14 | MobHandler, MobModelHandler, MobDescriptionHandler, one unresolved script reference |
| MobFollowing | 15 | MobHandler, MobModelHandler, MobDescriptionHandler, one unresolved script reference |
| MobModel | 2 | MobModelHandler |
| MobParade | 11 | MobParadeHandler, MobParadeTrigger, MobHandler, PetMutex, MobModelHandler, MobRarityRingHandler, MobDescriptionHandler |
| MobRarityRing | 2 | MobRarityRingHandler |
| NewMobDescription | 4 | MobDescriptionHandler |
| FronzenEffect | 1 | none |
| GoldenEffect | 1 | none |
| MagmaEffect | 1 | none |
| PlayerTrigger | 1 | PlayerTrigger |
| TeleportEffect | 2 | TeleportEffect |
| TextOverHead | 3 | none |

The unresolved script reference is `emjscp8lpru-mno4xs1s-ucomtm2qgx8`, attached to MobFollow and MobFollowing, and is not mapped by the project FC asset catalog. The catalog has one package ECA asset; whether this identifier is a package-only reference is not established. All disk paths are in 02.
