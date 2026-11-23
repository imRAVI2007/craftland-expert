# Hungry Fish 2.0 project workflows

These workflows summarize local project guidance and source relationships. They are project-specific and may depend on Craftland Studio version 1.19.4689915 / managed agent package 0.5.3 as recorded by the extraction. They are not universal Craftland instructions.

## FC work

Before FC coding in the original project, its guidance requires reading root `AGENTS.md`, `.craftland/agents/rules/fc-workflow.mdc`, and the scoped skills under `.craftland/agents/skills/`. Verify APIs, imports, types, enum values, generated symbols, and asset IDs against project/editor sources. `Temp/UGCLanguage/editorGen/` is read-only generated reference. The project workflow requires compilation after edits; this knowledge build performed no edits/builds. Archived wording is preserved as text files under [the instruction archive](../../sources/hungry-fish-2.0/instructions/).

## Editor-owned assets

Use Craftland Studio for scenes, prefabs, UI, ECA, asset registration, and other serialized editor-owned assets. Do not guess serialized formats. Read current connected editor instructions before invoking editor tools. This project guidance is captured for historical reference; active tool availability and instructions must be rechecked.

## Fish/configuration change trace

For fish configuration, trace `Assets/Config/fish_config.csv` → `Config/FishConfigReader.fcg` → player controller configuration and `OnSetPlayerConfig`; inspect registered model/material/UI assets and current editor bindings before editing. The extraction does not provide complete verified semantics for each table column.

## Source maintenance boundaries

Treat the original project as read-only unless a separate task explicitly authorizes changes. This repository contains no `.fcg` copies. Index/filter the 93-script CSV and then consult the original source path. Runtime/build behavior must be tested in an authorized project/editor session before claiming validation.

**Sources:** `D:\My project (6)\Craftland-Extraction\10_WORKFLOWS.md`, `15_SKILL_KNOWLEDGE.md`, and `03_PROMPT_LIBRARY.md`.
