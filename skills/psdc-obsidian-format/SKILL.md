---
name: psdc-obsidian-format
description: Create or check PSDC workspace Markdown maps and JSON Canvas views while preserving portable repository links and source authority. Use for vault navigation notes or .canvas files, not for changing contracts or decisions.
---

# PSDC Obsidian-Compatible Formats

Identify the owning repository and whether the file is a product document or a
workspace navigation view. Product documents use relative Markdown links that
work when cloned alone. Workspace views may use path-qualified wikilinks when
the target resolves from the vault root. Both remain ordinary Git files;
Obsidian is optional.

For Obsidian syntax, consult the pinned
[`obsidian-markdown`](../../vendor/obsidian/obsidian-markdown/SKILL.md) skill.
For `.canvas` shape, consult the pinned
[`json-canvas`](../../vendor/obsidian/json-canvas/SKILL.md) skill. These are
unmodified pilot sources; PSDC link and authority rules above take precedence.
Do not use an app-specific CLI to make ordinary file edits.

After changing a workspace map, run the owning workspace's local-link checker.
After changing a Canvas, run
`python skills/psdc-obsidian-format/scripts/validate_canvas.py <vault-root>`.
Report structural failures and whether visual rendering was actually checked.
Generated maps are derived from `repos.yaml`, contracts, and evidence records;
a visual edge never becomes a new dependency or accepted decision by itself.
