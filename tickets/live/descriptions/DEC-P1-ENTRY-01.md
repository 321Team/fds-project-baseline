<!-- fds-canonical-live:v3.1.21 record-id:DEC-P1-ENTRY-01:start -->
## 현행 정본 적용 — v3.1.21

- 정본: [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21), 2026-10-04 14:49:12 KST 발행. 기준 커밋: `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`.
- [이 티켓의 발행 Description](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tickets/v3.1.21/descriptions/DEC-P1-ENTRY-01.md) · [Baseline](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/baseline/FDS_Project_Implementation_Baseline_v3.1.21.md) · [WBS](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/wbs/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx).
- [테스트 전략](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tests/FDS_Test_Strategy_v3.1.21.md): 해당 업무의 기존 AC·Exit Criteria와 실행/인수 구분을 유지한다.
- 정본 Description은 2026-10-03 수집 시점 기록이다. 발행 후 실제 수행·검토·잔여·승인 변경은 아래 최신 운영 기록과 원본 증적을 따른다. 아래 과거 버전의 '현행/후보/미발행' 문구는 작성 당시 이력이다.
- 발행·동기화로 Status, AC 체크, 실제 완료일, 담당자, 일정, Runtime 승인 또는 종결을 상향하지 않는다. 신규 계획·사양 충돌은 별도 변경결정으로 정합화한다.
- 반영 근거: 사용자 '디스크립션 파일 반영과 이슈 본문 수정' 지시. AI 사용: CODEX_ASSISTED.
<!-- fds-canonical-live:v3.1.21 record-id:DEC-P1-ENTRY-01:end -->

<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/DEC-P1-ENTRY-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/DEC-P1-ENTRY-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** Edge exposure 결정 종결 유지. Service80→8000·Local topology는 APP/LB/HA 구현 검증과 연결.

- 확정된 Edge→Service80→Pod8000·externalTrafficPolicy Local과 Worker 분산을 APP/LB/HA 인수에 연결한다. #22의 실제 허용 오류/관찰 구간은 별도 시험 전 확정 사항이다.

