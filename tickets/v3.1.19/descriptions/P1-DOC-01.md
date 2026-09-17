# P1-DOC-01 — Architecture / Test / Runbook Freeze

> v3.1.19 CANDIDATE / NOT RELEASED · 2026-09-17 20:28 KST

## 현행 속성

| Property | 입력값 |
|---|---|
| Record ID | P1-DOC-01 |
| Phase | Phase 1 |
| Category | PMO / Documentation |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-09-11 |
| End | 2026-09-22 |
| Calendar Days | 12 |
| Working Days | 8 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | As-built Architecture, Test/Evidence Index, 구축·운영·복구 Runbook, P1 미완료 Known Issue의 풀네임 Owner·Due, Version/Source 및 Review 재현성 승인 |
| Related Decision IDs | D12; D20; D25 |
| Related Risk IDs | RISK-05; RISK-13 |
| Source | Baseline v3.1.19 CANDIDATE; GitHub #24 @ 2026-09-17T08:44:24Z; 원문 SHA256 8e5048acc49c8621747036729d3f1cba21a1fd040b2c7771222c415932539ae3 |
| Schedule Note | 구축 시 증적·Runbook을 병행 축적하고 09-22 오전 Final Evidence와 함께 동결한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |

## 상태와 인수 경계

현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다.

