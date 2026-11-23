# Contributing and knowledge maintenance

## Updating with verified information

1. Identify the information class and source artifact: project text, editor observation, authored tutorial, test result, or external documentation.
2. Identify which project the information belongs to; search knowledge, both indexes, and the relevant extraction (`rg`) to avoid duplicate explanations.
3. Add the information to one canonical page under `knowledge/`; keep project-specific implementations separated and cite exact extraction filenames and original project-relative asset paths.
4. Apply a status label: `VERIFIED`, `OBSERVED`, `INFERRED`, `UNVERIFIED`, or `UNKNOWN`. Record scope/date for editor snapshots and tests.
5. Update `craftland-core` only for Craftland guidance supported across projects or explicitly scoped. Update `craftland-project` for repository process/index changes. Avoid putting detailed references in either skill.
6. Update indexes/cross-references only where affected. Record important decisions in `REPOSITORY.md` or a dedicated decision record if one is needed.
7. Add a dated entry to `CHANGELOG.md`.
8. Audit links, frontmatter, both script counts, ECA counts, source hashes, duplicate content, and secret patterns. Do not run or claim game validation as a documentation check.

## Review checklist

- Source exists, was actually read, and is cited.
- Facts and interpretations are separated; unknowns remain explicit.
- No unrelated pages changed.
- Paths/links resolve or are explicitly described as external historical source paths.
- Both original project roots and the Project 5 extraction snapshot remain unchanged.
- Project 6's inventory and script-index paths remain aligned; 14 instruction copies remain hash-identical to original files.
- No credentials, tokens, or unnecessary data-storage identifiers are present.
- Script copy decisions meet the policy in `scripts/index/README.md`.
