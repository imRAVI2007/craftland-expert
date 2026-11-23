# ECA reference

## Observed graph

The only ECA graph read in the extraction was package/built-in **Spawn Point Auto Closer**, a read-only asset. Editor metadata: `OwnerType=Entity`, `ComponentTypes=SpawnPos`, server platform. Its graph contains one top-level event `OnPhaseEnd(Phase)`, followed by `SetActive(this_entity, false)`.

The behavior description is from Craftland Studio `eca-graph-get(depth=-1)`. The raw serialized `.eca` file was not hand-edited or copied. This single graph does not establish generic ECA mechanics or prove that project-owned components use ECA. The editor catalog reported one ECA asset overall; no project-authored custom events were returned.

## Editing guidance

For future ECA tasks, inspect the current graph, schema/config, platform, and component attachment through Craftland Studio. The extraction's archived asset rules prohibit guessing/hand-editing opaque serialized `.eca` when editor access is required. Current editor instructions must be checked in the active session.

## Sources

- `Craftland-Extraction/04_SCRIPT_DOCUMENTATION.md` (read-only ECA summary)
- `Craftland-Extraction/08_API_AND_INTEGRATIONS.md` (editor catalog and ECA guidance)
- `Craftland-Extraction/05_CRAFTLAND_KNOWLEDGE.md` (component definitions)
