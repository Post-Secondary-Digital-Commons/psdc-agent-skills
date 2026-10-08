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

Each example below illustrates a possible PSDC task, **not** a claim that the
skill was invoked, its output was accepted, or the underlying platform feature
exists. For a gated or prohibited skill, the example describes what it could
do *after* its activation gate is resolved. For a skill not added, the example
is hypothetical and does not recommend importing it. The registry, consumer
manifest, user request, and repository authority rules still govern use.

## Engineering (20 of 20 listed)

| Skill | PSDC disposition | What it does | PSDC example |
|---|---|---|---|
| ask-matt | Newly vendored; gated | Routes a request to a suitable skill or workflow. The upstream router can suggest flows PSDC has not authorized. | Given “I have a compute design but no implementation ticket,” it could suggest `to-spec` or `to-tickets` after a PSDC-aware router prevents a jump to `implement`. |
| code-review | Newly vendored; pack enabled | Reviews a bounded diff on two axes: repository standards and fidelity to its originating specification. It reports findings; it does not approve or merge by itself. | Review a proposed lease-service change against both coding rules and the lease contract, identifying a duplicate-lease path missed by schema tests. |
| codebase-design | Newly vendored; pack enabled | Designs deep modules: substantial behavior behind a narrow, testable interface at a clear ownership seam. | Define a `LeaseAuthority` interface that hides generation checks and persistence without copying the contract into each worker. |
| diagnosing-bugs | Newly vendored; gated | Uses a hypothesis-and-evidence loop to locate the first divergence behind a bug or performance regression. It needs running behavior to diagnose. | After an approved compute slice exists, reproduce a lease that expires early, compare clocks and events, then add a regression test for the actual cause. |
| domain-modeling | Previously vendored; pack enabled | Sharpens domain terms, boundaries and decisions; updates a glossary or ADR when the model changes. | Distinguish a provider *offer* from a scheduler *decision* and a signed *lease*, then propagate those terms into the compute glossary. |
| grill-with-docs | Previously vendored; pack enabled | Interviews the decision owner about a design and records resolved terminology or decisions in governed documents. | Work through who may revoke a lab-worker lease and draft the resulting glossary and ADR changes without marking a proposed answer accepted. |
| implement-spec | Newly vendored; prohibited | Coordinates implementation of a specification and its tickets. Upstream assumes an issue tracker and broader execution authority. | Once a policy change and explicit implementation task permit it, work through the approved VS-01 tickets in dependency order with contract and test evidence. |
| implement | Newly vendored; prohibited | Implements a bounded piece of work from a specification or ticket. Having the skill present grants no authority to change code. | After activation, implement an explicitly assigned lease-validation ticket rather than inferring permission from an architecture document. |
| improve-codebase-architecture | Newly vendored; pack enabled | Inspects existing code for shallow modules and proposes evidence-backed boundary improvements, with a visual report. It is not a refactor mandate. | Examine a future scheduler whose API leaks PostgreSQL queries and propose a narrower placement-decision interface. |
| pr | Newly vendored; pack enabled | Produces a reviewable pull-request description that explains the change, evidence, risks and unresolved work. | Describe a provider-schema PR with affected contracts, fixture results, compatibility impact and checks not run. |
| prototype | Newly vendored; pack enabled | Builds disposable code to answer a focused design or UX question; the result is not production evidence. | Use synthetic offers to test whether a reverse-auction explanation helps operators understand why a provider was selected. |
| research | Previously vendored; pack enabled | Investigates a question using primary sources and records source-backed findings and uncertainty. | Compare current Akash and Golem APIs, licenses and extension points before proposing which mechanics PSDC could adapt. |
| retro | Newly vendored; pack enabled | Reviews a completed work session for improvements to the agent environment and engineering feedback loop. | After a contract review, identify why fixture failures were hard to trace and propose a bounded validator-output improvement. |
| setup-matt-pocock-skills | Previously vendored; pack enabled | Sets up issue-tracker vocabulary and domain-document layout assumed by several upstream skills. It is a one-time configuration workflow. | Map upstream ticket states to PSDC GitHub labels and point domain changes to the existing glossary and ADR locations, with review before tracker writes. |
| tdd | Newly vendored; gated | Guides red–green–refactor development and test quality during an authorized implementation slice. | For an approved lease-renewal change, write a failing stale-generation test, implement the smallest fix, and rerun the suite. |
| to-spec | Previously vendored; pack enabled | Synthesizes known conversation and repository context into a specification; upstream can publish to an issue tracker, which still needs authorization. | Turn accepted workload-classification decisions into a candidate spec that cites the manifest contract and marks open policy questions. |
| to-tickets | Previously vendored; pack enabled | Breaks a plan into small, dependency-aware tracer-bullet tickets; publishing tickets is a separate authorized action. | Split a storage-placement slice into manifest validation, policy decision, provider call and failure-fixture tickets with blocking edges. |
| triage | Newly vendored; gated | Classifies issues and external PRs through a tracker state machine and prepares agent-ready briefs. It writes tracker state when authorized. | Once PSDC issue-state rules and permission are approved, classify a federation bug, verify reproduction evidence and prepare a bounded repair brief. |
| wayfinder | Previously vendored; pack enabled | Maps a large, uncertain effort as decision tickets so prerequisites are resolved before execution tickets. | Map the decisions needed before student credential portability—DID method, issuer trust, recovery and revocation—without pretending deployment is ready. |
| wizard | **Not added** | Generates an interactive Bash guide for human-only setup steps; upstream can write `.env` values and GitHub secrets. A Windows and institution-security design is needed first. | Hypothetically guide an operator through certificate-authority setup with confirmations and secret handling; do not import this workflow for PSDC as-is. |

