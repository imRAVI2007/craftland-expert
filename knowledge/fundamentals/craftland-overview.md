# Craftland project overview

**Scope:** this is verified knowledge about the extracted project named **Steal A Pet Template**, not a universal description of every Craftland project.

## Project identity and contents

The extraction identifies a Craftland UGC game project with root `main.gproj`, `fcconfig.json`, project instructions and English/Vietnamese tutorials. `Assets/` contains FC source, CSV/configuration, localization, HUDs, prefabs, materials, meshes, textures, sounds, and one scene. `ProjectSettings/`, generated `Temp/`, `Libraries/`, and `Cache/` are also present in the historical workspace inventory.

The project has one scene, `Assets/Scenes/MainScene.scene`; 63 `.fcg` source files; 27 local prefab assets (the editor also exposes five additional built-in/read-only prefab resources); 10 local UI assets; and one package-owned/read-only ECA graph. MainScene reports 1,186 children; the editor entity read included its synthetic root, totaling 1,187 rows.

The project name differs across sources: tutorials say “Steal A Pet Template,” while `Assets/Localization/key.csv` identifies “Steal A Shape.” Meaning/version relationship is unknown.

## Gameplay scope

Source declarations and script names support these implemented areas: pet collection/display, base ownership and locks, interaction, stealing, wallet/economy, rebirth, mutations, pet parade, player movement/interactions/teleport, and HUDs. Detailed source-linked flows are in [gameplay-systems.md](../gameplay/gameplay-systems.md).

## Evidence limits

The extraction read all 63 FC texts and editor structures, but did not execute or compile them. Scene/prefab/UI structural trees were inspected; not every serialized transform/material/property received semantic review. No playtest or performance measurement was performed. See [knowledge-status.md](../../research/knowledge-status.md) and the preserved [overview](../../Craftland-Extraction/01_PROJECT_OVERVIEW.md).

## Sources

- `Craftland-Extraction/01_PROJECT_OVERVIEW.md`
- `Craftland-Extraction/02_COMPLETE_FILE_INDEX.md`
- `Craftland-Extraction/05_CRAFTLAND_KNOWLEDGE.md`
- `Craftland-Extraction/08_API_AND_INTEGRATIONS.md`
