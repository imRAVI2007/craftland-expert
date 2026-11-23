# Project Overview

## Scope and method

Read-only extraction started 2026-11-23 in `D:\My project (5)`. No original files were edited, moved, renamed, deleted, compiled, or executed. The only workspace writes so far are documentation under `Craftland-Extraction/`.

The complete file metadata inventory is in [02_COMPLETE_FILE_INDEX.md](02_COMPLETE_FILE_INDEX.md): 963 regular files, 169,825,426 bytes. This includes cache, generated toolchain data, `.meta` companions, binaries and editor-owned project data. Inventory is not the same as content-level inspection; opaque binary/serialized data needs editor inspection.

## Project identity and observed structure

- Root contains `main.gproj`, `fcconfig.json`, `AGENTS.md`, English and Vietnamese tutorials, and Craftland project folders (`Assets/`, `ProjectSettings/`, `Temp/`, `Libraries/`, `Cache/`).
- Source language is Free Fire Craftland FC: 63 `.fcg` files under `Assets/Scripts/`; no source `.fcc` file is listed by Craftland Studio. `Temp/UGCLanguage/editorGen/` contains generated `.fcc` symbol libraries and is read-only.
- `Assets/` contains gameplay source, CSV tuning tables and localization, HUDs, prefabs, materials, meshes, textures, sounds, and one scene.
- The editor-connected asset catalog reports 1 scene, 32 prefabs (some built-in/read-only), 10 UI assets, 63 FC scripts, 1 ECA asset and project configuration modules. `MainScene.scene` reports 1,186 child entities; the MCP response includes an additional synthetic scene root, for 1,187 entity rows.
- The workspace is **Steal A Pet Template**, evidenced by both tutorials and game systems/scripts for pets, bases, stealing, mutations, rebirth, leaderboards, wallet, and pet parade.

## Extraction workflow

1. Inventory all accessible regular files and classify by path, extension, and size.
2. Read applicable root and `.craftland/agents/` workflow instructions before FC or editor-owned asset inspection.
3. Inspect project documentation, FC source, config/CSV, and generated FC references read-only. Do not execute unknown scripts or run builds.
4. Use Craftland Studio MCP for scene, prefab, UI, ECA, and other editor-owned serialized content; start with `instructions://index`.
5. Search saved prompt/instruction material and preserve original wording where relevant; do not treat normal in-game localization strings as AI prompts.
6. Record evidence, uncertainty, missing systems, and cache/generated-file exclusions in the corresponding numbered documents.
7. Cross-check references and counts against the inventory and editor asset catalog. Report any validation deliberately not run because this is a read-only investigation.

## Progress index

| Area | Status |
|---|---|
| Full path/size inventory | Complete; see 02 |
| Project FC workflow read | Complete; `.craftland/agents/rules/fc-workflow.mdc` |
| Craftland Studio MCP availability and index | Connected; `instructions://index` read |
| Text source and prompt extraction | All 17 local Markdown/MDc instruction/tutorial sources copied verbatim; 0 dedicated AI prompts; duplicate check complete |
| Scripts | 63 FC source files indexed; one built-in ECA graph read; feature summaries and concerns recorded in 04/09 |
| Scene/prefab/UI detail | Main scene, all 27 local prefab entity trees, and all 10 local UI entity trees inspected through MCP |
| Website/Discord | No website source or Discord server/bot export in full file/content search; see 06/07 |
| Git/history | Root is not a Git repository; no nested repository metadata; cache/history review complete |
| Quality check | Complete: requested files, local references, source archive, counts, and secret-pattern scan checked |

## Evidence and limits

Facts in this extraction are labeled as observed from project files, Craftland Studio MCP, or project-authored tutorials/rules. Generic Craftland knowledge is not presented as verified project behavior. This workspace contains game-editor project data, not an HTML/CSS/JS website, Discord server export, or deployment project. Absence from this project does not prove those systems do not exist elsewhere.

## Final coverage record

- 963/963 accessible project files have a path and byte-size inventory entry. This is a metadata inventory, not a claim that every binary/cache file was semantically decoded.
- Complete text was read for all 63 `.fcg` sources. Each has a searchable entry in 04 with source reference, imports, declarations/entry points and observed calls; central runtime systems also have behavior summaries. No source was executed or compiled.
- Seventeen local Markdown/MDc sources were archived verbatim in 03: project/agent/tool instructions and the two tutorials. Duplicate check found one identical pair of asset-rule documents. No saved dedicated model prompt was found; project strings named `PROMPT_*` are game UI/localization messages.
- Craftland Studio read-only inspection covered the current scene, 27 local prefab trees, 10 UI trees, definition catalog, configuration modules and one ECA graph. This established entity structure and schemas, not playtest outcomes or a semantic review of every transform/material/property value.
- Final checks: all 15 requested docs exist; 963 inventory rows; 63 FC script entries; 17 source archives; no broken Markdown links in the docs; no secret-pattern hits. Original project files remain outside the extraction folder and were not intentionally modified.
- Remaining scope limits and unavailable evidence are listed in 14. In particular, no website, Discord export, Git history, runtime test/build result, or accessible chat history was present locally. This extraction is substantial and source-verified, but does not claim complete semantic understanding of every opaque serialized/binary asset.
