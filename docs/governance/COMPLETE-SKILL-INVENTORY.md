# Complete Matt Pocock Skill Inventory

> Status: adoption inventory, not authorization to invoke a gated skill
> Upstream: `mattpocock/skills` at `f3fc5632f401156837ee3872f14fe33ccf1024ea`
> Inspected: 2026-10-08

The pinned upstream tree has **38** `SKILL.md` entrypoints. PSDC vendors 26
unchanged: the original eight plus eighteen selected in this batch. Twelve
are intentionally not vendored. "Pack enabled" means the common registry
allows a consumer to opt in; it does **not** mean every repository's pinned
consumer manifest has been updated or that an agent has run the skill. Gated
skills are present for provenance and future review, but the consumer
validator must reject them as enabled skills.

## Engineering (20 of 20 listed)

| Skill | PSDC disposition | Reason / use |
|---|---|---|
| ask-matt | Newly vendored; gated | Router can recommend prohibited implementation or external-write flows; needs PSDC routing review. |
| code-review | Newly vendored; pack enabled | Two-axis review against standards and approved spec; no implicit merge. |
| codebase-design | Newly vendored; pack enabled | Design narrow, contract-owned module seams. |
| diagnosing-bugs | Newly vendored; gated | Activate for a repository after executable behavior and regression harness exist. |
| domain-modeling | Previously vendored; pack enabled | Keep glossary and bounded contexts consistent. |
| grill-with-docs | Previously vendored; pack enabled | Resolve open human choices without inventing acceptance. |
| implement-spec | Newly vendored; prohibited | Multi-ticket implementation and subagent orchestration need explicit task, D2 handoffs, and a reviewed policy change. |
| implement | Newly vendored; prohibited | No autonomous implementation authority from a skill; currently specification-phase policy. |
| improve-codebase-architecture | Newly vendored; pack enabled | Review implemented code for justified seam improvements. |
| pr | Newly vendored; pack enabled | Evidence, blast radius, rollback, and limitations in PR descriptions. |
| prototype | Newly vendored; pack enabled | Disposable synthetic UX/logic compatibility spikes. |
| research | Previously vendored; pack enabled | Primary-source, license and security research. |
| retro | Newly vendored; pack enabled | Improve feedback loops and agent navigation after a slice. |
| setup-matt-pocock-skills | Previously vendored; pack enabled | One-time tracker/domain setup subject to PSDC authority. |
| tdd | Newly vendored; gated | Activate only for an approved implementation slice. |
| to-spec | Previously vendored; pack enabled | Bound accepted discussion into a candidate specification. |
| to-tickets | Previously vendored; pack enabled | Decompose reviewed specs into dependency-aware tickets. |
| triage | Newly vendored; gated | Issue mutation requires explicit authority and PSDC issue-state mapping. |
| wayfinder | Previously vendored; pack enabled | Map multi-stage decision frontiers. |
| wizard | **Not added** | Bash workflow handles credentials, `.env`, and GitHub secrets; needs a separate Windows/institution security design before adoption. |

## Productivity (7 of 7 listed)

| Skill | PSDC disposition | Reason / use |
|---|---|---|
| grill-me | Newly vendored; pack enabled | Explore ideas conversationally without mutating governed documents. |
| grilling | Newly vendored; pack enabled | Reusable decision interview mechanics. |
| handoff | Newly vendored; pack enabled | Preserve exact revisions, evidence and remaining work between maintainers. |
| teach | Newly vendored; pack enabled | Club-member learning and onboarding; not normative authority. |
| to-questionnaire | Newly vendored; pack enabled | Obtain institution, legal and operator decisions from their owners. |
| wait-what | Newly vendored; pack enabled | Repair a confusing explanation using the project glossary. |
| writing-for-agents | Previously vendored; pack enabled | Concise routed instructions for agents. |

## In-progress (0 of 7 added)

| Skill | Reason not added |
|---|---|
| chief-of-staff | Experimental long-running subagent orchestration; no need in the common skill pack yet. |
| claude-handoff | Claude-specific background-agent handoff, not a portable PSDC workflow. |
| loop-me | Experimental workflow interview; overlaps governed specification skills. |
| setup-ts-deep-modules | Experimental TypeScript-specific setup; assess only in a TypeScript client repo. |
| writing-beats | Editorial composition workflow, not a component/implementation control. |
| writing-fragments | Editorial composition workflow, not a component/implementation control. |
| writing-shape | Editorial composition workflow, not a component/implementation control. |

## Miscellaneous (0 of 4 added)

| Skill | Reason not added |
|---|---|
| git-guardrails-claude-code | Claude Code hook configuration; evaluate as an agent-specific overlay, not shared platform policy. |
| migrate-to-shoehorn | Depends on a specific TypeScript test-helper migration PSDC has not chosen. |
| scaffold-exercises | Assumes AI Hero course tooling; club labs require a PSDC-native teaching scaffold instead. |
| setup-pre-commit | Assumes Husky/lint-staged; not appropriate as one rule for Go, Python, and TypeScript repos. |

## PSDC-native skills

These are **not** part of the 38 upstream count:

| Skill | State | Purpose |
|---|---|---|
| psdc-project-assessment | Existing; enabled | Evidence-scored architecture and readiness review. |
| psdc-evidence-audit | Existing; enabled | Claim-to-artifact verification. |
| psdc-upstream-adoption | New; enabled | Reuse-versus-build review for every component and implementation delta. |

Before consumer manifests change, review the requested skills against the
owning repository's lifecycle and authority. Upstream files remain unchanged;
PSDC constraints live in the registry and native skills. The hash manifest
proves byte identity, not that a skill's behavior is safe for every task.
