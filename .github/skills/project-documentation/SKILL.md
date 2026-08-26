---
name: project-documentation
description: "Use when documenting, refreshing, reconciling, or auditing this project's architecture, development guide, conventions, decisions, roadmap, timeline, or changelog. Generates source-backed Markdown documentation with Mermaid diagrams and reports contradictions without silently changing code."
---

# Project Documentation

Generate and maintain the documentation set in `docs/` from evidence in the
repository. Treat documentation as a maintained technical artifact: accurate,
traceable, consistent, and stable across repeated runs.

## Scope

This skill covers these documentation files:

- `docs/architecture.md`
- `docs/CHANGELOG.md`
- `docs/conventions.md`
- `docs/decision.md`
- `docs/development.md`
- `docs/roadmap.md`
- `docs/timeline.md`

The repository README is the documentation index. At the end of a documentation
update, use the sibling `create-readme` skill to refresh `README.md` and link to
each maintained document.

Update documentation only unless the user explicitly requests source,
configuration, or tooling changes. Preserve authored historical content and
avoid replacing it with generated prose.

## Workflow

### 1. Inspect the repository

Read the relevant evidence before writing:

- `README.md`, `pyproject.toml`, `uv.lock`, and repository metadata
- `src/**/*.py`, `tests/**/*.py`, and package exports
- `.scripts/*`, `.vscode/*`, and `specs/*`
- all existing files under `docs/`
- recent git history and relevant commits for changelog context

Exclude `.venv/`, `__pycache__/`, `htmlcov/`, coverage files, build outputs,
lock caches, and other generated artifacts from the source inventory.

Build a compact fact table before editing. Each fact should include:

| Source | Observed fact | Confidence | Documentation target |
| --- | --- | --- | --- |
| path and symbol or config key | behavior supported by the source | observed or inferred | one or more docs |

Use `observed` for direct repository evidence. Use `inferred` only when the
inference is strong and label it in the resulting documentation. Do not turn a
template placeholder into a project fact.

### 2. Reconcile contradictions

Report contradictions with their source paths and impact before or alongside
the documentation update. Do not silently fix them. Check especially for:

- package directories that differ from build targets or project names
- duplicate TOML keys or conflicting dependency declarations
- stale names, commands, paths, task labels, or comments
- scripts that reference missing directories or modules
- order-dependent package, runner, or executable discovery
- missing CI, deployment, ownership, product, external-service, or release
  evidence

When evidence is missing, write `TBD` or an explicit open question. Never
invent product commitments, dates, owners, deployment topology, external
services, or release history.

### 3. Generate the documentation

Keep headings and terminology consistent across all files. Link to real
repository paths and symbols where useful.

#### `architecture.md`

Document only an evidenced purpose, then describe package boundaries, entry
points, module responsibilities, configuration, logging, data flow, build and
packaging behavior, dependencies, and known gaps. Include both diagrams:

```mermaid
flowchart TD
```

for the components and:

```mermaid
sequenceDiagram
```

for the runtime path from runner to package entry point, configuration and
logging, and output. Use stable names based on actual files and add a short
evidence note beneath each diagram.

#### `development.md`

Document prerequisites, environment setup, environment variables, run,
format, lint, type-check, test, coverage, build, and cleanup commands. Include
available VS Code task and debugger labels, platform caveats, and
troubleshooting supported by scripts. Add a Mermaid diagram using:

```mermaid
flowchart TD
```

to show setup, validation, testing, and build task dependencies.

#### `conventions.md`

Record actual source layout, Python version, naming, typing, formatting,
linting, testing, configuration, logging, branch, and commit conventions.
Distinguish enforced rules from recommendations and list unresolved policy
questions separately.

#### `decision.md`

Write one ADR per meaningful accepted, proposed, rejected, or deprecated
decision. Each ADR should include date, status, context, decision,
consequences, alternatives, and evidence. Use a Mermaid `flowchart` when an
ADR compares competing alternatives. Record unresolved package, build, or
tooling conflicts as open decisions instead of choosing for the user.

#### `CHANGELOG.md`

Follow Keep a Changelog and Semantic Versioning structure if already adopted.
Derive entries from git history and source evidence available in the
repository. Do not fabricate versions, dates, releases, or issue references.
Avoid duplicate entries on repeated runs and preserve existing release history.

#### `roadmap.md`

Include only goals supplied by the user or supported by repository planning
evidence. Keep a clearly labeled `TBD` or backlog section when product goals
are unknown. Do not convert generic template bullets into commitments.

#### `timeline.md`

Separate evidenced historical events from proposed phases. Use a Mermaid
`gantt` diagram only when real dates or durations are available. Without them,
use a textual TBD schedule and state what information is missing.

### 4. Make updates idempotent

Prefer stable generated sections and deterministic ordering. Preserve user-
authored facts, ADR history, changelog entries, and intentional decisions.
Do not duplicate headings, entries, diagrams, links, or warnings. A second run
with no source changes should produce no documentation diff.

### 5. Orchestrate the README

After all files under `docs/` have been updated and validated, invoke the
`create-readme` skill. Provide it with the final documentation facts and ask it
to update `README.md` so it:

- reflects the current project purpose and verified setup commands
- links to `architecture.md`, `CHANGELOG.md`, `conventions.md`,
   `decision.md`, `development.md`, `roadmap.md`, and `timeline.md`
- keeps the documentation links as an index rather than duplicating their full
   contents
- follows the `create-readme` skill's concise GFM structure and avoids adding
   standalone `CHANGELOG`, `CONTRIBUTING`, or `LICENSE` sections

The README step is last because its links and summary must reflect the final
state of every other documentation file. Validate that every linked path exists
after the README update.

## Validation

Before reporting completion:

1. Cross-check every documented path, symbol, command, task label, dependency,
   environment variable, and package name against the repository.
2. Parse `pyproject.toml` and compare discovered `src` packages with declared
   build targets. Flag duplicate keys and missing targets.
3. Scan for unresolved template markers such as `Provide`, `Component A`,
   `Date Range`, `Milestone`, `Feature A`, and `[Decision Title]`. Classify an
   intentional `TBD` as acceptable and everything else as a documentation
   defect.
4. Validate internal Markdown links and confirm cited files exist.
5. Check Mermaid fences, supported diagram types, balanced code fences, stable
   node names, and evidence notes. Render or parse diagrams when a validator
   is available.
6. Run available focused checks and report exact results. Typical checks are:

   ```bash
   uv run pytest
   uv run ruff check .
   uv run ruff format --check .
   uv run pyrefly check
   ```

   Run application or executable checks only when safe and supported by the
   current platform. Never claim a command ran when it was only recommended.

7. Re-run the source comparison after writing and report any remaining
   contradictions, stale references, or unsupported claims.

## Completion report

Summarize the documentation files changed, the evidence used, Mermaid diagrams
added or updated, validation commands and results, and unresolved `TBD` items
or contradictions. If documentation cannot be made reliable without product
input, stop at a proposed diff or clearly mark the missing decisions rather
than guessing.