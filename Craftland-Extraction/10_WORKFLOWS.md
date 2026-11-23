# Workflows

## FC coding workflow (project-authored)

`AGENTS.md` requires `.craftland/agents/rules/fc-workflow.mdc` for every FC task. That workflow routes symbol lookup, asset checks, registration, editing and validation. It prohibits invented FC APIs/project symbols and editing generated `Temp/UGCLanguage/editorGen/` sources. Any FC edit requires `fc-lint-fix` and a full `fccompile.exe -i Assets` validation or equivalent editor build. No FC edit was made here.

## Project content workflows documented by tutorials

### Add mob

1. Add configuration row in `Assets/CSV/mob.csv`.
2. Import mob mesh under `Assets/Meshes/Mobs/` and register it uppercase.
3. Import material under `Assets/Materials/MobMaterial/` and register it.
4. Add a localization row to `Assets/Localization/key.csv`, with key equal to mob name.
5. Mob IDs are to be unique, sequentially increasing; mob name and rarity are uppercase.

### Add mutation

Tutorial sequence: register enum in `MutationEnum`; create material and effect; align asset registration name with `EffectKey` in `mutation.csv`; add property in `MobMutation`; add effect/property registration in `Mob.prefab`; add localization; update `MUTATIONS_NAME` in `MutationConfig.fcg`; search `WARN: Add color for new mutation` and add colors in relevant HUDs.

### Add rebirth

Tutorial directs adding a row to `Assets/CSV/rebirth.csv`; no additional tutorial steps were supplied.

## Craftland editor procedures

Editor-specific workflow beyond project FC rules is sourced in the MCP instruction resources and needs to be summarized alongside the asset sections in later batches. This task used editor reads only, with no save/write/build operation.
