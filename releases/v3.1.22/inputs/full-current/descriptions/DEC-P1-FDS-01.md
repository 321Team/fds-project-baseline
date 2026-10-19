# DEC-P1-FDS-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. 미발행 정본 후보 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/4) · updated_at `2026-10-09T13:05:06Z` · body SHA256 `46c9744cb01d36d9f2f59eb0fe578d105f661637883a63675d4c59f470cc825e`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
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
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #4 snapshot 2026-09-10T01:21:55Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 현행 유지·신규 기능 확대 유예 결정 Done. 본 v3.1.18 후보에 통합하며 발행 전 운영 정본은 v3.1.17이다. 신규 기능 G2 편입·Runtime 승인은 아니다. |

실제 GitHub 종결 `2026-09-09T15:37:02+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

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

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
