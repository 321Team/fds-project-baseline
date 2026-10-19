문서 버전 **v3.1.22 / CANDIDATE**. 사용자 이권욱의 2026-10-19 정본 발행 지시에 따른다. PR191 내용 병합 `caa13c1839b31675794abd1ca9c1071376561643`와 실제 후속 인수·Signoff·Close를 입력으로 삼는다. 과거 입력 안의 후보/미발행·당시 미완료 표현은 당시 이력이며 현재 문서 상태는 이 절과 CURRENT/Release API를 따른다. 새 Runtime·서버·P2 실행·원 AC의 기술 MET 승격은 없다.

# DEC-P1-MON-02 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. v3.1.22 관리·인수 기록 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/109) · updated_at `2026-10-09T13:06:45Z` · body SHA256 `446bd362c4ccc94caf33335dee3cf0d7bac77be51722b2eade723a0195a2e63f`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | DEC-P1-MON-02 |
| Phase | Phase 1 |
| Category | Monitoring / Alerting / Security / Egress |
| Type | Decision |
| Status | Done |
| Priority | P1 |
| Start | 2026-09-26 |
| End | 2026-09-26 |
| Calendar Days | 1 |
| Working Days | 1 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | #75에서 승인된 Discord 제한 egress 범위, 발송 대상, Secret lifecycle, 실패·복구 인수 결과를 하나의 D-ID로 고정하고 #75/#17 및 v3.1.21 정본 인계 범위를 명시 |
| Related Decision IDs | DEC-P1-MON-01; DEC-P1-EGRESS-01 |
| Related Risk IDs | 미부여 — 정본 Risk Register 대조 후 부여 |
| Source | DEC-P1-EGRESS-01 #78; CR-P1-MON-01-02 #75; P1-MON-01 #17; 2026-09-26 Alertmanager Discord 제한 egress·발송·실패/복구 Runtime 인수 결과; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 2026-09-26 단일일 Decision으로 종결. #75의 Runtime/AC 인수 결과를 정책으로 고정했으며 P1-MON-01 route 형상·현장 반영 및 전체 Monitoring 인수는 별도 추적한다. |

실제 GitHub 종결 `2026-09-26T19:51:17+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

원 AC/Exit 및 상세 변경결정은 [현재 원문](https://github.com/321Team/fds-project-baseline/issues/109)을 따른다. 이 후보는 AC를 재작성하지 않는다.

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
