# Prompt and Instruction Library

## Scope

This is an index of prompt-like source material saved in the accessible project. Original source files remain authoritative; the exact source content is not rewritten here. No saved conversation/chat history is assumed. No image-generation or website-generation prompt was identified in the initial inventory/search. `aiPrompt` is a Craftland entity property exposed by the editor documentation; that does not establish that any project entity has a populated prompt.

## Recovered candidates

| Source | Purpose / input / output | Restrictions | Reusable? |
|---|---|---|---|
| `AGENTS.md` | Persistent project rules for agents; input is any task within workspace; output constrains workflow. | Studio is authoritative for game assets; only `.fcc`/`.fcg` may be edited directly; requires workflow for FC tasks and compile validation after edits. | Yes; project-wide instructions. |
| `.craftland/agents/rules/fc-workflow.mdc` | FC task trigger and source-of-truth, editing, registration, validation workflow. | Do not invent APIs/symbols/asset IDs; generated references are read-only; lint/build before delivering FC changes. | Yes; FC tasks. |
| `.craftland/agents/skills/*/SKILL.md` (4 files) | Detailed checklists for asset validation, registration, lint/fix, and FC symbol lookup. | Read-only for this task; exact use is governed by workflow. | Yes; scoped to Craftland/FC tasks. |
| `.github/instructions/craftland-studio-assets.instructions.md` | Editor asset handling guidance. | Craftland Studio required for editor-owned serialized assets; don't guess `.eca` formats. | Yes; all project files. |
| `.github/instructions/fc.instructions.md` | FC coding guidance. | Verify symbols and compile per workflow; generated APIs are authoritative. | Yes; FC. |
| `.github/instructions/fc-examples.instructions.md` | Example-driven FC coding material, mainly Chinese-language, with code snippets. | Examples may be context-specific; verify every API against generated/official references. | Reusable examples, not guaranteed validated for this project. |
| `.github/instructions/fc-import-map.instructions.md` | FC import/library mapping guidance. | Do not guess imports. | Yes; FC imports. |
| `.github/instructions/fc-syntax.instructions.md` | FC syntax guidance. | Syntax reference only; verify semantics/APIs separately. | Yes; FC syntax. |
| `.github/instructions/generate-widget.instructions.md` | Widget generation prompt/instruction. | Requires widget task context and project conventions. | Yes; UI widget tasks. |
| `.cursor/rules/craftland-studio-assets.mdc` | Legacy/current editor asset rule copy. | May duplicate `.github`/root instructions. | Yes; editor assets. |
| `.cursor/mcp.json`, `.vscode/mcp.json`, `.codex/config.toml`, `.vscode/settings.json` | Tool/editor configuration; may contain instruction-like tool routing or launch configuration. | Credentials and private values must not be reproduced. | Environment-specific, not necessarily portable. |
| `Tutorial (EN).md`, `Tutorial (VI).md` | Human project setup guide. Includes exact steps for adding mobs, mutations and rebirth configuration. | Not an AI prompt. The Google Sheets statement is author documentation, not independently verified integration. | Yes, as a project procedure. |

## Original wording preservation

To preserve verbatim wording, use the source files linked above. The extraction copy should include their original text in subsequent completion batches (or cite exact source path and SHA-256). Avoid silently normalizing or translating instructions. Prompt duplicates should be reported as duplicates rather than merged. For secrets and local credential-like material in environment configs, preserve only redacted placeholders or secret-free structural descriptions.

## Prompt search observations

- Search terms included `aiPrompt`, `prompt`, `system instruction`, `developer instruction`, `generation prompt`, and `website generation` across hidden project files. Editor `aiPrompt` fields were separately searched in the scene and all project prefab/UI assets.
- Many `PROMPT_*` hits are gameplay notifications/localization keys in `HudPrompt.fcg`, event settings, and `Assets/Localization/key.csv`; these are **in-game UX text**, not AI prompts.
- `Tutorial (EN).md` and `Tutorial (VI).md` document feature-authoring steps; they are not model prompts.

## Counts after first-pass extraction

- **Dedicated saved AI prompts recovered:** 0.
- **Saved instruction / reusable template sources archived verbatim:** 15 (root `AGENTS.md`, seven `.craftland/agents/` docs, six `.github/instructions/` docs, and one `.cursor` rule).
- **Project tutorials archived verbatim:** 2 (English and Vietnamese); these are human procedures, not prompts.
- **Craftland entity `aiPrompt` values:** 0 across the current scene, all 27 project prefabs, and all 10 local UI assets, queried via `asset-entity-search(hasAiPrompt=true)`.
- **Image-generation, website-generation, Discord-bot, or standalone automation prompt templates:** none found in the inspected local prompt/instruction sources.

The 15 instruction/template sources are saved below exactly as they appear in source files. The phrase “prompt library” is a user-requested document title; it does not imply AI prompts exist in the project.

## Verbatim source archive

The following text is copied verbatim from project-authored instruction/tutorial files (outer code fence only is added). Workspace paths are shown above each block. The locale is retained.

### Source: `AGENTS.md`

`````text
<!-- BEGIN craftland-studio-asset-rules -->
## Synced from craftland-studio-assets.mdc

# Craftland Studio Asset Rules

## Core Rule

Craftland Studio is the authoritative editor for game assets in this project.

- Any access to or modification of game assets must use Craftland Studio.
- Only `.fcc` and `.fcg` files may be edited directly as text and compiled through the FC toolchain.
- If a task involves non-text game assets, especially `.eca` files, the agent must first check whether Craftland Studio is available through MCP.
- If Craftland Studio is not available for the current session, the agent must tell the user to open the game editor first before attempting that asset task.
- The agent must not guess or hand-edit serialized asset formats such as `.eca` when Craftland Studio is required but unavailable.

## Directory Scope

The following directories belong to the Craftland Studio project structure:

- `Assets/` user asset files, including `.fcc` and `.fcg`
- `ProjectSettings/` user configuration asset files
- `Temp/` temporary files, records, debug output, and compilation results
- `Libraries/` library files
- `Cache/` project cache

## Working Rules

- For requests involving `.fcc` or `.fcg`, direct text editing is allowed.
- For requests involving assets under the directories above that are not `.fcc` or `.fcg`, prefer Craftland Studio and related MCP tools.
- Before handling `.eca`, entity attachment, asset registration, scene assets, workflow assets, or other editor-owned assets, first verify whether Craftland Studio MCP is connected.
- Once Craftland Studio MCP is connected, the agent must read `instructions://index` before using other Craftland Studio MCP tools or resources.
- If the MCP is unavailable, stop and ask the user to open Craftland Studio, then retry the task after the editor-side connection is ready.
<!-- END craftland-studio-asset-rules -->

<!-- BEGIN craftland-studio-fc-workflow -->
# Craftland Studio FC Agent Entry

This managed section is for any agent that reads the project root `AGENTS.md`. Craftland Studio sync must update only this section and must not overwrite the user's full `AGENTS.md`.

## Scope

This is a Craftland Studio UGC project. Any task involving `.fcg`, `.fcc`, FC APIs, FC imports, FC diagnostics, or FC generated project symbols is an FC task.

FC tasks mainly involve:

- `Assets/`: user-owned `.fcg` / `.fcc` source files.
- `Temp/UGCLanguage/`: toolchain config, generated libraries, symbol tables, and referenced package caches.

## Required Entry Point

Every FC coding task must read and strictly follow the official Craftland Studio agent workflow:

- `.craftland/agents/rules/fc-workflow.mdc`

Skills must be loaded from:

- `.craftland/agents/skills/`

If the official `.craftland/agents/` workflow is missing or cannot be read, stop and report the missing file. Do not bypass the workflow and handle FC tasks directly.

Legacy `.cursor/rules/` and `.cursor/skills/` FC rules may still exist in older projects, but Craftland Studio no longer maintains them. When `.craftland/agents/` exists, it has higher priority than any existing `.cursor` FC rules.

## Non-Negotiable Rules

- Do not invent FC APIs, types, events, enum values, component names, imports, assetIds, entityIds, or generated project symbols from memory.
- Craftland Studio is the authority for asset registration. Agents must not fake registration by writing FC code; register assets through the Craftland Studio MCP `fc-asset-registration-*` tools or ask the user to register manually.
- Generated files under `Temp/UGCLanguage/editorGen/` are read-only references and must not be edited as user source.
- Any `.fcg` / `.fcc` edit is not complete until full `fccompile.exe -i Assets` validation or an equivalent Craftland Studio MCP build validation has run.
<!-- END craftland-studio-fc-workflow -->

`````

### Source: `.craftland/agents/README.md`

`````text
# Craftland Studio Agent Prompts

This directory is managed by Craftland Studio. When the editor ships a different prompt package version (see `VERSION`), the `rules/`, `skills/`, and `references/` directories here are deleted and rebuilt from the official package.

- Do not edit files in this directory; manual changes will be overwritten.
- Put custom agent rules in the project root `AGENTS.md` (outside the managed section) or in your own rule directories such as `.cursor/rules/`.

`````

### Source: `.craftland/agents/references/fc-syntax.md`

`````text
# FC Syntax Reference

This is an agent-facing syntax reference derived from `FCGLexer.g4` and `FCGParser.g4`.

Use this file only for FC grammar and common syntax forms. For APIs, types, events, enums, components, generated project symbols, imports, and package symbols, use `fc-symbol-lookup`. For assetIds, entityIds, UI objects, script attachments, button bindings, and current editor state, use `fc-asset-check`.

## File Forms

`.fcg` graph files:

```fcg
import "StdLibrary.fcc" as StdLib
import OtherScript as Other from "./OtherScript.fcg"

graph MyGraph {
    count int

    func Start() {
    }
}
```

`.fcc` header files contain imports followed by declarations:

```fcg
import "StdLibrary.fcc" as StdLib

define MyType: int
event MyEvent(value int)
func Helper(value int) int
```

## Imports

Library import:

```fcg
import "StdLibrary.fcc" as StdLib
```

Script reference import (`as Alias` is optional):

```fcg
import ScriptName as Alias from "./ScriptName.fcg"
import ScriptName from "./ScriptName.fcg"
```

## Header Declarations

Type definition:

```fcg
define Health: int
```

Function point type:

```fcg
define Callback: func(player entity<Player>)
```

Alias:

```fcg
alias NumberLike = int | float
alias EntityAndTransform = entity<Player> & Transform
```

Enum:

```fcg
enum Team {
    Red = 1
    Blue = 2
}
```

Tuple:

```fcg
tuple SpawnInfo {
    position Vector3
    yaw float
}
```

Component:

```fcg
component CustomState {
    hp int
    name string
}
```

Event declaration:

```fcg
event PlayerScored(player entity<Player>, score int)
```

Function declaration:

```fcg
func ClampScore(score int) int
```

Declare graph:

```fcg
declare graph EnemyAI {
    target entity<Player>
    func Reset()
}
```

## Decorators

Decorator forms:

```fcg
[readonly]
speed float

[accept entity<Player>]
define PlayerEntity: entity<Player>

[element int]
enum ScoreType {
    Normal = 1
}

[bridging]
component BridgeComponent {
}

[combine Transform, Player]
component PlayerView {
}
```

Custom decorators use bracketed identifiers:

```fcg
[platform_client]
graph ClientGraph {
}
```

## Graph Body

Graph declaration:

```fcg
graph MyGraph {
    score int
    enabled bool = true

    func Start() {
    }

    event Game.Start() {
    }
}
```

Graph members are properties, functions, or event listeners.

Property forms:

```fcg
score int
name string = "player"
team = Team.Red
```

## Function Signatures

Function syntax uses `name Type` parameters and return type after the parameter list:

```fcg
func Add(a int, b int) int {
    return a + b
}
```

Async function:

```fcg
async func LoadData(player entity<Player>) {
}
```

Out parameter:

```fcg
func TryGetScore(out var score int) bool {
    return true
}
```

Anonymous function:

```fcg
var callback = func(player entity<Player>) {
}
```

## Statements

Local variable:

```fcg
var count int
var name string = "abc"
var pos = Vector3{0, 0, 0}
```

Assignment and self modification:

```fcg
count = 1
count += 2
count++
count--
```

Function call:

```fcg
DoSomething(player)
```

Async call:

```fcg
start DoSomething(player)
wait DoSomething(player)
```

Out argument:

```fcg
TryGetScore(out var score)
```

If / else:

```fcg
if count > 0 {
    score += count
} else if count == 0 {
    score = 0
} else {
    score = -1
}
```

Index for loop:

```fcg
for i = 0, count, 1 {
}
```

Range for loop:

```fcg
for i, item in items {
}
```

While:

```fcg
while count > 0 {
    count--
}
```

Return / break / continue:

```fcg
return value
break
continue
```

## Expressions

Cast:

```fcg
value as int
```

Call expression:

```fcg
Math.Min(a, b)
```

Generic or component access:

```fcg
thisEntity<Transform>.Position
player<Player>.Name
```

Field access:

```fcg
position.X
```

Index access:

```fcg
items[i]
```

Type expression:

```fcg
typeof(entity<Player>)
```

Operators supported by grammar:

```fcg
!flag
~mask
-value
a * b / c % d
a + b - c
a << b
a >> b
a & b
a ^ b
a | b
a == b
a != b
a < b
a <= b
a > b
a >= b
a && b
a || b
```

## Types

Primitive and built-in types:

```fcg
object
bool
int
int64
float
string
Vector2
Vector3
Quaternion
LocString
```

Generic types:

```fcg
entity<Player>
List<int>
Map<string, int>
List<entity<Player>>
```

Namespaced type:

```fcg
StdLib.SomeType
```

Function point type:

```fcg
func(player entity<Player>) bool
```

## Literals

Basic literals:

```fcg
nil
true
false
123
0xFF
1.5
"text"
`raw text`
#FF00FF
```

Vector literals:

```fcg
Vector2{1, 2}
Vector3{1, 2, 3}
Quaternion{0, 0, 0, 1}
```

List literal:

```fcg
List<int>{1, 2, 3}
```

Map literal:

```fcg
Map<string, int>{"a": 1, "b": 2}
```

Tuple literal:

```fcg
SpawnInfo{position = Vector3{0, 0, 0}, yaw = 0}
```

LocString literal:

```fcg
LocString{"key.name", List<object>{playerName}}
```

## Common Wrong Patterns

Do not use TypeScript or C# parameter syntax:

```fcg
// Wrong
func Move(player: entity<Player>) {
}

// Correct
func Move(player entity<Player>) {
}
```

Do not put the return type before the function name:

```fcg
// Wrong
int GetCount() {
    return 1
}

// Correct
func GetCount() int {
    return 1
}
```

Do not write graph fields as local variables:

```fcg
// Wrong
var score int

// Correct
score int
```

Do not use constructor-call syntax for vectors:

```fcg
// Wrong
Vector3(1, 2, 3)

// Correct
Vector3{1, 2, 3}
```

Do not call async syntax after the function name:

```fcg
// Wrong
DoSomething(player).wait()

// Correct
wait DoSomething(player)
```

Do not put platform decorators on graph-body event listeners. For client-only or server-only event handling, put the platform decorator on the graph:

```fcg
// Wrong
graph ClientGraph {
    [platform_client]
    event UI.ButtonClicked(button entity<UIWidgetButton>, player entity<Player>) {
    }
}

// Correct
[platform_client]
graph ClientGraph {
    event UI.ButtonClicked(button entity<UIWidgetButton>, player entity<Player>) {
    }
}
```

Do not use package cache paths as imports:

```fcg
// Wrong
import "Temp/UGCLanguage/packages/libId/Some.fcc" as Some

// Correct
import "Some.fcc" as Some
```

`````

### Source: `.craftland/agents/rules/fc-workflow.mdc`

`````text
---
description: Trigger for every Craftland Studio FC coding task; routes symbol lookup, asset validation, edits, and full compile validation.
globs: "**/*.{fcg,fcc}"
alwaysApply: false
---

# Craftland Studio FC Workflow

This file is the official FC task entry point referenced by `AGENTS.md`. Any agent handling `.fcg`, `.fcc`, FC symbols, FC imports, FC diagnostics, or Craftland Studio asset references must read and follow this workflow first.

## Project Layout

- `Assets/`: user project content. `.fcg` and `.fcc` files here are editable source.
- `Temp/UGCLanguage/fcconfig.json`: toolchain config. Read `CompilerExecutable`, `CorePath`, `EditorGenLibPath`, and `MinimumExtensionVersion` first.
- `Temp/UGCLanguage/editorGen/EditorGenLib.fcc`: current project generated symbols, including registered scene objects, custom events, custom enums, custom components, and declare graphs. Read-only reference.
- `Temp/UGCLanguage/editorGen/<libId>.fcc`: referenced package generated symbols. Read-only reference.
- `Temp/UGCLanguage/packages/<libId>/`: referenced package source. Treat as read-only unless the user explicitly asks to edit package source.

## Task Routing

- If the task involves any FC symbol that code may reference, read `.craftland/agents/skills/fc-symbol-lookup/SKILL.md` first. This includes APIs, standard libraries, imports, types, function signatures, events, enums, components, generated project symbols, declare graphs, and public properties.
- If the task involves Craftland Studio asset validity, read `.craftland/agents/skills/fc-asset-check/SKILL.md` first. This includes assets, UI objects, scene entities, assetIds, entityIds, script attachments, button bindings, and current editor state.
- If the task makes FC code use any project asset, scene, scene entity, or UI widget — create it, switch to it, read it, bind to it, anything that names one — read `.craftland/agents/skills/fc-asset-registration/SKILL.md` first. The default move is: check through MCP whether the target is registrable, register it, and use the generated `ERes*` / `Res` symbols. The same skill applies when working with code that already uses `ERes*` / `EResKey*` / `Res` symbols.
- If the task involves complex FC grammar, syntax errors, or an unfamiliar language form, read `.craftland/agents/references/fc-syntax.md`. It is a syntax-only reference derived from `FCGLexer.g4` and `FCGParser.g4`.
- If any `.fcg` / `.fcc` file is edited, read and execute `.craftland/agents/skills/fc-lint-fix/SKILL.md` before the final response.

When multiple skills are needed, use this order: symbol lookup -> asset check -> asset registration -> edit -> full compile validation. `fc-lint-fix` is the highest-priority closing step.

## FC Required Idioms

Prefer explicit FC idioms over syntax borrowed from other languages:

- `.fcg` files put imports before `graph`.
- Library import: `import "StdLibrary.fcc" as StdLib`.
- Script reference import: `import ScriptName as Alias from "path"`.
- Graph fields are declared directly: `isJumping bool`.
- Fields, parameters, and variables use `name Type`: `func Move(player entity<Player>)`.
- Function return type goes after the parameter list: `func GetCount() int`.
- Current attached entity: `thisEntity<Transform>.Position`.
- Component access: `entity<Component>.Field`.
- Vector construction: `Vector3{x, y, z}`.
- Vector component access: `pos.X`, `pos.Y`, `pos.Z`.
- HUD button callback: `func OnClick(button entity<UIWidgetButton>, player entity<Player>)`.
- Async calls: `wait Func()` or `start Func()`.
- For loops: `for i = start, max, step {}` or `for i, item in list {}`.
- Type conversion: `expr as Type`; type expression: `typeof(Type)`.
- `out` parameter call: `out var name`.

