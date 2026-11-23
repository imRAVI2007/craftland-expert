# Dependencies

## Runtime/editor dependencies visible in files

- Craftland Studio project/editor and its registered content types.
- Craftland FC toolchain, with configuration at root `fcconfig.json` and `Temp/UGCLanguage/fcconfig.json`.
- Craftland standard/generated FC libraries in `Temp/UGCLanguage/editorGen/` and package/cache locations.
- Project-local CSV data and localization sources consumed by FC config graphs.
- Project content assets: meshes, prefabs, UI, materials, sprites, textures, sounds, animation controllers.
- Craftland Data Storage service configured in `ProjectSettings/DataStorage.asset` (PlayerSave, IncomeRank and WealthRank sheets). IDs intentionally omitted.

## Conventional software package manifests

No `package.json`, `requirements.txt`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `pom.xml`, `composer.json`, `Gemfile`, `Pipfile`, or JS lockfile appeared in the full path inventory. The inventory has zero `.html`, `.htm`, `.css`, `.js`, `.mjs`, `.ts`, `.tsx`, `.py`, `.sh`, `.ps1`, `.bat`, or `.cmd` files. No conventional website/server package dependency set is present in this workspace.

## Built-in libraries and cache

`Cache/fab_stdlibrary/` and generated language/cache folders contain editor/runtime support data and should not be treated as project-authored source dependencies for redistribution without checking licensing and project rules. `.gitmodules` declares a CoreLib submodule at `Assets/Scripts/SharedLibs/CoreLib` while the actual checked-in-looking sources are under `_SharedLibs`; no Git metadata is available to verify origin or history.