**인계·관련 티켓:** [#9](https://github.com/321Team/fds-project-baseline/issues/9) · [#15](https://github.com/321Team/fds-project-baseline/issues/15) · [#22](https://github.com/321Team/fds-project-baseline/issues/22).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:DEC-P1-ENTRY-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:DEC-P1-ENTRY-01 -->
# DEC-P1-ENTRY-01 — Edge Service Exposure Decision

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | DEC-P1-ENTRY-01 |
| Phase | Phase 1 |
| Category | Architecture / Network |
| Type | Decision |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-27 |
| End | 2026-08-31 |
| Calendar Days | 5 |
| Working Days | 3 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | edge01→transaction-api 노출 방식을 Ingress/Reverse Proxy/NodePort 후보 중 확정하고 Port·Health Check·Firewall·NetworkPolicy 변경을 승인 |
| Related Decision IDs | D05; D18; D27 |
| Related Risk IDs | RISK-02; RISK-07 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #62 snapshot 2026-09-09T12:16:14Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | D18 PASS(2026-08-31). P1-APP-01 External Exposure와 P1-SEC-01 Allowlist/NetworkPolicy에 승인 결정을 전달한다. P1-LB-01 API LB와 P1-K8S-01 Cluster Bootstrap에는 Non-blocking이다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **Done / closed**. 원본 갱신 시각: `2026-09-09T12:16:14Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

기준 시점의 Done 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #62](https://github.com/321Team/fds-project-baseline/issues/62), Issue 갱신 시각 `2026-09-09T12:16:14Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- 이 티켓은 종결 이력이다. 과거 구성 설명은 해당 종결 범위를 설명하며 현재 배포 명령으로 사용하지 않는다. 후속 설계 변경은 Baseline의 현행 절과 책임 티켓을 따른다.

---

# User Story

인프라 설계자로서 `edge01`에서 Kubernetes `transaction-api`까지의 실제 노출 방식을 확정한다. 이를 통해 Interface Freeze의 논리 포트를 실행 가능한 구성과 테스트로 연결한다.

---

# 최종 결정안

P1 애플리케이션 외부 진입 방식으로 **Reverse Proxy(HAProxy) + 접근 제한 NodePort**를 채택한다.

```text
Client
  → edge01 10.1.93.50:80/443
  → HAProxy
  → Worker 10.1.93.105/107/108:30080
  → transaction-api Service port 80
  → transaction-api Pod targetPort 8000
```

NodePort는 외부 공개 방식이 아니라 `edge01`에서 Kubernetes Service로 전달하기 위한 내부 연결 수단으로만 사용한다. 일반 Client에서 Worker NodePort로 직접 접근하는 구성은 허용하지 않는다.

NodePort Service에는 `externalTrafficPolicy: Local`을 적용해 HAProxy Backend 연결의 출발지인 `edge01 10.1.93.50`을 Pod까지 보존한다. 실제 외부 Client 주소는 HAProxy가 생성한 신뢰 가능한 `X-Forwarded-For`로 전달한다.

본 결정은 Application Exposure에 한정한다. Kubernetes API Load Balancer `.109:6443` 및 Cluster Bootstrap은 D27에 따라 `P1-LB-01`/`P1-K8S-01` 범위이며 본 티켓의 직접 선행조건 또는 차단 대상이 아니다.

---

# Scope

## In Scope

- 노출 패턴 비교 및 단일 구현안 확정
- Service Port, targetPort 및 Health Check 경로
- `externalTrafficPolicy`와 Source IP 보존 기준
- Firewall·NetworkPolicy 영향
- HAProxy 및 Kubernetes Service Rollback 방식
- P2 전환 시 공통 구성과 P1 전용 Exposure Adapter 분리 기준
- 관련 후속 티켓의 구현·검증 책임 경계

## Out of Scope

- Kubernetes API LB와 Cluster Bootstrap 구현
- HAProxy, Service, Firewall 및 NetworkPolicy Manifest의 실제 적용
- TLS 인증서 발급과 Secret 값 결정
- Istio/Service Mesh 및 Kata Containers 도입
- PostgreSQL Containerization
- P2 ROSA/OpenShift Route의 실제 구축
- 명시되지 않은 P1/P2 기능과 Scope Out 기능

---

# Decision 비교표

| 후보 | 장점 | 제약 및 판단 | 결과 |
|---|---|---|---|
| Reverse Proxy + 제한 NodePort | 기존 `edge01` 재사용, TLS·로그·Health Check 중앙화, 방화벽 통제 용이 | HAProxy와 Worker Allowlist 관리 필요 | **채택** |
| 직접 NodePort | 추가 Controller 불필요 | Worker 직접 노출, TLS·접근 로그·접근통제 분산 | 제외 |
| Ingress Controller | Kubernetes 리소스와 연계 가능 | 별도 Controller 운영 및 유지보수 범위 증가 | P1 제외 |
| Gateway API | 향후 확장성과 표준화 가능성 | P1에서 CRD·Controller 및 운영 범위 추가 | P2 재검토 |
| MetalLB/별도 LB | Service `LoadBalancer` 패턴 사용 가능 | 현재 L2·장비·운영자원 대비 추가 구성 실익 부족 | 제외 |

Gateway API는 영구 제외하지 않는다. P2 진입 시 실제 ROSA/OpenShift 지원 상태와 운영 요구사항을 기준으로 `P2-ARC-01`에서 재평가한다. P2의 초기 안정화 기준은 OpenShift Route로 한다.

---

# 핵심 요구사항

- [x] External Entry `.50:80/443`을 유지한다.
- [x] `transaction-api` targetPort `8000`을 유지한다.
- [x] Worker NodePort는 `30080`으로 고정한다.
- [x] Service Port `80`에서 Pod targetPort `8000`으로 전달한다.
- [x] NodePort Service에 `externalTrafficPolicy: Local`을 적용한다.
- [x] Worker NodePort는 `edge01 10.1.93.50/32`에서만 접근을 허용한다.
- [x] 일반 Client에서 Worker NodePort로 직접 접근하는 경로를 차단한다.
- [x] DB 또는 `fds-engine`을 외부에 직접 노출하지 않는다.
- [x] 상태 변경 Transaction POST에 HAProxy 자동 재시도를 적용하지 않는다.
- [x] P1과 P2의 외부 노출 구성을 Adapter 형태로 분리한다.

---

# Interface 및 구성 기준

| Source | Destination | Protocol/Port | 목적 | 통제 기준 |
|---|---|---:|---|---|
| Client | `edge01 10.1.93.50` | TCP 80/443 | 외부 서비스 진입 | D19 적용 후 80→443 Redirect |
| `edge01 10.1.93.50` | Worker `.105/.107/.108` | TCP 30080 | HAProxy에서 NodePort 진입 | Worker Firewall `.50/32` Allowlist |
| NodePort Service | `transaction-api` Pod | TCP 8000 | 애플리케이션 요청 전달 | Service Selector 및 NetworkPolicy |
| `transaction-api` | `fds-engine` | TCP 8001 | FDS 판정 요청 | 단방향 명시 허용 |
| `transaction-api` | PostgreSQL `.55` | TCP 5432 | 거래 저장 | `transaction-api`만 명시 허용 |
| `fds-engine` | DB/외부 | 허용 없음 | 직접 접근 금지 | Egress 차단 |
| Pod | CoreDNS | TCP/UDP 53 | 이름 해석 | DNS만 명시 허용 |

## HAProxy 기준

- Frontend: `edge01:80/443`
- Backend: Worker `.105/.107/.108:30080`
- Backend Health Check: Worker별 `:30080/readyz`
- TLS 종료: `edge01`
- 실제 Client 주소: 신뢰 가능한 `X-Forwarded-For`로 전달
- Kubernetes 구간 Source IP: `externalTrafficPolicy: Local`로 `edge01 10.1.93.50` 보존
- Client가 임의로 전달한 Proxy Header는 신뢰하지 않음
- 상태 변경 POST에 Proxy 자동 재시도를 적용하지 않음
- 반영 전 HAProxy 문법 검증 수행
- 로컬 Ready Endpoint가 없는 Worker는 Backend 대상에서 제외

## Kubernetes 기준

- NodePort: `30080`
- Service Port: `80`
- Pod targetPort: `8000`
- `externalTrafficPolicy: Local`
- `transaction-api` Replica 2개 이상
- 최소 2개 Worker에 분산 배치
- `topologySpreadConstraints` 또는 Pod Anti-Affinity 적용
- Readiness Probe: `/readyz`
- Liveness Probe: `/livez`
- 필요 시 `startupProbe` 적용
- DB 장애를 Liveness 실패에 직접 연결하지 않음

`externalTrafficPolicy: Local`에서는 로컬 Ready Endpoint가 없는 Worker로 유입된 트래픽이 다른 Worker로 전달되지 않을 수 있다. HAProxy는 Worker별 `/readyz`를 점검하고 정상 Worker에만 신규 요청을 전달한다.

---

# 구성 위치 및 책임

| 구성 항목 | 책임 티켓 |
|---|---|
| HAProxy External Exposure 및 Health Check 연계 | `P1-APP-01` |
| `/livez`, `/readyz` 및 애플리케이션 장애 처리 | `P1-APP-01` |
| Worker TCP 30080 Allowlist | `P1-SEC-01` |
| NetworkPolicy 및 Source IP Runtime Test | `P1-SEC-01` |
| Worker Firewall 적용 가능 여부와 데이터패스 Preflight | `P1-K8S-01` |
| TLS 인증서 및 HTTPS 적용 | `D19` 및 관련 TLS 구현 티켓 |
| Harbor 이미지 인증 및 Pull Secret | `P1-HBR-01` |

Worker Firewall 변경이 기존 `D-NET-01` 기준선을 초과하거나 충돌하면 별도 Change Request로 관리한다.

---

# D-SEC-01 연계 기준

- `fds-app` PSA Restricted
- Namespace Default Deny
- Edge → `transaction-api` 경로만 명시 허용
- `ipBlock: 10.1.93.50/32` 적용
- `transaction-api → fds-engine:8001` 단방향 허용
- `transaction-api → PostgreSQL:5432` 허용
- `fds-engine`의 DB 및 외부 직접 접근 차단
- Kubernetes API를 사용하지 않는 Pod의 ServiceAccount Token 자동 마운트 차단
- `runAsNonRoot: true`
- `privileged: false`
- `allowPrivilegeEscalation: false`
- `seccompProfile: RuntimeDefault`
- Linux Capability `ALL` 제거
- Secret 값의 코드·Manifest·로그·Evidence 노출 금지

`D-SEC-01`에는 Mandatory Control, 허용 통신 원칙, System Exception 및 Security Test 기준을 유지한다.

SecurityContext, RBAC, NetworkPolicy 및 Firewall Allowlist의 작성·적용·Runtime Test는 `P1-SEC-01`에서 수행한다. Kubernetes Service NAT와 NetworkPolicy 적용 결과는 실제 CNI 및 kube-proxy 환경에서 검증한다.

---

# Rollback 방식

1. HAProxy 변경 전 현재 승인 설정을 버전 관리하고 백업한다.
2. 변경 설정의 문법과 Backend Health를 검증한 후 Reload한다.
3. 외부 진입 실패, 비정상 라우팅 또는 보안 정책 충돌 시 직전 HAProxy 설정으로 복원한다.
4. Kubernetes Service 변경이 원인인 경우 직전 승인 Service Manifest로 복원한다.
5. `externalTrafficPolicy: Local` 적용 후 가용성 문제가 발생하면 Replica 배치와 HAProxy Backend Health 상태를 우선 점검한다.
6. Rollback 중에도 Worker NodePort를 일반 Client에 직접 개방하지 않는다.
7. 복구 결과와 접근통제 재검증 결과를 Evidence에 남긴다.

---

# P2 이식성

Portable Core + Platform-specific Exposure Adapter 구조를 적용한다.

| 구분 | P1 | P2 ROSA |
|---|---|---|
| 애플리케이션 이미지 | 공통 | 공통 |
| Deployment 기본 구조 | 공통 | 공통 |
| 내부 Service | ClusterIP, port 80 → targetPort 8000 | 동일 |
| Health Contract | `/livez`, `/readyz` | 동일 |
| SecurityContext | 공통 | 공통 |
| ConfigMap/Secret 계약 | 공통 | 공통 |
| Exposure Adapter | HAProxy + NodePort 30080 | OpenShift Route + ClusterIP Service |
| P1 전용 구성 | 사용 | HAProxy·NodePort·Worker Allowlist 제거 |

P2 전환 시 애플리케이션 이미지와 내부 Service 계약은 유지하고 외부 진입 Adapter만 교체한다.

---

# 적용 수준

본 구성은 현재 보유 자원 내에서 금융권 주요 보안 통제를 재현하는 교육·개발·PoC 환경에 적용한다.

> 금융권 주요 보안통제를 제한된 자원에서 재현한 Mini FDS 교육·PoC 플랫폼

다음 제약으로 인해 실제 금융 Production 또는 규제 준수 완료 환경으로 주장하지 않는다.

- 전체 서버가 동일한 물리 L2 네트워크 사용
- `edge01`, DB, Harbor 및 Monitoring의 단일 장애점 존재
- Windows PC와 VMware Workstation 기반으로 서버급 HA 미제공
- 전용 NGFW, WAF, IDS/IPS, PAM, HSM/KMS 미구성
- 불변 감사 로그 저장소와 정식 SIEM 미구성
- DB HA 및 다중 사이트 DR 미구성
- 실제 금융 고객정보 및 운영 거래 데이터 사용 불가
- 금융보안 규제 준수 또는 취약점 분석·평가 완료를 주장할 수 없음

위 제약은 Risk Register에 기록하며 P1에서는 합성 데이터만 사용한다.

---

# Acceptance Criteria

- [x] 단일 구현안과 대체안이 기록된다.
- [x] Reverse Proxy + 제한 NodePort 방식에 대한 팀 합의가 완료된다.
- [x] `externalTrafficPolicy: Local` 적용이 결정값으로 확정된다.
- [x] Port와 Health Check 기준이 기록된다.
- [x] Firewall·NetworkPolicy 변경 범위와 Rollback 방식이 정의된다.
- [x] P1-APP/P1-SEC의 선행조건과 P1-LB/P1-K8S의 Non-blocking 관계가 반영된다.
- [x] P2 ROSA 전환 시 Exposure Adapter 교체 원칙이 정의된다.
- [x] 관련 Risk ID와 통제 기준이 연결된다.
- [x] 선택안, 책임 경계 및 Approver 승인 결과가 기록된다.

Runtime Manifest 적용 및 통합 테스트 완료 여부는 `P1-APP-01`, `P1-SEC-01`, `P1-HBR-01`에서 별도로 판정한다.

---

# 검증 및 증적

## 후속 Runtime Test

- `edge01 10.1.93.50 → Worker:30080 → transaction-api` 통신 성공
- 허가되지 않은 Client → Worker:30080 통신 차단
- Pod에서 관측되는 L3 Source IP가 `10.1.93.50`인지 확인
- 실제 Client 주소가 신뢰 가능한 `X-Forwarded-For`로 전달되는지 확인
- `ipBlock: 10.1.93.50/32` 정상 경로 및 비허용 Source 차단 확인
- Worker별 `/readyz` Health Check 및 비정상 Worker Backend 제외
- `/livez` 실패 시 재시작 동작 확인
- DB 장애가 Liveness 실패와 직접 연결되지 않는지 확인
- HAProxy 및 Service Rollback 후 접근통제 재검증

## Decision Evidence

- Decision 비교표
- 팀 합의 및 승인 기록
- Architecture/Interface 연계 정보
- 영향 티켓 링크
- 관련 Risk Register 연결
- Evidence Path: `321Team/fds-project-evidence:evidence/DEC-P1-ENTRY-01/`

Evidence에는 Secret, Token, 인증서 개인키, 고객정보 또는 거래 민감정보를 포함하지 않는다.

---

# Dependency

- **Blocked By:** `D-ARC-01`, `D-NET-01` — DONE
- **Blocks / Next:** `P1-APP-01` External Exposure; `P1-SEC-01` Allowlist / NetworkPolicy
- **Related Ticket:** `P1-LB-01`, `P1-K8S-01` — Non-blocking / Interface Reference only
- **Related Security:** `D-SEC-01`, `P1-HBR-01`
- **Related P2:** `P2-ARC-01`
- **Milestone:** G2 Security / Feature Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D05; D18; D27
- **Decision Control:** D18에서 Reverse Proxy + 제한 NodePort, `externalTrafficPolicy: Local`, 선택 사유 및 Rollback 방식을 승인한다. D27에 따라 Application Exposure와 API LB/Cluster Bootstrap 간 직접 차단 관계를 두지 않는다.
- **Related Risk IDs:** RISK-02; RISK-07
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance Criteria와 Evidence에 연결한다.
- **Accepted Limitation:** 단일 `edge01`, 동일 물리 L2 및 제한된 HA 구성은 교육·개발·PoC 범위의 수용 위험으로 관리한다.

---

# Completion Record

- **Result:** **PASS** — Reverse Proxy(HAProxy) + 접근 제한 NodePort 방식 및 `externalTrafficPolicy: Local` 적용 승인
- **Status:** Done
- **Exit Criteria:** edge01→transaction-api 노출 방식, Port·Health Check·Firewall·NetworkPolicy 변경 및 Rollback 기준 승인 완료
- **Approval Result:** PASS
- **Approval Date:** 2026-08-31
- **Completed Date:** 2026-08-31
- **Reviewer / Approver:** 이하영 / 이권욱
- **Evidence Path:** `321Team/fds-project-evidence:evidence/DEC-P1-ENTRY-01/`

본 Decision의 `Done`은 아키텍처 및 Interface 결정의 승인 완료를 의미한다. 실제 Manifest 적용과 Runtime Security Test 완료 여부는 후속 구현 티켓에서 별도로 판정한다.

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `2dd6943eda081044ff0e7965469fc050d22ae7e51f51a3b538af05be11884780`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:DEC-P1-ENTRY-01 -->
# DEC-P1-ENTRY-01 — Edge Service Exposure Decision

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | DEC-P1-ENTRY-01 |
| Phase | Phase 1 |
| Category | Architecture / Network |
| Type | Decision |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-27 |
| End | 2026-08-31 |
| Calendar Days | 5 |
| Working Days | 3 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | edge01→transaction-api 노출 방식을 Ingress/Reverse Proxy/NodePort 후보 중 확정하고 Port·Health Check·Firewall·NetworkPolicy 변경을 승인 |
| Related Decision IDs | D05; D18; D27 |
| Related Risk IDs | RISK-02; RISK-07 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Network_Baseline_v2.3; FDS_Phase1_Logical_Architecture_v3.1.2; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | D18 PASS(2026-08-31). P1-APP-01 External Exposure와 P1-SEC-01 Allowlist/NetworkPolicy에 승인 결정을 전달한다. P1-LB-01 API LB와 P1-K8S-01 Cluster Bootstrap에는 Non-blocking이다. |

## 이관 기준 및 확인 사항


- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) · [정본 WBS](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/wbs/FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx).
- 본문은 아래에 적힌 원본 버전의 기록이다. 위 속성·후속 승인과 다른 과거 상태는 현재 판정으로 사용하지 않는다. 이관 자체로 미실행 AC를 체크하거나 새 승인을 부여하지 않는다.
- Lead/Support의 풀네임은 본문 속성으로 보존한다. GitHub 계정 대응이 확인되지 않은 사람에게 자동 배정하지 않았다.

