# Website Architecture

## Finding

The accessible workspace inventory shows a Craftland UGC game project, not a conventional website source tree. No HTML, CSS, JS, TS, web framework manifest, frontend entry point, web API route, web deployment config, or website build config was found in the initial full path inventory.

There are UI assets (`Assets/HUDs/*.ui`) and FC UI controllers under `Assets/Scripts/HUDs/`. These are in-game HUDs authored for Craftland and must not be described as website pages or CSS components.

## Leaderboard

The project contains `Assets/HUDs/Leaderboard.ui`, `Ranking.ui`, `Assets/Scripts/HUDs/HudLeaderboard.fcg`, `HudRanking.fcg`, `Assets/Scripts/Manager/LeaderboardManager.fcg`, and `GlobalLeaderboard.fcg`. This is an in-game feature. `LeaderboardManager` uses Craftland Data Storage leaderboard calls for persistent `IncomeRank` and `WealthRank`; `GlobalLeaderboard` separately sends a live match ranking to clients every 10 seconds. See 04. No external website leaderboard was found.

## Missing website evidence

No database schema/dump, authentication system, hosting/deployment configuration, responsive web design, CSS design tokens, or website integration is present in the inventory. Craftland Data Storage sheets are part of the game's runtime persistence, not a conventional website database. The tutorials' reference to Google Sheets for balance data is not proof of a live Sheets integration; local CSVs are the observed source files.
