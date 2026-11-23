# FC functions, APIs, parameters and outputs

This reference directs readers to the complete searchable declarations in [fc-script-index.md](fc-script-index.md). Each script entry records declared function signatures (parameter/return types, including `out` parameters where listed), event entry points, imports, and compact observed engine-call names. Functions without a parsed declaration are explicitly noted as having none parsed; this does not prove the script has no internal statements or behavior.

The extraction's indexing process read all 63 `.fcg` sources completely. The documentation intentionally avoids copying every implementation body or inventing a prose description for each branch. Original project-relative paths are preserved as text. Detailed changes require opening the source file in the old project and re-reading its full implementation.

## Important limits

- The index is not an API reference for all Craftland FC. Verify current standard-library `.fcc` declarations and editor docs.
- Output/side-effect details that the extraction did not establish point back to source rather than guess.
- No compiler/runtime validation was run during the extraction.

## Sources

- `Craftland-Extraction/04_SCRIPT_DOCUMENTATION.md`
- `Craftland-Extraction/08_API_AND_INTEGRATIONS.md`
