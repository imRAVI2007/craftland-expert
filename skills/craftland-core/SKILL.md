---
name: craftland-core
description: A reusable Free Fire Craftland technical knowledge and assistance skill for map creation, scripting, gameplay mechanics, editor workflows, troubleshooting, documentation and technical research.
---

# Craftland Core

## Evidence first

Craftland details vary by project and editor version. Use current project/editor evidence; never fill gaps from analogy. In this repository, identify the source project first, then browse `knowledge/` and cite its exact source path. The two extracted projects are separate implementations: a pattern in both is evidence across two samples, not a universal Craftland rule.

Use **VERIFIED**, **OBSERVED**, **INFERRED**, **UNVERIFIED**, and **UNKNOWN** as defined in `research/knowledge-status.md`. Preserve technical spelling and distinguish archived project guidance from observed implementation. State when behavior was not runtime-tested. Do not include credentials, private identifiers, or local toolchain paths.

## Task workflow

1. Identify the project, requested artifact, and evidence available. Load `craftland-project` too when maintaining this repository.
2. For FC, open the index for the selected project: `knowledge/scripting/fc-script-index.md` (63 scripts, `Assets/Scripts/`) for Steal A Pet Template, or `knowledge/scripting/hungry-fish-2.0-script-reference.md` plus its CSV (93 scripts, `Assets/_Scripts/`) for Hungry Fish 2.0. Verify symbols/APIs against current `.fcc` references or editor docs. Treat generated symbols as read-only and follow the selected source project's workflow.
3. For gameplay, trace the related managers, controllers, CSV/config and UI/prefab bindings together. Do not infer execution order or online behavior from names alone.
4. For prefab/UI/entity settings, inspect current Craftland Studio schemas and assets when available. Entity property definitions combine type, component, and instance definitions; do not guess property names. Custom mesh creation alone does not establish collision behavior.
5. For CSV, compare header, row shape, enum indices, and reader code. Record unit assumptions and mismatches; do not silently normalize authoring data.
6. For scenes/maps, check the selected map and its ground/terrain context before using coordinates or spawn assumptions.
7. For ECA, inspect through Craftland Studio when available; do not hand-edit opaque serialized `.eca` files. This repository contains one built-in graph observation from Project 5 and three project graph observations from Project 6; neither establishes general runtime behavior.
8. Troubleshoot by collecting source path, editor/log evidence, and reproduction state. Separate static concerns from reproduced issues and fixes.
9. Research unknown features using current authoritative documentation/editor evidence where possible. Record search scope and date; if not established, say `UNKNOWN`.

## Scope and limits

The repository contains project-specific evidence for **Steal A Pet Template** and **Hungry Fish 2.0**, plus an explicit comparison at `knowledge/project-comparisons/project-5-vs-project-6.md`. The second extraction inventoried 2,840 files but semantically inspected 252; do not claim full project coverage. Neither extraction performed runtime/build validation. Website, Discord, authentication, deployment, and external API systems were not established in the inspected local projects. Start at `research/project-sources.md` and preserve each project's distinct scripts, configurations, assets, and unknowns.
