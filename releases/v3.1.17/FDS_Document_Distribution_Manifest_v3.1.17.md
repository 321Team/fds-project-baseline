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
| `audit/FDS_Canonical_Integrity_Audit_v3.1.17.md` | `141493632bf3397541ff192977d584bbdf96a6b415f880858f16b1cb33f8456f` |
| `releases/v3.1.17/D37_GitHub_Canonical_Baseline_Repository_and_v3.1.17_Release_Record_v1.0.md` | `41e03cb13ebbc41aa82e276ca2916fa02bffd74c264124a9ff1193e2638d60b0` |
| `releases/v3.1.17/FDS_Project_Implementation_Baseline_Release_Notes_v3.1.17.md` | `eec19b0740b9378ac768d1485373f50e35e7ca87572e0e961583b5a017a1c73b` |

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
