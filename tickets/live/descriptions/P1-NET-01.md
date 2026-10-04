<!-- fds-canonical-live:v3.1.21 record-id:P1-NET-01:start -->
## 현행 정본 적용 — v3.1.21

- 정본: [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21), 2026-10-04 14:49:12 KST 발행. 기준 커밋: `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`.
- [이 티켓의 발행 Description](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tickets/v3.1.21/descriptions/P1-NET-01.md) · [Baseline](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/baseline/FDS_Project_Implementation_Baseline_v3.1.21.md) · [WBS](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/wbs/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx).
- [테스트 전략](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tests/FDS_Test_Strategy_v3.1.21.md): 해당 업무의 기존 AC·Exit Criteria와 실행/인수 구분을 유지한다.
- 정본 Description은 2026-10-03 수집 시점 기록이다. 발행 후 실제 수행·검토·잔여·승인 변경은 아래 최신 운영 기록과 원본 증적을 따른다. 아래 과거 버전의 '현행/후보/미발행' 문구는 작성 당시 이력이다.
- 발행·동기화로 Status, AC 체크, 실제 완료일, 담당자, 일정, Runtime 승인 또는 종결을 상향하지 않는다. 신규 계획·사양 충돌은 별도 변경결정으로 정합화한다.
- 반영 근거: 사용자 '디스크립션 파일 반영과 이슈 본문 수정' 지시. AI 사용: CODEX_ASSISTED.
<!-- fds-canonical-live:v3.1.21 record-id:P1-NET-01:end -->

<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/D-NET-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/D-NET-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 기술 종결 유지. 실제 과거 Reviewer/Approver·시각/범위의 원본 참조 미확인 ; R04.

- Reviewer/Approver 미입력은 FUP-05에서 당시 승인자·일시·범위의 원본 URL/파일을 찾아 연결할 과제다. 과거 독립 승인자를 새로 추정해 채우지 않는다.