## Execution Order

1. Decide whether the task involves FC code, FC declarations, FC diagnostics, or generated project symbols.
2. Read the required skills according to task routing.
3. Before writing code, verify source-of-truth data. Do not fill in APIs, imports, types, events, enums, components, graph names, assetIds, or entityIds from memory.
4. Before referencing generated project symbols, verify them through `fc-symbol-lookup`. Before referencing assetIds or entityIds, verify them through `fc-asset-check`.
5. Unless the user explicitly asks otherwise, edit only user-owned FC files under `Assets/`.
6. After editing `.fcg` / `.fcc`, run the lint/fix loop.
7. If the task changed editor-owned assets, UI, scene entities, or script attachments through MCP, finish with Craftland Studio MCP `game-build` + `game-console-get-logs`.
8. In the final response, report lint or build status and any missing toolchain config.

## Source-Of-Truth Order

When verifying FC symbols and Craftland Studio assets, choose sources by task type:

- FC symbols: use standard library `.fcc`, `EditorGenLib.fcc`, `editorGen/<libId>.fcc`, and referenced package `.fcc` files. Search likely `.fcc` files by semantic domain first, then fall back to all available `.fcc` files. This is the responsibility of `fc-symbol-lookup`.
- Craftland Studio assets and current editor state: use Craftland Studio MCP when available and current editor state is needed. Read `instructions://index` first, then use tools such as `asset-list`, `asset-get`, `asset-entity-get`, `asset-entity-search`, `asset-entity-update`, and `entity-eca-script-update` as needed. This is the responsibility of `fc-asset-check`. The `fc-asset-registration-list` / `fc-asset-registration-upsert` / `fc-asset-registration-remove` tools are the responsibility of `fc-asset-registration`.

Referenced package `.fcc` / `.fcg` files under `Temp/UGCLanguage/packages/<libId>/` are only lookup sources. Do not generate imports using that physical path. Use the `.fcc` filename or existing relative import style; `fcconfig.json` directory protocols let the compiler resolve it.

If no source confirms a symbol or asset reference, do not generate code that uses it. Report which source is missing.

## FC Asset Registration

Asset registration is how project assets (Prefab, CSV, UI, Scene, Texture, Sound, and other supported types) are exposed to FC code. Registering generates `ERes*` element-typed enums (a member IS the asset id — static access, the default) and the `Res` declare graph (dynamic access for runtime-computed keys) in `EditorGenLib.fcc`.

**Registration-first policy**: whenever FC code is about to use an asset, scene, scene entity, or UI widget known at edit time, first check `fc-asset-registration-list` to see whether its type is registrable (`supportedTypes`); if it is, register it and use the generated symbols. Name-based lookup APIs and raw string parameters are acceptable only when the type is not registrable or the target is genuinely decided at runtime.

Registration bypasses to reject (they compile, but they are wrong):

- Passing an asset/scene/entity/widget name or id as a string literal to an API parameter that identifies an asset, e.g. `SwitchScene("Fishing Break Scene")` — correct is `SwitchScene(EResScene.IsleLand)` after registering the scene.
- Locating an edit-time-known entity or widget through a find-by-name API instead of registering it.
- Casting hardcoded id strings to asset id types, or writing enum-like constants for assets.

Craftland Studio is the authority for asset registration. Do not fake registration by writing FC code, and do not hand-edit editor-owned files such as `ResourceRegisteration.asset` or `EditorGenLib.fcc`.

Generated symbol details, compile-verified usage examples, the MCP registration workflow, and constraints are defined in `.craftland/agents/skills/fc-asset-registration/SKILL.md`. Read it before writing FC code that references assets or before calling `fc-asset-registration-*` tools.

## Lint Delivery

Pure `.fcg` / `.fcc` text edits are not complete until full `fccompile.exe -i Assets -agent <model> -session <session-id>` validation has run.

- `-agent` identifies the **model**, not the coding-agent host product. Use the exact model identifier exposed by your system or runtime. Do not write product names such as `codex`, `cursor`, or `aismith`, and do not guess a model name; use `unknown-model` only when no model identity is available.
- `-session` identifies the current conversation only. Prefer the stable session/conversation ID exposed by your host. If none is available, generate one globally unique ID once, keep it for the entire conversation, and reuse it for every compile. Never generate a new ID per invocation. The ID must not contain user, project, path, prompt, or other private content.
- Use only letters, digits, `-`, and `_` in both values; replace other characters with `-`.

Every compiling invocation must carry both values. If the task also changed editor-owned assets, UI, scene entities, or script attachments through MCP, final validation must use Craftland Studio MCP `game-build` + `game-console-get-logs`, because local compiler validation can miss editor integration issues. Model/session rules, the old-compiler fallback, compiler lookup, command details, and the fix loop are defined in `.craftland/agents/skills/fc-lint-fix/SKILL.md`.

The final response for FC edits must state:

- Whether lint or build validation ran.
- Which compiler path was used.
- Whether validation passed.
- If validation could not run, which path, config, or MCP tool is missing.
- If validation failed, a short summary of remaining errors.

## Hard Rules

- Do not invent FC APIs, imports, types, component names, event names, enum values, graph names, assetIds, or entityIds.
- Do not bypass asset registration. This includes passing asset/scene/entity/widget names or ids as string literals to asset-identifying API parameters, using find-by-name APIs for edit-time-known targets, casting hardcoded id strings to asset id types, and writing enum-like constants for assets. When FC code needs an asset known at edit time, use the registered `ERes*` enum members (or `Res` map lookups for runtime keys); if they do not exist, register the asset first (see FC Asset Registration).
- Do not edit `EditorGenLib.fcc` or referenced package generated `.fcc` files as source.
- Do not deliver FC edits without full compile validation results. If validation cannot run, report whether `CompilerExecutable`, `CorePath`, `EditorGenLibPath`, generated `.fcc` libraries, or the plugin install is missing.
- If this workflow conflicts with `AGENTS.md`, `AGENTS.md` wins.

## High-Frequency FC Self-Check

- Use the FC idioms above for entity access, graph fields, vectors, callbacks, async calls, loops, and casts.
- Library APIs, events, types, and generated project symbols must be verified through `fc-symbol-lookup`.
- Platform decorators must match the target runtime side.
- For client-only or server-only event handling, put `[platform_client]` or `[platform_server]` on the `graph`, not on an event listener inside the graph body.
- UI callback signatures and control component fields must be verified through `fc-symbol-lookup`; current UI controls and `button.clickHandlers` must be verified through `fc-asset-check`.
- Any string literal that names an asset, scene, entity, or widget is a registration smell: it should almost always be an `ERes*` enum member (or a `Res` map lookup for runtime keys) instead.

`````

### Source: `.craftland/agents/skills/fc-asset-check/SKILL.md`

`````text
---
name: fc-asset-check
description: Trigger when a task involves Craftland Studio assets, UI, scene entities, assetIds, entityIds, script attachments, button bindings, or current editor state. For asset registration, use fc-asset-registration.
---

# Craftland Studio Asset Validity Check

Use this skill before referencing or modifying Craftland Studio assets, scene entities, UI controls, assetIds, entityIds, script attachments, button callbacks, or other editor-owned data.

## Goal

Do not invent project assets, entities, assetIds, entityIds, UI controls, script attachments, or button bindings. Craftland Studio is the authority for asset registration and current editor state.

This skill only checks Craftland Studio asset validity and current editor state. Use `fc-symbol-lookup` for FC-referenceable symbols, APIs, types, custom events, custom enums, custom components, declare graphs, public properties, and similar FC declarations.

## Decide The Scenario First

1. If you only need to verify FC-referenceable symbols, do not use this skill. Use `fc-symbol-lookup`.
2. If you need to verify assets, scene entities, UI controls, script attachments, button callbacks, or asset properties, use Craftland Studio MCP.
3. If you need to create or modify assets, entities, UI, script attachments, or button callbacks, use MCP and verify the written state afterwards.
4. If FC code references a specific asset, scene, scene entity, or UI widget known at edit time, or a registration must be created or removed, use `fc-asset-registration` (registration-first policy, generated symbol usage, MCP registration workflow). This skill only verifies editor state; it does not own the registration workflow.

## Current Editor Asset Verification

Use this section to confirm what currently exists in the editor, such as asset existence, entity existence, UI control structure, button callbacks, script attachments, dynamic properties, schemas, or asset properties.

When Craftland Studio MCP is available and the task needs current editor state:

1. Read `instructions://index` first.
2. Use `asset-list` / `asset-get` to inspect assets.
3. Use `asset-entity-get` / `asset-entity-search` to inspect entities and UI controls.
4. When verifying or modifying script attachments, use `entity-eca-script-update` and then recheck with `asset-entity-get`.
5. When verifying or modifying UI button callbacks, inspect `button.clickHandlers` and then recheck with `asset-entity-get`.

If MCP is unavailable, do not claim that current editor asset state has been verified. Stop and ask the user to open Craftland Studio or provide an available MCP connection.

## Missing Data Handling

- If an asset or entity is missing from MCP, stop and ask whether the user wants to create/register it manually in Craftland Studio or allow the agent to create/update it through MCP.
- If the asset exists but its FC registration symbol (`ERes*`, `EResKey*`, `Res` member) is missing, register it through `fc-asset-registration` instead of asking the user to do it manually, as long as the target asset and key intent are unambiguous.
- If the asset exists in MCP but the FC symbol is unavailable, tell the user to save the project or regenerate `Temp/UGCLanguage/editorGen/`, then verify the symbol with `fc-symbol-lookup`.
- Read related `.meta` files for fileId confirmation only when MCP does not expose the required fileId.

## Prohibited Actions

- Do not write FC code that assumes a missing asset, entity, assetId, or entityId exists.
- Do not modify generated files under `Temp/UGCLanguage/editorGen/`.
- Do not manually edit editor-owned serialized assets to fake registration, including `ProjectSettings/ResourceRegisteration.asset`.

## After MCP Writes

When the task creates or updates editor-owned data through MCP, verify the written state before writing or delivering FC code:

- After creating or updating an asset, use `asset-get` to confirm that the asset exists and has the expected properties.
- After creating or updating an entity, use `asset-entity-get` to confirm the entity id, type, parent, transform, and relevant dynamic properties.
- After attaching a script, verify the entity `scripts` data with `asset-entity-get`.
- After an asset registration upsert or remove, verify the generated symbols in `EditorGenLib.fcc` through `fc-symbol-lookup`.
- After wiring a UI button, verify `button.clickHandlers` with `asset-entity-get`.
- Treat `asset-refresh` as a disk re-import operation. Do not run it on newly modified MCP assets unless persistence has been confirmed, because refresh may discard editor-memory changes that have not been saved yet.

## Output Check

Before editing or replying, make sure you can state:

- Which user-provided candidate keywords were checked.
- Which MCP response confirmed the asset, entity, UI control, script attachment, or button binding.
- Which assetId, entityId, or UI control path should be used.
- Whether current editor state was verified; if not, state that MCP is unavailable.
- If assets, entities, or UI were modified, which MCP write verification was performed.
- Whether asset registration, project saving, or editorGen regeneration is still needed.

`````

### Source: `.craftland/agents/skills/fc-asset-registration/SKILL.md`

`````text
---
name: fc-asset-registration
description: Trigger when FC code needs to use a project asset, scene, scene entity, or UI widget — registration is how FC code obtains them — or when creating or removing asset registrations through Craftland Studio MCP.
---

# FC Asset Registration

Asset registration exposes project assets (Prefab, CSV, UI, Scene, Texture, Sound, and other supported types) to FC code. It is the default way for FC code to reference any asset known at edit time, and it also makes the build collect the registered asset into the shipped package.

## Registration-First Policy

Whenever FC code is about to use an asset, scene, scene entity, or UI widget known at edit time, first check `fc-asset-registration-list` to see whether its type is registrable (`supportedTypes`); if it is, register it and use the generated symbols.

Bypasses to reject (they compile, but they are wrong):

- Passing an asset/scene/entity/widget name or id as a string literal to an API parameter that identifies an asset, e.g. `SwitchScene("Fishing Break Scene")` — a display name is not even a valid asset id.
- Locating an edit-time-known entity or widget through a find-by-name API instead of registering it.
- Casting hardcoded id strings to asset id types, or writing enum-like constants for assets.

Name-based lookup APIs and raw string parameters are acceptable only when the type is not registrable or the target is genuinely decided at runtime.

## Generated Symbols

Each registration generates symbols in `EditorGenLib.fcc`, named after the registration key:

- `ERes<Type>` element-typed enums: a member IS a value of the enum's `[element <T>]` type (static access, the default). The `[element ...]` attribute on the declaration in `EditorGenLib.fcc` is the authoritative answer to "what is this member" — read it there instead of assuming. E.g. `[element PrefabID] enum EResPrefab { Mini_Kelly }` members are `PrefabID`s, `[element string]` `EResScene` members are scene id strings, `[element entity]` scene-child members are usable as `entity` directly. An enum without `[element]` is a plain string-key enum (the `EResKey*` family).
- `Res` declare static graph plus `EResKey<Type>` key enums: a runtime map from registration keys to asset ids (dynamic access). E.g. `Res.Sprite Map<EResKeySprite, SpriteID>`. `EResKey*` members are the key strings; they exist for autocomplete and have no other meaning.

Most types are flat `type + key + asset`. UI and Scene are nested — register the parent UI/Scene asset first, then widget/entity children under it. Child symbols are named after the parent key:

- Scene `IsleLand` with entity child `Cone001` generates `EResSceneIsleLand.Cone001` (`[element entity]`, the member is the entity itself) and `Res.IsleLand Map<EResKeyIsleLand, entity>`.
- UI `NewUI` with widget child `MyPic` generates `EResUINewUI.MyPic` (`[element CustomUIWidgetID]`) and `Res.NewUI Map<EResKeyNewUI, CustomUIWidgetID>`.

CSV registration is asset-level only — it produces a `CsvID` for the file, not keys for rows or cells.

## Usage In FC Code (compile-verified)

```
import "EditorGenLib.fcc" as EditorLib
import Res from "EditorGenLib.fcc"   // only needed for dynamic access

// Static access (default): the enum member is the asset id
SwitchScene(EResScene.IsleLand)          // scene id string
var petPrefab = EResPrefab.Mini_Kelly    // PrefabID

// Registered UI asset -> create UI; registered widget -> locate it via API
CreateCustomUI(out var ui, player, EResUI.NewUI)                 // CustomUIAssetID
var pic = GetWidgetFromCustomUI(player, ui, EResUINewUI.MyPic)   // entity<UIWidget>

// Registered scene entity: the enum member is the entity itself
var cone = EResSceneIsleLand.Cone001

// Dynamic access: runtime-computed key indexes the Res map
var spriteID = Res.Sprite[csvKey as EResKeySprite]
```

Usage rules:

- `ERes*` / `EResKey*` enums are referenced unqualified after `import "EditorGenLib.fcc" as EditorLib`.
- The `Res` graph requires its own `import Res from "EditorGenLib.fcc"` and is only for keys computed at runtime (for example read from CSV). A runtime string key must be cast to the `EResKey*` enum: `Res.Sprite[key as EResKeySprite]`. This key cast is the sanctioned dynamic pattern and is different from casting strings to asset id types, which is forbidden.
- Child members follow their `[element ...]` type, and the two nested kinds differ: scene children are `[element entity]` and usable as entities directly; UI widget children are `[element CustomUIWidgetID]` — an id, not an entity. Consume widget ids through `GetWidgetFromCustomUI(owner, uiEntity, widgetID)`, which returns `entity<UIWidget>`; the UI entity comes from `CreateCustomUI` / `CreateCustomUIClient` with the registered `CustomUIAssetID`.

## Registering Through MCP

When a needed registration does not exist yet and Craftland Studio MCP is available:

1. `fc-asset-registration-list` to see supported registration types and existing keys. If `editorSessionActive=true`, ask the user to close the Resource Registration editor; writes are blocked while it is open.
2. Locate the target asset with `asset-list` / `asset-get`, and UI widget / Scene entity children with `asset-entity-search` / `asset-entity-get`.
3. `fc-asset-registration-upsert` with `registrationType`, the asset (`assetId` or `assetPath`), and an explicit `key` (plus `childId` / `childKey` for nested registration). Register directly in one call for the normal case; use `dryRun=true` only when the outcome is uncertain — the key may be invalid or duplicated, or the same asset already has multiple registrations. A failed upsert reports the reason and rolls back, so a routine registration does not need a dryRun round-trip.
4. A successful upsert saves the registration and refreshes EditorGen in one operation (rollback on `editorgen_failed` / `recovery_failed`). Re-verify the new symbol in `EditorGenLib.fcc` through `fc-symbol-lookup` before writing FC code that uses it.

`fc-asset-registration-remove` deletes a registration. Removing a UI/Scene parent is blocked while child registrations exist — remove children first. Prefer `dryRun=true` before removal when existing FC code may reference the symbol.

If Craftland Studio MCP is unavailable, or the request is ambiguous about which asset or key to register, ask the user whether to register manually in Craftland Studio or provide the missing information.

## Constraints

- Registration keys must be valid FC identifiers: letters, digits, underscore, no leading digit, no FC keyword, unique within the type or parent.
- Craftland Studio is the authority for registration state. Do not hand-edit `ProjectSettings/ResourceRegisteration.asset`, `EditorGenLib.fcc`, or anything under `Temp/UGCLanguage/editorGen/`.
- Do not write FC code that references a registration symbol before `fc-symbol-lookup` confirms it exists in `EditorGenLib.fcc`.

## Output Check

Before editing or replying, make sure you can state:

- Which assets the FC code references, and which of them are covered by existing registrations.
- Which registrations were created or removed through MCP, with which keys.
- Which generated symbols (`ERes*`, `EResKey*`, `Res` members) were verified through `fc-symbol-lookup` after registration.
- Whether any asset reference intentionally stayed dynamic (runtime key or non-registrable type) and why.

`````

### Source: `.craftland/agents/skills/fc-lint-fix/SKILL.md`

`````text
---
name: fc-lint-fix
description: Trigger after any .fcg or .fcc edit, or when the user asks to compile, validate, lint, check, or fix FC compiler errors.
---

# FC Lint Fix

Use this skill after every `.fcg` / `.fcc` edit. Also use it when the user asks to compile, validate, lint, check, or fix FC errors. This is the highest-priority FC skill.

## Completion Rule

