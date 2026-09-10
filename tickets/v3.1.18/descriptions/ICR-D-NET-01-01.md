<!-- fds-canonical-description:v3.1.18 record-id:ICR-D-NET-01-01 -->
# ICR-D-NET-01-01 — Kubernetes Node Host Firewall / Monitoring Route

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | ICR-D-NET-01-01 |
| Phase | Phase 1 |
| Category | Network / Interface Change Control |
| Type | Change Request |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-09-01 |
| End | TBD — Runtime Evidence 완료 후 확정 |
| Calendar Days | TBD |
| Working Days | TBD |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | Kubernetes 6개 Node의 보호 공백 없는 firewalld→Calico named HEP/GNP 전환, 30080/9100/10250 최소 허용, 관리망 반환 경로와 IF-06B 정합화, Positive/Negative/Regression/Reboot/Rollback 및 무결성 Evidence 완료 |
| Related Decision IDs | D17; D18; D33; D34; D35 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #14 snapshot 2026-09-10T05:03:39Z |
| Schedule Note | CP1 사전 진단 완료, 최소 CP 통신 canary 적용·독립 리뷰·운영 인수 대기. 6대 HEP/GNP·IF-06B·IF-16 및 NTP 목적지/Worker 검증은 잔여. End/기간 TBD 유지. |

## 현재 실행·검토 상태

v1.1 읽기 전용 CP 재점검은 snapshot/일반 조회 110개 기록 rc=0, gaps 없음으로 검토됐다. 소스 HEAD 068661e076de02669170d3582f3d596d6e1a8eb3는 Draft PR #2이며 독립 리뷰·실행 결정 대기다. CP1 제한 canary의 방화벽 적용·복구·join은 미실행. CP2/3·Worker·NTP 목적지 고정·HEP/GNP 및 기존 IF-06B/IF-16 범위는 잔여다. 6대 기준 AC와 종료일 TBD를 유지한다.

