# FDS Document Distribution Manifest v3.1.17

> Distribution date: 2026-09-04 candidate  
> Decision: D37  
> Status: READY FOR REVIEW  
> Repository: `321Team/fds-project-baseline`

## Payload inventory

| Path | SHA-256 |
|---|---|
| `baseline/FDS_Project_Implementation_Baseline_v3.1.17.md` | `0a5a73f1775464350dc4dacf4fdf672d3dab89cdd32a8ea5fbe837b711c908ff` |
| `wbs/FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx` | `68a75598da5ffdc8300b14c7ef2981252af7f713ddc5c11e79e75929be032c0b` |
| `tickets/FDS_v3.1.17_Canonical_Ticket_Update_Pack_v1.0.md` | `a881b488148d778551b58b79bc8c77d1e43cf6c7295bdd779359c08a5d508ca1` |
| `web/FDS_v3.1.17_Canonical_Status.html` | `1a7a58fd3d70a87512ef8ad106720baf59bbd1a6b5dd3be63cc10b5fddf081a3` |
| `audit/FDS_Canonical_Integrity_Audit_v3.1.17.md` | `245d9d39cb7b70c38bb95925d001e2cfdcf106e5a8396887342d213e1faef2b8` |
| `releases/v3.1.17/D37_GitHub_Canonical_Baseline_Repository_and_v3.1.17_Release_Record_v1.0.md` | `ed4f19b0a31684a781a09ca5e54e5e8a220ae8fde41b93129da8f08d30a8a1c7` |
| `releases/v3.1.17/FDS_Project_Implementation_Baseline_Release_Notes_v3.1.17.md` | `2a6db93b1050d01a875cef279929f65e0f6b906f1afcb4b7c62bdb01ca6b4b4a` |

## Preserved history

- `releases/v3.1.15/`: 5 source files preserved without modification.
- `releases/v3.1.16/`: 6 source files preserved without modification.

## Verification

Run from repository root:

```bash
sha256sum -c releases/v3.1.17/SHA256SUMS
```

The ZIP sidecar hash is distributed separately as `FDS_v3.1.17_Canonical_Baseline_Release_Package.zip.sha256` to avoid a circular package hash.

**DISTRIBUTION_MANIFEST_VERDICT=READY_FOR_REVIEW**
