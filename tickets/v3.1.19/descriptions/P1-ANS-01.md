# P1-ANS-01 — Ansible Inventory / OS-Node Bootstrap — Closed Update

> v3.1.19 CANDIDATE / NOT RELEASED · 2026-09-17 20:28 KST

## 현행 속성

| Property | 입력값 |
|---|---|
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
| Source | Baseline v3.1.19 CANDIDATE; GitHub #65 @ 2026-09-14T15:17:33Z; 원문 SHA256 b96e7c6b8d3b79c183c552f314d9e8f9943a3d3e3e3109a477237592284916e9 |
| Schedule Note | 2026-08-28 TECHNICAL PASS 후 2026-08-31 이하영 Reviewer PASS·Approver APPROVED를 기록했다. HO-ANS-08·09는 PASS이며 P1-ANS-01은 Done으로 종결한다. HO-ANS-01~04는 후속 Ticket Acceptance로 이관하고 미완료 상태를 유지한다. |

## 상태와 인수 경계

현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다.

- GitHub lifecycle: closed; Milestone: G1 Infrastructure Ready
- 일정은 조정 가능한 계획이며 실제 완료일·Gate 승인일과 구분한다.
- 원문·후속 댓글: [원본 티켓](https://github.com/321Team/fds-project-baseline/issues/65), [고정 수집본](../sources/issue-65.json).
- 상위 속성표는 이 후보의 현행 표다. 아래 원문은 수집 시점의 변경/승인/AC 이력이며 과거 버전 문구를 현재 발행 상태로 사용하지 않는다.

## 원문 보존

<details>
<summary>수집한 GitHub 본문 전체 — SHA256 b96e7c6b8d3b79c183c552f314d9e8f9943a3d3e3e3109a477237592284916e9</summary>

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** P1-ANS 원 종결 유지. #6/#7도 Closed. #8/#5/#9 후속을 원 구축 미완료로 바꾸지 않음 ; R03.

- 원 P1-ANS 및 SSH 운영 적용 #10의 종결을 유지한다. 후속 #6/#7도 Closed다. #8 재현 키트 실제시험/리뷰와 #5 CI/#9 운영2.21.3 전환은 별도 티켓에서 추적한다.

**인계·관련 티켓:** [#10](https://github.com/321Team/fds-project-baseline/issues/10) · [#16](https://github.com/321Team/fds-project-baseline/issues/16).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:P1-ANS-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P1-ANS-01 -->
# P1-ANS-01 — Ansible Inventory / OS-Node Bootstrap — Closed Update

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

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


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **Done / closed**. 원본 갱신 시각: `2026-09-10T03:37:26Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

P1-ANS-01 원 종결(2026-08-31, HO-ANS-08/09 PASS)은 유지한다. 후속 SSH 검증식 PR #4는 5a2c3786f6af9f107200654aa12c92c3b09700f0에서 승인되고 3a02dc8934adb1f80df48ec6763689c401a1e8d6로 병합됐다. 운영 Issue #10은 6대 apply·멱등성·SFTP 확인과 독립 승인 후 종결. Gate 0 도구 PR #3 merge 5cbf3b657014b32a20cb5816d90d3ea5fe4951ab는 코드 편입이며 6대 Cluster 완료가 아니다. 2.21.3 엔진 전환 Issue #9와 NTP 목적지 승인·재검증은 잔여다.

근거: [Issue #65](https://github.com/321Team/fds-project-baseline/issues/65), Issue 갱신 시각 `2026-09-10T03:37:26Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

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

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `2e08360659f51023a9d39104a9f7c9adc38634b9be8da3ab4ba705ecf711e7c1`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P1-ANS-01 -->
# P1-ANS-01 — Ansible Inventory / OS-Node Bootstrap — Closed Update

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

<!-- fds-cp-followup-20260910:start -->
## 진행 업데이트 — 2026-09-10 후속 진단 접속 및 NTP 연계

근거: 2026-09-10 11:30:59 KST 수집본 `FDS_CP_Log_Collection_glrr0dsq.tar.gz`, SHA-256 `265e7d3fe04c8c215b8c76847bac769c5445682d788c3f9ad2bf9afef100c594`. 압축파일 및 내부 8/8 체크섬 일치. [고정 검토서](https://github.com/321Team/infra-kubernetes/blob/8975ca0c45dd9aee6d4930b16315223f86215e1d/docs/change/ICR-D-NET-01-01/CP_LOG_REVIEW_20260910.md).

승인된 SSH 키를 명시한 재수집 이후 CP 3대의 svc_ansible SSH·Python 모듈·sudo가 모두 통과했다. 이전 진단 수집기의 SSH 인증 실패는 이번 실행에서 해소 확인됐다. 이것은 CP 3대의 후속 수집 결과이며 기존 P1-ANS-01 6대 완료 증적이나 Gate 0 전체 재검증을 대체하지 않는다.

CP kubelet 설정 부재·join·클러스터 완료 판정은 [#10](https://github.com/321Team/fds-project-baseline/issues/10), CP 방화벽 보완안은 [#14](https://github.com/321Team/fds-project-baseline/issues/14) / [infra-kubernetes Draft PR #2](https://github.com/321Team/infra-kubernetes/pull/2)로 연결했다.

**NTP 잔여:** CP 3대는 1.230.135.74를 선택하고 Leap Normal을 보고하지만 고정 NTP 목적지의 승인·공통 설정 반영은 입증되지 않았다. 이권욱이 #14에서 목적지·대체 서버·UDP 123 계약을 조정하고, 공통 chrony 구성 변경은 별도 P1-ANS-01 계열 후속 변경으로 관리한다. Worker 3대의 최신 NTP 증적도 필요하다.

**기존 Closed / Done 및 이하영의 완료 리뷰·승인 기록 유지.** 새 NTP 변경이나 Kubernetes Runtime 완료를 이 티켓의 기존 PASS에 합산하지 않는다.
### 후속 수집 도구 연계 — 2026-09-10

#14/[PR #2](https://github.com/321Team/infra-kubernetes/pull/2), HEAD `0325ee798ef7bdc4e6dc582362043d899c1f3641`의 CP1 키트는 기존 승인 Inventory HEAD·SSH 키 fingerprint·known_hosts·source IP를 명시적으로 검사한다. 현재 단계는 새 읽기 전용 CP 점검이며 아직 실서버 실행 결과는 없다. Ansible 저장소/키/공통 chrony 설정을 변경하지 않았다. 기존 Closed/Done과 NTP 후속 분리 상태를 유지한다.

<!-- fds-cp-followup-20260910:end -->

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
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
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Network_Baseline_v2.3; FDS_Phase1_Logical_Architecture_v3.1.2; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 2026-08-28 TECHNICAL PASS 후 2026-08-31 이하영 Reviewer PASS·Approver APPROVED를 기록했다. HO-ANS-08·09는 PASS이며 P1-ANS-01은 Done으로 종결한다. HO-ANS-01~04는 후속 Ticket Acceptance로 이관하고 미완료 상태를 유지한다. |

## 이관 기준 및 확인 사항


- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) · [정본 WBS](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/wbs/FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx).
- 본문은 아래에 적힌 원본 버전의 기록이다. 위 속성·후속 승인과 다른 과거 상태는 현재 판정으로 사용하지 않는다. 이관 자체로 미실행 AC를 체크하거나 새 승인을 부여하지 않는다.
- Lead/Support의 풀네임은 본문 속성으로 보존한다. GitHub 계정 대응이 확인되지 않은 사람에게 자동 배정하지 않았다.

## 원본 및 변경 출처

- `FDS_Notion_Remaining_Backlog_Manual_v1.9.md`

---

## Description — 보관 입력본

> 원본: `FDS_Notion_Remaining_Backlog_Manual_v1.9.md`. 원본의 완료/미완료 체크와 당시 이력을 보존했다.

# 🎯 User Story

자동화 담당자 이권욱으로서 ansible01에서 Kubernetes 예정 노드 6대의 OS와 Node Bootstrap 설정을 일관되게 적용한다. 이를 통해 수동 설정 편차를 줄이고 동일한 구성을 반복 재현할 수 있게 한다.

---

# 📌 Scope

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

# 📋 핵심 요구사항

- [x] Inventory Group과 host_vars를 실제 Node/IP와 일치시킨다.
- [x] Secret과 Private Key를 Source에 평문 저장하지 않는다.
- [x] 적용 전 --check --diff를 수행한다.
- [x] Network Freeze 변경은 Change Request 없이는 수행하지 않는다.

---

# ✅ Acceptance Criteria

- [x] ansible all -m ping 결과가 PASS=6, FAIL=0이다.
- [x] 접속 Source가 10.250.10.10으로 확인된다.
- [x] Playbook 결과가 failed=0, unreachable=0이다.
- [x] 2차 실행 결과가 changed=0이다.
- [x] Linux/Kubernetes 선행조건 검증이 통과한다.

---

# 🧪 검증 및 증적

- ansible-inventory --graph
- Ping·Check/Diff·Apply 로그
- 2차 실행 Recap
- Secret 통제 확인
- Evidence Path: docs/evidence/P1-ANS-01/

---

# 🔗 Dependency

- **Blocked By:** D-NET-01 — Done; P1-LNX-01 — Done
- **Blocks / Next:** P1-K8S-01; MS-G1-01
- **Related Ticket:** P1-DNS-01
- **Milestone:** G1 Infrastructure Ready

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D01; D13; D25; D28; D31
- **Decision Control:** 관련 Decision은 이권욱·이하영·이재환이 확인할 수 있는 기록으로 남기며, 승인 전 조건부 작업을 시작하지 않는다.
- **Related Risk IDs:** RISK-03; RISK-04; RISK-05; RISK-14
- **Risk Control:** 예방·탐지·복구 통제를 Acceptance Criteria와 Evidence에 연결한다.

---

# 🔍 Review / Handoff

- **Review Owner:** 이하영
- **Review Result:** PASS — 2026-08-31
- **Approval Result:** APPROVED — 2026-08-31
- **Closed Control:** HO-ANS-07·08·09 PASS
- **Transferred Control:** HO-ANS-01·02A·03·04A → P1-K8S-01; HO-ANS-02B·04C → P1-SEC-01; HO-ANS-04B → P1-LB-01; Service/Probe 계약 → P1-APP-01

---

# 📝 Completion Record

- **Result:** PASS / APPROVED
- **Status:** Done
- **Exit Criteria:** ansible01 10.250.10.10에서 CP 3대·Worker 3대 Inventory/SSH PASS=6, OS·Kubernetes 선행조건 적용, 재실행 changed=0 및 Evidence 확보
- **Completed Date:** 2026-08-31
- **Reviewer / Approver:** 이하영 / 이하영 — 동일인 겸임 명시
````

</details>


</details>
