# Skill Application Scope

> Generated from `config/application-scope.yaml`, `config/skill-registry.yaml`,
> the workspace catalog, and each repository's `origin/main` consumer manifest.
> This is a revision-bound structural snapshot, not evidence that an agent used a skill.

## Read this map

A profile names primary methods for a repository's work, **not** automatic enablement.
The complete map below adds cross-cutting and gated methods for every skill.
The consumer manifest lists declared opt-ins at its own pinned pack revision.
A task triggers only the applicable enabled method, subject to its gate, repository
instructions, and explicit user authority. The [registry](../../config/skill-registry.yaml)
sets current pack-wide modes; the [inventory](COMPLETE-SKILL-INVENTORY.md)
explains every skill. An older consumer pin is **not** validated against newer rules.

Workspace catalog revision: `e0e2535c3a03e31c9a85694ea8a1642c26f23de4`. Pack revision
inspected when generated: `318d204aedf183b63d5b0c1bcf5972ae981d964a`. Source manifests and commits
are recorded in `config/application-scope-snapshot.json`.
**22 of 22** consumer pins differ from that pack revision;
this map does not silently upgrade them.

## Repository and area profiles

| Profile / repositories | Areas and trigger | Primary methods | Evidence boundary |
|---|---|---|---|
| **workspace**: `psdc-workspace` | Repository catalog, Platform Home, generated views, Obsidian navigation, documentation links, and evidence projections. Trigger: A workspace source, generated map, vault navigation note, or cross-repository health claim changes. | `writing-for-agents`, `research`, `code-review`, `psdc-project-assessment`, `psdc-evidence-audit`, `psdc-upstream-adoption`, `psdc-engineering-quality`, `psdc-workspace-health` | A generated view or valid link does not prove the underlying service exists or a skill ran. |
| **architecture**: `psdc-architecture`, `algonquin-architecture` | Decisions, contracts, fixtures, roadmaps, and institution policy overlays. Trigger: Changes to shared terms, interfaces, decisions, or readiness claims. | `domain-modeling`, `research`, `to-spec`, `to-tickets`, `wayfinder`, `code-review`, `psdc-project-assessment`, `psdc-evidence-audit`, `psdc-upstream-adoption`, `psdc-engineering-quality` | A document or contract check does not establish service behavior or institution approval. |
| **cloud**: `psdc-cloud`, `algonquin-cloud` | Identity, policy, storage, evidence, networking, and infrastructure interfaces. Trigger: A shared service boundary, dependency, or deployment profile changes. | `research`, `codebase-design`, `code-review`, `prototype`, `psdc-upstream-adoption`, `psdc-evidence-audit`, `psdc-engineering-quality` | A local service test does not establish custody, disaster recovery, or production admission. |
| **ai**: `psdc-ai`, `algonquin-ai` | Session control, gateway, model routing, tool grants, and inference integration. Trigger: A model, tool, data-access, or session boundary changes. | `research`, `codebase-design`, `prototype`, `code-review`, `psdc-upstream-adoption`, `psdc-evidence-audit`, `psdc-engineering-quality` | A model demo does not establish safe tool authority, privacy, scale, or campus availability. |
| **compute**: `psdc-compute`, `algonquin-compute` | Providers, capabilities, workload admission, placement, leases, workers, and receipts. Trigger: A scheduler, worker, upstream mechanism, or lab-machine boundary changes. | `domain-modeling`, `research`, `codebase-design`, `prototype`, `code-review`, `psdc-upstream-adoption`, `psdc-evidence-audit`, `psdc-engineering-quality` | Synthetic and unit tests do not establish lab safety, operator consent, physical capacity, or settlement correctness. |
| **media**: `psdc-media`, `algonquin-media` | Image, video, spatial, 3D, and 4DGS processing and media custody. Trigger: A pipeline, format, model, provenance, or media-access boundary changes. | `research`, `codebase-design`, `prototype`, `code-review`, `psdc-upstream-adoption`, `psdc-evidence-audit`, `psdc-engineering-quality` | Render success does not establish provenance, rights, deletion, or cross-device performance. |
| **social**: `psdc-social`, `algonquin-social` | ActivityPub, social surfaces, moderation, federation, and spatial content policy. Trigger: A federation message, moderation, identity, or consent boundary changes. | `domain-modeling`, `research`, `to-spec`, `code-review`, `psdc-upstream-adoption`, `psdc-evidence-audit`, `psdc-engineering-quality` | Protocol parsing does not establish federation trust, consent, or moderation effectiveness. |
| **web**: `psdc-web`, `algonquin-web` | Browser client, accessibility, sessions, gateway integration, and user-facing flows. Trigger: A UI, accessibility, session, or shared API interaction changes. | `research`, `codebase-design`, `prototype`, `code-review`, `psdc-upstream-adoption`, `psdc-evidence-audit`, `psdc-engineering-quality` | A mock UI or browser build does not establish end-to-end identity or deployed usability. |
| **desktop**: `psdc-desktop`, `algonquin-desktop` | Managed and personal desktop clients, local permissions, updates, and session relay. Trigger: Packaging, local-file, tool, update, or gateway integration changes. | `research`, `codebase-design`, `prototype`, `code-review`, `psdc-upstream-adoption`, `psdc-evidence-audit`, `psdc-engineering-quality` | A developer-machine run does not establish managed-campus rollout or personal-device safety. |
| **mobile**: `psdc-mobile`, `algonquin-mobile` | Mobile client, store packaging, device permissions, offline state, and session handoff. Trigger: Device capability, permission, session, or release path changes. | `research`, `codebase-design`, `prototype`, `code-review`, `psdc-upstream-adoption`, `psdc-evidence-audit`, `psdc-engineering-quality` | A simulator run does not establish app-store approval, device privacy, or offline recovery. |
| **deployment**: `psdc-deployment-template`, `algonquin-deployment` | OpenTofu, Ansible, images, secrets separation, network profiles, and rollback. Trigger: A deployment module, environment binding, security setting, or recovery path changes. | `research`, `code-review`, `to-questionnaire`, `psdc-upstream-adoption`, `psdc-evidence-audit`, `psdc-engineering-quality` | A plan or dry run does not establish a safe institution deployment or recovery drill. |
| **agent-skills**: `psdc-agent-skills` | Skill provenance, routing, consumer manifests, agent guidance, and evidence rubrics. Trigger: An upstream skill, wrapper, registry gate, or consumer contract changes. | `writing-for-agents`, `research`, `code-review`, `retro`, `psdc-project-assessment`, `psdc-evidence-audit`, `psdc-upstream-adoption`, `psdc-engineering-quality` | Registry and hash checks prove structure and provenance, not agent compliance or product readiness. |

