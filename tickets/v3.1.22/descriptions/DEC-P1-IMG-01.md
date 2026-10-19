문서 버전 **v3.1.22 / CANDIDATE**. 사용자 이권욱의 2026-10-19 정본 발행 지시에 따른다. PR191 내용 병합 `caa13c1839b31675794abd1ca9c1071376561643`와 실제 후속 인수·Signoff·Close를 입력으로 삼는다. 과거 입력 안의 후보/미발행·당시 미완료 표현은 당시 이력이며 현재 문서 상태는 이 절과 CURRENT/Release API를 따른다. 새 Runtime·서버·P2 실행·원 AC의 기술 MET 승격은 없다.

# DEC-P1-IMG-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. v3.1.22 관리·인수 기록 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/110) · updated_at `2026-10-09T13:06:47Z` · body SHA256 `4b4697034576312673a8265cf8c3f8a8ca98797da40bb98569cff9ac45407682`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | DEC-P1-IMG-01 |
| Phase | Phase 1 |
| Category | Application / Container Supply Chain / Security |
| Type | Decision |
| Status | Done |
| Priority | P0 |
| Start | 2026-09-27 |
| End | 2026-10-06 |
| Calendar Days | 10 |
| Working Days | 7 |
| Lead | 이재환 |
| Support | 이하영, 이권욱 |
| Exit Criteria | P1 애플리케이션 런타임 공급망 선택안, signed attestation 처리 방식, 운영 Dockerfile·Harbor·Kubernetes 후속 게이트 및 롤백 조건을 명시적으로 승인 |
| Related Decision IDs | D12; D17; D18; D19; D34; DEC-P1-TLS-01 |
| Related Risk IDs | RISK-06; RISK-07; RISK-08; RISK-09 |
| Source | Baseline v3.1.20; 승인 전 candidate validation HEAD `88b494c58d057303672cc1502021ab4655a4e916`; Source validation Run `36261976339`; attestation probe Run `36261976189`; 승인 구현 `321Team/fds-msa#9` HEAD `0bea0d4fa8ece5ecbf7aa5fd8f054fc24f5556cf`, merge `1c7f3651504097096c3a3fe4a86ac1973e169688`; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 기존 G2 계획일은 경과했다. 본 Decision은 2026-10-06 Phase 1 Review / Close 전 공급망 방향을 확정하기 위한 후속 게이트이며, 일정 입력만으로 승인 또는 런타임 완료 상태를 상향하지 않는다. |

실제 GitHub 종결 `2026-09-27T23:20:19+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

원 AC/Exit 및 상세 변경결정은 [현재 원문](https://github.com/321Team/fds-project-baseline/issues/110)을 따른다. 이 후보는 AC를 재작성하지 않는다.

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
