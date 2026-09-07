# FDS Document Distribution Manifest v3.1.17

> Distribution date: 2026-09-07  
> Decision: D37  
> Status: RELEASED / FINALIZATION  
> Repository: `321Team/fds-project-baseline`

## Payload inventory

| Path | SHA-256 |
|---|---|
| `baseline/FDS_Project_Implementation_Baseline_v3.1.17.md` | `3b52486d9fb7f8d3458499a12ee5b92843467f52c30afb9dc151b45f1e014589` |
| `wbs/FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx` | `68a75598da5ffdc8300b14c7ef2981252af7f713ddc5c11e79e75929be032c0b` |
| `tickets/FDS_v3.1.17_Canonical_Ticket_Update_Pack_v1.0.md` | `b93f02499be033a5052f28d3c1017201e3b6de451e3f0858cff1ee9aef751fad` |
| `web/FDS_v3.1.17_Canonical_Status.html` | `2b18c006bf99c730a39590d615c96c8ba2bb5fb658c0bfa3e2c2f47e281acf91` |
| `audit/FDS_Canonical_Integrity_Audit_v3.1.17.md` | `3a74992bd961f1b1067b06c0f3c776df2e4ceb5b75427cb5b6c750dde3b53c8c` |
| `releases/v3.1.17/D37_GitHub_Canonical_Baseline_Repository_and_v3.1.17_Release_Record_v1.0.md` | `b9b28a4a189c0410c44c9cdbb36ac3ba429a2a664fe4fb03886085d1ae4dedec` |
| `releases/v3.1.17/FDS_Project_Implementation_Baseline_Release_Notes_v3.1.17.md` | `43e2490363905dfeae8827a818f7a7b3ebffaab45539e8e7aa33a3b7bbcb8393` |

## Preserved history

- `releases/v3.1.15/`: 5 source files preserved without modification.
- `releases/v3.1.16/`: 6 source files preserved without modification.

## Verification

Run from repository root:

```bash
sha256sum -c releases/v3.1.17/SHA256SUMS
```

The ZIP sidecar hash is distributed separately as `FDS_v3.1.17_Canonical_Baseline_Release_Package.zip.sha256` to avoid a circular package hash.

**DISTRIBUTION_MANIFEST_VERDICT=RELEASED_FINALIZATION_IN_PROGRESS**