- GitHub lifecycle: open; Milestone: G3 Review Ready
- 일정은 조정 가능한 계획이며 실제 완료일·Gate 승인일과 구분한다.
- 원문·후속 댓글: [원본 티켓](https://github.com/321Team/fds-project-baseline/issues/24), [고정 수집본](../sources/issue-24.json).
- 상위 속성표는 이 후보의 현행 표다. 아래 원문은 수집 시점의 변경/승인/AC 이력이며 과거 버전 문구를 현재 발행 상태로 사용하지 않는다.

## 원문 보존

<details>
<summary>수집한 GitHub 본문 전체 — SHA256 8e5048acc49c8621747036729d3f1cba21a1fd040b2c7771222c415932539ae3</summary>

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 현재 계약/As-built·WBS/Ticket/Evidence/Notes·Manifest 전체 대응 ; A04~A07/R01~R06.

**전체 수집 범위:** 일반 Issue78개(Open58/Closed20), 열린 PR10개. 사양/인수 입력7묶음(A01~A07)·기록6묶음(R01~R06)을 각 담당 티켓에 연결한다. 아래 ID는 점검표 내부 참조이며 신규 Ticket/Decision ID나 새 승인값이 아니다.

**이번 갱신의 범위:** GitHub Issue 실행·협업 기록을 갱신한다. CURRENT/README·Baseline/WBS/Ticket Pack/Manifest·PR#73 실제 수집 파일과 v19 배포 묶음의 수정/리뷰/발행은 아래 후속으로 남는다.

### A01 — NTP 실행·인수 입력

승인 시간 소스·운영 주체, 노드별 Source/Return·UDP123, 허용 오프셋·표본 주기/횟수·실패 처리·지속성 결과를 확정한다. `100ms·60초×6`은 미승인 초안이다. 해당 변경/인수 전 입력이며 읽기 전용 준비 전체의 신규 중단 조건이 아니다.

근거·실행 티켓: [ICR #14](https://github.com/321Team/fds-project-baseline/issues/14) · [K8S #10](https://github.com/321Team/fds-project-baseline/issues/10) · [SEC #19](https://github.com/321Team/fds-project-baseline/issues/19)

### A02 — CNI·MTU·CP1 인수

CP1 제한 Runtime 적용/롤백/최종 재적용과 TCP6/6 기록은 유지하되 최종 ACCEPTED는 CNI 회귀와 이하영 인수 회신 대기다. MTU1450은 후보이며 cross-node 실측으로 확정한다. trial의 시작부터 최대20분·마지막3분 정리 방향과 현재 `--until` 방식의 구현 차이를 추적한다. CP2 조사·보존/정리/재개 결정은 별도다.

근거·실행 티켓: [CP1 인수 보류](https://github.com/321Team/infra-kubernetes/pull/2#issuecomment-5662853042) · [ICR](https://github.com/321Team/fds-project-baseline/issues/14) · [PR #9 리뷰](https://github.com/321Team/infra-kubernetes/pull/9#pullrequestreview-5197580718)

### A03 — Worker Drain 합격 기준

3 Replica·Worker 분산을 유지하고 시험 URL/요청 유형·간격·관찰 구간·허용 오류/연속 실패·응답시간 사용 여부·Local endpoint·재배치/uncordon 합격값을 시험 전에 기록한다. 값은 아직 미확정이며 임시 단일노드 k3s 로그를 정본 무중단 AC로 사용하지 않는다.

근거·실행 티켓: [HA #22](https://github.com/321Team/fds-project-baseline/issues/22) · [시험 한계](https://github.com/321Team/fds-project-baseline/issues/22#issuecomment-5612847714)

### A04 — 현재 앱·Rule·시간 계약

앱 main `01758583c03bcbf45c96eb9d7b868cee4a2ed9df`를 현재 접근 가능한 소스로 연결한다. 계약 v1.0은 DRAFT·실패정책 OPEN·옛 Probe/P1-MSA-01 표기가 남아 있다. 구현의 엔진 실패 fail-open(connect1s/read2s), DB 실패 rollback/HTTP500, R04 KST01:00≤시각<05:00·100만원 이상을 소스/fixture/승인 근거와 대조한다. UTC 전송·KST 판정은 양립 가능하다. 입력 offset/naive 처리·DB timezone·저장 자료형·표시 기준을 분리해 기록하며 새 정책 승인으로 간주하지 않는다.

근거·실행 티켓: [계약](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/docs/transaction-api_fds-engine_contract_v1.0.md) · [Rule](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/fds-engine/app/rules.py) · [API](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/transaction-api/app/main.py) · [client](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/transaction-api/app/fds_client.py)

### A05 — 정본 Monitoring 배포 입력

현재 main의 prometheus.yaml은 임시 fds/업무포트·latest·emptyDir 설정이며 “실6Node의 Prometheus는 monitor01” 주석은 현행 정본과 다르다. E-K3S 참고와 E-CANON 적용 source/overlay·render SHA를 구분한다. monitoring-api/monitoring-node·metrics9091/9090·고정 Digest·SA와 3종 PVC의 SC/PV/Worker/host path/용량/UID/fsGroup·Resource 인계를 기록한다. WaitForFirstConsumer·Retain·15일 목표/PVC80% 상한은 이미 정해진 값이다.

근거·실행 티켓: [MON #17](https://github.com/321Team/fds-project-baseline/issues/17) · [현재 Prometheus 소스](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/kubernetes/monitoring/prometheus.yaml)

### A06 — OID·IF-06B 경로 인계

OID-01 관리자 Source/Identity, OID-02 CP/Calico/system image source/Digest·pull 경로, OID-03 bootstrap 반입 또는 최소 HTTPS 목적지/Owner/Expiry를 해당 실행 전에 확정한다. IF-06B는 in-cluster Prometheus→monitor01 10.250.10.30:443으로 주소/방향이 확인됐다. 실제 Source/Return·TLS path/auth·Secret 참조·self-metric allowlist와 긍정/부정 결과가 필요하다. heartbeat=1·5분 단절 탐지는 확정값이며 OID-04 관리망 DNS N/A를 확대하지 않는다.

근거·실행 티켓: [ICR #14](https://github.com/321Team/fds-project-baseline/issues/14) · [MON #17](https://github.com/321Team/fds-project-baseline/issues/17) · [SEC 부분 수용](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5654476728)

### A07 — 프록시 As-built·운영 계정 인계

server08/egress-proxy01·2vCPU/2GiB/30GiB·ens160 .56/24·DNS .52/.53, DNS UDP/TCP4/4와 관리 .10→.56:22 runtime/permanent·반환 .10/32 via .58·관리자 SSH 결과를 자산/IP/IF/inventory에 연결한다. svc_ansible 생성은 완료됐지만 공개키·sudo 범위·svc SSH·Ansible module/become 검증은 미완료다. 기존 control01의 NOPASSWD:ALL 확인을 프록시 권한 부여로 전용하지 않는다. Squid3128 적용은 rollback 결함/리뷰로 HOLD, 실제 Alertmanager source/selector·Secret 참조·허용/거부/복구·#75 인계는 잔여다.

근거·실행 티켓: [배치/실측 #78](https://github.com/321Team/fds-project-baseline/issues/78) · [관리 경로](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5663718791) · [계정](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5663963879) · [변경 요청](https://github.com/321Team/infra-ansible/pull/12#pullrequestreview-5195815386)

### R01 — Harbor/CA/CICD 결정 동기화

Robot Never 미채택·유한30일, Scanner 유지, 미해결 Critical/High의 Push/Deploy 차단과 오류 실패/미검증 처리는 9/14 사용자 결정이다. 예외는 CVE/Digest/사유/만료/승인자로 기록한다. ca01의 server01·2vCPU/4GiB·OS40GiB+CA2GiB LUKS2와 PR준비안 OS20GiB의 차이를 As-built에 남긴다. 새 Root 선택과 실제 발급을 구분하며 별도 암호화 백업/복구는 Harbor 적용·trust 배포 전에 확인한다.

근거·실행 티켓: [Harbor 정책](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5659049448) · [CICD 정책](https://github.com/321Team/fds-project-baseline/issues/16#issuecomment-5659051242) · [CA 진행 #16](https://github.com/321Team/fds-project-baseline/issues/16)

### R02 — DB 병합·운영·복구 기록

앱 PR#2는 2026-09-11T03:01:53Z에 84a79c8550d23737b15eda3aacb8950ceafd8d17로 병합됐고 0002가 main에 있다. “PR 병합 필요”는 과거 상태다. 운영 db01의 schema fingerprint/revision·stamp 또는 조건부 변경 판단·백업/rollback과 신규 DB upgrade 재현은 별도로 기록한다. dump 원본 URI/해시/DB버전·시각·독립 확인/Restore·Row/Rule/E2E 증거는 미완료 범위로 유지한다.

근거·실행 티켓: [앱 PR #2](https://github.com/supreme33-kr/fds-msa/pull/2) · [0002](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/alembic/versions/0002_add_fds_evaluation_columns.py) · [DB #11](https://github.com/321Team/fds-project-baseline/issues/11) · [DR #21](https://github.com/321Team/fds-project-baseline/issues/21)

### R03 — 최신 리뷰·증적 보관

Ansible #6/#7은 Closed. #8의 실제 새 Linux localhost fixture PASS와 코드PR#16 d2d46bd95ece3935373303187ef47cfc5e3e2eb7의 이하영 COMMENTED를 연결한다. 증적PR#12 1ffdd67a2cd1fc5f67ac5829b049ca01a90bcb13는 formal review0·검토댓글1, 두PR 미병합이다. 원문81+검토6=87개 원격 편입과 전체711개 압축의 로컬 보존을 구분하고 공용 원본 URI/접근/리뷰 범위를 남긴다. SEC PR#7 실제HEAD122e3b4의 부분수용·HOLD와 본문의 옛HEAD/대기표기를 대조한다.

근거·실행 티켓: [Ansible #8](https://github.com/321Team/infra-ansible/issues/8) · [코드 리뷰](https://github.com/321Team/infra-ansible/pull/16#pullrequestreview-5198204062) · [증적 PR #12](https://github.com/321Team/fds-project-evidence/pull/12) · [SEC PR #7](https://github.com/321Team/infra-kubernetes/pull/7)

### R04 — 종결 승인·원본 참조

P1-NET #67의 당시 Reviewer/Approver·일시/범위는 FUP-05의 기존 참조로 보완한다. FUP-04 최초 원본, FUP-06/07 개인별 회신/정확한 시각/WBS 열람, FUP-09 DAD 원본과 이하영의 Supplement 조건 판단은 잔여다. 현재 Permanent Supplement의 수신·독립승인·main편입은 완료돼 있다. 기존 Done·Stage A PASS·조건부 인수·Bootstrap HOLD를 보존하며 소급 승인 서명을 만들지 않는다.

근거·실행 티켓: [#67](https://github.com/321Team/fds-project-baseline/issues/67) · [FUP 후속](https://github.com/321Team/fds-project-evidence/issues/4) · [매핑 PR #7](https://github.com/321Team/fds-project-evidence/pull/7)

### R05 — 발행 메타데이터·v19 실제 편입

실제 docs-v3.1.18은 2026-09-11T02:23:47Z 발행됐다. CURRENT의 NOT PUBLISHED/준비 문구는 정정 대상이다. PR#73 HEAD89a3dbc86ac3034f2e1c720f9828523980cc24ee는 Draft 수집이며 9/14 댓글 연결이 실제 파일·전체 bundle 편입 완료를 뜻하지 않는다. 78개 Issue·최신 PR/실행·앱 저장소 source를 Baseline/WBS/Ticket/As-built/IF/Evidence/Notes/Manifest에 대조 편입한다.

근거·실행 티켓: [Release](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · [CURRENT](https://github.com/321Team/fds-project-baseline/blob/main/CURRENT.md) · [PR #73 files](https://github.com/321Team/fds-project-baseline/pull/73/files)

### R06 — native 속성·보조 ID 매핑

#78 전체 Issue API에서 native Type/Milestone null을 확인했다. 본문 Decision과 실제속성·단일 Gate/비차단 근거의 대응은 후속 기록이며 이번 본문 갱신으로 완료 처리하지 않는다. D/IF는 레지스터 대조 후 번호를 부여한다. P1-MSA-01/P1-DB-03/P1-DB-05는 현재 #15/#11 또는 로컬 세부작업과 매핑한다. 기존 Risk ID의 역사적 참조 제한을 유지하고 실제 위험 수용 전 현행 정의/승인 출처를 고정한다.

근거·실행 티켓: [#78](https://github.com/321Team/fds-project-baseline/issues/78) · [DB 보조 ID](https://github.com/321Team/infra-db/issues/1) · [범위 결정 #4](https://github.com/321Team/fds-project-baseline/issues/4)

**담당:** 이권욱은 정본·수집/As-built/Interface·일정·증적 출처를 연결하고, 이하영은 기존 정본 독립 리뷰·보안/플랫폼 인수 역할을 유지한다. 이재환은 APP/DB/MON 계약과 증적 구현/리뷰를 인계한다. 실제 source·전체 SHA·review permalink·결과·미검증 범위가 각각 대응하도록 편입한다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:P1-DOC-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P1-DOC-01 -->
# P1-DOC-01 — Architecture / Test / Runbook Freeze

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P1-DOC-01 |
| Phase | Phase 1 |
| Category | PMO / Documentation |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-09-11 |
| End | 2026-09-22 |
| Calendar Days | 12 |
| Working Days | 8 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | As-built Architecture, Test/Evidence Index, 구축·운영·복구 Runbook, P1 미완료 Known Issue의 풀네임 Owner·Due, Version/Source 및 Review 재현성 승인 |
| Related Decision IDs | D12; D20; D25 |
| Related Risk IDs | RISK-05; RISK-13 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #24 snapshot 2026-09-10T02:09:36Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청 |
| Schedule Note | 구축 시 증적·Runbook을 병행 축적하고 09-22 오전 Final Evidence와 함께 동결한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-10T02:09:36Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

이번 v3.1.18은 정본 후보의 누적 이력·설명·배포 정합성 통합 작업이다. 독립 리뷰·명시적 병합 승인·발행은 아직 없으며 P1-DOC 전체 문서 Freeze/Done을 의미하지 않는다. 정본 발행 뒤 Issue Description 최신화, 마지막에 속성 재계획을 수행한다. 현재 후보 Plan: 2026-09-11 ~ 2026-09-22 (권장안; 실제 완료일·Gate 승인은 미확정).

근거: [Issue #24](https://github.com/321Team/fds-project-baseline/issues/24), Issue 갱신 시각 `2026-09-10T02:09:36Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 일정 권장안

Start/End는 이번 Fast Tracking 후보의 계획값이다. 기존 승인 일정은 `audit/v3.1.18/fast-track-plan.json`에 전후 값으로 보존한다. 실제 착수·완료·Status·AC·승인을 변경한 것이 아니다. 교육장 주말 작업은 없으며 세부 AM/PM 배정과 선행 조건을 따른다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

PMO 담당자로서 Phase 1의 설계·구축·검증 정보를 재현 가능한 정본으로 동결한다. 이를 통해 Review가 개인 설명에 의존하지 않고 문서와 Evidence로 반복 가능하게 한다.

---

# Scope

## In Scope

- As-built Architecture
- Configuration Inventory
- Test/Evidence Index
- Runbook
- Known Issue
- Version Trace

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] 설계와 실제 IP/Port/배치를 대조한다.
- [ ] 각 P0 Exit Criteria를 Evidence와 연결한다.
- [ ] 복구와 Rollback 명령의 전제조건을 명시한다.
- [ ] 금융 규제 준수 완료 표현을 금지한다.

---

# Acceptance Criteria

- [ ] P0 Ticket별 Evidence 링크가 존재한다.
- [ ] As-built와 Baseline 차이가 Change/Known Issue로 기록된다.
- [ ] 제3자가 Runbook으로 핵심 검증을 재현할 수 있다.
- [ ] Critical 문서 결함이 0건이다.

---

# 검증 및 증적

- Deliverable Index
- As-built Diagram
- Test Report
- Runbook Review
- Known Issue Register
- Evidence Path: `docs/evidence/P1-DOC-01/`

---

# Dependency

- **Blocked By:** P1-HA-01, P1-DR-01, P1-E2E-01
- **Blocks / Next:** P1-REV-01
- **Related Ticket:** 전체 Phase 1
- **Milestone:** G3 Review Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D12; D20
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-05; RISK-13
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** As-built Architecture, Test/Evidence Index, 구축·운영·복구 Runbook, Known Issue, Version/Source 및 Review 재현성 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `6162bb43b787b524feb5f2bebbf9b188179ff6595bce70d23a6681d20dbfe23c`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P1-DOC-01 -->
# P1-DOC-01 — Architecture / Test / Runbook Freeze

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P1-DOC-01 |
| Phase | Phase 1 |
| Category | PMO / Documentation |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-09-12 |
| End | 2026-09-18 |
| Calendar Days | 7 |
| Working Days | 5 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | As-built Architecture, Test/Evidence Index, 구축·운영·복구 Runbook, P1 미완료 Known Issue의 풀네임 Owner·Due, Version/Source 및 Review 재현성 승인 |
| Related Decision IDs | D12; D20; D25 |
| Related Risk IDs | RISK-05; RISK-13 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Network_Baseline_v2.3; FDS_Phase1_Logical_Architecture_v3.1.2; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 이재환 부재 전 09-13까지 HA/DR Evidence 초안을 인계하고 09-18 최종 검토한다. |

## 이관 기준 및 확인 사항

- 속성의 일정·담당·상태는 RELEASED v3.1.17 WBS(기준일 2026-09-04)를 우선 반영했다. 이후 별도 근거가 있는 변경만 아래에 명시한다.
- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) · [정본 WBS](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/wbs/FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx).
- 본문은 아래에 적힌 원본 버전의 기록이다. 위 속성·후속 승인과 다른 과거 상태는 현재 판정으로 사용하지 않는다. 이관 자체로 미실행 AC를 체크하거나 새 승인을 부여하지 않는다.
- Lead/Support의 풀네임은 본문 속성으로 보존한다. GitHub 계정 대응이 확인되지 않은 사람에게 자동 배정하지 않았다.

## 원본 및 변경 출처

- `FDS_Notion_Remaining_Backlog_Manual_v1.9.md`
- `FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx`

---

## Description — 보관 입력본

> 원본: `FDS_Notion_Remaining_Backlog_Manual_v1.9.md`. 원본의 완료/미완료 체크와 당시 이력을 보존했다.

# 🎯 User Story

PMO 담당자로서 Phase 1의 설계·구축·검증 정보를 재현 가능한 정본으로 동결한다. 이를 통해 Review가 개인 설명에 의존하지 않고 문서와 Evidence로 반복 가능하게 한다.

---

# 📌 Scope

## In Scope

- As-built Architecture
- Configuration Inventory
- Test/Evidence Index
- Runbook
- Known Issue
- Version Trace

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 📋 핵심 요구사항

- [ ] 설계와 실제 IP/Port/배치를 대조한다.
- [ ] 각 P0 Exit Criteria를 Evidence와 연결한다.
- [ ] 복구와 Rollback 명령의 전제조건을 명시한다.
- [ ] 금융 규제 준수 완료 표현을 금지한다.

---

# ✅ Acceptance Criteria

- [ ] P0 Ticket별 Evidence 링크가 존재한다.
- [ ] As-built와 Baseline 차이가 Change/Known Issue로 기록된다.
- [ ] 제3자가 Runbook으로 핵심 검증을 재현할 수 있다.
- [ ] Critical 문서 결함이 0건이다.

---

# 🧪 검증 및 증적

- Deliverable Index
- As-built Diagram
- Test Report
- Runbook Review
- Known Issue Register
- Evidence Path: `docs/evidence/P1-DOC-01/`

---

# 🔗 Dependency

- **Blocked By:** P1-HA-01, P1-DR-01, P1-E2E-01
- **Blocks / Next:** P1-REV-01
- **Related Ticket:** 전체 Phase 1
- **Milestone:** G3 Review Ready

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D12; D20
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-05; RISK-13
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** As-built Architecture, Test/Evidence Index, 구축·운영·복구 Runbook, Known Issue, Version/Source 및 Review 재현성 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>


</details>
