# Unknown / Inaccessible Information

- Whether any website, Discord server, bot, database, deployment system, external API, or connected Google Sheet exists outside this local project.
- Runtime behavior/playtest confirmation of map/spawn configuration. Current map metadata and scene hierarchy have been inspected, but gameplay was not launched.
- Runtime outcomes of Data Storage load/save and leaderboard calls, including service availability, failure frequency and current production behavior; source call paths are documented in 04/08, but they were not executed.
- Existing build/test outcome: no build or scripts were run for this read-only extraction.
- Git history: no root Git repository is present; no nested repository was located in initial check.
- Full property-by-property semantic review of all 1,186 scene children and every serialized property in all 27 prefabs/10 UIs; structural/entity trees and main bindings were inspected, not every transform/material/field value.
- Cache and temporary history conclusion is now available in 11; no reliable history was present in those files.
- Entity `aiPrompt` search found no values in the current scene, 27 project prefabs, or 10 UI assets.
- Any private credentials in editor/MCP configuration. Never copy their values into these documents.
- The 13 `.fcg.meta` sidecars without matching source files may be stale or represent deliberately removed scripts. They are: `Assets/Scripts/Base/MoneyCollectTrigger.fcg.meta`; `Assets/Scripts/Base/LaserWall/InBtnTapped.fcg.meta`; `InTrigger.fcg.meta`; `OutBtnTapped.fcg.meta`; `OutTrigger.fcg.meta`; `PlayerLaserUI.fcg.meta`; `Assets/Scripts/HUDs/HudChat.fcg.meta`; `HudLoginReward.fcg.meta`; `Assets/Scripts/Manager/ChatManager.fcg.meta`; `CoreDataManager.fcg.meta`; `MeteorDigEventManager.fcg.meta`; `Assets/Scripts/Mobs/MobSwitchRender.fcg.meta`; `MobSwitchRenderHandler.fcg.meta`. No source content was available to inspect.

Mark each unknown resolved/unavailable with the source checked and date. Do not fill gaps with generic Craftland assumptions.
