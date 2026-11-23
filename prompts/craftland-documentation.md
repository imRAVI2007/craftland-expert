# NEW REUSABLE PROMPT — Craftland documentation

**Purpose:** Turn inspected Craftland evidence into traceable, non-duplicated technical documentation.

**Required input:** Source files/editor observations, documentation destination, scope, evidence date, and known validation performed.

**Prompt:**

> Document the supplied Craftland information in the single canonical topic page for its category. Cite exact source paths and retain technical terminology. Label each claim VERIFIED, OBSERVED, INFERRED, UNVERIFIED, or UNKNOWN. Keep static code review separate from runtime testing; preserve unresolved information. Search existing docs first and link to related pages instead of duplicating explanations. Do not add unsourced examples or claims.

**Expected output:** Proposed page update, source list, evidence labels, affected cross-references, and changelog note.

**Basis:** Newly authored from `REPOSITORY.md`, `CONTRIBUTING.md`, and `research/knowledge-status.md`. Not a recovered prompt.
