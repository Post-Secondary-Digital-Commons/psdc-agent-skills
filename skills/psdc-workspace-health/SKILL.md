---
name: psdc-workspace-health
description: Check the PSDC workspace command center, local documentation links, and skill-scope snapshot against explicit repository revisions. Use for Platform Home or vault health requests, not product deployment readiness.
---

# PSDC Workspace Health

Ask for or resolve the explicit PSDC workspace and checkout roots. Run
`python skills/psdc-workspace-health/scripts/check_workspace.py
--workspace-root <psdc-workspace> --checkout-root <checkout-parent>` from the
skill-pack root. The script writes generated views only to a temporary folder
and returns a JSON report; it never refreshes the live vault. Obsidian is not
required.

Explain each failing or unrun check from that report. Separate the inspected
workspace `HEAD` from `origin/main`; a stale checkout is not current evidence.
Report command-center generation, workspace documentation validation, and skill-scope
drift separately. A successful generator verifies only its declared structural
and artifact-digest checks. It does not assess semantic clones, external links,
security, deployment, or production behavior.

For a request to repair the vault, use the report to bound a separate change;
preview the exact files and respect the authority of source repositories.
Generated maps and the Platform Home are navigation views, not new decisions.
