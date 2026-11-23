# APIs and Integrations

## Project source dependencies

- FC scripts import Craftland-provided `.fcc` libraries such as `StdLibrary.fcc`, `Player.fcc`, `Hud.fcc`, `Map.fcc`, `List.fcc`, `CSVData.fcc`, `Items.fcc`, `Workflow.fcc`, and `Physics.fcc`, as well as project `.fcg` modules and generated `EditorGenLib.fcc`.
- `fcconfig.json` and `Temp/UGCLanguage/fcconfig.json` are compiler/toolchain configuration sources. Do not publish local absolute executable paths or environment-specific values without checking for private content.
- Craftland Studio MCP is connected in this investigation. `instructions://index` was read before further Craftland MCP calls. Asset catalog methods used were read-only: supported-type discovery, asset listing, and `asset-get`.
- Craftland editor MCP exposes scene/assets, entities/components, ECA, FC registration, game build/log tools, timeline, behavior tree, and physics. This extraction used only read operations.

## Runtime service/API status

Project source uses Craftland's built-in Data Storage APIs: `ReadFromDataStoreSteady`, `ReadFromDataStoreBatch`, `ReadFromDataStore`, `WriteToDataStoreV2`, `ReadFromLeaderboardByRank`, and `WriteToLeaderboard`. `ProjectSettings/DataStorage.asset` describes the `PlayerSave` key/value sheet and persistent `WealthRank`/`IncomeRank` sheets; values are private project identifiers and are intentionally omitted. `PlayersManager` stores last-log time; `RebirthManager` stores rebirth level; pet managers persist pet state; leaderboard manager persists income and wealth ranks. `MAP_CODE` fields in the reviewed managers are empty strings. These are Craftland runtime integrations, not evidence of an external website API.

The initial code/config scan found no external HTTP client, OAuth/authentication implementation, Discord bot, or webhook integration. Do not confuse engine APIs (`Player`, `Workflow`, `DataStorage`, etc.) with external APIs.

## Asset catalog snapshot (read-only, current editor connection)

| Type | Count | Notes |
|---|---:|---|
| scene | 1 | MainScene, 1,186 children plus scene root in MCP entity response |
| prefab | 32 | 27 project prefabs and 5 editor/library read-only resources |
| ui | 10 | Local HUD assets; returned entity trees have root plus catalog entity count |
| fcg | 63 | Matches local source count |
| fcc | 0 | Asset list did not expose `.fcc` assets; generated libraries are in Temp |
| eca | 1 | Read-only built-in “Spawn Point Auto Closer” |
| ac | 38 | Includes read-only library controllers and project built-in AC content |
| modification | 12 | ProjectSettings modules reported by editor |

Additional editor-catalog project-local rows: 27 prefabs, 28 `.ac` controllers, 23 materials, 3 FBX assets, and 26 `texture2d` assets (including the project screenshot). Project content has 0 `.phymat`, `.particles`, `.timeline`, `.xbt`, `.playerdata`, `.bpc`, `.fcc`, `.mesh`, `.sk`, `.uma`, `.clothskin`, or `.anim` entries returned as local assets. Many other catalog rows are built-in library resources and are not project files. The built-in catalog itself includes 702 textures, 653 sprites, 785 animations and 371 preset items, returned in pages; these are not project dependencies simply because Craftland exposes them.

The full entity trees for all 10 local UI assets were read via `asset-get(entities_page_size=200)`. Returned totals include one root each; UI-specific detail is in 05. `MainScene.scene` was read in six 200-row pages; it returns 1,187 unique entities including the root, while its reported child `entityCount` is 1,186.

Asset list is filtered by project/editor semantics; it is not the same as raw disk-extension counts. See 02 for disk inventory.

## Editor documentation consulted

The Craftland Studio index and instruction resources for entities/assets, UI widgets, ECA overview, ECA graph, game tools, physics, timeline and behavior trees were read. Project-relevant points:

- Entity properties combine static type schema, component schema and per-entity dynamic definitions; verify current schemas instead of inferring keys.
- UI `computedRect` is a resolved read-only layout measurement; widget tint multiplies its source art. Button callbacks must be attached to the UI root and use the documented callback signature; editor docs identify `CallCustomFunc failed` when callback scripts are attached to a child/button rather than root.
- ECA graph edits require schema/config discovery and platform matching; graph operations are the preferred batched edit path. These rules describe the editor, not a bug found in the current UI.
- Physics guidance: custom mesh creation does not itself add a collider; `collidable`, trigger state, component schema and collision matrix determine interactions. The current scene has collider components on 559 entities per MCP component counts, but collision correctness was not tested.
- Current scene map is flat, so the editor reports a base ground Y of 0; other maps have terrain, a different flat height, or no ground. Do not transfer the current map's height assumption to other maps.
- Timeline and behavior-tree tools/resources exist in the editor integration, but the project asset catalog returned zero project timeline and XBT assets.
# Project definition catalog

The read-only Craftland Studio definition catalog returned 25 custom component definitions (18 complete project-owned definitions and 7 partial editor extensions), 17 project-owned enums, and 0 project-owned custom events. Complete component labels/properties and enum names are cataloged in [05_CRAFTLAND_KNOWLEDGE.md](05_CRAFTLAND_KNOWLEDGE.md). This adds schema information to the project's local code/API picture; no editor state was changed.

