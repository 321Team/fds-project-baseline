# P1-HBR-01 — Harbor / Trivy Registry

> v3.1.19 CANDIDATE / NOT RELEASED · 2026-09-17 20:28 KST

## 현행 속성

| Property | 입력값 |
|---|---|
| Record ID | P1-HBR-01 |
| Phase | Phase 1 |
| Category | Registry / Supply Chain |
| Type | Task |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-08-31 |
| End | 2026-09-17 |
| Calendar Days | 18 |
| Working Days | 12 |
| Lead | 이하영 |
| Support | 이권욱 |
| Exit Criteria | harbor01 `.54:443`, Private CA Trust, 최소권한 Robot Account, IF-09 Runner Push·IF-10 Worker Pull/Pod Start, 비승인 Push/Pull DENY, Trivy/Digest/Evidence PASS |
| Related Decision IDs | D04; D17; D19; D35 |
| Related Risk IDs | RISK-04; RISK-06; RISK-07 |
| Source | Baseline v3.1.19 CANDIDATE; GitHub #13 @ 2026-09-17T08:44:13Z; 원문 SHA256 8a5159fa6aecafdb1c61652bd0be2a234fa3b9792c53e910eeb39d6a17b400ff |
| Schedule Note | Harbor 준비는 CP 후속과 병행하고 09-16 CI Scan Digest까지 4/4 대조 후 09-17 인수 목표다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |

## 상태와 인수 경계

HBR 수정 PR #2 병합은 코드 편입이다. Worker Pull-only Robot·유한 만료·인증서/Scanner·소비자별 Runtime 인수는 책임 티켓의 실제 증적으로 구분한다.

