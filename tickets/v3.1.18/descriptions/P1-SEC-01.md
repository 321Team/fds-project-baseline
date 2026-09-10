<!-- fds-canonical-description:v3.1.18 record-id:P1-SEC-01 -->
# P1-SEC-01 — Kubernetes Security Controls

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P1-SEC-01 |
| Phase | Phase 1 |
| Category | Security / Kubernetes |
| Type | Task |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-09-04 |
| End | 2026-09-21 |
| Calendar Days | 18 |
| Working Days | 10 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | PSA/SecurityContext/Default Deny/RBAC/HEP-GNP/Secretbox/LimitRange/Probe와 `.50/32→30080` 포함 Positive·Negative·Rollback Evidence PASS |
| Related Decision IDs | D12; D17; D18; D19; D27; D31; D34 |
| Related Risk IDs | RISK-06; RISK-07; RISK-08 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #19 snapshot 2026-09-10T05:05:52Z; 사용자 2026-09-10 면접 휴가 추가 지시; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청 |
| Schedule Note | 09-10 휴가 추가 후 기존 09-04~11 가용일은 4일. 권장 종료 09-21로 확장한 전체 계획창의 가용일은 10일이며 잔여 공수를 뜻하지 않는다. Runtime 검증은 플랫폼·앱 인수와 연계한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |

## 현재 실행·검토 상태

Manifest/Prework와 호스트 보호 선행도구 연계 착수로 In Progress. D17/D34 설계 승인 완료. Runtime AC는 PASS 0 / FAIL 0 / NOT VERIFIED 6, 완료 HOLD / NOT READY. CP1의 HEP/GNP 각 0개, 3CP firewalld active 및 전체 Platform Ready 미완료 상태에서 일괄 firewalld OFF를 실행하지 않는다. 현재 후보 Plan: 2026-09-04 ~ 2026-09-21 (권장안; 실제 완료일·Gate 승인은 미확정).

근거: [Issue #19](https://github.com/321Team/fds-project-baseline/issues/19), Issue 갱신 시각 `2026-09-10T05:05:52Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 일정 권장안

Start/End는 이번 Fast Tracking 후보의 계획값이다. 기존 승인 일정은 `audit/v3.1.18/fast-track-plan.json`에 전후 값으로 보존한다. 실제 착수·완료·Status·AC·승인을 변경한 것이 아니다. 교육장 주말 작업은 없으며 세부 AM/PM 배정과 선행 조건을 따른다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- [후속 기록](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5613475033)

---

### User Story

Kubernetes 보안 담당자로서 D-SEC-01 승인 설계를 Manifest와 Runtime Policy로 구현하고 최소권한과 기본차단을 증명한다.

### Scope

#### In Scope

- Namespace/PSA/version label
- SecurityContext/SA/RBAC
- Workload NetworkPolicy
- Calico named HEP/GNP 및 preDNAT NodePort
- Secretbox at-rest encryption
- LimitRange/Resource presence/Probe verification
- cicd-runner-sa Role/TokenRequest 정책

#### Out of Scope

- Self-hosted Runner 설치·GitHub 등록·Service·Workflow 운영
- Application 코드와 Monitoring Workload 자체 구현
- P2 Admission Policy·Image 서명 강제·KMS v2

### 핵심 요구사항

- [ ] kube-system enforce Privileged, audit/warn Restricted
- [ ] CoreDNS 실제 Manifest dry-run
- [ ] monitoring-node 신규 Workload 생성 제한
- [ ] `.50/32→Worker:30080`만 preDNAT 허용
- [ ] Prometheus `nodes/metrics`와 `/metrics`만, `nodes/proxy`·Secret 금지
- [ ] Runner는 기존 2개 Deployment get/update/patch만 허용
- [ ] Secretbox key root-only, 3CP 동일 Config, etcd 원문 비노출

### Acceptance Criteria

- [ ] PSA 위반 Pod 차단
- [ ] Allow 흐름 PASS / Deny 흐름 FAIL
- [ ] SA별 `kubectl auth can-i` Positive/Negative PASS
- [ ] NodePort/9100/10250 HEP/GNP PASS
- [ ] Secret encryption·backup·rotation·rollback PASS
- [ ] Probe 장애 주입과 Endpoint 제외 PASS

### Evidence

- `docs/evidence/P1-SEC-01/`
- 비밀정보는 fingerprint 또는 마스킹만 기록

### Dependency

- Blocked By Runtime: P1-K8S Platform Ready
- Related: ICR-D-NET-01-01, P1-APP, P1-MON, P1-CICD

### Decision / Risk Control

- Decision: D17/D34와 D-SEC-01 v1.0을 구현 기준으로 사용한다.
- Risk Control: HEP/GNP는 Bootstrap Allow와 canary를 먼저 적용하고 Secretbox key는 Git/Evidence에서 제외한다. Deployment patch 우회 위험은 P1 Residual Risk로 유지한다.

### Review / Handoff

- Review Owner: 이권욱, 이재환
- Handoff: SA/RBAC/TokenRequest 정책은 P1-CICD에, Probe·Resource 검증 결과는 P1-APP/P1-MON에 전달한다.

### Completion Record

- Result: STARTED — Manifest/Prework 및 호스트 보호 선행도구 연계 / Runtime Not Verified
- Status: In Progress
- Completed Date: 미입력
- Reviewer / Approver: Review Owner 이권욱·이재환 / Runtime 승인 미완료
