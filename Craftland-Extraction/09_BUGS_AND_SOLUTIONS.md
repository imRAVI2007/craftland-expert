# Bugs and Solutions

## Verified bug reports / fixes

No project bug tracker, issue export, saved conversation history, or explicit “fixed” log has been identified. No bug is labeled fixed without a source and verification record.

## Candidate issue signals requiring source review

- `Tutorial (EN).md` instructs searching for `WARN: Add color for new mutation` when adding a mutation. This is an authoring note about required color coverage, not proof of an active runtime bug.
- The tutorial text has potential stale terminology (`Mob` alongside player-facing pet terminology) but no independent version history was found; treat as a documentation consistency observation, not a defect report.
- The editor reports 1,186 scene children. Paginated `asset-get` returns 1,187 unique entities because the list includes the synthetic `Scene` root plus its 1,186 children. All six pages were read and IDs deduplicated; this is not a project bug.
- `Assets/Scripts/Configs/MutationConfig.fcg` indexes `rowInfo[MutationConfigEnum.Tier]`; read-only generated `EditorGenLib.fcc` defines `Tier = 7`, while `Assets/CSV/mutation.csv` currently has six columns (indexes 0–5) and no `Tier` column. This is a source/schema mismatch and likely an out-of-range configuration read when mutation rows load. No runtime failure was reproduced and no fix was made; classify as **unresolved, high-confidence static concern** pending a non-read-only validation task.
- `DatabaseController.SetDatabaseSaved` checks whether `_DBReadyStatus` contains a player UID before creating `_DBSavedStatus[playerUID]`. The map named in the guard differs from the map being initialized. This is a likely state-initialization bug; no runtime failure was reproduced and no fix was made.
- `Assets/Scripts/Manager/GlobalBase.fcg` leaves base assignment commented out in `OnPlayerJoin`. Current source evidence shows `RebirthManager.LoadRebirthData` calls `GlobalBase.SetBasePlayer` after database load, so this is not, by itself, confirmed as a bug. It makes initial base assignment depend on the rebirth data-load workflow; runtime behavior was not tested.

## Additional source inspection findings

- Static marker scan found no `TODO`, `FIXME`, `BUG`, or `NotImplemented` markers in `.fcg` source. It found four `DEBUG` comments in `WeightedRandom.fcg` and explicit authoring warnings for adding new mutation effects and rarity/mutation colors. These are source notes, not runtime diagnostics.
- `Assets/Scripts/` has 76 `.fcg.meta` files but only 63 corresponding `.fcg` sources; 13 sidecars have no matching source path. This may represent intentionally removed scripts or stale metadata; no broken runtime reference was confirmed.
- `Assets/Localization/key.csv` has 116 non-header rows, 15 columns, no duplicate keys and no blank keys when parsed as CSV. Localization text quality/translation correctness was not reviewed.
- The mutation CSV mismatch is a high-confidence static issue, but runtime impact remains unconfirmed because no build/game execution was allowed. `MutationConfig.fcg` also reads the enum's Tier index 7; current CSV's highest index is 5. `FusionWeight` index 6 is not read by the script. No fix is recorded.

## Validation status

No game build, compiler invocation, test suite, or unknown script was run, per the read-only investigation request. Existing logs/caches can be examined as historical artifacts, but their timestamp and completeness must be verified before calling them current test results.

## Required record format for later findings

For each confirmed issue: exact source file/line or editor record; observed symptom/error; root cause supported by evidence; workaround/fix source; validation method/date/result; current status. Unverified hypotheses go in 14, not here as “solutions.”
