# FDS 사양·기록 점검의 티켓 반영 결과

검증 완료: 2026-09-15 00:21:00 KST. 원 점검은 2026-09-14 기준이며, 실제 반영 시각은 아래와 같다.

**78/78개 티켓 본문 갱신 및 재조회 확인 완료.** 상태는 Open58 / Closed20으로 유지됐다.

- 반영 구간: 2026-09-15 00:13:33 KST ~ 2026-09-15 00:18:36 KST.
- 저장소: fds-project-baseline67 / fds-project-evidence2 / infra-ansible6 / infra-db2 / infra-kubernetes1.
- 새 본문과 계획 일치 78/78; 기존 본문 원문 보존 78/78; 보호 필드 일치 78/78; 댓글 수 동일 78/78.
- 요청 필드는 body만 사용했다. 제목·Record ID·migration marker·AC/체크·Lead/Support·계획·상태·라벨·Assignee·Type·Milestone·잠금 상태를 보존했다. 원문이 그대로 포함됨을 확인했으며 실제 사람 승인·Runtime·완료 상태를 새로 부여하지 않았다.
- 공식 PR 리뷰·다른 사람의 댓글·소스 코드·서버·Notion·CURRENT·v19 정본 파일/배포 묶음은 수정하지 않았다.

## 반영 내용

