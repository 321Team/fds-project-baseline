<!-- fds-canonical-live:v3.1.21 record-id:DEC-P1-TXN-01:start -->
## 현행 정본 적용 — v3.1.21

- 정본: [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21), 2026-10-04 14:49:12 KST 발행. 기준 커밋: `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`.
- [이 티켓의 발행 Description](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tickets/v3.1.21/descriptions/DEC-P1-TXN-01.md) · [Baseline](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/baseline/FDS_Project_Implementation_Baseline_v3.1.21.md) · [WBS](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/wbs/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx).
- [테스트 전략](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tests/FDS_Test_Strategy_v3.1.21.md): 해당 업무의 기존 AC·Exit Criteria와 실행/인수 구분을 유지한다.
- 정본 Description은 2026-10-03 수집 시점 기록이다. 발행 후 실제 수행·검토·잔여·승인 변경은 아래 최신 운영 기록과 원본 증적을 따른다. 아래 과거 버전의 '현행/후보/미발행' 문구는 작성 당시 이력이다.
- 발행·동기화로 Status, AC 체크, 실제 완료일, 담당자, 일정, Runtime 승인 또는 종결을 상향하지 않는다. 신규 계획·사양 충돌은 별도 변경결정으로 정합화한다.
- 반영 근거: 사용자 '디스크립션 파일 반영과 이슈 본문 수정' 지시. AI 사용: CODEX_ASSISTED.
<!-- fds-canonical-live:v3.1.21 record-id:DEC-P1-TXN-01:end -->

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 종결 유지. 기존 API/DB 계약 유지. 새 상태·멱등성 TTL 추가 대상 아님. A04/R02/R06의 현재 소스 연결.

- 기존 계약 유지 선택에 따라 현재 OpenAPI/코드/Migration·실패 응답의 정합성을 #15/#11/#20에서 확인한다. 보류용 status/release/reject·새 멱등성 저장소/TTL을 추가하지 않는다.