## Complete skill-by-skill application map

This maps all pinned pack skills and format pilots to task triggers across the
22 scoped repositories (workspace root plus catalog entries).
`all` means every repository profile above; a
named profile narrows ownership. Gated, prohibited, and pilot rows are
**planning scope only**, not permission to invoke or add to a consumer manifest.
Workspace views live in `psdc-workspace`; skill policy is owned by `psdc-agent-skills`.
The [inventory](COMPLETE-SKILL-INVENTORY.md) explains each method and example.

| Skill | Pack state | Repository profiles | Use when | Activation boundary |
|---|---|---|---|---|
| `setup-matt-pocock-skills` | adapted | agent-skills | Design or revise the common issue and domain-document conventions. | Consumer opt-in at pinned revision and task authority |
| `grill-with-docs` | adapted | All 22 repositories | An unresolved human decision must be elicited and recorded in governed documents. | Consumer opt-in at pinned revision and task authority |
| `domain-modeling` | adapted | All 22 repositories | A bounded-context term, invariant, glossary entry, or ADR changes. | Consumer opt-in at pinned revision and task authority |
| `to-spec` | adapted | All 22 repositories | Approved context needs a bounded specification with acceptance criteria. | Consumer opt-in at pinned revision and task authority |
| `to-tickets` | adapted | All 22 repositories | A reviewed specification needs dependency-aware implementation handoffs. | Consumer opt-in at pinned revision and task authority |
| `wayfinder` | adapted | All 22 repositories | A broad effort has unresolved decisions or unclear sequencing. | Consumer opt-in at pinned revision and task authority |
| `research` | adapted | All 22 repositories | A technical, licensing, or protocol claim needs primary-source evidence. | Consumer opt-in at pinned revision and task authority |
| `writing-for-agents` | enabled | All 22 repositories | Agent instructions, skill pointers, or completion criteria change. | Consumer opt-in at pinned revision and task authority |
| `code-review` | adapted | All 22 repositories | A bounded diff or PR needs standards and specification review. | Consumer opt-in at pinned revision and task authority |
| `codebase-design` | adapted | All 22 repositories | An implemented or planned module needs an ownership seam and narrow interface. | Consumer opt-in at pinned revision and task authority |
| `improve-codebase-architecture` | adapted | All 22 repositories | Existing code shows evidenced boundary or dependency problems; propose changes before refactoring. | Consumer opt-in at pinned revision and task authority |
| `pr` | adapted | All 22 repositories | An authorized change is ready for a reviewable pull-request description. | Consumer opt-in at pinned revision and task authority |
| `prototype` | adapted | All 22 repositories | A focused uncertainty can be answered with a disposable synthetic spike. | Consumer opt-in at pinned revision and task authority |
| `retro` | adapted | All 22 repositories | A completed work session needs a bounded process or agent-environment retrospective. | Consumer opt-in at pinned revision and task authority |
| `grill-me` | adapted | All 22 repositories | The user asks to stress-test an idea without immediately changing governed records. | Consumer opt-in at pinned revision and task authority |
| `grilling` | adapted | All 22 repositories | The user requests a staged interview about a design or decision. | Consumer opt-in at pinned revision and task authority |
| `handoff` | adapted | All 22 repositories | Work changes maintainer or agent and exact revisions, evidence, and next actions must transfer. | Consumer opt-in at pinned revision and task authority |
| `teach` | adapted | All 22 repositories | A club member requests a structured learning path for a component. | Consumer opt-in at pinned revision and task authority |
| `to-questionnaire` | adapted | All 22 repositories | An institution, operator, counsel, or other human owner must answer scoped questions. | Consumer opt-in at pinned revision and task authority |
| `wait-what` | adapted | All 22 repositories | A prior explanation needs a simpler, glossary-consistent retelling. | Consumer opt-in at pinned revision and task authority |
| `psdc-project-assessment` | enabled | All 22 repositories | A maturity or readiness claim must be graded against revision-bound evidence. | Consumer opt-in at pinned revision and task authority |
| `psdc-evidence-audit` | enabled | All 22 repositories | A claim needs an artifact, producer, revision, check, scope, and limitation trace. | Consumer opt-in at pinned revision and task authority |
| `psdc-upstream-adoption` | enabled | All 22 repositories | A component or implementation delta needs adopt/adapt/patch/fork/build analysis. | Consumer opt-in at pinned revision and task authority |
| `psdc-engineering-quality` | enabled | All 22 repositories | A PSDC repository change needs revision-bound documentation or engineering conformance review; proposed rules remain advisory. | Consumer opt-in at pinned revision and task authority |
| `psdc-workspace-health` | enabled | workspace, agent-skills | The workspace command center, documentation, and skill-scope snapshot need a read-only health report across all checkouts. | Consumer opt-in at pinned revision and task authority |
| `psdc-obsidian-format` | gated | workspace, agent-skills | A derived workspace Markdown or Canvas view needs PSDC portable-link and authority rules; human adoption gate remains open. | Human policy review before consumer opt-in |
| `ask-matt` | gated | All 22 repositories | A PSDC-safe skill router is accepted; currently gated against unsafe implementation routing. | PSDC router must exclude gated implementation and external-write flows |
| `triage` | gated | All 22 repositories | Issue-state rules and tracker mutation authority are accepted; currently gated. | explicit issue-tracker mutation authority and PSDC issue-state mapping |
| `diagnosing-bugs` | gated | All 22 repositories | Executable behavior exists and a reproducible failure needs hypothesis-driven diagnosis; currently gated. | executable-system-exists |
| `tdd` | gated | All 22 repositories | An approved implementation slice permits test-first work; currently gated. | approved-implementation-slice |
| `implement` | prohibited | All 22 repositories | A future policy change explicitly permits this workflow; currently prohibited. | Documentation-first lifecycle does not authorize autonomous implementation. |
| `implement-spec` | prohibited | All 22 repositories | A future policy change explicitly permits specification-wide execution; currently prohibited. | Approved specs require an explicit implementation instruction and handoff gate. |
| `obsidian-markdown` | pilot | workspace, agent-skills | A reviewed workspace view needs Obsidian Markdown syntax; pilot only, with repository links kept portable. | Verify PSDC link portability and record optional rendering status before consumer opt-in. |
| `json-canvas` | pilot | workspace, agent-skills | A reviewed workspace dependency or authority view needs JSON Canvas syntax; pilot only. | Verify generated Canvas schema, link targets, and optional rendering before consumer opt-in. |

