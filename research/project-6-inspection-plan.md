# Hungry Fish 2.0 prioritized inspection plan

## Scope and constraint

The Project 6 baseline has 2,840 paths; the extraction reports 252 content/structure inspections and 2,588 files with inventory coverage only, plus targeted keyword scans for some text files. The extraction does not provide a per-file inspection manifest and does not name eight additional project/config/support files it says were read. Do not label an exact 2,588-path set until those eight files and the full inspected set are reconstructed. Use the preserved [FILE_INVENTORY.csv](../sources/hungry-fish-2.0/indexes/FILE_INVENTORY.csv) as the path/size authority and [inspection-gap register](project-6-inspection-gaps.md) for known coverage.

All work below is read-only. Do not run `.fcg`, modify serialized assets, or treat MCP structure reads as runtime tests. Use the current Craftland Studio instructions before any editor query.

## Priorities

| Priority | Inspection batch | Paths / inventory filters | Why first | Deliverable and stop condition |
|---|---|---|---|---|
| **P0 — scope accuracy** | Reconstruct the inspected-file manifest. Identify the eight unnamed support files and enumerate the 93 indexed scripts, 14 instruction sources, 137 editor records, and 8 support files without double-counting. | `FILE_INVENTORY.csv`; extraction `01_PROJECT_OVERVIEW.md`, `02_COMPLETE_FILE_INDEX.md`, `04_SCRIPT_DOCUMENTATION.md`; `Assets/_Scripts/**/*.fcg`; listed ECA/UI/prefab/playerdata and settings paths. | Establishes which individual files make up the 252 and prevents false claims about the remaining 2,588. | Add a dated 2,840-row status CSV (`inspected-signature-only`, `inspected-narrative`, `editor-observed`, `targeted-scan-only`, `inventory-only`, or `unresolved`) with evidence path. Stop if the source cannot classify a file; retain `unresolved`. |
| **P1 — configuration conflicts** | Resolve the static configuration discrepancies without changing the project. | `ProjectSettings/Workflow.wfl`, `WorkflowMod.asset`, `GlobalMod.asset`, `PlayerSetting.asset`, `DataStorage.asset`, `PlayerEntity.asset`, and the remaining `ProjectSettings/*.asset` not among the 16 queried modification modules. Cross-check `Assets/Config/fish_config.csv`, `Assets/Localization/key.csv`, and related FC readers. | These settings affect match phase, map/room behavior, player setup, and persistence wiring; the extraction already flags mismatched values and an unknown selected map profile. | Record each property, owning editor schema/module, value source, and unresolved precedence. Use Craftland Studio for serialized settings. Do not decide which value is authoritative without editor/runtime evidence. |
| **P1 — gameplay-linked asset details** | Deepen property-level review only for assets tied to core fish-selection, combat, pickups, spawn, ranking, and result flows. | Main scene; fish/food/coin/weapon prefabs; `FishSelection.ui`, gameplay HUDs, ranking/result UIs; referenced components and `Assets/PlayerData/**/*.playerdata`. The extraction has structure observations for many of these; mark follow-up as property-level, not wholly uninspected. | Clarifies source-to-asset bindings for the main game loop while avoiding an indiscriminate reread of all 90 queried prefab/UI assets. | Produce binding/property maps for only the selected paths; retain the original path and editor-query provenance. Do not infer dynamic behavior from the tree. |
| **P2 — player data and leaderboard static trace** | Cross-check DataStorage call schemas, retry branches, and UI consumers against the four sheets and leaderboard/result APIs. | `Player/PlayerWalletData.fcg`, `PlayerInventoryData.fcg`, `PlayerLoginData.fcg`, `PlayerScoreData.fcg`, `PlayerRankingData.fcg`; `ProjectSettings/DataStorage.asset`; wallet/inventory/login/score/ranking UIs. | Resolves the highest-impact static unknowns: zero-value retries, terminal non-timeout errors, rank ordering, and service/graph wiring. | Document code paths and schemas. Runtime behavior remains `UNKNOWN` unless separately tested in an authorized environment. No actual data-store writes during this audit. |
| **P2 — visual/audio representative review** | Review representative assets by gameplay role, then expand only when a referenced asset remains ambiguous. | Inventory filters for `Assets/Art/`, `Assets/Meshes/`, `Assets/Animations/`, `Assets/Audio/`, `Assets/Particles/`, `Assets/SampleMaterials/`; prioritize fish, pickups, abilities, HUD icons, and attached effects. | Current evidence mainly establishes inventory path/size; visual and audio meaning is not catalogued. | Create a small, cited asset guide with visual/audio inspection method and status. Do not claim a full review from sampling. |
| **P3 — asset registration and sidecar integrity** | Check registration and cross-reference metadata for active assets only. | `ProjectSettings/ResourceRegisteration.asset`, `.meta`, `.info`, `.json`, and `.gdvar` files referenced by active scene/prefab/UI/script resources. | There are many sidecars and metadata records; indiscriminate reading has low value without an active reference. | Report unresolved registration references and exact source paths. Skip orphan/cache files unless an active asset references them. |
| **P4 — generated/cache/support files** | Defer unless an earlier priority depends on them. | `Cache/`, `Temp/ProjectCache/`, `Temp/TimelineData/`, generated compiler output, `.pvr`, `.~@*` sidecars, and unreferenced `Libraries/` content. | These make up many inventory rows but are generated, cached, or not yet tied to authored behavior. | Inspect only targeted files needed to explain a source/editor discrepancy; preserve them read-only and label generated evidence. |

## Suggested execution order

1. Produce the P0 manifest and resolve the eight unnamed paths.
2. Read active project settings and resolve which discrepancies are explainable from schema/source alone; leave runtime precedence unknown otherwise.
3. Trace core gameplay assets and persistence/leaderboards through source, configuration, and editor observations.
4. Review representative visual/audio assets and registration links.
5. Scan remaining generated/cache/support files only when a referenced question requires it.

## Completion criteria

- Every baseline path has an explicit inspection status or `unresolved`; inventory-only is not described as semantic review.
- Each new fact cites an original path and source extraction/editor record.
- Project-specific details remain scoped to Hungry Fish 2.0 and do not get merged into Steal A Pet Template behavior.
- No original project file is changed, no FC script is executed, no external service is called, and no runtime validation is claimed.