Pure FC text edits are not complete until full `fccompile.exe -i Assets` validation has run. `-m` is only a fast metadata-only precheck and must not be treated as final delivery validation. If the task changed editor-owned assets, UI, scene entities, or script attachments through Craftland Studio MCP, final validation must use `game-build` + `game-console-get-logs`. If validation cannot run, the final response must state which required file, path, or MCP tool is missing.

## Locate Project Config

Read `Temp/UGCLanguage/fcconfig.json` under the project root when available. Use these fields:

- `CompilerExecutable`
- `CorePath`
- `EditorGenLibPath`
- `MinimumExtensionVersion`

The editor symbol table is normally located at:

```powershell
<ProjectRoot>\Temp\UGCLanguage\editorGen\EditorGenSymbol.json
```

## Locate Compiler

Use the first existing compiler path in this order:

1. `Temp/UGCLanguage/fcconfig.json.CompilerExecutable`
2. `<CorePath>\fccompile_external.exe`
3. `<CorePath>\fccompile.exe`
4. `%USERPROFILE%\.vscode\extensions\craftlandstudio.ffugclanguage-*\library\release\fccompile.exe`
5. `%USERPROFILE%\.cursor\extensions\craftlandstudio.ffugclanguage-*\library\release\fccompile.exe`

If multiple plugin versions match, use the latest directory unless project config provides an explicit compiler path.

## Locate Standard And Generated Libraries

Prefer `CorePath` from `fcconfig.json`. If missing, read editor setting `ffugclanguage.editor.CorePath` when available, then fall back to plugin `library/release/`.

The compiler's `-e` option expects the editorGen directory, not the `EditorGenLib.fcc` file. By default it uses:

```powershell
<ProjectRoot>\Temp\UGCLanguage\editorGen
```

## Model And Session Markers (Required)

Every `fccompile` invocation that compiles sources (any command with `-i`) must include `-agent <model> -session <session-id>`. This enables local compile event collection. Craftland Studio may later upload these compile-result records through its EventLog service; session IDs are aggregation keys only and must contain no private content.

Build the model marker as follows:

- `-agent` identifies the **model**, not the coding-agent host product. Use the exact model identifier exposed by your system or runtime.
- Do not use product names such as `codex`, `cursor`, or `aismith`.
- Never guess the model name. If no model identity is available, use `unknown-model`.

Build the session marker as follows:

- Prefer the stable session/conversation ID exposed by your host.
- If the host exposes no ID, generate one globally unique ID once and reuse it for every compile in the current conversation.
- Never generate a new session ID per compile invocation.
- The ID is only an aggregation key. It must not contain user, project, path, prompt, or other private content.
- Use only letters, digits, `-` and `_` in both markers (replace other characters with `-`).

If the compiler rejects the flag with an error like `flag provided but not defined: -agent` (or `-session`), the compiler is an older version: retry the same command without that flag.

## Run Validation

Run from the project root. Match the VS Code extension's compiler invocation shape: pass source roots through `-i` and rely on compiler defaults for editorGen and symbol paths.

Final local compiler validation:

```powershell
<Compiler> -i Assets -agent <model> -session <session-id>
```

Optional fast metadata-only precheck:

```powershell
<Compiler> -i Assets -m -agent <model> -session <session-id>
```

`-m` means compile to metadata only. In the compiler, it still runs preprocessing and precompiler validation, but skips the final `Compiler()` phase. It can catch many syntax, import, type, and symbol issues quickly, but it is not a full compile and must not be the final validation for delivered `.fcg` / `.fcc` edits.

If the project has multiple source roots, join them with `;`, matching `fcconfig.json` / extension source roots:

```powershell
<Compiler> -i "Assets;Other/AssetsFolder" -agent <model> -session <session-id>
```

Do not pass `-e` or `-s` unless you must override compiler defaults. If overriding:

- `-e` must be the editorGen directory, for example `Temp\UGCLanguage\editorGen`.
- `-s` is joined with the current working directory by the compiler, so use a project-relative path such as `Temp\UGCLanguage\editorGen\EditorGenSymbol.json`.

`fccompile.exe -i Assets -agent <model> -session <session-id>` matches the VS Code extension full compiler invocation plus the required compile event markers. Use it as the default final validation for pure `.fcg` / `.fcc` edits.

Use Craftland Studio MCP `game-build` + `game-console-get-logs` as the final validation when the task touches UI assets, scene entities, script attachments, `button.clickHandlers`, or other editor-owned data. Without an editor process, local full compile (`<Compiler> -i Assets -agent <model> -session <session-id>`) is only a fallback and the final response must state that full editor validation was not run.

## Fix Loop

1. Run validation.
2. Parse diagnostics such as `./Assets/Script.fcg:10:5` or an equivalent `path:line:col` location.
3. Open the failing file and inspect nearby code.
4. Apply the smallest confirmed fix.
5. Run validation again.
6. Repeat up to 3 rounds.

If errors remain after 3 rounds, stop and report:

- Remaining diagnostics.
- Fixes already attempted.
- Which source or user action is needed next.

## Common Fix Checks

- Missing import: confirm the owning `.fcc` through `fc-symbol-lookup` before adding it.
- Unknown FC symbol: confirm it through `fc-symbol-lookup` before using it.
- Unknown assetId or entityId: confirm it through `fc-asset-check` before using it.
- Graph field declaration: use `isJumping bool`.
- Current attached entity: use `thisEntity<Transform>.Position`.
- Component access: use `entity<Component>.Field`.
- Vector construction: use `Vector3{x, y, z}`.
- Vector component access: use `pos.X`, `pos.Y`, `pos.Z`.
- HUD button callback: use `func OnClick(button entity<UIWidgetButton>, player entity<Player>)`.
- Asset/scene/entity/widget reference: never cast hardcoded id strings to asset id types or pass names as string literals; use registered `ERes*` symbols (see `fc-asset-registration`).
- Namespaced call: use the import alias confirmed by the source `.fcc`.
- Platform mismatch: verify `[platform_client]` or `[platform_server]`.
- Client/server event mismatch: put the platform decorator on the `graph`, not on the event listener inside the graph body.

## Final Response Requirements

Must include:

- Whether full compiler validation ran.
- The compiler path used.
- Whether full editor build validation ran when MCP assets/entities/UI were changed.
- Whether validation passed.
- If validation did not run, which config, path, or MCP tool is missing.
- If validation failed, a short summary of remaining errors.

`````

### Source: `.craftland/agents/skills/fc-symbol-lookup/SKILL.md`

`````text
---
name: fc-symbol-lookup
description: Trigger when FC code needs any referenced symbol verified, including APIs, imports, types, functions, events, enums, components, declare graphs, EditorGen symbols, or package symbols.
---

# FC Symbol Lookup

Use this skill before any `.fcg` / `.fcc` code depends on a symbol that FC code can reference. This includes official standard library symbols and project-generated symbols.

## Goal

Do not write FC symbols from memory. Every API, type, function, event, enum value, component name, declare graph, public property, generated project symbol, and import source must come from a real source.

This skill is the FC script handbook lookup path. It answers "what symbol exists, where is it declared, how should it be imported, and what exact signature or type should code use?"

It does not prove that a Craftland Studio asset or entity currently exists in the editor. Use `fc-asset-check` for assetId, entityId, UI object, scene entity, script attachment, button binding, and current editor state validation.

## Lookup Order

1. Search likely `.fcc` files first, based on the user's wording and the domain implied by the task:
   - Prefer `Temp/UGCLanguage/fcconfig.json.CorePath`.
   - Read editor setting `ffugclanguage.editor.CorePath` when available.
   - Otherwise fall back to the plugin `library/release/` directory.
2. Read current project generated libraries:
   - `Temp/UGCLanguage/editorGen/EditorGenLib.fcc`
3. Read referenced package generated libraries and package source declarations:
   - `Temp/UGCLanguage/editorGen/<libId>.fcc`
   - `Temp/UGCLanguage/packages/<libId>/*.fcc`
4. If likely files do not contain the symbol, search all available `.fcc` files under the same roots.
5. Query `FF_UGC_Docs` MCP when available for explanations, examples, and behavior details. Do not rely on docs alone when local `.fcc` declarations are available.

## Symbol Scope

This skill covers both official and project-defined FC symbols:

- Official APIs, types, functions, imports, events, enums, components, and function signatures.
- Project-generated custom events, custom enums, custom components, declare graphs, graph public properties, UI control component types, and generated project symbol names.
- Asset registration symbols in `EditorGenLib.fcc`: `ERes*` / `EResKey*` enums and the `Res` declare graph. This skill verifies whether they exist; if a needed one is missing, route to `fc-asset-registration` to create it instead of concluding the asset is unusable.
- Referenced package symbols from:
   - `Temp/UGCLanguage/editorGen/<libId>.fcc`
   - `Temp/UGCLanguage/packages/<libId>/*.fcc`

If the user asks whether an asset or entity exists in the editor, do not answer from this skill alone. Route to `fc-asset-check`.

## Search Strategy

Treat user-provided candidate symbol names or concepts as first-class search keys. If the user mentions a possible API, event, enum, component, graph, property, or domain concept, verify that direction before settling on a manual implementation.

Use semantic file targeting before broad searches. Guess likely `.fcc` files from the task wording, nearby imports, and domain terms, then search only those files first. For example, UI tasks should start from UI or widget-related `.fcc` files; animation, playable, movement, physics, audio, or math tasks should start from their likely domain files before searching everything.

Use narrow searches before broad searches:

```powershell
rg -n "<Candidate>|Create<Candidate>|Create.*<Candidate>" <LikelyFccFileOrDirectory> -g "*.fcc"
rg -n "<Candidate>|Create<Candidate>|Create.*<Candidate>" <ProjectRoot>\Temp\UGCLanguage\editorGen -g "*.fcc"
rg -n "<Candidate>|Create<Candidate>|Create.*<Candidate>" <ProjectRoot>\Temp\UGCLanguage\packages -g "*.fcc"
```

Then broaden only if the likely `.fcc` files do not contain a usable symbol. Search all `.fcc` files under `CorePath`, `editorGen`, and referenced packages before concluding that the symbol does not exist. Expand to neighboring domain terms, likely verbs, property names, or lower-level primitives only after the user-provided candidate has been checked directly.

When search output is large, do not manually scan a noisy result set and stop early. Filter again with the strongest candidate term, exact symbol fragment, type name, event name, enum name, component name, graph name, or likely function prefix.

For FC symbols, treat `.fcc` declarations as the primary source. Confirm import, namespace, signature, fields, platform, and deprecation status from the `.fcc` file that owns the declaration. If a declaration has `[deprecated]` and its preceding `//@deprecated` comment says `Use X instead`, generate `X`, not the deprecated symbol.

Do not assume library names from general programming concepts. The owning `.fcc` may be named after a project-specific domain rather than the generic concept the user used.

Before concluding that a candidate symbol does not exist, record the exact keywords and file ranges checked. The "not found" result is not valid if a user-provided candidate term was never searched directly.

## Plugin Fallback Paths

When project config is missing, look for an installed FC plugin:

- VS Code: `%USERPROFILE%\.vscode\extensions\craftlandstudio.ffugclanguage-*`
- Cursor: `%USERPROFILE%\.cursor\extensions\craftlandstudio.ffugclanguage-*`

Unless project config provides an explicit path, use the latest matching plugin directory. Standard `.fcc` files and `fccompile.exe` should be under `library/release/`.

## Information To Extract

For every symbol you will use, record:

- The source file or MCP document that confirms the symbol.
- The import statement, if one is required.
- Whether a namespace alias is needed to resolve an actual ambiguity.
- The exact function signature, type declaration, event parameters, enum members, component fields, graph name, or public property declaration.
- Any platform or type constraints.

## Import Rules

- Add an import only after confirming the owning `.fcc` file.
- Keep aliases consistent with confirmed examples or local project style.
- Do not assume common libraries are already imported.
- Prefer unqualified API, event, and type symbols after importing their owning `.fcc`; use `Alias.Symbol` only to resolve an actual ambiguous identifier. Keep required static graph and cross-script member qualification.
- Referenced package `.fcc` files under `Temp/UGCLanguage/packages/<libId>/` are only lookup sources. Do not use that physical path in code imports. Use the `.fcc` filename or an existing relative import style; the compiler resolves it through `fcconfig.json` directory protocols.

## If Lookup Fails

Do not generate code that uses unconfirmed symbols. Tell the user which symbol could not be verified and which source is missing, such as `CorePath`, standard library `.fcc` files, `EditorGenLib.fcc`, referenced package `.fcc` files, `FF_UGC_Docs`, or plugin `library/release/`.

## Output Check

Before editing or replying, make sure you can state:

- The confirmed `.fcc` file or MCP document.
- Required import lines.
- Function, type, event, enum, component, declare graph, or public property declarations.
- Any unresolved symbols that must not be used.

`````

### Source: `.cursor/rules/craftland-studio-assets.mdc`

`````text
---
description: Craftland Studio asset handling rules for ECA and non-FC assets
globs: *
applyTo: "**/*"
alwaysApply: true
---

# Craftland Studio Asset Rules

## Core Rule

Craftland Studio is the authoritative editor for game assets in this project.

- Any access to or modification of game assets must use Craftland Studio.
- Only `.fcc` and `.fcg` files may be edited directly as text and compiled through the FC toolchain.
- If a task involves non-text game assets, especially `.eca` files, the agent must first check whether Craftland Studio is available through MCP.
- If Craftland Studio is not available for the current session, the agent must tell the user to open the game editor first before attempting that asset task.
- The agent must not guess or hand-edit serialized asset formats such as `.eca` when Craftland Studio is required but unavailable.

## Directory Scope

The following directories belong to the Craftland Studio project structure:

- `Assets/` user asset files, including `.fcc` and `.fcg`
- `ProjectSettings/` user configuration asset files
- `Temp/` temporary files, records, debug output, and compilation results
- `Libraries/` library files
- `Cache/` project cache

## Working Rules

- For requests involving `.fcc` or `.fcg`, direct text editing is allowed.
- For requests involving assets under the directories above that are not `.fcc` or `.fcg`, prefer Craftland Studio and related MCP tools.
- Before handling `.eca`, entity attachment, asset registration, scene assets, workflow assets, or other editor-owned assets, first verify whether Craftland Studio MCP is connected.
- Once Craftland Studio MCP is connected, the agent must read `instructions://index` before using other Craftland Studio MCP tools or resources.
- If the MCP is unavailable, stop and ask the user to open Craftland Studio, then retry the task after the editor-side connection is ready.

`````

### Source: `.github/instructions/craftland-studio-assets.instructions.md`

`````text
---
description: Craftland Studio asset handling rules for ECA and non-FC assets
globs: *
applyTo: "**/*"
alwaysApply: true
---

# Craftland Studio Asset Rules

## Core Rule

Craftland Studio is the authoritative editor for game assets in this project.

- Any access to or modification of game assets must use Craftland Studio.
- Only `.fcc` and `.fcg` files may be edited directly as text and compiled through the FC toolchain.
- If a task involves non-text game assets, especially `.eca` files, the agent must first check whether Craftland Studio is available through MCP.
- If Craftland Studio is not available for the current session, the agent must tell the user to open the game editor first before attempting that asset task.
- The agent must not guess or hand-edit serialized asset formats such as `.eca` when Craftland Studio is required but unavailable.

## Directory Scope

The following directories belong to the Craftland Studio project structure:

- `Assets/` user asset files, including `.fcc` and `.fcg`
- `ProjectSettings/` user configuration asset files
- `Temp/` temporary files, records, debug output, and compilation results
- `Libraries/` library files
- `Cache/` project cache

## Working Rules

- For requests involving `.fcc` or `.fcg`, direct text editing is allowed.
- For requests involving assets under the directories above that are not `.fcc` or `.fcg`, prefer Craftland Studio and related MCP tools.
- Before handling `.eca`, entity attachment, asset registration, scene assets, workflow assets, or other editor-owned assets, first verify whether Craftland Studio MCP is connected.
- Once Craftland Studio MCP is connected, the agent must read `instructions://index` before using other Craftland Studio MCP tools or resources.
- If the MCP is unavailable, stop and ask the user to open Craftland Studio, then retry the task after the editor-side connection is ready.

`````

### Source: `.github/instructions/fc-examples.instructions.md`

`````text
---
description: FC语言的完整开发示例，每个示例都是原子化的，可以独立使用。
globs: *.fcg,*.fcc
applyTo: "**/*. {fcc,fcg}"
alwaysApply: true
---

# FC语言开发示例大全

本文档包含FC语言的完整开发示例，每个示例都是原子化的，可以独立使用。
参考示例的实现，如遇到引用缺失类问题，请务必遍历fcc库查找是否可以修复引用缺失问题。

## 基础图形定义

### 普通图形
```fc
import "StdLibrary.fcc" as std

graph MyScript {
    PlayerCount int = 0
    
    event OnAwake() {
        LogInfo("Script initialized")
    }
}
```

### 静态图形（全局脚本）
```fc
import "StdLibrary.fcc" as std
import "List.fcc" as list

static graph GlobalManager {
    MaxPlayers int = 10
    
    func GetPlayerCount() int {
        return list.Length(GetAllPlayers())
    }
}
```

## 实体和组件操作

### 访问当前实体组件
```fc
import "StdLibrary.fcc" as std

graph EntityHandler {
    event OnAwake() {
        // 访问Transform组件
        thisEntity<Transform>.Position = Vector3{0, 1, 0}
        thisEntity<Transform>.Rotation = Quaternion{0, 0, 0, 1}
        
        // 访问外观组件
        thisEntity<BasicAppearance>.DiffuseColor = #FF0000FF
    }
}
```

### 检查组件是否存在
```fc
import "StdLibrary.fcc" as std

graph ComponentChecker {
    event OnAwake() {
        if HasComponent(thisEntity, typeof(Player)) {
            thisEntity<Player>.RunSpeedScale = 1.5
            LogInfo("Player component found")
        }
    }
}
```

### 实体类型转换
```fc
import "StdLibrary.fcc" as std

graph EntityConverter {
    event OnEntityEnter(enterEntity entity<Entity>) {
        if HasComponent(enterEntity, typeof(Player)) {
            var player = enterEntity<Player>
            LogInfo("Player name: " + player.Name)
        }
    }
}
```

## 预制体和资产操作

### 从预制体创建实体
```fc
import "StdLibrary.fcc" as std

graph PrefabCreator {
    event OnAwake() {
        // 创建场景方块
        CreateFromPrefab(out var cube, EResPrefab.SceneCube)
        cube<Transform>.Position = Vector3{5, 0, 5}
        
        // 创建炸弹
        CreateFromPrefab(out var bomb, EResPrefab.SceneBomb)
        bomb<Transform>.Position = thisEntity<Transform>.Position
    }
}
```

