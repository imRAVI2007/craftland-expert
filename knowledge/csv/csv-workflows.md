# CSV authoring and data-reader relationships

## Files and table roles

| Original project path | Role / documented shape |
|---|---|
| `Assets/CSV/globalConfig.csv` | One configuration data row; extracted values include `MobSpawnInterval=6000`, `PlayerMoveSpeed=1.0`, `PlayerStealSpeed=0.35`, `PlayerHitInvulnerableTime=3000`, `DurationRiseSpeed=30000`, `SpeedRiseItem=0.1`, `DurationSuperWeapon=30000`. Units are not consistently specified. `GlobalConfig.fcg` reads only the first four values; no FC references were found for the final three. |
| `Assets/CSV/mob.csv` | 20 mob/pet records across `COMMON`, `RARE`, `EPIC`, `LEGENDARY`, `MYTHIC`; `MobConfig.fcg` reads from row index 2 and maps ID/name/rarity/value/price/weight/mesh/material/sprite. |
| `Assets/CSV/mutation.csv` | Current records: Normal, Golden, Frozen, Magma; header has six columns `ID,Name,MaterialKey,EffectKey,Multiplier,Weight`. |
| `Assets/CSV/rebirth.csv` | Ten rows for starting money, multiplier, base lock duration/level, pet capacity, next-level money/pet requirements and money cap. |
| `Assets/Localization/key.csv` | Localization table with a 15-language header and 116 non-header rows. Duplicate/blank-key scan found none; translation quality was not assessed. |

The source CSVs remain in the original project, not this repository. Do not assume tutorial mention of Google Sheets proves an active Sheets integration; only local CSV copies were established.

## Documented authoring workflow: add a mob

From the English/Vietnamese project tutorials: add a configuration row in `mob.csv`; import mesh under `Assets/Meshes/Mobs/` and register it uppercase; import/register material under `Assets/Materials/MobMaterial/`; add localization where key equals mob name. Tutorial conventions say mob IDs must be unique and sequentially increasing, and names/rarities uppercase. This is documented project procedure; current editor-version behavior was not independently validated.

## Documented authoring workflow: add a mutation

Tutorial sequence: register it in `MutationEnum`; create material/effect; match asset registration name with `EffectKey` in `mutation.csv`; add property in `MobMutation`; add effect/property registration in `Mob.prefab`; add localization; update `MUTATIONS_NAME` in `MutationConfig.fcg`; search for `WARN: Add color for new mutation` and add relevant HUD colors. The current source has Golden/Frozen/Magma mappings and the known schema mismatch; verify before editing.

## Rebirth

Tutorial says add a row to `rebirth.csv`; it gives no further detailed step sequence.

## Reader/schema warning

`MutationConfigEnum` defines `Tier=7` and `FusionWeight=6` in generated symbols; current `mutation.csv` ends at index 5, while `MutationConfig.fcg` reads Tier index 7 and does not read FusionWeight. This is a high-confidence **static concern**, not reproduced runtime failure. See [known issues](../troubleshooting/known-issues.md).

## Sources

- `Craftland-Extraction/05_CRAFTLAND_KNOWLEDGE.md`
- `Craftland-Extraction/10_WORKFLOWS.md`
- `Craftland-Extraction/09_BUGS_AND_SOLUTIONS.md`
- `Craftland-Extraction/02_COMPLETE_FILE_INDEX.md`
