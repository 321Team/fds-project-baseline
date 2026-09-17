# DEC-P1-ADMIN-01 — 보안 시연 범위·테스트 전제·조건부 운영 통제 결정

> v3.1.19 CANDIDATE / NOT RELEASED · 2026-09-17 20:28 KST

## 현행 속성

| Property | 입력값 |
|---|---|
| Record ID | DEC-P1-ADMIN-01 |
| Phase | Phase 1 |
| Category | Application Security / Demonstration / Governance |
| Type | Decision |
| Status | Done |
| Priority | P0 |
| Start | 2026-09-08 |
| End | 2026-09-09 |
| Calendar Days | 2 |
| Working Days | 1 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | 프론트엔드 배치 제외, 합성 데이터·최소 노출 원칙, 5개 검토 축 적용/유예, 기존 접근 통제 재사용 및 후속 시나리오 인계 기록 |
| Related Decision IDs | D03; D12; D17; D18; D19; D28; D33; D34; D35; DEC-P1-FDS-01; DEC-P1-TXN-01; OID-01 |
| Related Risk IDs | 현행 정의 연결 대기. v1.0 인용: RISK-05; RISK-06; RISK-07; RISK-08; RISK-09 — 본 종결의 위험 승인 근거로 사용하지 않음 |
| Source | Baseline v3.1.19 CANDIDATE; GitHub #6 @ 2026-09-14T15:13:42Z; 원문 SHA256 2e84b06c6de790bbdc142a1556a938fdfd485babe8314202f83b2d0836b36464 |
| Schedule Note | 현행 유지·신규 기능 확대 유예 결정 Done. v18 편입 이력을 유지한다. 현재 발행 정본은 v3.1.18이며 본 자료는 v19 후보이다. 신규 기능 G2 편입·Runtime 승인은 아니다. |

## 상태와 인수 경계

현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다.