[P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에 A01~A07/R01~R06의 공통 점검 항목과 담당 티켓·근거를 연결하고, 각 티켓 본문 상단에 해당 결과와 후속 기록을 추가했다. 이 ID는 점검표 참조이며 신규 Ticket/Decision ID가 아니다.

| 구분 | 반영 |
|---|---|
| 사양·인수 입력 | NTP·CNI/MTU·CP1/CP2 경계, HA 합격 기준, 앱/Rule/시간계약, 정본 Monitoring 입력, OID/IF06B, 프록시 계정/As-built |
| 현재 기록 정정 | 0002 병합 완료와 운영 적용 미검증 분리, Ansible #6/#7 Closed·#8 실제시험/COMMENTED·증적범위, 현재 Harbor 정책/CA 실측 |
| 종료 이력 | 기존 종료 범위 유지, FUP의 당시 승인자/시각·원본 참조와 신규 변경 티켓 연결 |
| 계획·후속 | Review의 실제 일정 확정, P1 유예/P2 조건부 실행·N/A 근거, CURRENT/PR#73·native 속성/보조 ID의 후속 연결 |

## 티켓 기록 갱신 후 남는 업무

- 미확정 NTP/MTU·HA 기준·앱 계약/운영 값은 각 Lead의 근거·실측·인수 절차로 확정한다. 이번 기록 자체가 새 기술 사양 승인은 아니다.
- Squid rollback 수정·운영 계정/module/become·CNI trial·정본 Runtime·PR 독립 승인/병합은 각 구현 티켓에 남는다.
- CURRENT와 README의 발행 준비 문구, PR#73 실제 파일 편입·v19 전체 정본 묶음은 P1-DOC 후속이다.
- #78의 native Type·Milestone 미설정은 전체 Issue API에서 확인했고 후속으로 기록했다. 이번 body-only 갱신으로 속성 완료라고 보고하지 않는다.
- 증적 PR#12의 잘못된 링크는 관련 티켓에서 정확한 대상을 연결했다. 원 작성자의 댓글은 편집하지 않았다.

## 78개 적용 목록

| 티켓 | 상태 | 담당 | 본문/원문/보호필드 재조회 |
|---|---|---|---|
| [fds-project-baseline #4](https://github.com/321Team/fds-project-baseline/issues/4) [DEC-P1-FDS-01] 거래 보류 도입 범위·판정·평가 실패·Gate 편입 결정 | Closed | 이재환 | 일치 |
| [fds-project-baseline #5](https://github.com/321Team/fds-project-baseline/issues/5) [DEC-P1-TXN-01] 거래 상태·API 응답·재시도·데이터 정합성 계약 결정 | Closed | 이재환 | 일치 |
| [fds-project-baseline #6](https://github.com/321Team/fds-project-baseline/issues/6) [DEC-P1-ADMIN-01] 보안 시연 범위·테스트 전제·조건부 운영 통제 결정 | Closed | 이하영 | 일치 |
| [fds-project-baseline #7](https://github.com/321Team/fds-project-baseline/issues/7) [D-SEC-01] Security Design Scope / Approval Review | Closed | 이하영 | 일치 |
| [fds-project-baseline #8](https://github.com/321Team/fds-project-baseline/issues/8) [MS-G0-01] G0 Design Freeze | Closed | 이권욱 | 일치 |
| [fds-project-baseline #9](https://github.com/321Team/fds-project-baseline/issues/9) [P1-LB-01] Kubernetes API Load Balancer | Open | 이권욱 | 일치 |
| [fds-project-baseline #10](https://github.com/321Team/fds-project-baseline/issues/10) [P1-K8S-01] kubeadm 3CP + 3Worker / Calico | Open | 이하영 | 일치 |
| [fds-project-baseline #11](https://github.com/321Team/fds-project-baseline/issues/11) [P1-DB-01] PostgreSQL External VM | Open | 이재환 | 일치 |
| [fds-project-baseline #12](https://github.com/321Team/fds-project-baseline/issues/12) [P1-DNS-01] Internal DNS Primary/Secondary | Closed | 이권욱 | 일치 |
| [fds-project-baseline #13](https://github.com/321Team/fds-project-baseline/issues/13) [P1-HBR-01] Harbor / Trivy Registry | Open | 이하영 | 일치 |
| [fds-project-baseline #14](https://github.com/321Team/fds-project-baseline/issues/14) [ICR-D-NET-01-01] Kubernetes Node Host Firewall / Monitoring Route | Open | 이권욱 | 일치 |
| [fds-project-baseline #15](https://github.com/321Team/fds-project-baseline/issues/15) [P1-APP-01] transaction-api / fds-engine | Open | 이재환 | 일치 |
| [fds-project-baseline #16](https://github.com/321Team/fds-project-baseline/issues/16) [P1-CICD-01] GitHub Actions / Self-hosted Runner Delivery | Open | 이권욱 | 일치 |
| [fds-project-baseline #17](https://github.com/321Team/fds-project-baseline/issues/17) [P1-MON-01] Kubernetes-Integrated Hybrid Monitoring 구축 및 검증 | Open | 이재환 | 일치 |
| [fds-project-baseline #18](https://github.com/321Team/fds-project-baseline/issues/18) [MS-G1-01] G1 Infrastructure Ready | Open | 이권욱 | 일치 |
| [fds-project-baseline #19](https://github.com/321Team/fds-project-baseline/issues/19) [P1-SEC-01] Kubernetes Security Controls | Open | 이하영 | 일치 |
| [fds-project-baseline #20](https://github.com/321Team/fds-project-baseline/issues/20) [P1-E2E-01] Initial / Final E2E & Regression | Open | 이재환 | 일치 |
| [fds-project-baseline #21](https://github.com/321Team/fds-project-baseline/issues/21) [P1-DR-01] PostgreSQL Backup / Restore | Open | 이재환 | 일치 |
| [fds-project-baseline #22](https://github.com/321Team/fds-project-baseline/issues/22) [P1-HA-01] Worker Drain Continuity | Open | 이재환 | 일치 |
| [fds-project-baseline #23](https://github.com/321Team/fds-project-baseline/issues/23) [MS-G2-01] G2 Security / Feature Ready | Open | 이하영 | 일치 |
| [fds-project-baseline #24](https://github.com/321Team/fds-project-baseline/issues/24) [P1-DOC-01] Architecture / Test / Runbook Freeze | Open | 이권욱 | 일치 |
| [fds-project-baseline #25](https://github.com/321Team/fds-project-baseline/issues/25) [P1-MON-02] Dashboard / Alert Enhancement | Open | 이재환 | 일치 |
| [fds-project-baseline #26](https://github.com/321Team/fds-project-baseline/issues/26) [P1-DR-02] Harbor / etcd Backup and Restore | Open | 이하영 | 일치 |
| [fds-project-baseline #27](https://github.com/321Team/fds-project-baseline/issues/27) [P1-HA-02] Platform Resilience P1 Validation | Open | 이하영 | 일치 |
| [fds-project-baseline #28](https://github.com/321Team/fds-project-baseline/issues/28) [DEC-CAL-P1-01] Phase 1 Weekend Review Decision | Open | 이권욱 | 일치 |
| [fds-project-baseline #29](https://github.com/321Team/fds-project-baseline/issues/29) [MS-G3-01] G3 Review Ready | Open | 이권욱 | 일치 |
| [fds-project-baseline #30](https://github.com/321Team/fds-project-baseline/issues/30) [P1-REV-01] Phase 1 Review / Close Execution | Open | 이권욱 | 일치 |
| [fds-project-baseline #31](https://github.com/321Team/fds-project-baseline/issues/31) [MS-P1-REVIEW-01] Phase 1 Review | Open | 이권욱 | 일치 |
| [fds-project-baseline #32](https://github.com/321Team/fds-project-baseline/issues/32) [MS-P1-CLOSE-01] Phase 1 Close | Open | 이권욱 | 일치 |
| [fds-project-baseline #33](https://github.com/321Team/fds-project-baseline/issues/33) [MS-P2-START-01] Phase 2 Start | Open | 이권욱 | 일치 |
| [fds-project-baseline #34](https://github.com/321Team/fds-project-baseline/issues/34) [P2-ARC-01] Hybrid / OCI / AWS / ROSA Architecture Freeze | Open | 이권욱 | 일치 |
| [fds-project-baseline #35](https://github.com/321Team/fds-project-baseline/issues/35) [P2-IAC-01] AWS / ROSA Terraform IaC | Open | 이권욱 | 일치 |
| [fds-project-baseline #36](https://github.com/321Team/fds-project-baseline/issues/36) [P2-OCI-01] OCI Relay Go / No-Go | Open | 이권욱 | 일치 |
| [fds-project-baseline #37](https://github.com/321Team/fds-project-baseline/issues/37) [P2-VPN-01] OCI Relay / AWS Site-to-Site VPN | Open | 이권욱 | 일치 |
| [fds-project-baseline #38](https://github.com/321Team/fds-project-baseline/issues/38) [P2-ROSA-01] ROSA Platform / Security | Open | 이하영 | 일치 |
| [fds-project-baseline #39](https://github.com/321Team/fds-project-baseline/issues/39) [MS-G4-01] G4 Cloud / VPN Ready | Open | 이권욱 | 일치 |
| [fds-project-baseline #40](https://github.com/321Team/fds-project-baseline/issues/40) [DEC-P2-DNS-01] Hybrid DNS Scope Decision | Open | 이권욱 | 일치 |
| [fds-project-baseline #41](https://github.com/321Team/fds-project-baseline/issues/41) [DEC-P2-OP-01] Operator Supply Chain Scope Decision | Open | 이하영 | 일치 |
| [fds-project-baseline #42](https://github.com/321Team/fds-project-baseline/issues/42) [DEC-P2-REG-01] ROSA Image Registry Source Decision | Open | 이하영 | 일치 |
| [fds-project-baseline #43](https://github.com/321Team/fds-project-baseline/issues/43) [P2-APP-01] ROSA Application Deployment | Open | 이재환 | 일치 |
| [fds-project-baseline #44](https://github.com/321Team/fds-project-baseline/issues/44) [P2-OADP-01] OADP / S3 Backup | Open | 이하영 | 일치 |
| [fds-project-baseline #45](https://github.com/321Team/fds-project-baseline/issues/45) [MS-G5-01] G5 ROSA Application Ready | Open | 이하영 | 일치 |
| [fds-project-baseline #46](https://github.com/321Team/fds-project-baseline/issues/46) [P2-CICD-01] Runner to ROSA Delivery | Open | 이권욱 | 일치 |
| [fds-project-baseline #47](https://github.com/321Team/fds-project-baseline/issues/47) [P2-HYB-01] Hybrid DB / Registry Integration | Open | 이재환 | 일치 |
| [fds-project-baseline #48](https://github.com/321Team/fds-project-baseline/issues/48) [P2-DNS-01] Hybrid DNS Implementation Conditional | Open | 이권욱 | 일치 |
| [fds-project-baseline #49](https://github.com/321Team/fds-project-baseline/issues/49) [P2-DOC-01] Cloud / Hybrid Deliverable Freeze | Open | 이권욱 | 일치 |
| [fds-project-baseline #50](https://github.com/321Team/fds-project-baseline/issues/50) [P2-E2E-01] Hybrid E2E / Regression | Open | 이재환 | 일치 |
| [fds-project-baseline #51](https://github.com/321Team/fds-project-baseline/issues/51) [P2-OP-01] Operator Supply Chain Implementation Conditional | Open | 이하영 | 일치 |
| [fds-project-baseline #52](https://github.com/321Team/fds-project-baseline/issues/52) [DEC-CAL-P2-01] Phase 2 Weekend Review Decision | Open | 이권욱 | 일치 |
| [fds-project-baseline #53](https://github.com/321Team/fds-project-baseline/issues/53) [MS-G6-01] G6 Hybrid Integration Ready | Open | 이권욱 | 일치 |
| [fds-project-baseline #54](https://github.com/321Team/fds-project-baseline/issues/54) [MS-DELIVERABLE-FREEZE-01] Deliverable Freeze | Open | 이권욱 | 일치 |
| [fds-project-baseline #55](https://github.com/321Team/fds-project-baseline/issues/55) [P2-REV-01] Phase 2 Review / Project Close Execution | Open | 이권욱 | 일치 |
| [fds-project-baseline #56](https://github.com/321Team/fds-project-baseline/issues/56) [MS-P2-REVIEW-01] Phase 2 Review | Open | 이권욱 | 일치 |
| [fds-project-baseline #57](https://github.com/321Team/fds-project-baseline/issues/57) [MS-PROJECT-CLOSE-01] Project Close | Open | 이권욱 | 일치 |
| [fds-project-baseline #58](https://github.com/321Team/fds-project-baseline/issues/58) [CR-P1-ANS-01-01] Ansible Kubernetes Node DNS Resolver 변경 | Closed | 이권욱 | 일치 |
| [fds-project-baseline #59](https://github.com/321Team/fds-project-baseline/issues/59) [D-ARC-01] Phase 1 Logical / Physical Architecture Design Freeze | Closed | 이권욱 | 일치 |
| [fds-project-baseline #60](https://github.com/321Team/fds-project-baseline/issues/60) [D-NET-01] Physical / Management Network Design Freeze | Closed | 이권욱 | 일치 |
| [fds-project-baseline #61](https://github.com/321Team/fds-project-baseline/issues/61) [D-WBS-01] WBS / Backlog / Interface Management Freeze | Closed | 이권욱 | 일치 |
| [fds-project-baseline #62](https://github.com/321Team/fds-project-baseline/issues/62) [DEC-P1-ENTRY-01] Edge Service Exposure Decision | Closed | 이권욱 | 일치 |
| [fds-project-baseline #63](https://github.com/321Team/fds-project-baseline/issues/63) [DEC-P1-MON-01] Kubernetes-Integrated Hybrid Monitoring Architecture | Closed | 이권욱 | 일치 |
| [fds-project-baseline #64](https://github.com/321Team/fds-project-baseline/issues/64) [DEC-P1-TLS-01] Harbor / Edge TLS Trust Decision | Closed | 이권욱 | 일치 |
| [fds-project-baseline #65](https://github.com/321Team/fds-project-baseline/issues/65) [P1-ANS-01] Ansible Inventory / OS-Node Bootstrap — Closed Update | Closed | 이권욱 | 일치 |
| [fds-project-baseline #66](https://github.com/321Team/fds-project-baseline/issues/66) [P1-LNX-01] CentOS Stream 10 Linux / Network Baseline | Closed | 이권욱 | 일치 |
| [fds-project-baseline #67](https://github.com/321Team/fds-project-baseline/issues/67) [P1-NET-01] Bridged Multi-MAC Smoke Test / Source Preservation | Closed | 이권욱 | 일치 |
| [fds-project-baseline #74](https://github.com/321Team/fds-project-baseline/issues/74) [CR-P1-MON-01-01] Alertmanager Egress 프록시 서버 구성 | Open | 이하영 | 일치 |
| [fds-project-baseline #75](https://github.com/321Team/fds-project-baseline/issues/75) [CR-P1-MON-01-02] Alertmanager Egress Kubernetes 보안 설정 (NetworkPolicy) | Open | 이하영 | 일치 |
| [fds-project-baseline #78](https://github.com/321Team/fds-project-baseline/issues/78) [DEC-P1-EGRESS-01] Alertmanager 전용 프록시 배치·예약 IP 사용 결정 | Open | 이권욱 | 일치 |
| [fds-project-evidence #4](https://github.com/321Team/fds-project-evidence/issues/4) [증적 후속] FUP-04/05/06/07 잔여 참조 및 FUP-09 조건부 인수 반영 | Open | 이권욱 | 일치 |
| [fds-project-evidence #8](https://github.com/321Team/fds-project-evidence/issues/8) [Evidence] P1-DB-01 증적 등록 현황 및 잔여 후속 항목 | Open | 이재환 | 일치 |
| [infra-ansible #5](https://github.com/321Team/infra-ansible/issues/5) [P1-CICD-01 연관] infra-ansible CI 회귀 시험과 실패 차단 연동 | Open | 이권욱 | 일치 |
| [infra-ansible #6](https://github.com/321Team/infra-ansible/issues/6) [PR4 후속] SSH 회귀 시험의 Ansible 내부 API 의존 제거 | Closed | 이권욱 | 일치 |
| [infra-ansible #7](https://github.com/321Team/infra-ansible/issues/7) [PR4 후속] 서버 검증 결과 구조화 및 누락·실패 판정 강화 | Closed | 이권욱 | 일치 |
| [infra-ansible #8](https://github.com/321Team/infra-ansible/issues/8) [PR4 후속] 검증 키트의 완전한 재현 가능한 배포 구성 | Open | 이권욱 | 일치 |
| [infra-ansible #9](https://github.com/321Team/infra-ansible/issues/9) [P1-ANS-01 연관] ansible-core 2.16.19 → 2.21.3 운영 전환 영향 검토·검증 | Open | 이권욱 | 일치 |
| [infra-ansible #10](https://github.com/321Team/infra-ansible/issues/10) [PR4 운영 적용] 승인 main SSH 수정의 6대 순차 적용·멱등성·신규 SSH 검증 | Closed | 이권욱 | 일치 |
| [infra-db #1](https://github.com/321Team/infra-db/issues/1) [P1-DB-01] db01 PostgreSQL 구축 · 스키마 · 마이그레이션 · 백업 작업 내역 | Open | 이재환 | 일치 |
| [infra-db #2](https://github.com/321Team/infra-db/issues/2) [관측/DB] db01 장애 시 거래 저장 실패 탐지·알림 공백 — 동작 확정 + 알림 룰 추가 제안 | Open | 이재환 | 일치 |
| [infra-kubernetes #5](https://github.com/321Team/infra-kubernetes/issues/5) [P1-K8S 연관] Alertmanager egress 허용 요청 — 이상거래 탐지 알림 외부 통지 (E-CANON 대상) | Closed | 이하영 | 일치 |

## 변경 감사 자료

[증적 압축본](sandbox:/workspace/scratch/f136ee38a25c/FDS_Ticket_Spec_Update_Evidence_20260915_v1.0.zip)에는 원격 전체 응답 before/after, 적용한 블록, 작업 결과, 티켓별 원문/갱신 본문 SHA256, 전체 재조회 판정과 파일 Manifest를 포함한다.

이 자료는 본문 갱신의 무결성·필드 보존 증거다. 실제 서버의 구성·시험 결과나 기술 인수를 새로 검증한 증거가 아니다.
