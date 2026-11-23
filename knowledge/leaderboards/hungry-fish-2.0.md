# Hungry Fish 2.0 leaderboards and match results

Two related but distinct paths are described:

1. **Persistent ranking data:** `Player/PlayerRankingData.fcg` reads ranks 1–120 from `KillRanking` and `ScoreRanking`, matches stored names to find a player's rank, uses `120+` if absent, and calls the built-in leaderboard write for current kill and score totals. `Player/PlayerScoreData.fcg` loads lifetime elimination/score values.
2. **Round/match ranking and results:** `Player/PlayerScore.fcg` maintains per-player round score/ranking interfaces. Server `Global/ScoreManager.fcg` syncs score maps, removes quitters, waits five seconds after result phase begins, then sends ranking data and calls result upload. `HUD/MatchResultUI.fcg` creates a built-in multi-team result HUD at End, sorts by score, fills player/team/score arrays, and selects `GameResultType.Booyah`.

`Ranking.ui`, `KillRanking.ui`, `ScoreRanking.ui`, `MatchRanking.ui`, and related item components are editor-observed assets. Exact UI bindings and the interaction between persistent rank reads and the live round display require current project/editor inspection.

No leaderboard read/write, ranking order, service response, or result upload was exercised. This feature does not imply a website or external leaderboard service.

**Sources:** `D:\My project (6)\Craftland-Extraction\04_SCRIPT_DOCUMENTATION.md`, `05_CRAFTLAND_KNOWLEDGE.md`, `08_API_AND_INTEGRATIONS.md`.