- GitHub lifecycle: open; Milestone: G1 Infrastructure Ready
- 일정은 조정 가능한 계획이며 실제 완료일·Gate 승인일과 구분한다.
- 원문·후속 댓글: [원본 티켓](https://github.com/321Team/fds-project-baseline/issues/13), [고정 수집본](../sources/issue-13.json).
- 상위 속성표는 이 후보의 현행 표다. 아래 원문은 수집 시점의 변경/승인/AC 이력이며 과거 버전 문구를 현재 발행 상태로 사용하지 않는다.

## 원문 보존

<details>
<summary>수집한 GitHub 본문 전체 — SHA256 8a5159fa6aecafdb1c61652bd0be2a234fa3b9792c53e910eeb39d6a17b400ff</summary>

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 30일 Robot·Scanner·Critical/High 정책은 결정됨. 구현 잔여·정본 반영·Runtime 증거 ; R01/R03.

- HBR-AC05의 CI Workflow/Source SHA·Run ID/Attempt·CI Scan Digest·Negative Gate/Push·Manifest Digest patch/이전 승인 Digest 복구는 #16의 기존 책임이다. Harbor 측 Scanner/Robot/Registry 증적과 4/4 Traceability로 연결한다.

**Harbor/CA/CICD 결정 동기화 (R01)** — Robot Never 미채택·유한30일, Scanner 유지, 미해결 Critical/High의 Push/Deploy 차단과 오류 실패/미검증 처리는 9/14 사용자 결정이다. 예외는 CVE/Digest/사유/만료/승인자로 기록한다. ca01의 server01·2vCPU/4GiB·OS40GiB+CA2GiB LUKS2와 PR준비안 OS20GiB의 차이를 As-built에 남긴다. 새 Root 선택과 실제 발급을 구분하며 별도 암호화 백업/복구는 Harbor 적용·trust 배포 전에 확인한다.
근거: [Harbor 정책](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5659049448) · [CICD 정책](https://github.com/321Team/fds-project-baseline/issues/16#issuecomment-5659051242) · [CA 진행 #16](https://github.com/321Team/fds-project-baseline/issues/16)

**인계·관련 티켓:** [#16](https://github.com/321Team/fds-project-baseline/issues/16) · [#19](https://github.com/321Team/fds-project-baseline/issues/19).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:P1-HBR-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P1-HBR-01 -->
# P1-HBR-01 — Harbor / Trivy Registry

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P1-HBR-01 |
| Phase | Phase 1 |
| Category | Registry / Supply Chain |
| Type | Task |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-08-31 |
| End | 2026-09-17 |
| Calendar Days | 18 |
| Working Days | 12 |
| Lead | 이하영 |
| Support | 이권욱 |
| Exit Criteria | harbor01 `.54:443`, Private CA Trust, 최소권한 Robot Account, IF-09 Runner Push·IF-10 Worker Pull/Pod Start, 비승인 Push/Pull DENY, Trivy/Digest/Evidence PASS |
| Related Decision IDs | D04; D17; D19; D35 |
| Related Risk IDs | RISK-04; RISK-06; RISK-07 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #13 snapshot 2026-09-10T03:15:50Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청 |
| Schedule Note | Harbor 준비는 CP 후속과 병행하고 09-16 CI Scan Digest까지 4/4 대조 후 09-17 인수 목표다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **In Progress / open**. 원본 갱신 시각: `2026-09-11T00:11:53Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.
- 수집된 운영 댓글은 원래 위치에 보존한다. 신규 구현 제출/리뷰 요청은 실행 PASS나 승인으로 간주하지 않는다.
  - [5612005674](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5612005674) · 2026-09-10T03:02:54Z
  - [5612102303](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5612102303) · 2026-09-10T03:15:50Z
  - [5627287809](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5627287809) · 2026-09-11T00:11:42Z
  - [5627289520](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5627289520) · 2026-09-11T00:11:52Z
- 최신 제출본의 후속 검토와 Runtime 인수는 계속 별도 진행한다. 기존 6개 Runtime AC와 완료 HOLD를 유지한다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

구현 절차 및 6차 리뷰 후속 보완 착수로 In Progress. Runtime AC는 PASS 0 / FAIL 0 / NOT VERIFIED 6, 완료 HOLD. AC-05는 CI Scan Digest·Harbor Artifact·Manifest image@sha256·Pod imageID 4개 동일성으로 검증하고 CI 산출물은 P1-CICD에서 인수한다. Harbor Scanner 제외/CI-only 전환, Robot Token Never와 미확정 Threshold는 승인 대기 제안이다. 현재 후보 Plan: 2026-08-31 ~ 2026-09-17 (권장안; 실제 완료일·Gate 승인은 미확정).

근거: [Issue #13](https://github.com/321Team/fds-project-baseline/issues/13), Issue 갱신 시각 `2026-09-10T03:15:50Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 일정 권장안

Start/End는 이번 Fast Tracking 후보의 계획값이다. 기존 승인 일정은 `audit/v3.1.18/fast-track-plan.json`에 전후 값으로 보존한다. 실제 착수·완료·Status·AC·승인을 변경한 것이 아니다. 교육장 주말 작업은 없으며 세부 AM/PM 배정과 선행 조건을 따른다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- [후속 기록](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5612005674)
- [후속 기록](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5612102303)

---

### User Story

Registry 담당자 이하영으로서 Private CA로 보호된 Harbor/Trivy와 최소권한 계정을 제공해 Runner의 승인 Image Push와 Worker의 검증된 Pull/Pod Start를 보장한다.

### Scope

#### In Scope

- harbor01 `10.1.93.54:443`, 서비스 전용 Leaf 인증서와 Consumer CA Trust
- CI/CD Push+Pull Robot Account와 Worker Pull-only Credential 분리
- IF-09 `runner .20 → harbor01 .54:443` Positive/Negative
- IF-10 `Worker .105/.107/.108 → harbor01 .54:443` Pull/Pod Start와 Push DENY
- Trivy 결과, Image Digest Pinning, Credential 회전·마스킹 Evidence
- OID-02 CP/Calico/kube-system Image Registry Source 결정 지원

#### Out of Scope

- Harbor HA — Phase 1 Scope Out, P2 별도 검토
- 실제 Harbor Backup/Restore — P1-DR-02
- P2 ROSA Image Source — D22/P2 Decision
- 결정 전 Control Plane Source를 IF-10에 임의 포함

### 핵심 요구사항

- [ ] TLS 1.2 이상, hostname/SAN/Chain 검증과 우회 금지
- [ ] Runner `.20` Source 보존 및 인증 Push/Pull PASS
- [ ] Worker 3대 Pull/Pod Start PASS와 Push DENY
- [ ] 비승인 Source·잘못된 CA·잘못된 Credential DENY
- [ ] Robot Account 권한·회전·Secret 저장 경계 준수
- [ ] Trivy 결과와 배포 Digest 일치
- [ ] OID-02를 P1-K8S Gate 1 전 결정

### Acceptance Criteria

- [ ] Harbor Service/Health와 Certificate Chain PASS
- [ ] IF-09 Positive/Negative PASS
- [ ] IF-10 Pull/Pod Start 및 Push DENY PASS
- [ ] 실제 Source IP와 Host Firewall Allowlist 일치
- [ ] Image Digest·Scan 결과·Credential fingerprint Evidence 확보
- [ ] 비밀정보 평문 미포함

### 검증 및 증적

- `docs/evidence/P1-HBR-01/`
- TLS Chain/SAN, Login, Push/Pull, Trivy, Digest, Negative, Rotation, Rollback 및 `99_SHA256SUMS.txt`

### Dependency

- Blocked By Runtime: Network/Linux 기반, D19 Private CA; Worker Pull은 P1-K8S Node 준비
- Blocks / Next: P1-CICD-01 Delivery, P1-K8S/APP/MON Image Pull, G1 Infrastructure Ready
- Related: P1-SEC-01 Credential/RBAC, P1-DR-02 Harbor Restore

### Decision / Risk Control

- Decision: D19의 Private Root CA + Harbor 전용 Leaf + Consumer CA Trust를 구현한다.
- Risk Control: `insecure`/검증 우회를 금지하고 Push·Pull Identity를 분리한다. OID-02 전에는 CP Source를 허용하지 않는다.

### Review / Handoff

- Review Owner: 이권욱
- Handoff: CA Bundle, Repository, Robot Account Scope, Digest와 Pull 예시를 P1-K8S/P1-CICD/P1-APP/P1-MON에 전달한다.

<!-- p1-hbr-r6-sync:start -->
## 2026-09-10 — 6차 리뷰 및 AC-05 책임 경계 동기화

### 리뷰 판정

| 항목 | 현재 판정 |
|---|---|
| 종합 결과 | **HOLD / NOT READY** |
| Ticket 상태 | **In Progress / Open** |
| AC 집계 | **PASS 0 / FAIL 0 / NOT VERIFIED 6** |
| 완료 전환 | Runtime 원본 증적과 AC Matrix가 확보되기 전 `In Review` 또는 `Done` 전환 금지 |

상태관리상 Harbor 자체 구현·보완은 선행 티켓과 독립적으로 진행할 수 있으므로 `In Progress`로 전환한다. AC-05의 P1-CICD-01 의존성과 Runtime 증적 미확보는 착수 차단이 아니라 완료 차단이다.

문서와 검증 절차가 개선된 사실은 확인했지만, 실행 결과를 대신하지 않는다. `FAIL 0`은 Acceptance Criteria 통과를 의미하지 않는다.

### Acceptance Criteria 상태

| AC | 검증 대상 | 상태 | 미충족 또는 선행조건 |
|---|---|---|---|
| AC-01 | Harbor Service/Health 및 TLS Chain/SAN | NOT VERIFIED | 실제 Health, Chain, 재기동 복구 원본 증적 필요 |
| AC-02 | IF-09 Runner Push/Pull 및 음성시험 | NOT VERIFIED | Runner Runtime과 Source IP 증적 필요 |
| AC-03 | IF-10 Worker 3대 Pull/Pod Start 및 Push DENY | NOT VERIFIED | `.105/.107/.108` 각각의 Runtime 증적 필요 |
| AC-04 | 실제 Source IP와 Host Firewall Allowlist | NOT VERIFIED | IF-16 Route Drift 해소 또는 승인 예외와 도착지 로그 필요 |
| AC-05 | Scan/Harbor/Manifest/Pod Digest Traceability | **BLOCKED / NOT VERIFIED** | [P1-CICD-01 #16](https://github.com/321Team/fds-project-baseline/issues/16)의 CI/Trivy 산출물 필요 |
| AC-06 | Credential 비노출 및 Evidence 무결성 | NOT VERIFIED | Worker argv 노출 제거, Rotation/Fingerprint, Secret Scan, SHA-256 검증 필요 |

### AC-05 책임 경계

- **P1-CICD-01 — 이권욱:** Workflow/Source Commit SHA, Run ID/Attempt, CI Trivy 실행 결과와 Scan Digest, Negative Gate, Push 제어, 배포 Digest patch 및 이전 승인 Digest 복구 산출물을 생성·제공한다.
- **P1-HBR-01 — 이하영:** Harbor Service/Scanner·Registry 정책, Harbor Artifact Digest, Robot Account/CA/Worker Pull 경계의 실행 증적을 수집하고 P1-CICD-01 산출물을 인수·검증한다.
- **공동 산출:** 아래 4개 값의 동일성을 한 Review Run 기준으로 대조하고 Rollback 후 Pod Start/Health를 재검증한다.
  1. CI/Trivy Scan Digest
  2. Harbor Artifact Digest
  3. 배포 Manifest의 `image@sha256` Digest
  4. 실행 Pod의 `containerStatuses[].imageID`

`LOCAL_DIGEST ↔ HARBOR_DIGEST` 2-way 비교는 보조 사전점검으로 유지할 수 있으나 AC-05 PASS 또는 CI Scan Digest를 대체하지 않는다. CI 산출물이 제공되기 전에는 P1-HBR-01에서 값을 임의 생성하지 않고 `BLOCKED BY #16 / NOT VERIFIED`로 관리한다.

Harbor Trivy Scanner 서비스 확인과 CI Trivy Scan 실행은 서로 다른 책임이다. 정본이 요구하는 Harbor Scanner 항목은 P1-HBR-01에서 유지하며, CI-only 모델 또는 Harbor Scanner 제외는 Scope/AC 변경 승인 전까지 `Proposed / Approval Pending`이다.

### 6차 리뷰 후속 조치

- [ ] Worker Push DENY 시험의 `ctr --user` argv Credential 노출 제거 — 권장안: `nerdctl --password-stdin`
- [ ] Runner/Worker/Control Plane 간 동일 Review Run Metadata를 무결성 검증 가능한 형태로 인계
- [ ] `fds-app` Restricted PSA, Pull Secret, 명시적 non-root UID/GID 및 Pod cleanup 실제 검증
- [ ] TLS Negative Test를 정상 CA 선행 성공 + 잘못된 CA의 정확한 `curl` Exit Code 60으로 판정
- [ ] Worker 3대별 Pull/Pod/Push DENY, 실제 Source IP 및 Firewall 원본 증적 확보
- [ ] 4/4 Digest Traceability 및 이전 승인 Digest Rollback/Health 증적 확보
- [ ] Credential Rotation/Fingerprint, Secret Scan, `AC_Evidence_Matrix.md`, `99_SHA256SUMS.txt` 제출

### 비차단·승인 대기 항목

- Retention/GC는 Optional / Non-blocking이며 보호 Digest와 Rollback 보존 기준 확정 후 적용한다.
- Robot Token `Never`, Trivy Threshold, Harbor Scanner 제외는 승인 전까지 완료 근거로 사용하지 않는다.
<!-- p1-hbr-r6-sync:end -->

---

### Completion Record

- Result: 6차 리뷰 HOLD — 구현 절차 보완 중 / Runtime Not Verified
- Status: In Progress
- Completed Date: 미입력
- Reviewer / Approver: 이권욱(6차 리뷰) / 미승인

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `01eb9372348a27ff51da1edd97fa9c1a77c5390a63b7aea020c0e078e4c4293e`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P1-HBR-01 -->
# P1-HBR-01 — Harbor / Trivy Registry

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P1-HBR-01 |
| Phase | Phase 1 |
| Category | Registry / Supply Chain |
| Type | Task |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-08-31 |
| End | 2026-09-04 |
| Calendar Days | 5 |
| Working Days | 5 |
| Lead | 이하영 |
| Support | 이권욱 |
| Exit Criteria | harbor01 `.54:443`, Private CA Trust, 최소권한 Robot Account, IF-09 Runner Push·IF-10 Worker Pull/Pod Start, 비승인 Push/Pull DENY, Trivy/Digest/Evidence PASS |
| Related Decision IDs | D04; D17; D19; D35 |
| Related Risk IDs | RISK-04; RISK-06; RISK-07 |
| Source | Baseline v3.1.15; DEC-P1-TLS-01/D19; D-SEC-01 Security Design Baseline v1.0; D35; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 이하영 08-28 휴가를 반영해 08-31 시작한다. TLS 결정 D19를 선행한다. Harbor HA는 P2, 실제 Backup/Restore는 P1-DR-02 범위다. |

## 이관 기준 및 확인 사항

- 속성의 일정·담당·상태는 RELEASED v3.1.17 WBS(기준일 2026-09-04)를 우선 반영했다. 이후 별도 근거가 있는 변경만 아래에 명시한다.
- v3.1.17 WBS의 `To Do`는 당시 상태 스냅샷이다. 2026-09-10 기준 구현 절차 작성과 6차 리뷰 후속 보완의 실제 착수를 확인하여 `In Progress`로 전환했다. Runtime Acceptance는 계속 미검증 상태다.
- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) · [정본 WBS](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/wbs/FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx).
- 본문은 아래에 적힌 원본 버전의 기록이다. 위 속성·후속 승인과 다른 과거 상태는 현재 판정으로 사용하지 않는다. 이관 자체로 미실행 AC를 체크하거나 새 승인을 부여하지 않는다.
- Lead/Support의 풀네임은 본문 속성으로 보존한다. GitHub 계정 대응이 확인되지 않은 사람에게 자동 배정하지 않았다.

## 원본 및 변경 출처

- `FDS_Notion_Remaining_Backlog_Manual_v1.9.md`
- `FDS_v3.1.15_Canonical_Ticket_Update_Pack_v1.0.md`
- `FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx`

---

## Description — 보관 입력본

> 원본: `FDS_v3.1.15_Canonical_Ticket_Update_Pack_v1.0.md`. 원본의 완료/미완료 체크와 당시 이력을 보존했다.

### 🎯 User Story

Registry 담당자 이하영으로서 Private CA로 보호된 Harbor/Trivy와 최소권한 계정을 제공해 Runner의 승인 Image Push와 Worker의 검증된 Pull/Pod Start를 보장한다.

### 📌 Scope

#### In Scope

- harbor01 `10.1.93.54:443`, 서비스 전용 Leaf 인증서와 Consumer CA Trust
- CI/CD Push+Pull Robot Account와 Worker Pull-only Credential 분리
- IF-09 `runner .20 → harbor01 .54:443` Positive/Negative
- IF-10 `Worker .105/.107/.108 → harbor01 .54:443` Pull/Pod Start와 Push DENY
- Trivy 결과, Image Digest Pinning, Credential 회전·마스킹 Evidence
- OID-02 CP/Calico/kube-system Image Registry Source 결정 지원

#### Out of Scope

- Harbor HA와 실제 Backup/Restore — P1-DR-02
- P2 ROSA Image Source — D22/P2 Decision
- 결정 전 Control Plane Source를 IF-10에 임의 포함

### 📋 핵심 요구사항

- [ ] TLS 1.2 이상, hostname/SAN/Chain 검증과 우회 금지
- [ ] Runner `.20` Source 보존 및 인증 Push/Pull PASS
- [ ] Worker 3대 Pull/Pod Start PASS와 Push DENY
- [ ] 비승인 Source·잘못된 CA·잘못된 Credential DENY
- [ ] Robot Account 권한·회전·Secret 저장 경계 준수
- [ ] Trivy 결과와 배포 Digest 일치
- [ ] OID-02를 P1-K8S Gate 1 전 결정

### ✅ Acceptance Criteria

- [ ] Harbor Service/Health와 Certificate Chain PASS
- [ ] IF-09 Positive/Negative PASS
- [ ] IF-10 Pull/Pod Start 및 Push DENY PASS
- [ ] 실제 Source IP와 Host Firewall Allowlist 일치
- [ ] Image Digest·Scan 결과·Credential fingerprint Evidence 확보
- [ ] 비밀정보 평문 미포함

### 🧪 검증 및 증적

- `docs/evidence/P1-HBR-01/`
- TLS Chain/SAN, Login, Push/Pull, Trivy, Digest, Negative, Rotation, Rollback 및 `99_SHA256SUMS.txt`

### 🔗 Dependency

- Blocked By Runtime: Network/Linux 기반, D19 Private CA; Worker Pull은 P1-K8S Node 준비
- Blocks / Next: P1-CICD-01 Delivery, P1-K8S/APP/MON Image Pull, G1 Infrastructure Ready
- Related: P1-SEC-01 Credential/RBAC, P1-DR-02 Harbor Restore

### ⚖️ Decision / Risk Control

- Decision: D19의 Private Root CA + Harbor 전용 Leaf + Consumer CA Trust를 구현한다.
- Risk Control: `insecure`/검증 우회를 금지하고 Push·Pull Identity를 분리한다. OID-02 전에는 CP Source를 허용하지 않는다.

### 🔍 Review / Handoff

- Review Owner: 이권욱
- Handoff: CA Bundle, Repository, Robot Account Scope, Digest와 Pull 예시를 P1-K8S/P1-CICD/P1-APP/P1-MON에 전달한다.

<!-- p1-hbr-r6-sync:start -->
## 2026-09-10 — 6차 리뷰 및 AC-05 책임 경계 동기화

### 리뷰 판정

| 항목 | 현재 판정 |
|---|---|
| 종합 결과 | **HOLD / NOT READY** |
| Ticket 상태 | **In Progress / Open** |
| AC 집계 | **PASS 0 / FAIL 0 / NOT VERIFIED 6** |
| 완료 전환 | Runtime 원본 증적과 AC Matrix가 확보되기 전 `In Review` 또는 `Done` 전환 금지 |

상태관리상 Harbor 자체 구현·보완은 선행 티켓과 독립적으로 진행할 수 있으므로 `In Progress`로 전환한다. AC-05의 P1-CICD-01 의존성과 Runtime 증적 미확보는 착수 차단이 아니라 완료 차단이다.

문서와 검증 절차가 개선된 사실은 확인했지만, 실행 결과를 대신하지 않는다. `FAIL 0`은 Acceptance Criteria 통과를 의미하지 않는다.

### Acceptance Criteria 상태

| AC | 검증 대상 | 상태 | 미충족 또는 선행조건 |
|---|---|---|---|
| AC-01 | Harbor Service/Health 및 TLS Chain/SAN | NOT VERIFIED | 실제 Health, Chain, 재기동 복구 원본 증적 필요 |
| AC-02 | IF-09 Runner Push/Pull 및 음성시험 | NOT VERIFIED | Runner Runtime과 Source IP 증적 필요 |
| AC-03 | IF-10 Worker 3대 Pull/Pod Start 및 Push DENY | NOT VERIFIED | `.105/.107/.108` 각각의 Runtime 증적 필요 |
| AC-04 | 실제 Source IP와 Host Firewall Allowlist | NOT VERIFIED | IF-16 Route Drift 해소 또는 승인 예외와 도착지 로그 필요 |
| AC-05 | Scan/Harbor/Manifest/Pod Digest Traceability | **BLOCKED / NOT VERIFIED** | [P1-CICD-01 #16](https://github.com/321Team/fds-project-baseline/issues/16)의 CI/Trivy 산출물 필요 |
| AC-06 | Credential 비노출 및 Evidence 무결성 | NOT VERIFIED | Worker argv 노출 제거, Rotation/Fingerprint, Secret Scan, SHA-256 검증 필요 |

### AC-05 책임 경계

- **P1-CICD-01 — 이권욱:** Workflow/Source Commit SHA, Run ID/Attempt, CI Trivy 실행 결과와 Scan Digest, Negative Gate, Push 제어, 배포 Digest patch 및 이전 승인 Digest 복구 산출물을 생성·제공한다.
- **P1-HBR-01 — 이하영:** Harbor Service/Scanner·Registry 정책, Harbor Artifact Digest, Robot Account/CA/Worker Pull 경계의 실행 증적을 수집하고 P1-CICD-01 산출물을 인수·검증한다.
- **공동 산출:** 아래 4개 값의 동일성을 한 Review Run 기준으로 대조하고 Rollback 후 Pod Start/Health를 재검증한다.
  1. CI/Trivy Scan Digest
  2. Harbor Artifact Digest
  3. 배포 Manifest의 `image@sha256` Digest
  4. 실행 Pod의 `containerStatuses[].imageID`

`LOCAL_DIGEST ↔ HARBOR_DIGEST` 2-way 비교는 보조 사전점검으로 유지할 수 있으나 AC-05 PASS 또는 CI Scan Digest를 대체하지 않는다. CI 산출물이 제공되기 전에는 P1-HBR-01에서 값을 임의 생성하지 않고 `BLOCKED BY #16 / NOT VERIFIED`로 관리한다.

Harbor Trivy Scanner 서비스 확인과 CI Trivy Scan 실행은 서로 다른 책임이다. 정본이 요구하는 Harbor Scanner 항목은 P1-HBR-01에서 유지하며, CI-only 모델 또는 Harbor Scanner 제외는 Scope/AC 변경 승인 전까지 `Proposed / Approval Pending`이다.

### 6차 리뷰 후속 조치

- [ ] Worker Push DENY 시험의 `ctr --user` argv Credential 노출 제거 — 권장안: `nerdctl --password-stdin`
- [ ] Runner/Worker/Control Plane 간 동일 Review Run Metadata를 무결성 검증 가능한 형태로 인계
- [ ] `fds-app` Restricted PSA, Pull Secret, 명시적 non-root UID/GID 및 Pod cleanup 실제 검증
- [ ] TLS Negative Test를 정상 CA 선행 성공 + 잘못된 CA의 정확한 `curl` Exit Code 60으로 판정
- [ ] Worker 3대별 Pull/Pod/Push DENY, 실제 Source IP 및 Firewall 원본 증적 확보
- [ ] 4/4 Digest Traceability 및 이전 승인 Digest Rollback/Health 증적 확보
- [ ] Credential Rotation/Fingerprint, Secret Scan, `AC_Evidence_Matrix.md`, `99_SHA256SUMS.txt` 제출

### 비차단·승인 대기 항목

- Retention/GC는 Optional / Non-blocking이며 보호 Digest와 Rollback 보존 기준 확정 후 적용한다.
- Robot Token `Never`, Trivy Threshold, Harbor Scanner 제외는 승인 전까지 완료 근거로 사용하지 않는다.
<!-- p1-hbr-r6-sync:end -->

---

### 📝 Completion Record

- Result: 6차 리뷰 HOLD — 구현 절차 보완 중 / Runtime Not Verified
- Status: In Progress
- Completed Date: 미입력
- Reviewer / Approver: 이권욱(6차 리뷰) / 미승인
````

</details>


</details>
