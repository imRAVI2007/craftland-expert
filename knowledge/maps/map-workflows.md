# Map and scene workflows

## Evidence-backed process for this project

1. Confirm the active scene and selected Craftland map in the editor. Do not assume MainScene's map/ground applies elsewhere.
2. Inspect current scene ground/map metadata and locate scene entities through the registered symbols/editor tree; names in this archive are historical evidence, not current IDs.
3. For base/spawn logic, read `GlobalBase.fcg`, `PlayerBase.fcg`, `PlayerTeleport.fcg`, `RebirthManager.fcg`, and project registration. The source summary says base assignment occurs through the rebirth data-load path after database load, while the direct join call in `GlobalBase` is commented out.
4. Check component and entity schemas in current Craftland Studio. Do not infer properties from prefab names. For custom mesh collision, inspect collider/trigger state and collision matrix.
5. Make edits using the editor for editor-owned scene/prefab/UI/ECA data. Validate with an actual build/playtest if the task requires runtime assurance, and record what was run.

## Current snapshot

Only map 10 (100 m × 100 m flat, ground Y=0) is active in the inspected project. Other editor maps in the catalog differ. Current game mode numeric code `0` was not decoded. No playtest/build was run.

## Sources

- `Craftland-Extraction/05_CRAFTLAND_KNOWLEDGE.md`
- `Craftland-Extraction/08_API_AND_INTEGRATIONS.md`
- `Craftland-Extraction/10_WORKFLOWS.md`
