# Design Decisions

## Documented decisions

- Project balance/content tables are CSV-backed: this is documented in both tutorials. The tutorials call the underlying source “Google Sheets”; the workspace only establishes local CSV copies, not a live Sheets API connection.
- Mob naming and rarity conventions are uppercase; mob identifiers are sequential and unique, per tutorial.
- Mob localization key equals mob name, per tutorial.
- New mutations are represented across enum/config, material, prefab/effect, localization and HUD color presentation, per tutorial.
- FC symbol and project asset references must be verified using Craftland-generated sources and asset registration; do not hardcode asset identifiers. This is a coding governance decision in the official project workflow.

## Inferences (not confirmed rationale)

The file layout suggests separation into config readers, managers, player/mob behavior, HUD controllers, shared state/database controllers, and utility modules. This is a structural inference from source paths and graph names, not a recorded architecture decision.

## Missing rationale / history

No ADR/decision log, PR history, issue history, or reliable Git history has been found. Do not attribute motivations or author identities without evidence.