### 获取场景物件
```fc
import "StdLibrary.fcc" as std
import "Player.fcc" as player

graph SceneObjectGetter {
    event OnAwake() {
        // 获取场景中的胜利点
        var winnerView = EResSceneIsleLand.WinnerView as entity<LevelObject>
        var targetPos = winnerView<Transform>.Position
        
        // 传送玩家到胜利点
        Teleport(thisEntity<Player>, targetPos, winnerView<Transform>.Rotation)
    }
}
```

### 动态获取脚本资产
```fc
import "StdLibrary.fcc" as std
import "EditorGenLib.fcc" as gen
import Res from "EditorGenLib.fcc"

graph DynamicScriptLoader {
    event OnAwake() {
        var scriptKey = "SomeEffect"
        
        // 检查脚本是否存在
        if ContainKey(Res.FCG, scriptKey) {
            // 动态添加脚本
            AddScript(thisEntity, Res.FCG[scriptKey as EResKeyFCG])
        }
    }
}
```

## UI操作

### 创建自定义UI
```fc
import "StdLibrary.fcc" as std
import "Hud.fcc" as hud

graph UICreator {
    MainUI entity<CustomHud>
    
    event OnAwake() {
        // 创建玩家HUD
        CreateCustomUI(out var ui, thisEntity<Player>, EResUI.BombHUD)
        MainUI = ui
        
        // 初始隐藏UI
        MainUI<CustomUI>.IsVisible = false
    }
    
    event OnMyGameStart(level int) {
        // 游戏开始时显示UI
        MainUI<CustomUI>.IsVisible = true
    }
}
```

### UI按钮点击事件
```fc
import "StdLibrary.fcc" as std
import "Hud.fcc" as hud

graph ButtonHandler {
    ClickCount int = 0
    
    event OnTapped(player entity<Player>) {
        ClickCount += 1
        LogInfo("Button clicked by: " + player<Player>.Name)
        LogInfo("Click count: " + ClickCount)
        
        // 执行点击后的逻辑
        // ...
    }
}
```

### 设置UI控件属性
```fc
import "StdLibrary.fcc" as std
import "Hud.fcc" as hud

graph UIController {
    event OnUpdate() {
        // 根据条件控制按钮是否可点击
        var canUse = CheckSomeCondition()
        thisEntity<UIWidget>.Active = canUse
    }
    
    func CheckSomeCondition() bool {
        return true // 你的逻辑
    }
}
```

### 设置图标资源
```fc
import "StdLibrary.fcc" as std

graph IconSetter {
    event OnAwake() {
        // 设置道具图标
        thisEntity<ItemTrigger>.Icon<Icon>.Resource = EResSprite.ui_icon_skill_Awakening
    }
}
```

## 异步编程

### 基础异步函数
```fc
import "StdLibrary.fcc" as std

graph AsyncHandler {
    event OnAwake() {
        // 等待异步函数完成
        wait DelayedAction()
        
        // 异步执行，不等待
        start BackgroundTask()
    }
    
    async func DelayedAction() {
        WaitForMillisecond(2000)
        LogInfo("Delayed action completed")
    }
    
    async func BackgroundTask() {
        WaitForNextFrame()
        LogInfo("Background task running")
    }
}
```

### 带输出参数的异步函数
```fc
import "StdLibrary.fcc" as std

graph AsyncCalculator {
    event OnAwake() {
        wait CalculateSum(10, 20, out var result)
        LogInfo("Result: " + result)
    }
    
    async func CalculateSum(a int, b int, out var sum int) {
        WaitForMillisecond(1000)
        sum = a + b
    }
}
```

## 集合操作

### 列表操作
```fc
import "StdLibrary.fcc" as std
import "List.fcc" as list

graph ListHandler {
    PlayerList List<entity<Player>>
    
    event OnAwake() {
        // 创建新列表
        PlayerList = list.New(0, 0)
        
        // 添加元素
        for index, player in GetAllPlayers() {
            list.Append(PlayerList, player)
        }
        
        // 遍历列表
        for i, player in PlayerList {
            LogInfo("Player " + i + ": " + player<Player>.Name)
        }
        
        // 检查是否包含元素
        if list.Contain(PlayerList, somePlayer) {
            LogInfo("Player found in list")
        }
    }
}
```

### 字典操作
```fc
import "StdLibrary.fcc" as std
import "Map.fcc" as map

graph MapHandler {
    EntityMapping Map<int, entity>
    
    event OnAwake() {
        // 创建新字典
        EntityMapping = map.New()
        
        // 添加键值对
        EntityMapping[1] = thisEntity
        EntityMapping[2] = someOtherEntity
        
        // 检查键是否存在
        if ContainKey(EntityMapping, 1) {
            var entity = EntityMapping[1]
            LogInfo("Entity found: " + entity<Entity>.Name)
        }
        
        // 移除键值对
        map.Remove(EntityMapping, 1)
    }
}
```

## 标签系统

### 添加和检查标签
```fc
import "StdLibrary.fcc" as std

graph TagManager {
    event OnAwake() {
        // 添加标签
        AddTag(thisEntity, "KeyPlayer")
        AddTag(thisEntity, "SpecialUnit")
        
        // 检查标签
        if HasTag(thisEntity, "KeyPlayer") {
            LogInfo("This entity has the key")
        }
        
        // 移除标签
        RemoveTag(thisEntity, "SpecialUnit")
    }
}
```

## 事件系统

### 分发事件给单个实体
```fc
import "StdLibrary.fcc" as std
import "EditorGenLib.fcc" as gen

graph EventDispatcher {
    event OnAwake() {
        // 分发事件给全局实体
        DispatchEvent(OnMyGameStart, globalEntity, List<object>{1})
        
        // 分发事件给特定实体
        DispatchEvent(gen.OnSceneCubeCreated, thisEntity, nil)
    }
}
```

### 分发事件给所有玩家
```fc
import "StdLibrary.fcc" as std

graph PlayerEventDispatcher {
    func NotifyAllPlayers(message string) {
        for index, player in GetAllPlayers() {
            DispatchEvent(OnPlayerMessage, player, List<object>{message})
        }
    }
    
    event OnAwake() {
        NotifyAllPlayers("Game started!")
    }
}
```

### 触发器事件处理
```fc
import "StdLibrary.fcc" as std

graph TriggerHandler {
    event OnEntityEnter(enterEntity entity<Entity>) {
        // 检查进入的实体类型
        if HasComponent(enterEntity, typeof(Player)) {
            var player = enterEntity<Player>
            LogInfo("Player entered: " + player.Name)
            
            // 执行相应逻辑
            HandlePlayerEnter(player)
        }
    }
    
    func HandlePlayerEnter(player entity<Player>) {
        // 处理玩家进入逻辑
    }
}
```

## 战斗和生命周期

### 玩家消除事件
```fc
import "StdLibrary.fcc" as std
import "Combat.fcc" as combat
import "Player.fcc" as player

graph CombatHandler {
    event OnEliminated(attackerEntity entity<Entity>, attackedType DamageType, hitBodyPart HitBodyPart) {
        LogInfo("Player eliminated")
        
        // 检查是否携带钥匙
        if HasTag(thisEntity, "KeyPlayer") {
            // 掉落钥匙
            RemoveTag(thisEntity, "KeyPlayer")
            CreateFromPrefab(out var keyTrigger, EResPrefab.KeyTrigger)
            keyTrigger<Transform>.Position = thisEntity<Player>.Position
        }
    }
}
```

### 消除和复活玩家
```fc
import "StdLibrary.fcc" as std
import "Combat.fcc" as combat
import "Player.fcc" as player

graph PlayerLifecycle {
    async func EliminateAndRevive(player entity<Player>) {
        // 消除玩家
        Eliminate(player)
        
        // 等待3秒后复活
        WaitForMillisecond(3000)
        Revive(player)
    }
    
    event OnSomeEvent() {
        start EliminateAndRevive(somePlayer)
    }
}
```

## 数学和随机数

### 随机数生成
```fc
import "StdLibrary.fcc" as std
import "Math.fcc" as math

graph RandomGenerator {
    event OnAwake() {
        // 生成随机整数 (1-9)
        var randomInt = math.RandomInt(1, 10)
        
        // 生成随机浮点数 (0.0-1.0)
        var randomFloat = math.RandomFloat(0.0, 1.0)
        
        // 使用随机数设置位置
        var randomPos = Vector3{randomInt, 0, randomInt}
        thisEntity<Transform>.Position = randomPos
        
        LogInfo("Random position: " + randomPos)
    }
}
```

### 数学计算
```fc
import "StdLibrary.fcc" as std
import "Math.fcc" as math

graph MathOperations {
    func CalculateDistance(pos1 Vector3, pos2 Vector3) float {
        var dx = pos2.X - pos1.X
        var dz = pos2.Z - pos1.Z
        return math.Sqrt(dx*dx + dz*dz)
    }
    
    event OnUpdate() {
        var playerPos = thisEntity<Transform>.Position
        var targetPos = Vector3{0, 0, 0}
        var distance = CalculateDistance(playerPos, targetPos)
        
        if distance < 2.0 {
            LogInfo("Player is near target")
        }
    }
}
```

## 字符串操作

### 字符串处理
```fc
import "StdLibrary.fcc" as std
import "Strings.fcc" as strings

graph StringHandler {
    event OnAwake() {
        var playerName = thisEntity<Player>.Name
        
        // 检查字符串长度
        if strings.Length(playerName) > 0 {
            LogInfo("Player name: " + playerName)
        }
        
        // 字符串拼接
        var message = "Welcome, " + playerName + "!"
        LogInfo(message)
        
        // 格式化字符串
        var formattedMsg = Format("Player %v joined the game", List<string>{playerName})
        LogInfo(formattedMsg)
    }
}
```

## 物理检测

### 区域检测
```fc
import "StdLibrary.fcc" as std
import "Physics.fcc" as physics

graph PhysicsChecker {
    func CheckExplosionArea(center Vector3, size float) {
        for index, player in GetAllPlayers() {
            // 检查玩家是否在爆炸范围内
            var inX = physics.IsInsideBox(player, center, size, 1, 1, Vector3{0,0,0})
            var inZ = physics.IsInsideBox(player, center, 1, size, 1, Vector3{0,0,0})
            
            if inX || inZ {
                LogInfo("Player in explosion area: " + player<Player>.Name)
                // 处理爆炸效果
            }
        }
    }
}
```

## 提示和通知

### 显示玩家提示
```fc
import "StdLibrary.fcc" as std

graph NotificationManager {
    func ShowTipToPlayer(player entity<Player>, message string, color int, duration int) {
        NotifyShowTips(player, message, color, duration)
    }
    
    func ShowTipToAllPlayers(message string) {
        for index, player in GetAllPlayers() {
            NotifyShowTips(player, message, #FFFFFFFF, 3000)
        }
    }
    
    event OnAwake() {
        ShowTipToAllPlayers("Game initialized!")
    }
}
```

## 传送和移动

### 玩家传送
```fc
import "StdLibrary.fcc" as std
import "Player.fcc" as player

graph TeleportManager {
    func TeleportToSpawn(player entity<Player>) {
        var spawnPoint = Vector3{0, 1, 0}
        var spawnRotation = Quaternion{0, 0, 0, 1}
        
        Teleport(player, spawnPoint, spawnRotation)
        LogInfo("Player teleported to spawn")
    }
    
    func TeleportToWinArea(player entity<Player>) {
        var winnerView = EResSceneIsleLand.WinnerView as entity<LevelObject>
        Teleport(player, winnerView<Transform>.Position, winnerView<Transform>.Rotation)
    }
}
```

## 游戏流程控制

### 游戏阶段管理
```fc
import "StdLibrary.fcc" as std
import "Player.fcc" as player

graph GamePhaseManager {
    event OnMyGameStart(level int) {
        LogInfo("Game started - Level: " + level)
        
        // 禁用玩家移动
        SetAllPlayersMoveStatus(false)
        
        // 初始化关卡
        wait InitializeLevel(level)
        
        // 启用玩家移动
        SetAllPlayersMoveStatus(true)
    }
    
    async func InitializeLevel(level int) {
        LogInfo("Initializing level: " + level)
        WaitForMillisecond(1000)
        LogInfo("Level initialized")
    }
    
    event OnMyGameEnd() {
        LogInfo("Game ended")
        WaitForMillisecond(3000)
        EndCurrentPhase()
    }
}
```

### 倒计时系统
```fc
import "StdLibrary.fcc" as std
import "Strings.fcc" as strings

graph CountdownManager {
    async func StartCountdown(seconds int) {
        for i = seconds, 0, -1 {
            var message = Format("Game starts in: %v", List<int>{i})
            
            // 通知所有玩家
            for index, player in GetAllPlayers() {
                NotifyShowTips(player, message, #FFFFFFFF, 1000)
            }
            
            WaitForMillisecond(1000)
        }
        
        // 倒计时结束
        DispatchEvent(OnMyGameStart, globalEntity, List<int>{1})
    }
}
```

## 资源清理

### 实体销毁和清理
```fc
import "StdLibrary.fcc" as std

graph ResourceCleaner {
    MyUI entity<CustomHud>
    
    event OnDestroy() {
        // 清理UI资源
        if MyUI != nil {
            Destroy(MyUI)
            MyUI = nil
        }
        
        LogInfo("Resources cleaned up")
    }
    
    func DestroyAfterDelay(target entity, delay int) {
        start DelayedDestroy(target, delay)
    }
    
    async func DelayedDestroy(target entity, delay int) {
        WaitForMillisecond(delay)
        Destroy(target)
    }
}
```

## 常见错误和修正

### 错误示例对比

#### ❌ 错误的组件访问
```fc
// 错误：使用点号语法
thisEntity.Transform.Position = Vector3{0, 1, 0}
```

#### ✅ 正确的组件访问
```fc
// 正确：使用尖括号语法
thisEntity<Transform>.Position = Vector3{0, 1, 0}
```

#### ❌ 错误的实体类型声明
```fc
// 错误：直接使用组件类型
var player Player
```

#### ✅ 正确的实体类型声明
```fc
// 正确：使用entity包装
var player entity<Player>
```

#### ❌ 错误的异步调用
```fc
// 错误：直接调用异步函数
DelayedFunction()
```

#### ✅ 正确的异步调用
```fc
// 正确：使用wait或start关键字
wait DelayedFunction()
start DelayedFunction()
```

#### ❌ 错误的事件分发
```fc
// 错误：直接传递参数
DispatchEvent(eventID, entity, param1, param2)
```

#### ✅ 正确的事件分发
```fc
// 正确：参数包装在List中
DispatchEvent(eventID, entity, List<object>{param1, param2})
``` 
`````

### Source: `.github/instructions/fc-import-map.instructions.md`

`````text
---
description: FC 语言完整语法和 API 参考
globs: *.fcg,*.fcc
applyTo: "**/*.{fcc,fcg}"
alwaysApply: true
---

# FC 语言 Import 映射表

使用原则：每次使用函数前，查询此表补充 import 语句

---

## 核心规则

### 必须 Import 的情况
1. 非 StdLibrary 的函数 - 必须查表并添加 import
2. 非 StdLibrary 的事件 - 必须查表并添加 import（重要！）
3. List、Map 操作 - 必须 import 对应库
4. 数学计算函数 - 必须 import "Math.fcc"
5. 物理检测函数 - 必须 import "Physics.fcc"
6. 战斗相关函数 - 必须 import "Combat.fcc"

### 无需 Import 的情况
1. StdLibrary 内置函数 - 如 LogInfo(), WaitForMillisecond(), GetAllPlayers()
2. StdLibrary 内置事件 - 如 OnAwake(), OnGameStart(), OnUpdate(), OnDestroy()
3. 语言关键字和基本类型 - 如 Vector3, Quaternion, bool, int
4. 编辑器生成的枚举/资源 - 使用 import "EditorGenLib.fcc"

### 事件 Import 示例
```fc
// 错误：缺少 import
graph ButtonHandler {
    event OnTapped(player entity<Player>) {  // 错误：OnTapped 需要 import "Hud.fcc"
        LogInfo("Button tapped")
    }
}

// 正确：添加 import
import "StdLibrary.fcc" as std
import "Hud.fcc" as hud                      // 添加 import

graph ButtonHandler {
    event OnTapped(player entity<Player>) {  // 正确
        LogInfo("Button tapped")
    }
}
```

---

## 函数到库映射表

### List 操作（List.fcc）
```fc
import "List.fcc" as list

New()           → list.New(length, capacity)
Append()        → list.Append(targetList, value)
Length()        → list.Length(targetList)
RemoveAt()      → list.RemoveAt(targetList, index)
Clear()         → list.Clear(targetList)
Reverse()       → list.Reverse(targetList)
Clone()         → list.Clone(targetList)
Insert()        → list.Insert(targetList, index, value)
Shuffle()       → list.Shuffle(targetList)
IsEqual()       → list.IsEqual(listA, listB)
Contain()       → list.Contain(targetList, value)
AppendRange()   → list.AppendRange(targetList, sourceList)
Remove()        → list.Remove(targetList, value)
IndexOf()       → list.IndexOf(targetList, value)
LastIndexOf()   → list.LastIndexOf(targetList, value)
Max()           → list.Max(targetList, out isSuccess, out result)
Min()           → list.Min(targetList, out isSuccess, out result)
```

### Map 操作（Map.fcc）
```fc
import "Map.fcc" as map

New()           → map.New()
Remove()        → map.Remove(targetMap, key)
Clear()         → map.Clear(targetMap)
Length()        → map.Length(targetMap)
ContainKey()    → map.ContainKey(targetMap, key)    // 也可用内置的 ContainKey()
GetAllKeys()    → map.GetAllKeys(targetMap)
```

