# Historical audit recovery — 2026-09-18

Status: ORIGINALS_REMOTE_VERIFIED (2026-09-23). All five originals are committed byte-for-byte under originals/. Remote SHA-256, size and Git blob checks passed 5/5; the ZIP was downloaded again from GitHub and compared byte-for-byte. See REMOTE_VERIFICATION_20260923.json and SHA256SUMS.

## Scope

The user requested verification of the recovered P1-K8S v4.0 reference and preservation of seven historical audit/review artifacts. Five cross-project originals belong here; the two DNS review records are handled separately in infra-dns.

Current published baseline used only as context: [docs-v3.1.20](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.20), tag commit 336446500ef9a71c4796e6cfc8bc4db18daceb09, published 2026-09-23 02:37:13 KST. The 2026-09-18 recovery originally referred to v3.1.19; that historical context is not rewritten inside the originals. No released baseline, CURRENT, WBS, tag, issue AC/status, or server setting is changed.

## Preserved originals

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

## Review resolution — 2026-09-23

- The five original files were recovered again from their retained file identities; local size/SHA-256/Git blob matched the 2026-09-18 manifest 5/5. No ZIP regeneration or Markdown normalization was used.
- Exact binary/text blobs were uploaded and bound to originals/ in commit f87a4088d62196d5dcf68fc303a521c2e71db731. GitHub tree blob IDs and sizes matched 5/5.
- The four Markdown blobs were fetched again and their UTF-8 bytes hashed. The binary ZIP was downloaded through the authenticated GitHub file page and its 632,622 bytes matched the recovered ZIP exactly. Remote SHA-256 verification passed 5/5.
- ZIP CRC, eight-file exact member set, internal SHA256SUMS 7/7, and historical before/after body preservation and protected-field equality 78/78 were rechecked. This remains a historical snapshot audit, not present-day AC acceptance.
- SHA256SUMS covers the five originals and the four metadata/verification documents; it excludes itself.
- The DNS originals were already merged through infra-dns PR #2. Their historical HEAD/path remain in EXPECTED_ORIGINALS.json together with the checked merge metadata.
- V4_REFERENCE_CHECK.json remains the original dated reference check; this update does not claim a new ansible01 or K8S Runtime validation.

## Merge classification

This baseline PR contains archival records only; no recovered content is installed, executed, or consumed as operating input. Under governance/REVIEW_AUTHORITY_POLICY.md §2, the document Lead may decide the manual merge after checking these resolved findings. The separate fds-project-evidence independent-review rule is unchanged. AI-assisted checks are not represented as another person's independent approval.

Rollback is a reviewed repository revert; no server rollback is involved.

Tracking: https://github.com/321Team/fds-project-baseline/issues/24
