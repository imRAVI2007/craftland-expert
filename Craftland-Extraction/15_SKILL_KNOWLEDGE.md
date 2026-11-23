# Skill Knowledge Seed

This file consolidates stable, project-supported guidance for a future Craftland Expert Skill. It is a seed, not a claim that all Craftland editor behavior has been reverse-engineered.

## Project-specific authoring

- This project is a pet-collection/base-management Craftland template.
- CSV configuration: global, mob, mutation and rebirth tables under `Assets/CSV/`; localization under `Assets/Localization/key.csv`.
- For new content follow the English/Vietnamese tutorials and then verify current asset registration and generated FC symbols in Craftland Studio.
- Keep mob IDs unique/sequential and names/rarities uppercase as documented by tutorials; mob localization key matches the mob name.
- A mutation spans data/config, enum, material, effect prefab, component registration, localization and UI color treatment.

## Agent handling rules

- Treat Craftland Studio as the authority for non-text assets and editor-owned serialized content.
- Read `.craftland/agents/rules/fc-workflow.mdc` before any FC task. Read scoped skills as routed there.
- Never invent APIs, symbols, enum values, component names, asset IDs, or entity IDs. Verify them against current generated libraries or MCP.
- Do not hand-edit generated `Temp/UGCLanguage/editorGen/` files or opaque serialized formats such as `.eca`.
- Use registered `ERes*`/`Res` symbols for edit-time-known project assets where applicable; do not use hard-coded asset name/id strings as a substitute for registration.
- FC edits are incomplete until lint/fix and full compile validation finish; this rule is for coding work and was not exercised during this read-only extraction.

## Editor-wide guidance requiring project/task-specific verification

The Craftland MCP entity guide warns that mesh placement collision is not automatic, material slots depend on mesh submeshes, and ground height varies by map. A future skill should preserve these as editor guidance and require schema/current-scene checks before action rather than assume them for every asset.

## Gaps before skill publication

Finish complete script semantics, exact verbatim instruction/prompt archive, editor entity/component analysis, stable toolchain/library mapping, prompt de-duplication, and verification status. Keep generic editor facts, project-authored rules, and inferences in separate sections.
