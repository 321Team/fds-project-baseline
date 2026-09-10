<!-- fds-canonical-description:v3.1.18 record-id:P1-HBR-01 -->
# P1-HBR-01 — Harbor / Trivy Registry

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

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

## 현재 실행·검토 상태

구현 절차 및 6차 리뷰 후속 보완 착수로 In Progress. Runtime AC는 PASS 0 / FAIL 0 / NOT VERIFIED 6, 완료 HOLD. AC-05는 CI Scan Digest·Harbor Artifact·Manifest image@sha256·Pod imageID 4개 동일성으로 검증하고 CI 산출물은 P1-CICD에서 인수한다. Harbor Scanner 제외/CI-only 전환, Robot Token Never와 미확정 Threshold는 승인 대기 제안이다. 현재 후보 Plan: 2026-08-31 ~ 2026-09-17 (권장안; 실제 완료일·Gate 승인은 미확정).

근거: [Issue #13](https://github.com/321Team/fds-project-baseline/issues/13), Issue 갱신 시각 `2026-09-10T03:15:50Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

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
