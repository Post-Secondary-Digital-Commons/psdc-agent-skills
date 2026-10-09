# Skill Application Scope

> Generated from `config/application-scope.yaml`, `config/skill-registry.yaml`,
> the workspace catalog, and each repository's `origin/main` consumer manifest.
> This is a revision-bound structural snapshot, not evidence that an agent used a skill.

## Read this map

A profile names useful methods for a repository's work, **not** automatic enablement.
The consumer manifest lists declared opt-ins at its own pinned pack revision.
A task triggers only the applicable enabled method, subject to its gate, repository
instructions, and explicit user authority. The [registry](../../config/skill-registry.yaml)
sets current pack-wide modes; the [inventory](COMPLETE-SKILL-INVENTORY.md)
explains every skill. An older consumer pin is **not** validated against newer rules.

Workspace catalog revision: `123cfa62b98b4add00330d7cd1ad260d3eecf517`. Pack revision
inspected when generated: `d527cbeda07fac579f9088197b71f785f082acc4`. Source manifests and commits
are recorded in `config/application-scope-snapshot.json`.
**21 of 21** consumer pins differ from that pack revision;
this map does not silently upgrade them.

## Repository and area profiles

| Profile / repositories | Areas and trigger | Relevant methods | Evidence boundary |
|---|---|---|---|
| **architecture**: `psdc-architecture`, `algonquin-architecture` | Decisions, contracts, fixtures, roadmaps, and institution policy overlays. Trigger: Changes to shared terms, interfaces, decisions, or readiness claims. | `domain-modeling`, `research`, `to-spec`, `to-tickets`, `wayfinder`, `code-review`, `psdc-project-assessment`, `psdc-evidence-audit`, `psdc-upstream-adoption` | A document or contract check does not establish service behavior or institution approval. |
| **cloud**: `psdc-cloud`, `algonquin-cloud` | Identity, policy, storage, evidence, networking, and infrastructure interfaces. Trigger: A shared service boundary, dependency, or deployment profile changes. | `research`, `codebase-design`, `code-review`, `prototype`, `psdc-upstream-adoption`, `psdc-evidence-audit` | A local service test does not establish custody, disaster recovery, or production admission. |
| **ai**: `psdc-ai`, `algonquin-ai` | Session control, gateway, model routing, tool grants, and inference integration. Trigger: A model, tool, data-access, or session boundary changes. | `research`, `codebase-design`, `prototype`, `code-review`, `psdc-upstream-adoption`, `psdc-evidence-audit` | A model demo does not establish safe tool authority, privacy, scale, or campus availability. |
| **compute**: `psdc-compute`, `algonquin-compute` | Providers, capabilities, workload admission, placement, leases, workers, and receipts. Trigger: A scheduler, worker, upstream mechanism, or lab-machine boundary changes. | `domain-modeling`, `research`, `codebase-design`, `prototype`, `code-review`, `psdc-upstream-adoption`, `psdc-evidence-audit` | Synthetic and unit tests do not establish lab safety, operator consent, physical capacity, or settlement correctness. |
| **media**: `psdc-media`, `algonquin-media` | Image, video, spatial, 3D, and 4DGS processing and media custody. Trigger: A pipeline, format, model, provenance, or media-access boundary changes. | `research`, `codebase-design`, `prototype`, `code-review`, `psdc-upstream-adoption`, `psdc-evidence-audit` | Render success does not establish provenance, rights, deletion, or cross-device performance. |
| **social**: `psdc-social`, `algonquin-social` | ActivityPub, social surfaces, moderation, federation, and spatial content policy. Trigger: A federation message, moderation, identity, or consent boundary changes. | `domain-modeling`, `research`, `to-spec`, `code-review`, `psdc-upstream-adoption`, `psdc-evidence-audit` | Protocol parsing does not establish federation trust, consent, or moderation effectiveness. |
| **web**: `psdc-web`, `algonquin-web` | Browser client, accessibility, sessions, gateway integration, and user-facing flows. Trigger: A UI, accessibility, session, or shared API interaction changes. | `research`, `codebase-design`, `prototype`, `code-review`, `psdc-upstream-adoption`, `psdc-evidence-audit` | A mock UI or browser build does not establish end-to-end identity or deployed usability. |
| **desktop**: `psdc-desktop`, `algonquin-desktop` | Managed and personal desktop clients, local permissions, updates, and session relay. Trigger: Packaging, local-file, tool, update, or gateway integration changes. | `research`, `codebase-design`, `prototype`, `code-review`, `psdc-upstream-adoption`, `psdc-evidence-audit` | A developer-machine run does not establish managed-campus rollout or personal-device safety. |
| **mobile**: `psdc-mobile`, `algonquin-mobile` | Mobile client, store packaging, device permissions, offline state, and session handoff. Trigger: Device capability, permission, session, or release path changes. | `research`, `codebase-design`, `prototype`, `code-review`, `psdc-upstream-adoption`, `psdc-evidence-audit` | A simulator run does not establish app-store approval, device privacy, or offline recovery. |
| **deployment**: `psdc-deployment-template`, `algonquin-deployment` | OpenTofu, Ansible, images, secrets separation, network profiles, and rollback. Trigger: A deployment module, environment binding, security setting, or recovery path changes. | `research`, `code-review`, `to-questionnaire`, `psdc-upstream-adoption`, `psdc-evidence-audit` | A plan or dry run does not establish a safe institution deployment or recovery drill. |
| **agent-skills**: `psdc-agent-skills` | Skill provenance, routing, consumer manifests, agent guidance, and evidence rubrics. Trigger: An upstream skill, wrapper, registry gate, or consumer contract changes. | `writing-for-agents`, `research`, `code-review`, `retro`, `psdc-project-assessment`, `psdc-evidence-audit`, `psdc-upstream-adoption` | Registry and hash checks prove structure and provenance, not agent compliance or product readiness. |

## Declared consumer opt-ins at the inspected revisions

| Repository | Commit | Pack pin | Declared enabled skills |
|---|---|---|---|
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
| `psdc-agent-skills` | `d527cbeda07f` | `45386cb2f1cc (older/different)` | `psdc-project-assessment`, `psdc-evidence-audit`, `domain-modeling`, `writing-for-agents` |

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

`--check` without a workspace verifies the committed snapshot against the registry
and generated document. With a workspace it additionally detects source drift.
A new skill-pack commit alone is ignored when its consumer manifest digest is unchanged;
a changed manifest still fails the check.
Neither mode tests actual agent behavior or product readiness.
