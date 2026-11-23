# Editor concepts and evidence-backed guidance

**VERIFIED editor guidance from the extraction's Craftland Studio MCP documentation**, not universal project behavior:

- Entity properties can combine a static type schema, component schema, and per-instance `dynamicDefine`. Check the active schema instead of guessing keys.
- UI `computedRect` is a resolved, read-only layout measurement; widget tint multiplies source art.
- The editor guide specifies that button callbacks belong on the UI root and use the documented callback signature. It identifies `CallCustomFunc failed` when callback scripts are attached to a child/button rather than the root. This is editor documentation guidance, not a reproduced defect in this project.
- Creating a custom mesh does not itself add a collider. Collision behavior depends on `collidable`, trigger state, component schema, and collision matrix.
- ECA graph edits should start with schema/config discovery and matching platform; graph operations are the preferred batched edit path.
- Map ground behavior depends on selected map: this project's flat map reports ground Y=0, while other selectable maps have terrain, a different flat height, or no ground.
- Timeline and behavior-tree facilities are exposed by the editor integration; this project catalog returned no local timeline or XBT asset.

For editor-owned serialized assets, Craftland Studio is the authority. The archived project rule says to read `instructions://index` before other Craftland Studio MCP calls and not to hand-edit opaque `.eca`. In a different project/session, re-check tool availability and current instructions.

## Sources

- `Craftland-Extraction/08_API_AND_INTEGRATIONS.md` (editor docs consulted and asset catalog)
- `Craftland-Extraction/05_CRAFTLAND_KNOWLEDGE.md` (project structures)
- `Craftland-Extraction/03_PROMPT_LIBRARY.md` (verbatim archived editor rules and FC workflow)