**인계·관련 티켓:** [#11](https://github.com/321Team/fds-project-baseline/issues/11) · [#15](https://github.com/321Team/fds-project-baseline/issues/15) · [#20](https://github.com/321Team/fds-project-baseline/issues/20).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-milestone-assignment:2026-09-11 issue:5 -->
## 대표 Milestone 배정 — 2026-09-11

- **추적 Milestone:** G2 Security / Feature Ready (GitHub #3)
- **배정 성격:** 완료 이력 · 이권욱 사용자 지시에 따른 대표 추적 항목 지정.
- **배정 근거:** 2026-09-09 기존 API·DB 계약 유지 결정 종결. G2 계약·범위 결정 이력으로 추적하며 신규 상태/API 구현 PASS를 뜻하지 않는다.
- **출처:** [발행 정본에 보존된 종결·승인 이력](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)
- **일정 원칙:** 일정은 고정된 필수 기한이 아닌 조정 가능한 계획 목표다. 선행조건과 영향 확인 후 유연하게 조정하며, 실제 완료일·승인·Runtime 증적 요건과 구분한다.
- **적용 범위:** 대표 Milestone 연결과 이 근거 기록. 기존 상태·완료 사실·AC·담당·티켓 Start/End 및 Gate 요건을 유지한다.

---

<!-- fds-canonical-description:v3.1.18 record-id:DEC-P1-TXN-01 -->
# DEC-P1-TXN-01 — 거래 상태·API 응답·재시도·데이터 정합성 계약 결정

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | DEC-P1-TXN-01 |
| Phase | Phase 1 |
| Category | Application / Data / Interface |
| Type | Decision |
| Status | Done |
| Priority | P0 |
| Start | 2026-09-08 |
| End | 2026-09-09 |
| Calendar Days | 2 |
| Working Days | 2 |
| Lead | 이재환 |
| Support | 이하영, 이권욱 |
| Exit Criteria | 기존 계약 유지 선택, 신규 상태/API·Migration 변경 유예, #4/#6과 정책·표현 소유권 및 기존 구현 정합성 후속 기록 |
| Related Decision IDs | D03; D04; D18; D28; D34; D35; DEC-P1-FDS-01 |
| Related Risk IDs | 현행 정의 연결 대기. v1.0 인용: RISK-05; RISK-07; RISK-09 — 본 종결의 위험 승인 근거로 사용하지 않음 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #5 snapshot 2026-09-10T01:22:10Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 현행 유지·신규 기능 확대 유예 결정 Done. 본 v3.1.18 후보에 통합하며 발행 전 운영 정본은 v3.1.17이다. 신규 기능 G2 편입·Runtime 승인은 아니다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **Done / closed**. 원본 갱신 시각: `2026-09-10T01:22:10Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.
- 수집된 운영 댓글은 원래 위치에 보존한다. 신규 구현 제출/리뷰 요청은 실행 PASS나 승인으로 간주하지 않는다.
  - [5596626893](https://github.com/321Team/fds-project-baseline/issues/5#issuecomment-5596626893) · 2026-09-09T06:03:20Z

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

2026-09-09 Decision Done. C 선택: 기존 API·DB 계약 유지. 보류용 상태·API·Migration을 추가하지 않는다. 기존 Schema drift, 소스·배포 SHA 및 실패 응답 검증은 P1-APP/DB/E2E에서 계속 수행한다.

근거: [Issue #5](https://github.com/321Team/fds-project-baseline/issues/5), Issue 갱신 시각 `2026-09-10T01:22:10Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- 이 티켓은 종결 이력이다. 과거 구성 설명은 해당 종결 범위를 설명하며 현재 배포 명령으로 사용하지 않는다. 후속 설계 변경은 Baseline의 현행 절과 책임 티켓을 따른다.
- [후속 기록](https://github.com/321Team/fds-project-baseline/issues/5#issuecomment-5596626893)

---

# User Story

Application·Data 담당자로서 선택된 현행 유지 범위에 맞춰 새 상태/API 변경을 유예하고 현재 계약과 Migration 정합성 확인을 기존 구현 티켓에 연결한다.

# Scope

## In Scope

- #4의 현행 유지 선택에 따른 API·DB 계약 변경 없음 결정
- 201 자원 생성과 업무 실행 승인 구분
- Migration drift 및 실패 응답 근거 등 기존 계약 확인의 후속 인계

## Out of Scope

- 보류 상태·해제/거절 API·새 멱등성 저장소/TTL/잡의 추가
- 신규 관리 상태를 위한 backfill·Migration 또는 기존 201 일괄 403 변경
- 기존 Schema drift·미검증 실패 경로를 해소된 것으로 처리

# 핵심 요구사항

## 종결 근거와 범위

2026-09-09 사용자가 “4 / 5번 리드 의견도 같은 기준으로 검토해주고, 4~6번 티켓 종결 처리해줘”라고 지시했다. 앞선 프론트엔드 배치 사양 제외 지시와 첨부 시연 초안의 현행 탐지·기록 방향을 함께 적용해 **현행 유지·기능 확대 유예**로 종결한다. v1.0에 규정된 미도입/유예 종결 경로를 사용한다.

이 기록은 불확실한 현재 구현을 승인하는 기록이 아니다. 리드의 작성 측 자체점검/PENDING을 독립 승인으로 바꾸지 않는다. 사람의 신규 독립 승인 서명을 생성하지 않으며, 사용자 최종 종결 지시와 Codex의 문서 검토 범위를 구분해 기록한다. 기존 Runtime AC, G2와 보안 기준은 유지한다.


**선택 결과:** C 선택 — 보류 미도입에 따른 기존 계약 유지. 신규 status 컬럼, release/reject endpoint, 응답 코드 전면 변경, 관리 조치 감사·멱등성 체계를 추가하지 않음.

## 리드 의견 검토·반영

[리드 원문](https://github.com/321Team/fds-project-baseline/issues/5#issuecomment-5596626893)을 보존하고 다음과 같이 처리한다.

- 권위 OpenAPI/Migration 경로와 SHA 필요성은 수용한다. “연결에서 미확보”로 기록하며 앱 소스가 존재하지 않는다고 단정하지 않는다.
- v1.0 In Scope의 “확보”는 수행 목표이므로 그 문구만으로 이미 확보했다고 주장한 상충은 아니다. 현재 확보 상태는 별도 명시한다.
- #4 실패 정책과 #5 응답·저장 계약 소유권을 분리한다. 관리 조치 감사 정책은 #6, 원자성/응답 구현 계약은 #5다.
- 멱등성 TTL/저장소, IF-03 Payload ICR, 동기 타임아웃, 복구 호환성은 해당 변경을 채택할 때 함께 결정할 항목으로 수용한다. 현행 유지 선택에 새 기능 의무를 만들지 않는다.
- 기존 Migration drift 보완은 보류 기능과 무관한 기존 구현 작업이다. 코드 작성·병합·운영 적용·API 재현·복구를 따로 확인한다.
- 고정 태그/커밋 사용 제안은 수용한다. `2d93395a…`는 유효한 정본 최종화 커밋이며 잘못된 참조로 취급하지 않는다.

# Acceptance Criteria

v1.0의 AC ID를 보존한다. 표의 “후속 검증”은 미검증 상태를 뜻하며 체크박스 PASS로 대체하지 않는다. 이번 Done은 현행 유지·유예 선택의 종결이다.

| 기존 AC ID | 처리 | 결정/후속 |
|---|---|---|
| TXN-DAC-01 | 변경 없음 / 후속 검증 | 새 계약을 승인하지 않음. 현행 OpenAPI·Migration·Rule 경로/SHA 확보는 P1-APP-01/P1-DB-01의 기존 Runtime 근거로 유지. |
| TXN-DAC-02 | 확대 계약 유예 | 신규 업무 상태·HTTP 표를 만들지 않음. 기존 정상/탐지/평가 실패/DB 실패 응답은 권위 소스 및 fixture로 확인. 단일 201 증적을 전체 계약으로 확대하지 않음. |
| TXN-DAC-03 | 조건부 유예 | release/reject/만료·직무분리·관리 감사 원자성 신규 설계는 미적용. 향후 채택 시 멱등 키 범위·저장소·TTL·경합까지 함께 결정. |
| TXN-DAC-04 | 추가 Migration 없음 / 기존 보완 유지 | 보류용 backfill/rollback 설계는 유예. 기존 0002 drift·운영 적용·복구 검증은 P1-DB-01/P1-DR-01에서 유지. |
| TXN-DAC-05 | 변경 없음 | 이번 선택으로 Interface 변경 ICR 없음. 향후 IF-03 Payload/Auth/Port 등 변경 시 전체 Producer/Consumer 영향으로 ICR 수행. |
| TXN-DAC-06 | 현행 유지 / 후속 검증 | 기존 저장 성공/실패와 Rule 탐지 메트릭 구분 유지. 신규 보류/거절 메트릭 없음. 현재 메트릭 타입·집계·실패 시 의미는 P1-APP/MON/E2E 확인. |
| TXN-DAC-07 | 종결 지시 확보 | #4 정책 선택 → #5 계약 유지 순서를 적용하고 사용자 지시로 종결. 현재 API/DB Runtime PASS를 선언하지 않음. |

# 검증 및 증적

- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) / D-SEC-01 v1.0 / D34 승인 기록.
- 리드 원문, `FDS_Decisions_4-6_Review_and_Closure_v1.1.md`, `FDS_Security_Demo_Scenarios_v1.5.md`.
- 사용자 종결 지시: 2026-09-09 현재 대화의 명시적 지시. 종결 실행·재조회 결과는 GitHub 기록 및 배포 Release Notes에 연결.
- Runtime 실행: 이번 검토에서 NOT RUN. 앱 저장소 현재 접근 결과 404는 미존재 증명이 아님.
- 신규 시험의 명령·입력·환경·정책 SHA·기대결과·복구·원본 증적은 각 구현 티켓에 연결.

# Dependency

- Related Ticket: P1-APP-01; P1-DB-01; P1-SEC-01; P1-E2E-01; P1-DR-01; P1-MON-01; P1-DOC-01
- #4는 업무 정책, #5는 API·DB 표현, #6은 업무 권한·관리 조치 감사 정책을 소유한다. 이번에는 모두 현행 유지·조건부 유예다.
- 기존 업무의 근거 확인과 Runtime 선행은 유지한다. #6의 기존 보안 시험 설계를 미채택 보류 정책에 종속시키지 않는다.
- 후속 Due: 각 기존 티켓의 Gate/종결 전. 시연 후보의 경우 리허설 GO 판정 전. G2 2026-09-11 및 기존 WBS를 자동 변경하지 않음.

# Decision / Risk Control

- **재검토 조건:** 상태/응답/IF-03 Payload/Schema·멱등성 계약의 실질 변경 요청 발생 시.
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
- **Exit Criteria:** 기존 계약 유지 선택, 신규 상태/API·Migration 변경 유예, #4/#6과 정책·표현 소유권 및 기존 구현 정합성 후속 기록.
- **Approved Option / Rationale:** C 선택 — 보류 미도입에 따른 기존 계약 유지. 신규 status 컬럼, release/reject endpoint, 응답 코드 전면 변경, 관리 조치 감사·멱등성 체계를 추가하지 않음.
- **Approver / Authority:** 이권욱의 명시적 4~6번 종결 지시.
- **Runtime Result:** NOT RUN / NOT VERIFIED, 기존 부분 증적의 판정 유지.
- **Baseline Integration:** v3.1.18 CANDIDATE에 반영. 발행 전 RELEASED v3.1.17 유지.
- **AI 사용:** CODEX_ASSISTED. 정책값·실서버 결과·사람의 독립 승인을 생성하지 않음.

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `5538d2581e405a721740a841bd64a28a5f56e959268a93fa6503bc9e751812ae`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
# DEC-P1-TXN-01 — 거래 상태·API 응답·재시도·데이터 정합성 계약 결정

> **버전:** v1.1 — 종결 결정 기록  
> **결정일:** 2026-09-09  
> **Lifecycle:** Done / GitHub Closed  
> **결과:** C 선택 — 보류 미도입에 따른 기존 계약 유지. 신규 status 컬럼, release/reject endpoint, 응답 코드 전면 변경, 관리 조치 감사·멱등성 체계를 추가하지 않음.  
> **정본 반영:** 미반영 — 합의 결과의 정본 통합은 후속. 현행 RELEASED v3.1.17 유지.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | DEC-P1-TXN-01 |
| Phase | Phase 1 |
| Category | Application / Data / Interface |
| Type | Decision |
| Status | Done |
| Priority | P0 |
| Start | 2026-09-08 |
| End | 2026-09-09 |
| Calendar Days | 2 |
| Working Days | 2 |
| Lead | 이재환 |
| Support | 이하영, 이권욱 |
| Exit Criteria | 기존 계약 유지 선택, 신규 상태/API·Migration 변경 유예, #4/#6과 정책·표현 소유권 및 기존 구현 정합성 후속 기록 |
| Related Decision IDs | D03; D04; D18; D28; D34; D35; DEC-P1-FDS-01 |
| Related Risk IDs | 현행 정의 연결 대기. v1.0 인용: RISK-05; RISK-07; RISK-09 — 본 종결의 위험 승인 근거로 사용하지 않음 |
| Source | Baseline v3.1.17; D-SEC-01 v1.0/D34; Issue #4~6 리드 의견; 2026-09-09 사용자 종결 지시; 통합 검토 v1.1 |
| Schedule Note | 현행 유지·신규 기능 유예 결정 종결. Priority는 결정 우선순위이며 신규 기능 G2 편입 아님. Runtime/정본 반영은 별도. Notion은 같은 Record ID로 수동 Upsert. |

# 🎯 User Story

Application·Data 담당자로서 선택된 현행 유지 범위에 맞춰 새 상태/API 변경을 유예하고 현재 계약과 Migration 정합성 확인을 기존 구현 티켓에 연결한다.

# 📌 Scope

## In Scope

- #4의 현행 유지 선택에 따른 API·DB 계약 변경 없음 결정
- 201 자원 생성과 업무 실행 승인 구분
- Migration drift 및 실패 응답 근거 등 기존 계약 확인의 후속 인계

## Out of Scope

- 보류 상태·해제/거절 API·새 멱등성 저장소/TTL/잡의 추가
- 신규 관리 상태를 위한 backfill·Migration 또는 기존 201 일괄 403 변경
- 기존 Schema drift·미검증 실패 경로를 해소된 것으로 처리

# 📋 핵심 요구사항

## 종결 근거와 범위

2026-09-09 사용자가 “4 / 5번 리드 의견도 같은 기준으로 검토해주고, 4~6번 티켓 종결 처리해줘”라고 지시했다. 앞선 프론트엔드 배치 사양 제외 지시와 첨부 시연 초안의 현행 탐지·기록 방향을 함께 적용해 **현행 유지·기능 확대 유예**로 종결한다. v1.0에 규정된 미도입/유예 종결 경로를 사용한다.

이 기록은 불확실한 현재 구현을 승인하는 기록이 아니다. 리드의 작성 측 자체점검/PENDING을 독립 승인으로 바꾸지 않는다. 사람의 신규 독립 승인 서명을 생성하지 않으며, 사용자 최종 종결 지시와 Codex의 문서 검토 범위를 구분해 기록한다. 기존 Runtime AC, G2와 보안 기준은 유지한다.


**선택 결과:** C 선택 — 보류 미도입에 따른 기존 계약 유지. 신규 status 컬럼, release/reject endpoint, 응답 코드 전면 변경, 관리 조치 감사·멱등성 체계를 추가하지 않음.

## 리드 의견 검토·반영

[리드 원문](https://github.com/321Team/fds-project-baseline/issues/5#issuecomment-5596626893)을 보존하고 다음과 같이 처리한다.

- 권위 OpenAPI/Migration 경로와 SHA 필요성은 수용한다. “연결에서 미확보”로 기록하며 앱 소스가 존재하지 않는다고 단정하지 않는다.
- v1.0 In Scope의 “확보”는 수행 목표이므로 그 문구만으로 이미 확보했다고 주장한 상충은 아니다. 현재 확보 상태는 별도 명시한다.
- #4 실패 정책과 #5 응답·저장 계약 소유권을 분리한다. 관리 조치 감사 정책은 #6, 원자성/응답 구현 계약은 #5다.
- 멱등성 TTL/저장소, IF-03 Payload ICR, 동기 타임아웃, 복구 호환성은 해당 변경을 채택할 때 함께 결정할 항목으로 수용한다. 현행 유지 선택에 새 기능 의무를 만들지 않는다.
- 기존 Migration drift 보완은 보류 기능과 무관한 기존 구현 작업이다. 코드 작성·병합·운영 적용·API 재현·복구를 따로 확인한다.
- 고정 태그/커밋 사용 제안은 수용한다. `2d93395a…`는 유효한 정본 최종화 커밋이며 잘못된 참조로 취급하지 않는다.

# ✅ Acceptance Criteria

v1.0의 AC ID를 보존한다. 표의 “후속 검증”은 미검증 상태를 뜻하며 체크박스 PASS로 대체하지 않는다. 이번 Done은 현행 유지·유예 선택의 종결이다.

| 기존 AC ID | 처리 | 결정/후속 |
|---|---|---|
| TXN-DAC-01 | 변경 없음 / 후속 검증 | 새 계약을 승인하지 않음. 현행 OpenAPI·Migration·Rule 경로/SHA 확보는 P1-APP-01/P1-DB-01의 기존 Runtime 근거로 유지. |
| TXN-DAC-02 | 확대 계약 유예 | 신규 업무 상태·HTTP 표를 만들지 않음. 기존 정상/탐지/평가 실패/DB 실패 응답은 권위 소스 및 fixture로 확인. 단일 201 증적을 전체 계약으로 확대하지 않음. |
| TXN-DAC-03 | 조건부 유예 | release/reject/만료·직무분리·관리 감사 원자성 신규 설계는 미적용. 향후 채택 시 멱등 키 범위·저장소·TTL·경합까지 함께 결정. |
| TXN-DAC-04 | 추가 Migration 없음 / 기존 보완 유지 | 보류용 backfill/rollback 설계는 유예. 기존 0002 drift·운영 적용·복구 검증은 P1-DB-01/P1-DR-01에서 유지. |
| TXN-DAC-05 | 변경 없음 | 이번 선택으로 Interface 변경 ICR 없음. 향후 IF-03 Payload/Auth/Port 등 변경 시 전체 Producer/Consumer 영향으로 ICR 수행. |
| TXN-DAC-06 | 현행 유지 / 후속 검증 | 기존 저장 성공/실패와 Rule 탐지 메트릭 구분 유지. 신규 보류/거절 메트릭 없음. 현재 메트릭 타입·집계·실패 시 의미는 P1-APP/MON/E2E 확인. |
| TXN-DAC-07 | 종결 지시 확보 | #4 정책 선택 → #5 계약 유지 순서를 적용하고 사용자 지시로 종결. 현재 API/DB Runtime PASS를 선언하지 않음. |

# 🧪 검증 및 증적

- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) / D-SEC-01 v1.0 / D34 승인 기록.
- 리드 원문, `FDS_Decisions_4-6_Review_and_Closure_v1.1.md`, `FDS_Security_Demo_Scenarios_v1.5.md`.
- 사용자 종결 지시: 2026-09-09 현재 대화의 명시적 지시. 종결 실행·재조회 결과는 GitHub 기록 및 배포 Release Notes에 연결.
- Runtime 실행: 이번 검토에서 NOT RUN. 앱 저장소 현재 접근 결과 404는 미존재 증명이 아님.
- 신규 시험의 명령·입력·환경·정책 SHA·기대결과·복구·원본 증적은 각 구현 티켓에 연결.

# 🔗 Dependency

- Related Ticket: P1-APP-01; P1-DB-01; P1-SEC-01; P1-E2E-01; P1-DR-01; P1-MON-01; P1-DOC-01
- #4는 업무 정책, #5는 API·DB 표현, #6은 업무 권한·관리 조치 감사 정책을 소유한다. 이번에는 모두 현행 유지·조건부 유예다.
- 기존 업무의 근거 확인과 Runtime 선행은 유지한다. #6의 기존 보안 시험 설계를 미채택 보류 정책에 종속시키지 않는다.
- 후속 Due: 각 기존 티켓의 Gate/종결 전. 시연 후보의 경우 리허설 GO 판정 전. G2 2026-09-11 및 기존 WBS를 자동 변경하지 않음.

# ⚖️ Decision / Risk Control

- **재검토 조건:** 상태/응답/IF-03 Payload/Schema·멱등성 계약의 실질 변경 요청 발생 시.
- **Risk 참조:** v1.0 ID는 역사적 참조로 보존. 발견된 구 v3.0 Risk CSV의 의미·상태를 현행 정본에 자동 승격하지 않음. 실제 위험 수용이 필요할 때 권위 정의·영향·수용자·근거를 먼저 고정.
- **미확인 구현:** fail-open·인증·Migration/Schema drift·정책 차단 원인·CI 상태를 포괄 승인하지 않음.
- **변경 통제:** 실질 계약/통신/권한 변경 발생 시 CR/ICR 영향도 검토. 기존 D번호 의미를 바꾸거나 신규 번호를 임의 부여하지 않음.

# 🔍 Review / Handoff

- Lead: 이재환; Support: 이하영, 이권욱.
- 기술 검토: Codex 보조 문서·소스 대조. 리드의 작성 측 자체점검과 별도 기록.
- 최종 종결 지시: 이권욱, 2026-09-09 현재 대화.
- 사람 독립 리뷰: 새 승인 서명 미생성. 기존 리드 PENDING/자체점검을 APPROVED로 변경하지 않음.
- 구현 확인과 보안 부정시험은 위 기존 티켓 담당자가 수행하고 실제 증적으로 판정.
- 정본 통합: P1-DOC-01에서 승인 기록·변경 이력·Ticket Pack·WBS/Gantt·Release Notes 영향 검토 후 후보로 반영.

# 📝 Completion Record

- **Result:** Decision Completed — 현행 유지 / 신규 기능 확대 유예.
- **Status:** Done.
- **Completed Date:** 2026-09-09.
- **Exit Criteria:** 기존 계약 유지 선택, 신규 상태/API·Migration 변경 유예, #4/#6과 정책·표현 소유권 및 기존 구현 정합성 후속 기록.
- **Approved Option / Rationale:** C 선택 — 보류 미도입에 따른 기존 계약 유지. 신규 status 컬럼, release/reject endpoint, 응답 코드 전면 변경, 관리 조치 감사·멱등성 체계를 추가하지 않음.
- **Approver / Authority:** 이권욱의 명시적 4~6번 종결 지시.
- **Runtime Result:** NOT RUN / NOT VERIFIED, 기존 부분 증적의 판정 유지.
- **Baseline Integration:** 미반영. 현재 RELEASED v3.1.17 유지.
- **AI 사용:** CODEX_ASSISTED. 정책값·실서버 결과·사람의 독립 승인을 생성하지 않음.
````

</details>
