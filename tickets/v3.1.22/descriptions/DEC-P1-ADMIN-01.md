문서 버전 **v3.1.22 / CANDIDATE**. 사용자 이권욱의 2026-10-19 정본 발행 지시에 따른다. PR191 내용 병합 `caa13c1839b31675794abd1ca9c1071376561643`와 실제 후속 인수·Signoff·Close를 입력으로 삼는다. 과거 입력 안의 후보/미발행·당시 미완료 표현은 당시 이력이며 현재 문서 상태는 이 절과 CURRENT/Release API를 따른다. 새 Runtime·서버·P2 실행·원 AC의 기술 MET 승격은 없다.

# DEC-P1-ADMIN-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. v3.1.22 관리·인수 기록 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/6) · updated_at `2026-10-09T13:05:12Z` · body SHA256 `bbf7b122c22921cd5716fd1edad36a167170afd5a83801b1a666204c9e80285d`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
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
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #6 snapshot 2026-09-10T01:22:24Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 현행 유지·신규 기능 확대 유예 결정 Done. 본 v3.1.18 후보에 통합하며 발행 전 운영 정본은 v3.1.17이다. 신규 기능 G2 편입·Runtime 승인은 아니다. |

실제 GitHub 종결 `2026-09-09T15:37:24+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

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

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