## 원본 및 변경 출처

- `FDS_Notion_Remaining_Backlog_Manual_v1.9.md`

---

## Description — 보관 입력본

> 원본: `FDS_Notion_Remaining_Backlog_Manual_v1.9.md`. 원본의 완료/미완료 체크와 당시 이력을 보존했다.

# 🎯 User Story

인프라 설계자로서 `edge01`에서 Kubernetes `transaction-api`까지의 실제 노출 방식을 확정한다. 이를 통해 Interface Freeze의 논리 포트를 실행 가능한 구성과 테스트로 연결한다.

---

# 📍 최종 결정안

P1 애플리케이션 외부 진입 방식으로 **Reverse Proxy(HAProxy) + 접근 제한 NodePort**를 채택한다.

```text
Client
  → edge01 10.1.93.50:80/443
  → HAProxy
  → Worker 10.1.93.105/107/108:30080
  → transaction-api Service port 80
  → transaction-api Pod targetPort 8000
```

NodePort는 외부 공개 방식이 아니라 `edge01`에서 Kubernetes Service로 전달하기 위한 내부 연결 수단으로만 사용한다. 일반 Client에서 Worker NodePort로 직접 접근하는 구성은 허용하지 않는다.

NodePort Service에는 `externalTrafficPolicy: Local`을 적용해 HAProxy Backend 연결의 출발지인 `edge01 10.1.93.50`을 Pod까지 보존한다. 실제 외부 Client 주소는 HAProxy가 생성한 신뢰 가능한 `X-Forwarded-For`로 전달한다.

