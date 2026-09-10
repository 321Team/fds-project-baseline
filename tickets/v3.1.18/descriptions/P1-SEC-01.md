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
| Source | Baseline/Ticket Pack v3.1.18; GitHub #19; K8S PR #2 097ddb5, #3 merge 7d44afc, #4 75d476e; audit/v3.1.18/k8s-intake-20260910.json |
| Schedule Note | 09-10 휴가 추가 후 기존 09-04~11 가용일은 4일. 권장 종료 09-21로 확장한 전체 계획창의 가용일은 10일이며 잔여 공수를 뜻하지 않는다. Runtime 검증은 플랫폼·앱 인수와 연계한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |

## 현재 실행·검토 상태

Manifest/Prework GO와 In Progress를 유지한다. D17/D34 설계 승인과 별도로 Runtime AC는 PASS 0 / FAIL 0 / NOT VERIFIED 6, 완료 HOLD다. PR #2 현장 증적에서 CP1 Calico Running·firewalld active·HEP/GNP 각각 0을 확인했다. Worker Cockpit socket/service 6 unit mask·9090 listener 부재는 보완 증적 PASS이나 잔여 방화벽 허용 제거·CP 포함 전체 Gate 0는 별도다. PR #3 수집기 병합 및 PR #4 75d476edc33d6368fe4ab07e78fc51759e81a6fc Runtime 전용 보완/74개 로컬 모의시험 기록을 연결하되 실제 보호 전환·차단·회귀·재부팅·복구 인수로 확대하지 않는다. 최신 HEAD 독립 리뷰, 실제 보호·콘솔·백업·복구·변경창 확인, NTP 승인 egress와 전체 Platform Ready가 남는다. 현재 후보 Plan: 2026-09-04 ~ 2026-09-21 (조건부 목표).

근거: [Issue #19](https://github.com/321Team/fds-project-baseline/issues/19), Issue 갱신 시각 `2026-09-10T05:05:52Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

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