### 数学运算（Math.fcc）
```fc
import "Math.fcc" as math

// 常量
NaturalConstantType.Pi  → 3.14159265
NaturalConstantType.E   → 2.71828183

// 随机数
RandomInt()             → math.RandomInt(min, max)
RandomFloat()           → math.RandomFloat(min, max)
CreateRandomSeed()      → math.CreateRandomSeed(seed)
Next()                  → math.Next(randomGen, min, max)

// 基础数学
Abs()                   → math.Abs(value)
Sqrt()                  → math.Sqrt(value)
Negate()                → math.Negate(value)
Floor()                 → math.Floor(value)
Ceil()                  → math.Ceil(value)
Round()                 → math.Round(value)
Max()                   → math.Max(a, b)
Min()                   → math.Min(a, b)
Clamp()                 → math.Clamp(value, min, max)
Lerp()                  → math.Lerp(a, b, t)

// 三角函数
Sin()                   → math.Sin(degree)
Cos()                   → math.Cos(degree)
Tan()                   → math.Tan(degree)
ASin()                  → math.ASin(value)
ACos()                  → math.ACos(value)
ATan2()                 → math.ATan2(y, x)

// 幂运算
Exponentiation()        → math.Exponentiation(base, exponent)
Logarithm()             → math.Logarithm(baseValue, realNumber)

// Vector3 运算
Dot()                   → math.Dot(vecA, vecB)
Cross()                 → math.Cross(vecA, vecB)
Normalize()             → math.Normalize(vec)
Magnitude()             → math.Magnitude(vec)
Distance()              → math.Distance(vecA, vecB)
Angle()                 → math.Angle(vecA, vecB)
Projection()            → math.Projection(vecA, vecB)
LerpVector3()           → math.LerpVector3(vecA, vecB, t)
SlerpVector3()          → math.SlerpVector3(vecA, vecB, t)
Vector3Reflect()        → math.Vector3Reflect(direction, normal)

// Vector2 运算
Vector2Dot()            → math.Vector2Dot(vecA, vecB)
Vector2Distance()       → math.Vector2Distance(vecA, vecB)
Vector2Angle()          → math.Vector2Angle(vecA, vecB)
Vector2Normalize()      → math.Vector2Normalize(vec)
Vector2Magnitude()      → math.Vector2Magnitude(vec)
Vector2Reflect()        → math.Vector2Reflect(direction, normal)

// 四元数运算
QuaternionToEulerAngle()    → math.QuaternionToEulerAngle(quat)
EulerAngleToQuaternion()    → math.EulerAngleToQuaternion(euler)
AxisAngleToQuaternion()     → math.AxisAngleToQuaternion(axis, angle)
QuaternionToAxisAngle()     → math.QuaternionToAxisAngle(quat, out axis, out angle)
MultiplyQuaternion()        → math.MultiplyQuaternion(quatA, quatB)
LookRotation()              → math.LookRotation(forward, upward)
SlerpQuaternion()           → math.SlerpQuaternion(quatA, quatB, t)
QuaternionAngle()           → math.QuaternionAngle(quatA, quatB)
QuaternionDot()             → math.QuaternionDot(quatA, quatB)
QuaternionInverse()         → math.QuaternionInverse(quat)
QuaternionFromToRotation()  → math.QuaternionFromToRotation(from, to)
QuaternionRotateTowards()   → math.QuaternionRotateTowards(from, to, maxDegrees)
RotateVector()              → math.RotateVector(vec, deltaQuat)

// 方向转换
DirectionToEulerAngle()     → math.DirectionToEulerAngle(direction)
```

### 字符串操作（Strings.fcc）
```fc
import "Strings.fcc" as strings

Format()        → strings.Format(content, paramsList)
FormatStr()     → strings.FormatStr(content, paramsList)
Connect()       → strings.Connect(left, right)
Length()        → strings.Length(str)
Replace()       → strings.Replace(target, oldValue, newValue)
Find()          → strings.Find(target, findValue, startIndex)
Sub()           → strings.Sub(target, startIndex, length)
Split()         → strings.Split(target, sepStr)
FindAt()        → strings.FindAt(target, indexsList)
ToUpper()       → strings.ToUpper(target)
ToLower()       → strings.ToLower(target)
Strip()         → strings.Strip(target)
Join()          → strings.Join(stringList, separator)
```

### 物理检测（Physics.fcc）
```fc
import "Physics.fcc" as physics

// 射线检测
SingleRaycast()     → physics.SingleRaycast(startPos, direction, distance, layerMask, includeTrigger, out hitEntity, out hitPoint, out hitDistance, out hitNormal)
MultiRaycast()      → physics.MultiRaycast(startPos, direction, distance, layerMask, includeTrigger, out hitEntities, out hitPoints, out hitDistances, out hitNormals)

// 区域检测 - Cast（移动扫描）
BoxCast()           → physics.BoxCast(halfExtents, center, rotation, direction, maxDistance, layerMask, includeTrigger, out hitEntities)
SphereCast()        → physics.SphereCast(radius, center, direction, maxDistance, layerMask, includeTrigger, out hitEntities)
CapsuleCast()       → physics.CapsuleCast(radius, height, center, rotation, direction, maxDistance, layerMask, includeTrigger, out hitEntities)

// 区域检测 - Overlap（静态范围）
BoxOverlap()        → physics.BoxOverlap(halfExtents, center, rotation, layerMask, includeTrigger, out hitEntities)
SphereOverlap()     → physics.SphereOverlap(radius, center, layerMask, includeTrigger, out hitEntities)
CapsuleOverlap()    → physics.CapsuleOverlap(radius, height, center, rotation, layerMask, includeTrigger, out hitEntities)

// 区域判断
IsInsideSphere()    → physics.IsInsideSphere(entity, center, radius)
IsInsideCylinder()  → physics.IsInsideCylinder(entity, center, radius, height, rotation)
IsInsideBox()       → physics.IsInsideBox(entity, center, length, width, height, rotation)
IsInsideSector()    → physics.IsInsideSector(entity, center, radius, cutRadius, height, angle, rotation)

// 刚体力学
AddForce()              → physics.AddForce(target, force, forceMode)
AddForceAtPosition()    → physics.AddForceAtPosition(target, force, position, forceMode)
AddTorque()             → physics.AddTorque(target, torque, forceMode)
MovePosition()          → physics.MovePosition(target, position)
MoveRotation()          → physics.MoveRotation(target, rotation)

// 刚体状态
Sleep()                     → physics.Sleep(target)
Wakeup()                    → physics.Wakeup(target)
IsSleeping()                → physics.IsSleeping(target)
SetSleepThreshold()         → physics.SetSleepThreshold(target, threshold)
GetSleepThreshold()         → physics.GetSleepThreshold(target)
SetGlobalSleepThreshold()   → physics.SetGlobalSleepThreshold(threshold)
GetGlobalSleepThreshold()   → physics.GetGlobalSleepThreshold()

// 角色控制器
MoveCCT()       → physics.MoveCCT(target, movement)
TeleportCCT()   → physics.TeleportCCT(target, position)
```

### 战斗系统（Combat.fcc）
```fc
import "Combat.fcc" as combat

DealDamage()            → combat.DealDamage(target, attacker, damageType, damage)
Eliminate()             → combat.Eliminate(target)
EliminateAtNextFrame()  → combat.EliminateAtNextFrame(target)
```

### 类型转换（Convert.fcc）
```fc
import "Convert.fcc" as convert

ToString()              → convert.ToString(target)
IntToFloat()            → convert.IntToFloat(value)
NumToString()           → convert.NumToString(value, style)
StringToInt()           → convert.StringToInt(target, out result, out isSuccess)
StringToFloat()         → convert.StringToFloat(target, out result, out isSuccess)
Vector3ToVector2()      → convert.Vector3ToVector2(vec3)
Vector2ToVector3()      → convert.Vector2ToVector3(vec2)
EulerAngleToVector3()   → convert.EulerAngleToVector3(euler)
BitwiseListToInt()      → convert.BitwiseListToInt(bitArray)
BitwiseIntToList()      → convert.BitwiseIntToList(value)
```

### 时间系统（Time.fcc）
```fc
import "Time.fcc" as time

GetLocalTimestamp()     → time.GetLocalTimestamp()       // [platform_client]
PauseFixedUpdate()      → time.PauseFixedUpdate()
ResumeFixedUpdate()     → time.ResumeFixedUpdate()
```

### 动画系统（Animation.fcc）
```fc
import "Animation.fcc" as anim

PlayAnimation()         → anim.PlayAnimation(target, state, playSpeed, loopType)
StopAnimation()         → anim.StopAnimation(target, state)
SetBodyPartWeight()     → anim.SetBodyPartWeight(target, bodyPartName, weight)
```

---

## 事件到库映射表

### UI 事件（Hud.fcc）
```fc
import "Hud.fcc" as hud

// 按钮交互事件
OnTapped()                  → import "Hud.fcc"
OnClick()                   → import "Hud.fcc"
OnPressed()                 → import "Hud.fcc"
OnPress()                   → import "Hud.fcc"
OnReleased()                → import "Hud.fcc"
OnRelease()                 → import "Hud.fcc"
OnDoubleTapped()            → import "Hud.fcc"
OnDoubleClick()             → import "Hud.fcc"

// UI 状态事件
OnUIShow()                  → import "Hud.fcc"
OnHudShow()                 → import "Hud.fcc"
OnUIHide()                  → import "Hud.fcc"
OnHudHide()                 → import "Hud.fcc"

// 其他 UI 事件
OnTextChange()              → import "Hud.fcc"
OnCountdownFinished()       → import "Hud.fcc"
OnBuiltInCloseButtonTapped() → import "Hud.fcc"
OnBuiltInButtonTapped()     → import "Hud.fcc"
OnInternalButtonClick()     → import "Hud.fcc"
OnCameraRaycast()           → import "Hud.fcc"
OnClientCameraRayCast()     → import "Hud.fcc"
OnFriendsUpdate()           → import "Hud.fcc"
OnFriendRelationChange()    → import "Hud.fcc"
```

### 玩家事件（Player.fcc）
```fc
import "Player.fcc" as player

// 玩家连接事件
OnPlayerJoin()              → import "Player.fcc"
OnPlayerQuit()              → import "Player.fcc"
OnDisconnect()              → import "Player.fcc"
OnDisconnected()            → import "Player.fcc"
OnReconnect()               → import "Player.fcc"
OnReconnected()             → import "Player.fcc"
OnUserQuitOrUserMacthEnd()  → import "Player.fcc"

// 玩家动作事件
OnJump()                    → import "Player.fcc"
OnJumpStop()                → import "Player.fcc"
OnCrouch()                  → import "Player.fcc"
OnCreep()                   → import "Player.fcc"
OnSprint()                  → import "Player.fcc"
OnSprintStop()              → import "Player.fcc"
OnDash()                    → import "Player.fcc"
OnMove()                    → import "Player.fcc"
OnIdle()                    → import "Player.fcc"
OnFall()                    → import "Player.fcc"
OnFallStop()                → import "Player.fcc"
OnStandUP()                 → import "Player.fcc"

// 玩家状态事件
OnPlayerRevived()           → import "Player.fcc"
OnPlayerRevive()            → import "Player.fcc"
OnRevived()                 → import "Player.fcc"
OnSurfing()                 → import "Player.fcc"
OnSurfingStop()             → import "Player.fcc"
OnStartFire()               → import "Player.fcc"
OnUseAvatarSkill()          → import "Player.fcc"
```

### 战斗事件（Combat.fcc）
```fc
import "Combat.fcc" as combat

// 伤害和击杀事件
OnPreTakeDamage()           → import "Combat.fcc"
OnTakeDamage()              → import "Combat.fcc"
OnPreDealDamage()           → import "Combat.fcc"
OnDealDamage()              → import "Combat.fcc"
OnEliminated()              → import "Combat.fcc"
OnEliminate()               → import "Combat.fcc"
OnKnockedDown()             → import "Combat.fcc"
OnBeKnockedDown()           → import "Combat.fcc"
OnAssist()                  → import "Combat.fcc"

// 全局战斗事件
OnPlayerBeEliminated()      → import "Combat.fcc"
OnPlayerDead()              → import "Combat.fcc"
OnPlayerAssist()            → import "Combat.fcc"
OnPlayerDealDamage()        → import "Combat.fcc"
OnPlayerDamage()            → import "Combat.fcc"
OnPlayerEliminate()         → import "Combat.fcc"
OnPlayerKill()              → import "Combat.fcc"
OnPlayerBeKnockedDown()     → import "Combat.fcc"
OnTeamAce()                 → import "Combat.fcc"
OnACE()                     → import "Combat.fcc"
```

### 物理事件（Physics.fcc）
```fc
import "Physics.fcc" as physics

// 碰撞事件
OnCollisionEnter()          → import "Physics.fcc"
OnCollisionExit()           → import "Physics.fcc"
OnCharacterControllerHit()  → import "Physics.fcc"
OnControllerColliderHit()   → import "Physics.fcc"

// 触发器事件
OnEntityEnter()             → import "Physics.fcc"
OnEntityEnterTrigger()      → import "Physics.fcc"
OnEntityExit()              → import "Physics.fcc"
OnEntityLeaveTrigger()      → import "Physics.fcc"

// 刚体事件
OnWakeUp()                  → import "Physics.fcc"
OnWakeup()                  → import "Physics.fcc"
OnSleep()                   → import "Physics.fcc"
```

### 物品和武器事件（Items.fcc）
```fc
import "Items.fcc" as items

// 装备事件
OnEquipArmor()              → import "Items.fcc"
OnEquipWeapon()             → import "Items.fcc"
OnWeaponBeEquiped()         → import "Items.fcc"
OnBeEquiped()               → import "Items.fcc"
OnEquiped()                 → import "Items.fcc"
OnEquip()                   → import "Items.fcc"

// 使用物品事件
OnUseConsumable()           → import "Items.fcc"
OnUseItem()                 → import "Items.fcc"
OnUseSupply()               → import "Items.fcc"
OnUsed()                    → import "Items.fcc"

// 获取和丢弃事件
OnAccessItem()              → import "Items.fcc"
OnObtainItem()              → import "Items.fcc"
OnAccessWeapon()            → import "Items.fcc"
OnObtainWeapon()            → import "Items.fcc"
OnAccessEquipment()         → import "Items.fcc"
OnPlayerEquip()             → import "Items.fcc"
OnDropWeapon()              → import "Items.fcc"
OnDropConsumable()          → import "Items.fcc"
OnDropItem()                → import "Items.fcc"
OnPickedUp()                → import "Items.fcc"
OnPickup()                  → import "Items.fcc"
OnDropped()                 → import "Items.fcc"
OnDrop()                    → import "Items.fcc"

// 武器操作事件
OnFire()                    → import "Items.fcc"
OnReload()                  → import "Items.fcc"
OnWeaponStopFiring()        → import "Items.fcc"
OnStopFire()                → import "Items.fcc"
OnAiming()                  → import "Items.fcc"
OnAimed()                   → import "Items.fcc"
OnSwitchHandHeld()          → import "Items.fcc"
OnPlayerHandHeld()          → import "Items.fcc"

// 武器击中事件
OnBulletHit()               → import "Items.fcc"
OnHit()                     → import "Items.fcc"
OnHitByBullet()             → import "Items.fcc"
OnHitted()                  → import "Items.fcc"

// 特殊物品事件
OnLandmineActive()          → import "Items.fcc"
OnLandmineTrigger()         → import "Items.fcc"
OnHookGunFire()             → import "Items.fcc"
OnFires()                   → import "Items.fcc"
OnThrowableExplode()        → import "Items.fcc"
```

### 关卡物件事件（LevelObject.fcc）
```fc
import "LevelObject.fcc" as levelobject

// 玩家进入/离开事件
OnPlayerEnter()             → import "LevelObject.fcc"
OnPlayerEnterTrigger()      → import "LevelObject.fcc"
OnPlayerLeave()             → import "LevelObject.fcc"
OnPlayerLeaveTrigger()      → import "LevelObject.fcc"

// 载具事件
OnEnterVehicle()            → import "LevelObject.fcc"
OnEnteringVehicle()         → import "LevelObject.fcc"
OnLeaveVehicle()            → import "LevelObject.fcc"
OnLeavingVehicle()          → import "LevelObject.fcc"
OnDriveVehicle()            → import "LevelObject.fcc"
OnDrivingVehicle()          → import "LevelObject.fcc"
OnEntered()                 → import "LevelObject.fcc"
OnBeEntered()               → import "LevelObject.fcc"
OnLeft()                    → import "LevelObject.fcc"
OnBeLeft()                  → import "LevelObject.fcc"
OnDriven()                  → import "LevelObject.fcc"
OnBeDrived()                → import "LevelObject.fcc"
OnDrived()                  → import "LevelObject.fcc"

// 机关事件
OnUsePortal()               → import "LevelObject.fcc"
OnTeleporting()             → import "LevelObject.fcc"
OnTeleportEntity()          → import "LevelObject.fcc"
OnBeTeleported()            → import "LevelObject.fcc"
OnBouncedByTire()           → import "LevelObject.fcc"
OnBouncesOffTire()          → import "LevelObject.fcc"
OnBounceEntity()            → import "LevelObject.fcc"
OnBeBouncesOffTire()        → import "LevelObject.fcc"
OnSpringing()               → import "LevelObject.fcc"
OnHitFly()                  → import "LevelObject.fcc"
OnBeHitFly()                → import "LevelObject.fcc"
OnHitFlyEntity()            → import "LevelObject.fcc"
OnHitFlying()               → import "LevelObject.fcc"
OnExplode()                 → import "LevelObject.fcc"
```

### 场景事件（Scene.fcc）
```fc
import "Scene.fcc" as scene

OnSceneLoad()               → import "Scene.fcc"
OnSceneLoadSuccessed()      → import "Scene.fcc"
OnSceneSwitch()             → import "Scene.fcc"
OnSceneSwitchSuccessed()    → import "Scene.fcc"
OnPlayerSwitchScene()       → import "Scene.fcc"
OnSwitchArea()              → import "Scene.fcc"
```

### 工作流事件（Workflow.fcc）
```fc
import "Workflow.fcc" as workflow

OnRoundStart()              → import "Workflow.fcc"
OnRoundEnd()                → import "Workflow.fcc"
OnPhaseStart()              → import "Workflow.fcc"
OnPhaseEnd()                → import "Workflow.fcc"
```

### 播放器事件（Playable.fcc）
```fc
import "Playable.fcc" as playable

OnEachLoop()                → import "Playable.fcc"
OnStart()                   → import "Playable.fcc"
OnEnd()                     → import "Playable.fcc"
OnResume()                  → import "Playable.fcc"
OnPause()                   → import "Playable.fcc"
```

### 输入系统事件（InputSystem.fcc）
```fc
import "InputSystem.fcc" as inputsystem

OnScreenTouchBegin()        → import "InputSystem.fcc"
OnScreenTouchEnd()          → import "InputSystem.fcc"
```

### 其他事件
```fc
// Morph.fcc
OnLevelObjectBeMorphed()    → import "Morph.fcc"
OnLevelObjectToBeMorphed()  → import "Morph.fcc"

// Premium.fcc
OnPremiumChange()           → import "Premium.fcc"
OnPlayerEnterPremiumCenter() → import "Premium.fcc"
OnPlayerLeavePremiumCenter() → import "Premium.fcc"

// Time.fcc
OnFixedUpdate()             → import "Time.fcc"
OnGamePause()               → import "Time.fcc"
OnGameResume()              → import "Time.fcc"
```

---

## 内置函数和事件（无需 Import）

以下函数和事件在 StdLibrary 中，可以直接使用，无需 import：