본 결정은 Application Exposure에 한정한다. Kubernetes API Load Balancer `.109:6443` 및 Cluster Bootstrap은 D27에 따라 `P1-LB-01`/`P1-K8S-01` 범위이며 본 티켓의 직접 선행조건 또는 차단 대상이 아니다.

---

# 📌 Scope

## In Scope

- 노출 패턴 비교 및 단일 구현안 확정
- Service Port, targetPort 및 Health Check 경로
- `externalTrafficPolicy`와 Source IP 보존 기준
- Firewall·NetworkPolicy 영향
- HAProxy 및 Kubernetes Service Rollback 방식
- P2 전환 시 공통 구성과 P1 전용 Exposure Adapter 분리 기준
- 관련 후속 티켓의 구현·검증 책임 경계

## Out of Scope

- Kubernetes API LB와 Cluster Bootstrap 구현
- HAProxy, Service, Firewall 및 NetworkPolicy Manifest의 실제 적용
- TLS 인증서 발급과 Secret 값 결정
- Istio/Service Mesh 및 Kata Containers 도입
- PostgreSQL Containerization
- P2 ROSA/OpenShift Route의 실제 구축
- 명시되지 않은 P1/P2 기능과 Scope Out 기능

---

# 🔎 Decision 비교표

| 후보 | 장점 | 제약 및 판단 | 결과 |
|---|---|---|---|
| Reverse Proxy + 제한 NodePort | 기존 `edge01` 재사용, TLS·로그·Health Check 중앙화, 방화벽 통제 용이 | HAProxy와 Worker Allowlist 관리 필요 | **채택** |
| 직접 NodePort | 추가 Controller 불필요 | Worker 직접 노출, TLS·접근 로그·접근통제 분산 | 제외 |
| Ingress Controller | Kubernetes 리소스와 연계 가능 | 별도 Controller 운영 및 유지보수 범위 증가 | P1 제외 |
| Gateway API | 향후 확장성과 표준화 가능성 | P1에서 CRD·Controller 및 운영 범위 추가 | P2 재검토 |
| MetalLB/별도 LB | Service `LoadBalancer` 패턴 사용 가능 | 현재 L2·장비·운영자원 대비 추가 구성 실익 부족 | 제외 |

