# Current Canonical Release

최종화 PR 병합 후 적용하는 정본 메타데이터다. 승인된 내용·최종화 병합·체크섬 기준 RELEASED이며 실제 GitHub 게시 완료는 Release API의 published_at과 네 Asset 검증으로 확인한다.

| Field | Value |
|---|---|
| Canonical document version | v3.1.22 / RELEASED after reviewed finalization merge |
| Source snapshot | 2026-10-19 / 78 records · 발행 전 freshGET 실질차이0 |
| Input integration merge | `caa13c1839b31675794abd1ca9c1071376561643` / PR191 |
| Approved content HEAD | `ccf4c2fd5d9d0cc6ff24694e6f11d437e6b309d1` |
| Content merge | `881a38bd79b3f7c92ac3b68b528bf20e454d1da7` / PR192 |
| Review authority | 정본 Lead 이권욱 / 문서전용 최신HEAD검토·사용자 발행 지시 |
| Earlier independent reviews | PR191 원HEAD bcade180 범위: 이하영·이재환 APPROVED; 후속정정/발행은 Lead검토 |
| Finalization authority | 사용자 실제 docs-v3.1.22 발행 지시(2026-10-19 KST) |
| Canonical release tag | `docs-v3.1.22` — 최종화 merge commit으로 Tag API에서 확인 |
| Publication | 미리 완료로 기록하지 않음. Release API published_at·4 Asset 해시·published 검증이 최종근거 |

- [Release](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.22)
- [최종화 기록](releases/v3.1.22/FDS_Release_Finalization_Record_v3.1.22.md)
- [Baseline](baseline/FDS_Project_Implementation_Baseline_v3.1.22.md) · [WBS](wbs/FDS_v3.1.22_WBS_and_Gantt_v1.0.xlsx) · [Ticket Pack](tickets/FDS_v3.1.22_Canonical_Ticket_Update_Pack_v1.0.md) · [WEB](web/v3.1.22/status-snapshot.html)
- [원 조건과 잔여위험](tickets/v3.1.22/SIGNOFF_CLOSE_REVIEW.md) · [실제 Signoff/Close](tickets/v3.1.22/SIGNOFF_CLOSE_CURRENT.md)

Phase1 조건부 최종 Signoff/Close·기존 RA/KI/Owner/재검토·보호보관·#25~27 Phase2 구현ToDo/고정Due미배정을 보존한다. P2 #34 확정사양/작성시점운영스냅샷은 새 Runtime GO가 아니다. 전체기술PASS·새시스템Critical0·새서버/계정/보안 변경·P2실행을 이 발행으로 부여하지 않는다.

## Preserved publication history

기존 docs-v3.1.21/Tag/Assets/과거 정본은 변경하지 않는다. inputs/와 audit/의 후보·미발행·당시미완료 문구는 당시 원문이다. 실제 새 Release 게시/배포 검증 전까지 이전 게시본도 계속 보존한다.
