# Player experience and feature surface

The extracted source supports a player loop organized around owning a base, acquiring/displaying pets, collecting pet-generated value, improving progression through rebirth, and interacting with parade pets and other players' pets. This is a source-based description of feature surface, not a measured user-experience assessment.

Observed player-facing HUD assets: Debug, LaserWallInteract, Leaderboard, Mail, Menu, PetInteract, Prompt, Ranking, Rebirth, Wallet. Their controllers are documented in `Assets/Scripts/HUDs/` and summarized in [UI overview](../ui/ui-overview.md).

Interaction topics supported by source declarations include buy/sell/steal pet flows, laser-wall unlock and confirmation, rebirth requirements/rewards/confirmation, wallet updates, local leaderboard tabs and live ranking display. Exact visible text, usability, accessibility, balance quality and mobile-device behavior were not evaluated.

## Unknowns

- No play session, usability study, device test, or balance/performance measurement was run.
- Whether each tutorial step still matches the current editor release is not established.
- Some interface assets/controllers such as Mail are present, but external service behavior is not established by presence alone.

## Sources

- `Craftland-Extraction/04_SCRIPT_DOCUMENTATION.md`
- `Craftland-Extraction/05_CRAFTLAND_KNOWLEDGE.md`
- `Craftland-Extraction/14_UNKNOWN_INFORMATION.md`