Gateway API는 영구 제외하지 않는다. P2 진입 시 실제 ROSA/OpenShift 지원 상태와 운영 요구사항을 기준으로 `P2-ARC-01`에서 재평가한다. P2의 초기 안정화 기준은 OpenShift Route로 한다.

---

# 📋 핵심 요구사항

- [x] External Entry `.50:80/443`을 유지한다.
- [x] `transaction-api` targetPort `8000`을 유지한다.
- [x] Worker NodePort는 `30080`으로 고정한다.
- [x] Service Port `80`에서 Pod targetPort `8000`으로 전달한다.
- [x] NodePort Service에 `externalTrafficPolicy: Local`을 적용한다.
- [x] Worker NodePort는 `edge01 10.1.93.50/32`에서만 접근을 허용한다.
- [x] 일반 Client에서 Worker NodePort로 직접 접근하는 경로를 차단한다.
- [x] DB 또는 `fds-engine`을 외부에 직접 노출하지 않는다.
- [x] 상태 변경 Transaction POST에 HAProxy 자동 재시도를 적용하지 않는다.
- [x] P1과 P2의 외부 노출 구성을 Adapter 형태로 분리한다.

---

# 🔌 Interface 및 구성 기준

| Source | Destination | Protocol/Port | 목적 | 통제 기준 |
|---|---|---:|---|---|
| Client | `edge01 10.1.93.50` | TCP 80/443 | 외부 서비스 진입 | D19 적용 후 80→443 Redirect |
| `edge01 10.1.93.50` | Worker `.105/.107/.108` | TCP 30080 | HAProxy에서 NodePort 진입 | Worker Firewall `.50/32` Allowlist |
| NodePort Service | `transaction-api` Pod | TCP 8000 | 애플리케이션 요청 전달 | Service Selector 및 NetworkPolicy |
| `transaction-api` | `fds-engine` | TCP 8001 | FDS 판정 요청 | 단방향 명시 허용 |
| `transaction-api` | PostgreSQL `.55` | TCP 5432 | 거래 저장 | `transaction-api`만 명시 허용 |
| `fds-engine` | DB/외부 | 허용 없음 | 직접 접근 금지 | Egress 차단 |
| Pod | CoreDNS | TCP/UDP 53 | 이름 해석 | DNS만 명시 허용 |

