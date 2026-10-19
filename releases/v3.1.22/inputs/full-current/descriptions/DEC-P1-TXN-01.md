# DEC-P1-TXN-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. 미발행 정본 후보 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/5) · updated_at `2026-10-09T13:05:09Z` · body SHA256 `ebf035d43ba39e9c0fbbedb018bf784bfab1996f6c940fdbfa2a88806c70654e`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
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
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #5 snapshot 2026-09-10T01:22:10Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 현행 유지·신규 기능 확대 유예 결정 Done. 본 v3.1.18 후보에 통합하며 발행 전 운영 정본은 v3.1.17이다. 신규 기능 G2 편입·Runtime 승인은 아니다. |

실제 GitHub 종결 `2026-09-09T15:37:13+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

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

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
