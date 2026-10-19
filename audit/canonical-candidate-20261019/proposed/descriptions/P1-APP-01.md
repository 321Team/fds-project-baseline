# P1-APP-01 후속 상태 후보 — 2026-10-19

**후보 범위:** 실제 Status Done/closed(completed), 완료시각 `2026-10-19T18:04:23+09:00`. 원 계획일·Owner·Exit/체크는 v3.1.21 입력을 보존한다. 아래 기존 수집시점 open/미완료 표현과 체크는 당시 이력이며 현재 종결은 [실제 기록](https://github.com/321Team/fds-project-baseline/issues/15#issuecomment-6263617401) 및 이 단락을 따른다. 기술 미입증·미실행의 체크를 바꾸지 않는다.

**유지할 한계:** D07 Major/P1 코드 무수정·해당 Negative NOT_RUN/운영 DB 제약 NOT_VERIFIED, I01 Minor, E1/E2 단회, 2분 NodePort 부하·PG16.8/16.14·HA POST 무손실/전체 Drain 미입증 경계 유지. 최종224/실패233/부하228·DB11·HA221/10월19일 분산 증거의 실제 범위만 수용.

기존본문 source body SHA는 당시 원문 식별자다. 현재 GitHub body SHA256 `139c96c3100e454eff08d1328afba3d362d9ea2ffacbc01ce5827ec66918cd7d`·updated_at `2026-10-19T09:04:25Z`. 본 후보 편입은 새 시험·승인·정본발행·전체Close가 아니다. CODEX_ASSISTED.

---

# P1-APP-01 — transaction-api / fds-engine

Version: v3.1.21 기반 후속 반영 후보 — 선택7건 상태·실제종결 범위
Source: https://github.com/321Team/fds-project-baseline/issues/15
Updated at: 2026-10-02T07:33:37Z
Source body SHA256: `3c881a85b1918c4f8a025e2693f0f1a14fee72830206ba53566c0c39c2cdb236`
GitHub: open / None
Current disposition: local endpoint guarantee NOT MET.

| Property | Current source value |
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
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #15 snapshot 2026-09-10T04:01:11Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청 |
| Schedule Note | 09-11 인계 및 사전 검증, 09-18 복귀 후 정본 Runtime 통합. 휴가 중 미승인 업무 계약·Schema 변경은 중단한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |

## Source checklist

- [x] 업무 API와 metrics Listener/Service를 분리한다.
- [x] 외부 DB 장애는 Readiness에 반영하되 Liveness 재시작 루프를 만들지 않는다.
- [ ] `externalTrafficPolicy: Local` 대상 Worker에 local endpoint를 보장한다.
- [x] Workload별 Request/Limit을 부하 시험으로 확정한다.
- [x] 업무·메트릭 Port 분리
- [x] 외부 DB 장애 시 transaction-api `/readyz` 503와 Endpoint 제외
- [x] fds-engine 장애 시 transaction-api는 Ready를 유지하고 거래를 fail-open(`fds_evaluation_skipped=true`, HTTP 201)으로 저장
- [x] 외부 DB 장애가 Liveness 재시작 루프를 만들지 않음
- [x] 승인 Worker backend에 local endpoint 존재
- [x] R01/R02/R04/R07와 DB 저장 PASS

## Source body snapshot

아래 원문은 보관 문구와 과거 제안을 포함한다. 위 current disposition 및 원문의 최신 명시적 결정이 과거 제안보다 우선한다. 원문 수정·인수 상태 승격 없음.

<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23 (누락분 2026-09-25 반영)

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/P1-APP-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/P1-APP-01/`
- 이 티켓은 2026-09-23 일괄 반영(49건)의 대상 추출에서 누락되어 2026-09-25 같은 형식으로 반영했다(“Evidence Path:” 표기 없이 경로만 적힌 형식). 근거: `audit/phase2-repo-bootstrap-20260923/evidence-path-followup-20260925/`.
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 접근 가능한 앱 repo/고정 SHA와 현재 계약·Rule·Probe·실패 fixture 연결 ; A04. 정본 배포는 별도.

- 현재 Probe는 /livez·/readyz 기준으로 계약·manifest·시험을 맞춘다. API/engine 업무 8000/8001과 metrics9091/9090, Service80→8000, local endpoint topology·Resource를 고정 소스와 정본 Runtime 결과에 연결한다.

**현재 앱·Rule·시간 계약 (A04)** — 앱 main `01758583c03bcbf45c96eb9d7b868cee4a2ed9df`를 현재 접근 가능한 소스로 연결한다. 계약 v1.0은 DRAFT·실패정책 OPEN·옛 Probe/P1-MSA-01 표기가 남아 있다. 구현의 엔진 실패 fail-open(connect1s/read2s), DB 실패 rollback/HTTP500, R04 KST01:00≤시각<05:00·100만원 이상을 소스/fixture/승인 근거와 대조한다. UTC 전송·KST 판정은 양립 가능하다. 입력 offset/naive 처리·DB timezone·저장 자료형·표시 기준을 분리해 기록하며 새 정책 승인으로 간주하지 않는다.
근거: [계약](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/docs/transaction-api_fds-engine_contract_v1.0.md) · [Rule](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/fds-engine/app/rules.py) · [API](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/transaction-api/app/main.py) · [client](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/transaction-api/app/fds_client.py)

**인계·관련 티켓:** [#11](https://github.com/321Team/fds-project-baseline/issues/11) · [#17](https://github.com/321Team/fds-project-baseline/issues/17) · [#19](https://github.com/321Team/fds-project-baseline/issues/19) · [#20](https://github.com/321Team/fds-project-baseline/issues/20).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:P1-APP-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P1-APP-01 -->
# P1-APP-01 — transaction-api / fds-engine

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

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
| End | 2026-09-18 |
| Calendar Days | 18 |
| Working Days | 9 |
| Lead | 이재환 |
| Support | 이하영 |
| Exit Criteria | 2개 Deployment/Service, 업무 8000/8001·metrics 9091/9090, `/livez`·`/readyz`, DB/FDS 장애정책, Resource, local endpoint topology, Contract/E2E Evidence |
| Related Decision IDs | D03; D04; D18; D27; D31; D34 |
| Related Risk IDs | RISK-07; RISK-09 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #15 snapshot 2026-09-10T04:01:11Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청 |
| Schedule Note | 09-11 인계 및 사전 검증, 09-18 복귀 후 정본 Runtime 통합. 휴가 중 미승인 업무 계약·Schema 변경은 중단한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **In Progress / open**. 원본 갱신 시각: `2026-09-10T04:01:11Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.
- 수집된 운영 댓글은 원래 위치에 보존한다. 신규 구현 제출/리뷰 요청은 실행 PASS나 승인으로 간주하지 않는다.
  - [5612760489](https://github.com/321Team/fds-project-baseline/issues/15#issuecomment-5612760489) · 2026-09-10T04:01:11Z

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

임시 k3s/fds의 FastAPI 스캐폴딩, /livez·/readyz 및 Secret 갱신 이력이 보고됐다. 정본 fds-app 배포는 미검증이며 Service 80→8000, 불변 Digest, RBAC, 승인 경로 및 실패 응답/DB 저장 계약 확인이 남아 있다. D17/D34 설계 승인은 2026-09-01 완료됐고 현재 대기는 Platform Ready와 실제 보안 적용이다. DEC-P1-FDS/TXN/ADMIN의 현행 유지·확대 유예 선택을 적용한다. 현재 후보 Plan: 2026-09-01 ~ 2026-09-18 (권장안; 실제 완료일·Gate 승인은 미확정).

근거: [Issue #15](https://github.com/321Team/fds-project-baseline/issues/15), Issue 갱신 시각 `2026-09-10T04:01:11Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 일정 권장안

Start/End는 이번 Fast Tracking 후보의 계획값이다. 기존 승인 일정은 `audit/v3.1.18/fast-track-plan.json`에 전후 값으로 보존한다. 실제 착수·완료·Status·AC·승인을 변경한 것이 아니다. 교육장 주말 작업은 없으며 세부 AM/PM 배정과 선행 조건을 따른다.

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

> 2026-09-18 증적 대조: 조직 앱 [main `60f46a9a95b363fb8d6117c9ae098081171caaf9`](https://github.com/321Team/fds-msa/blob/60f46a9a95b363fb8d6117c9ae098081171caaf9)에 dual-port 구현과 앱 이관·오프라인 인계가 병합됐다. [기존 CI](https://github.com/321Team/fds-msa/actions/runs/35312767908) 원본 로그에서 정적 73파일 PASS, transaction-api 8 PASS·fds-engine 24 PASS를 확인했다(원 실행 2026-09-18 14:56 KST). 실제 DB·클러스터·오프라인 Build/Scan/Deploy 시험과 구분한다.

- [x] 업무 API와 metrics Listener/Service를 분리한다.
  - 코드 진전: [API run.py](https://github.com/321Team/fds-msa/blob/60f46a9a95b363fb8d6117c9ae098081171caaf9/transaction-api/run.py) `8000/9091`, [engine run.py](https://github.com/321Team/fds-msa/blob/60f46a9a95b363fb8d6117c9ae098081171caaf9/fds-engine/run.py) `8001/9090` 분리 리스너가 구현됐다. 다만 업무 app의 `/metrics` 라우트도 남아 있어 접근 통제와 최종 Service/Prometheus/NetworkPolicy·배포값의 일치 검증이 필요하다. 예전 '전용 listener 미구현'을 현재 상태로 반복하지 않는다.
- [x] 외부 DB 장애는 Readiness에 반영하되 Liveness 재시작 루프를 만들지 않는다.
  - 코드·MOCK: `/readyz`는 db_ping 실패 시 503, `/livez`는 외부 호출 없이 응답한다. [health 시험](https://github.com/321Team/fds-msa/blob/60f46a9a95b363fb8d6117c9ae098081171caaf9/transaction-api/tests/test_health.py)은 실제 PostgreSQL 없이 DB 성공/실패를 mock한다. 실제 장애 주입·Endpoint 제외·재시작 관측은 잔여다.
- [ ] `externalTrafficPolicy: Local` 대상 Worker에 local endpoint를 보장한다.
  - 정본 Worker의 최종 Service/EndpointSlice·backend 관측을 P1-K8S/P1-LB와 연결해야 하며 앱 소스 병합만으로 완료되지 않는다.
- [x] Workload별 Request/Limit을 부하 시험으로 확정한다.
  - 현재 Unit/Contract CI는 부하 시험이 아니다. 최종 digest·부하/자원 관측 근거는 미확인이다.

### Acceptance Criteria

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
- [x] R01/R02/R04/R07와 DB 저장 PASS
  - engine Unit/Contract 시험 24건과 [임시 k3s 저장·조회 증적](https://github.com/321Team/fds-project-evidence/blob/90093f88167055f81e8789d2a848f44ead0ee9ce/docs/evidence/P1-DB-01/evidence-20260907.md)는 유지한다. 실제 DB를 쓰지 않는 CI32건을 Rule→DB→정본 E2E 전체 PASS로 계산하지 않는다.

### Evidence

- `321Team/fds-project-evidence:evidence/P1-APP-01/`
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

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `58a9bc9529bfd5180620d1a274bf9166f9b24d8c992ed504b560111984102581`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P1-APP-01 -->
# P1-APP-01 — transaction-api / fds-engine

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
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
| Source | Baseline v3.1.15; D-SEC-01 Security Design Baseline v1.0; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 이재환 09-04 개인 휴가를 owner-specific 비가용일로 반영해 종료를 09-10으로 조정한다. 이하영이 기술 지원하며 G2 09-11 목표는 유지한다. |

## 이관 기준 및 확인 사항

- 속성의 일정·담당·상태는 RELEASED v3.1.17 WBS(기준일 2026-09-04)를 우선 반영했다. 이후 별도 근거가 있는 변경만 아래에 명시한다.
- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) · [정본 WBS](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/wbs/FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx).
- 본문은 아래에 적힌 원본 버전의 기록이다. 위 속성·후속 승인과 다른 과거 상태는 현재 판정으로 사용하지 않는다. 이관 자체로 미실행 AC를 체크하거나 새 승인을 부여하지 않는다.
- Lead/Support의 풀네임은 본문 속성으로 보존한다. GitHub 계정 대응이 확인되지 않은 사람에게 자동 배정하지 않았다.

## 원본 및 변경 출처

- `FDS_Notion_Remaining_Backlog_Manual_v1.9.md`
- `FDS_v3.1.15_Canonical_Ticket_Update_Pack_v1.0.md`
- `FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx`

---

## Description — 보관 입력본

> 원본: `FDS_v3.1.15_Canonical_Ticket_Update_Pack_v1.0.md`. 원본의 완료/미완료 체크와 당시 이력을 보존했다.

### 🎯 User Story

애플리케이션 담당자로서 거래 처리와 FDS 판정을 독립 서비스로 구현하고, 업무·메트릭·상태 계약을 분리한다.

### 📌 Scope

#### In Scope

- transaction-api 8000 / metrics 9091
- fds-engine 8001 / metrics 9090
- `/livez`, `/readyz`
- Request/Limit 수치 측정
- Replica/topology/local endpoint

#### Out of Scope

- PSA/RBAC/NetworkPolicy/HostEndpoint 구현
- edge01 HAProxy 및 Kubernetes API LB 구성

### 📋 핵심 요구사항

- [ ] 업무 API와 metrics Listener/Service를 분리한다.
- [ ] 외부 DB 장애는 Readiness에 반영하되 Liveness 재시작 루프를 만들지 않는다.
- [ ] `externalTrafficPolicy: Local` 대상 Worker에 local endpoint를 보장한다.
- [ ] Workload별 Request/Limit을 부하 시험으로 확정한다.

### ✅ Acceptance Criteria

- [ ] 업무·메트릭 Port 분리
- [ ] DB/FDS 장애 시 `/readyz` 503와 Endpoint 제외
- [ ] 외부 DB 장애가 Liveness 재시작 루프를 만들지 않음
- [ ] 승인 Worker backend에 local endpoint 존재
- [ ] R01/R02/R04/R07와 DB 저장 PASS

### 🧪 Evidence

- `docs/evidence/P1-APP-01/`
- OpenAPI/Contract/Probe/Resource/Topology/E2E

### 🔗 Dependency

- Blocked By Runtime: P1-K8S Platform Ready
- Related: P1-SEC-01, P1-DB-01, P1-LB-01, P1-CICD-01

### ⚖️ Decision / Risk Control

- Decision: D18/D34의 Port·Probe·local endpoint 계약을 적용한다.
- Risk Control: local endpoint가 없는 Worker는 edge01 backend에서 제외하고 Replica/Topology 실패를 별도 Evidence로 남긴다.

### 🔍 Review / Handoff

- Review Owner: 이하영
- Handoff: metrics·Probe·Resource·topology 결과를 P1-SEC/P1-MON/P1-CICD에 전달한다.

### 📝 Completion Record

- Result: TBD
- Status: In Progress
- Completed Date: 미입력
- Reviewer / Approver: 미입력 — 입력 시 풀네임 사용
````

</details>
