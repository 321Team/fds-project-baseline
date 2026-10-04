# FDS Project Baseline

Private canonical repository for the FDS hybrid cloud project's approved baseline, WBS/Gantt, ticket pack, release records, WEB snapshot and integrity audits.

이 저장소는 **비공개 정본**이다. 공개 팀 소개는 Organization 프로필(`321Team/.github`의 `profile/README.md`)을 사용한다. 이 README는 내부 개발·문서 정책을 찾는 입구이며, 정책 본문은 `governance/`와 승인된 Release Tag가 정본이다.

## 프로젝트와 팀 (내부)

321Team은 [코오롱 베니트] 하이브리드 클라우드 컨테이너 플랫폼 설계 및 구현 9기 과정 팀이다. 대상 서비스는 On-prem 가상화 + Kubernetes 기반 하이브리드 컨테이너 플랫폼 위의 FDS(`transaction-api`, `fds-engine`)이다.

최종화된 문서 정본은 **v3.1.21**이며 `CURRENT.md`와 태그 `docs-v3.1.21`을 우선한다. 실제 게시 완료는 Release 페이지/API와 Asset 검증 기록으로 확인한다. `main` HEAD가 태그보다 앞설 수 있으며, 문서 인용은 태그/Release를 기준으로 한다.

> v3.1.20 태그 주의: `docs-v3.1.20`은 최종화 병합이 아니라 내용 병합 `3364465`(PR #87)를 가리킨다. 그래서 태그 시점의 `CURRENT.md`에는 v3.1.19가 표시된다. v3.1.20 발행 메타데이터는 최종화 `9f57e69`(PR #91) 이후 main의 `CURRENT.md`를 기준으로 한다. 발행 후 정정 사항은 [v3.1.20 발행 후 정정 기록](audit/canonical-followup-20260923/README.md)을 따른다.

| 실명 | GitHub | 업무 | 정본 권한 경계 |
|---|---|---|---|
| 이하영 | `hayeounglee` | 정본 리뷰·독립 승인, 품질 검증 | 정본 리뷰·승인 규칙 적용 |
| 이재환 | `supreme33-kr` | Application / Data / Monitoring / QA | 정본 승인·리뷰·병합·발행 역할 제외 |
| 이권욱 | `GWONUK` | PMO·인프라 구현, 정본 운영 | 정본 운영·승인 규칙 적용 |

근거: `governance/GITHUB_IDENTITY_MAP.md` (정본 태그 `docs-v3.1.20`). Issue Assignee가 있다고 정본 파일 승인 권한이 생기지는 않는다.

## 개발·문서 정책 색인

정책 원문은 아래 파일을 수정하지 않고 인용한다. README 요약과 원문이 다르면 원문과 최신 승인 변경이 우선한다.

| 주제 | 정본 위치 |
|---|---|
| 정본 브랜치·발행·checksum | [RELEASE_POLICY.md](governance/RELEASE_POLICY.md) |
| 리뷰 권한·독립 승인 범위 | [REVIEW_AUTHORITY_POLICY.md](governance/REVIEW_AUTHORITY_POLICY.md) |
| 실명·GitHub 계정·권한 경계 | [GITHUB_IDENTITY_MAP.md](governance/GITHUB_IDENTITY_MAP.md) |
| 티켓 속성 동기화 | [TICKET_SYNC_POLICY.md](governance/TICKET_SYNC_POLICY.md) |
| 라벨·Issue Type | [GITHUB_LABEL_SCHEMA.md](governance/GITHUB_LABEL_SCHEMA.md) |
| Milestone 매핑 | [GITHUB_MILESTONE_MAP.md](governance/GITHUB_MILESTONE_MAP.md) |
| 티켓 동기화 실행 | [TICKET_SYNC_RUNBOOK.md](governance/TICKET_SYNC_RUNBOOK.md) |
| Projects 보드 동기화 | [PROJECT_SYNC_RUNBOOK.md](governance/PROJECT_SYNC_RUNBOOK.md) |
| 현재 발행 메타데이터 | [CURRENT.md](CURRENT.md) |

핵심 운영 규칙(요약, 원문 대체 아님):

- `main`에는 승인된 RELEASED 문서만 둔다. 직접 `main` push를 금지한다.
- 변경은 release/작업 브랜치와 Pull Request로만 제출한다.
- 문서 정본 발행과 Runtime/Gate 인수는 별개다. CI 미실행을 CI PASS로 쓰지 않는다.
- 비밀·개인키·비밀번호를 저장소와 산출물에 넣지 않는다.
- 계획일과 실제 완료일, STATIC/MOCK/CI/RUNTIME/REVIEW/MERGE/PUBLICATION을 구분한다.

## Source-of-truth rule

- `main` contains only approved `RELEASED` document baselines.
- `release/vX.Y.Z` prepares one candidate release through review.
- A release is canonical after the responsible Lead's exact-HEAD decision, manual merge by an authorized operator, manifest verification and SHA-256 verification. Independent review is required only when the PR includes code or executable configuration changes; documentation-only PRs, finalization and publication are delegated to the canonical Lead. Follow [REVIEW_AUTHORITY_POLICY](governance/REVIEW_AUTHORITY_POLICY.md) and the compensating controls in `governance/RELEASE_POLICY.md`; do not claim protected `main` or CI PASS when unavailable.
- Project-wide exception: every PR in `fds-project-evidence` retains independent review, including documentation/evidence-only changes. This does not add independent approval to each Runtime step in other repositories.
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
| `retrospectives/` | 팀 회고·강사 피드백 기록. v3.1.21 Manifest/체크섬에 참고 이력으로 편입; AC 자동 승격 없음 |
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

## 발행 이력

| 버전 | Tag | 핵심 기록 |
|---|---|---|
| v3.1.20 (이전 발행) | `docs-v3.1.20` → `3364465` (내용 병합 PR #87; 최종화 PR #91 `9f57e69`는 태그 이후) | [Release 디렉터리](releases/v3.1.20/), [Release Notes](releases/v3.1.20/FDS_Project_Implementation_Baseline_Release_Notes_v3.1.20.md), [Manifest](releases/v3.1.20/FDS_Document_Distribution_Manifest_v3.1.20.md), [무결성 감사](audit/FDS_Canonical_Integrity_Audit_v3.1.20.md), [발행 후 정정 기록](audit/canonical-followup-20260923/README.md) |
| v3.1.19 | `docs-v3.1.19` → `966fc53` (최종화 PR #79) | [최종화 기록](releases/v3.1.19/FDS_Release_Finalization_Record_v3.1.19.md), [Release Notes](releases/v3.1.19/FDS_Project_Implementation_Baseline_Release_Notes_v3.1.19.md) |
| v3.1.18 | `docs-v3.1.18` → `72599ae` | [최종화 기록](releases/v3.1.18/FDS_Release_Finalization_Record_v3.1.18.md). PR #69 승인 HEAD `04c1ca46dcf82f814d350b4d49539e3ba4d6a9b4`, 내용 병합 `02be2150f7662319a3d796cdcb99f6d26aec5472` |
| v3.1.17 | `docs-v3.1.17` → `2d93395` | [Release Notes](releases/v3.1.17/FDS_Project_Implementation_Baseline_Release_Notes_v3.1.17.md) |

각 버전의 후보 원문·감사·Description 적용 입력은 당시 기록으로 보존한다. 그 안의 CANDIDATE/미발행 표시는 해당 수집·작성 시점의 상태다.

후보 로컬 검증과 ZIP 재생성(버전은 대상 후보로 바꾼다):

```bash
bash scripts/verify-canonical-release.sh
python3 scripts/build-canonical-package.py vX.Y.Z /tmp/fds-package
FDS_RELEASE_ZIP=/tmp/fds-package/FDS_vX.Y.Z_Canonical_Baseline_Release_Package.zip RELEASE_VERSION=vX.Y.Z bash scripts/verify-canonical-release.sh
```

이 명령들은 Release 발행이나 GitHub 티켓 변경을 수행하지 않는다. 현재 승인 절차는 [Lead 위임 정책](governance/REVIEW_AUTHORITY_POLICY.md)을 적용한다.
