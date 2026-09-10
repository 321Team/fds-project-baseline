<!-- fds-canonical-description:v3.1.18 record-id:P1-APP-01 -->
# P1-APP-01 — transaction-api / fds-engine

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P1-APP-01 |
| Phase | Phase 1 |
| Category | Application / MSA |
| Type | Task |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-09-01 |
| End | 2026-09-10 |
| Calendar Days | 10 |
| Working Days | 7 |
| Lead | 이재환 |
| Support | 이하영 |
| Exit Criteria | 2개 Deployment/Service, 업무 8000/8001·metrics 9091/9090, `/livez`·`/readyz`, DB/FDS 장애정책, Resource, local endpoint topology, Contract/E2E Evidence |
| Related Decision IDs | D03; D04; D18; D27; D31; D34 |
| Related Risk IDs | RISK-07; RISK-09 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #15 snapshot 2026-09-10T04:01:11Z |
| Schedule Note | 이재환 09-04 개인 휴가를 owner-specific 비가용일로 반영해 종료를 09-10으로 조정한다. 이하영이 기술 지원하며 G2 09-11 목표는 유지한다. |

## 현재 실행·검토 상태

임시 k3s/fds의 FastAPI 스캐폴딩, /livez·/readyz 및 Secret 갱신 이력이 보고됐다. 정본 fds-app 배포는 미검증이며 Service 80→8000, 불변 Digest, RBAC, 승인 경로 및 실패 응답/DB 저장 계약 확인이 남아 있다. D17/D34 설계 승인은 2026-09-01 완료됐고 현재 대기는 Platform Ready와 실제 보안 적용이다. DEC-P1-FDS/TXN/ADMIN의 현행 유지·확대 유예 선택을 적용한다.

근거: [Issue #15](https://github.com/321Team/fds-project-baseline/issues/15), Issue 갱신 시각 `2026-09-10T04:01:11Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- [후속 기록](https://github.com/321Team/fds-project-baseline/issues/15#issuecomment-5612760489)

---

### User Story

애플리케이션 담당자로서 거래 처리와 FDS 판정을 독립 서비스로 구현하고, 업무·메트릭·상태 계약을 분리한다.

### Scope

#### In Scope

- transaction-api 8000 / metrics 9091
- fds-engine 8001 / metrics 9090
- `/livez`, `/readyz`
- Request/Limit 수치 측정
- Replica/topology/local endpoint

#### Out of Scope

- PSA/RBAC/NetworkPolicy/HostEndpoint 구현
- edge01 HAProxy 및 Kubernetes API LB 구성

### 핵심 요구사항

- [ ] 업무 API와 metrics Listener/Service를 분리한다.
- [ ] 외부 DB 장애는 Readiness에 반영하되 Liveness 재시작 루프를 만들지 않는다.
- [ ] `externalTrafficPolicy: Local` 대상 Worker에 local endpoint를 보장한다.
- [ ] Workload별 Request/Limit을 부하 시험으로 확정한다.

### Acceptance Criteria

- [ ] 업무·메트릭 Port 분리
- [ ] DB/FDS 장애 시 `/readyz` 503와 Endpoint 제외
- [ ] 외부 DB 장애가 Liveness 재시작 루프를 만들지 않음
- [ ] 승인 Worker backend에 local endpoint 존재
- [ ] R01/R02/R04/R07와 DB 저장 PASS

### Evidence

- `docs/evidence/P1-APP-01/`
- OpenAPI/Contract/Probe/Resource/Topology/E2E

### Dependency

- Blocked By Runtime: P1-K8S Platform Ready
- Related: P1-SEC-01, P1-DB-01, P1-LB-01, P1-CICD-01

### Decision / Risk Control

- Decision: D18/D34의 Port·Probe·local endpoint 계약을 적용한다.
- Risk Control: local endpoint가 없는 Worker는 edge01 backend에서 제외하고 Replica/Topology 실패를 별도 Evidence로 남긴다.

### Review / Handoff

- Review Owner: 이하영
- Handoff: metrics·Probe·Resource·topology 결과를 P1-SEC/P1-MON/P1-CICD에 전달한다.

### Completion Record

- Result: TBD
- Status: In Progress
- Completed Date: 미입력
- Reviewer / Approver: 미입력 — 입력 시 풀네임 사용
