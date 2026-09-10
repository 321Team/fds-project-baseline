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
| End | 2026-09-21 |
| Calendar Days | 21 |
| Working Days | 15 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | Kubernetes 6개 Node의 보호 공백 없는 firewalld→Calico named HEP/GNP 전환, 30080/9100/10250 최소 허용, 관리망 반환 경로와 IF-06B 정합화, Positive/Negative/Regression/Reboot/Rollback 및 무결성 Evidence 완료 |
| Related Decision IDs | D17; D18; D33; D34; D35 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | Baseline/Ticket Pack v3.1.18; GitHub #14; K8S PR #2 097ddb5, #3 merge 7d44afc, #4 75d476e; audit/v3.1.18/k8s-intake-20260910.json |
| Schedule Note | 09-21은 권장 Plan End이며 실제 종료일 확정이나 AC 완료가 아니다. 기존 End TBD 이력은 보존한다. CP→Worker·NTP·IF-16을 먼저, IF-06B·Negative/Reboot/Rollback·보호 인계를 후속 검증한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |

## 현재 실행·검토 상태

PR #2 실행 source afc246d의 현장 Linux 모의시험 37/37·CP 읽기 전용 115개 조회가 검증됐고 최신 HEAD는 097ddb56d87b229a9eb465f72ea9f55d16524c51이다. Worker 보완 24개 조회·내부 8/8 체크섬과 시간·kubelet 원인·Cockpit mask 증적 PASS, PR #3 merge 7d44afc3afff4d322cb4dbeff4433d61e23e111a를 반영한다. 과거 CP→Worker TCP 0/9 및 Worker→LB TCP 3/3은 당시 부분 증적이다. PR #4 75d476edc33d6368fe4ab07e78fc51759e81a6fc는 최신 영수증/실제 인수 연결·Runtime 전용 변경/복구로 보완됐고 로컬 모의시험 74개 PASS 기록이 있다. 새 HEAD 독립 리뷰·실제 CP1 canary·후속 노드 적용/복구는 미완료이며 Permanent 승격은 미구현이다. NTP 목적지/운영 주체·동기화 기준, Cockpit 잔여 방화벽 허용 제거, HEP/GNP·IF-06B·IF-16 및 ICR AC-01~20은 잔여다. 실제 종료일 미확정·이전 End TBD 이력을 보존한다. 현재 후보 Plan: 2026-09-01 ~ 2026-09-21 (조건부 목표).

