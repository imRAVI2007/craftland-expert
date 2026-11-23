# Repository guide

## Structure

```text
Craftland-Extraction/             Immutable copied source documentation (15 files)
skills/craftland-core/            Concise reusable global Craftland skill
skills/craftland-project/         This repository's maintenance skill
.agents/skills/craftland-project/ Codex-discoverable repo-local copy of the project skill
sources/hungry-fish-2.0/           Project 6's inventory, script index, and 14 verbatim instruction copies
knowledge/projects/                Isolated project-specific references
knowledge/project-comparisons/     Evidence-limited comparison across both projects
knowledge/player-data/             Project-specific PlayerData and player-state references
knowledge/persistence/             Project-specific DataStorage flows
knowledge/leaderboards/            Project-specific ranking/result flows
knowledge/workflows/               Project-specific authoring workflows
knowledge/fundamentals/           Template identity, editor concepts, terminology
knowledge/gameplay/               Gameplay systems, map settings, player experience
knowledge/scripting/              Separate 63- and 93-entry FC references plus 18 Project 6 module notes
knowledge/prefabs/                Project-specific 27- and 70-prefab inventories
knowledge/ui/                     Project-specific 10- and 20-UI inventories
knowledge/csv/                    CSV schemas and documented authoring procedures
knowledge/eca/                    One Project 5 built-in and three Project 6 local ECA observations
knowledge/maps/                   Scene hierarchy and documented map workflows
knowledge/troubleshooting/        Static concerns, symptoms and evidence-qualified debugging
knowledge/tutorials/              Archive locator and tutorials synthesis
prompts/                           Eight NEW REUSABLE PROMPTS, derived from verified workflows
scripts/by-category/              Empty until vetted reusable source copies are approved by quality criteria
scripts/index/                    Script library index and reuse policy
research/                          Evidence-status register and two-project source register
tools/                             Read-only FC declaration index refresh utility
```

## Knowledge policy

Use labels precisely: **VERIFIED** means directly supported by a named file/editor record; **OBSERVED** means captured as a state/structure by the extraction but not behaviorally tested; **INFERRED** means a reasoned interpretation, labeled as such; **UNVERIFIED** means a static concern or claim not validated; **UNKNOWN** means evidence is absent. Source references use extraction-relative paths and original project-relative paths. Do not imply project files are packaged when they are only referenced.

Keep one canonical explanation per topic. Other pages link to it. Preserve each project's source spelling and terminology, even when names appear inconsistent (for example, `Steal A Pet Template` versus `Steal A Shape`, or `FronzenEffect`). Similar names or shared APIs do not prove identical implementations.

## Script reference policy

Keep two independent searchable indexes: 63 Project 5 scripts in `knowledge/scripting/fc-script-index.md`, and 93 Project 6 scripts in `knowledge/scripting/hungry-fish-2.0-script-reference.md` plus its CSV. Source paths refer to their respective original project roots and do not imply code is copied here. Never infer function behavior beyond recorded source review. No original FC source copies are approved in `scripts/by-category/`.

## Prompt provenance

No dedicated saved AI prompts were recovered from either extraction. Each prompt under `prompts/` is marked **NEW REUSABLE PROMPT**. Project 5's archived instructions/tutorials remain in its immutable extraction. Project 6's 14 local instruction copies (13 unique texts) are preserved under `sources/hungry-fish-2.0/instructions/`; they are not user prompt templates.

## Original extraction

The 15 Project 5 Markdown documents remain preserved verbatim under `Craftland-Extraction/`. The Project 6 original project and full extraction remain read-only at `D:\My project (6)`; selected indexes and instruction copies are preserved here. See `research/project-sources.md` for coverage and limits. Never replace either historical source silently.



