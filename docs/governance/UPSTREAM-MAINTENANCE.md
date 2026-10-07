# Upstream Maintenance

## Update procedure

1. Select an explicit upstream commit; never import a floating branch.
2. Review upstream license and security-relevant changes.
3. Import into a new branch with the installer recorded in the pull request.
4. Compare every vendored path to upstream and record added, changed, and removed files.
5. Re-run skill validation and the PSDC assessment fixtures.
6. Review PSDC wrappers for assumptions invalidated by upstream changes.
7. Update `config/skill-registry.yaml` and `THIRD_PARTY_NOTICES.md` together.
8. Merge only after human review.

## Fork policy

PSDC does not edit vendored upstream files. A necessary behavioral change is
implemented in a PSDC wrapper when possible. If an upstream file must be forked,
copy it into `skills/`, record its source and modifications, and stop describing
it as unmodified upstream.
