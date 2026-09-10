# FDS Project Baseline

Private canonical repository for the FDS hybrid cloud project's approved baseline, WBS/Gantt, ticket pack, release records, WEB snapshot and integrity audits.

## Source-of-truth rule

- `main` contains only approved `RELEASED` document baselines.
- `release/vX.Y.Z` prepares one candidate release through review.
- A release is canonical only after independent PR approval, the exact-HEAD review gate, manual merge by an approved operator, manifest verification and SHA-256 verification. If technical branch protection or Actions is unavailable, use the approved Free-plan compensating controls in `governance/RELEASE_POLICY.md`; do not claim protected `main` or CI PASS.
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

## Ticket property synchronization

문서 정본, 실행 기록과 GitHub 메타데이터는 구분한다. 같은 표가 있다고 실제 Issue Type·Label·Assignee·Milestone이 설정된 것은 아니다. 검색 결과의 `null`도 미설정 증거가 아니므로 전체 Issue 응답으로 검증한다.

- 계획·Scope·일정 정본: 승인된 `baseline/`, `wbs/`, `tickets/`와 승인 변경 기록. 최신 실행 결과는 근거가 있는 Issue·리뷰·증적에 기록하고 다음 정본 후보에 인계한다.
- GitHub Issues: 티켓 실행·협업 기록. 메타데이터는 확인된 본문 속성의 검색·배정용 표현이다. 본문과 메타데이터를 임의의 양방향 정본으로 사용하지 않는다.
- Notion: 승인된 속성과 Description의 협업·표시 대상. GitHub 속성 동기화가 Notion 원격 수정 완료를 뜻하지 않는다.
- 식별 키: `Record ID`. 저장소+Issue 번호는 대상을 찾는 주소다. 제목·번호만으로 Upsert하지 않는다. 기존 migration marker를 보존한다.
- 기존 17개 속성, 풀네임 Lead/Support, Description, 댓글, AC, 승인·종결 기록을 보존한다. `원본 속성 미확인`은 추정하지 않고 예외 처리한다.

| 본문 속성 | GitHub 표현 | 통제 |
|---|---|---|
| Phase / Category / Priority | `phase:*` / `area:*` / `priority:*` | 기존 명칭과 대소문자 유지 |
| Type | 실제 Issue Type + `type:*` 보조 라벨 | 정확히 일치하는 사용 가능 Type만 적용. 미지원 시 Label fallback을 명시 |
| Status | Issue state + `status:*` | Done/Cancelled 구분. 동기화만으로 close/reopen하지 않음 |
| Lead | 확인된 GitHub Assignee | 기존 유효 배정 보존. 정본 승인 권한과 구분 |
| Support | 본문 풀네임 | 자동 Assignee 추가·PR Reviewer 요청 없음 |
| Start / End / 기간 | 본문 및 WBS/Notion | 실제 완료일과 계획일 구분. 일정·휴가·기간 재계산 없음 |
| Milestone | 실제 GitHub Milestone | 확정된 단일 매핑만 적용. 누락·복수 Gate·날짜 충돌은 HOLD |
| Exit Criteria / Decision·Risk / Source | 본문과 승인·증적 링크 | 의미·체크·PASS를 자동 생성하지 않음 |

### 정책과 실행

- [동기화 정책](governance/TICKET_SYNC_POLICY.md)
- [라벨·Type 사전](governance/GITHUB_LABEL_SCHEMA.md)
- [마일스톤 매핑](governance/GITHUB_MILESTONE_MAP.md)
- [실명·계정과 권한 경계](governance/GITHUB_IDENTITY_MAP.md)
- [기계 판독 매핑](governance/ticket-sync-map.json)
- [검증·실행 Runbook](governance/TICKET_SYNC_RUNBOOK.md)

GitHub Issue 작업에는 Ansible 실행이 필요하지 않다. `gh api`는 저장소를 명시하므로 어느 디렉터리에서도 가능하다. 아래 스크립트의 상대 경로는 **이 저장소 체크아웃 루트** 기준이며 `infra-ansible`에서 실행할 명령이 아니다.

```bash
python3 scripts/ticket-sync.py --help
python3 -m unittest discover -s tests -p 'test_ticket_sync.py'
```

기본 흐름은 전체 조회 → Record ID/17개 속성 검증 → 차이 계획 → 명시적 Apply → 재조회다. 재실행 시 차이가 없으면 쓰지 않는다. 실제 Type·Milestone이 미설정이거나 원본 미확인 값이 남으면 결과는 `PARTIAL`이며 완전 동기화 PASS로 선언하지 않는다.

