<!-- fds-canonical-description:v3.1.18 record-id:DEC-P1-FDS-01 -->
# DEC-P1-FDS-01 — 거래 보류 도입 범위·판정·평가 실패·Gate 편입 결정

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | DEC-P1-FDS-01 |
| Phase | Phase 1 |
| Category | Application / Governance |
| Type | Decision |
| Status | Done |
| Priority | P0 |
| Start | 2026-09-08 |
| End | 2026-09-09 |
| Calendar Days | 2 |
| Working Days | 2 |
| Lead | 이재환 |
| Support | 이하영, 이권욱 |
| Exit Criteria | 현행 탐지·기록 유지, 신규 보류·운영 기능 미도입, 실패 정책·계약 소유권, G2 영향 없음 및 후속 검증·재검토 조건 기록 |
| Related Decision IDs | D03; D12; D17; D28; D34; D36; D37 |
| Related Risk IDs | 현행 정의 연결 대기. v1.0 인용: RISK-05; RISK-07; RISK-09 — 본 종결의 위험 승인 근거로 사용하지 않음 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #4 snapshot 2026-09-10T01:21:55Z |
| Schedule Note | 현행 유지·신규 기능 확대 유예 결정 Done. 본 v3.1.18 후보에 통합하며 발행 전 운영 정본은 v3.1.17이다. 신규 기능 G2 편입·Runtime 승인은 아니다. |

## 현재 실행·검토 상태

2026-09-09 Decision Done. A 선택: 기존 탐지·기록·관측 유지. 별도 발표 프론트엔드, 거래 보류·해제·거절·운영 UI 확대는 미도입/유예. Runtime 및 G2 완료 승인이 아니다.

