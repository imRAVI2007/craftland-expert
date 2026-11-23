# Hungry Fish 2.0 limitations and unresolved questions

## Coverage limits

- The 2,840-path inventory is complete against the captured baseline, but semantic inspection covered 252 files. The other 2,588 have inventory coverage and some targeted keyword-scan coverage only.
- Visual assets (models, textures, sprites, animation, audio, materials) were not semantically reviewed as a set. Many serialized settings remain inventory-only.
- No `.fcg` was executed. No compilation, build, playtest, multiplayer test, data-store exercise, leaderboard read/write, or result upload was performed.
- No Git history was available. Timestamp ordering does not establish project history or design intent.
- No local website, web app, Discord bot/server configuration, external database, REST/GraphQL service, or authentication integration was identified in the inspected local project. This does not prove such systems do not exist elsewhere.

## Specific unresolved items

- Exact runtime effect of differing values in `Workflow.wfl` and `WorkflowMod.asset` / `GlobalMod.asset`, including reconnect disable and recommended start count, is not established.
- `GameStart.ui` says 30 seconds while the workflow phase data says five seconds; precedence is unknown.
- Selected map ID and full terrain/ground context are not established in the reviewed project summary.
- Some persisted score reads retry while values are zero, though zero may be valid; performance or failure impact is untested.
- DataStorage write flows retry timeout statuses; final non-timeout error handling is incomplete or unclear in the source summaries.
- `AttackController` has no explicit empty spawn-list fallback in the reviewed source; the runtime consequence is untested.
- The `playerdata` asset listing returned zero while 27 files existed and were subsequently read individually; the listing discrepancy is unexplained.
- Several legacy instruction references point to paths absent from the baseline inventory. They may have moved or come from an older managed instruction package.

## Source and provenance

See `D:\My project (6)\Craftland-Extraction\14_UNKNOWN_INFORMATION.md` and `01_PROJECT_OVERVIEW.md`. Treat all behavior not explicitly tested as source-described, editor-observed, inferred, or unknown. Do not present static review candidates as reproduced bugs or verified fixes.