근거: [Issue #14](https://github.com/321Team/fds-project-baseline/issues/14), Issue 갱신 시각 `2026-09-10T05:03:39Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

이전 후보 출처: [Worker/NTP 검토·잔여 작업](https://github.com/321Team/infra-kubernetes/blob/3309866766236bbdbe20b9e2ae1d8fd6f9233bcd/docs/change/ICR-D-NET-01-01/RESIDUAL_WORK_20260910.md). 원래 수집본은 보존하고 `audit/v3.1.18/followup-20260910.json`에 추가 기록을 고정했다. 이번 정본 보완은 연결된 검토 기록의 반영이며 서버 재시험은 아니다.

## 2026-09-10 K8S 최신 이력 통합

- PR #2: 실행 source `afc246d2db041c68de5014972107484dad122558`, 증적 편입 HEAD `097ddb56d87b229a9eb465f72ea9f55d16524c51`. 현장 Linux **모의시험 37/37**, CP **읽기 전용 조회 115개**의 검증 기록을 반영한다. Runtime apply/rollback 증적은 아니다.
- Worker: 15:34 KST 보완 증적에서 6대 시간 속성, Worker kubelet의 config.yaml 부재 오류, Cockpit 6 unit mask 및 9090 listener 부재를 확인했다. 같은 supplement의 추가 재수집은 잔여에서 제외한다. TCP·firewall·chrony source를 재조회한 결과는 아니다.
- PR #3: `3309866766236bbdbe20b9e2ae1d8fd6f9233bcd`의 수집기 소스가 **Merged**, merge `7d44afc3afff4d322cb4dbeff4433d61e23e111a`. 병합을 클러스터·방화벽 운영 인수로 해석하지 않는다.
- PR #4: 최신 `75d476edc33d6368fe4ab07e78fc51759e81a6fc`에서 최신 PR #2 영수증·실제 인수 연결, Runtime 전용 변경/복구, 정책·상태·실행 통제를 보완했다. 로컬 Linux **모의시험 74개**(PR #4 55+Worker 회귀 19) PASS 기록이며 새 HEAD 리뷰·실서버 검증은 미완료다. 구 소스의 계약/순서 지적은 보존하되 보완 미착수로 표시하지 않는다.
- PR #2/#4는 이하영의 최신 HEAD 독립 리뷰와 실제 Runtime 인수가 남는다. 현재 구현은 Runtime 전용이며 Permanent 승격은 미구현이다. CP2 재개·6대 가입·etcd 3 Member·DNS/cross-node·NTP·HEP/GNP·Storage·재부팅/복구는 기존 미완료 상태다.
- 09-11의 완료된 Worker supplement 재수집 문구를 CP1 보호/복구·inspect 준비로 교체한다. PR #2/#4 재리뷰를 연결하며 날짜·담당·배정 인일·휴가·주말 가용량·Gate/AC는 유지한다.

고정 출처·당시 본문·이전 후보 값은 `audit/v3.1.18/k8s-intake-20260910.json`, 자세한 조건은 `releases/v3.1.18/FDS_K8S_Candidate_Integration_20260910.md`에 기록한다. 이 통합은 후보 문서 갱신이며 운영 적용·정본 발행이 아니다.

### 미결 사양과 실행 조건

현재 3CP+3Worker·kubeadm·Calico·static local PV 범위를 유지한다. 추가 노드·플랫폼 도입 결정은 없다. NTP 목적지/운영 주체(#14), 동기화 수치 인수조건(#10), 최소 egress(#19)는 해당 변경·인수 전에 확정한다. `100ms·60초×6`은 미승인 초안이고 MTU 1450도 실측 확정 전 후보값이다. CP2 원래 join 단계·비표준 data 경로와 보존/정리/재개 방식은 실제 조사 후 판단한다.

발행 D34의 Calico 설치 전 firewalld OFF 이력과 실제 CP1 공존 drift를 구분한다. ADV-20260910에 따라 사유·기간·보호·복구·종료조건을 기록한 제한적 선행 준비를 이어간다. 최종 6대 firewalld disabled/inactive 및 named HEP/GNP 목표, Bootstrap Allow→canary Worker→Worker 확대→CP의 보호 전환 순서를 유지한다. CP 통신 canary가 HEP 전환 순서를 대체하지 않는다.

PR #2 최신 HEAD 리뷰·실행 창의 inspect·보호/콘솔/백업/복구·실행 결정 후 CP1 제한 Runtime을 검증한다. 실제 CP1 인수 및 PR #4 최신 HEAD 리뷰 후 후속 대상의 실행·복구/가입을 판단한다. Runtime 시험·리뷰 이후의 Permanent 또는 최종 보호 인계 종료 절차는 별도 결정·구현 대상이다. 승인 JSON을 실제 GitHub 리뷰 인증으로 해석하지 않는다. NTP 미결을 모든 준비의 전역 중단 조건으로 만들거나 기존 시간 동기화 선행조건을 면제하지 않는다.

## 일정 권장안

Start/End는 이번 Fast Tracking 후보의 계획값이다. 기존 승인 일정은 `audit/v3.1.18/fast-track-plan.json`에 전후 값으로 보존한다. 실제 착수·완료·Status·AC·승인을 변경한 것이 아니다. 교육장 주말 작업은 없으며 세부 AM/PM 배정과 선행 조건을 따른다.

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
- 기존 2026-09-08 기록의 End / 기간: **TBD**. 현재 권장 Plan End/기간은 상단 속성표를 따르며 실제 완료일은 미확정이다.

`ICR-D-NET-01-01`은 2026-09-08 기준 완료 조건을 충족하지 않았다. ICR-AC-01~20의 PASS Evidence 또는 승인된 N/A 근거, IF-06B 차단 해소, IF-16 Drift 시정, Positive/Negative/Regression/Reboot/Rollback 결과, Evidence 무결성, 독립 리뷰 및 Lead 승인을 모두 확보한 후에만 `Done`으로 상향한다.