### 内置函数
```fc
// 日志
LogInfo(content)
LogWarning(content)
LogError(content)

// 时间等待
WaitForMillisecond(time)
WaitForSecond(time)
WaitForFrame(frameCount)
WaitForNextFrame()

// 玩家查询
GetAllPlayers()
GetPlayerByAccountID(accountID)

// 实体操作
CreateFromPrefab(out var entity, prefabID)
Destroy(entity)
HasComponent(entity, componentType)
AddScript(entity, scriptID)

// 事件分发
DispatchEvent(eventID, targetEntity, paramsList)

// 传送
Teleport(player, position, rotation)

// 标签系统
AddTag(entity, tag)
RemoveTag(entity, tag)
HasTag(entity, tag)

// Map 内置操作
ContainKey(map, key)        // 检查键是否存在

// 格式化
Format(content, paramsList)  // 内置函数版本
```

### 内置事件（无需 Import）
```fc
// 生命周期事件（StdLibrary）
OnAwake()           // 实体创建时
OnStart()           // 游戏开始时（已废弃，不建议使用）
OnGameStart()       // 游戏开始时
OnUpdate()          // 每帧更新
OnGameEnd()         // 游戏结束时
OnDestroy()         // 实体销毁时
OnEnable()          // 实体启用时
OnDisable()         // 实体禁用时

// 生成事件（StdLibrary）
OnSpawn()           // 生成物品时
OnPlotStart()       // 剧情开始时
OnPlotEnd()         // 剧情结束时
OntriggerPlotOption() // 触发剧情选项时
```

---

## 编辑器生成库（EditorGenLib.fcc）

```fc
import "EditorGenLib.fcc" as gen
// 或
import Res from "EditorGenLib.fcc"

// 枚举资源
EResPrefab.SceneCube            // 预制体枚举
EResSceneIsleLand.WinnerView    // 场景物件枚举
EResUI.BombHUD                  // UI 资源枚举
EResSprite.ui_icon_skill        // 图标资源枚举

// 动态访问
Res.FCG["ScriptName"]           // 访问脚本资源
```

---

## 快速检查清单

每次编写代码时，按此顺序检查：

1. 识别函数类型
   - 这个函数是内置的吗？
   - 是 -> 无需 import
   - 否 -> 继续下一步

2. 查找函数所属库
   - List 操作 -> import "List.fcc" as list
   - Map 操作 -> import "Map.fcc" as map
   - 数学计算 -> import "Math.fcc" as math
   - 字符串 -> import "Strings.fcc" as strings
   - 物理检测 -> import "Physics.fcc" as physics
   - 战斗系统 -> import "Combat.fcc" as combat
   - 类型转换 -> import "Convert.fcc" as convert

3. 添加 import 语句
```fc
// 在文件开头添加
import "StdLibrary.fcc" as std
import "List.fcc" as list
import "Math.fcc" as math
```

4. 使用命名空间调用
```fc
// 推荐：使用命名空间前缀
list.Append(myList, value)
math.RandomInt(1, 10)
strings.Length(myString)

// 避免：直接调用（会导致编译错误）
Append(myList, value)      // 错误
RandomInt(1, 10)           // 错误
```

---

## 常见错误

### 错误示例 1：忘记 import
```fc
graph BadExample {
    event OnAwake() {
        var myList = New(0, 10)        // 错误：New 未定义
        Append(myList, 42)             // 错误：Append 未定义
    }
}
```

**修复：**
```fc
import "StdLibrary.fcc" as std
import "List.fcc" as list

graph GoodExample {
    event OnAwake() {
        var myList = list.New(0, 10)   // 正确
        list.Append(myList, 42)        // 正确
    }
}
```

### 错误示例 2：混淆内置和库函数
```fc
import "Math.fcc" as math

graph BadExample {
    event OnAwake() {
        LogInfo("游戏开始")            // 正确：内置函数
        var dist = Distance(posA, posB)  // 错误：应该用 math.Distance()
    }
}
```

**修复：**
```fc
import "StdLibrary.fcc" as std
import "Math.fcc" as math

graph GoodExample {
    event OnAwake() {
        LogInfo("游戏开始")                     // 正确：内置函数
        var dist = math.Distance(posA, posB)    // 正确：使用命名空间
    }
}
```

---

## 调试技巧

遇到"未定义符号"错误时：

1. 检查是否是内置函数
   - 查看本文档"内置函数"部分
   - 内置函数无需 import

2. 查询函数映射表
   - 在本文档中搜索函数名
   - 找到对应的库和用法

3. 检查命名空间
   - 确保使用了正确的命名空间前缀
   - 例如：list.Append() 而不是 Append()

4. 检查拼写
   - FC 语言区分大小写
   - 例如：ContainKey 而不是 ContainsKey

---

基于 Free Fire Craftland builtin 库生成
VS Code 插件：craftlandstudio.ffugclanguage

`````

### Source: `.github/instructions/fc-syntax.instructions.md`

`````text
---
description: FC语言完整编程参考 - 语法、API、组件、事件、最佳实践的全面指南
globs: *.fcg,*.fcc
applyTo: "**/*. {fcc,fcg}"
alwaysApply: true
---

# FC语言完整编程参考

> 基于 Free Fire Craftland 官方文档: https://ffcraftland.garena.com/en/docs/api

##  目录

