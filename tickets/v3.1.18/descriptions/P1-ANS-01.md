<!-- fds-canonical-description:v3.1.18 record-id:P1-ANS-01 -->
# P1-ANS-01 — Ansible Inventory / OS-Node Bootstrap — Closed Update

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P1-ANS-01 |
| Phase | Phase 1 |
| Category | Automation / Configuration Management |
| Type | Task |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-27 |
| End | 2026-09-01 |
| Calendar Days | 6 |
| Working Days | 4 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | ansible01 10.250.10.10에서 CP 3대·Worker 3대 Inventory/SSH PASS=6, OS·Kubernetes 선행조건 적용, 재실행 changed=0 및 Evidence 확보 |
| Related Decision IDs | D01; D13; D25; D28; D31 |
| Related Risk IDs | RISK-03; RISK-04; RISK-05; RISK-14 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #65 snapshot 2026-09-10T03:37:26Z |
| Schedule Note | 2026-08-28 TECHNICAL PASS 후 2026-08-31 이하영 Reviewer PASS·Approver APPROVED를 기록했다. HO-ANS-08·09는 PASS이며 P1-ANS-01은 Done으로 종결한다. HO-ANS-01~04는 후속 Ticket Acceptance로 이관하고 미완료 상태를 유지한다. |

## 현재 실행·검토 상태

P1-ANS-01 원 종결(2026-08-31, HO-ANS-08/09 PASS)은 유지한다. 후속 SSH 검증식 PR #4는 5a2c3786f6af9f107200654aa12c92c3b09700f0에서 승인되고 3a02dc8934adb1f80df48ec6763689c401a1e8d6로 병합됐다. 운영 Issue #10은 6대 apply·멱등성·SFTP 확인과 독립 승인 후 종결. Gate 0 도구 PR #3 merge 5cbf3b657014b32a20cb5816d90d3ea5fe4951ab는 코드 편입이며 6대 Cluster 완료가 아니다. 2.21.3 엔진 전환 Issue #9와 NTP 목적지 승인·재검증은 잔여다.

근거: [Issue #65](https://github.com/321Team/fds-project-baseline/issues/65), Issue 갱신 시각 `2026-09-10T03:37:26Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- 이 티켓은 종결 이력이다. 과거 구성 설명은 해당 종결 범위를 설명하며 현재 배포 명령으로 사용하지 않는다. 후속 설계 변경은 Baseline의 현행 절과 책임 티켓을 따른다.

---

# User Story

자동화 담당자 이권욱으로서 ansible01에서 Kubernetes 예정 노드 6대의 OS와 Node Bootstrap 설정을 일관되게 적용한다. 이를 통해 수동 설정 편차를 줄이고 동일한 구성을 반복 재현할 수 있게 한다.

---

# Scope

## In Scope

- ansible01 10.250.10.10
- CP 3대·Worker 3대 Inventory
- svc_ansible·SSH Key·sudo
- common·k8s_prereq Role
- Check/Diff·멱등성·Evidence

## Out of Scope

- VMware VM 생성
- 동결된 IP·Route 자동 변경
- kubeadm init/join과 Calico 완료 판정
- Kubernetes 보안 Manifest
- 애플리케이션 Delivery

---

# 핵심 요구사항

- [x] Inventory Group과 host_vars를 실제 Node/IP와 일치시킨다.
- [x] Secret과 Private Key를 Source에 평문 저장하지 않는다.
- [x] 적용 전 --check --diff를 수행한다.
- [x] Network Freeze 변경은 Change Request 없이는 수행하지 않는다.

---

# Acceptance Criteria

- [x] ansible all -m ping 결과가 PASS=6, FAIL=0이다.
- [x] 접속 Source가 10.250.10.10으로 확인된다.
- [x] Playbook 결과가 failed=0, unreachable=0이다.
- [x] 2차 실행 결과가 changed=0이다.
- [x] Linux/Kubernetes 선행조건 검증이 통과한다.

---

# 검증 및 증적

- ansible-inventory --graph
- Ping·Check/Diff·Apply 로그
- 2차 실행 Recap
- Secret 통제 확인
- Evidence Path: docs/evidence/P1-ANS-01/

---

# Dependency

- **Blocked By:** D-NET-01 — Done; P1-LNX-01 — Done
- **Blocks / Next:** P1-K8S-01; MS-G1-01
- **Related Ticket:** P1-DNS-01
- **Milestone:** G1 Infrastructure Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D01; D13; D25; D28; D31
- **Decision Control:** 관련 Decision은 이권욱·이하영·이재환이 확인할 수 있는 기록으로 남기며, 승인 전 조건부 작업을 시작하지 않는다.
- **Related Risk IDs:** RISK-03; RISK-04; RISK-05; RISK-14
- **Risk Control:** 예방·탐지·복구 통제를 Acceptance Criteria와 Evidence에 연결한다.

---

# Review / Handoff

- **Review Owner:** 이하영
- **Review Result:** PASS — 2026-08-31
- **Approval Result:** APPROVED — 2026-08-31
- **Closed Control:** HO-ANS-07·08·09 PASS
- **Transferred Control:** HO-ANS-01·02A·03·04A → P1-K8S-01; HO-ANS-02B·04C → P1-SEC-01; HO-ANS-04B → P1-LB-01; Service/Probe 계약 → P1-APP-01

---

# Completion Record

- **Result:** PASS / APPROVED
- **Status:** Done
- **Exit Criteria:** ansible01 10.250.10.10에서 CP 3대·Worker 3대 Inventory/SSH PASS=6, OS·Kubernetes 선행조건 적용, 재실행 changed=0 및 Evidence 확보
- **Completed Date:** 2026-08-31
- **Reviewer / Approver:** 이하영 / 이하영 — 동일인 겸임 명시
