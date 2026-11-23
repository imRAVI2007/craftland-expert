# NEW REUSABLE PROMPT — Craftland map audit

**Purpose:** Audit a Craftland scene/map against an explicit design brief and available editor evidence.

**Required input:** Map/scene asset, design brief, active map settings, expected spawn/base/entity behavior, current editor tree/schema/logs, audit scope.

**Prompt:**

> Audit the supplied Craftland map against the brief. Confirm the active scene/map and ground context before interpreting coordinates. Report only inspected entity/schema/settings evidence. Compare required versus observed structure, call out unresolved bindings/components and properties needing editor inspection, and separate static observations from runtime behavior. Do not infer game mode names from undecoded numeric values or state that collision/spawn works without testing.

**Expected output:** Scope, verified scene/map snapshot, requirement-by-requirement findings, unknowns/risks, and validation steps.

**Basis:** Newly authored from `knowledge/maps/scene-structure.md`, `knowledge/gameplay/map-settings.md`, and editor guidance. Not a recovered prompt.
