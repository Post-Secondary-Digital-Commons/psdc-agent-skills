# PSDC Agent Skills

Governed, provenance-pinned skills for agents that work on the Post-Secondary
Digital Commons (PSDC). This repository is a specification and review toolset;
it is not evidence that any PSDC runtime service exists.

## What is here

- `vendor/mattpocock/`: an unmodified, revision-pinned selection from
  [`mattpocock/skills`](https://github.com/mattpocock/skills).
- `skills/`: PSDC-native router and audit skills that add authority, evidence,
  privacy, federation, and readiness rules.
- `config/skill-registry.yaml`: machine-readable enablement, provenance, and
  phase policy.
- [`docs/governance/COMPLETE-SKILL-INVENTORY.md`](docs/governance/COMPLETE-SKILL-INVENTORY.md):
  every upstream skill at the pinned commit, including twelve deliberately not added.
- [`docs/governance/SKILL-APPLICATION-SCOPE.md`](docs/governance/SKILL-APPLICATION-SCOPE.md):
  generated repository-area map and revision-bound consumer opt-in snapshot.
- `skills/psdc-upstream-adoption/`: component-level reuse decisions and a
  lightweight implementation-delta check; records use
  `schemas/upstream-adoption-record.schema.json`.
- `docs/`: scope, threat model, adoption rules, and assessment records.
- `schemas/`: validation contracts for the registry and assessment results.

## Safety boundary

The current lifecycle is **specification**. Skills may research, model domains,
interview, prepare specifications, decompose approved specifications, and audit
evidence. They may not infer authority to deploy infrastructure, merge changes,
alter production state, or turn proposals into accepted decisions.

## Evidence ladder

Every assessment uses this ordered vocabulary:

`proposed -> documented -> contracted -> structurally_validated -> implemented -> deployed -> production_proven`

Later states require new evidence. A passing documentation or schema check does
not imply implementation, deployment, or production behavior.

## Upstream baseline

The vendored files are pinned to `mattpocock/skills` commit
`f3fc5632f401156837ee3872f14fe33ccf1024ea`. See
[`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and
[`docs/governance/UPSTREAM-MAINTENANCE.md`](docs/governance/UPSTREAM-MAINTENANCE.md).

## Start here

1. Read [`AGENTS.md`](AGENTS.md).
2. Inspect [`config/skill-registry.yaml`](config/skill-registry.yaml).
3. Use `psdc-project-assessment` for a bounded project review.
4. Validate the repository with `scripts/Test-AgentSkills.ps1`.

Consuming repositories pin this pack through `.psdc/agent-skills.yaml`.
The schema, validator, and adoption boundary are documented in
[`docs/governance/CONSUMER-MANIFEST.md`](docs/governance/CONSUMER-MANIFEST.md).
