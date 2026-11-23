# Known issues and static concerns

No issue tracker or explicit fixed-bug log was found. None of the following is a reproduced runtime failure or confirmed fix.

| Status | Finding | Evidence and confidence | Follow-up |
|---|---|---|---|
| **UNVERIFIED — high-confidence static concern** | `MutationConfigEnum.Tier=7`, but `mutation.csv` has only six columns (indices 0–5); `MutationConfig.fcg` reads Tier at index 7. | Cross-check of generated `EditorGenLib.fcc`, CSV header and FCG reader in source extraction. Likely invalid/out-of-range access during mutation load; no runtime reproduction. | Reconcile intended schema in a controlled source/editor task, then compile/run. Do not silently add columns or change code from this note alone. |
| **UNVERIFIED — likely state-initialization bug** | `DatabaseController.SetDatabaseSaved` checks `_DBReadyStatus` for player UID before creating `_DBSavedStatus[playerUID]`. | Static inspection recorded in extraction. No runtime failure reproduced. | Inspect exact implementation and exercise load/save/disconnect lifecycle. |
| **UNKNOWN resolution** | Script reference ID `emjscp8lpru-mno4xs1s-ucomtm2qgx8` is attached in `MobFollow.prefab` and `MobFollowing.prefab`, but not mapped to a project `.fcg` in the catalog. | Editor reference observed. Could be package-only; runtime impact not established. | Inspect current editor package/catalog/attachments. |
| **OBSERVED, not a bug by itself** | `GlobalBase.OnPlayerJoin` has base assignment commented out. `RebirthManager.LoadRebirthData` calls `GlobalBase.SetBasePlayer` after data load. | Static source flow. | Runtime timing not tested. |
| **OBSERVED, not a bug by itself** | Scene tree returned 1,187 rows versus `entityCount=1,186`. | The 1,187 includes synthetic Scene root plus 1,186 children. | No fix needed based on this count difference. |
| **UNKNOWN** | 13 `.fcg.meta` sidecars lack matching source files. | File inventory; names listed in extraction 14. | May be stale or removed scripts; no broken runtime reference confirmed. |
| **OBSERVED authoring note** | Tutorial asks to search `WARN: Add color for new mutation`. | Tutorial instruction; not evidence of an active runtime bug. | Follow documented color workflow and verify current source/editor. |

The static marker scan found no `TODO`, `FIXME`, `BUG`, or `NotImplemented` markers in `.fcg` source; four `DEBUG` comments were in `WeightedRandom.fcg`. These are not runtime diagnostics. `key.csv` had 116 data rows, 15 columns and no duplicate/blank keys in the extraction's CSV scan; translation quality was not evaluated.

## Sources

- `Craftland-Extraction/09_BUGS_AND_SOLUTIONS.md`
- `Craftland-Extraction/14_UNKNOWN_INFORMATION.md`
- `Craftland-Extraction/04_SCRIPT_DOCUMENTATION.md`
