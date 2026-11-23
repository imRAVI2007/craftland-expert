# NEW REUSABLE PROMPT — Craftland FC script analysis

**Purpose:** Analyze an FC script without guessing APIs or behavior.

**Required input:** FC source text or exact source path; project/editor context; analysis question; generated `.fcc`/symbol references if symbol-level explanation is requested.

**Prompt:**

> Analyze the supplied Craftland FC source. Preserve exact graph, function, type, event, import, enum and component names. Separate statements directly visible in code from interpretation. Trace declared inputs, outputs, side effects and imported project modules; verify external symbols against their owning `.fcc` or current editor documentation. Identify dependencies and related scripts. Record untested branches and unknown semantics. Do not change the source, invent APIs, or claim compilation/runtime validation unless performed.

**Expected output:** Script identity/path, declarations and signatures, flow summary, dependencies/cross-references, evidence citations, limitations and validation status.

**Basis:** Newly authored from `knowledge/scripting/fc-script-overview.md`, the 63-entry index, and archived FC symbol/workflow rules in `Craftland-Extraction/03_PROMPT_LIBRARY.md`. Not a recovered prompt.