근거: [Issue #14](https://github.com/321Team/fds-project-baseline/issues/14), Issue 갱신 시각 `2026-09-10T05:03:39Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

### User Story

네트워크 및 보안 담당자로서 Kubernetes Node의 호스트 방화벽 통제를 firewalld에서 Calico named HostEndpoint와 GlobalNetworkPolicy로 전환한다. 이를 통해 관리망과 Monitoring 경로의 실제 Source/Return Path를 정본 Interface 계약과 일치시키고, 승인된 최소 통신만 재현 가능하게 허용한다.

---

### Scope

#### In Scope

- Kubernetes 6개 Node의 보호 전환 후 firewalld 비활성화 검증
- Calico named HostEndpoint, `expectedIPs`, Bootstrap Allow 및 최소 허용 GNP
- NodePort 30080, node-exporter 9100, kubelet 10250의 승인 Source 허용과 비승인 Source 차단
- Control Plane 관리 기능과 Harbor Pull 회귀 검증
- IF-06B Prometheus Remote Write 경로의 TLS/Auth/Payload Allowlist 및 egress 차단
- IF-16 관리망 반환 경로, Source Preservation 및 내부 SNAT 미사용 검증
- Reboot 지속성, Rollback 재현성, Evidence 무결성 및 비밀정보 미노출 검증

#### Out of Scope

- 설계 승인만으로 Runtime PASS를 선언하는 행위
- 관측되지 않은 Source IP 또는 추정 경로를 기준으로 허용 정책 확정
- 평문 Token, Password 또는 Private Key의 Evidence 저장
- ICR 외 기능 티켓의 완료 상태 자동 상향

---

### 핵심 요구사항

- [x] firewalld 비활성화와 Calico named HEP/GNP 전환 설계를 D34/D35 기준으로 확정한다.
- [x] IF-06B와 IF-16의 정본 Interface 계약을 유지한다.
- [ ] Kubernetes 6개 Node의 변경 전 상태와 SHA-256 Evidence를 확보한다.
- [ ] named HEP/`expectedIPs`와 Bootstrap Allow를 승인안대로 적용한다.
- [ ] 30080/9100/10250에 대해 승인 Source 허용과 비승인 Source 차단을 검증한다.
- [ ] Control Plane 관리 기능, Harbor Pull 및 Worker Route 회귀를 검증한다.
- [ ] IF-06B Receiver/TLS/Auth/Payload Allowlist와 실제 Source/Return Path를 검증한다.
- [ ] IF-16 edge/harbor/db Route Drift를 시정한다.
- [ ] Reboot 지속성과 Rollback 재현성을 검증한다.
- [ ] Evidence Index·SHA256SUMS·비밀정보 검사를 완료한다.
- [ ] 고정 Commit/Artifact에 대한 독립 리뷰와 Lead 최종 승인을 완료한다.

---

### Acceptance Criteria

- [ ] `ICR-AC-01` — 6개 Node 변경 전 firewall/listener/route 설정과 SHA Evidence를 확보한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-02` — firewalld가 disabled/inactive이고 Calico Pod/Node 통신이 정상이다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-03` — named HEP/`expectedIPs`/Bootstrap Allow가 승인안과 일치한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-04` — `.50 → Worker:30080`은 허용되고 비승인 Source는 차단된다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-05` — Prometheus에서 Worker node-exporter 9100 Target이 `UP`이다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-06` — Prometheus에서 Worker kubelet 10250을 CA+SA로 인증한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-07` — 비승인 Workload의 9100/10250 접근이 차단된다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-08` — Control Plane의 logs/exec/port-forward가 정상이다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-09` — Worker에서 Harbor `.54:443` Pull과 Pod 시작이 성공한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-10` — Cockpit 9090이 노출되지 않는다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-11` — monitor01에서 Cluster Workload로 신규 Ingress를 시작할 수 없다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-12` — IF-06B Remote Write의 TLS/Auth/Payload Allowlist가 충족되고 비승인 Egress가 차단된다. 현재: **BLOCKED**.
- [ ] `ICR-AC-13` — edge/harbor/db에 `10.250.10.0/24 via .58`가 적용되고 `.30` route-get이 통과한다. 현재: **FAIL — DRIFT**.
- [ ] `ICR-AC-14` — Worker 3대에서 동일 경로 조회 회귀가 통과한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-15` — mgmt-gw IP Forward/Zone/Policy/NAT가 승인안과 일치하고 내부 SNAT가 없다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-16` — monitor01 `.30:443` Receiver/Protocol/TLS/Auth가 정본과 일치한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-17` — 패킷 관찰의 실제 Source와 양방향 Return Path가 정본과 일치한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-18` — Reboot 후 정책이 유지되고 재시험이 통과한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-19` — Rollback을 재현할 수 있다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-20` — Evidence에 평문 비밀정보가 없다. 현재: **NOT VERIFIED**.

---

### 검증 및 증적

- `ICR-D-NET-01-01` v1.4의 설계와 정본 ID 매핑: **APPROVED**
- firewalld 비활성화와 Calico HEP/GNP 전환 전략: **설계 승인**
- IF-06B 계약 유지: **정본 결정 완료, Runtime BLOCKED**
- IF-16: **DRIFT — edge/harbor/db Remediation Pending**
- 연결된 `321Team` GitHub 범위에서 `ICR-D-NET-01-01`, `IF-06B`, `HostEndpoint`, `management_return_route`, `30080/9100/10250` 관련 코드 또는 PR 증적: **검색 결과 없음**
- 6개 Node Runtime Evidence, Positive/Negative/Regression/Reboot/Rollback 결과: **미확인**
- Evidence Index, SHA256SUMS 및 비밀정보 검사 결과: **미확인**

설계 승인과 Runtime Acceptance를 합산하여 PASS로 처리하지 않는다. 검색 결과가 없다는 사실만으로 구현 실패를 단정하지 않으며, 검증 가능한 Evidence가 제출될 때까지 `NOT VERIFIED`로 관리한다.

---

### Dependency

- P1-LB-01 Stage A Evidence의 공식 Handoff
- P1-K8S-01 Calico Ready 및 Port Matrix 검증
- Prometheus 실제 Source 관찰
- IF-06B Receiver/TLS/Auth 및 관리망 Forward/Return Path 확정
- IF-16 edge/harbor/db Route Drift 시정
- 본 ICR은 P1-SEC-01, P1-MON-01 및 G2 Runtime 판정에 영향을 준다.

---

### Decision / Risk Control

- `D17`: Kubernetes Host 보호의 Mandatory Control을 유지한다.
- `D18`: 승인된 서비스 진입 경로와 NodePort 범위를 유지한다.
- `D33`: IF-06B Prometheus Remote Write 계약을 유지한다.
- `D34`: firewalld 비활성화와 Calico named HEP/GNP 전환 설계를 적용한다.
- `D35`: 중복 Interface를 정리한 v1.4 매핑과 설계/Runtime 상태 분리를 유지한다.
- `RISK-04`: 실제 Source 및 Return Path 오판 위험을 route, tcpdump, conntrack Evidence로 통제한다.
- `RISK-07`: 증적 부재와 완료 상태 과대판정을 Evidence Index, SHA-256, 독립 리뷰로 통제한다.
- IF-06B 부분 차단을 티켓 전체 `Blocked`로 과장하지 않되, Runtime Evidence 없이 `Done`으로 상향하지 않는다.

---

### Review / Handoff

- 현재 Review 상태: Runtime Evidence 제출 전이므로 독립 기술 리뷰 미착수
- Reviewer: Evidence 고정 후 별도 지정 및 승인 필요
- Lead 최종 승인: 미완료
- Handoff 전 필수 조치:
  1. 6개 Node와 mgmt-gw/monitor01/edge/harbor/db의 변경 전 Evidence 수집
  2. 승인된 HEP/GNP와 Route 변경안을 고정 Commit으로 구성
  3. Positive/Negative/Regression 시험 수행
  4. Reboot 지속성 및 Rollback 시험 수행
  5. Evidence Index·SHA256SUMS·비밀정보 검사 완료
  6. 독립 리뷰와 Lead 승인 후 상태와 종료일 확정

---

### Completion Record

- Acceptance: **미달성**
- Runtime Evidence: **미확인**
- IF-06B: **BLOCKED**
- IF-16: **FAIL — DRIFT**
- 독립 Reviewer 승인: **미완료**
- Lead 최종 승인: **미완료**
- 최종 판정: **In Progress 유지**
- End / Calendar Days / Working Days: **TBD 유지**

`ICR-D-NET-01-01`은 2026-09-08 기준 완료 조건을 충족하지 않았다. ICR-AC-01~20의 PASS Evidence 또는 승인된 N/A 근거, IF-06B 차단 해소, IF-16 Drift 시정, Positive/Negative/Regression/Reboot/Rollback 결과, Evidence 무결성, 독립 리뷰 및 Lead 승인을 모두 확보한 후에만 `Done`으로 상향한다.
