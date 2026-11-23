# NEW REUSABLE PROMPT — Craftland debugging

**Purpose:** Diagnose a Craftland issue while separating static evidence from reproduction.

**Required input:** Exact symptom/reproduction steps; project/editor version/session; scene/map and asset paths; logs/compiler messages; relevant source/data; what validation has already run.

**Prompt:**

> Help investigate this Craftland issue from the supplied evidence. Start by recording scope and reproduction state. Trace the relevant FC, CSV/config, component/prefab/UI/ECA and player lifecycle paths as needed. Verify APIs/schemas with current sources. Separate observed symptoms, verified source facts, inferences, and unknowns. Propose the smallest diagnostic next step before suggesting a fix. Do not edit opaque serialized assets, guess APIs, call a static suspicion a confirmed bug, or claim a fix worked without validation.

**Expected output:** Evidence map, likely causes ranked by confidence, safe diagnostic steps, unresolved questions, and exact validation needed.

**Basis:** Newly authored from `knowledge/troubleshooting/debugging-guide.md` and `knowledge/troubleshooting/known-issues.md`. Not a recovered prompt.
