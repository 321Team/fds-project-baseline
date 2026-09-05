# FDS Project Baseline

Private canonical repository for the FDS hybrid cloud project's approved baseline, WBS/Gantt, ticket pack, release records, WEB snapshot and integrity audits.

## Source-of-truth rule

- `main` contains only approved `RELEASED` document baselines.
- `release/vX.Y.Z` prepares one candidate release through review.
- A release is canonical only after PR approval, required checks, merge to protected `main`, manifest verification and SHA-256 verification.
- Working branches, local files and development repositories are not document canonical sources.
- `CURRENT.md` identifies the active release and its immutable merge commit SHA.

## Repository layout

| Path | Purpose |
|---|---|
| `baseline/` | Project implementation baseline |
| `wbs/` | Master WBS and Gantt workbook |
| `tickets/` | Canonical ticket property and description pack |
| `architecture/` | Approved logical and physical architecture sources/exports |
| `web/` | Static distribution snapshot; not live Runtime evidence |
| `releases/` | Immutable version history, release notes, manifest, checksums and package |
| `audit/` | Read-only integrity and consistency audit results |
| `governance/` | Release and document-control rules |
| `scripts/` | Local and CI integrity verification |

## Candidate verification

```bash
bash scripts/verify-canonical-release.sh
```

See `governance/RELEASE_POLICY.md` before publishing.