## HAProxy 기준

- Frontend: `edge01:80/443`
- Backend: Worker `.105/.107/.108:30080`
- Backend Health Check: Worker별 `:30080/readyz`
- TLS 종료: `edge01`
- 실제 Client 주소: 신뢰 가능한 `X-Forwarded-For`로 전달
- Kubernetes 구간 Source IP: `externalTrafficPolicy: Local`로 `edge01 10.1.93.50` 보존
- Client가 임의로 전달한 Proxy Header는 신뢰하지 않음
- 상태 변경 POST에 Proxy 자동 재시도를 적용하지 않음
- 반영 전 HAProxy 문법 검증 수행
- 로컬 Ready Endpoint가 없는 Worker는 Backend 대상에서 제외

## Kubernetes 기준

- NodePort: `30080`
- Service Port: `80`
- Pod targetPort: `8000`
- `externalTrafficPolicy: Local`
- `transaction-api` Replica 2개 이상
- 최소 2개 Worker에 분산 배치
- `topologySpreadConstraints` 또는 Pod Anti-Affinity 적용
- Readiness Probe: `/readyz`
- Liveness Probe: `/livez`
- 필요 시 `startupProbe` 적용
- DB 장애를 Liveness 실패에 직접 연결하지 않음

`externalTrafficPolicy: Local`에서는 로컬 Ready Endpoint가 없는 Worker로 유입된 트래픽이 다른 Worker로 전달되지 않을 수 있다. HAProxy는 Worker별 `/readyz`를 점검하고 정상 Worker에만 신규 요청을 전달한다.