근거: [Issue #4](https://github.com/321Team/fds-project-baseline/issues/4), Issue 갱신 시각 `2026-09-10T01:21:55Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- 이 티켓은 종결 이력이다. 과거 구성 설명은 해당 종결 범위를 설명하며 현재 배포 명령으로 사용하지 않는다. 후속 설계 변경은 Baseline의 현행 절과 책임 티켓을 따른다.
- [후속 기록](https://github.com/321Team/fds-project-baseline/issues/4#issuecomment-5596603899)

---

# User Story

Application Lead로서 현행 FDS 탐지·기록 PoC의 범위를 유지하고 거래 보류·운영 조치 확대를 유예한다. 발표는 기존 관측 화면과 검증 증적으로 구성한다.

# Scope

## In Scope

- R01/R02/R04/R07의 기존 탐지·기록 범위 유지
- 실패 정책(#4)과 API·DB 표현 계약(#5)의 소유권 분리
- 현재 G2 범위·일정 유지와 기능 확대 재검토 조건

## Out of Scope

- 보류/해제/거절/자동 만료·재평가 기능, 새 심각도 또는 차단 정책
- 현재 fail-open·무인증 여부의 근거 없는 확정 또는 포괄적 잔여위험 수용
- 실제 금전 이체·원장·정산 및 Runtime 완료 선언

# 핵심 요구사항

## 종결 근거와 범위

2026-09-09 사용자가 “4 / 5번 리드 의견도 같은 기준으로 검토해주고, 4~6번 티켓 종결 처리해줘”라고 지시했다. 앞선 프론트엔드 배치 사양 제외 지시와 첨부 시연 초안의 현행 탐지·기록 방향을 함께 적용해 **현행 유지·기능 확대 유예**로 종결한다. v1.0에 규정된 미도입/유예 종결 경로를 사용한다.

이 기록은 불확실한 현재 구현을 승인하는 기록이 아니다. 리드의 작성 측 자체점검/PENDING을 독립 승인으로 바꾸지 않는다. 사람의 신규 독립 승인 서명을 생성하지 않으며, 사용자 최종 종결 지시와 Codex의 문서 검토 범위를 구분해 기록한다. 기존 Runtime AC, G2와 보안 기준은 유지한다.


**선택 결과:** A 선택 — 현행 탐지·기록·관측 유지. 별도 발표 프론트엔드 배치, L1 보류, L2 해제·거절, L3 운영 UI 확대는 미도입/유예.

## 리드 의견 검토·반영

[리드 원문](https://github.com/321Team/fds-project-baseline/issues/4#issuecomment-5596603899)을 보존하고 다음과 같이 처리한다.

- 권위 소스 경로·SHA 요구는 수용한다. 이번 연결에서 `321Team/fds-msa`는 404로 접근하지 못했다. 저장소나 구현이 존재하지 않는다고 단정하지 않는다. 기능을 확대하지 않는 결정과 기존 구현 확인을 구분한다.
- Risk 정의 출처 확인 요구를 수용한다. 구 v3.0 Risk CSV는 발견했지만 현행 대응을 보증하지 않으므로 v1.0의 ID 인용은 역사적 참조로만 보존한다.
- 실패 정책 중복 지적을 수용한다. #4는 업무 정책, #5는 그 정책의 API·DB 표현이다.
- B/C는 현재 채택하지 않으며 현 G2에 넣지 않는다. 추후 채택 시 견적·가용일·새 일정과 보안/회귀 영향을 다시 결정한다.
- Reviewer 이름을 자동 기입해 실제 독립 승인이 있었던 것처럼 만들지 않는다. 후속 보안 검토 담당은 이하영이며 본 종결의 최종 지시는 이권욱이다.

# Acceptance Criteria

v1.0의 AC ID를 보존한다. 표의 “후속 검증”은 미검증 상태를 뜻하며 체크박스 PASS로 대체하지 않는다. 이번 Done은 현행 유지·유예 선택의 종결이다.

| 기존 AC ID | 처리 | 결정/후속 |
|---|---|---|
| FDS-DAC-01 | 결정 완료 | A 현행 유지. 발표용 별도 UI 배치를 요구하지 않고 B/C 신규 기능은 유예. |
| FDS-DAC-02 | 결정 완료 | 탐지는 Rule 평가, 기록은 거래/FDS 결과 저장이다. 보류·승인·실제 자금 실행을 구현했다고 표현하지 않음. |
| FDS-DAC-03 | 현행 유지 / 후속 검증 | Rule ID는 유지. 새 임계값·심각도·조치 매핑을 도입하지 않음. 현재 Rule 소스·SHA·fixture는 P1-APP-01에서 확인. |
| FDS-DAC-04 | 확대 정책 유예 / 기존 검증 유지 | 새 Fail-Open/Closed/Hold 정책을 선택하지 않음. 기존 실패 경로는 P1-APP-01/P1-E2E-01에서 확인하고 결과를 #5의 계약 관점과 구분. |
| FDS-DAC-05 | 유예 | 보류 기능 미도입이므로 종료·만료·재평가 신규 설계를 하지 않음. 재도입 시 본 결정의 후속 변경 검토. |
| FDS-DAC-06 | 결정 완료 | 신규 기능의 G2 미편입. 기존 일정 유지. 구현 근거 확인은 이재환, 보안 검증은 이하영, 정본 인계는 이권욱. 각 기존 Gate 전 인계. |
| FDS-DAC-07 | 종결 지시 확보 | 리드 자체점검과 Codex 보조 검토를 연결하고 사용자 지시로 현행 유지/유예 종결. 신규 설계의 사람 독립 승인으로 확대하지 않음. |

# 검증 및 증적

- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) / D-SEC-01 v1.0 / D34 승인 기록.
- 리드 원문, `FDS_Decisions_4-6_Review_and_Closure_v1.1.md`, `FDS_Security_Demo_Scenarios_v1.5.md`.
- 사용자 종결 지시: 2026-09-09 현재 대화의 명시적 지시. 종결 실행·재조회 결과는 GitHub 기록 및 배포 Release Notes에 연결.
- Runtime 실행: 이번 검토에서 NOT RUN. 앱 저장소 현재 접근 결과 404는 미존재 증명이 아님.
- 신규 시험의 명령·입력·환경·정책 SHA·기대결과·복구·원본 증적은 각 구현 티켓에 연결.

# Dependency

- Related Ticket: P1-APP-01; P1-SEC-01; P1-E2E-01; P1-MON-01; P1-DOC-01
- #4는 업무 정책, #5는 API·DB 표현, #6은 업무 권한·관리 조치 감사 정책을 소유한다. 이번에는 모두 현행 유지·조건부 유예다.
- 기존 업무의 근거 확인과 Runtime 선행은 유지한다. #6의 기존 보안 시험 설계를 미채택 보류 정책에 종속시키지 않는다.
- 후속 Due: 각 기존 티켓의 Gate/종결 전. 시연 후보의 경우 리허설 GO 판정 전. G2 2026-09-11 및 기존 WBS를 자동 변경하지 않음.

# Decision / Risk Control

- **재검토 조건:** 실제 거래 보류·차단, 운영 조치, Rule 임계값/조치 또는 실패 정책의 변경 요청 발생 시.
- **Risk 참조:** v1.0 ID는 역사적 참조로 보존. 발견된 구 v3.0 Risk CSV의 의미·상태를 현행 정본에 자동 승격하지 않음. 실제 위험 수용이 필요할 때 권위 정의·영향·수용자·근거를 먼저 고정.
- **미확인 구현:** fail-open·인증·Migration/Schema drift·정책 차단 원인·CI 상태를 포괄 승인하지 않음.
- **변경 통제:** 실질 계약/통신/권한 변경 발생 시 CR/ICR 영향도 검토. 기존 D번호 의미를 바꾸거나 신규 번호를 임의 부여하지 않음.

# Review / Handoff

- Lead: 이재환; Support: 이하영, 이권욱.
- 기술 검토: Codex 보조 문서·소스 대조. 리드의 작성 측 자체점검과 별도 기록.
- 최종 종결 지시: 이권욱, 2026-09-09 현재 대화.
- 사람 독립 리뷰: 새 승인 서명 미생성. 기존 리드 PENDING/자체점검을 APPROVED로 변경하지 않음.
- 구현 확인과 보안 부정시험은 위 기존 티켓 담당자가 수행하고 실제 증적으로 판정.
- 정본 통합: P1-DOC-01에서 승인 기록·변경 이력·Ticket Pack·WBS/Gantt·Release Notes 영향 검토 후 후보로 반영.

# Completion Record

- **Result:** Decision Completed — 현행 유지 / 신규 기능 확대 유예.
- **Status:** Done.
- **Completed Date:** 2026-09-09.
- **Exit Criteria:** 현행 탐지·기록 유지, 신규 보류·운영 기능 미도입, 실패 정책·계약 소유권, G2 영향 없음 및 후속 검증·재검토 조건 기록.
- **Approved Option / Rationale:** A 선택 — 현행 탐지·기록·관측 유지. 별도 발표 프론트엔드 배치, L1 보류, L2 해제·거절, L3 운영 UI 확대는 미도입/유예.
- **Approver / Authority:** 이권욱의 명시적 4~6번 종결 지시.
- **Runtime Result:** NOT RUN / NOT VERIFIED, 기존 부분 증적의 판정 유지.
- **Baseline Integration:** v3.1.18 CANDIDATE에 반영. 발행 전 RELEASED v3.1.17 유지.
- **AI 사용:** CODEX_ASSISTED. 정책값·실서버 결과·사람의 독립 승인을 생성하지 않음.
