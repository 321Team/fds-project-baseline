# FDS Project Baseline

Private canonical repository for the FDS hybrid cloud project's approved baseline, WBS/Gantt, architecture, ticket pack, release records, and audit results.

## Source-of-truth rule

- `main` contains only approved `RELEASED` document baselines.
- `release/vX.Y.Z` prepares one candidate release through review.
- A release is canonical only after PR approval, merge to `main`, manifest verification, and SHA-256 verification.
- Working branches and local files are not canonical.
- `CURRENT.md` identifies the active release and its immutable commit SHA.

## Repository layout

| Path | Purpose |
|---|---|
| `baseline/` | Project implementation baseline |
| `wbs/` | Master WBS and Gantt workbook |
| `tickets/` | Canonical ticket property and description pack |
| `architecture/` | Approved logical and physical architecture sources/exports |
| `releases/` | Versioned release notes, manifest, checksums, and package |
| `audit/` | Read-only integrity and consistency audit results |
| `governance/` | Release and document-control rules |

See `governance/RELEASE_POLICY.md` before publishing.