- GitHub lifecycle: closed; Milestone: G2 Security / Feature Ready
- 일정은 조정 가능한 계획이며 실제 완료일·Gate 승인일과 구분한다.
- 원문·후속 댓글: [원본 티켓](https://github.com/321Team/fds-project-baseline/issues/6), [고정 수집본](../sources/issue-6.json).
- 상위 속성표는 이 후보의 현행 표다. 아래 원문은 수집 시점의 변경/승인/AC 이력이며 과거 버전 문구를 현재 발행 상태로 사용하지 않는다.

## 원문 보존

<details>
<summary>수집한 GitHub 본문 전체 — SHA256 2e84b06c6de790bbdc142a1556a938fdfd485babe8314202f83b2d0836b36464</summary>

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 종결 유지. 신규 관리 UI/역할·15/60분 세션 초안은 미채택. 기존 보안시험은 #19/#20에서 유지.

- 보안 시연의 기존 범위를 #19/#20에 연결한다. 과거 댓글의 Viewer/Operator/Approver·Idle15분/Absolute60분은 채택된 운영 사양이 아니므로 신규 구현 입력으로 사용하지 않는다.

**인계·관련 티켓:** [#19](https://github.com/321Team/fds-project-baseline/issues/19) · [#20](https://github.com/321Team/fds-project-baseline/issues/20).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-milestone-assignment:2026-09-11 issue:6 -->
## 대표 Milestone 배정 — 2026-09-11

- **추적 Milestone:** G2 Security / Feature Ready (GitHub #3)
- **배정 성격:** 완료 이력 · 이권욱 사용자 지시에 따른 대표 추적 항목 지정.
- **배정 근거:** 2026-09-09 보안 시연·조건부 운영 통제 범위 결정 종결. G2 보안 범위 결정 이력으로 추적하며 미도입 기능이나 Runtime 승인을 추가하지 않는다.
- **출처:** [발행 정본에 보존된 종결·승인 이력](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)
- **일정 원칙:** 일정은 고정된 필수 기한이 아닌 조정 가능한 계획 목표다. 선행조건과 영향 확인 후 유연하게 조정하며, 실제 완료일·승인·Runtime 증적 요건과 구분한다.
- **적용 범위:** 대표 Milestone 연결과 이 근거 기록. 기존 상태·완료 사실·AC·담당·티켓 Start/End 및 Gate 요건을 유지한다.

---

<!-- fds-canonical-description:v3.1.18 record-id:DEC-P1-ADMIN-01 -->
# DEC-P1-ADMIN-01 — 보안 시연 범위·테스트 전제·조건부 운영 통제 결정

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | DEC-P1-ADMIN-01 |
| Phase | Phase 1 |
| Category | Application Security / Demonstration / Governance |
| Type | Decision |
| Status | Done |
| Priority | P0 |
| Start | 2026-09-08 |
| End | 2026-09-09 |
| Calendar Days | 2 |
| Working Days | 1 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | 프론트엔드 배치 제외, 합성 데이터·최소 노출 원칙, 5개 검토 축 적용/유예, 기존 접근 통제 재사용 및 후속 시나리오 인계 기록 |
| Related Decision IDs | D03; D12; D17; D18; D19; D28; D33; D34; D35; DEC-P1-FDS-01; DEC-P1-TXN-01; OID-01 |
| Related Risk IDs | 현행 정의 연결 대기. v1.0 인용: RISK-05; RISK-06; RISK-07; RISK-08; RISK-09 — 본 종결의 위험 승인 근거로 사용하지 않음 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #6 snapshot 2026-09-10T01:22:24Z |
| Schedule Note | 현행 유지·신규 기능 확대 유예 결정 Done. 본 v3.1.18 후보에 통합하며 발행 전 운영 정본은 v3.1.17이다. 신규 기능 G2 편입·Runtime 승인은 아니다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **Done / closed**. 원본 갱신 시각: `2026-09-10T01:22:24Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.
- 수집된 운영 댓글은 원래 위치에 보존한다. 신규 구현 제출/리뷰 요청은 실행 PASS나 승인으로 간주하지 않는다.
  - [5596682397](https://github.com/321Team/fds-project-baseline/issues/6#issuecomment-5596682397) · 2026-09-09T06:06:42Z

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

2026-09-09 Decision Done. 기존 Grafana 관측·합성 데이터 시연으로 범위를 한정했다. 새 업무 역할·2인 승인·세션 수명·관리 감사 정책값은 유예. OID-01 Source/Identity와 기존 보안 부정시험은 유지한다.

근거: [Issue #6](https://github.com/321Team/fds-project-baseline/issues/6), Issue 갱신 시각 `2026-09-10T01:22:24Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- 이 티켓은 종결 이력이다. 과거 구성 설명은 해당 종결 범위를 설명하며 현재 배포 명령으로 사용하지 않는다. 후속 설계 변경은 Baseline의 현행 절과 책임 티켓을 따른다.
- [후속 기록](https://github.com/321Team/fds-project-baseline/issues/6#issuecomment-5596682397)

---

# User Story

보안 설계 담당자로서 기존 승인 통제로 가능한 시연과 테스트 전제를 정한다. 배치 사양과 미채택 업무 기능의 정책을 현재 구현 의무로 만들지 않고 시험과 증적의 경계를 명확히 한다.

# Scope

## In Scope

- 합성 데이터만 사용하는 시연과 화면/로그의 최소 정보 노출
- 기존 Grafana/Prometheus/Alertmanager 관측 및 보안 부정시험 전제
- 새 업무 정책은 기능 채택 시 결정하는 조건부 인계

## Out of Scope

- 프론트엔드 배치 사양, 신규 BFF/Namespace/Workload/Runner 권한 확대
- Hold/Release·운영 UI, 신규 업무 3역할/2인 승인/고정 세션 수명 구현
- Grafana→App/DB 연결, 외부 Grafana 공개, 새 Plugin·외부 알림 통합

# 핵심 요구사항

## 종결 근거와 범위

2026-09-09 사용자가 “4 / 5번 리드 의견도 같은 기준으로 검토해주고, 4~6번 티켓 종결 처리해줘”라고 지시했다. 앞선 프론트엔드 배치 사양 제외 지시와 첨부 시연 초안의 현행 탐지·기록 방향을 함께 적용해 **현행 유지·기능 확대 유예**로 종결한다. v1.0에 규정된 미도입/유예 종결 경로를 사용한다.

이 기록은 불확실한 현재 구현을 승인하는 기록이 아니다. 리드의 작성 측 자체점검/PENDING을 독립 승인으로 바꾸지 않는다. 사람의 신규 독립 승인 서명을 생성하지 않으며, 사용자 최종 종결 지시와 Codex의 문서 검토 범위를 구분해 기록한다. 기존 Runtime AC, G2와 보안 기준은 유지한다.


**선택 결과:** A 범위 축소 적용 — 기존 Grafana 관측·증적 시연. 프론트엔드 배치 사양 제거. 리드의 5개 항목은 테스트 검토 축으로 수용하고 신규 업무 권한·관리 기능·세션·관리 감사 정책값은 조건부 유예.

## 리드 의견 검토·반영

[리드 원문](https://github.com/321Team/fds-project-baseline/issues/6#issuecomment-5596682397)을 보존하고 다음과 같이 처리한다.

- 합성 데이터·역할·경로·세션·감사 실패의 5개 축을 수용한다. 구체 값은 확정안이 아니라 Placeholder라는 리드의 전제를 유지한다.
- 기존 통제의 시험 설계는 먼저 진행한다. 다섯 신규 값이 모두 정해져야 모든 보안 시험을 시작할 수 있다는 선행조건은 적용하지 않는다.
- `TST_`/`SIM_`는 명명 예시다. 접두어만으로 실데이터 혼입을 방지했다고 판단하지 않는다. 필드별 마스킹은 숨길 자리/보일 자리를 명확히 하고 테스트 데이터 시트에서 고정한다.
- 업무 사용자 3역할은 Kubernetes RBAC와 별도다. 관리 기능을 채택할 때 검토하며 현재 Grafana 인증을 대체하거나 무인증을 허용하지 않는다.
- 관리 조치 감사 실패와 FDS 엔진 실패·모니터링 전송 실패를 구분한다. 모든 거래 실패에 Fail-Closed를 일괄 적용하지 않는다.
- 새 frontend 사양 삭제와 기존 OID-01 관리 접근 확인은 별개다. 후자는 계속 필요한 Runtime 선행조건이다.

# Acceptance Criteria

v1.0의 AC ID를 보존한다. 표의 “후속 검증”은 미검증 상태를 뜻하며 체크박스 PASS로 대체하지 않는다. 이번 Done은 현행 유지·유예 선택의 종결이다.

| 기존 AC ID | 처리 | 결정/후속 |
|---|---|---|
| ADMIN-DAC-01 | 결정 완료 | 기존 Grafana 관측·증적 시연. 신규 거래별 조회/운영 화면·배치 미도입. 데이터는 합성 데이터만 사용하고 재현에 필요한 필드만 노출. |
| ADMIN-DAC-02 | 기존 경계 재사용 / 조건부 유예 | D18/D19/D33/D34 유지. Grafana ClusterIP·승인 port-forward, OID-01 정확한 Source/Identity 확인은 기존 Runtime 선행. 신규 관리 listener/Pod 선택은 현재 유예. |
| ADMIN-DAC-03 | 미적용 사유 기록 | 신규 UI/잡이 없어 새 SA/RBAC/Runner delta 없음. 기존 SA 최소권한·token automount 정책은 유지. |
| ADMIN-DAC-04 | 조건부 유예 | 새 관리 기능이 없어 업무 역할·지점별 인가·2인 승인·15/60분 세션·관리 감사 Fail-Closed 값은 미채택. 기능 도입 시 재검토. |
| ADMIN-DAC-05 | 재사용 확인 | Grafana→Prometheus만, API/App/DB 직접 접근 금지. 3개 View·Plugin 제한·관리 접근 정책 유지. OID-01을 신규 결정으로 복제하지 않음. |
| ADMIN-DAC-06 | 인계 결정 | P1-SEC/MON/APP/DB/CICD/K8S/E2E/HA/DOC의 기존 AC로 시나리오 연결. 새 인터페이스가 없어 추가 보안 설계/ICR 없음. |
| ADMIN-DAC-07 | 종결 지시 확보 | 적용/유예 사유와 재검토 조건을 기록하고 사용자 지시로 종결. 조건부 기능의 미실행 시험을 PASS로 바꾸지 않음. |

# 검증 및 증적

- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) / D-SEC-01 v1.0 / D34 승인 기록.
- 리드 원문, `FDS_Decisions_4-6_Review_and_Closure_v1.1.md`, `FDS_Security_Demo_Scenarios_v1.5.md`.
- 사용자 종결 지시: 2026-09-09 현재 대화의 명시적 지시. 종결 실행·재조회 결과는 GitHub 기록 및 배포 Release Notes에 연결.
- Runtime 실행: 이번 검토에서 NOT RUN. 앱 저장소 현재 접근 결과 404는 미존재 증명이 아님.
- 신규 시험의 명령·입력·환경·정책 SHA·기대결과·복구·원본 증적은 각 구현 티켓에 연결.

# Dependency

- Related Ticket: P1-SEC-01; P1-MON-01; P1-APP-01; P1-DB-01; P1-CICD-01; P1-K8S-01; P1-E2E-01; P1-HA-01; P1-DOC-01
- #4는 업무 정책, #5는 API·DB 표현, #6은 업무 권한·관리 조치 감사 정책을 소유한다. 이번에는 모두 현행 유지·조건부 유예다.
- 기존 업무의 근거 확인과 Runtime 선행은 유지한다. #6의 기존 보안 시험 설계를 미채택 보류 정책에 종속시키지 않는다.
- 후속 Due: 각 기존 티켓의 Gate/종결 전. 시연 후보의 경우 리허설 GO 판정 전. G2 2026-09-11 및 기존 WBS를 자동 변경하지 않음.

# Decision / Risk Control

- **재검토 조건:** 신규 거래별 조회/운영 API·화면·사용자 인증·권한·감사 또는 발표 데이터 공개 범위 확대 시.
- **Risk 참조:** v1.0 ID는 역사적 참조로 보존. 발견된 구 v3.0 Risk CSV의 의미·상태를 현행 정본에 자동 승격하지 않음. 실제 위험 수용이 필요할 때 권위 정의·영향·수용자·근거를 먼저 고정.
- **미확인 구현:** fail-open·인증·Migration/Schema drift·정책 차단 원인·CI 상태를 포괄 승인하지 않음.
- **변경 통제:** 실질 계약/통신/권한 변경 발생 시 CR/ICR 영향도 검토. 기존 D번호 의미를 바꾸거나 신규 번호를 임의 부여하지 않음.

# Review / Handoff

- Lead: 이하영; Support: 이권욱, 이재환.
- 기술 검토: Codex 보조 문서·소스 대조. 리드의 작성 측 자체점검과 별도 기록.
- 최종 종결 지시: 이권욱, 2026-09-09 현재 대화.
- 사람 독립 리뷰: 새 승인 서명 미생성. 기존 리드 PENDING/자체점검을 APPROVED로 변경하지 않음.
- 구현 확인과 보안 부정시험은 위 기존 티켓 담당자가 수행하고 실제 증적으로 판정.
- 정본 통합: P1-DOC-01에서 승인 기록·변경 이력·Ticket Pack·WBS/Gantt·Release Notes 영향 검토 후 후보로 반영.

# Completion Record

- **Result:** Decision Completed — 현행 유지 / 신규 기능 확대 유예.
- **Status:** Done.
- **Completed Date:** 2026-09-09.
- **Exit Criteria:** 프론트엔드 배치 제외, 합성 데이터·최소 노출 원칙, 5개 검토 축 적용/유예, 기존 접근 통제 재사용 및 후속 시나리오 인계 기록.
- **Approved Option / Rationale:** A 범위 축소 적용 — 기존 Grafana 관측·증적 시연. 프론트엔드 배치 사양 제거. 리드의 5개 항목은 테스트 검토 축으로 수용하고 신규 업무 권한·관리 기능·세션·관리 감사 정책값은 조건부 유예.
- **Approver / Authority:** 이권욱의 명시적 4~6번 종결 지시.
- **Runtime Result:** NOT RUN / NOT VERIFIED, 기존 부분 증적의 판정 유지.
- **Baseline Integration:** v3.1.18 CANDIDATE에 반영. 발행 전 RELEASED v3.1.17 유지.
- **AI 사용:** CODEX_ASSISTED. 정책값·실서버 결과·사람의 독립 승인을 생성하지 않음.

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `58f4442e3ca1cbb99a6fdfaf6fbe6ff2c6d571d36cc94a4db736e50dbc9bceb6`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
# DEC-P1-ADMIN-01 — 보안 시연 범위·테스트 전제·조건부 운영 통제 결정

> **버전:** v1.1 — 종결 결정 기록  
> **결정일:** 2026-09-09  
> **Lifecycle:** Done / GitHub Closed  
> **결과:** A 범위 축소 적용 — 기존 Grafana 관측·증적 시연. 프론트엔드 배치 사양 제거. 리드의 5개 항목은 테스트 검토 축으로 수용하고 신규 업무 권한·관리 기능·세션·관리 감사 정책값은 조건부 유예.  
> **정본 반영:** 미반영 — 합의 결과의 정본 통합은 후속. 현행 RELEASED v3.1.17 유지.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | DEC-P1-ADMIN-01 |
| Phase | Phase 1 |
| Category | Application Security / Demonstration / Governance |
| Type | Decision |
| Status | Done |
| Priority | P0 |
| Start | 2026-09-08 |
| End | 2026-09-09 |
| Calendar Days | 2 |
| Working Days | 2 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | 프론트엔드 배치 제외, 합성 데이터·최소 노출 원칙, 5개 검토 축 적용/유예, 기존 접근 통제 재사용 및 후속 시나리오 인계 기록 |
| Related Decision IDs | D03; D12; D17; D18; D19; D28; D33; D34; D35; DEC-P1-FDS-01; DEC-P1-TXN-01; OID-01 |
| Related Risk IDs | 현행 정의 연결 대기. v1.0 인용: RISK-05; RISK-06; RISK-07; RISK-08; RISK-09 — 본 종결의 위험 승인 근거로 사용하지 않음 |
| Source | Baseline v3.1.17; D-SEC-01 v1.0/D34; Issue #4~6 리드 의견; 2026-09-09 사용자 종결 지시; 통합 검토 v1.1 |
| Schedule Note | 현행 유지·신규 기능 유예 결정 종결. Priority는 결정 우선순위이며 신규 기능 G2 편입 아님. Runtime/정본 반영은 별도. Notion은 같은 Record ID로 수동 Upsert. |

# 🎯 User Story

보안 설계 담당자로서 기존 승인 통제로 가능한 시연과 테스트 전제를 정한다. 배치 사양과 미채택 업무 기능의 정책을 현재 구현 의무로 만들지 않고 시험과 증적의 경계를 명확히 한다.

# 📌 Scope

## In Scope

- 합성 데이터만 사용하는 시연과 화면/로그의 최소 정보 노출
- 기존 Grafana/Prometheus/Alertmanager 관측 및 보안 부정시험 전제
- 새 업무 정책은 기능 채택 시 결정하는 조건부 인계

## Out of Scope

- 프론트엔드 배치 사양, 신규 BFF/Namespace/Workload/Runner 권한 확대
- Hold/Release·운영 UI, 신규 업무 3역할/2인 승인/고정 세션 수명 구현
- Grafana→App/DB 연결, 외부 Grafana 공개, 새 Plugin·외부 알림 통합

# 📋 핵심 요구사항

## 종결 근거와 범위

2026-09-09 사용자가 “4 / 5번 리드 의견도 같은 기준으로 검토해주고, 4~6번 티켓 종결 처리해줘”라고 지시했다. 앞선 프론트엔드 배치 사양 제외 지시와 첨부 시연 초안의 현행 탐지·기록 방향을 함께 적용해 **현행 유지·기능 확대 유예**로 종결한다. v1.0에 규정된 미도입/유예 종결 경로를 사용한다.

이 기록은 불확실한 현재 구현을 승인하는 기록이 아니다. 리드의 작성 측 자체점검/PENDING을 독립 승인으로 바꾸지 않는다. 사람의 신규 독립 승인 서명을 생성하지 않으며, 사용자 최종 종결 지시와 Codex의 문서 검토 범위를 구분해 기록한다. 기존 Runtime AC, G2와 보안 기준은 유지한다.


**선택 결과:** A 범위 축소 적용 — 기존 Grafana 관측·증적 시연. 프론트엔드 배치 사양 제거. 리드의 5개 항목은 테스트 검토 축으로 수용하고 신규 업무 권한·관리 기능·세션·관리 감사 정책값은 조건부 유예.

## 리드 의견 검토·반영

[리드 원문](https://github.com/321Team/fds-project-baseline/issues/6#issuecomment-5596682397)을 보존하고 다음과 같이 처리한다.

- 합성 데이터·역할·경로·세션·감사 실패의 5개 축을 수용한다. 구체 값은 확정안이 아니라 Placeholder라는 리드의 전제를 유지한다.
- 기존 통제의 시험 설계는 먼저 진행한다. 다섯 신규 값이 모두 정해져야 모든 보안 시험을 시작할 수 있다는 선행조건은 적용하지 않는다.
- `TST_`/`SIM_`는 명명 예시다. 접두어만으로 실데이터 혼입을 방지했다고 판단하지 않는다. 필드별 마스킹은 숨길 자리/보일 자리를 명확히 하고 테스트 데이터 시트에서 고정한다.
- 업무 사용자 3역할은 Kubernetes RBAC와 별도다. 관리 기능을 채택할 때 검토하며 현재 Grafana 인증을 대체하거나 무인증을 허용하지 않는다.
- 관리 조치 감사 실패와 FDS 엔진 실패·모니터링 전송 실패를 구분한다. 모든 거래 실패에 Fail-Closed를 일괄 적용하지 않는다.
- 새 frontend 사양 삭제와 기존 OID-01 관리 접근 확인은 별개다. 후자는 계속 필요한 Runtime 선행조건이다.

# ✅ Acceptance Criteria

v1.0의 AC ID를 보존한다. 표의 “후속 검증”은 미검증 상태를 뜻하며 체크박스 PASS로 대체하지 않는다. 이번 Done은 현행 유지·유예 선택의 종결이다.

| 기존 AC ID | 처리 | 결정/후속 |
|---|---|---|
| ADMIN-DAC-01 | 결정 완료 | 기존 Grafana 관측·증적 시연. 신규 거래별 조회/운영 화면·배치 미도입. 데이터는 합성 데이터만 사용하고 재현에 필요한 필드만 노출. |
| ADMIN-DAC-02 | 기존 경계 재사용 / 조건부 유예 | D18/D19/D33/D34 유지. Grafana ClusterIP·승인 port-forward, OID-01 정확한 Source/Identity 확인은 기존 Runtime 선행. 신규 관리 listener/Pod 선택은 현재 유예. |
| ADMIN-DAC-03 | 미적용 사유 기록 | 신규 UI/잡이 없어 새 SA/RBAC/Runner delta 없음. 기존 SA 최소권한·token automount 정책은 유지. |
| ADMIN-DAC-04 | 조건부 유예 | 새 관리 기능이 없어 업무 역할·지점별 인가·2인 승인·15/60분 세션·관리 감사 Fail-Closed 값은 미채택. 기능 도입 시 재검토. |
| ADMIN-DAC-05 | 재사용 확인 | Grafana→Prometheus만, API/App/DB 직접 접근 금지. 3개 View·Plugin 제한·관리 접근 정책 유지. OID-01을 신규 결정으로 복제하지 않음. |
| ADMIN-DAC-06 | 인계 결정 | P1-SEC/MON/APP/DB/CICD/K8S/E2E/HA/DOC의 기존 AC로 시나리오 연결. 새 인터페이스가 없어 추가 보안 설계/ICR 없음. |
| ADMIN-DAC-07 | 종결 지시 확보 | 적용/유예 사유와 재검토 조건을 기록하고 사용자 지시로 종결. 조건부 기능의 미실행 시험을 PASS로 바꾸지 않음. |

# 🧪 검증 및 증적

- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) / D-SEC-01 v1.0 / D34 승인 기록.
- 리드 원문, `FDS_Decisions_4-6_Review_and_Closure_v1.1.md`, `FDS_Security_Demo_Scenarios_v1.5.md`.
- 사용자 종결 지시: 2026-09-09 현재 대화의 명시적 지시. 종결 실행·재조회 결과는 GitHub 기록 및 배포 Release Notes에 연결.
- Runtime 실행: 이번 검토에서 NOT RUN. 앱 저장소 현재 접근 결과 404는 미존재 증명이 아님.
- 신규 시험의 명령·입력·환경·정책 SHA·기대결과·복구·원본 증적은 각 구현 티켓에 연결.

# 🔗 Dependency

- Related Ticket: P1-SEC-01; P1-MON-01; P1-APP-01; P1-DB-01; P1-CICD-01; P1-K8S-01; P1-E2E-01; P1-HA-01; P1-DOC-01
- #4는 업무 정책, #5는 API·DB 표현, #6은 업무 권한·관리 조치 감사 정책을 소유한다. 이번에는 모두 현행 유지·조건부 유예다.
- 기존 업무의 근거 확인과 Runtime 선행은 유지한다. #6의 기존 보안 시험 설계를 미채택 보류 정책에 종속시키지 않는다.
- 후속 Due: 각 기존 티켓의 Gate/종결 전. 시연 후보의 경우 리허설 GO 판정 전. G2 2026-09-11 및 기존 WBS를 자동 변경하지 않음.

# ⚖️ Decision / Risk Control

- **재검토 조건:** 신규 거래별 조회/운영 API·화면·사용자 인증·권한·감사 또는 발표 데이터 공개 범위 확대 시.
- **Risk 참조:** v1.0 ID는 역사적 참조로 보존. 발견된 구 v3.0 Risk CSV의 의미·상태를 현행 정본에 자동 승격하지 않음. 실제 위험 수용이 필요할 때 권위 정의·영향·수용자·근거를 먼저 고정.
- **미확인 구현:** fail-open·인증·Migration/Schema drift·정책 차단 원인·CI 상태를 포괄 승인하지 않음.
- **변경 통제:** 실질 계약/통신/권한 변경 발생 시 CR/ICR 영향도 검토. 기존 D번호 의미를 바꾸거나 신규 번호를 임의 부여하지 않음.

# 🔍 Review / Handoff

- Lead: 이하영; Support: 이권욱, 이재환.
- 기술 검토: Codex 보조 문서·소스 대조. 리드의 작성 측 자체점검과 별도 기록.
- 최종 종결 지시: 이권욱, 2026-09-09 현재 대화.
- 사람 독립 리뷰: 새 승인 서명 미생성. 기존 리드 PENDING/자체점검을 APPROVED로 변경하지 않음.
- 구현 확인과 보안 부정시험은 위 기존 티켓 담당자가 수행하고 실제 증적으로 판정.
- 정본 통합: P1-DOC-01에서 승인 기록·변경 이력·Ticket Pack·WBS/Gantt·Release Notes 영향 검토 후 후보로 반영.

# 📝 Completion Record

- **Result:** Decision Completed — 현행 유지 / 신규 기능 확대 유예.
- **Status:** Done.
- **Completed Date:** 2026-09-09.
- **Exit Criteria:** 프론트엔드 배치 제외, 합성 데이터·최소 노출 원칙, 5개 검토 축 적용/유예, 기존 접근 통제 재사용 및 후속 시나리오 인계 기록.
- **Approved Option / Rationale:** A 범위 축소 적용 — 기존 Grafana 관측·증적 시연. 프론트엔드 배치 사양 제거. 리드의 5개 항목은 테스트 검토 축으로 수용하고 신규 업무 권한·관리 기능·세션·관리 감사 정책값은 조건부 유예.
- **Approver / Authority:** 이권욱의 명시적 4~6번 종결 지시.
- **Runtime Result:** NOT RUN / NOT VERIFIED, 기존 부분 증적의 판정 유지.
- **Baseline Integration:** 미반영. 현재 RELEASED v3.1.17 유지.
- **AI 사용:** CODEX_ASSISTED. 정책값·실서버 결과·사람의 독립 승인을 생성하지 않음.
````

</details>


</details>
