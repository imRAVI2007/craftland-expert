# Knowledge status and research register

Audit date: 2026-11-23 (client timezone Asia/Calcutta). Project sources: Project 5 `Craftland-Extraction/` copied from `D:\My project (5)\Craftland-Extraction\`; Project 6 `D:\My project (6)\Craftland-Extraction\` with selected indexes and instruction copies preserved under `sources/hungry-fish-2.0/`.

## Status vocabulary

- **VERIFIED** — explicit source text/config/script or cross-checked declarations support the claim. Verification is limited to the artifact inspected.
- **OBSERVED** — captured editor/catalog/tree state; does not imply runtime behavior.
- **INFERRED** — reasoned from evidence, clearly labeled and not stated as fact.
- **UNVERIFIED** — a plausible technical concern/claim without required runtime or independent validation.
- **UNKNOWN** — source unavailable or not established after stated search scope.

## Verified/observed coverage

- **VERIFIED (source inventory):** all 15 expected Markdown extraction files exist. The extraction reports 963 accessible source-project files, 63 `.fcg` source scripts, and complete text reading of those scripts; 13 extra `.fcg.meta` files have no matching source.
- **VERIFIED (archive):** 03 contains 15 saved instruction/template source texts and two tutorials verbatim; dedicated saved AI prompts found: 0. Duplicate check identified an identical pair of asset-rule documents.
- **OBSERVED (editor):** one scene, 27 local prefab trees, 10 UI trees, 18 complete project-owned component schemas plus seven partial/editor entries, 17 project enums, no project custom events, one read-only built-in ECA graph. Entity rows include synthetic roots in counts.
- **VERIFIED (local project):** 5 CSVs (4 config tables + localization), project settings, 63 script index entries, static mutation CSV/enum/read mismatch, Data Storage code usage.
- **VERIFIED as absence within inspected workspace only:** no conventional website source tree, no Discord server/bot export, no external HTTP/OAuth/webhook implementation found in the 963-file inventory/search. This does not prove such systems do not exist elsewhere.

## Open research register

| Topic | Status | Evidence checked / remaining |
|---|---|---|
| Mutation Tier field runtime effect | UNVERIFIED | Static mismatch: enum index 7, CSV max index 5, reader accesses Tier. No build/game load test. |
| `DatabaseController.SetDatabaseSaved` map guard | UNVERIFIED | Static condition/initialization mismatch; reproduce lifecycle before classifying. |
| MobFollow/MobFollowing script ID | UNKNOWN | Editor catalog did not map the attached ID to local FCG; could be package-provided. Inspect live asset/package catalog. |
| Base assignment/spawn runtime ordering | UNKNOWN | Static flow documented; no gameplay launch. |
| Data Storage load/save/leaderboard behavior | UNKNOWN | Calls documented; no service execution/outcomes. Private sheet identifiers intentionally omitted. |
| Full serialized scene/prefab/UI semantic review | Incomplete | Trees read; not every property/transform/material semantically reviewed. |
| Collision correctness | UNKNOWN | Editor guidance and component counts only; no collision test. |
| Website/Discord/auth/deployment/external Sheets | UNKNOWN outside workspace | Project inventory/text/config search found no implementation/export; scope is local project only. |
| Git/project history | UNKNOWN | Original root not Git repository; no reliable timeline found. |
| 13 orphan FCG meta files | UNKNOWN | Listed in `14_UNKNOWN_INFORMATION.md`; no source file matched. |
| Prompt field/content outside inspected asset scope | UNKNOWN outside snapshot | `aiPrompt` search returned none across inspected scene, 27 prefab trees and 10 UI trees. |
| Current editor release compatibility | UNKNOWN | Tutorials/workflows are source snapshot; no version-current validation. |
| Performance, localization quality, usability, device behavior | UNKNOWN | Not measured/reviewed. |

## Secret handling and source boundary

Project 5 Data Storage identifiers were omitted in extraction. Do not reproduce credentials, environment config, absolute compiler paths, or private identifiers from either project's original settings. The repository contains no original game `.fcg`, `.eca`, scene, UI, prefab, playerdata, or other game-asset source copies. Project 6's inventory/index CSVs and instruction texts are documentation artifacts only.

## Project 6 — Hungry Fish 2.0 coverage

- **VERIFIED (baseline inventory):** 2,840 unique original file paths across 772 directories; all paths and byte sizes match the baseline inventory CSV against the read-only original workspace. No missing/extra paths or size mismatches were found.
- **VERIFIED (FC index):** 93 `.fcg` source files and 93 unique script-index paths; the two path sets match exactly. Each row records `Read source signatures; runtime behavior not executed`.
- **VERIFIED (instruction archive):** 14 original local instruction/rule/reference files are preserved byte-for-byte in `sources/hungry-fish-2.0/instructions/`; they represent 13 unique texts because `.github/instructions/craftland-studio-assets.instructions.md` and `.cursor/rules/craftland-studio-assets.mdc` are identical.
- **OBSERVED (Craftland Studio reports):** three project ECA graphs; 20 UI trees; 70 project prefab trees; 27 PlayerData definitions; one scene plus project setting observations. These are not runtime tests.
- **VERIFIED (extraction scope):** 15 Markdown reports exist; extraction reports 252 files with content/structure inspection out of a 2,840-file inventory. The remaining 2,588 have inventory coverage and targeted-scan coverage for some text files only.
- **VERIFIED (credential scan):** no credential-like pattern matches in extraction Markdown/CSV or the 14 instruction-source files. The scan is pattern-based, not proof of absence of every secret format.

## Project 6 open research register

| Topic | Status | Evidence checked / remaining |
|---|---|---|
| Full project semantic coverage | Incomplete | 252 inspected; 2,588 remain inventory/targeted-scan only. Visual assets and many serialized settings are not semantically reviewed. |
| Runtime/gameplay/data behavior | UNKNOWN | No script execution, build, playtest, multiplayer test, DataStorage call, leaderboard operation, or result upload. |
| Workflow setting precedence | UNKNOWN | `Workflow.wfl`, `WorkflowMod.asset`, and `GlobalMod.asset` show differing settings; editor/runtime precedence not tested. |
| Start message duration | UNVERIFIED discrepancy | `GameStart.ui` says 30 seconds while workflow phase has five-second data; effect/precedence not known. |
| Selected map profile | UNKNOWN | Scene spawn/ground observations exist; selected map ID and complete terrain profile not established in reviewed summary. |
| DataStorage terminal failures | UNVERIFIED concern | Source summaries show bounded timeout retries and incomplete non-timeout result handling; no failure reproduced. |
| Empty spawn list | UNVERIFIED concern | `AttackController.fcg` has no explicit empty-list fallback in the source note; runtime consequence unknown. |
| Zero-valued score retries | UNVERIFIED concern | `PlayerScoreData.fcg` retries zero values even though zero may be legitimate; behavior/performance untested. |
| `playerdata` list discrepancy | UNKNOWN | Studio list returned zero; 27 files were individually queried through raw-asset reader. Reason unknown. |
| Website/Discord/auth/external API | UNKNOWN outside inspected workspace | No local implementation/export found in the reviewed inventory/search; external systems are out of scope. |
| Git history/design rationale | UNKNOWN | Project root has no `.git`; timestamps do not establish development history. |

## Sources

- `Craftland-Extraction/01_PROJECT_OVERVIEW.md`
- `Craftland-Extraction/02_COMPLETE_FILE_INDEX.md`
- `Craftland-Extraction/03_PROMPT_LIBRARY.md`
- `Craftland-Extraction/08_API_AND_INTEGRATIONS.md`
- `Craftland-Extraction/09_BUGS_AND_SOLUTIONS.md`
- `Craftland-Extraction/14_UNKNOWN_INFORMATION.md`
- `sources/hungry-fish-2.0/indexes/FILE_INVENTORY.csv`
- `sources/hungry-fish-2.0/indexes/SCRIPT_INDEX.csv`
- `D:\My project (6)\Craftland-Extraction\01_PROJECT_OVERVIEW.md`
- `D:\My project (6)\Craftland-Extraction\14_UNKNOWN_INFORMATION.md`
