# Open-source workspace and Obsidian skill survey

> Status: Research and adoption proposal, not an accepted decision or an enabled skill.
>
> Inspected: 2026-10-09. Workspace catalog: `Post-Secondary-Digital-Commons/psdc-workspace` `origin/main` at `123cfa62b98b4add00330d7cd1ad260d3eecf517`.
>
> Scope: Agent skills and open-source tools for the PSDC polyrepo knowledge plane.

## Recommendation

There **are** open-source Obsidian skills. Evaluate a pinned, reviewed subset of
[`kepano/obsidian-skills`](https://github.com/kepano/obsidian-skills/tree/3ccff5338ea700537839b21900aa5358a0402c98)
before writing format guidance from scratch. Begin with `obsidian-markdown` and
`json-canvas`; add `obsidian-bases` only for explicitly derived, optional views.
Do not make `obsidian-cli` a CI or platform dependency. No upstream skill knows
PSDC's authority hierarchy, Common/institution boundary, or evidence states, so
those behaviors need narrow PSDC-native wrappers around existing workspace
generators and validators, not a second vault framework.

The upstream skill files are MIT-licensed, but the Obsidian application is not
open source: its [terms](https://obsidian.md/terms) reserve software rights.
The [official CLI](https://obsidian.md/help/cli) needs a compatible installed
and running Obsidian desktop app. PSDC's accepted architecture makes Obsidian
an optional editor over Git-controlled Markdown; no product or test gate may
require it. See the [workspace knowledge architecture](https://github.com/Post-Secondary-Digital-Commons/psdc-architecture/blob/main/docs/architecture/Workspace-Knowledge-and-Agent-Skills.md)
and [open-source-only policy](https://github.com/Post-Secondary-Digital-Commons/psdc-architecture/blob/main/docs/vision/11-Open-Source-Only-Policy.md).

## Candidate matrix

| Candidate at inspected source | License and useful capability | PSDC disposition and reason |
|---|---|---|
| [`kepano/obsidian-skills` at `3ccff53`](https://github.com/kepano/obsidian-skills/tree/3ccff5338ea700537839b21900aa5358a0402c98) | [MIT](https://github.com/kepano/obsidian-skills/blob/3ccff5338ea700537839b21900aa5358a0402c98/LICENSE); skills for Markdown, Bases, JSON Canvas, CLI, Defuddle and Knap. | **Pilot selected format skills**, pinning exact files and hashes. Review each skill separately; no bulk install or automatic consumer opt-in. |
| [`gmickel/obsidian-skill` at `d10be94`](https://github.com/gmickel/obsidian-skill/tree/d10be948bb5b8e8a8159ac8fc98d64b4603a1ec3) | [MIT](https://github.com/gmickel/obsidian-skill/blob/d10be948bb5b8e8a8159ac8fc98d64b4603a1ec3/LICENSE); cross-platform CLI skill with scoped reference files. | **Alternative CLI guide**, not a second default. It still depends on Obsidian and does not replace headless checks. |
| [`pariyar07/ariadne` at `f898253`](https://github.com/pariyar07/ariadne/tree/f8982537fcbb18b807b717ce3d613eb68b07066f) | [MIT](https://github.com/pariyar07/ariadne/blob/f8982537fcbb18b807b717ce3d613eb68b07066f/LICENSE); vault navigation, workspace instructions, scope topology, and deterministic validation. | **Study/adapt individual patterns**; do not bootstrap its entire vault into PSDC. Its scope descriptors and generated views would overlap PSDC's existing catalog, maps and authority rules. |
| [`lycheeverse/lychee` at `c11d779`](https://github.com/lycheeverse/lychee/tree/c11d7794e9be55fc57d5ffd35543bf6221799fb3) | [Apache-2.0](https://github.com/lycheeverse/lychee/blob/c11d7794e9be55fc57d5ffd35543bf6221799fb3/LICENSE-APACHE); checks external links in Markdown and other formats. | **Candidate checker**, not an agent skill or wikilink/authority checker. Pin its version and use bounded online checks separately from local-link checks. |
| [Backstage software catalog](https://backstage.io/docs/features/software-catalog/) | [Apache-2.0](https://github.com/backstage/backstage/blob/master/LICENSE); catalog and ownership/dependency portal. | **Later portal option**, not warranted for the current static command center. Do not copy product source into a portal. |
| [SilverBullet](https://github.com/silverbulletmd/silverbullet) | [MIT](https://github.com/silverbulletmd/silverbullet/blob/main/LICENSE); self-hosted Markdown knowledge app. | **Optional FOSS editor/viewer evaluation**. Preserve link and metadata portability before any migration. |

These are source and license observations, not a security audit, integration test,
or promise of long-term maintenance. GitHub metadata inspected on 2026-10-09
reported the three skill repositories above as unarchived; that is a weak
maintenance signal, not a support guarantee.

## Fit against the workspace that already exists

The workspace `origin/main` already contains `repos.yaml`, a Platform Home,
generated authority/contract/evidence/dependency maps, and
`scripts/Build-WorkspaceCommandCenter.py` plus its test script. Therefore a
new skill should **invoke and interpret those sources**, not maintain a second
repository inventory or hand-authored readiness dashboard. The command center
itself says broken links, semantic clones and security findings are not assessed
by that generator; a skill must not turn those blanks into zeroes. The local
workspace checkout had modified Obsidian `graph.json` and `workspace.json`
when inspected; this survey did not edit them.

The upstream [`obsidian-markdown` instructions](https://github.com/kepano/obsidian-skills/blob/3ccff5338ea700537839b21900aa5358a0402c98/skills/obsidian-markdown/SKILL.md)
prefer wikilinks for vault notes. PSDC needs a narrower rule: use repository-
portable relative Markdown links for independently cloned repository docs, and
allow vault-qualified wikilinks in workspace navigation views where the local
link checker resolves them. An upstream format preference cannot override
repository portability. The upstream [`obsidian-cli` skill](https://github.com/kepano/obsidian-skills/blob/3ccff5338ea700537839b21900aa5358a0402c98/skills/obsidian-cli/SKILL.md)
defaults to the most recently focused vault and includes overwrite and `eval`
examples; a PSDC wrapper must require an explicit vault target, preview the
write set, and disallow arbitrary app-context evaluation in routine workflows.

## PSDC-native workspace skill scopes

These are **proposed**, not implemented or added to the enabled registry.
Each must name the inspected commit, read-only versus write authority, and
which observations remain unverified. Combine nearby scopes if tests show
one narrower skill is easier to maintain.

| Proposed skill | Trigger and bounded output | Reuse and gate |
|---|---|---|
| `psdc-vault-navigation` | “Show where a decision/contract lives.” Resolve the owning repository, exact source path, revision, and vault navigation link; report missing or ambiguous targets. | Read `repos.yaml` and generated maps; never invent a cross-repo edge or edit an authoritative document. |
| `psdc-workspace-health` | “Check Platform Home, links, and skill scope.” Run existing workspace command-center, link/document and skill-scope checks; return a source-bound report with errors and unassessed fields. | Reuse workspace scripts; optionally compare with Obsidian CLI locally, but headless Git/Markdown checks remain mandatory. |
| `psdc-contract-trace` | “Trace this lease or credential claim.” Follow concept → decision → contract → fixture → test → implementation/runbook, identifying absent edges. | Read existing Contract Explorer and owning repositories; a missing implementation remains missing. |
| `psdc-overlay-sync-review` | “Compare Common and Algonquin.” Report baseline tag, fork revision, overlay-only policy, drift and conflict candidates; no automatic overwrite or merge. | Read the workspace catalog and both Git histories; institution policy remains sovereign. |
| `psdc-evidence-view` | “Why does the dashboard say implemented?” Trace a displayed claim to artifact, producer, commit, test, scope, age and omitted checks. | Extend the existing `psdc-evidence-audit` skill only if a separate view skill proves necessary. |

**First implementation slice:** pilot `obsidian-markdown` and `json-canvas`
against a disposable copy of the workspace maps, with explicit expected links
and rendering checks. Then build one read-only `psdc-workspace-health` wrapper
that calls the existing validators and emits a structured report. Keep it
disabled in consumer manifests until provenance, behavior, failure fixtures,
Windows/headless operation, and a rollback procedure pass review.

## Acceptance checks before adoption

1. Pin an upstream commit, inspect every selected `SKILL.md` and reference file,
   record exact hashes and MIT notice, and apply PSDC rules in a separate wrapper.
2. Verify ordinary relative Markdown links survive independent repository clones;
   verify allowed workspace wikilinks resolve and ambiguous ones fail.
3. Run format and health checks without Obsidian installed, and optional CLI
   checks only with an explicitly selected local vault.
4. Demonstrate negative cases: missing repository, stale commit, broken link,
   absent evidence, unintended institution data, and attempted out-of-scope write.
5. Verify generated views never upgrade `documented` or
   `structurally_validated` to `implemented`, `deployed`, or `production_proven`.
6. Review security of any import, then update the registry and individual
   consumer manifests deliberately. A green structural check is not proof of
   agent compliance or a functioning platform.

## Unverified in this survey

- No candidate skill was installed, vendored, or exercised against the live vault.
- No Obsidian version, CLI availability, or vault rendering was tested here.
- No whole-repository security audit or dependency/license transitivity review
  was performed. In particular, Defuddle and Knap need separate evaluation.
- Backstage and SilverBullet are product options, not ready-made PSDC agent
  skills; their operational cost has not been measured.