---

# 👤 구성 위치 및 책임

| 구성 항목 | 책임 티켓 |
|---|---|
| HAProxy External Exposure 및 Health Check 연계 | `P1-APP-01` |
| `/livez`, `/readyz` 및 애플리케이션 장애 처리 | `P1-APP-01` |
| Worker TCP 30080 Allowlist | `P1-SEC-01` |
| NetworkPolicy 및 Source IP Runtime Test | `P1-SEC-01` |
| Worker Firewall 적용 가능 여부와 데이터패스 Preflight | `P1-K8S-01` |
| TLS 인증서 및 HTTPS 적용 | `D19` 및 관련 TLS 구현 티켓 |
| Harbor 이미지 인증 및 Pull Secret | `P1-HBR-01` |

Worker Firewall 변경이 기존 `D-NET-01` 기준선을 초과하거나 충돌하면 별도 Change Request로 관리한다.

---

# 🔐 D-SEC-01 연계 기준

- `fds-app` PSA Restricted
- Namespace Default Deny
- Edge → `transaction-api` 경로만 명시 허용
- `ipBlock: 10.1.93.50/32` 적용
- `transaction-api → fds-engine:8001` 단방향 허용
- `transaction-api → PostgreSQL:5432` 허용
- `fds-engine`의 DB 및 외부 직접 접근 차단
- Kubernetes API를 사용하지 않는 Pod의 ServiceAccount Token 자동 마운트 차단
- `runAsNonRoot: true`
- `privileged: false`
- `allowPrivilegeEscalation: false`
- `seccompProfile: RuntimeDefault`
- Linux Capability `ALL` 제거
- Secret 값의 코드·Manifest·로그·Evidence 노출 금지

`D-SEC-01`에는 Mandatory Control, 허용 통신 원칙, System Exception 및 Security Test 기준을 유지한다.

SecurityContext, RBAC, NetworkPolicy 및 Firewall Allowlist의 작성·적용·Runtime Test는 `P1-SEC-01`에서 수행한다. Kubernetes Service NAT와 NetworkPolicy 적용 결과는 실제 CNI 및 kube-proxy 환경에서 검증한다.

---

# ♻️ Rollback 방식

1. HAProxy 변경 전 현재 승인 설정을 버전 관리하고 백업한다.
2. 변경 설정의 문법과 Backend Health를 검증한 후 Reload한다.
3. 외부 진입 실패, 비정상 라우팅 또는 보안 정책 충돌 시 직전 HAProxy 설정으로 복원한다.
4. Kubernetes Service 변경이 원인인 경우 직전 승인 Service Manifest로 복원한다.
5. `externalTrafficPolicy: Local` 적용 후 가용성 문제가 발생하면 Replica 배치와 HAProxy Backend Health 상태를 우선 점검한다.
6. Rollback 중에도 Worker NodePort를 일반 Client에 직접 개방하지 않는다.
7. 복구 결과와 접근통제 재검증 결과를 Evidence에 남긴다.

---

# 🚚 P2 이식성

Portable Core + Platform-specific Exposure Adapter 구조를 적용한다.

| 구분 | P1 | P2 ROSA |
|---|---|---|
| 애플리케이션 이미지 | 공통 | 공통 |
| Deployment 기본 구조 | 공통 | 공통 |
| 내부 Service | ClusterIP, port 80 → targetPort 8000 | 동일 |
| Health Contract | `/livez`, `/readyz` | 동일 |
| SecurityContext | 공통 | 공통 |
| ConfigMap/Secret 계약 | 공통 | 공통 |
| Exposure Adapter | HAProxy + NodePort 30080 | OpenShift Route + ClusterIP Service |
| P1 전용 구성 | 사용 | HAProxy·NodePort·Worker Allowlist 제거 |

P2 전환 시 애플리케이션 이미지와 내부 Service 계약은 유지하고 외부 진입 Adapter만 교체한다.

---

# 🏦 적용 수준

본 구성은 현재 보유 자원 내에서 금융권 주요 보안 통제를 재현하는 교육·개발·PoC 환경에 적용한다.

> 금융권 주요 보안통제를 제한된 자원에서 재현한 Mini FDS 교육·PoC 플랫폼

다음 제약으로 인해 실제 금융 Production 또는 규제 준수 완료 환경으로 주장하지 않는다.

