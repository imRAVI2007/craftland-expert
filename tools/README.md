# Repository tools

## FC script declaration index

`build_fc_script_index.py` reads the 63 original `Assets/Scripts/**/*.fcg` files from a supplied old-project root and refreshes declaration-level fields, event signatures, and function signatures in `knowledge/scripting/fc-script-index.md`. It does not write to the original project or copy source code. Run from this repository:

```powershell
python tools/build_fc_script_index.py --project-root 'D:\path\to\old-project'
```

The tool expects exactly 63 source files and 63 matching index headings; it stops with an error if counts differ. Its parser is declaration-oriented and intentionally does not claim to validate FC semantics, runtime behavior, or compiler compatibility. Review changes and refresh provenance/limitations when the upstream source version changes.