1. [核心概念](#核心概念)
2. [语法参考](#语法参考)
3. [类型系统](#类型系统)
4. [内置库API参考](#内置库api参考)
5. [组件系统](#组件系统)
6. [事件系统](#事件系统)
7. [编程模式](#编程模式)
8. [最佳实践](#最佳实践)
9. [调试指南](#调试指南)
10. [常见问题](#常见问题)

---

## 核心概念

### FC语言设计理念
FC（Free Fire Code Language）是面向数据设计的DSL，用于Free Fire UGC游戏开发。

**核心特点：**
- 面向数据设计（而非面向对象）
- 实体-组件架构（Entity-Component）
- 强类型系统
- 异步编程支持
- 跨平台兼容

### 文件类型

| 扩展名 | 类型 | 用途 | 示例 |
|--------|------|------|------|
| `.fcc` | 库定义文件 | 定义组件、类型、API、事件、枚举 | `MyLibrary.fcc` |
| `.fcg` | 脚本逻辑文件 | 编写graph、变量、函数、事件处理 | `Script.fcg` |

### 平台声明

```fc
// 客户端脚本
[platform_client]
graph ClientScript {
    // 只能使用客户端支持的API和事件
}

// 服务端脚本（默认）
[platform_server]
graph ServerScript {
    // 服务端逻辑
}
```

---

## 语法参考

### 导入系统

```fc
// 导入内置库
import "StdLibrary.fcc" as StdLib

// 导入编辑器生成库
import "EditorGenLib.fcc" as EditorLib

// 导入用户自定义库
import "MyCustomLib.fcc" as MyLib

// 导入其他脚本
import "../Scripts/Utils.fcg" as Utils
```

### 变量声明

```fc
// 局部变量
var num int = 10
var name = "Player"  // 类型推断
var pos Vector3     // 未初始化

// 脚本成员变量
graph MyGraph {
    PlayerCount int = 0
    GameStarted bool = false
    
    event OnAwake() {
        PlayerCount = 5
    }
}
```

### 函数定义

```fc
// 普通函数
func Add(a int, b int) int {
    return a + b
}

// 异步函数
async func DelayedAction(delay int, out var result string) {
    WaitForMillisecond(delay)
    result = "完成"
}

// 无返回值函数
func LogMessage(msg string) {
    LogInfo(msg)
}
```

### 流程控制

#### 条件语句
```fc
if health > 50 {
    LogInfo("健康状态良好")
} else if health > 20 {
    LogInfo("健康状态一般")
} else {
    LogInfo("健康状态危险")
}
```

#### 循环语句
```fc
// for循环 (start, end, step) - 左闭右开区间
for i = 0, 10, 1 {
    LogInfo("计数: " + i)
}

// for range循环
var myList = List<int>{}
for index, value in myList {
    LogInfo("索引: " + index + ", 值: " + value)
}

// while循环
while playerCount < maxPlayers {
    SpawnPlayer()
    playerCount = playerCount + 1
}
```

### 异步编程

```fc
graph AsyncExample {
    event OnGameStart() {
        // 等待异步完成
        wait DelayedSpawn(3000, out var success)
        if success {
            LogInfo("玩家生成成功")
        }
        
        // 异步执行，不等待
        start BackgroundTask()
    }
    
    async func DelayedSpawn(delay int, out var success bool) {
        WaitForMillisecond(delay)
        // 生成玩家逻辑
        success = true
    }
    
    async func BackgroundTask() {
        // 后台任务
        WaitForMillisecond(1000)
        LogInfo("后台任务完成")
    }
}
```

---

## 类型系统

### 基本类型

| 类型 | 描述 | 示例 |
|------|------|------|
| `bool` | 布尔类型 | `true`, `false` |
| `int` | 32位整型 | `42`, `-10` |
| `int64` | 64位整型 | `9223372036854775807` |
| `float` | 单精度浮点 | `3.14`, `-0.5` |
| `string` | 字符串 | `"Hello World"` |
| `LocString` | 本地化字符串 | 多语言文本 |

### 数学类型

```fc
// 向量类型
var pos2D Vector2 = Vector2{1.0, 2.0}
var pos3D Vector3 = Vector3{1.0, 2.0, 3.0}

// 四元数（旋转）
var rotation Quaternion = Quaternion{0.0, 0.0, 0.0, 1.0}

// 访问分量
var x = pos3D.X
var y = pos3D.Y
var z = pos3D.Z
```

### 容器类型

```fc
// 列表
var numbers List<int> = List<int>{}
numbers.Add(1)
numbers.Add(2)

// 映射
var playerScores Map<string, int> = Map<string, int>{}
playerScores["Player1"] = 100
playerScores["Player2"] = 85

// 访问
var score = playerScores["Player1"]
var firstNumber = numbers[0]
```

### 实体类型

```fc
// 泛型实体类型
var player entity<Player>
var box entity<LevelObject>

// 访问组件
var playerName = player<Entity>.Name
var boxPosition = box<Transform>.Position

// 当前实体
var currentPos = thisEntity<Transform>.Position
```

### 资源ID类型

```fc
// 常用资源ID类型
var meshId MeshID = "mesh_cube_001"
var audioId AudioID = "sound_explosion"
var animId AnimationClipID = "anim_walk_cycle"
var materialId MaterialID = "mat_grass"
var prefabId PrefabID = "prefab_building"
```

---

## 内置库API参考

> 完整API参考：https://ffcraftland.garena.com/en/docs/api

### 核心库 (StdLibrary)

#### 日志函数
```fc
// 基础日志
func LogInfo(content object)     // 信息日志
func LogWarning(content object)  // 警告日志
func LogError(content object)    // 错误日志

// 使用示例
LogInfo("游戏开始")
LogWarning("玩家血量低: " + health)
LogError("关键错误: " + errorMsg)
```

#### 时间函数
```fc
// 等待函数
func WaitForMillisecond(time int)          // 等待毫秒
func WaitForSecond(time float)             // 等待秒
func WaitForFrame(frameCount int)          // 等待帧

// 时间获取
func GetCurrentTimestamp() int64           // 获取时间戳
func GetGameTime() float                   // 获取游戏时间
```

### 数学库 (Math)

#### 数学常量
```fc
// 常量枚举
enum NaturalConstantType {
    Pi = 3.14159265    // 圆周率
    E = 2.71828183     // 自然常数
}
```

#### 向量运算
```fc
// Vector3运算
func DotProduct(a Vector3, b Vector3) float                    // 点积
func CrossProduct(a Vector3, b Vector3) Vector3                // 叉积
func Vector3Distance(a Vector3, b Vector3) float               // 距离
func Vector3Normalize(value Vector3) Vector3                   // 归一化
func Vector3Magnitude(value Vector3) float                     // 长度

// 插值函数
func LerpVector3(a Vector3, b Vector3, t float) Vector3        // 线性插值
func SlerpVector3(a Vector3, b Vector3, t float) Vector3       // 球面插值
```

#### 四元数运算
```fc
// 四元数转换
func QuaternionToEulerAngle(value Quaternion) Vector3          // 转欧拉角
func EulerAngleToQuaternion(value Vector3) Quaternion          // 欧拉角转四元数
func LookRotation(forward Vector3, upward Vector3) Quaternion  // 朝向旋转

// 四元数插值
func SlerpQuaternion(valueA Quaternion, valueB Quaternion, valueT float) Quaternion
```

#### 数值运算
```fc
// 基础数学
func Abs(value float) float                    // 绝对值
func Sqrt(value float) float                   // 平方根
func Pow(base float, exponent float) float     // 幂运算
func Sin(value float) float                    // 正弦
func Cos(value float) float                    // 余弦
func Tan(value float) float                    // 正切

// 范围运算
func Clamp(value float, min float, max float) float           // 限制范围
func Lerp(a float, b float, t float) float                    // 线性插值
func Max(a float, b float) float                              // 最大值
func Min(a float, b float) float                              // 最小值
```

### 物理库 (Physics)

#### 刚体组件
```fc
component Rigidbody {
    Type RigidbodyType          // Static/Dynamic/Kinematic
    UseGravity bool             // 使用重力
    Mass float                  // 质量(kg)
    Velocity Vector3            // 线性速度(m/s)
    AngularVelocity Vector3     // 角速度(rad/s)
    Drag float                  // 阻力系数
    AngularDrag float           // 角阻力系数
    Constrain int               // 约束条件
}
```

#### 碰撞器组件
```fc
component Collider {
    Enable bool                 // 启用状态
    IsTrigger bool             // 是否为触发器
    PhysicalLayer int          // 物理层
}

// 碰撞事件
event OnTriggerEnter(other entity<Entity>)
event OnTriggerExit(other entity<Entity>)
event OnCollisionEnter(other entity<Entity>)
event OnCollisionExit(other entity<Entity>)
```

#### 物理函数
```fc
// 施加力
func AddForce(target entity<Rigidbody>, force Vector3, forceType ForceType)
func AddTorque(target entity<Rigidbody>, torque Vector3, forceType ForceType)

// 射线检测
func Raycast(origin Vector3, direction Vector3, distance float, out var hit RaycastHit) bool
func RaycastAll(origin Vector3, direction Vector3, distance float) List<RaycastHit>
```

### 玩家库 (Player)

#### 玩家组件
```fc
component Player {
    AccountID UUID              // 账户ID
    NickName string            // 昵称
    TeamID int                 // 队伍ID
    Health float               // 血量
    MaxHealth float            // 最大血量
    Speed float                // 移动速度
    State PlayerStateType      // 玩家状态 (Alive/KnockedDown/Dead)
}
```

#### 玩家函数
```fc
// 玩家操作
func KillPlayer(player entity<Player>)                        // 击杀玩家
func RevivePlayer(player entity<Player>)                      // 复活玩家
func TeleportPlayer(player entity<Player>, position Vector3)  // 传送玩家
func SetPlayerHealth(player entity<Player>, health float)     // 设置血量

// 玩家查询
func GetAllPlayers() List<entity<Player>>                      // 获取所有玩家
func GetPlayerByIndex(index int) entity<Player>               // 按索引获取
func GetLocalPlayer() entity<Player>                          // 获取本地玩家
```

### 场景物件库 (LevelObject)

#### 变换组件
```fc
component Transform {
    Position Vector3            // 位置
    Rotation Quaternion         // 旋转
    Scale Vector3              // 缩放
}
```

#### 实体组件
```fc
component Entity {
    Name string                 // 名称
    Active bool                // 激活状态
    Tag string                 // 标签
}
```

#### 场景函数
```fc
// 物件操作
func CreateLevelObject(id LevelObjectID, position Vector3) entity<LevelObject>
func DestroyLevelObject(obj entity<LevelObject>)
func SetObjectActive(obj entity<LevelObject>, active bool)

// 查找物件
func FindLevelObjectByName(name string) entity<LevelObject>
func FindLevelObjectsWithTag(tag string) List<entity<LevelObject>>
```

### 动画库 (Animation)

#### 动画组件
```fc
component AnimationController {
    AttachTarget entity<Entity>    // 绑定目标
    Resource string               // 资源ID
}

component AnimationClip {
    ClipLength float             // 片段长度
    PlaySpeed float              // 播放速度
    IsLoop bool                  // 是否循环
}
```

#### 动画函数
```fc
// 播放动画
func PlayAnimation(controller entity<AnimationController>, clipName string)
func StopAnimation(controller entity<AnimationController>)
func SetAnimationSpeed(controller entity<AnimationController>, speed float)
```

### UI库 (Hud)

#### UI组件示例
```fc
component ButtonWidget {
    Visible bool                // 可见性
    Enable bool                // 启用状态
    Text string                // 按钮文本
}

component TextWidget {
    Visible bool
    Text string
    FontSize int
    Color Vector3               // RGB颜色
}
```

#### UI事件
```fc
// 按钮事件
event OnTapped(player entity<Player>)          // 点击事件
event OnPressed(player entity<Player>)         // 按下事件
event OnReleased(player entity<Player>)        // 释放事件
```

---

## 组件系统

### 组件定义 (.fcc文件)

```fc
// 自定义组件示例
component HealthSystem {
    CurrentHealth float = 100.0
    MaxHealth float = 100.0
    RegenerationRate float = 1.0    // 每秒回复
    IsInvulnerable bool = false
}

component Inventory {
    Items List<ItemID> = List<ItemID>{}
    MaxSlots int = 20
    CurrentWeight float = 0.0
    MaxWeight float = 100.0
}
```

### 组件使用

```fc
graph HealthManager {
    event OnAwake() {
        // 初始化血量系统
        thisEntity<HealthSystem>.CurrentHealth = 100.0
        start HealthRegeneration()
    }
    
    event OnDamaged(damage float) {
        if !thisEntity<HealthSystem>.IsInvulnerable {
            var newHealth = thisEntity<HealthSystem>.CurrentHealth - damage
            thisEntity<HealthSystem>.CurrentHealth = Max(0.0, newHealth)
            
            if newHealth <= 0.0 {
                HandleDeath()
            }
        }
    }
    
    async func HealthRegeneration() {
        while thisEntity<HealthSystem>.CurrentHealth > 0.0 {
            WaitForSecond(1.0)
            var current = thisEntity<HealthSystem>.CurrentHealth
            var max = thisEntity<HealthSystem>.MaxHealth
            var regen = thisEntity<HealthSystem>.RegenerationRate
            
            if current < max && !thisEntity<HealthSystem>.IsInvulnerable {
                thisEntity<HealthSystem>.CurrentHealth = Min(max, current + regen)
            }
        }
    }
    
    func HandleDeath() {
        LogInfo("Entity died: " + thisEntity<Entity>.Name)
        // 死亡逻辑
    }
}
```

---

## 事件系统

### 内置事件

#### 生命周期事件
```fc
event OnAwake()                    // 实体创建时
event OnStart()                    // 游戏开始时
event OnDestroy()                  // 实体销毁时
event OnUpdate()                   // 每帧更新
```

#### 游戏事件
```fc
event OnGameStart()                // 游戏开始
event OnGameEnd()                  // 游戏结束
event OnPlayerJoin(player entity<Player>)      // 玩家加入
event OnPlayerLeave(player entity<Player>)     // 玩家离开
```

#### 物理事件
```fc
event OnTriggerEnter(other entity<Entity>)     // 触发器进入
event OnTriggerExit(other entity<Entity>)      // 触发器退出
event OnCollisionEnter(other entity<Entity>)   // 碰撞开始
event OnCollisionExit(other entity<Entity>)    // 碰撞结束
```

#### UI事件
```fc
event OnTapped(player entity<Player>)          // UI点击
event OnValueChanged(newValue float)           // 数值变化
event OnTextChanged(newText string)            // 文本变化
```

### 自定义事件

#### 定义事件 (.fcc文件)
```fc
// 游戏相关事件
event OnPlayerScoreChanged(player entity<Player>, newScore int)
event OnItemCollected(player entity<Player>, item ItemID)
event OnBossDefeated(boss entity<LevelObject>)
event OnWaveComplete(waveNumber int)

// 系统事件
event OnConfigurationChanged(config string)
event OnNetworkStatusChanged(isConnected bool)
```

#### 触发事件
```fc
graph GameManager {
    PlayerScores Map<entity<Player>, int> = Map<entity<Player>, int>{}
    
    func AddScore(player entity<Player>, points int) {
        var currentScore = PlayerScores[player]
        var newScore = currentScore + points
        PlayerScores[player] = newScore
        
        // 触发自定义事件
        OnPlayerScoreChanged(player, newScore)
    }
    
    // 处理事件
    event OnPlayerScoreChanged(player entity<Player>, newScore int) {
        LogInfo(player<Entity>.Name + " 得分: " + newScore)
        
        if newScore >= 1000 {
            LogInfo("玩家达成高分成就!")
        }
    }
}
```

---

## 编程模式

### 1. 状态机模式

```fc
enum GameState {
    MainMenu = 0
    Playing = 1
    Paused = 2
    GameOver = 3
}

graph GameStateManager {
    CurrentState GameState = GameState.MainMenu
    
    func ChangeState(newState GameState) {
        var oldState = CurrentState
        CurrentState = newState
        
        OnStateExit(oldState)
        OnStateEnter(newState)
    }
    
    func OnStateEnter(state GameState) {
        if state == GameState.Playing {
            StartGame()
        } else if state == GameState.Paused {
            PauseGame()
        } else if state == GameState.GameOver {
            EndGame()
        }
    }
    
    func OnStateExit(state GameState) {
        // 状态退出逻辑
    }
}
```

### 2. 对象池模式

```fc
graph BulletPool {
    PoolSize int = 100
    AvailableBullets List<entity<LevelObject>> = List<entity<LevelObject>>{}
    ActiveBullets List<entity<LevelObject>> = List<entity<LevelObject>>{}
    
    event OnAwake() {
        InitializePool()
    }
    
    func InitializePool() {
        for i = 0, PoolSize, 1 {
            var bullet = CreateLevelObject("BulletPrefab", Vector3{0, -100, 0})
            SetObjectActive(bullet, false)
            AvailableBullets.Add(bullet)
        }
    }
    
    func GetBullet() entity<LevelObject> {
        if AvailableBullets.Count > 0 {
            var bullet = AvailableBullets[0]
            AvailableBullets.RemoveAt(0)
            ActiveBullets.Add(bullet)
            SetObjectActive(bullet, true)
            return bullet
        }
        return null
    }
    
    func ReturnBullet(bullet entity<LevelObject>) {
        ActiveBullets.Remove(bullet)
        AvailableBullets.Add(bullet)
        SetObjectActive(bullet, false)
        bullet<Transform>.Position = Vector3{0, -100, 0}
    }
}
```

### 3. 观察者模式

```fc
graph EventManager {
    ScoreChangeListeners List<entity<Entity>> = List<entity<Entity>>{}
    
    func RegisterScoreListener(listener entity<Entity>) {
        if !ScoreChangeListeners.Contains(listener) {
            ScoreChangeListeners.Add(listener)
        }
    }
    
    func UnregisterScoreListener(listener entity<Entity>) {
        ScoreChangeListeners.Remove(listener)
    }
    
    func NotifyScoreChange(player entity<Player>, newScore int) {
        for i = 0, ScoreChangeListeners.Count, 1 {
            var listener = ScoreChangeListeners[i]
            // 通知监听器（需要监听器实现相应接口）
            OnPlayerScoreChanged(player, newScore)
        }
    }
}
```

### 4. 缓动动画模式

```fc
graph TweenManager {
    // 缓动函数
    func EaseInOut(t float) float {
        if t < 0.5 {
            return 2.0 * t * t
        } else {
            var temp = 1.0 - t
            return 1.0 - 2.0 * temp * temp
        }
    }
    
    func EaseIn(t float) float {
        return t * t
    }
    
    func EaseOut(t float) float {
        return 1.0 - (1.0 - t) * (1.0 - t)
    }
    
    // 通用Tween函数
    async func TweenFloat(from float, to float, duration float, easeType string, out var result float) {
        var frameTime = 16  // 60FPS
        var totalTime = duration * 1000
        var totalFrames = totalTime / frameTime
        
        for frame = 0, totalFrames, 1 {
            var t = frame / totalFrames
            var easedT = t
            
            if easeType == "EaseIn" {
                easedT = EaseIn(t)
            } else if easeType == "EaseOut" {
                easedT = EaseOut(t)
            } else if easeType == "EaseInOut" {
                easedT = EaseInOut(t)
            }
            
            result = from + (to - from) * easedT
            WaitForMillisecond(frameTime)
        }
        
        result = to  // 确保最终值准确
    }
    
    // Vector3插值
    async func TweenVector3(target entity<LevelObject>, from Vector3, to Vector3, duration float, easeType string) {
        var frameTime = 16
        var totalTime = duration * 1000
        var totalFrames = totalTime / frameTime
        
        for frame = 0, totalFrames, 1 {
            var t = frame / totalFrames
            var easedT = EaseInOut(t)  // 默认使用EaseInOut
            
            var currentPos = LerpVector3(from, to, easedT)
            target<Transform>.Position = currentPos
            WaitForMillisecond(frameTime)
        }
        
        target<Transform>.Position = to
    }
}
```

---

## 最佳实践

### 1. 代码组织

#### 文件结构建议
```
Assets/
├── Scripts/
│   ├── Core/
│   │   ├── GameManager.fcg
│   │   └── EventManager.fcg
│   ├── Player/
│   │   ├── PlayerController.fcg
│   │   └── PlayerInventory.fcg
│   ├── UI/
│   │   ├── MainMenu.fcg
│   │   └── HUD.fcg
│   └── Utils/
│       ├── MathUtils.fcg
│       └── TweenUtils.fcg
├── Libraries/
│   ├── GameComponents.fcc
│   ├── GameEvents.fcc
│   └── GameEnums.fcc
└── Data/
    └── GameConfiguration.csv
```

#### 命名约定
```fc
// 组件名称：PascalCase
component PlayerController { }
component HealthSystem { }

// 函数名称：PascalCase
func CalculateDamage() { }
func GetPlayerCount() { }

// 变量名称：camelCase
var playerHealth int
var maxJumpHeight float

// 常量：UPPER_CASE
var MAX_PLAYERS int = 100
var DEFAULT_SPEED float = 5.0

// 事件名称：On + PascalCase
event OnPlayerDeath() { }
event OnGameStart() { }
```

### 2. 性能优化

#### 避免频繁内存分配
```fc
// ❌ 不好：每帧创建新列表
event OnUpdate() {
    var nearbyObjects = List<entity<LevelObject>>{}
    // 处理逻辑
}

// ✅ 好：复用列表
graph ObjectManager {
    NearbyObjectsCache List<entity<LevelObject>> = List<entity<LevelObject>>{}
    
    event OnUpdate() {
        NearbyObjectsCache.Clear()
        // 重复使用同一个列表
    }
}
```

#### 合理使用异步
```fc
// ❌ 不好：阻塞式操作
func SpawnMultipleEnemies() {
    for i = 0, 100, 1 {
        CreateEnemy()
        WaitForMillisecond(100)  // 阻塞10秒
    }
}

// ✅ 好：分批异步处理
async func SpawnMultipleEnemiesAsync() {
    var batchSize = 5
    for batch = 0, 20, 1 {
        for i = 0, batchSize, 1 {
            CreateEnemy()
        }
        WaitForMillisecond(50)  // 每批间隔
    }
}
```

### 3. 错误处理

```fc
graph SafePlayerManager {
    func GetPlayerSafely(index int) entity<Player> {
        var allPlayers = GetAllPlayers()
        
        if index < 0 || index >= allPlayers.Count {
            LogWarning("无效的玩家索引: " + index)
            return null
        }
        
        return allPlayers[index]
    }
    
    func TeleportPlayerSafely(player entity<Player>, position Vector3) {
        if player == null {
            LogError("尝试传送空玩家引用")
            return
        }
        
        if player<Player>.State == PlayerStateType.Dead {
            LogWarning("无法传送死亡玩家")
            return
        }
        
        TeleportPlayer(player, position)
        LogInfo("玩家传送成功: " + player<Entity>.Name)
    }
}
```

### 4. 调试支持

```fc
graph DebugManager {
    DebugMode bool = true
    
    func DebugLog(message string) {
        if DebugMode {
            LogInfo("[DEBUG] " + message)
        }
    }
    
    func DebugDrawLine(from Vector3, to Vector3, color Vector3) {
        if DebugMode {
            // 绘制调试线条（如果支持）
        }
    }
    
    event OnKeyPressed(key string) {
        if DebugMode {
            if key == "F1" {
                ShowDebugInfo()
            } else if key == "F2" {
                TeleportToNextCheckpoint()
            }
        }
    }
}
```

---

## 调试指南

### 1. 日志调试

```fc
graph DebuggingExample {
    func ProcessPlayerAction(player entity<Player>, action string) {
        LogInfo("开始处理玩家动作: " + player<Entity>.Name + " -> " + action)
        
        var startTime = GetCurrentTimestamp()
        
        if action == "jump" {
            HandleJump(player)
        } else if action == "shoot" {
            HandleShoot(player)
        } else {
            LogWarning("未知动作: " + action)
            return
        }
        
        var endTime = GetCurrentTimestamp()
        LogInfo("动作处理完成，耗时: " + (endTime - startTime) + "ms")
    }
}
```

### 2. 断言和验证

```fc
graph ValidationHelper {
    func AssertNotNull(obj object, message string) {
        if obj == null {
            LogError("断言失败: " + message)
            // 可以选择停止执行或其他处理
        }
    }
    
    func ValidatePlayerState(player entity<Player>) bool {
        if player == null {
            LogError("玩家引用为空")
            return false
        }
        
        if player<Player>.Health < 0 {
            LogError("玩家血量异常: " + player<Player>.Health)
            return false
        }
        
        return true
    }
}
```

### 3. 性能监控

```fc
graph PerformanceMonitor {
    FrameCount int = 0
    LastSecondTime int64 = 0
    FPS float = 0.0
    
    event OnUpdate() {
        FrameCount = FrameCount + 1
        var currentTime = GetCurrentTimestamp()
        
        if currentTime - LastSecondTime >= 1000 {
            FPS = FrameCount / ((currentTime - LastSecondTime) / 1000.0)
            LogInfo("当前FPS: " + FPS)
            
            FrameCount = 0
            LastSecondTime = currentTime
        }
    }
}
```

---

## 常见问题

### Q1: 如何在不同平台间共享数据？

**A:** 使用全局变量或数据存储API：

```fc
// 服务端脚本
[platform_server]
graph ServerData {
    GlobalPlayerCount int = 0
    
    event OnPlayerJoin(player entity<Player>) {
        GlobalPlayerCount = GlobalPlayerCount + 1
        // 同步到客户端
        SyncDataToClient("playerCount", GlobalPlayerCount)
    }
}

// 客户端脚本
[platform_client]
graph ClientUI {
    event OnDataReceived(key string, value object) {
        if key == "playerCount" {
            UpdatePlayerCountUI(value as int)
        }
    }
}
```

### Q2: 如何处理大量实体的性能问题？

**A:** 使用对象池和LOD系统：

```fc
graph EntityManager {
    EntityPool Map<string, List<entity<LevelObject>>> = Map<string, List<entity<LevelObject>>>{}
    MaxDistance float = 100.0
    
    func GetPooledEntity(type string) entity<LevelObject> {
        if !EntityPool.ContainsKey(type) {
            EntityPool[type] = List<entity<LevelObject>>{}
        }
        
        var pool = EntityPool[type]
        if pool.Count > 0 {
            var entity = pool[0]
            pool.RemoveAt(0)
            SetObjectActive(entity, true)
            return entity
        }
        
        return CreateLevelObject(type, Vector3{0, 0, 0})
    }
    
    func UpdateEntityLOD() {
        var playerPos = GetLocalPlayer()<Transform>.Position
        var allEntities = FindLevelObjectsWithTag("Managed")
        
        for i = 0, allEntities.Count, 1 {
            var entity = allEntities[i]
            var distance = Vector3Distance(entity<Transform>.Position, playerPos)
            
            if distance > MaxDistance {
                SetObjectActive(entity, false)
            }
        }
    }
}
```

### Q3: 如何实现复杂的UI交互？

**A:** 使用事件驱动的UI系统：

```fc
graph UIManager {
    CurrentMenu string = "MainMenu"
    MenuStack List<string> = List<string>{}
    
    func ShowMenu(menuName string) {
        if CurrentMenu != "" {
            MenuStack.Add(CurrentMenu)
            HideMenu(CurrentMenu)
        }
        
        CurrentMenu = menuName
        DisplayMenu(menuName)
    }
    
    func GoBack() {
        if MenuStack.Count > 0 {
            var previousMenu = MenuStack[MenuStack.Count - 1]
            MenuStack.RemoveAt(MenuStack.Count - 1)
            
            HideMenu(CurrentMenu)
            CurrentMenu = previousMenu
            DisplayMenu(previousMenu)
        }
    }
    
    event OnMenuButtonTapped(player entity<Player>, buttonName string) {
        if buttonName == "Settings" {
            ShowMenu("SettingsMenu")
        } else if buttonName == "Back" {
            GoBack()
        }
    }
}
```

### Q4: 如何处理网络同步？

**A:** 使用事件系统进行状态同步：

```fc
// 服务端权威数据
[platform_server]
graph NetworkManager {
    PlayerPositions Map<entity<Player>, Vector3> = Map<entity<Player>, Vector3>{}
    
    event OnPlayerMove(player entity<Player>, newPosition Vector3) {
        // 验证移动合法性
        if ValidateMovement(player, newPosition) {
            PlayerPositions[player] = newPosition
            BroadcastPlayerPosition(player, newPosition)
        }
    }
    
    func BroadcastPlayerPosition(player entity<Player>, position Vector3) {
        // 广播给所有客户端
        var allPlayers = GetAllPlayers()
        for i = 0, allPlayers.Count, 1 {
            if allPlayers[i] != player {
                SendToClient(allPlayers[i], "playerPosition", player, position)
            }
        }
    }
}

// 客户端接收同步
[platform_client]
graph ClientSync {
    event OnNetworkMessage(messageType string, data object) {
        if messageType == "playerPosition" {
            var playerData = data as PlayerPositionData
            UpdatePlayerPosition(playerData.Player, playerData.Position)
        }
    }
}
```

---

## 🔗 相关资源

- **官方文档**: https://ffcraftland.garena.com/en/docs/api

---

*本文档基于 Free Fire Craftland Studio 官方文档和内置库源码分析生成，包含完整的语法参考、API文档和最佳实践指南。*

`````

### Source: `.github/instructions/fc.instructions.md`

`````text
---
description: FC 语言语法支持与开发参考，用于辅助 LLM 理解 .fcg 与 .fcc 文件中的脚本结构，提升补全、提示、解释、纠错等能力。
globs: *.fcc,*.fcg
applyTo: "**/*. {fcc,fcg}"
alwaysApply: true
---
# LLM 任务目标

## 角色定位

你是一位专业的 **FC（Free Fire Code Language）脚本编程助手**，专门为 Free Fire Craftland Studio 的 UGC 游戏开发提供智能编程支持。

你深度理解：
- FC语言的面向数据设计理念和实体-组件架构
- `.fcc` 库定义文件和 `.fcg` 脚本逻辑文件的区别和用途
- Free Fire UGC游戏开发的特殊需求和约束
- 跨平台（客户端/服务端）开发的注意事项

## 核心能力

### 编程辅助能力
- **智能代码补全** - 提供准确的语法、API、组件、事件补全
- **类型推断** - 理解FC的强类型系统，提供精确的类型提示
- **语法检查** - 识别并修复语法错误、类型不匹配等问题
- **API建议** - 推荐最适合的内置API和最佳调用方式

### 代码质量提升
- **最佳实践指导** - 基于FC语言特性提供架构和编码建议
- **性能优化建议** - 针对游戏开发场景的性能优化策略
- **错误诊断** - 快速定位并解释错误原因，提供修复方案
- **代码重构** - 改善代码结构、可读性和维护性

### 开发效率提升
- **模式识别** - 识别常见的编程模式并提供模板
- **快速原型** - 为常见功能提供可用的代码框架
- **调试支持** - 提供调试策略和问题排查指导
- **文档整合** - 结合官方文档提供最新、准确的信息

## 工作准则

### 信息来源优先级
1. **优先参考** `@fc-complete-reference.mdc` - 获取完整的API文档和语法参考
2. **学习借鉴** `@fc-example.mdc` - 参考实际的代码示例和编程风格
3. **在线查询** 当遇到不确定的内容时，查询 [FFCraftland 官方文档](https://ffcraftland.garena.com/en/docs/)
4. **项目内置库** 利用 `Temp/UGCLanguage/builtin/` 中的40+个内置库文件

### 代码建议原则
- **可立即运行** - 提供的代码必须是完整、可用的
- **遵循规范** - 使用标准的FC语言语法和命名约定
- **性能优先** - 考虑游戏开发的性能要求
- **平台兼容** - 明确区分客户端/服务端代码的使用场景

### 交互方式
- **主动询问** - 当需求不明确时，主动询问用户的具体需求
- **提供选择** - 给出多种实现方案供用户选择
- **解释原理** - 不仅提供代码，还解释为什么这样写
- **渐进式帮助** - 从简单示例开始，逐步深入复杂实现

### 特殊注意事项
- **文件类型区分** - 明确 `.fcc` 文件（库定义）和 `.fcg` 文件（脚本逻辑）的不同用途
- **平台标注** - 为代码明确标注 `[platform_client]` 或 `[platform_server]`
- **异步编程** - 正确使用 `async`、`await`、`start` 等异步编程关键字
- **实体组件系统** - 正确使用 `entity<ComponentType>` 和 `thisEntity<ComponentType>` 语法
- **资源引用** - 准确使用各种资源ID类型（AssetID、LevelObjectID等）
- 对基本类型敏感，注意不同类型之间的计算与转换

### 错误处理策略
- **语法错误** - 立即指出并提供正确的语法
- **API使用错误** - 参考最新文档纠正API调用
- **类型错误** - 提供准确的类型转换建议
- **逻辑错误** - 分析代码逻辑并提供改进建议

### 学习和更新
- **持续学习** - 从用户的代码中学习项目特定的模式和需求
- **文档同步** - 当发现文档过时时，提醒查询最新的官方文档
- **最佳实践更新** - 根据社区和官方的最新实践更新建议

---

## 🔧 快速开始指南

当用户需要帮助时，你应该：

1. **理解需求** - 分析用户想要实现的功能
2. **确定文件类型** - 判断应该在 `.fcc` 还是 `.fcg` 文件中实现
3. **选择合适的API** - 从内置库中选择最适合的组件和函数
4. **提供完整示例** - 给出可运行的完整代码
5. **解释关键点** - 说明重要的设计决策和注意事项
6. **建议优化** - 提供性能和维护性方面的改进建议

记住：你的目标是让用户能够高效、正确地编写FC脚本，创造出优秀的UGC游戏内容！

---

*参考资源：*
- *完整API文档*：`@fc-complete-reference.mdc`
- *代码示例库*：`@fc-example.mdc`  
- *官方文档*：https://ffcraftland.garena.com/en/docs/
- *内置库路径*：`./Temp/UGCLanguage/builtin/`
编辑器库的位置在`$FCC_TEMP_PATH/EditorGenLib.fcc`，编辑器库中定义了编辑器动态生成的枚举、组件、事件、api等。

### 用户库

当前工程Assets目录下的所有fcc文件都是用户定义库，用户库中可以定义组件、枚举、事件。
`````

### Source: `.github/instructions/generate-widget.instructions.md`

`````text
---
alwaysApply: true
description: Inspector 添加新组件智能提示
globs: *.vue,*.ts
applyTo: "**/Inspector/widget/**/*.{vue,ts},**/Inspector.ts"
---

# Overview

# Inspector Widget 组件生成知识库

## 简介

本知识库用于指导AI和开发者自动生成Inspector Widget组件。所有新的组件添加流程都遵循相同的模式。

## 目录结构

```
docs/knowledge_base/
├── README.md                          # 本文件（包含所有生成规范）
├── generate-widget.js                 # 组件生成脚本（可选工具）
└── templates/                         # 代码模板目录
    ├── widget_vue_template.vue        # Vue组件模板
    └── widget_interface_template.ts   # TypeScript接口模板
```

## 组件结构

每个Inspector Widget组件由以下部分组成：

1. **Vue组件文件** (`{ComponentName}Editor.vue`)
   - 位置：`src/components/Inspector/widget/{ComponentName}/{ComponentName}Editor.vue`
   - 实现组件的UI和交互逻辑

2. **接口定义文件** (`interface.ts`)
   - 位置：`src/components/Inspector/widget/{ComponentName}/interface.ts`
   - 定义组件的TypeScript类型和接口

3. **注册到系统**
   - 在 `src/ts/common/property/Inspector.ts` 的 `CompName` 枚举中添加组件名
   - 在 `src/components/Inspector/widget/index.ts` 中导入和导出类型

## 生成步骤（AI和开发者通用）

### 步骤1: 理解需求

提取以下信息：
- **组件名称**（ComponentName）：必须是PascalCase格式，如 `MyWidget`
- **值类型**（ValueType）：如 `string`、`number`、`boolean`、`Array<string>` 等
- **组件功能**：了解组件的作用，以便实现正确的UI

### 步骤2: 创建组件目录和文件

**目录结构：**
```
src/components/Inspector/widget/{ComponentName}/
├── {ComponentName}Editor.vue
└── interface.ts
```

**文件1: {ComponentName}Editor.vue**
- 基于模板：`docs/knowledge_base/templates/widget_vue_template.vue`
- 替换变量：
  - `{{ComponentName}}` → 实际组件名（PascalCase）
  - `{{componentNameLower}}` → 组件名首字母小写（camelCase）
  - `{{ValueType}}` → 值类型

**文件2: interface.ts**
- 基于模板：`docs/knowledge_base/templates/widget_interface_template.ts`
- 替换相同的变量

### 步骤3: 更新注册文件

**文件3: Inspector.ts**
- 位置：`src/ts/common/property/Inspector.ts`
- 操作：在 `CompName` 枚举中添加新值
- 格式：`{ComponentName} = '{ComponentName}Editor',`

**文件4: widget/index.ts**
- 位置：`src/components/Inspector/widget/index.ts`
- 操作：
  1. 在文件顶部添加导入：`import type { {ComponentName} } from './{ComponentName}/interface';`
  2. 在 `Widget` 类型联合中添加：`| {ComponentName}`

### 步骤4: 实现组件逻辑

根据组件功能，在生成的Vue文件中实现：
- UI组件（使用项目中的组件库）
- 事件处理
- 数据绑定

## 标准组件模板

### Vue组件模板结构

参考 `templates/widget_vue_template.vue`，基本结构如下：

```vue
<template>
    <div class="inspector-property-{componentNameLower}">
        <!-- 根据组件功能实现UI -->
    </div>
</template>

<script lang="ts">
import InspectorItemChangeCommand from '@/ts/unredo/commands/InspectorItemChangeCommand';
import { Vue, Component, Prop, Emit } from 'vue-property-decorator';
import { I{ComponentName} } from './interface';
import { IWidgetProps } from '@/components/Inspector/widget/IWidgetProps';
import { ECustomBG } from '@/ts/common/property/Inspector';

@Component({
    name: '{ComponentName}Editor',
})
export default class {ComponentName}Editor extends Vue implements I{ComponentName}, IWidgetProps {
    @Prop() readonly value: {ValueType};
    @Prop({ default: (): boolean => false }) readonly disabled: boolean;
    @Prop() customBG: ECustomBG;

    @Emit('notify')
    notify(val: {ValueType}) {
        return { path: '', val, command: InspectorItemChangeCommand.Create() };
    }
}
</script>

<style lang="scss" scoped>
@import '@/styles/common.scss';
</style>
```

### Interface文件模板结构

参考 `templates/widget_interface_template.ts`，基本结构如下：

```typescript
import { CompName, ECustomBG } from '@/ts/common/property/Inspector';
import { IEditor, Component, Input, Output } from '../index';

export interface {ComponentName}Input extends Input<{ValueType}> {
    disabled?: boolean;
    customBG?: ECustomBG;
    // 根据组件需求添加其他自定义属性
}

export interface {ComponentName}Output extends Output {
    
}

export type I{ComponentName} = IEditor<{ComponentName}Input, {ComponentName}Output>;

export type {ComponentName} = Component<CompName.{ComponentName}, Omit<{ComponentName}Input, 'value'>>;

export const {ComponentName}Comparer = (val1: {ValueType}, val2: {ValueType}) => {
    if(val1 === undefined || val2 === undefined) {
        return '—';
    } else {
        return val1 === val2 ? val1 : '—';
    }
}
```

## 常见组件类型参考

### 字符串输入组件
- 值类型：`string`
- UI：使用 `<Input>` 组件
- 参考：`src/components/Inspector/widget/Input/InputEditor.vue`

### 数字输入组件
- 值类型：`number`
- UI：使用 `<InputNumber>` 组件
- 参考：`src/components/Inspector/widget/InputNumber/InputNumberEditor.vue`

### 布尔值组件
- 值类型：`boolean`
- UI：使用 `<checkbox>` 组件
- 参考：`src/components/Inspector/widget/Checkbox/CheckboxEditor.vue`

### 下拉选择组件
- 值类型：`string | number`
- UI：使用 `<Select>` 或自定义下拉组件
- 参考：`src/components/Inspector/widget/DropDown/DropDownEditor.vue`

### 列表组件
- 值类型：`Array<T>`
- UI：使用列表编辑器
- 参考：`src/components/Inspector/widget/List/ListEditor.vue`

## 命名规范

1. **组件名**：使用PascalCase，如 `MyComponent`
2. **文件名**：组件文件夹和文件使用PascalCase
3. **接口名**：使用 `I{ComponentName}` 格式
4. **类型名**：使用 `{ComponentName}Input`、`{ComponentName}Output` 格式

## 注意事项

1. **必须实现的接口**：
   - `IWidgetProps`：所有组件必须实现
   - `I{ComponentName}`：组件特定的接口

2. **必须实现的方法**：
   - `notify(val: ValueType)`：用于通知值变化
   - 返回格式：`{ path: '', val, command: InspectorItemChangeCommand.Create() }`

3. **多选支持**：
   - 实现 `{ComponentName}Comparer` 函数
   - 用于多选模式下比较值

4. **样式**：
   - 使用项目中的SCSS变量和mixins
   - 导入 `@/styles/common.scss`

5. **其他要求**：
   - 支持 `disabled` 和 `customBG` 属性
   - 使用 `InspectorItemChangeCommand.Create()` 创建命令对象

## 完整示例：生成 "MyWidget" 组件

假设要创建一个新的widget组件 "MyWidget"，用于编辑字符串值：

### 1. 创建目录
```
src/components/Inspector/widget/MyWidget/
```

### 2. 生成 MyWidgetEditor.vue

```vue
<template>
    <div class="inspector-property-myWidget">
        <Input
            :value="value"
            :disabled="disabled"
            @change="notify"
        />
    </div>
</template>

<script lang="ts">
import InspectorItemChangeCommand from '@/ts/unredo/commands/InspectorItemChangeCommand';
import { Vue, Component, Prop, Emit } from 'vue-property-decorator';
import { IMyWidget } from './interface';
import { IWidgetProps } from '@/components/Inspector/widget/IWidgetProps';
import { ECustomBG } from '@/ts/common/property/Inspector';

@Component({
    name: 'MyWidgetEditor',
})
export default class MyWidgetEditor extends Vue implements IMyWidget, IWidgetProps {
    @Prop() readonly value: string;
    @Prop({ default: (): boolean => false }) readonly disabled: boolean;
    @Prop() customBG: ECustomBG;

    @Emit('notify')
    notify(val: string) {
        return { path: '', val, command: InspectorItemChangeCommand.Create() };
    }
}
</script>

<style lang="scss" scoped>
@import '@/styles/common.scss';

.inspector-property-myWidget {
    // 组件样式
}
</style>
```

### 3. 生成 interface.ts

```typescript
import { CompName, ECustomBG } from '@/ts/common/property/Inspector';
import { IEditor, Component, Input, Output } from '../index';

export interface MyWidgetInput extends Input<string> {
    disabled?: boolean;
    customBG?: ECustomBG;
}

export interface MyWidgetOutput extends Output {
    
}

export type IMyWidget = IEditor<MyWidgetInput, MyWidgetOutput>;

export type MyWidget = Component<CompName.MyWidget, Omit<MyWidgetInput, 'value'>>;

export const MyWidgetComparer = (val1: string, val2: string) => {
    if(val1 === undefined || val2 === undefined) {
        return '—';
    } else {
        return val1 === val2 ? val1 : '—';
    }
}
```

### 4. 更新 Inspector.ts

在 `CompName` 枚举中添加：
```typescript
MyWidget = 'MyWidgetEditor',
```

### 5. 更新 widget/index.ts

添加导入：
```typescript
import type { MyWidget } from './MyWidget/interface';
```

在 `Widget` 类型中添加：
```typescript
export type Widget = (
    // ... 其他组件
    | MyWidget
);
```

## 验证清单

生成完成后，检查：

- [ ] 组件目录已创建
- [ ] Vue文件已生成并实现基本功能
- [ ] interface.ts文件已生成
- [ ] Inspector.ts中已添加枚举值
- [ ] widget/index.ts中已添加导入和类型导出
- [ ] 代码符合TypeScript规范
- [ ] 代码符合Vue规范
- [ ] 样式已正确导入

## 使用生成脚本（可选，仅限开发者）

知识库提供了生成脚本 `docs/knowledge_base/generate-widget.js`，可以快速生成基础文件：

```bash
node docs/knowledge_base/generate-widget.js MyWidget string
```

**注意：**
- 此脚本主要用于开发者快速生成基础文件框架
- **AI应该直接按照本知识库规范生成文件**，而不是使用脚本，以便更好地控制生成的内容和实现细节
- 脚本生成的文件需要手动完善UI逻辑和自定义属性

`````

### Source: `Tutorial (EN).md`

`````text
# 🐾 Game Project - Configuration & Development Guide

Welcome to the internal configuration guide for the **Steal A Pet Template**.
This document provides quick access to important setup files, regional map code, and development guides for adding new pets and mutations.


---


## ⚙️ Configuration

All game balance and content data are managed via Google Sheets.

| Sheet Configuration | Description | CSV | Note |
|-|-|-|-|
| Mobs | Mobs balance regarding cost, value, random weight | [`mob.csv`](./Assets/CSV/mob.csv) | Mob names & Mob rarity must be written in **ALL UPPERCASE** (including when registering assets)
| Mutations | Mutation balance regarding multiplier and random weight | [`mutation.csv`](./Assets/CSV/mutation.csv) |
| Rebirth | Rebirth balance regarding rewards and requirements for each level | [`rebirth.csv`](./Assets/CSV/rebirth.csv) |


---


## 🐳 How to Add a New Mob

1. Open [`mob.csv`](./Assets/CSV/mob.csv) to add the new mob's config
2. Import the mob's mesh into the [`Mobs`](./Assets/Meshes/Mobs/) folder and register asset with **ALL UPPERCASE** name
3. Import the mob's material into the [`MobMaterial`](./Assets/Materials/MobMaterial/) folder and register asset
4. Open [`key.csv`](./Assets/Localization/key.csv) to add the new mob's localization. The localization key must be same as the mob's name.

⚠️ **NOTE**:
- Mob IDs must always be **unique and sequentially increasing**
- Mob names must be written in **ALL UPPERCASE** (including when registering assets)
- Mob rarity values must also be written in **ALL UPPERCASE**


---


## 🧬 How to Add a New Mutation

1. Register the new mutation enum in Enum Manager - `MutationEnum` (Ctrl + E)
2. Create a new material in [`Mutations`](./Assets/Materials/Mutations) folder
3. Create a new effect in [`MutationEffects`](./Assets/Prefabs/MutationEffects/) folder
4. Register the assets using the same name as column EffectKey defined in [`mutation.csv`](./Assets/CSV/mutation.csv) file
5. Add new mutation property in `MobMutation` component in Component Manager (Ctrl + P)
6. Add new effect into [`Mob.prefab`](./Assets/Prefabs/Mob/Mob.prefab) prefab and register it in prefab's `MobMutation` component
7. Open [`key.csv`](./Assets/Localization/key.csv) to add the new mutation's localization.
8. Update `MUTATIONS_NAME` value in [`MutationConfig.fcg`](./Assets/Scripts/Configs/MutationConfig.fcg) script with added localization key.
9. Search for the keyword `WARN: Add color for new mutation` across all files to locate where you need to add the new mutation color so it matches the theme of each HUD


---


## 🔄 How to Add a New Rebirth

Open [`rebirth.csv`](./Assets/CSV/rebirth.csv) to add the new rebirth's config

`````

### Source: `Tutorial (VI).md`

`````text
# 🐾 Dự án Game - Hướng dẫn Cấu hình & Phát triển

Chào mừng bạn đến với tài liệu cấu hình nội bộ cho **Steal A Pet Template**.
Tài liệu này cung cấp truy cập nhanh đến các file thiết lập quan trọng, dữ liệu bản đồ theo khu vực, và hướng dẫn phát triển để thêm pet và mutation mới.

---

## ⚙️ Cấu hình

Tất cả dữ liệu cân bằng game và nội dung được quản lý thông qua Google Sheets.

| Cấu hình Sheet | Mô tả | CSV | Ghi chú |
|-|-|-|-|
| Mobs | Cân bằng mobs: chi phí, giá trị, tỉ lệ xuất hiện ngẫu nhiên | [`mob.csv`](./Assets/CSV/mob.csv) | Tên Mob & độ hiếm phải viết **IN HOA TOÀN BỘ** (bao gồm cả khi đăng ký asset) |
| Mutations | Cân bằng mutation: hệ số nhân và tỉ lệ xuất hiện | [`mutation.csv`](./Assets/CSV/mutation.csv) | |
| Rebirth | Cân bằng rebirth: phần thưởng và yêu cầu mỗi cấp | [`rebirth.csv`](./Assets/CSV/rebirth.csv) | |

---

## 🐳 Cách thêm Mob mới

1. Mở [`mob.csv`](./Assets/CSV/mob.csv) để thêm cấu hình mob mới
2. Import mesh của mob vào thư mục [`Mobs`](./Assets/Meshes/Mobs/) và đăng ký asset với tên **IN HOA TOÀN BỘ**
3. Import material của mob vào thư mục [`MobMaterial`](./Assets/Materials/MobMaterial/) và đăng ký asset
4. Mở [`key.csv`](./Assets/Localization/key.csv) để thêm localization cho mob. Key phải giống tên mob

⚠️ **LƯU Ý**:
- ID mob phải luôn **duy nhất và tăng dần tuần tự**
- Tên mob phải viết **IN HOA TOÀN BỘ** (bao gồm cả khi đăng ký asset)
- Giá trị độ hiếm của mob cũng phải viết **IN HOA TOÀN BỘ**

---

## 🧬 Cách thêm Mutation mới

1. Đăng ký enum mutation mới trong Enum Manager - `MutationEnum` (Ctrl + E)
2. Tạo material mới trong thư mục [`Mutations`](./Assets/Materials/Mutations)
3. Tạo effect mới trong thư mục [`MutationEffects`](./Assets/Prefabs/MutationEffects/)
4. Đăng ký asset với tên giống cột `EffectKey` trong [`mutation.csv`](./Assets/CSV/mutation.csv)
5. Thêm thuộc tính mutation mới trong component `MobMutation` tại Component Manager (Ctrl + P)
6. Thêm effect mới vào prefab [`Mob.prefab`](./Assets/Prefabs/Mob/Mob.prefab) và đăng ký trong component `MobMutation`
7. Mở [`key.csv`](./Assets/Localization/key.csv) để thêm localization cho mutation
8. Cập nhật giá trị `MUTATIONS_NAME` trong script [`MutationConfig.fcg`](./Assets/Scripts/Configs/MutationConfig.fcg) với key vừa thêm
9. Tìm kiếm từ khóa `WARN: Add color for new mutation` trong toàn bộ project để xác định nơi cần thêm màu cho mutation mới nhằm đồng bộ với giao diện HUD

---

## 🔄 Cách thêm Rebirth mới

Mở [`rebirth.csv`](./Assets/CSV/rebirth.csv) để thêm cấu hình rebirth mới

`````


