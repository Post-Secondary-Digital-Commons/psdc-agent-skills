# Agent Instructions

## Authority

The PSDC Decision Register and accepted ADRs are normative decisions. Contracts
define machine-facing behavior. Repository documents elaborate their own
subsystems. Institution overlays may specialize branding, policy bindings,
topology, contacts, and deployment choices without silently changing common
contracts. Obsidian notes and generated dashboards are navigation views only.

Read `docs/governance/AUTHORITY-AND-EVIDENCE.md` before publishing an assessment.

## Agent skills

### Issue tracker

Work is tracked in GitHub Issues. A generated recommendation is not permission
to create or close an issue unless the user requests that tracker change.

### Domain docs

This is a single-context repository. Canonical terms belong in `GLOSSARY.md`;
durable, surprising, hard-to-reverse trade-offs belong in `docs/adr/`.

### Skill policy

Use `config/skill-registry.yaml` as the enablement and provenance source. Load
vendored upstream skills only through the PSDC policy described there. Preserve
upstream files unchanged; PSDC-specific behavior belongs under `skills/`.

### Evidence

Keep observed facts, documentation claims, inferences, and recommendations in
separate fields. Never promote a readiness state without evidence for that
state. Assess the commit actually inspected and record its identifier.

## Current lifecycle

The project is documentation- and contract-first. Implementation/deployment
skills are disabled until an accepted decision changes `config/skill-registry.yaml`.

