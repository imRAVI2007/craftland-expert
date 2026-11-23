# Hungry Fish 2.0 ECA observations

Three project ECA graphs were read through Craftland Studio MCP. These are editor observations only; no graph was executed. The extraction describes them as small test/utility graphs, and names do not prove production use.

| Project graph | Observed context and nodes | Flow detail / unknowns |
|---|---|---|
| `Assets/ECA/NumberUtils.eca` | Static client Entity graph; function `ToDecimalNumber(number: Int) -> String`. | The graph calls an integer-to-string conversion block. The extraction does not document additional edges, formatting semantics, or runtime behavior. |
| `Assets/ECA/Test.eca` | Non-static client Weapon graph. Event roots `OnPlayerAdd(Player)`, `OnUserQuitOrUserMacthEnd(Player)` (saved spelling), `OnUserQuit(Player)`, and one enum input block. | The extraction lists four top blocks; connections/branches beyond this node inventory are not described. Enum identity and effects are unknown. |
| `Assets/ECA/TestServer.eca` | Non-static server Player graph with `OnPlayerReconnect(Player)`. | One top block is listed; downstream nodes/connections are not documented. |

Do not hand-edit serialized `.eca` files or infer more behavior than the editor graph report states. Reinspect current graph and schemas through Craftland Studio before any changes. This differs from the first project's single read-only built-in `Spawn Point Auto Closer` graph, described in [eca-reference.md](eca-reference.md).

**Sources:** `D:\My project (6)\Craftland-Extraction\04_SCRIPT_DOCUMENTATION.md`, `08_API_AND_INTEGRATIONS.md`; original paths `Assets/ECA/NumberUtils.eca`, `Assets/ECA/Test.eca`, `Assets/ECA/TestServer.eca`.
