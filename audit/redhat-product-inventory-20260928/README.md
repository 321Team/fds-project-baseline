# Red Hat 제품 사용 현황 — 2026-09-28 KST

사용자 요청: "우리 프로젝트에서 구현된 내용 중에 레드햇 제품 나열해줘 ROSA 기반". 읽기 전용 조회 결과다. 제품 도입·범위·Status·AC는 판정하지 않는다.

**결론:** 2026-09-28 기준으로 ROSA 위에 구현된 Red Hat 제품은 없다. ROSA는 Phase 2 범위이고, Phase 2 티켓(#33~#57, #95)은 모두 `To Do`로 10-06에 착수한다. Phase 1에 구현한 것은 On-Prem kubeadm Kubernetes(3CP+3Worker)이며 OpenShift가 아니다.

## 1. 실제 구현됨 (Phase 1, On-Prem, ROSA 아님)

| 제품 | 사용 | 비고 |
| --- | --- | --- |
| Ansible | OS·노드 Bootstrap 자동화 (P1-ANS-01 Done) | 커뮤니티 Ansible인지 Ansible Automation Platform인지는 확인하지 않음 |
| CentOS Stream 10 | 전체 VM OS (D01 Fixed) | Red Hat이 후원하는 RHEL 업스트림. Red Hat 지원 제품은 아님 |
| Cockpit | 노드 기본 포함 | 6대 모두 unit mask 처리해 사용하지 않음 |

## 2. ROSA 기반 정본 계획 (Phase 2, 미착수)

| 제품·기능 | 용도 | 티켓 |
| --- | --- | --- |
| ROSA (Red Hat OpenShift Service on AWS) | transaction-api·fds-engine 배포 플랫폼 | #38 · #43 |
| OpenShift Route·SecurityContext | 서비스 노출, 보안 통제 | #38 · #43 |
| OADP (OpenShift API for Data Protection) | ROSA → S3 백업·복구 | #44 |
| Operator 카탈로그 (Direct Catalog) 또는 oc-mirror | Operator 공급망. D26 결정에 따름 | #41 · #51 |

정본에는 "ROSA"로만 적혀 있다. HCP(Hosted Control Plane) 방식은 9/23 비용 검토에서 가정한 값이다.

## 3. 추가 제품 제안 (9/23 #34 코멘트, 미확정)

| 구분 | 제품 |
| --- | --- |
| 도입 권장 | OpenShift GitOps, Compliance Operator |
| 결정 대기 | RHOAI (#95, 연장 기간 PoC 제안) |
| 조건부 | Advanced Cluster Security (ACS) Cloud Service |
| 선택 | OpenShift Logging(CloudWatch 연계), Network Observability, cert-manager Operator |
| 보류 | Trusted Artifact Signer, Quay, Advanced Cluster Management |
| 제외 | OpenShift Pipelines(§5 Fixed와 충돌), Service Mesh(§1.3 Scope Out), Streams for Apache Kafka(DEC-P1-TXN-01과 충돌) |

## 2026-09-30 유입 범위 갱신

사용자 회의 결과에 따라 추가 제품의 **활성 유입 검토 대상**을 다음 두 건으로 한정한다.

| 제품 | Decision | Priority | Gate 영향 | 상태 |
|---|---|---|---|---|
| OpenShift GitOps (Argo CD) | #120 DEC-P2-GITOPS-01 | P1 | G5/G6 non-blocking | 도입/유예/미도입 결정 대기 |
| Compliance Operator | #121 DEC-P2-COMP-01 | P1 | G5/G6 non-blocking | 도입/유예/미도입 결정 대기 |

- OpenShift GitOps가 미결정이면 #46의 Runner direct ROSA Delivery를 유지한다.
- Compliance Operator가 미결정이면 #38의 기존 ROSA Platform/Security P0 AC를 유지한다.
- RHOAI(#95)는 P1/Deferred 우선이며 이번 활성 유입 검토에 포함하지 않는다.
- ACS, Logging, Network Observability, cert-manager 등은 별도 승인 전 검토 후보/Deferred로 유지한다.
- 추가 절차 간소화안은 이번에 적용하지 않고 현행 Governance/Review/Evidence 절차를 유지한다.

## 표기 기준

발표 자료 등에 "ROSA 기반 Red Hat 제품"을 쓸 때는 1번만 "구현", 2번은 "계획", 3번은 "검토 중"으로 표기한다.

## 근거

- 정본 Baseline v3.1.16 §5 OS/Platform Baseline, §13 Phase 2 OCI/AWS/ROSA, §14 Decision Register (D01·D22·D26)
- GitHub Issue 상태 조회 (2026-09-28): Phase 2 티켓 전부 OPEN / `To Do`
- [#34 코멘트 (2026-09-23)](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-5798738776): 추가 제품 범위 제안
- [#95 코멘트 (2026-09-28)](https://github.com/321Team/fds-project-baseline/issues/95#issuecomment-5863864717): ROSA·RHOAI 비용 재계산

AI 사용: Claude Code가 조회·작성했다.