**인계·관련 티켓:** [#9](https://github.com/321Team/fds-project-baseline/issues/9) · [#60](https://github.com/321Team/fds-project-baseline/issues/60).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-milestone-assignment:2026-09-11 issue:67 -->
## 대표 Milestone 배정 — 2026-09-11

- **추적 Milestone:** G0 Design Freeze (GitHub #1)
- **배정 성격:** 완료 이력 · 이권욱 사용자 지시에 따른 대표 추적 항목 지정.
- **배정 근거:** 2026-08-26 종결 및 G0 Network PASS 실행 검증 근거를 기준으로 G0에 연결한다. G1 Network 선행 기여는 유지하며 FUP-04/05 잔여 이력을 완료로 확대하지 않는다.
- **출처:** [발행 정본에 보존된 종결·승인 이력](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)
- **일정 원칙:** 일정은 고정된 필수 기한이 아닌 조정 가능한 계획 목표다. 선행조건과 영향 확인 후 유연하게 조정하며, 실제 완료일·승인·Runtime 증적 요건과 구분한다.
- **적용 범위:** 대표 Milestone 연결과 이 근거 기록. 기존 상태·완료 사실·AC·담당·티켓 Start/End 및 Gate 요건을 유지한다.

---

<!-- fds-notion-migration:2026-09-09 record-id:P1-NET-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P1-NET-01 -->
# P1-NET-01 — Bridged Multi-MAC Smoke Test / Source Preservation

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P1-NET-01 |
| Phase | Phase 1 |
| Category | Network / Connectivity Validation |
| Type | Task |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-27 |
| End | 2026-08-27 |
| Calendar Days | 1 |
| Working Days | 1 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | Bridged Node 6대의 `/24`·Gateway·승인 통신 경로와 Physical/Management Return Route를 검증하고, Management Source Preservation `PASS=6`, `FAIL=0` 증적을 확보 |
| Related Decision IDs | D05; D13; D14; D15; D16 |
| Related Risk IDs | RISK-02; RISK-04 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #67 snapshot 2026-09-10T02:10:17Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 최초 계획은 2026-08-27 1일이었으나 D-NET-01 및 P1-LNX-01 통합 검증 증적이 2026-08-26 확보되어 조기 종결했다. Remaining Backlog에는 재등록하지 않고 Closed Ticket로 관리한다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **Done / closed**. 원본 갱신 시각: `2026-09-10T02:10:17Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

P1-NET-01 원 종결과 당시 Source Preservation PASS는 유지한다. FUP-04 일부 최초 원본과 FUP-05 당시 Reviewer/Approver·시각 참조는 잔여이며 새 승인자를 생성하지 않는다.

근거: [Issue #67](https://github.com/321Team/fds-project-baseline/issues/67), Issue 갱신 시각 `2026-09-10T02:10:17Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- 이 티켓은 종결 이력이다. 과거 구성 설명은 해당 종결 범위를 설명하며 현재 배포 명령으로 사용하지 않는다. 후속 설계 변경은 Baseline의 현행 절과 책임 티켓을 따른다.

---

# User Story

Infrastructure / Network 담당자 이권욱으로서 Kubernetes 예정 Physical Node 6대의 VMware Bridged 통신과 Management Return Path를 검증한다.

이를 통해 Shared L2 환경에서 Node별 Bridged 연결이 승인된 경로로 동작하고, `ansible01(10.250.10.10)`의 Management Source가 원본 주소로 유지되는지 확인하여 Kubernetes 및 Ansible 후속 구축의 네트워크 선행조건을 종결한다.

---

# Scope

## In Scope

- Kubernetes 예정 Physical Node 6대의 Bridged NIC 및 `/24` Prefix 확인
- Default Gateway `10.1.93.254` 설정 확인
- Node 간 승인된 Physical 경로의 통신 확인
- Physical Node의 `10.250.10.0/24 via 10.1.93.58` Return Route 확인
- `ansible01(10.250.10.10)`에서 Physical Node로 접속 시 Remote Observed Source 확인
- Management Source Preservation `PASS=6`, `FAIL=0` 검증
- DAD / ARP / Route / 승인 TCP 경로 기반 Positive·Negative Test
- Network Baseline 및 Closure Evidence 연결

## Out of Scope

- `containerd`, `kubelet`, `kubeadm`, Kubernetes API Server 및 Calico 구성
- Kubernetes Required Port의 서비스 기동 완료 판정
- BIND Primary / Secondary 및 `fds.internal` 구축
- Reverse Zone / PTR
- 현장 Gateway `10.1.93.254`의 설정 변경 또는 관리권 확보
- Phase 2 OCI / AWS VPN 구성

---

# 핵심 요구사항

- [x] Physical Node 6대의 Bridged Interface가 Physical LAN `10.1.93.0/24`에 연결된다.
- [x] 각 Node의 Prefix가 `/24`로 설정되어 있다.
- [x] 각 Node의 Default Gateway가 `10.1.93.254`로 설정되어 있다.
- [x] 모든 Physical Node에 `10.250.10.0/24 via 10.1.93.58` Return Route가 존재한다.
- [x] 내부 Physical / Management 경로에 Source NAT를 적용하지 않는다.
- [x] Management Source를 `10.250.10.10` 원본 주소로 보존한다.
- [x] `.100`, `.101`, `.106`은 `DO_NOT_USE`로 유지하고 FDS VM에 할당하지 않는다.
- [x] 프로젝트 비관리 Gateway의 Ping 단독 결과를 완료 Gate로 사용하지 않는다.

---

# Acceptance Criteria

- [x] Bridged Node 6대의 Prefix가 모두 `/24`다.
- [x] Bridged Node 6대의 Default Gateway가 모두 `10.1.93.254`다.
- [x] Physical / Management Return Route가 `10.1.93.58` 경유로 정상 동작한다.
- [x] Node 간 승인 경로 통신이 정상이다.
- [x] `ansible01(10.250.10.10)`에서 접속할 때 Remote Observed Source가 `10.250.10.10`으로 유지된다.
- [x] Management Source Preservation 결과가 `PASS=6`, `FAIL=0`이다.
- [x] 관련 Linux Network Verify 결과가 `FAIL=0`이다.
- [x] 비관리 Gateway의 ICMP 응답 여부와 무관하게 Route / ARP / 승인 TCP 경로로 합격 근거를 확보했다.

---

# Test Result

| TC ID | 검증 항목 | 예상 결과 | 실제 결과 | 판정 |
|---|---|---|---|---|
| TC-P1NET-01 | Node 6대 Prefix / Gateway | `/24`, Gateway `10.1.93.254` | 기준값 일치 | PASS |
| TC-P1NET-02 | Bridged Node 승인 경로 | Node 간 승인 경로 통신 가능 | 통신 정상 | PASS |
| TC-P1NET-03 | Management Return Route | `10.250.10.0/24 via 10.1.93.58` | 6대 경로 정상 | PASS |
| TC-P1NET-04 | Source Preservation | Remote Observed Source=`10.250.10.10` | `PASS=6`, `FAIL=0` | PASS |
| TC-P1NET-05 | Gateway 비관리 조건 | Ping 단독이 아닌 Route / ARP / TCP로 판정 | 승인 경로 증적 확보 | PASS |
| TC-P1NET-06 | 사용금지 IP Negative Test | `.100/.101/.106` 미할당 | `DO_NOT_USE` 유지 | PASS |

---

# 검증 및 증적

## Primary Evidence

- `03_Linux_Node_Network_Verify`
- `05_Physical_Return_Route`
- `06_Source_Preservation_PASS6`
- `07_Management_VM_Verify`

## Supporting Evidence

- `01_Windows_PostBuild_server01-08`
- `02_VMware_Virtual_Network_Editor`
- `04_K8s_Linux_Prerequisites`
- `08_mgmt-gw01_Verify`
- `09_DO_NOT_USE_IP_Exception`
- `10_D-NET-01_Closure`

## Evidence Location / Source

- Evidence Path: `321Team/fds-project-evidence:evidence/D-NET-01/`
- Configuration Baseline: `FDS_Network_Baseline_v2.3`
- Closure Record: `D-NET-01_Closure_Report_v1.0`
- Parameter Patch: `FDS_Notion_Network_Parameter_Patch_v1.2`
- Closed Register: `FDS_Remaining_Backlog_WBS_v3.1.5`

> P1-NET-01은 D-NET-01 및 P1-LNX-01 수행 과정에서 확보된 공통 Network Evidence를 재사용한다. 증적 제출 시 위 인덱스의 실제 로그·요약·캡처 파일을 함께 첨부한다.

---

# Dependency

- **Blocked By:** `D-NET-01`, `P1-LNX-01` — `DONE / CLOSED`
- **Blocks / Next:** `P1-ANS-01`, `P1-K8S-01`, G1 Infrastructure Ready
- **Related Ticket:** `D-NET-01`, `P1-LNX-01`, `P1-ANS-01`, `P1-K8S-01`
- **Milestone Contribution:** G0 Network `PASS`의 실행 검증 근거 및 G1 Network 선행조건

---

# Decision / Risk Control

- **Related Decision IDs:** `D05`, `D13`, `D14`, `D15`, `D16`
- **Decision Control:** Bridged Endpoint, VMnet 분리, Return Route, 내부 Source NAT 금지, 비관리 Gateway 및 Reserved / DO_NOT_USE 주소 결정을 준수한다.
- **Related Risk IDs:** `RISK-02`, `RISK-04`
- **Risk Control:** Bridged Multi-MAC 제한은 Node 6대 실제 통신으로 검증하고, 비관리 Gateway는 Ping 단독이 아닌 Route / ARP / 승인 TCP 경로로 판정한다.
- **Change Control:** IP, Prefix, Gateway, VMnet 역할, Route, NAT 또는 승인 통신 경로 변경은 Network / Interface Change Request 후 반영한다.

---

# Completion Record

- **Result:** `PASS`
- **Status:** `DONE`
- **Ticket Gate:** `CLOSED`
- **Lead:** 이권욱
- **Support:** 이하영
- **Original Plan:** `2026-08-27` / 1일
- **Completed Date:** `2026-08-26`
- **Exit Criteria:** Bridged Node 6대 Connectivity, Physical / Management Return Route, Management Source Preservation `PASS=6`, `FAIL=0`, 관련 Network Verify `FAIL=0`
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
- **Closure Basis:** `FDS_Network_Baseline_v2.3`, `D-NET-01_Closure_Report_v1.0`, `FDS_Notion_Network_Parameter_Patch_v1.2`, `FDS_Remaining_Backlog_WBS_v3.1.5`
- **Closure Boundary:** 본 종결은 Bridged Connectivity와 Management Source Preservation 범위에 한한다. Kubernetes 서비스 및 Required Port 기동 완료는 `P1-K8S-01`에서 판정한다.
- **Next:** 종결 이력을 유지하고 `P1-ANS-01`, `P1-K8S-01`의 선행 Network Evidence로 연결한다.

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `7f5b7b7f6d6e38c92f0017ad4509921e5f3ad0f15a87b3145a71878aea34c396`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P1-NET-01 -->
# P1-NET-01 — Bridged Multi-MAC Smoke Test / Source Preservation

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P1-NET-01 |
| Phase | Phase 1 |
| Category | Network / Connectivity Validation |
| Type | Task |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-27 |
| End | 2026-08-27 |
| Calendar Days | 1 |
| Working Days | 1 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | Bridged Node 6대의 `/24`·Gateway·승인 통신 경로와 Physical/Management Return Route를 검증하고, Management Source Preservation `PASS=6`, `FAIL=0` 증적을 확보 |
| Related Decision IDs | D05; D13; D14; D15; D16 |
| Related Risk IDs | RISK-02; RISK-04 |
| Source | FDS_Project_Implementation_Baseline_v3.1.5; FDS_Remaining_Backlog_WBS_v3.1.5; FDS_Network_Baseline_v2.3; D-NET-01_Closure_Report_v1.0; FDS_Notion_Network_Parameter_Patch_v1.2; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 최초 계획은 2026-08-27 1일이었으나 D-NET-01 및 P1-LNX-01 통합 검증 증적이 2026-08-26 확보되어 조기 종결했다. Remaining Backlog에는 재등록하지 않고 Closed Ticket로 관리한다. |

## 이관 기준 및 확인 사항


- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) · [정본 WBS](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/wbs/FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx).
- 본문은 아래에 적힌 원본 버전의 기록이다. 위 속성·후속 승인과 다른 과거 상태는 현재 판정으로 사용하지 않는다. 이관 자체로 미실행 AC를 체크하거나 새 승인을 부여하지 않는다.
- Lead/Support의 풀네임은 본문 속성으로 보존한다. GitHub 계정 대응이 확인되지 않은 사람에게 자동 배정하지 않았다.

## 원본 및 변경 출처

- `FDS_Notion_Closed_Ticket_P1-NET-01_v1.0.md`

---

## Description — 보관 입력본

> 원본: `FDS_Notion_Closed_Ticket_P1-NET-01_v1.0.md`. 원본의 완료/미완료 체크와 당시 이력을 보존했다.

# 🎯 User Story

Infrastructure / Network 담당자 이권욱으로서 Kubernetes 예정 Physical Node 6대의 VMware Bridged 통신과 Management Return Path를 검증한다.

이를 통해 Shared L2 환경에서 Node별 Bridged 연결이 승인된 경로로 동작하고, `ansible01(10.250.10.10)`의 Management Source가 원본 주소로 유지되는지 확인하여 Kubernetes 및 Ansible 후속 구축의 네트워크 선행조건을 종결한다.

---

# 📌 Scope

## In Scope

- Kubernetes 예정 Physical Node 6대의 Bridged NIC 및 `/24` Prefix 확인
- Default Gateway `10.1.93.254` 설정 확인
- Node 간 승인된 Physical 경로의 통신 확인
- Physical Node의 `10.250.10.0/24 via 10.1.93.58` Return Route 확인
- `ansible01(10.250.10.10)`에서 Physical Node로 접속 시 Remote Observed Source 확인
- Management Source Preservation `PASS=6`, `FAIL=0` 검증
- DAD / ARP / Route / 승인 TCP 경로 기반 Positive·Negative Test
- Network Baseline 및 Closure Evidence 연결

## Out of Scope

- `containerd`, `kubelet`, `kubeadm`, Kubernetes API Server 및 Calico 구성
- Kubernetes Required Port의 서비스 기동 완료 판정
- BIND Primary / Secondary 및 `fds.internal` 구축
- Reverse Zone / PTR
- 현장 Gateway `10.1.93.254`의 설정 변경 또는 관리권 확보
- Phase 2 OCI / AWS VPN 구성

---

# 📋 핵심 요구사항

- [x] Physical Node 6대의 Bridged Interface가 Physical LAN `10.1.93.0/24`에 연결된다.
- [x] 각 Node의 Prefix가 `/24`로 설정되어 있다.
- [x] 각 Node의 Default Gateway가 `10.1.93.254`로 설정되어 있다.
- [x] 모든 Physical Node에 `10.250.10.0/24 via 10.1.93.58` Return Route가 존재한다.
- [x] 내부 Physical / Management 경로에 Source NAT를 적용하지 않는다.
- [x] Management Source를 `10.250.10.10` 원본 주소로 보존한다.
- [x] `.100`, `.101`, `.106`은 `DO_NOT_USE`로 유지하고 FDS VM에 할당하지 않는다.
- [x] 프로젝트 비관리 Gateway의 Ping 단독 결과를 완료 Gate로 사용하지 않는다.

---

# ✅ Acceptance Criteria

- [x] Bridged Node 6대의 Prefix가 모두 `/24`다.
- [x] Bridged Node 6대의 Default Gateway가 모두 `10.1.93.254`다.
- [x] Physical / Management Return Route가 `10.1.93.58` 경유로 정상 동작한다.
- [x] Node 간 승인 경로 통신이 정상이다.
- [x] `ansible01(10.250.10.10)`에서 접속할 때 Remote Observed Source가 `10.250.10.10`으로 유지된다.
- [x] Management Source Preservation 결과가 `PASS=6`, `FAIL=0`이다.
- [x] 관련 Linux Network Verify 결과가 `FAIL=0`이다.
- [x] 비관리 Gateway의 ICMP 응답 여부와 무관하게 Route / ARP / 승인 TCP 경로로 합격 근거를 확보했다.

---

# 🧪 Test Result

| TC ID | 검증 항목 | 예상 결과 | 실제 결과 | 판정 |
|---|---|---|---|---|
| TC-P1NET-01 | Node 6대 Prefix / Gateway | `/24`, Gateway `10.1.93.254` | 기준값 일치 | PASS |
| TC-P1NET-02 | Bridged Node 승인 경로 | Node 간 승인 경로 통신 가능 | 통신 정상 | PASS |
| TC-P1NET-03 | Management Return Route | `10.250.10.0/24 via 10.1.93.58` | 6대 경로 정상 | PASS |
| TC-P1NET-04 | Source Preservation | Remote Observed Source=`10.250.10.10` | `PASS=6`, `FAIL=0` | PASS |
| TC-P1NET-05 | Gateway 비관리 조건 | Ping 단독이 아닌 Route / ARP / TCP로 판정 | 승인 경로 증적 확보 | PASS |
| TC-P1NET-06 | 사용금지 IP Negative Test | `.100/.101/.106` 미할당 | `DO_NOT_USE` 유지 | PASS |

---

# 🧪 검증 및 증적

## Primary Evidence

- `03_Linux_Node_Network_Verify`
- `05_Physical_Return_Route`
- `06_Source_Preservation_PASS6`
- `07_Management_VM_Verify`

## Supporting Evidence

- `01_Windows_PostBuild_server01-08`
- `02_VMware_Virtual_Network_Editor`
- `04_K8s_Linux_Prerequisites`
- `08_mgmt-gw01_Verify`
- `09_DO_NOT_USE_IP_Exception`
- `10_D-NET-01_Closure`

## Evidence Location / Source

- Evidence Path: `docs/evidence/D-NET-01/`
- Configuration Baseline: `FDS_Network_Baseline_v2.3`
- Closure Record: `D-NET-01_Closure_Report_v1.0`
- Parameter Patch: `FDS_Notion_Network_Parameter_Patch_v1.2`
- Closed Register: `FDS_Remaining_Backlog_WBS_v3.1.5`

> P1-NET-01은 D-NET-01 및 P1-LNX-01 수행 과정에서 확보된 공통 Network Evidence를 재사용한다. 증적 제출 시 위 인덱스의 실제 로그·요약·캡처 파일을 함께 첨부한다.

---

# 🔗 Dependency

- **Blocked By:** `D-NET-01`, `P1-LNX-01` — `DONE / CLOSED`
- **Blocks / Next:** `P1-ANS-01`, `P1-K8S-01`, G1 Infrastructure Ready
- **Related Ticket:** `D-NET-01`, `P1-LNX-01`, `P1-ANS-01`, `P1-K8S-01`
- **Milestone Contribution:** G0 Network `PASS`의 실행 검증 근거 및 G1 Network 선행조건

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** `D05`, `D13`, `D14`, `D15`, `D16`
- **Decision Control:** Bridged Endpoint, VMnet 분리, Return Route, 내부 Source NAT 금지, 비관리 Gateway 및 Reserved / DO_NOT_USE 주소 결정을 준수한다.
- **Related Risk IDs:** `RISK-02`, `RISK-04`
- **Risk Control:** Bridged Multi-MAC 제한은 Node 6대 실제 통신으로 검증하고, 비관리 Gateway는 Ping 단독이 아닌 Route / ARP / 승인 TCP 경로로 판정한다.
- **Change Control:** IP, Prefix, Gateway, VMnet 역할, Route, NAT 또는 승인 통신 경로 변경은 Network / Interface Change Request 후 반영한다.

---

# 📝 Completion Record

- **Result:** `PASS`
- **Status:** `DONE`
- **Ticket Gate:** `CLOSED`
- **Lead:** 이권욱
- **Support:** 이하영
- **Original Plan:** `2026-08-27` / 1일
- **Completed Date:** `2026-08-26`
- **Exit Criteria:** Bridged Node 6대 Connectivity, Physical / Management Return Route, Management Source Preservation `PASS=6`, `FAIL=0`, 관련 Network Verify `FAIL=0`
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
- **Closure Basis:** `FDS_Network_Baseline_v2.3`, `D-NET-01_Closure_Report_v1.0`, `FDS_Notion_Network_Parameter_Patch_v1.2`, `FDS_Remaining_Backlog_WBS_v3.1.5`
- **Closure Boundary:** 본 종결은 Bridged Connectivity와 Management Source Preservation 범위에 한한다. Kubernetes 서비스 및 Required Port 기동 완료는 `P1-K8S-01`에서 판정한다.
- **Next:** 종결 이력을 유지하고 `P1-ANS-01`, `P1-K8S-01`의 선행 Network Evidence로 연결한다.
````

</details>
