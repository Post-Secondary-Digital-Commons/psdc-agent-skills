---
name: psdc-upstream-adoption
description: Evaluate reuse of open-source projects for a PSDC component or implementation change, and record an evidence-bounded adopt, adapt, patch, fork, or build decision. Use before introducing a component, dependency, adapter, upstream-derived code, or substantial implementation.
---

# PSDC Upstream Adoption

Use this skill for **every component** at its design boundary and for **every
implementation change** at its ticket or PR boundary. Scale the investigation
to risk: a small change within an already reviewed integration needs a short
delta check; a new authority, dependency, imported source, fork, or license
change needs a full review. This skill does not authorize code import, tracker
writes, merging, deployment, or an institutional policy decision.

## Component review

1. Bind the repository, component ID, inspected revisions, governing Decision
   Register/ADR/contract versions, and institution scope. Inspect existing
   PSDC code before proposing another abstraction.
2. State the PSDC-owned outcome and trust boundary. Separate mechanics an
   upstream can provide from identity, policy, custody, credits, federation,
   and other authority PSDC or an institution must retain.
3. Search primary upstream code, documentation, tests, release and license
   materials. Compare at least the meaningful options: adopt/configure,
   external adapter, upstream extension, bounded patch, fork, and build.
   Include "no suitable upstream" when supported by evidence, not preference.
4. Test the narrowest promising seam with synthetic positive, denial, retry,
   revocation, recovery, and privacy cases applicable to the component. Record
   what was actually executed versus inferred from documentation.
5. Produce the [adoption record](references/record-format.md), including exact
   source revision and SPDX/license evidence, excluded upstream behavior,
   patch/update budget, replacement path, consumer impact, and unresolved
   approvals. A proposed record is not an accepted dependency or release.

## Implementation change check

Before changing code, resolve the owning adoption record. If absent, create a
proposed component review first. Check whether the task changes the selected
upstream revision, license, integration mode, authority boundary, or downstream
contract. An ordinary fix may cite the existing record and document only the
delta; source import or a new dependency requires renewed provenance and
compatibility checks. At review, compare the actual diff, dependency graph,
tests, notices, and SBOM against the record. Report unverified claims plainly.

## Stop conditions

- Do not copy source or publish a dependency with unknown copyright, license,
  provenance, or security-update path. Legal compatibility and relicensing
  judgments belong to qualified reviewers under ADR-0030.
- Do not let an upstream's public market, identity, ledger, data-access model,
  or default egress override sovereign institutional authority. A signed
  artifact or passing schema is not authorization or runtime proof.
- A fork needs an explicit owner, patch budget, rebase/security plan, exit path,
  and the required architecture decision. If those are missing, mark the
  candidate blocked; do not silently substitute a custom clone.
- Follow repository and user permissions for issues, PRs, messages, remote
  actions, and deployment. Skill invocation grants none of these permissions.

Use the pinned `research` skill for deeper source investigation, `prototype`
for a throwaway compatibility spike, `codebase-design` for the adapter seam,
and `psdc-evidence-audit` for claim verification when those skills are enabled.
They do not replace this record or PSDC authority.
