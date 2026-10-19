# P1-APP-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. 미발행 정본 후보 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/15) · updated_at `2026-10-19T09:04:25Z` · body SHA256 `139c96c3100e454eff08d1328afba3d362d9ea2ffacbc01ce5827ec66918cd7d`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | P1-APP-01 |
| Phase | Phase 1 |
| Category | Application / MSA |
| Type | Task |
| Status | Done |
| Priority | P0 |
| Start | 2026-09-01 |
| End | 2026-09-18 |
| Calendar Days | 18 |
| Working Days | 9 |
| Lead | 이재환 |
| Support | 이하영 |
| Exit Criteria | 2개 Deployment/Service, 업무 8000/8001·metrics 9091/9090, `/livez`·`/readyz`, DB/FDS 장애정책, Resource, local endpoint topology, Contract/E2E Evidence |
| Related Decision IDs | D03; D04; D18; D27; D31; D34 |
| Related Risk IDs | RISK-07; RISK-09 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #15 snapshot 2026-09-10T04:01:11Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 09-11 인계 및 사전 검증, 09-18 복귀 후 정본 Runtime 통합. 휴가 중 미승인 업무 계약·Schema 변경은 중단한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |

실제 GitHub 종결 `2026-10-19T18:04:23+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

- [x] 업무·메트릭 Port 분리
  - 전용 리스너 구현·단위시험은 확보. 최종 Image/Service/정본 Runtime 포트 분리 및 업무 포트 `/metrics` 접근 통제 확인은 남아 있다.
- [x] 외부 DB 장애 시 transaction-api `/readyz` 503와 Endpoint 제외
  - DB mock 503 시험은 PASS. 최종 계약의 FDS 장애 처리 및 실제 Kubernetes Endpoint 제외 증적은 미확인이다.
  - **2026-09-23 정본 클러스터 시도(미완료)**: worker02(10.1.93.107)→db01:5432를 firewalld rich-rule로 임시 차단 후 기존 transaction-api Pod로 확인했더니 readyz=200/실제 거래도 201로 계속 성공 — **커넥션 풀이 차단 전에 이미 맺어둔 연결을 재사용**해서 신규 연결 차단의 영향을 안 받는 것으로 추정(방화벽은 신규 연결만 막고 기존 세션은 안 끊김). 이를 확인하려고 해당 Pod를 삭제해 재생성 유도했으나, **재생성된 Pod가 차단 안 된 worker01로 스케줄**돼 실패 재현이 안 됨. 3개 Worker(.105/.107/.108) 전부 동시 차단하면 확실하지만 두 replica가 한꺼번에 NotReady 될 위험이 있어 **사용자 판단으로 중단**, db01 방화벽은 즉시 원복 완료(rich-rule 제거 확인함). 재시도 시 3-replica 확보(worker당 1개) 후 1개씩 통제된 차단을 권장.
- [x] fds-engine 장애 시 transaction-api는 Ready를 유지하고 거래를 fail-open(`fds_evaluation_skipped=true`, HTTP 201)으로 저장
  - [CR-P1-APP-01-01 #119](https://github.com/321Team/fds-project-baseline/issues/119)로 기존 "DB/FDS 장애 시 `/readyz` 503" 줄을 두 줄로 나눴다(2026-10-01, APP Lead 결정·G3 수용). Runtime 증적 필요.
- [x] 외부 DB 장애가 Liveness 재시작 루프를 만들지 않음
  - `/livez`의 무의존성 코드·단위시험은 확인. 실제 DB 장애/복구 중 restartCount·Probe 결과는 미확인이다.
- [x] 승인 Worker backend에 local endpoint 존재
  - 승인 Worker별 EndpointSlice/local endpoint와 P1-LB Stage B 검증이 필요하다.
  - **2026-10-06 기준시점 정정:** 이 체크는 10/2 16:12 조회 시점의 결과다([evidence#100](https://github.com/321Team/fds-project-evidence/pull/100)). 10/4 worker03 장애 뒤 worker03의 앱 Pod와 local endpoint가 0이 되어 현재는 충족되지 않는다. 핵심 요구 "`externalTrafficPolicy: Local` 대상 Worker에 local endpoint를 보장한다"와 함께 NOT MET·Known Issue로 관리한다([5980422387](https://github.com/321Team/fds-project-baseline/issues/15#issuecomment-5980422387), PMO 수용 [5989190781](https://github.com/321Team/fds-project-baseline/issues/15#issuecomment-5989190781)). 이 체크를 현재 충족으로 읽지 않으며, Close 분류는 #30에서 한다.
- [x] R01/R02/R04/R07와 DB 저장 PASS
  - engine Unit/Contract 시험 24건과 [임시 k3s 저장·조회 증적](https://github.com/321Team/fds-project-evidence/blob/90093f88167055f81e8789d2a848f44ead0ee9ce/docs/evidence/P1-DB-01/evidence-20260907.md)는 유지한다. 실제 DB를 쓰지 않는 CI32건을 Rule→DB→정본 E2E 전체 PASS로 계산하지 않는다.

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
