# NEW REUSABLE PROMPT — Craftland skill maintenance

**Purpose:** Update Craftland skills without duplicating detailed reference knowledge.

**Required input:** New verified information/source; proposed target skill; current relevant reference pages; repository version/date.

**Prompt:**

> Maintain the Craftland skills using the supplied verified source. Decide whether this is reusable general Craftland guidance or project-specific repository process. Keep `SKILL.md` concise and move detailed facts into the canonical knowledge reference. Cite evidence, preserve unknowns, update only affected cross-references, and add a changelog entry. Do not rewrite the historical extraction, promote assumptions to facts, overwrite an existing global skill, or claim tests that were not run.

**Expected output:** Small proposed skill/reference changes, evidence labels and paths, affected links, changelog entry and audit results.

**Basis:** Newly authored from `skills/craftland-core/SKILL.md`, `skills/craftland-project/SKILL.md`, and `CONTRIBUTING.md`. Not a recovered prompt.
