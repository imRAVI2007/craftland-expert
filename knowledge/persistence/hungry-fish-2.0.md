# Hungry Fish 2.0 persistence

This project uses Craftland DataStorage APIs imported from `Database.fcc`; this is not evidence of an external database vendor, SQL server, or website backend.

| Module | Sheet and fields in extraction | Recorded flow |
|---|---|---|
| `Player/PlayerWalletData.fcg` | `Wallet`: `Coin` | Read retries up to 10 on result `-1`; defaults absent balance to 0, dispatches it, then writes. Write retries are for `DataStorageTimeout`. |
| `Player/PlayerInventoryData.fcg` | `Inventory`: `Fish`, `Effect` | Reads/retries nil values, fills default unlocked/locked lists, dispatches and persists sync changes. |
| `Player/PlayerLoginData.fcg` / `Player/PlayerLogin.fcg` | `Login`: `LastTimestamp`, `Reward`, `LastLoginDay` | Reads/sends login state; login/reward changes sync back at End. |
| `Player/PlayerScoreData.fcg` | `Score`: `Elimination`, `Score` | Reads lifetime values and retries zero-valued results; sync persists both. |

The extraction reports timeout-specific retry limits, but terminal non-timeout errors are not handled consistently in the source summaries. `PlayerScoreData` treats zero as a retry condition even though zero can be valid. These are static resilience observations, not confirmed incidents. No DataStorage request was run; service availability, ordering, quotas, and live schema are unknown.

**Sources:** `D:\My project (6)\Craftland-Extraction\04_SCRIPT_DOCUMENTATION.md`, `08_API_AND_INTEGRATIONS.md`, `09_BUGS_AND_SOLUTIONS.md`.