## Productivity (7 of 7 listed)

| Skill | PSDC disposition | What it does | PSDC example |
|---|---|---|---|
| grill-me | Newly vendored; pack enabled | Invokes a decision interview without automatically writing domain documents. | Stress-test a proposed campus GPU-sharing rule through successive questions before drafting any policy. |
| grilling | Newly vendored; pack enabled | Interviews in rounds, asking the currently answerable decision questions and showing recommended answers. | Ask the club owner first who may offer lab machines, then ask about reclaim deadlines only after ownership is clear. |
| handoff | Newly vendored; pack enabled | Writes a compact session handoff for another agent, including exact state and next actions. It does not transfer authority. | Capture the inspected commit, passing fixture count, unresolved lease issue and safe next command before another maintainer takes over. |
| teach | Newly vendored; pack enabled | Builds a sustained learning path with explanations, exercises and learning records. | Teach a new club member the difference between a workload request, a placement decision and an execution receipt using synthetic examples. |
| to-questionnaire | Newly vendored; pack enabled | Turns questions only another person can answer into a questionnaire for that person. Sending it remains a separate action. | Prepare a facilities questionnaire on lab hours, power limits and network ownership for the campus operator. |
| wait-what | Newly vendored; pack enabled | Re-explains a confusing previous answer in simpler language using the project's established vocabulary. | Re-pitch “lease generation fencing” as “an old controller must not renew a newer worker's permission.” |
| writing-for-agents | Previously vendored; pack enabled | Makes agent-facing instructions concise, routed and testable instead of repeating policy everywhere. | Keep a repo's `AGENTS.md` short and link to the exact contract, validator and authority documents an agent must use. |

## In-progress (0 of 7 added)

| Skill | What it does | Hypothetical PSDC example | Why not added |
|---|---|---|---|
| chief-of-staff | Coordinates subagents around a long-running goal and adjusts the working environment. | Could coordinate a multi-week architecture review across repositories. | Experimental long-running orchestration is unnecessary in the common pack and needs explicit delegation rules. |
| claude-handoff | Launches a fresh Claude background agent using a handoff summary. | Could hand a compute-spec review to another Claude session. | Claude-specific execution is not portable common behavior. |
| loop-me | Interviews someone to specify recurring personal or organizational workflows. | Could explore a recurring club-member onboarding loop. | Experimental; overlaps governed specification skills and is not a component control. |
| setup-ts-deep-modules | Installs dependency-cruiser rules to enforce TypeScript package entry-point boundaries. | Could constrain imports in a future TypeScript web client. | Experimental and TypeScript-specific; evaluate in the owning client repo. |
| writing-beats | Shapes fixed raw material into an article's sequence of explanatory beats. | Could turn approved architecture notes into a public explainer. | Editorial composition is outside the shared component-engineering pack. |
| writing-fragments | Interviews to collect raw writing fragments without imposing an article structure. | Could gather student stories for an outreach article. | Editorial exploration is outside the shared component-engineering pack. |
| writing-shape | Restructures an existing pile of raw material into an article, paragraph by paragraph. | Could shape a club launch narrative from approved source notes. | Editorial composition is outside the shared component-engineering pack. |

## Miscellaneous (0 of 4 added)

| Skill | What it does | Hypothetical PSDC example | Why not added |
|---|---|---|---|
| git-guardrails-claude-code | Adds Claude Code hooks that block specified risky Git commands. | Could block a Claude agent from running `git push` in one checkout. | Claude-specific hooks belong in an agent overlay, not common platform policy. |
| migrate-to-shoehorn | Rewrites TypeScript tests that use `as` assertions to use the Shoehorn test helper. | Could migrate tests in a web client if that dependency is adopted. | PSDC has not selected that TypeScript helper or migration. |
| scaffold-exercises | Creates exercise directories that pass AI Hero course-tooling checks. | Could scaffold a lesson on lease fencing if PSDC used that curriculum tool. | Club labs need their own teaching structure; upstream assumes AI Hero tooling. |
| setup-pre-commit | Installs Husky and lint-staged with formatting, type checks and tests. | Could add commit-time checks to a TypeScript client. | Not one universal rule for Go, Python and TypeScript repositories. |

## PSDC-native skills

These are **not** part of the 38 upstream count:

| Skill | State | What it does | PSDC example |
|---|---|---|---|
| psdc-project-assessment | Existing; enabled | Scores a bounded, revision-specific architecture or readiness claim against the assessment rubric. | Assess whether VS-01 is merely contracted, structurally validated, implemented or actually running, citing evidence for each state. |
| psdc-evidence-audit | Existing; enabled | Traces a claim to the cited artifact, commit, check, scope and limitations. | Challenge a dashboard's “deployed” badge when its only evidence is a passing JSON Schema test. |
| psdc-upstream-adoption | New; enabled | Records whether PSDC should adopt, adapt, patch, fork or build for a component, then checks each implementation delta against that decision. | Compare Akash-derived placement with an adapter and a custom scheduler; record the chosen seam, source revision, license, tests and maintenance owner before importing code. |

Before consumer manifests change, review the requested skills against the
owning repository's lifecycle and authority. Upstream files remain unchanged;
PSDC constraints live in the registry and native skills. The hash manifest
proves byte identity, not that a skill's behavior is safe for every task.
