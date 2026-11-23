# Craftland Expert

Craftland Expert is a source-backed Free Fire Craftland knowledge repository with separate, traceable evidence for two projects: **Steal A Pet Template** (Project 5) and **Hungry Fish 2.0** (Project 6). Similarities across these samples are not assumed to be universal Craftland behavior.

## Knowledge library

The repository covers fundamentals, gameplay, FC scripting, CSV/configuration, maps/scenes, prefabs, UI, ECA, player data, persistence, leaderboards, workflows, troubleshooting, and project comparisons.

- [Project source register](research/project-sources.md) states each source location, coverage, and limitations.
- [Project 6 inspection plan](research/project-6-inspection-plan.md) prioritizes the remaining inventory with explicit coverage limits.
- [Project comparison](knowledge/project-comparisons/project-5-vs-project-6.md) contrasts the two implementations.
- Project 5 has a 63-entry [FC script index](knowledge/scripting/fc-script-index.md), 27 prefab trees, 10 UI trees, and one read-only built-in ECA graph.
- Project 6 has a 93-entry [FC script index](knowledge/scripting/hungry-fish-2.0-script-reference.md), detailed notes for 18 modules, three observed local ECA graphs, 70 project prefabs, 20 UI trees, and 27 PlayerData entity definitions.
- Project 6's complete baseline inventory and searchable script index CSVs, plus 14 verbatim instruction-file copies, are in [sources/hungry-fish-2.0](sources/hungry-fish-2.0/README.md).

Project 5's 15-document extraction is preserved in [`Craftland-Extraction/`](Craftland-Extraction/). Project 6's full 15-document extraction remains read-only at `D:\My project (6)\Craftland-Extraction\`; 252 files were inspected for content or structure from its 2,840-file baseline. The other 2,588 have inventory coverage and targeted scans for some text only. The extraction does not enumerate eight additional support-file paths individually; [inspection gaps](research/project-6-inspection-gaps.md) records this uncertainty. Neither extraction claims runtime/build validation.

## Skills

- [Global skill](skills/craftland-core/SKILL.md): evidence-led Craftland assistance; identifies project-specific references and keeps implementations distinct.
- [Project skill](.agents/skills/craftland-project/SKILL.md): repo-discoverable maintenance workflow. The packaged copy at `skills/craftland-project/SKILL.md` is kept byte-identical.

## Use

Read [REPOSITORY.md](REPOSITORY.md), identify the project, then open its project reference and script index. Preserve source paths and evidence labels. Use the [prompt library](prompts/) for eight clearly marked **NEW REUSABLE PROMPTS** based on documented workflows. The two-project extraction found no dedicated saved user prompt templates; Project 6's archived instruction files are not prompts.

## Limits

Project-specific mechanics, data schemas, IDs, asset counts, and workflows are not interchangeable. Website, Discord, authentication, deployment, and external API systems were not established in the inspected local project trees; absence beyond those scopes is unknown. Project 6's inventory is complete but semantic inspection is partial. No open-source license has been selected; see [LICENSE](LICENSE). The repository has not been uploaded to GitHub.

See [INSTALL.md](INSTALL.md) for the global core-skill installation and update process.
