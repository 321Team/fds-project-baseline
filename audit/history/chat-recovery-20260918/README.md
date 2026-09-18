# Historical audit recovery — 2026-09-18

Status: ORIGINAL_TRANSFER_PENDING. This directory currently records recovery/verification metadata; the five original files below are not yet committed here. Do not mark the recovery complete or merge this staging PR until their remote bytes have been checked.

## Scope

The user requested verification of the recovered P1-K8S v4.0 reference and preservation of seven historical audit/review artifacts. Five cross-project originals belong here; the two DNS review records are handled separately in infra-dns.

Current published baseline used only as context: docs-v3.1.19, target 966fc5365874b1d259a9810fc876b57c3bfa0e08, published 2026-09-18 09:20:13 KST. No released baseline, CURRENT, WBS, tag, issue AC/status, or server setting is changed.

## Recovered originals awaiting transfer

| File | Bytes | SHA-256 |
|---|---:|---|
| FDS_All_Issues_AC_Baseline_Audit_20260912_v1.0.md | 30324 | acdfce4299e09f11c8c39e0d11537fa51cf950cf5d52f53442e61f9f955fac07 |
| FDS_All_Ticket_Spec_Record_Audit_20260914_v1.0.md | 54478 | d14788aa314215f4cb818356e90a26d91c28855f81350945099775e9f2da90fc |
| FDS_Ticket_Spec_Update_Result_20260915_v1.0.md | 16668 | d6415721f104dbcbbe16eb996cd52ecf504626095dab74eff53449cd27d9d9b0 |
| FDS_Ticket_Spec_Update_Evidence_20260915_v1.0.zip | 632622 | 62a31d966ce6be89196bc63dab6c3d7bd5ec0dbeafc6c785e37f2acbcb61691b |
| FDS_Canonical_Alignment_and_Followup_Review_20260910_v1.0.md | 15557 | a6c1910059a0f0fc6096f04c64fcc6a16afdfdf5db2c026b192b6d47097390ab |

The exact Project Library bytes were recovered to the analysis workspace. No recreation from chat summaries or normalization of the originals was performed.

## Verification actually performed

- Historical ticket-update ZIP: 8 files, CRC valid, internal SHA256SUMS 7/7, exact file-set coverage.
- Historical before/after snapshots: 78 unique issue IDs on each side, identical ID sets, original bodies preserved 78/78; title/state/lock/labels/assignees/milestone/type/state_reason/closed_at/comments/issue_field_values equal 78/78. These are checks of historical snapshots, not a fresh comparison of all live issues or a claim that every AC was implemented.
- Six historical Markdown files plus eight ZIP members were screened for six concrete credential-pattern classes; no matches. Limited pattern screening is not proof that every possible secret is absent.
- Recovery is HISTORICAL / REFERENCE ONLY. Earlier PASS/Done/approval statements remain attributed to the original record and its date, not new approval or Runtime credit.

## Inventory limitation

The earlier review used selected filenames against main and selected issue/PR references. Filename absence from main does not prove that equivalent content is absent from every branch, PR, release asset, or extracted evidence registry. This recovery does not certify a project-wide SHA-to-evidence inventory audit.

## Remaining action

Transfer the original five files with their exact bytes into originals/, verify remote SHA-256 and Git blob IDs, update this status and the PR body, then obtain the applicable Lead review/merge decision. The current connector supports text writes but has no mounted-file binary upload action; a bounded gh-API transfer procedure is being supplied for the existing ansible01 account. Do not rebuild or reformat the ZIP to bypass this limitation.

Rollback is a reviewed repository revert; no server rollback is involved.

Tracking: https://github.com/321Team/fds-project-baseline/issues/24