## Not imported into the common skill pack

These upstream skills have no PSDC application route. Reconsider them in a
separate source, license, security, and owner review; this map does not
make them available in any consumer repository.

| Upstream skill | Why excluded |
|---|---|
| `wizard` | Credential and GitHub-secret writing needs a separate Windows and institution security review. |
| `chief-of-staff` | Experimental long-running subagent orchestration. |
| `claude-handoff` | Claude-specific agent handoff; not portable common behavior. |
| `loop-me` | Experimental workflow interview overlaps governed specification skills. |
| `setup-ts-deep-modules` | Experimental and TypeScript-specific; assess in a client repo. |
| `writing-beats` | Editorial composition outside component engineering. |
| `writing-fragments` | Editorial composition outside component engineering. |
| `writing-shape` | Editorial composition outside component engineering. |
| `git-guardrails-claude-code` | Claude Code hooks belong in an agent-specific overlay. |
| `migrate-to-shoehorn` | A specific TypeScript test-helper migration not selected by PSDC. |
| `scaffold-exercises` | Assumes AI Hero course tooling rather than PSDC club-lab tooling. |
| `setup-pre-commit` | Husky and lint-staged are not a universal Go, Python and TypeScript repository rule. |

## Declared consumer opt-ins at the inspected revisions

| Repository | Commit | Pack pin | Declared enabled skills |
|---|---|---|---|
| `psdc-workspace` | `e0e2535c3a03` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `to-spec`, `wayfinder`, `writing-for-agents` |
| `psdc-architecture` | `992359c9a2bf` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `grill-with-docs`, `to-spec`, `wayfinder`, `research`, `writing-for-agents` |
| `algonquin-architecture` | `7347cbc45158` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `to-spec`, `writing-for-agents` |
| `psdc-cloud` | `600240827e0c` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `to-spec`, `research`, `writing-for-agents` |
| `algonquin-cloud` | `05f728a3f78c` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `to-spec`, `writing-for-agents` |
| `psdc-ai` | `fea3454ee111` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `to-spec`, `research`, `writing-for-agents` |
| `algonquin-ai` | `07219f498a40` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `to-spec`, `writing-for-agents` |
| `psdc-compute` | `9ed1e812f63e` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `to-spec`, `research`, `writing-for-agents` |
| `algonquin-compute` | `b2a02e10c0b3` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `to-spec`, `writing-for-agents` |
| `psdc-media` | `a0667a857858` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `to-spec`, `research`, `writing-for-agents` |
| `algonquin-media` | `5193327a1426` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `to-spec`, `writing-for-agents` |
| `psdc-social` | `b7bb37352f99` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `to-spec`, `research`, `writing-for-agents` |
| `algonquin-social` | `03d7bb29eb12` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `to-spec`, `writing-for-agents` |
| `psdc-web` | `064cfe07a051` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `to-spec`, `research`, `writing-for-agents` |
| `algonquin-web` | `bb8d7469aa77` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `to-spec`, `writing-for-agents` |
| `psdc-desktop` | `9798d259fafa` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `to-spec`, `research`, `writing-for-agents` |
| `algonquin-desktop` | `f0c1dd3a035d` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `to-spec`, `writing-for-agents` |
| `psdc-mobile` | `58dc054af89a` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `to-spec`, `research`, `writing-for-agents` |
| `algonquin-mobile` | `6f024b2d2032` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `to-spec`, `writing-for-agents` |
| `psdc-deployment-template` | `6e1f52a2f4cf` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `to-spec`, `research`, `writing-for-agents` |
| `algonquin-deployment` | `278377f97ca2` | `dc7baf75ecad (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `to-spec`, `writing-for-agents` |
| `psdc-agent-skills` | `318d204aedf1` | `45386cb2f1cc (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `writing-for-agents` |

## Task selection and completion

1. Identify the owning repository, changed area, manifest revision, and authority.
2. Use a relevant method only if the manifest enables it and the pinned pack permits it.
   Resolve an older pin at its own revision; do not apply today's registry retroactively.
3. Match evidence to the claim: code tests, physical lab safety, institution approval,
   deployment, and sustained operation are different checks.
4. Record the exact checks and omitted checks. A skill, manifest, or generated map
   never grants permission to merge, publish, enroll devices, or deploy.

## Refresh and verification

From `psdc-agent-skills`, refresh after fetching the workspace and consumer
repositories' `origin/main` refs:

```powershell
python scripts/Build-ApplicationScope.py --refresh --workspace-root C:\path\to\psdc-workspace
python scripts/Build-ApplicationScope.py --check --workspace-root C:\path\to\psdc-workspace
```

When the workspace source is a separate worktree, add
`--checkout-root C:\path\to\product-checkouts` to point at sibling repositories.

`--check` without a workspace verifies the committed snapshot against the registry
and generated document. With a workspace it additionally detects source drift.
A new skill-pack commit alone is ignored when its consumer manifest digest is unchanged;
a changed manifest still fails the check.
Neither mode tests actual agent behavior or product readiness.
