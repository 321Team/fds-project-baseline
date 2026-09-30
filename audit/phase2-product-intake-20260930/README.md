# Phase 2 선택 제품 유입 검토 — 2026-09-30 KST

## 1. 적용 기준

- 현행 정본: `docs-v3.1.20 / RELEASED`
- 차기 정본 후보: Draft PR #112 / `release/v3.1.21`
- 팀 규모: 3인
- 프로젝트 가치: 재현성 · 무결성 · 추적성
- 이번 회의 결정:
  - **추가 절차 간소화안은 적용하지 않는다.**
  - 현행 Governance/Review/Evidence 절차를 유지한다.
  - 절차 간소화는 후속 회의에서 다시 검토한다.
  - 기존에 이미 적용된 정책·자동화·주기 변경을 이번 결정으로 소급 취소하지 않는다.

## 2. 현재 추가 제품 유입 검토 범위

이번 시점의 활성 검토 대상은 아래 2개로 한정한다.

| Issue | 제품 | Priority | Gate 영향 | 기본값 |
|---:|---|---|---|---|
| #120 | OpenShift GitOps (Argo CD) | **P1** | G5/G6 non-blocking | 미결정이면 #46 Runner direct deploy 유지 |
| #121 | Compliance Operator | **P1** | G5/G6 non-blocking | 미결정이면 #38 현행 ROSA security AC 유지 |

RHOAI(#95)는 기존 P1/Deferred 우선 상태를 유지하며 이번 활성 유입 범위에는 포함하지 않는다.
ACS, Logging, Network Observability, cert-manager 등 나머지 제품은 별도 승인 전 검토 후보/Deferred 상태로 유지한다.

## 3. OpenShift GitOps / Argo CD

### 기존 반영 상태

- 팀 회고 및 Red Hat 제품 인벤토리에는 검토 후보로 존재.
- #46에는 "별도 승인 전 P0 요구로 확대하지 않는다"는 운영 delta가 존재.
- 그러나 제품 **도입 여부를 결정하는 독립 Decision ticket은 없었다.**

따라서 #120 `DEC-P2-GITOPS-01`을 신규 발행했다.

### P0/P1 판정

**P1 유지.**

사유:
1. v3.1.20 §1.4의 P0는 Runner 기반 ROSA Delivery이며 Argo CD 자체를 요구하지 않는다.
2. 도입하지 않아도 #46의 기존 Runner direct deploy로 G5/G6를 진행할 수 있다.
3. 도입 시 Delivery Contract와 권한 모델을 변경하므로 별도 CR이 필요하다.
4. Git 선언 기반 복원·Drift 관리·Runner cluster write 축소는 재현성/추적성 측면에서 실익이 있으나 3인 P0 일정 침해 시 Deferred 가능해야 한다.

### 도입 시 경계

- Runner: Build/Test/Scan/Registry Push
- Argo CD: Git desired state → ROSA Runtime Sync
- 필수 Chain:
  `Commit → Scan → Registry Digest → Git Revision → Argo CD Sync Revision → Runtime imageID → Evidence`
- Cluster-admin 또는 과도한 namespace-admin을 기본으로 사용하지 않는다.

공식 근거:
- ROSA의 Red Hat OpenShift GitOps는 Argo CD를 declarative GitOps engine으로 사용한다.
- https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/gitops/about-redhat-openshift-gitops
- https://docs.redhat.com/en/documentation/red_hat_openshift_gitops/1.19/html/argo_cd_instance/setting-up-argocd-instance

## 4. Compliance Operator

### 기존 반영 상태

- 팀 회고 및 Red Hat 제품 인벤토리에는 검토 후보로 존재.
- #38 ROSA Platform/Security 본문에는 독립 Adoption Decision이 없었다.
- 별도 Decision ticket이 없었다.

따라서 #121 `DEC-P2-COMP-01`을 신규 발행했다.

### P0/P1 판정

**P1 유지.**

사유:
1. Hybrid E2E·ROSA App Delivery의 필수 성공조건이 아니다.
2. 보안 설정 점검을 반복 가능한 결과로 만드는 실익은 있으나 모든 NonCompliant를 즉시 수정하는 것은 범위 폭증 위험이 있다.
3. HCP는 managed control plane 제약이 있어 Scan/Remediation 책임을 명확히 분리해야 한다.
4. 미도입/유예 상태에서도 #38 P0 Security Controls는 기존 AC로 진행 가능하다.

### ROSA HCP 특이사항

Red Hat 공식 문서는 Compliance Operator 1.5.0부터 ROSA Hosted Control Planes에 대해 테스트되었다고 명시하며, HCP에는 master node pool이 없으므로 기본 scheduling을 그대로 사용할 수 없어 Subscription 설정을 조정하도록 안내한다.

공식 근거:
- https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/compliance-operator

### 결과 처리 원칙

- Compliance Operator 결과를 규제 인증으로 표현하지 않는다.
- `Compliant / NonCompliant / Error / NotApplicable`을 구분한다.
- NonCompliant 발견은 Severity·적용가능성·P0 영향 검토 후:
  - Known Issue
  - 별도 P1 Task
  - P0 blocker(직접 P0 AC/보안통제 위반인 경우만)
  로 분류한다.
- 자동 remediation은 이번 Decision 범위가 아니다.

## 5. 기존 티켓 연계

- #34 P2-ARC-01: #120/#121을 P1 optional product decision으로 참조
- #38 P2-ROSA-01: #121 관련, P0 blocker 아님
- #41 DEC-P2-OP-01: 두 제품이 Go일 때만 D26 Operator 공급 대상
- #46 P2-CICD-01: #120 관련, Go 전까지 Runner direct deploy 유지
- #49 P2-DOC-01: 최종 산출물에 Adopt/Deferred/No-Go 상태 기록
- #53 MS-G6-01: 두 제품 미구현은 Gate blocker 아님

## 6. 정본 반영 상태

**실제 반영 완료**
- #120 / #121 신규 Decision ticket 발행
- #34/#38/#41/#46/#49 운영 delta 연결
- Draft PR #112 정본 후보 입력 갱신
- 회의록 후보에 "추가 절차 간소화 미적용 / 현행 유지 / 후속 재검토" 반영

**아직 미실행**
- #120/#121 Decision 승인
- OpenShift GitOps 설치
- Compliance Operator 설치/Scan
- 해당 구현 CR/Task
- WBS/Ticket Pack/Baseline 전체 재생성
- Review/Merge/Publication
