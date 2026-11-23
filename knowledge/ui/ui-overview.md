# UI overview

The project has 10 local HUD/UI assets. Craftland Studio returned the complete entity trees; counts below include the synthetic `UIRootEntity`, while catalog `entityCount` is one lower for each. Structure is observed; layout correctness and runtime behavior were not playtested.

| UI | Returned entities incl. root |
|---|---:|
| Debug | 3 |
| LaserWallInteract | 16 |
| Leaderboard | 85 |
| Mail | 9 |
| Menu | 23 |
| PetInteract | 20 |
| Prompt | 4 |
| Ranking | 6 |
| Rebirth | 59 |
| Wallet | 8 |

Widget types are primarily buttons, images, text, layouts, scroll and profile widgets. Controllers are under `Assets/Scripts/HUDs/`. Some broad relationships are in [script-relationships.md](../scripting/script-relationships.md); project custom components/enums are in [ui-components.md](ui-components.md).

Editor guidance: `computedRect` is resolved/read-only; tint multiplies the source art; callbacks belong on the UI root using the documented signature. Re-check the live tree/schema before making changes.

## Sources

- `Craftland-Extraction/05_CRAFTLAND_KNOWLEDGE.md`
- `Craftland-Extraction/08_API_AND_INTEGRATIONS.md`
