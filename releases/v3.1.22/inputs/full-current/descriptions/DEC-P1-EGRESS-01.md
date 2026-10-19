# DEC-P1-EGRESS-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. 미발행 정본 후보 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/78) · updated_at `2026-10-09T13:06:42Z` · body SHA256 `3f09efe53d1f01206b30ed01350e2db4571cc49f6cad3f255390058edbf28b9b`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | DEC-P1-EGRESS-01 |
| Phase | Phase 1 |
| Category | Monitoring / Architecture / Egress |
| Type | Decision |
| Status | Done |
| Priority | P1 |
| Start | 2026-09-14 |
| End | 2026-09-21 |
| Calendar Days | 8 |
| Working Days | 6 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | 배치·예외 정책 기록, 예약 IP/자산 충돌 확인, 자원 영향 검토, #74/#75 구현·인계 조건 연결 |
| Related Decision IDs | D17; D33; D34; D35 — 기존 의미 유지. 신규 D/IF 순번은 정본 레지스터 대조 후 부여 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | 사용자 2026-09-14 “위 권장안 적용하고 예비 주소 사용을 위한 체크”; 발행 docs-v3.1.18; #74/#75; infra-ansible PR #12; 2026-09-14~15 실행·증적; 사용자 2026-09-16 전수 종결 지시; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | Decision 범위 종결. 초기 계획 End 2026-09-21은 G2 추적 목표로 보존한다. 배치·정책·예약 IP/자산·자원 영향·#74/#75 구현/인계 조건 확정이 완료되어 2026-09-16 Done 처리한다. #74/#75의 Squid/NetworkPolicy Runtime·독립 리뷰·서비스 인수는 계속 별도 추적하며 본 종결로 완료 처리하지 않는다. 교육장 주말 작업 0 원칙 유지. |

실제 GitHub 종결 `2026-09-16T18:59:17+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

원 AC/Exit 및 상세 변경결정은 [현재 원문](https://github.com/321Team/fds-project-baseline/issues/78)을 따른다. 이 후보는 AC를 재작성하지 않는다.

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