README·정책 보완은 PR #69의 승인·내용 병합에 포함됐다. 최종화 PR·Tag·배포 Asset 검증을 거쳐 문서 정본을 발행하며 Runtime 완료 상태는 해당 증적으로 별도 판정한다.

## v3.1.18 통합 후보

현재 발행 정본은 `CURRENT.md`의 v3.1.17이다. v3.1.18은 누적 이력 통합과 티켓 최신화를 준비한 후보이며 운영 완료 승인으로 사용하지 않는다.

- [Baseline 후보](baseline/FDS_Project_Implementation_Baseline_v3.1.18.md)
- [WBS/Gantt 55건](wbs/FDS_v3.1.18_WBS_and_Gantt_v1.0.xlsx)
- [64개 티켓 Description 후보](tickets/FDS_v3.1.18_Canonical_Ticket_Update_Pack_v1.0.md)
- [변경·출처·인수 조건 대장](releases/v3.1.18/FDS_Canonical_Consolidation_Record_v3.1.18.md)
- [Release Notes](releases/v3.1.18/FDS_Project_Implementation_Baseline_Release_Notes_v3.1.18.md)
- [배포 Manifest](releases/v3.1.18/FDS_Document_Distribution_Manifest_v3.1.18.md)
- [무결성 감사](audit/FDS_Canonical_Integrity_Audit_v3.1.18.md)

순서는 정본 리뷰·명시적 merge 승인·발행 → 실제 티켓 Description 최신화 → 새 속성 map/plan 생성·적용이다. 현재 `governance/ticket-sync-map.json`은 이전 본문을 대상으로 만든 이력이며 v3.1.18 Description 적용 후 그대로 사용하지 않는다. `canonical-records.json`은 문서 원본이지 apply 계획이 아니다. 본문의 최신 실행 기록, 기존 migration marker, 댓글·AC·승인 기록은 후속 갱신에서도 보존한다.

로컬 후보 검증과 ZIP 재생성:

```bash
python3 scripts/verify-v18-candidate.py
python3 scripts/build-canonical-package.py v3.1.18 /tmp/fds-v18-package
FDS_RELEASE_ZIP=/tmp/fds-v18-package/FDS_v3.1.18_Canonical_Baseline_Release_Package.zip RELEASE_VERSION=v3.1.18 bash scripts/verify-canonical-release.sh
```

이 명령들은 Release 발행이나 GitHub 티켓 변경을 수행하지 않는다. `governance/RELEASE_POLICY.md`의 독립 리뷰·정확한 HEAD 승인·최종 발행 Gate를 그대로 적용한다.

추가 유입: 이하영 09-10 면접 휴가(09-08 유지), P1-SEC 기존 계획창 가용 작업일 4일(권장 종료 09-21 창은 10일), ICR/K8S Worker·NTP 검토 및 PR #2 리뷰 요청 상태를 후보에 반영했다. 상세 원문은 `audit/v3.1.18/followup-20260910.json`을 참조한다.

Fast Tracking 권장안은 [일정 변경안](releases/v3.1.18/FDS_Phase1_Fast_Track_Schedule_Recommendation_v1.0.md)과 WBS의 `Fast Track Plan` 시트에 반영했다. 주말 작업 가용량 0, 개인 부재 반영, 총 23인일 중 1.5인일 버퍼다. 이는 metadata 자동 동기화의 일정 변경 금지 규칙과 별개인 사용자 요청 기반의 계획 변경 후보다. 문서 내용은 PR #69에서 승인·병합됐다. 정식 게시와 실제 실행 승인은 별도 절차로 추적한다.

K8S 최신 이력은 [후보 통합 기록](releases/v3.1.18/FDS_K8S_Candidate_Integration_20260910.md)을 참조한다. Worker 보완·PR #3 병합, PR #2 현장 모의/읽기 전용 검증, PR #4 Runtime 전용 보완을 동기화했으며 전체 Runtime 인수는 미완료다.

## v3.1.18 발행 이력

[릴리즈 최종화 기록](releases/v3.1.18/FDS_Release_Finalization_Record_v3.1.18.md)과 `CURRENT.md`에서 현재 발행 단계를 확인한다. PR #69 승인 HEAD `04c1ca46dcf82f814d350b4d49539e3ba4d6a9b4`와 내용 병합 `02be2150f7662319a3d796cdcb99f6d26aec5472`를 고정했다. 후보 원문·감사·Description 적용 입력은 당시 기록으로 보존하며, 그 안의 CANDIDATE/미발행 표시는 해당 수집·작성 시점의 상태다.