- 전체 서버가 동일한 물리 L2 네트워크 사용
- `edge01`, DB, Harbor 및 Monitoring의 단일 장애점 존재
- Windows PC와 VMware Workstation 기반으로 서버급 HA 미제공
- 전용 NGFW, WAF, IDS/IPS, PAM, HSM/KMS 미구성
- 불변 감사 로그 저장소와 정식 SIEM 미구성
- DB HA 및 다중 사이트 DR 미구성
- 실제 금융 고객정보 및 운영 거래 데이터 사용 불가
- 금융보안 규제 준수 또는 취약점 분석·평가 완료를 주장할 수 없음

위 제약은 Risk Register에 기록하며 P1에서는 합성 데이터만 사용한다.

---

# ✅ Acceptance Criteria

- [x] 단일 구현안과 대체안이 기록된다.
- [x] Reverse Proxy + 제한 NodePort 방식에 대한 팀 합의가 완료된다.
- [x] `externalTrafficPolicy: Local` 적용이 결정값으로 확정된다.
- [x] Port와 Health Check 기준이 기록된다.
- [x] Firewall·NetworkPolicy 변경 범위와 Rollback 방식이 정의된다.
- [x] P1-APP/P1-SEC의 선행조건과 P1-LB/P1-K8S의 Non-blocking 관계가 반영된다.
- [x] P2 ROSA 전환 시 Exposure Adapter 교체 원칙이 정의된다.
- [x] 관련 Risk ID와 통제 기준이 연결된다.
- [x] 선택안, 책임 경계 및 Approver 승인 결과가 기록된다.

Runtime Manifest 적용 및 통합 테스트 완료 여부는 `P1-APP-01`, `P1-SEC-01`, `P1-HBR-01`에서 별도로 판정한다.

---

# 🧪 검증 및 증적

## 후속 Runtime Test

- `edge01 10.1.93.50 → Worker:30080 → transaction-api` 통신 성공
- 허가되지 않은 Client → Worker:30080 통신 차단
- Pod에서 관측되는 L3 Source IP가 `10.1.93.50`인지 확인
- 실제 Client 주소가 신뢰 가능한 `X-Forwarded-For`로 전달되는지 확인
- `ipBlock: 10.1.93.50/32` 정상 경로 및 비허용 Source 차단 확인
- Worker별 `/readyz` Health Check 및 비정상 Worker Backend 제외
- `/livez` 실패 시 재시작 동작 확인
- DB 장애가 Liveness 실패와 직접 연결되지 않는지 확인
- HAProxy 및 Service Rollback 후 접근통제 재검증

## Decision Evidence

- Decision 비교표
- 팀 합의 및 승인 기록
- Architecture/Interface 연계 정보
- 영향 티켓 링크
- 관련 Risk Register 연결
- Evidence Path: `docs/evidence/DEC-P1-ENTRY-01/`

Evidence에는 Secret, Token, 인증서 개인키, 고객정보 또는 거래 민감정보를 포함하지 않는다.

---

# 🔗 Dependency

- **Blocked By:** `D-ARC-01`, `D-NET-01` — DONE
- **Blocks / Next:** `P1-APP-01` External Exposure; `P1-SEC-01` Allowlist / NetworkPolicy
- **Related Ticket:** `P1-LB-01`, `P1-K8S-01` — Non-blocking / Interface Reference only
- **Related Security:** `D-SEC-01`, `P1-HBR-01`
- **Related P2:** `P2-ARC-01`
- **Milestone:** G2 Security / Feature Ready

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D05; D18; D27
- **Decision Control:** D18에서 Reverse Proxy + 제한 NodePort, `externalTrafficPolicy: Local`, 선택 사유 및 Rollback 방식을 승인한다. D27에 따라 Application Exposure와 API LB/Cluster Bootstrap 간 직접 차단 관계를 두지 않는다.
- **Related Risk IDs:** RISK-02; RISK-07
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance Criteria와 Evidence에 연결한다.
- **Accepted Limitation:** 단일 `edge01`, 동일 물리 L2 및 제한된 HA 구성은 교육·개발·PoC 범위의 수용 위험으로 관리한다.

---

# 📝 Completion Record

- **Result:** **PASS** — Reverse Proxy(HAProxy) + 접근 제한 NodePort 방식 및 `externalTrafficPolicy: Local` 적용 승인
- **Status:** Done
- **Exit Criteria:** edge01→transaction-api 노출 방식, Port·Health Check·Firewall·NetworkPolicy 변경 및 Rollback 기준 승인 완료
- **Approval Result:** PASS
- **Approval Date:** 2026-08-31
- **Completed Date:** 2026-08-31
- **Reviewer / Approver:** 이하영 / 이권욱
- **Evidence Path:** `docs/evidence/DEC-P1-ENTRY-01/`

본 Decision의 `Done`은 아키텍처 및 Interface 결정의 승인 완료를 의미한다. 실제 Manifest 적용과 Runtime Security Test 완료 여부는 후속 구현 티켓에서 별도로 판정한다.
````

</details>
