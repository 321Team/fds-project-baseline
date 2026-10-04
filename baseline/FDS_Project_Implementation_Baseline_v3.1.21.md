# On-Premises / Hybrid FDS Implementation Baseline v3.1.21

Status: RELEASED after reviewed finalization merge. Version: docs-v3.1.21. Actual publication: Release API / Assets verification.
기준일: 2026-10-03 KST. 사용자 요청에 따라 현 시점 계획·테스트 전략·실제 잔여를 동기화한다. 이 문서 발행은 P1 Close·Architecture Freeze·운영 Runtime 인수를 대신하지 않는다.

## 1. 이번 버전의 권위와 변경

현재 계획/담당/상태는 아래 78개 Record와 Ticket Pack이 기준이다. 승인된 기술 요구는 이전 v3.1.20에서 상속하며, 최신 정식 Decision/CR과 본 절의 명시적 정정이 충돌 항목에 우선한다. 과거 완료·날짜·후보 표기는 역사이며 현재 상태로 재사용하지 않는다.

- D21 FINAL: OCI Primary NO-GO(project suitability), AWS EC2+EIP self-managed Libreswan relay 선택. Region ap-northeast-2, VPC10.20/16, Relay10.20.110.10/subnet10.20.110/24, AZ2a/apne2-az1, t3.medium, encrypted gp3 40GiB, EIP1, public SSH DENY/SSM. 정확 AMI/route/security frozen input은 #36과 Architecture source snapshot 참조. 신규 sizing/NAT/source 모델 권장안은 미승인.
- P1 Close HOLD. #15 local endpoint 보장, #16 Delivery Runtime, #19 rollback 잔여를 보존한다. 10/6 심사 결과는 아직 없다.
- #119 Done: DB 장애는 API /readyz503·Endpoint 제외, engine 장애는 API Ready·HTTP201·skipped=true·DB 저장. ROSA에서 별도 검증.
- #125 Done: backup/rollback은 P1 필수, 예방 rotation은 NOT MET/RISK ACCEPTED. Receiver 없는 P2 이관 완료 금지. #126/#127/#128은 no-change 이력.
- #130 Done: OID02 결정은 #14가 추적하며 HBR 입력 제공은 유지. #16이 동일 Review Run 4/4·rollback을 생산하고 #13이 05B를 인수한다. HBR 종결 Gate를 제거하지 않는다.
- #110 Done: Wolfi/apko 공급망 Decision 승인. 구현 Source 병합과 Delivery Runtime을 구분한다.
- #74/#75/#109 등 완료 결정·변경은 최신 Record/원문으로 동기화하며 관련 Runtime·다른 Gate를 자동 Done으로 바꾸지 않는다.

## 2. 일정과 실행 의존성

P1 Review/Close10/6 → Phase2 Start10/7 → Architecture 목표10/8 → Stage-A 조건부10/8 → VPN10/12~14/G4 10/14 → Platform10/15~19 → App10/16~19 → G5/Delivery10/20 → Hybrid10/21 → G6/E2E10/22 → Deliverable Freeze/Review10/23 → Project Close10/26.
10/5·10/9 비근무일, 주말 근무 없음. 계획일은 실제 수행/승인이 아니다. #34 10/8과 capacity 입력 제안10/12 충돌은 **최초 Freeze 전에 입력 제출**로 제약을 명시하고 정확 날짜는 미확정으로 둔다. 기존 Issue 날짜는 임의 변경하지 않는다.
D21 결정은 10/3에 완료했지만 원래10/7~8 계획과 별도 기록한다. Architecture/Stage-A는 후속 사양·계정·검토plan/비용 조건 전 HOLD다.

## 3. 테스트 전략

상세 정본 입력: [FDS Test Strategy](../tests/FDS_Test_Strategy_v3.1.21.md). WBS의 Test Strategy 시트와 TS01~16으로 대응한다.
W0 Local/CI/LAB → W1 계약·계정·network/VPN → W2 Platform/App/Delivery → W3 동일 ROSA Hybrid/E2E/negative/recovery → 10/23 원본 보존·teardown. 생성 전 준비와 생성 후 실제 인수 조건을 분리한다. PG03 actual을 admission/mock로 대체하지 않는다. #16/#13 동일 회차 증적 공유와 소비자 인수 기록으로 중복 시험을 줄인다.
Source→digest→runtime imageID→test/data→raw/hash→독립 review/편입의 추적을 유지한다. 보안·실패/복구 AC 축소, 무근거 PASS, broad SCC/TLS/방화벽 우회는 없다.

## 4. 비용·미확정 계약과 발행 경계

교육장 한도·기간 및 일일 리포트와 전체 자원 비용/잔여 가동시간을 연결해야 한다. 400/450/500 역사 입력과 최신 비용 권위의 정렬은 미완이다. 미조회 금액은 0이 아니며 별도 Billing 관리자 권한·교육장 승인 요구를 추가하지 않는다. 신규 유료 실행 전 해당 Lead가 실제 입력을 고정한다.
Architecture PR8 c421733 revision2는 설계 후보다. HCP지원/sizing/N-1·management DNS/route·stable source/권한/SLA·Harbor CA·managed recovery·계정/비용이 남아 있다. D21 raw8706B의 수신 재해시·발행도 HOLD다. 이 잔여는 실제 구축/인수 Gate이며 문서에서 숨기지 않는다.
정본 발행 조건은 산출물 일치·workbook/manifest/hash·민감정보 검사·PR112 혼합 코드 독립 리뷰·검토 병합·최종화·Tag/Release Asset 동일성이다. 이번 생성만으로 RELEASED라고 표시하지 않는다.

## 5. 현재 Record register

| Record | Source status | GitHub | Lead | Plan Start | Plan End |
|---|---|---|---|---|---|
| [DEC-P1-FDS-01](https://github.com/321Team/fds-project-baseline/issues/4) | Done | closed/completed | 이재환 | 2026-09-08 | 2026-09-09 |
| [DEC-P1-TXN-01](https://github.com/321Team/fds-project-baseline/issues/5) | Done | closed/completed | 이재환 | 2026-09-08 | 2026-09-09 |
| [DEC-P1-ADMIN-01](https://github.com/321Team/fds-project-baseline/issues/6) | Done | closed/completed | 이하영 | 2026-09-08 | 2026-09-09 |
| [D-SEC-01](https://github.com/321Team/fds-project-baseline/issues/7) | Done | closed/completed | 이하영 | 2026-08-26 | 2026-09-01 |
| [MS-G0-01](https://github.com/321Team/fds-project-baseline/issues/8) | Done | closed/completed | 이권욱 | 2026-08-26 | 2026-09-01 |
| [P1-LB-01](https://github.com/321Team/fds-project-baseline/issues/9) | In Progress | open/None | 이권욱 | 2026-08-27 | 2026-09-17 |
| [P1-K8S-01](https://github.com/321Team/fds-project-baseline/issues/10) | In Progress | open/None | 이하영 | 2026-08-27 | 2026-09-17 |
| [P1-DB-01](https://github.com/321Team/fds-project-baseline/issues/11) | In Progress | open/None | 이재환 | 2026-08-28 | 2026-09-17 |
| [P1-DNS-01](https://github.com/321Team/fds-project-baseline/issues/12) | Done | closed/completed | 이권욱 | 2026-08-28 | 2026-09-03 |
| [P1-HBR-01](https://github.com/321Team/fds-project-baseline/issues/13) | In Progress | open/None | 이하영 | 2026-08-31 | 2026-09-17 |
| [ICR-D-NET-01-01](https://github.com/321Team/fds-project-baseline/issues/14) | In Progress | open/None | 이권욱 | 2026-09-01 | 2026-09-21 |
| [P1-APP-01](https://github.com/321Team/fds-project-baseline/issues/15) | In Progress | open/None | 이재환 | 2026-09-01 | 2026-09-18 |
| [P1-CICD-01](https://github.com/321Team/fds-project-baseline/issues/16) | In Progress | open/None | 이권욱 | 2026-09-01 | 2026-09-18 |
| [P1-MON-01](https://github.com/321Team/fds-project-baseline/issues/17) | In Progress | open/None | 이재환 | 2026-09-07 | 2026-09-18 |
| [MS-G1-01](https://github.com/321Team/fds-project-baseline/issues/18) | To Do | open/None | 이권욱 | 2026-09-17 | 2026-09-17 |
| [P1-SEC-01](https://github.com/321Team/fds-project-baseline/issues/19) | In Progress | open/None | 이하영 | 2026-09-04 | 2026-09-21 |
| [P1-E2E-01](https://github.com/321Team/fds-project-baseline/issues/20) | In Progress | open/None | 이재환 | 2026-09-11 | 2026-10-02 |
| [P1-DR-01](https://github.com/321Team/fds-project-baseline/issues/21) | In Progress | open/None | 이재환 | 2026-09-11 | 2026-10-02 |
| [P1-HA-01](https://github.com/321Team/fds-project-baseline/issues/22) | In Progress | open/None | 이재환 | 2026-09-11 | 2026-10-02 |
| [MS-G2-01](https://github.com/321Team/fds-project-baseline/issues/23) | To Do | open/None | 이하영 | 2026-09-21 | 2026-09-21 |
| [P1-DOC-01](https://github.com/321Team/fds-project-baseline/issues/24) | To Do | open/None | 이권욱 | 2026-09-11 | 2026-10-02 |
| [P1-MON-02](https://github.com/321Team/fds-project-baseline/issues/25) | To Do | open/None | 이재환 | TBD — P0 인수 후 재계획 | TBD — 구현 유예 권장 |
| [P1-DR-02](https://github.com/321Team/fds-project-baseline/issues/26) | To Do | open/None | 이하영 | TBD — P0 인수 후 재계획 | TBD — 구현 유예 권장 |
| [P1-HA-02](https://github.com/321Team/fds-project-baseline/issues/27) | To Do | open/None | 이하영 | TBD — P0 인수 후 재계획 | TBD — 구현 유예 권장 |
| [DEC-CAL-P1-01](https://github.com/321Team/fds-project-baseline/issues/28) | Done | closed/completed | 이권욱 | 2026-09-11 | 2026-09-11 |
| [MS-G3-01](https://github.com/321Team/fds-project-baseline/issues/29) | To Do | open/None | 이권욱 | 2026-10-02 | 2026-10-02 |
| [P1-REV-01](https://github.com/321Team/fds-project-baseline/issues/30) | To Do | open/None | 이권욱 | 2026-10-06 | 2026-10-06 |
| [MS-P1-REVIEW-01](https://github.com/321Team/fds-project-baseline/issues/31) | To Do | open/None | 이권욱 | 2026-10-06 | 2026-10-06 |
| [MS-P1-CLOSE-01](https://github.com/321Team/fds-project-baseline/issues/32) | To Do | open/None | 이권욱 | 2026-10-06 | 2026-10-06 |
| [MS-P2-START-01](https://github.com/321Team/fds-project-baseline/issues/33) | To Do | open/None | 이권욱 | 2026-10-07 | 2026-10-07 |
| [P2-ARC-01](https://github.com/321Team/fds-project-baseline/issues/34) | To Do | open/None | 이권욱 | 2026-10-08 | 2026-10-08 |
| [P2-IAC-01](https://github.com/321Team/fds-project-baseline/issues/35) | To Do | open/None | 이하영 | 2026-10-08 | 2026-10-14 |
| [P2-OCI-01](https://github.com/321Team/fds-project-baseline/issues/36) | To Do | open/None | 이권욱 | 2026-10-07 | 2026-10-08 |
| [P2-VPN-01](https://github.com/321Team/fds-project-baseline/issues/37) | To Do | open/None | 이재환 | 2026-10-12 | 2026-10-14 |
| [P2-ROSA-01](https://github.com/321Team/fds-project-baseline/issues/38) | To Do | open/None | 이하영 | 2026-10-15 | 2026-10-19 |
| [MS-G4-01](https://github.com/321Team/fds-project-baseline/issues/39) | To Do | open/None | 이권욱 | 2026-10-14 | 2026-10-14 |
| [DEC-P2-DNS-01](https://github.com/321Team/fds-project-baseline/issues/40) | To Do | open/None | 이권욱 | 2026-10-16 | 2026-10-16 |
| [DEC-P2-OP-01](https://github.com/321Team/fds-project-baseline/issues/41) | To Do | open/None | 이하영 | TBD — G5 이후 P0 잔여 capacity 시 | TBD — 10-26 이전 강제하지 않음 |
| [DEC-P2-REG-01](https://github.com/321Team/fds-project-baseline/issues/42) | To Do | open/None | 이권욱 | 2026-10-15 | 2026-10-15 |
| [P2-APP-01](https://github.com/321Team/fds-project-baseline/issues/43) | To Do | open/None | 이재환 | 2026-10-16 | 2026-10-19 |
| [P2-OADP-01](https://github.com/321Team/fds-project-baseline/issues/44) | To Do | open/None | 이하영 | TBD — G5 이후 P0 잔여 capacity 시 | TBD — 10-26 이전 강제하지 않음 |
| [MS-G5-01](https://github.com/321Team/fds-project-baseline/issues/45) | To Do | open/None | 이하영 | 2026-10-20 | 2026-10-20 |
| [P2-CICD-01](https://github.com/321Team/fds-project-baseline/issues/46) | To Do | open/None | 이권욱 | 2026-10-20 | 2026-10-20 |
| [P2-HYB-01](https://github.com/321Team/fds-project-baseline/issues/47) | To Do | open/None | 이재환 | 2026-10-21 | 2026-10-21 |
| [P2-DNS-01](https://github.com/321Team/fds-project-baseline/issues/48) | To Do | open/None | 이권욱 | TBD — D23 Go + P0 잔여 capacity 시 | TBD — 10-26 이전 강제하지 않음 |
| [P2-DOC-01](https://github.com/321Team/fds-project-baseline/issues/49) | To Do | open/None | 이권욱 | 2026-10-23 | 2026-10-23 |
| [P2-E2E-01](https://github.com/321Team/fds-project-baseline/issues/50) | To Do | open/None | 이재환 | 2026-10-22 | 2026-10-22 |
| [P2-OP-01](https://github.com/321Team/fds-project-baseline/issues/51) | To Do | open/None | 이하영 | TBD — D26 Mirror + P0 잔여 capacity 시 | TBD — 10-26 이전 강제하지 않음 |
| [DEC-CAL-P2-01](https://github.com/321Team/fds-project-baseline/issues/52) | To Do | open/None | 이권욱 | 2026-10-07 | 2026-10-07 |
| [MS-G6-01](https://github.com/321Team/fds-project-baseline/issues/53) | To Do | open/None | 이권욱 | 2026-10-22 | 2026-10-22 |
| [MS-DELIVERABLE-FREEZE-01](https://github.com/321Team/fds-project-baseline/issues/54) | To Do | open/None | 이권욱 | 2026-10-23 | 2026-10-23 |
| [P2-REV-01](https://github.com/321Team/fds-project-baseline/issues/55) | To Do | open/None | 이권욱 | 2026-10-23 | 2026-10-26 |
| [MS-P2-REVIEW-01](https://github.com/321Team/fds-project-baseline/issues/56) | To Do | open/None | 이권욱 | 2026-10-23 | 2026-10-23 |
| [MS-PROJECT-CLOSE-01](https://github.com/321Team/fds-project-baseline/issues/57) | To Do | open/None | 이권욱 | 2026-10-26 | 2026-10-26 |
| [CR-P1-ANS-01-01](https://github.com/321Team/fds-project-baseline/issues/58) | Done | closed/completed | 이권욱 | 2026-09-04 | 2026-09-07 |
| [D-ARC-01](https://github.com/321Team/fds-project-baseline/issues/59) | Done | closed/completed | 이권욱 | 2026-08-24 | 2026-08-26 |
| [D-NET-01](https://github.com/321Team/fds-project-baseline/issues/60) | Done | closed/completed | 이권욱 | 2026-08-24 | 2026-08-26 |
| [D-WBS-01](https://github.com/321Team/fds-project-baseline/issues/61) | Done | closed/completed | 이권욱 | 2026-08-24 | 2026-08-26 |
| [DEC-P1-ENTRY-01](https://github.com/321Team/fds-project-baseline/issues/62) | Done | closed/completed | 이권욱 | 2026-08-27 | 2026-08-31 |
| [DEC-P1-MON-01](https://github.com/321Team/fds-project-baseline/issues/63) | Done | closed/completed | 이권욱 | 2026-08-31 | 2026-08-31 |
| [DEC-P1-TLS-01](https://github.com/321Team/fds-project-baseline/issues/64) | Done | closed/completed | 이권욱 | 2026-08-27 | 2026-08-31 |
| [P1-ANS-01](https://github.com/321Team/fds-project-baseline/issues/65) | Done | closed/completed | 이권욱 | 2026-08-27 | 2026-09-01 |
| [P1-LNX-01](https://github.com/321Team/fds-project-baseline/issues/66) | Done | closed/completed | 이권욱 | 2026-08-24 | 2026-08-26 |
| [P1-NET-01](https://github.com/321Team/fds-project-baseline/issues/67) | Done | closed/completed | 이권욱 | 2026-08-27 | 2026-08-27 |
| [CR-P1-MON-01-01](https://github.com/321Team/fds-project-baseline/issues/74) | Done | closed/completed | 이하영 | 2026-09-11 | 2026-10-06 |
| [CR-P1-MON-01-02](https://github.com/321Team/fds-project-baseline/issues/75) | Done | closed/completed | 이하영 | 2026-09-11 | 2026-10-06 |
| [DEC-P1-EGRESS-01](https://github.com/321Team/fds-project-baseline/issues/78) | Done | closed/completed | 이권욱 | 2026-09-14 | 2026-09-21 |
| [DEC-P2-RHOAI-01](https://github.com/321Team/fds-project-baseline/issues/95) | To Do | open/None | 이하영 | TBD — Deferred 우선 | TBD — 프로젝트 종료 후 별도 PoC는 Project Scope 밖 |
| [DEC-P1-MON-02](https://github.com/321Team/fds-project-baseline/issues/109) | Done | closed/completed | 이권욱 | 2026-09-26 | 2026-09-26 |
| [DEC-P1-IMG-01](https://github.com/321Team/fds-project-baseline/issues/110) | Done | closed/completed | 이재환 | 2026-09-27 | 2026-10-06 |
| [CR-P1-APP-01-01](https://github.com/321Team/fds-project-baseline/issues/119) | Done | closed/completed | 이재환 | 2026-09-29 | 2026-10-02 |
| [DEC-P2-GITOPS-01](https://github.com/321Team/fds-project-baseline/issues/120) | To Do | open/None | 이권욱 | TBD — G5 이후 P0 잔여 capacity 시 | TBD — 10-26 이전 강제하지 않음 |
| [DEC-P2-COMP-01](https://github.com/321Team/fds-project-baseline/issues/121) | To Do | open/None | 이하영 | TBD — G5 이후 P0 잔여 capacity 시 | TBD — 10-26 이전 강제하지 않음 |
| [CR-P1-SEC-01-01](https://github.com/321Team/fds-project-baseline/issues/125) | Done | closed/completed | 이하영 | 2026-09-30 | 2026-10-02 |
| [CR-P1-SEC-01-02](https://github.com/321Team/fds-project-baseline/issues/126) | Done | closed/not_planned | 이하영 | 2026-09-30 | 2026-10-02 |
| [CR-P1-SEC-01-03](https://github.com/321Team/fds-project-baseline/issues/127) | Done | closed/not_planned | 이하영 | 2026-09-30 | 2026-10-02 |
| [CR-P1-K8S-01-01](https://github.com/321Team/fds-project-baseline/issues/128) | Todo | closed/not_planned | 이하영 | 2026-09-30 | 2026-10-02 |
| [CR-P1-HBR-01-01](https://github.com/321Team/fds-project-baseline/issues/130) | Done | closed/completed | 이하영 | 2026-09-30 | 2026-10-02 |

## 6. 상속 명세와 역사적 상태

아래는 v3.1.20 문서 원문의 상속 명세다. 날짜·Status·집계·정본 버전·변경결정은 위 현행 register/정정으로 대체하며 나머지 승인 요구만 상속한다. 발행 v3.1.20 파일 자체는 수정하지 않는다.

<details>
<summary>v3.1.20 명세 원문 — 당시 변경·상태 포함</summary>


# On-Premises / Hybrid FDS 프로젝트 Implementation Baseline v3.1.20

> **Release:** v3.1.20  
> **Status:** CANDIDATE / COLLECTING — 정식 발행 보류, release/v3.1.20 후보 수집 중 (PR #87)  
> **팀 프로젝트 착수일:** 2026-08-24  
> **팀 구성:** 3인  
> **1차 부제:** MSA 기반 거래 시스템 구축 및 FDS 모니터링  
> **2차 부제:** Terraform IaC 기반 Cloud 확장 및 Rule-Based FDS 운영  
> **Architecture Theme:** Kubernetes 표준 보안통제를 적용한 금융 Mini FDS 실습 플랫폼  
> **주의:** 교육/PoC 목적이며 실제 금융 규제 준수 인증 또는 Production 적합성을 주장하지 않는다.

---

## 0. v3.1.20 통합 변경 (CANDIDATE)

기준 2026-09-22 KST. v3.1.19 태그(`966fc5365874b1d259a9810fc876b57c3bfa0e08`, 2026-09-17) 이후 **종결(Done) 처리된 GitHub Issue 0건**이며, WBS/Ticket Pack/Baseline/Architecture 콘텐츠(완료 상태) 변경은 없다. 아래 두 종류의 변경만 반영한다.

**governance/tooling 드리프트(§2.4 운영 경로 예외 대상, RELEASE_POLICY 참조)**: PR #80/#81(governance 정책 개정), PR #82(canonical-integrity checkout SHA 고정), PR #88(WARN/FAIL 분리 로직), PR #89(미사용 Gemini 리뷰 워크플로 제거).

**Phase 2 일정 재계획(Lead 결정, 2026-09-22)**: Phase 1 지연으로 Phase 2 착수(`MS-P2-START-01` #33)가 09-28→10-06으로 순연. 뒷단(G6 Hybrid Integration Ready 10-22 ~ Project Close 10-26)은 기존 §2 일정 그대로 유지하고, 앞단(설계 동결~G5)만 24일→16일로 압축(비율 0.667)했다. `DEC-P2-DNS-01`/`DEC-P2-OP-01`/`DEC-P2-REG-01`은 Decision Register(D22/D23/D26, 2026-10-16 고정)와의 정합을 위해 압축 예외로 원래 일정을 유지한다. `CR-P1-MON-01-01`(#74) Start 09-11 유지, `CR-P1-MON-01-02`(#75) Start 09-11 신규 입력, 두 건 End 2026-10-06 입력. 세부 근거는 각 GitHub Issue 코멘트(2026-09-22) 및 `wbs/FDS_v3.1.20_WBS_and_Gantt_v1.0.xlsx`의 Sources & Change Log 시트를 참조한다.

이 절은 §2.3(완료 변경 요청의 정본 동기화)이 요구하는 "Done/Merged Change Request 동기화"의 대상이 되는 실제 티켓 완료 건이 없음을 확인한 기록이며, 일정 재계획 자체는 §4.1(일정 유연성)에 따른 계획 목표 조정이다. 아래 §0(v3.1.19 통합 변경)부터는 이전 버전 시점의 기록으로 보존한다.

---

## 0. v3.1.19 통합 변경

기준 2026-09-17 20:28 KST. 전체 67건 / 일정관리 58건 / 역사적 종결 9건 / Milestone 67/67건. 상태 집계: Done 18, In Progress 11, To Do 38.

v19 내용은 이하영의 독립 승인 후 PR #73으로 병합됐다. 이 변경은 배포 메타데이터 최종화이며 최종화 PR 승인·병합과 GitHub Tag/Asset 게시 검증이 필요하다. 실제 발행 여부는 CURRENT와 Release API를 따른다. 아래 §0의 승인 변경과 §16의 현행 상태가 과거 버전의 당시 상태보다 우선한다. 과거 버전 명칭·날짜는 이력으로 보존한다.

## 승인 입력과 적용 경계

| 항목 | 반영한 값·결정 | 유지되는 경계 |
|---|---|---|
| PR #72 | v18 게시 사실·WEB 필수 배포·일정 유연성·#59/#61 08-26·#46 10-16·Milestone 배정 | 기존 v18 태그와 Asset 소급 변경 없음 |
| DEC-CAL-P1-01 #28 | 09-22 오후 평일 Review 일정 결정 Done | 실제 Review/G3/Close 승인 아님 |
| DEC-P1-EGRESS-01 #78 | server08 / egress-proxy01 / .56:3128, 2vCPU·2GiB·30GiB, .57 예비 유지 | #74 Squid·#75 NetworkPolicy/Secret Runtime 별도 |
| OID-01 | ansible01 10.250.10.10/32 + svc_ansible, 내부 SNAT 금지·기존 Return Route | HEP/GNP 실제 적용은 6/6 Ready 이후 별도 실행창 |
| Monitoring storage | worker03(.108), /home/fds-local-pv/{prometheus,grafana,alertmanager}; static local PV/WFFC/Retain/nodeAffinity | 단일 Worker non-HA, 경로·SELinux·공간 검증 및 Runtime 미완료 |
| PVC 초기값 | Prometheus 20Gi / Grafana 5Gi / Alertmanager 2Gi, Prometheus 15d·retention.size≤16GB | 사용률에 따른 조정 가능한 초기값 |
| NTP 결정 | control01 내부 chronyd, UDP123, offset≤100ms, 60초×6, sync lost≥5m FAIL, reboot≤5m 재동기화 | control01 upstream/time authority 미정; INPUT_INCOMPLETE/RUNTIME_HOLD |
| Harbor/CI 정책 | Worker pull-only 분리, Robot 유한 30일 결정·Never 미채택, Harbor Scanner 유지, HIGH/CRITICAL·Scanner/DB 오류 차단 | 실제 계정·소비자별 인수 별도 |
| Trivy 운영 | 검토 버전/SHA 고정·관리자 교체, Scan 전 DB 갱신 필요·유효성 검사, 오류 fail-closed | latest 자기 갱신·오래된 DB fallback·임의 유예기간 도입 없음 |
| ICR 단순화 | 기존 증적 재사용, 도구 qualification과 운영 보완 분리, 인수/영수증 연결 | 추가 VM 반복 시험·광역 허용·CP1/CP2/CP3 인수 예외 자동 승인 없음 |

근거: [PR72](https://github.com/321Team/fds-project-baseline/pull/72), [#28](https://github.com/321Team/fds-project-baseline/issues/28), [#78](https://github.com/321Team/fds-project-baseline/issues/78), [Lead 결정](https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-5697547621), [Harbor 결정](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5659049448), [CI 결정](https://github.com/321Team/fds-project-baseline/issues/16#issuecomment-5659051242). 세부 수집 문서 및 원문은 audit/v3.1.19/intake와 tickets/v3.1.19/sources에 보존한다.

## 승인·관측·보류 분류

APPROVED_INPUT은 확인된 사용자/Lead 결정의 명시 범위만 뜻한다. GitHub의 Merged는 코드 편입 사실이며 Runtime 인수가 아니다. PENDING_REVIEW/INPUT_INCOMPLETE 및 합성 시험·제출 영수증 검증은 그대로 표시한다. GitHub ticket lifecycle과 원문 체크상태를 보존했으며 이번 작업에서 운영 AC를 새로 체크하지 않았다. 새 D/IF 순번은 임의 발급하지 않고 DEC-P1-EGRESS-01·CR Record ID로 추적한다.

<details>
<summary>v3.1~v3.1.17 변경 이력 — 당시 상태</summary>

v3.1은 v3.0의 Kubernetes 중심 구조를 유지하면서, **3인·3주 실습에 맞게 Phase 1 P0 범위를 축소**하고 신규 Physical Network 정보를 반영한 Minor Release다.

v3.1.2는 D-NET-01과 P1-LNX-01 검증 결과를 반영한 Network Design Freeze다. Windows server01~08 PostBuild, Linux Network Baseline, Physical Return Route, Management Source 보존을 완료했으며 Kubernetes 서비스 구축은 `P1-K8S-01`로 분리한다.

v3.1.3은 2026-08-26 공통 백로그 검토 결과를 반영한 Governance Correction Release다. `D-ARC-01`, `D-NET-01`, `D-WBS-01`, `P1-LNX-01`은 종결 상태를 유지하고 Remaining Backlog에서 제외한다. `D-SEC-01`의 기존 `DONE` 판정과 임의 담당자 지정을 취소하고 `Decision / IN REVIEW / Lead TBD`로 전환한다. 이에 따라 G0 Design Freeze는 Security Ownership/Scope 결정 전까지 `CONDITIONAL PASS`로 정정한다.

v3.1.4는 D-SEC-01 담당 및 진행상태 확정 결과를 반영한 Assignment Correction Release다. `D-SEC-01` Lead는 `이하영`, 상태는 `IN PROGRESS`로 변경한다. 담당자 지정은 완료되었으나 승인권자, 검토 범위, 산출물, Exit Criteria 및 P1-SEC-01 경계에 대한 D17 검토는 진행 중이므로 G0 Design Freeze는 `CONDITIONAL PASS`를 유지한다.

v3.1.5는 2026-08-27 전수 백로그 대조 결과를 반영한 Backlog Integrity Correction Release다. `P1-ANS-01`, `P1-HA-02`, `P1-DR-02`, `P1-MON-02`, `P2-ARC-01`, `P2-CICD-01`을 복원·통합하고, `DEC-P2-OP-01`, `P2-OP-01`, `P2-DNS-01`의 조건부 추적성을 추가한다. `P1-NET-01`은 수행 증적에 따라 Closed Register에 보정한다. 담당·지원·검토 인명은 이권욱·이하영·이재환의 풀네임으로 표준화한다. D17이 진행 중이므로 G0는 `CONDITIONAL PASS`를 유지한다.

v3.1.6은 2026-08-28 `DEC-P1-ENTRY-01` 의존성 검토 결과를 반영한 Dependency Correction Release다. Application External Entry `.50:80/443 → transaction-api`와 Kubernetes API LB `.109:6443 → CP .102~.104:6443`를 분리하고, `DEC-P1-ENTRY-01/D18`을 `P1-LB-01` 및 `P1-K8S-01`의 직접 선행조건에서 제거한다. API LB는 Stage A Listener Ready 후 Cluster Bootstrap을 해제하고, CP API 기동 후 Stage B Health/Failover 검증으로 종결한다. `D-SEC-01/D17`은 미종결 상태를 유지하며 `P1-SEC-01`과 G2의 선행조건으로 관리한다. 변경 추적 Decision은 `D27`이다.

v3.1.7은 Ticket Lifecycle / Review Status Correction Release다. 모든 티켓 상태를 `To Do → In Progress → In Review → Done` 또는 `Cancelled`로 표준화하고, 테크니션 리뷰를 포함한 모든 리뷰 단계는 `In Review`로 통일한다. `P1-ANS-01`은 2026-08-28 기술 검증을 PASS했으나 Support의 단위 테스트 결과·영향성 검토와 잔여 통제가 열려 있으므로 `In Review`로 보정한다. `D-SEC-01/D17`도 미종결 리뷰 작업이므로 `In Review`로 전환한다. 본 릴리즈는 아직 현업에 배포되지 않은 준비본이며, D28과 릴리즈 노트 승인 후 배포한다.

v3.1.8은 Decision Review / Canonical Distribution Release다. `DEC-P1-ENTRY-01/D18`과 `DEC-P1-TLS-01/D19`를 `In Review`로 동기화하고, Master WBS·Notion 입력본·Decision 정본의 상태와 Source를 일치시킨다. 6개 Kubernetes 예정 노드의 현재 `firewalld`와 Cockpit Listener를 대조해 NodePort 30080 미구현, Host Egress Allowlist 미구현, Cockpit `*:9090` 관리 필요를 Handoff 조건으로 기록한다. v3.1.6과 v3.1.7이 현업에 실제 배포되지 않았다는 사실을 반영해 두 버전의 릴리즈 노트를 소급 작성하고, 이번 v3.1.8 정본과 함께 배포한다. 변경 추적 Decision은 `D29`다.

v3.1.9는 Phase 1 Status Activation Release다. 2026-08-28 착수 지시에 따라 `P1-LB-01`, `P1-DNS-01`, `P1-DB-01`, `P1-APP-01`, `P1-MON-01`을 `In Progress`로 동기화한다. `P1-APP-01`은 Interface/Schema, `P1-MON-01`은 Metrics/Target 설계의 조기 착수이며 각 통합 선행조건은 유지한다. 요청된 `MS-G0-01`은 v3.1.8 Remaining Backlog에 존재하지 않으므로 신규 레코드를 임의 생성하지 않고, 기존 `G0 Design Freeze`를 `CONDITIONAL PASS`로 유지한다. 변경 추적 Decision은 `D30`이다.

v3.1.10은 P1-ANS-01 Closure / Kubernetes Handoff Release다. 2026-08-31 Reviewer·Approver 이하영의 명시적 검토 결과에 따라 `HO-ANS-08=PASS`, `HO-ANS-09=PASS`를 기록하고 `P1-ANS-01`을 `Done`으로 종결한다. 미구현 Kubernetes 통제인 `HO-ANS-01~04`는 완료로 간주하지 않고 `P1-K8S-01`, `P1-SEC-01`, `P1-LB-01`, `P1-APP-01`의 Acceptance·Schedule Note로 분리 이관한다. 실제 Ansible Repository에는 승인본 `05h`, `05j`를 배치한 뒤 `99_SHA256SUMS.txt`를 재생성·검증해야 하며, 이 배포 작업은 승인 판정과 구분해 추적한다. 변경 추적 Decision은 `D31`이다.

v3.1.11은 DEC-P1-ENTRY-01 / DEC-P1-TLS-01 Approval Closure Release다. 2026-08-31 `DEC-P1-ENTRY-01/D18`은 Reviewer 이하영·Approver 이권욱의 `PASS`, `DEC-P1-TLS-01/D19`는 Reviewer·Approver 이하영의 `PASS`로 승인되어 두 Decision Ticket을 `Done`으로 종결한다. D18은 HAProxy + 접근 제한 NodePort와 `externalTrafficPolicy: Local`을, D19는 프로젝트 Private Root CA + Harbor/edge01 서비스별 Leaf + Consumer CA Trust를 고정한다. 실제 Manifest 적용, 인증서 배포 및 Push/Pull Runtime Test 완료 여부는 P1-APP-01·P1-SEC-01·P1-HBR-01·P1-CICD-01에서 별도 판정하며 G1/G2 완료를 자동 선언하지 않는다.

v3.1.12는 MS-G0-01 Backlog Registration Release다. 2026-08-31 사용자 승인에 따라 과거 미등록 상태였던 `MS-G0-01 — G0 Design Freeze`를 Remaining Backlog와 Decision/Milestone Register에 정식 등록한다. Milestone Lifecycle Status는 `In Progress`, Gate 판정은 `CONDITIONAL PASS`로 분리한다. `D-ARC-01`, `D-NET-01`, `D-WBS-01`은 Done이나 `D-SEC-01/D17`이 `Revision Required / In Review`이므로 Full PASS와 Done은 선언하지 않는다. 변경 추적 Decision은 `D32`다.

v3.1.13은 Kubernetes-Integrated Hybrid Monitoring Architecture Release다. 2026-08-31 사용자 승인에 따라 Grafana를 Phase 1 P0에 포함하고, Prometheus·kube-state-metrics·Alertmanager·Grafana는 Kubernetes `monitoring-api` Namespace에 배치한다. node-exporter는 `monitoring-node` Namespace의 통제된 PSA Privileged 예외로 분리하며, `monitor01(.30)`은 폐기하지 않고 외부 Prometheus·Blackbox Exporter 기반의 독립 Watchdog 및 선택 메트릭 증적 보관 역할로 전환한다. In-cluster Prometheus의 heartbeat를 `monitor01`로 제한적 `remote_write`하여 클러스터 내부 모니터링 중단을 외부에서 탐지한다. Grafana는 `ClusterIP`만 사용하고 승인된 관리 단말의 `kubectl port-forward`로만 접근한다. 설계 Decision은 `DEC-P1-MON-01/D33`으로 고정하되, 실제 배포·Scrape·Alert·장애탐지 Evidence 전에는 `P1-MON-01`을 `In Progress`로 유지한다. D17과 `D-SEC-01`은 본 변경으로 자동 종결하지 않는다.

v3.1.14는 D-SEC-01 Security Design Approval / Kubernetes Host Protection Release다. 2026-09-01 Project Lead 이권욱의 승인에 따라 D-SEC-01/D17의 Scope·예외·P1-SEC-01 경계·Exit Criteria를 확정하고 D-SEC-01과 MS-G0-01을 `Done`, G0를 `FULL PASS`로 종결한다. Kubernetes 6개 Node의 `firewalld`는 Calico 설치 전에 비활성화하고 Host 보호는 named HostEndpoint와 GlobalNetworkPolicy로 통일한다. Calico 초기값은 `BGP Disabled + VXLANCrossSubnet + natOutgoing=true`이며 실제 경로 시험 실패 시 Change Control을 거쳐 VXLAN Always로 전환한다. `kube-system`은 Namespace 단위 PSA 제약에 따라 `enforce=privileged`, `audit/warn=restricted`를 적용하고 CoreDNS는 별도 Manifest 하드닝과 dry-run으로 검증한다. D33의 IF-06B Remote Write를 유지하고 IF-24 Webhook은 P1 N/A로 정리한다. Monitoring static local PV와 Secret at-rest encryption을 Runtime 선행조건으로 추가한다. 변경 추적 Decision은 `D34`다.

v3.1.15는 Interface Contract Integrity / IF-11A Approval Release다. 2026-09-02 `FDS_Interface_Full_Audit_v3.1.14_R1` 전수 점검과 이하영의 IF-11A 승인, Project Lead 이권욱의 정본 발행 승인을 반영한다. IF-11A `Kubernetes Node 6대 → API LB .109:6443`를 동결하고, IF-06A `monitor01 .30 → API LB .109:6443`를 API LB Source Allowlist에서 보존한다. D-SEC-01·P1-K8S-01에 이미 승인된 Prometheus→Alertmanager 9093, Workload→CoreDNS 53, etcd 2379~2380, Control Plane→kubelet 10250, Node 간 VXLAN 4789 계약을 Register에 추가한다. ICR의 IF-21/22와 IF-23 Prometheus 부분은 기존 IF-02/IF-06에 병합하며 IF-24 Webhook은 RETIRED/P1 N/A로 고정한다. 설계 상태와 Runtime Evidence 상태를 분리하고 Phase 2 미확정 IF-17~20은 PROVISIONAL로 정정한다. P1-HBR-01을 Project Status Register에 복원한다. 변경 추적 Decision은 `D35`다.

v3.1.16은 Team Availability / Phase 1 Schedule & Status Update Release다. 2026-09-03 사용자 승인에 따라 이재환의 2026-09-04 개인 사정 휴가를 개인 부재로 등록하고 전사 Non-working Date와 분리한다. 단독 Lead 종료를 휴가일에 배치하지 않는 원칙에 따라 `P1-DB-01`과 `MS-G1-01`을 09-07로, `P1-APP-01` 종료를 09-10으로, `P1-MON-01` 착수를 09-07로 조정한다. `G2 09-11`, `G3 09-18`, `Phase 1 Close 09-23`은 유지한다. 실행 상태는 `P1-DNS-01=Done`, `P1-K8S-01=In Progress`, `P1-LB-01=In Progress(Stage A Technical/Evidence PASS, Stage B Pending)`으로 동기화한다. 변경 추적 Decision은 `D36`이다.

v3.1.17은 GitHub Canonical Baseline Repository / Integrity Correction Release Candidate다. 2026-09-04 사용자 승인에 따라 개발 저장소와 분리된 Private 정본 저장소 `321Team/fds-project-baseline`을 사용하고, `main`은 승인된 정본만 수용하며 `release/v3.1.17`과 Pull Request로 발행을 통제한다. v3.1.15·v3.1.16 이력을 저장소에 보존하고 WBS의 `KW LEE/KW-HY LEE` 표기를 `GU LEE/GU-HY LEE`로, P1-K8S Source를 Preflight v1.1로, ICR Source를 v1.4로 정정한다. `P1-LB-01` Stage B 목표는 승인된 D36 G1 목표와 정렬해 2026-09-07로 재기준선화하되 Runtime PASS 전에는 `In Progress`를 유지한다. `CR-P1-ANS-01-01`은 `infra-ansible` PR #1의 Reviewer 요청까지 확인된 `In Review`이며 Merge·CI·Runtime 완료로 간주하지 않는다. 변경 추적 Decision은 `D37`이다.


</details>

## 0.1 Configuration-controlled Deliverables

| Deliverable | Version | Status | Freeze Ticket |
|---|---|---|---|
| `FDS_Project_Implementation_Baseline_v3.1.19.md` | v3.1.19 | RELEASED / FINALIZATION | v3.1.19 누적 변경 통합 / PR #73 승인·내용 병합 완료 |
| `D37_GitHub_Canonical_Baseline_Repository_and_v3.1.17_Release_Record_v1.0.md` | v1.0 | APPROVED / RELEASED | PR #1 approved and merged; finalization metadata synchronized |
| `FDS_v3.1.19_WBS_and_Gantt_v1.0.xlsx` | v1.0 | RELEASED / FINALIZATION | v3.1.19 상태·58건 집계·가용일 정합성 |
| `FDS_v3.1.19_Canonical_Ticket_Update_Pack_v1.0.md` | v1.0 | RELEASED / FINALIZATION | v3.1.19 Description 후보 / 발행 후 적용 |
| `FDS_Project_Implementation_Baseline_Release_Notes_v3.1.19.md` | v3.1.19 | RELEASED / FINALIZATION | v3.1.19 통합 변경 |
| `FDS_Document_Distribution_Manifest_v3.1.19.md` | v3.1.19 | RELEASED / FINALIZATION | v3.1.19 배포 무결성 |
| `FDS_v3.1.19_Canonical_Status.html` | v3.1.19 | RELEASED / FINALIZATION | v3.1.19 현재 상태 스냅샷 |
| `FDS_Project_Implementation_Baseline_v3.1.16.md` | v3.1.16 | SUPERSEDED | D36 / Team Availability / Phase 1 Schedule & Status Update |
| `D36_Team_Availability_and_Status_Update_Record_v1.0.md` | v1.0 | APPROVED | 09-04 이재환 개인 휴가 / 연동 일정 / 상태 동기화 |
| `FDS_v3.1.16_WBS_and_Gantt_v1.0.xlsx` | v1.0 | RELEASED | D36 / WBS·Gantt·Team Calendar |
| `FDS_v3.1.16_Canonical_Ticket_Update_Pack_v1.0.md` | v1.0 | RELEASED | D36 / Notion Upsert Source |
| `FDS_Project_Implementation_Baseline_Release_Notes_v3.1.16.md` | v3.1.16 | RELEASED | D36 |
| `FDS_Document_Distribution_Manifest_v3.1.16.md` | v3.1.16 | RELEASED | D36 / Canonical File Integrity |
| `FDS_Project_Implementation_Baseline_v3.1.15.md` | v3.1.15 | SUPERSEDED | v3.1.16 정본으로 대체; D35 이력 보존 |
| `D35_Interface_Register_Correction_and_IF-11A_Approval_Record_v1.0.md` | v1.0 | APPROVED | 이하영 IF-11A 승인 / 이권욱 정본 발행 승인 |
| `FDS_Interface_Full_Audit_v3.1.14_R1.md` | R1 | APPROVED REVIEW BASIS | D35 / Interface 전수 점검 |
| `FDS_IF-11A_Ticket_Impact_and_Verification_Record_v1.1.md` | v1.1 | APPROVED / RUNTIME PENDING | D35 / 티켓별 영향·검증 주체 |
| `ICR-D-NET-01-01_Kubernetes_Node_Host_Firewall_및_Monitoring_Route_변경요청_v1.4.md` | v1.4 | APPROVED / IN PROGRESS | D35 / IF 중복 제거 및 정본 매핑 |
| `FDS_P1-LB-01_Stage_A_Build_Guide_v1.3.md` | v1.3 | RELEASED | D35 / IF-11A 승인 및 IF-06A 보존 |
| `P1-LB-01_Stage_A_Completion_Pack_v1.1.zip` | v1.1 | RELEASED | D35 / Source Allowlist·Evidence 실행 팩 |
| `FDS_v3.1.15_Canonical_Ticket_Update_Pack_v1.0.md` | v1.0 | SUPERSEDED | v3.1.16 Ticket Update Pack 우선; D35 이력 보존 |
| `FDS_Project_Implementation_Baseline_Release_Notes_v3.1.15.md` | v3.1.15 | RELEASED | D35 |
| `FDS_Document_Distribution_Manifest_v3.1.15.md` | v3.1.15 | RELEASED | D35 / Canonical File Integrity |
| `FDS_Project_Implementation_Baseline_v3.1.14.md` | v3.1.14 | SUPERSEDED | v3.1.15 정본으로 대체; 이력 보존 |
| `D-SEC-01_Kubernetes_Security_Design_Baseline_v1.0.md` | v1.0 | APPROVED | D17 / D34 |
| `D34_D-SEC-01_Approval_and_Disposition_Record_v1.0.md` | v1.0 | APPROVED | Project Lead 승인·리뷰 조치 증적 |
| `ICR-D-NET-01-01_Kubernetes_Node_Host_Firewall_및_Monitoring_Route_변경요청_v1.3.md` | v1.3 | SUPERSEDED | v1.4로 대체; 이력 보존 |
| `FDS_P1-K8S-01_Preflight_Review_v1.1.md` | v1.1 | APPROVED / RUNTIME CONDITIONAL | D34 / P1-LB-01 Stage A 선행 |
| `P1-MON-01_Notion_Description_UserStory_v1.2.md` | v1.2 | RELEASED / RUNTIME CONDITIONAL | D33 / D34 |
| `FDS_P1-LB-01_Stage_A_Build_Guide_v1.2.md` | v1.2 | SUPERSEDED | v1.3으로 대체; 이력 보존 |
| `P1-DNS-01_Notion_Description_v1.1.md` | v1.1 | SUPERSEDED FOR STATUS | v3.1.16 Ticket Update Pack의 `Done` 판정 우선 |
| `FDS_v3.1.14_Canonical_Ticket_Update_Pack_v1.0.md` | v1.0 | SUPERSEDED | v3.1.15 Ticket Update Pack 우선 |
| `FDS_Project_Implementation_Baseline_Release_Notes_v3.1.14.md` | v3.1.14 | RELEASED | D34 |
| `FDS_Document_Distribution_Manifest_v3.1.14.md` | v3.1.14 | RELEASED | D34 / Canonical File Integrity |
| `FDS_Network_Baseline_v2.3.md` | v2.3 | APPROVED | D-NET-01 |
| `FDS_Phase1_Logical_Architecture_v3.1.3.mmd` | v3.1.3 | RELEASED | D33 Monitoring Architecture Change |
| `FDS_Phase1_Physical_Architecture_v3.1.3.mmd` | v3.1.3 | RELEASED | D33 Monitoring Placement Change |
| `FDS_Remaining_Backlog_WBS_v3.1.12.xlsx` | v3.1.12 | RELEASED | MS-G0-01 / D32 / Gate Status Control |
| `FDS_Notion_Remaining_Backlog_Manual_v1.9.md` | v1.9 | SUPERSEDED FOR AFFECTED TICKETS | v3.1.15 Ticket Update Pack 우선 |
| `FDS_Notion_Remaining_Backlog_Descriptions_v1.8.md` | v1.8 | RELEASED | MS-G0-01 Page Body Description 포함 |
| `FDS_Notion_Remaining_Backlog_Properties_v1.8.csv` | v1.8 | RELEASED | MS-G0-01 속성 포함 / WBS v3.1.12 동기화 |
| `FDS_Notion_Technical_PASS_P1-ANS-01_v1.3.md` | v1.3 | RELEASED | P1-ANS-01 Approved Closure / Done |
| `FDS_P1-ANS-01_SSH_Control_Release_Notes_v1.3.md` | v1.3 | RELEASED | HO-ANS-08·09 PASS / Closure Record |
| `FDS_Ticket_Lifecycle_Review_Correction_v1.0.md` | v1.0 | RELEASED | D28 Governance Control |
| `FDS_Ticket_Lifecycle_Review_Correction_Release_Notes_v3.1.7.md` | v3.1.7 | RELEASED | Mandatory Release Notes |
| `FDS_Project_Implementation_Baseline_Release_Notes_v3.1.6.md` | v3.1.6 | RELEASED | Backfilled Release Notes |
| `FDS_Project_Implementation_Baseline_Release_Notes_v3.1.7.md` | v3.1.7 | RELEASED | Backfilled Release Notes |
| `FDS_Project_Implementation_Baseline_Release_Notes_v3.1.8.md` | v3.1.8 | RELEASED | Previous Release Notes |
| `FDS_Project_Implementation_Baseline_Release_Notes_v3.1.9.md` | v3.1.9 | RELEASED | Previous Release Notes |
| `FDS_Project_Implementation_Baseline_Release_Notes_v3.1.10.md` | v3.1.10 | RELEASED | Previous Release Notes |
| `FDS_Project_Implementation_Baseline_Release_Notes_v3.1.11.md` | v3.1.11 | RELEASED | Previous Release Notes |
| `FDS_Project_Implementation_Baseline_Release_Notes_v3.1.12.md` | v3.1.12 | RELEASED | Previous Release Notes |
| `FDS_Project_Implementation_Baseline_Release_Notes_v3.1.13.md` | v3.1.13 | RELEASED | Previous Release Notes |
| `DEC-P1-MON-01_Notion_Description_UserStory_v1.0.md` | v1.0 | RELEASED | D33 Hybrid Monitoring Decision |
| `P1-MON-01_Notion_Description_UserStory_v1.0.md` | v1.0 | SUPERSEDED | v1.2 정본으로 대체 |
| `FDS_D-SEC-01_Monitoring_System_Exception_Addendum_v1.0.md` | v1.0 | RELEASED | monitoring-node Controlled Exception |
| `DEC-P1-ENTRY-01_Notion_Description_UserStory.md` | v1.0 | RELEASED | D18 PASS / Done |
| `DEC-P1-TLS-01_Notion_Description_UserStory_v1.1.md` | v1.1 | RELEASED | D19 PASS / Done |
| `FDS_Project_Implementation_Baseline_Cumulative_Release_Notes_v3.1.6_to_v3.1.13.md` | v3.1.13 | RELEASED | Cumulative Distribution History |
| `FDS_Document_Distribution_Manifest_v3.1.10.md` | v3.1.10 | RELEASED | Previous Canonical File Integrity |
| `FDS_Document_Distribution_Manifest_v3.1.11.md` | v3.1.11 | RELEASED | Previous Canonical File Integrity |
| `FDS_Document_Distribution_Manifest_v3.1.12.md` | v3.1.12 | RELEASED | Canonical File Integrity / Receipt Pending |
| `FDS_Document_Distribution_Manifest_v3.1.13.md` | v3.1.13 | RELEASED | Canonical File Integrity / Receipt Pending |
| `FDS_Backlog_Integrity_Correction_Release_Notes_v3.1.5.md` | v3.1.5 | APPROVED | Distribution / Change Control |
| `FDS_DEC-P1-ENTRY-01_Dependency_Correction_v1.0.md` | v1.0 | APPROVED | D27 Dependency Correction / Distribution |

Freeze 이후 P0 범위, IP, 배치, 인터페이스, 일정 또는 Exit Criteria 변경은 Change Request와 영향도 검토를 거쳐야 한다.

| 영역 | v3.0 | v3.1 |
|---|---|---|
| Phase 1 App | FastAPI/FDS 통합 표현 | **transaction-api + fds-engine 2개 Microservice** |
| Phase 1 성공 기준 | 플랫폼/HA 항목 다수 P0 | **거래→FDS→DB→Monitoring 핵심 E2E 중심** |
| HA P0 | Worker Drain, Rolling Update, CP 장애 | **Worker Drain만 P0** |
| Backup P0 | DB + Harbor/Source | **PostgreSQL Restore만 P0** |
| DNS | 미정/추가 검토 | **Primary/Secondary BIND P1, G1 비차단** |
| Node/Service IP | `.100~.109` 전제 | **사용 불가 `.100/.101/.106` 반영** |
| Windows Host IP | 기존 계획 주소 | **현장 Fixed IP `.22~.31` 반영** |
| Harbor/DB | Private subnet 중심 | **Bridged Service IP + Host Firewall Allowlist** |
| Hybrid DNS | 미정 | **P0는 IP Endpoint, Hybrid DNS는 P1** |

---

# 1. 프로젝트 목표와 범위

## 1.1 Phase 1 목표

VMware와 CentOS Stream 10 기반 On-Premises 환경에 3 Control Plane + 3 Worker Kubernetes Cluster를 구축하고 다음 핵심 흐름을 완성한다.

```text
Git Commit
  → GitHub Actions / Self-hosted Runner
  → Build / Test / Trivy
  → Harbor
  → Kubernetes Deploy
  → Client / edge01
  → transaction-api
  → fds-engine
  → PostgreSQL
  → In-cluster Prometheus
  → Grafana / Alertmanager
  → monitor01 External Watchdog / Evidence
```

### Phase 1 P0 성공 조건

1. `transaction-api`와 `fds-engine`을 별도 Deployment/Service로 운영
2. R01/R02/R04/R07 Rule 동작
3. Transaction 및 FDS Result PostgreSQL 저장
4. Default Deny + Required Allowlist + RBAC + SecurityContext/seccomp 적용
5. GitHub Actions → Harbor → Kubernetes 배포
6. Prometheus에서 핵심 거래/FDS/상태 지표를 확인하고 Grafana 기본 Dashboard와 Alertmanager Firing/Resolved 흐름 검증
7. Worker Drain 중 서비스 지속
8. PostgreSQL Backup/Restore 후 E2E 재검증
9. Evidence와 기본 구축/복구 Runbook 확보

## 1.2 Phase 1 P1

- Primary/Secondary Infrastructure DNS
- Rolling Update 검증
- Control Plane 1대 장애 검증
- PDB / TopologySpreadConstraint
- Harbor 실제 Restore
- etcd Snapshot/Restore
- Prometheus 2 Replica / Alertmanager 3 Replica 기반 Monitoring HA
- Dashboard/Alert 고도화 및 장기 보존·Remote Storage 검토
- DNS TSIG/Failover 심화 검증

P1 추적 티켓:

- `P1-DNS-01`: Primary/Secondary DNS + TSIG/Failover
- `P1-HA-02`: Rolling Update + Control Plane 1대 장애 + PDB/TopologySpreadConstraint
- `P1-DR-02`: Harbor Backup/Restore + etcd Snapshot/Restore
- `P1-MON-02`: Monitoring HA + Dashboard/Alert 고도화 + 장기 보존

P1 미완료는 Gate를 차단하지 않지만 풀네임 Owner, Due, Known Issue와 Evidence 경로를 반드시 유지한다.

## 1.3 Phase 1 Scope Out

- Istio / Service Mesh
- Kata Containers
- AI Inference
- PostgreSQL HA
- Harbor HA
- Loki/SIEM 통합
- WAF
- DNSSEC
- Authoritative/Recursive DNS 완전 분리
- Route 53 Resolver 기반 Hybrid DNS
- 다중 DR Site

## 1.4 Phase 2 목표

Terraform으로 AWS/ROSA 기반 Infrastructure를 구축하고, OCI VPN Relay를 Primary Transit으로 사용하여 On-Prem과 AWS Site-to-Site VPN을 연계한다. 동일한 `transaction-api`와 `fds-engine`을 ROSA에 배포하고 On-Prem PostgreSQL과 Hybrid E2E를 검증한다. Phase 2 구현 전 `P2-ARC-01`로 설계를 동결하고 `P2-CICD-01`로 Runner 기반 ROSA Delivery를 검증한다.

---

# 2. 일정 / 인력 Baseline

| 구분 | 날짜 |
|---|---|
| 프로젝트 착수 | 2026-08-24 |
| `MS-G0-01` / G0 Design Freeze | 09-01 — **Done / FULL PASS** (`D-SEC-01/D17`, `D34` PASS) |
| G1 Infrastructure Ready | 09-17 오후 — Fast Tracking 권장안 |
| G2 Security / Feature Ready | 09-21 오후 — 권장안 |
| G3 Review Ready Freeze | 09-22 오전 — 권장안 |
| Phase 1 Review | 09-22 오후 — 평일 권장안 |
| Phase 1 Close | 09-23 |
| Phase 2 Start | 09-28 |
| OCI Go/No-Go | 10-02 |
| G4 Cloud / VPN Ready | 10-08 |
| G5 ROSA Application Ready | 10-16 |
| G6 Hybrid Integration Ready | 10-22 |
| Deliverable Freeze | 10-23 |
| Phase 2 Review | 10-23 오후 — 평일 권장안 |
| Project Close | 10-26 |

### Non-working / Absence

- 이하영: 08-28 시험 휴가, 09-08 면접 휴가(개인 부재, 이권욱 지원), 09-10 면접 휴가(사용자 추가 지시)
- 이재환: 09-04 개인 사정 휴가, 09-14 ~ 09-17 예비군
- Non-working: 09-24 ~ 09-25, 10-05, 10-09

개인 휴가는 해당 담당자의 가용일에서만 제외하며 전사 Non-working Date로 취급하지 않는다. 휴가/비근무일에는 Critical Task의 단독 담당 완료일을 배치하지 않는다. WBS의 `Lead Workdays`는 전사 비근무일과 해당 Lead의 개인 부재를 제외해 산정한다. 2026-09-08 및 2026-09-10 개인 부재는 해당 Lead의 가용일에서 제외하며 Start/End를 자동 변경하지 않는다. 실제 지연·미완료는 별도 Lead 판단 대상으로 기록한다. 2026-09-04 부재 영향은 `P1-DB-01`, `P1-APP-01`, `P1-MON-01`, `MS-G1-01`에만 적용하며 다른 담당자의 작업일은 유지한다.

---

# 3. 3인 업무분장

| 담당 | Primary Domain | 주요 책임 |
|---|---|---|
| 이권욱 | Infrastructure / Network / Automation / Cloud IaC | 8대 Windows Host/VMware, Physical IP, Bridged Network, API LB, CentOS 10, Ansible, Runner, Terraform, OCI/AWS |
| 이하영 | Kubernetes / Container Security / Registry / OpenShift | 3CP+3Worker, containerd, Calico, Namespace, NetworkPolicy, RBAC, Pod Security, Harbor/Trivy, ROSA/OADP |
| 이재환 | Application / Data / Monitoring / QA | transaction-api, fds-engine, PostgreSQL, Prometheus/App Metrics, E2E, Worker Drain, DB Restore |

## 3.1 Closed Ticket Register / Remaining Backlog Authority

종결 티켓은 Remaining Backlog에서 제외한다.

| ID | Status | Closed Date | Basis |
| --- | --- | --- | --- |
| DEC-P1-FDS-01 | Done | 2026-09-09 | 2026-09-09 Decision Done. A 선택: 기존 탐지·기록·관측 유지. 별도 발표 프론트엔드, 거래 보류·해제·거절·운영 UI 확대는 미도입/유예. Runtime 및 G2 완료 승인이 아니다. |
| DEC-P1-TXN-01 | Done | 2026-09-09 | 2026-09-09 Decision Done. C 선택: 기존 API·DB 계약 유지. 보류용 상태·API·Migration을 추가하지 않는다. 기존 Schema drift, 소스·배포 SHA 및 실패 응답 검증은 P1-APP/DB/E2E에서 계속 수행한다. |
| DEC-P1-ADMIN-01 | Done | 2026-09-09 | 2026-09-09 Decision Done. 기존 Grafana 관측·합성 데이터 시연으로 범위를 한정했다. 새 업무 역할·2인 승인·세션 수명·관리 감사 정책값은 유예. OID-01 Source/Identity와 기존 보안 부정시험은 유지한다. |
| D-SEC-01 | Done | 2026-09-01 | 승인권자 지정, D-SEC-01 검토 범위·산출물·Exit Criteria 승인, P1-SEC-01과의 경계 승인, 요구사항과 검증 증적 연결 후 Done 판정 |
| MS-G0-01 | Done | 2026-09-01 | D-ARC-01·D-NET-01·D-WBS-01·D-SEC-01 승인과 정본 Evidence를 확인하고 G0 FULL PASS 기록 확보 |
| P1-DNS-01 | Done | 2026-09-03 | Primary/Secondary·TSIG·제한 Query/Recursion·Failover Evidence와 k8s-api-lb01 `.109` Resolver/ACL/IPSet 검증 및 Support Review 승인 |
| CR-P1-ANS-01-01 | Done | 2026-09-07 | 2026-09-07 CR 최종 승인·병합 완료. 승인 HEAD 507d8882a04f53640b07251bcc234b7d6ee81c09, merge 4f9bdb7c08704eebb3d1b294751e51b0721b6af4, AC 11/11은 당시 실행·Support 승인 기록에 근거한다. CI NOT RUN. FUP-01 원본 보완·독립 편입과 증적 PR #1 병합은 완료됐으며 Stage A 조건부 인수의 잔여 조건, Bootstrap 해제·Stage B는 별도다. |
| D-ARC-01 | Done | 2026-08-26 | D-ARC-01 Done/2026-08-26 유지. FUP-06 후보 원본 편입과 수용은 완료됐으나 개인별 과거 승인 회신·시각 참조 한계는 유지한다. PR #72의 복원 속성과 사용자 정정 End 2026-08-26·기간 3일을 적용한다. |
| D-NET-01 | Done | 2026-08-26 | D-NET-01 Done/2026-08-26 유지. 기존 종결 문서와 일부 8/28 보완 원본은 매핑 후보로 연결됐으나 FUP-04 최초 로그·Windows/VMware·관리 경로 전문은 잔여다. 8/28 자료를 8/26 최초 증적으로 소급하지 않는다. |
| D-WBS-01 | Done | 2026-08-26 | D-WBS-01 Done/2026-08-26 유지. FUP-07 WBS 참조 편입은 완료됐으나 당시 개인별 승인 회신·시각 및 WBS 바이너리 실제 열람 확인은 잔여다. PR #72의 복원 속성과 사용자 확정 완료일 2026-08-26을 적용하며 기존 승인 범위를 확대하지 않는다. |
| DEC-P1-ENTRY-01 | Done | 2026-08-31 | edge01→transaction-api 노출 방식을 Ingress/Reverse Proxy/NodePort 후보 중 확정하고 Port·Health Check·Firewall·NetworkPolicy 변경을 승인 |
| DEC-P1-MON-01 | Done | 2026-08-31 | D33 Done/2026-08-31 및 현행 Hybrid Monitoring 설계를 유지한다. FUP-08 원본 수신·Hash·독립 승인·main 편입은 완료됐고 과거 비교 Hash 부재의 수용된 한계는 유지한다. P1-MON-01 Runtime과 P1-MON-02 고도화는 별도다. |
| DEC-P1-TLS-01 | Done | 2026-08-31 | Harbor와 edge01의 인증서 발급·SAN·CA Trust 배포·갱신·Rollback 방식을 확정하고 Consumer별 검증방법 승인 |
| P1-ANS-01 | Done | 2026-08-31 | P1-ANS-01 원 종결(2026-08-31, HO-ANS-08/09 PASS)은 유지한다. 후속 SSH 검증식 PR #4는 5a2c3786f6af9f107200654aa12c92c3b09700f0에서 승인되고 3a02dc8934adb1f80df48ec6763689c401a1e8d6로 병합됐다. 운영 Issue #10은 6대 apply·멱등성·SFTP 확인과 독립 승인 후 종결. Gate 0 도구 PR #3 merge 5cbf3b657014b32a20cb5816d90d3ea5fe4951ab는 코드 편입이며 6대 Cluster 완료가 아니다. 2.21.3 엔진 전환 Issue #9와 NTP 목적지 승인·재검증은 잔여다. |
| P1-LNX-01 | Done | 2026-08-26 | P1-LNX-01 원 종결과 당시 PASS는 유지한다. FUP-04의 일부 원본 수신 한계 및 이후 Runtime drift 검증을 원 종결과 구분한다. |
| P1-NET-01 | Done | 2026-08-26 | P1-NET-01 원 종결과 당시 Source Preservation PASS는 유지한다. FUP-04 일부 최초 원본과 FUP-05 당시 Reviewer/Approver·시각 참조는 잔여이며 새 승인자를 생성하지 않는다. |

| DEC-CAL-P1-01 | Done | 2026-09-16 | 09-22 오후 Review 일정 결정 종결. 실제 Review 실행·Gate 승인 별도. |
| DEC-P1-EGRESS-01 | Done | 2026-09-16 | .56 프록시 배치·정책·자원 영향·#74/#75 인계 결정 종결. 구현·Runtime 별도. |

Remaining Backlog의 권위 Source는 다음 파일이다.

- `FDS_v3.1.19_WBS_and_Gantt_v1.0.xlsx`: 이 후보의 일정·Team Calendar·Decision/Milestone·Risk·Status. 58개 일정관리 레코드
- `FDS_v3.1.19_Canonical_Ticket_Update_Pack_v1.0.md`: 67개 티켓의 속성·현재 Description·Gate·Handoff 통합 후보
- `FDS_Remaining_Backlog_WBS_v3.1.12.xlsx`: D36 비영향 기존 속성·일정의 역사적 Schedule Base
- `FDS_Notion_Remaining_Backlog_Manual_v1.9.md`: D34 비영향 티켓의 기존 Notion 수동 입력 Source

`D-SEC-01`은 2026-09-01 D17/D34 승인으로 `Done`이며, 실제 Manifest·Runtime·Positive/Negative Test는 `P1-SEC-01`에서 별도 판정한다. 설계 승인만으로 Runtime 통제를 완료했다고 표현하지 않는다.

`MS-G0-01`은 같은 날 `FULL PASS / Done`으로 종결한다. G1/G2는 실제 Platform·Security·Application·Monitoring Evidence가 필요하며 G0 종결로 자동 통과하지 않는다.

## 3.2 Backlog Freeze Rules

- Phase 1 P0는 1.1, Phase 1 P1은 1.2, Scope Out은 1.3을 권위 목록으로 사용한다.
- Phase 2 P0는 13장의 Hybrid P0와 `FDS_Remaining_Backlog_WBS_v3.1.12.xlsx`를 권위 목록으로 사용한다.
- 신규 티켓 Description은 `FDS_Notion_Remaining_Backlog_Manual_v1.9.md` 3장의 고정 템플릿을 사용한다. 현재 Description 후보는 `FDS_v3.1.19_Canonical_Ticket_Update_Pack_v1.0.md`와 67개 개별 파일을 사용한다. 67개 Description 파일은 현행 17개 속성과 수집 시점의 원문을 구분해 보존한다. 최신 운영 delta 대조와 Issue 적용은 별도 절차다. 전체 문서 버전의 발행 상태는 CURRENT.md를 따른다.
- P1 미완료는 해당 P0 Gate를 차단하지 않으며 Owner, Due, Known Issue를 남긴다.
- Scope Out 기능을 일정에 추가하거나 P0/P1 우선순위를 변경할 때는 Change Request가 필요하다.
- 작업 상태 변경은 Exit Criteria와 Evidence 확인 후 수행하며 단순 구현 완료만으로 `DONE` 처리하지 않는다.
- 문서를 현업에 배포할 때는 변경 범위, 영향, 적용 절차, Rollback, 배포 상태를 기록한 릴리즈 노트를 반드시 함께 배포한다.

## 3.3 DEC-P1-ENTRY-01 Dependency Correction

- `P1-LB-01`의 직접 선행조건은 동결 Network/Linux 기반과 API LB Stage A 구성이다. `DEC-P1-ENTRY-01`은 직접 선행조건이 아니다.
- `P1-K8S-01` Gate 0 설치 전 Preflight는 선행 실행할 수 있다. kubeadm Bootstrap은 `P1-LB-01` Stage A Listener Ready와 OS/Node Bootstrap Evidence 확인 후 해제하며, CP API 기동 후 `P1-LB-01` Stage B 검증을 수행한다.
- `DEC-P1-ENTRY-01/D18`은 2026-08-31 PASS로 고정되었으며 `P1-APP-01`의 External Exposure와 `P1-SEC-01`의 관련 Allowlist/NetworkPolicy에 적용한다.
- `D-SEC-01/D17`은 D34 승인으로 종결되었다. `P1-LB-01`과 `P1-K8S-01`의 선행관계는 변하지 않으며, G2는 `P1-SEC-01` Runtime Acceptance와 Evidence가 확보될 때까지 통과하지 않는다.

## 3.4 Ticket Lifecycle / Review Control

- 허용 Status는 `To Do`, `In Progress`, `In Review`, `Done`, `Cancelled`뿐이다. 기존 `Not Started`는 `To Do`로 일괄 보정한다.
- `Blocked`는 Lifecycle Status가 아니다. 선행조건과 차단 사유는 Dependency 또는 Schedule Note에 기록한다.
- `N/A`는 기술 적용 결과로만 사용할 수 있다. 구현이 취소된 티켓은 결정 근거와 함께 `Cancelled`로 변경한다.
- Lead가 구현 및 단위 테스트를 수행하는 동안은 `In Progress`, 검토 제출 시점부터는 `In Review`다.
- 테크니션 리뷰, Support 리뷰, 영향성 리뷰, 승인 리뷰를 별도 Status로 만들지 않고 모두 `In Review`로 관리한다. 해당 단계 담당자는 티켓에 등록된 Support다.
- Support는 단위 테스트 결과와 타 모듈·보안·운영 영향성을 순서대로 검토하고 Review Result를 기록한다.
- 보완이 필요하면 Lead가 보완한다. 보완은 조건부이며 강제 절차가 아니고, 단순 보완만으로 Status를 `In Progress`로 강제 환원하지 않는다.
- Exit Criteria, Evidence, Review Result와 필요한 승인 기록이 모두 확인된 후 `Done`으로 종결한다. 기술 PASS만으로 자동 종결하지 않는다.
- 현업 배포 전 상태는 `READY FOR DISTRIBUTION`, 검토 승인 후 배포본 발행 상태는 `RELEASED`로 관리한다. 배포 시 릴리즈 노트를 필수 동반하고 수신 확인은 별도로 기록한다.

## 3.5 Decision Review / Distribution Control

- `DEC-P1-ENTRY-01/D18`은 Reviewer 이하영·Approver 이권욱의 `PASS`, `DEC-P1-TLS-01/D19`는 Reviewer·Approver 이하영의 `PASS`로 2026-08-31 승인되었다. 두 Decision Ticket은 `Done`이며 승인 결과와 일자를 Evidence에 연결한다.
- D18은 HAProxy + 접근 제한 NodePort, `externalTrafficPolicy: Local`, Worker `.50/32` Allowlist 및 P2 Exposure Adapter 전환 원칙을 고정한다.
- D19는 프로젝트 Private Root CA, Harbor/edge01 서비스별 Leaf, Consumer CA Trust, TLS 1.2 이상 및 검증 우회 금지를 고정한다.
- Robot Account 권한 설계·발급은 TLS 설계와 병행할 수 있으나 실제 로그인·Push/Pull Runtime Test는 인증서 설치와 Consumer CA Trust 완료 후 수행한다.
- Decision `Done`은 설계 승인 완료를 의미한다. 실제 Runtime Evidence와 G1/G2 완료는 후속 구현 티켓에서 별도 판정한다.
- v3.1.13은 ChatGPT Work 정본 발행 상태를 `RELEASED`로 기록하되, 현업 전달·수신 확인은 별도 필드에서 `Pending`으로 유지한다.

## 3.6 P1-ANS-01 Closure / Handoff Control

- `HO-ANS-08`은 Operational Owner 이권욱, 90일 또는 Event 기반 회전, 폐기·복구 절차와 Evidence가 검토되어 `PASS`다.
- `HO-ANS-09`는 Reviewer·Approver 이하영의 Review `PASS`, Approval `APPROVED`, 일자 `2026-08-31`로 종결한다. 동일인 겸임 사실을 승인 Evidence에 명시한다.
- `P1-ANS-01`의 기술 Scope와 승인 통제가 모두 충족되어 `Done / Closed Date 2026-08-31`로 전환한다.
- `HO-ANS-01~04`는 Kubernetes 설치 전 검증 통제이며 `P1-ANS-01`의 미결함으로 남기지 않는다. 각 책임 Ticket에서 미완료 상태로 검증한다.

| Handoff | 책임 Ticket | 후속 Acceptance / Evidence |
|---|---|---|
| HO-ANS-01 | P1-K8S-01 | containerd와 kubelet cgroup driver 일치 |
| HO-ANS-02A | P1-K8S-01 | SELinux Enforcing에서 Runtime·kubelet·Calico 정상 |
| HO-ANS-02B | P1-SEC-01 | SecurityContext·PSA Restricted 실클러스터 호환성 |
| HO-ANS-03 | P1-K8S-01 | 6대 hostname·MAC·product_uuid 중복 0 |
| HO-ANS-04A | P1-K8S-01 | Kubernetes·Calico Port Matrix와 Node 간 통신 PASS |
| HO-ANS-04B | P1-LB-01 | `.109:6443 → .102~.104:6443` Stage A/B 검증 |
| HO-ANS-04C | P1-SEC-01 | `.50/32 → Worker:30080` 허용, 기타 Source 차단 |
| Related | P1-APP-01 | Service `80→8000`, `/readyz`, `/livez` 계약 검증 |

## 3.7 DEC-P1-ENTRY-01 / DEC-P1-TLS-01 Approval Closure

### D18 Application Exposure

- P1 외부 진입은 `edge01` HAProxy + Worker NodePort `30080`으로 고정한다.
- NodePort는 `edge01 10.1.93.50/32`에서만 접근 가능하며 일반 Client의 Worker 직접 접근은 금지한다.
- Service는 `port 80 → targetPort 8000`, Health Contract는 `/readyz`와 `/livez`를 사용한다.
- `externalTrafficPolicy: Local`로 edge01 출발지 주소를 보존하고 실제 Client 주소는 신뢰 가능한 `X-Forwarded-For`로 전달한다.
- 실제 HAProxy·Service·Firewall·NetworkPolicy 적용과 Runtime Test는 P1-APP-01·P1-SEC-01에서 판정한다.

### D19 TLS Trust

- 프로젝트 전용 Private Root CA가 Harbor와 edge01의 서로 다른 Server Leaf 인증서를 서명한다.
- Consumer에는 CA 공개 인증서만 배포하고 Root/Leaf Private Key는 Git·Manifest·Notion·로그·Evidence에 저장하지 않는다.
- DNS/IP SAN, TLS 1.2 이상, 인증서 검증 우회 금지, 만료·갱신·Rollback 및 Positive·Negative Test를 적용한다.
- D-SEC-01은 Harbor Robot Account의 인증 주체·권한·회전 기준을, D19는 서버 신뢰와 전송구간 TLS를 다룬다.
- Worker는 Pull 전용 계정, CI/CD는 Harbor 제약상 Push+Pull 계정을 사용하며 자격증명은 분리한다.
- Robot Account 설계·발급은 병행 가능하나 실제 로그인·Push/Pull Runtime Test는 CA Trust 적용 후 수행한다.
- RISK-06은 Runtime 배포·검증 전까지 `Open`을 유지한다.

## 3.8 DEC-P1-MON-01 / D33 Monitoring Change Control

- D33은 Grafana를 포함한 Kubernetes 내부 관측 스택과 monitor01 외부 Watchdog을 결합한 Hybrid Monitoring 구조를 고정한다.
- `P1-MON-01`의 Priority·Owner·일정·Lifecycle은 변경하지 않으며 Status는 `In Progress`를 유지한다.
- D33은 `D-ARC-01` 최초 Freeze 이후 승인 변경으로 Logical/Physical Architecture v3.1.3을 발행하지만 D-ARC-01을 재개방하지 않는다.
- node-exporter 예외는 `FDS_D-SEC-01_Monitoring_System_Exception_Addendum_v1.0.md`에서 통제하며, D17과 D-SEC-01의 전체 승인 완료를 대체하지 않는다.
- 실제 Dashboard, Target UP, Alert, PVC, RBAC, NetworkPolicy, Host Firewall, Heartbeat 장애탐지와 Recovery Evidence는 `P1-MON-01`의 책임이다.
- Rollback 시 v3.1.12의 monitor01 중심 수집구성으로 즉시 회귀하지 않는다. 보안 영향도와 IF-05/IF-06 Interface Change를 재검토한 승인된 Rollback Decision이 필요하다.

---

# 4. Physical Resource / Placement

## 4.1 Physical Server

8대 동일급 장비:

- CPU: Intel Core i5-13400
- RAM: 64GB
- SSD: 932GB
- OS Host: Windows + VMware Workstation Pro

## 4.2 Physical Placement

| Server | Windows Host IP | 주요 VM / Service |
|---|---:|---|
| server01 | `10.1.93.23` | mgmt-gw01, ansible01, cicd-runner01, monitor01 External Watchdog, k8s-api-lb01, dns01(P1) |
| server02 | `10.1.93.30` | k8s-control01 |
| server03 | `10.1.93.31` | k8s-control02 |
| server04 | `10.1.93.22` | k8s-control03 |
| server05 | `10.1.93.26` | k8s-worker01 |
| server06 | `10.1.93.24` | k8s-worker02 |
| server07 | `10.1.93.25` | k8s-worker03 |
| server08 | `10.1.93.29` | edge01, harbor01, db01, dns02(P1), vpn-gw01(Phase 2) |

---

# 5. OS / Platform Baseline

| 영역 | 기술 | 상태 |
|---|---|---|
| Virtualization | VMware Workstation Pro | Fixed |
| VM OS | CentOS Stream 10 | Fixed |
| Automation | Ansible | Fixed |
| Runtime | containerd | Fixed |
| Kubernetes | kubeadm 3CP + 3Worker | Fixed |
| CNI | Calico | Fixed |
| SCM / Workflow | GitHub Private Repo / GitHub Actions | Fixed |
| Internal Execution | Self-hosted Runner | Fixed |
| Registry / Scan | Harbor / Trivy | Fixed |
| Application | Python / FastAPI | Fixed |
| Microservices | transaction-api / fds-engine | Fixed |
| Data | PostgreSQL External VM | Fixed |
| Monitoring | Kubernetes Prometheus + Alertmanager + Grafana + kube-state-metrics + node-exporter + App Metrics; monitor01 External Watchdog | P0 Core / Hybrid Failure Domain |
| Infrastructure DNS | BIND Primary/Secondary | P1 |
| Hybrid | OCI Relay + AWS S2S + ROSA | Fixed / Validation Required |

---

# 6. Network Baseline

## 6.1 Windows Host Fixed IP

| Host | Fixed IP |
|---|---:|
| server01 | `10.1.93.23` |
| server02 | `10.1.93.30` |
| server03 | `10.1.93.31` |
| server04 | `10.1.93.22` |
| server05 | `10.1.93.26` |
| server06 | `10.1.93.24` |
| server07 | `10.1.93.25` |
| server08 | `10.1.93.29` |

## 6.2 Approved / Reserved / Unavailable IP

**Approved Assignment Pool**
- `10.1.93.50 ~ 10.1.93.55`
- `10.1.93.56` (`egress-proxy01`, DEC-P1-EGRESS-01 승인)
- `10.1.93.58` (`mgmt-gw01` 전용)
- `10.1.93.102 ~ 10.1.93.105`
- `10.1.93.107 ~ 10.1.93.109`

**Reserved**
- `10.1.93.57`
- `10.1.93.59`

**DO_NOT_USE**
- `10.1.93.100`
- `10.1.93.101`
- `10.1.93.106`

## 6.2.1 Physical LAN Parameters — Fixed

| Parameter | Value | State |
|---|---|---|
| Network | `10.1.93.0/24` | Fixed |
| Subnet Mask | `255.255.255.0` | Fixed |
| Default Gateway | `10.1.93.254` | Fixed |
| Upstream DNS | `8.8.8.8` | Fixed |
| Broadcast | `10.1.93.255` | Derived |
| Usable Host Range | `10.1.93.1 ~ 10.1.93.254` | Derived |

> `8.8.8.8`는 외부 이름해석용 Upstream Resolver다.  
> P1 내부 DNS 구현 후 일반 Node/VM은 `dns01(10.1.93.52)` 및 `dns02(10.1.93.53)`를 사용하고, BIND 서버만 `8.8.8.8`로 Forward한다.

> `10.1.93.254`는 프로젝트 관리 대상이 아니며 설정 변경이나 반환 Route 추가가 불가능하다. ICMP 단독 응답이 아닌 Route, ARP 및 승인 TCP 경로로 검증한다.

## 6.3 Service / Node Assignment

| IP | Assignment | Priority |
|---|---|---|
| `10.1.93.50` | edge01 / Service Entry | P0 |
| `10.1.93.51` | vpn-gw01 LAN Endpoint | Phase 2 |
| `10.1.93.52` | dns01 Primary | P1 |
| `10.1.93.53` | dns02 Secondary | P1 |
| `10.1.93.54` | harbor01 | P0 |
| `10.1.93.55` | db01 PostgreSQL | P0 |
| `10.1.93.56` | egress-proxy01 / server08 / TCP3128 | DEC-P1-EGRESS-01 확정, 서비스 인수 #74/#75 |
| `10.1.93.57` | Reserve | Reserved |
| `10.1.93.58` | mgmt-gw01 Physical NIC | P0 |
| `10.1.93.59` | Future Infrastructure / Reserve | Reserved |
| `10.1.93.102` | k8s-control01 | P0 |
| `10.1.93.103` | k8s-control02 | P0 |
| `10.1.93.104` | k8s-control03 | P0 |
| `10.1.93.105` | k8s-worker01 | P0 |
| `10.1.93.107` | k8s-worker02 | P0 |
| `10.1.93.108` | k8s-worker03 | P0 |
| `10.1.93.109` | k8s-api-lb01 | P0 |

## 6.4 Network Design

- Kubernetes Node Plane: VMware Bridged
- VMware VMnet0: Bridged `10.1.93.0/24`, 실제 Windows `이더넷`에 명시 연결
- VMware VMnet1: Host-only `10.250.10.0/24`, DHCP Off, Windows Host `.254`
- VMware VMnet8: NAT `192.168.10.0/24`, FDS VM NIC 연결 금지
- API Endpoint: `10.1.93.109:6443`
- Edge Entry: `10.1.93.50`
- Harbor: `10.1.93.54:443`
- PostgreSQL: `10.1.93.55:5432`
- VPN: `10.1.93.51`
- DNS P1: `10.1.93.52`, `10.1.93.53`
- Physical Default Gateway: `10.1.93.254`
- External DNS Forwarder: `8.8.8.8`
- Management VMnet: `10.250.10.0/24`
  - mgmt-gw01 Management `.1`
  - ansible01 `.10`
  - cicd-runner01 `.20`
  - monitor01 `.30`

- mgmt-gw01 Physical: `10.1.93.58/24`, Default Gateway `10.1.93.254`
- 모든 Physical FDS VM Return Route: `10.250.10.0/24 via 10.1.93.58`
- 내부 FDS 목적지 Source NAT 금지
- 외부 비내부 목적지에 한해 조건부 Masquerade 허용

Management Source 보존 검증 결과는 `.102/.103/.104/.105/.107/.108` 전체 `PASS=6`, `FAIL=0`이다.

서비스 VM을 Bridged Endpoint로 단순화하고, Host Firewall / Service ACL과 Kubernetes NetworkPolicy를 사용한다. 이는 실습 일정 보호를 위한 설계이며, 물리적 L2 망분리 구현으로 표현하지 않는다.

## 6.5 Cluster / Cloud CIDR Reservation

- Pod: `10.244.0.0/16` (`P1-K8S-01` 적용 전 최종 확인)
- Service: `10.96.0.0/12` (`P1-K8S-01` 적용 전 최종 확인)
- AWS VPC: `10.20.0.0/16`

## 6.6 Node Firewall / Management Endpoint Review

**2026-08-28 사전 상태 이력:** 당시 CP 3대와 Worker 3대의 `firewalld`는 `enabled/active`이며 `ens160`은 `public` Zone, `forward=yes`다. Runtime/Permanent Zone에 `ssh`, `cockpit`, `dhcpv6-client`가 있고 별도 Port, Rich Rule, Direct Rule, Host Egress Policy는 없다.

- Worker NodePort `30080/tcp`, Kubernetes/Calico 필수 Port 및 Worker→Harbor Egress는 아직 구현되지 않았다.
- External Entry 구현 시 Worker `30080/tcp`는 `edge01 10.1.93.50/32`에서만 허용하고 다른 Source의 직접 접근은 차단한다.
- `cockpit.socket`은 6개 노드에서 `enabled/active`, `*:9090` Listener 상태다. P1-K8S 착수 전 비활성화하거나 관리 Source Allowlist·TLS·Owner를 별도 승인한다.
- **D34 목표 / 최신 전환 리뷰 반영 후보:** 최종 Node 보호는 Calico named HostEndpoint와 GlobalNetworkPolicy로 통일한다. 과거 “Calico 설치 전 일괄 firewalld OFF” 문구를 현재 실행 명령으로 사용하지 않는다. 실제 전환은 GNP/Bootstrap Allow 준비, 노드별 HEP·failsafe 및 집행·차단·회귀·복구·재부팅 검증을 연결하고 보호 공백이 없음을 확인한 고정 변경안의 리뷰·실행 결정에 따른다. 본 정본 후보는 서버 적용 승인이 아니다.
- **D34 확정:** Calico 초기 Network Mode는 `BGP Disabled + VXLANCrossSubnet + natOutgoing=true`다. Underlay MTU 1500 기준 MTU 1450을 후보로 두되 실제 CNI 출력과 경로 시험으로 확정한다. CrossSubnet 검증이 실패하면 ICR 영향도·Rollback 검토 후 VXLAN Always로 전환한다.
- `edge01 .50/32 → Worker:30080`은 `preDNAT: true`, `applyOnForward: true` 정책으로 제한하고 그 외 외부 Source는 명시적으로 거부한다.
- HostEndpoint 정책은 Bootstrap Allow → canary Worker → Worker 확장 → Control Plane 순서로 적용하며 SSH/API/etcd/kubelet/Calico/DNS/Harbor와 Host Egress 회귀시험을 선행한다.
- Host Firewall 허용, Kubernetes NetworkPolicy, TLS Trust는 서로 다른 통제다. 하나의 PASS를 다른 통제의 Evidence로 대체하지 않는다.
- `HO-ANS-04A`의 Kubernetes/Calico Node Port Matrix는 `P1-K8S-01`, `HO-ANS-04B`의 API LB 경로는 `P1-LB-01`, `HO-ANS-04C`의 제한 NodePort Source Allow/Deny는 `P1-SEC-01`에서 각각 검증한다.

---


### 6.6.1 2026-09-10 실제 상태와 실행 경계

CP1 단일 Ready Node·etcd voter·API 정상, CP2/3→CP1 TCP 0/6 및 CP2 manifest 3개 잔존은 제출 시점의 증적이다. PR #2 증적 HEAD `097ddb56d87b229a9eb465f72ea9f55d16524c51`에는 실행 source afc246d의 현장 Linux 모의시험 37/37·읽기 전용 115개 조회가 연결됐다. PR #3 병합과 PR #4 `75d476edc33d6368fe4ab07e78fc51759e81a6fc` Runtime 전용 보완 기록을 §16과 K8S 통합 기록에 반영한다. CP2/3·Worker 가입과 6/6 Ready·최종 보호 인수는 미완료다.

### 미결 사양과 실행 조건

현재 3CP+3Worker·kubeadm·Calico·static local PV 범위를 유지한다. 추가 노드·플랫폼 도입 결정은 없다. NTP 목적지/운영 주체(#14), 동기화 수치 인수조건(#10), 최소 egress(#19)는 해당 변경·인수 전에 확정한다. `100ms·60초×6`은 2026-09-16 Lead 결정으로 수용했다. control01 upstream/time authority가 미정이므로 NTP 실제 적용은 INPUT_INCOMPLETE/RUNTIME_HOLD다. MTU 1450은 실측 확정 전 후보값이다. CP2 원래 join 단계·비표준 data 경로와 보존/정리/재개 방식은 실제 조사 후 판단한다.

발행 D34의 Calico 설치 전 firewalld OFF 이력과 실제 CP1 공존 drift를 구분한다. ADV-20260910에 따라 사유·기간·보호·복구·종료조건을 기록한 제한적 선행 준비를 이어간다. 최종 6대 firewalld disabled/inactive 및 named HEP/GNP 목표, Bootstrap Allow→canary Worker→Worker 확대→CP의 보호 전환 순서를 유지한다. CP 통신 canary가 HEP 전환 순서를 대체하지 않는다.

PR #2 최신 HEAD 리뷰·실행 창의 inspect·보호/콘솔/백업/복구·실행 결정 후 CP1 제한 Runtime을 검증한다. 실제 CP1 인수 및 PR #4 최신 HEAD 리뷰 후 후속 대상의 실행·복구/가입을 판단한다. Runtime 시험·리뷰 이후의 Permanent 또는 최종 보호 인계 종료 절차는 별도 결정·구현 대상이다. 승인 JSON을 실제 GitHub 리뷰 인증으로 해석하지 않는다. NTP 미결을 모든 준비의 전역 중단 조건으로 만들거나 기존 시간 동기화 선행조건을 면제하지 않는다.


CP1의 HEP/GNP는 각 0개이고 CP 3대 firewalld는 active로 관측됐다. 필요한 CP 간 IF-12A/IF-12B 일부 허용이 누락됐다. 일괄 OFF·일괄 reset·preflight 무시를 후속 조치로 승인하지 않는다. CP1 최소 방화벽 canary와 최종 Calico 보호 전환은 범위를 분리한다. NTP 목적지·실제 Source/Return Route·Worker 및 ICR 나머지 경로는 별도 확인 사항이다.

# 7. Phase 1 MSA Application

## 7.1 transaction-api

책임:

- Client Request 검증
- `transaction_id`, `source_ip`, `received_at` 생성
- `fds-engine` 호출
- Transaction + FDS Result PostgreSQL 저장
- 최종 Response 반환
- `/livez`, `/readyz`, 메트릭 전용 TCP 9091 `/metrics`

## 7.2 fds-engine

책임:

- R01/R02/R04/R07 평가
- `fds_detected`
- `fds_rules`
- Rule별 Metric
- 내부 Service로만 노출
- `/livez`, `/readyz`, 메트릭 전용 TCP 9090 `/metrics`

## 7.3 Internal Contract

| Source | Destination | Port | Purpose |
|---|---|---:|---|
| Client | edge01 | TCP 80/443 | Service Entry; HTTP는 필요 시 HTTPS Redirect |
| edge01 | transaction-api | Service TCP 80 → target 8000 | Client Entry |
| transaction-api | fds-engine | TCP 8001 | Internal REST Rule Evaluation |
| transaction-api | db01 | TCP 5432 | Data Persistence |
| `monitoring-api/Prometheus` | transaction-api | TCP 9091 `/metrics` | Application Monitoring; 업무 8000과 분리, edge01의 외부 접근 차단 |
| `monitoring-api/Prometheus` | fds-engine | TCP 9090 `/metrics` | FDS Monitoring; 업무 8001과 분리, Cluster 내부 전용 |
| `monitoring-api/Grafana` | `monitoring-api/Prometheus` | TCP 9090 | Prometheus Datasource Query |
| `monitoring-api/Prometheus` | kube-state-metrics | TCP 8080 | Kubernetes Object State Metrics |
| `monitoring-api/Prometheus` | `monitoring-node/node-exporter` | TCP 9100 | Node OS Metrics |
| `monitoring-api/Prometheus` | kubelet | TCP 10250 HTTPS | Kubelet/cAdvisor Metrics; ServiceAccount 인증·읽기 전용 |
| `monitoring-api/Prometheus` | monitor01 `.30` | TCP 443 HTTPS | 제한 heartbeat/self-metric `remote_write`; 전체 메트릭 외부 복제 금지 |
| monitor01 `.30` | edge01 `.50` / API LB `.109` | TCP 443 / 6443 | Cluster 외부 관점 HTTPS/TCP Blackbox Probe |

Application API와 DB Schema의 세부 필드는 Version-controlled OpenAPI 및 Migration Source를 권위 계약으로 사용한다. 호환성을 깨는 변경은 Interface Change Request, Consumer 영향도 검토, Regression Test가 필요하다.

---


## 7.4 2026-09-09 현행 유지·기능 확대 유예 결정

DEC-P1-FDS-01(#4)은 A 선택으로 탐지·기록·관측을 유지하고 거래 보류·해제·거절·운영 UI 및 별도 발표 프론트엔드 배치를 도입하지 않는다. DEC-P1-TXN-01(#5)은 C 선택으로 현재 API·DB 표현 계약을 유지하며 새 status 컬럼·release/reject endpoint·일괄 응답 변경·보류용 Migration을 추가하지 않는다. DEC-P1-ADMIN-01(#6)은 기존 Grafana·합성 데이터·최소 노출 시연을 사용하고 새 업무 역할·2인 승인·15/60분 세션·관리 감사 정책값은 유예한다.

#4는 업무 실패 정책, #5는 API·DB 표현, #6은 관리 조치·권한·감사 정책의 소유 경계다. 기존 fail-open/인증/원자성/시간대가 검증됐다는 승인이 아니다. 기존 Migration drift·실패 경로·Metric 의미·정본 배포와 Source SHA는 P1-APP/DB/MON/E2E에서 검증한다. OID-01 관리 Source/Identity와 기존 D17/D34 보안 부정시험은 그대로 필요하다.

세 Decision의 Done은 사용자 2026-09-09 종결 지시와 현행 유지/확대 유예에 한정한다. 사람의 새 독립 승인·Runtime PASS·G2 통과를 생성하지 않는다. 신규 기능은 현 G2 범위에 편입하지 않으며 실제 도입 요청 시 일정·권한·Interface·회귀 영향으로 다시 검토한다. 기존 D번호를 재사용해 다른 의미를 부여하지 않는다.

# 8. Financial-style Kubernetes Security

Business Workload P0:

- Namespace 분리
- Default Deny Ingress/Egress
- DNS / Edge→transaction-api / transaction-api→fds-engine / transaction-api→DB / Monitoring→Metrics만 허용
- RBAC / Namespace-scoped ServiceAccount
- `runAsNonRoot: true`
- `privileged: false`
- `allowPrivilegeEscalation: false`
- `seccompProfile: RuntimeDefault`
- `capabilities.drop: ["ALL"]`
- `hostPID/hostIPC/hostNetwork: false`
- Private Registry + Trivy
- Secret Hard Coding 금지

System Pod(Calico, kube-proxy 등)는 업무 Workload와 분리하여 예외를 기록한다.

Namespace PSA 확정:

| Namespace | PSA | 적용 원칙 |
|---|---|---|
| `fds-app` | `enforce/audit/warn=restricted` | 업무 Pod 전용 |
| `monitoring-api` | `enforce/audit/warn=restricted` | Prometheus·Alertmanager·Grafana·kube-state-metrics |
| `monitoring-node` | `enforce=privileged`, `audit/warn=restricted` | node-exporter DaemonSet 전용; 임의 Workload 생성 RBAC 금지 |
| `ci-cd` | `enforce/audit/warn=restricted` | Runner SA Identity; 외부 Runner VM |
| `kube-system` | `enforce=privileged`, `audit/warn=restricted` | Namespace 단위 System Exception |

- PSA는 Namespace 단위이므로 같은 `kube-system`의 CoreDNS만 Baseline으로 별도 라벨링하지 않는다.
- CoreDNS는 실제 kubeadm 생성 Manifest를 대상으로 non-root, seccomp, capability, read-only root filesystem과 필요한 `NET_BIND_SERVICE` 예외를 dry-run 후 확정한다.
- PSA version label은 적용 클러스터의 실제 Kubernetes Minor `vX.Y`를 확인한 후 렌더링한다. `<TBD-...>` 값은 Template에서만 사용하며 API에 제출하지 않는다.

Monitoring Security Boundary:

| Namespace | Workload | PSA | Mandatory Control |
|---|---|---|---|
| `monitoring-api` | Prometheus, Alertmanager, Grafana, kube-state-metrics | `enforce/audit/warn=restricted` | non-root, `allowPrivilegeEscalation=false`, seccomp `RuntimeDefault`, capability `drop ALL`, 전용 ServiceAccount, 읽기 전용 RBAC |
| `monitoring-node` | node-exporter DaemonSet만 허용 | `enforce=privileged`, `audit/warn=restricted` | 승인 Digest, `privileged=false`, Host Namespace/HostPath 최소화, HostPath read-only, 불필요 Collector 비활성, 변경 승인 없는 추가 Workload 금지 |

- `monitoring-node`의 PSA Privileged 적용은 node-exporter의 `hostNetwork`·`hostPID`·`hostPath` 사용을 허용하기 위한 Namespace 수준 예외다. Container 자체를 `privileged=true`로 실행한다는 의미가 아니다.
- node-exporter HostPath는 Host Root/필요 경로를 read-only로 마운트하고 `--path.rootfs`를 명시한다. Host 쓰기 권한과 불필요한 Linux Capability는 허용하지 않는다.
- `hostNetwork` Pod에 대한 NetworkPolicy 동작은 CNI 구현 의존성이 있으므로 NetworkPolicy만으로 TCP 9100을 통제했다고 판정하지 않는다. Calico 실제 동작 시험과 Node Host Firewall Allowlist를 함께 Evidence로 확보한다.
- Prometheus ClusterRole은 `get/list/watch`와 필요한 non-resource `/metrics`의 `get`만 허용하며 create/update/patch/delete와 Secret 읽기는 금지한다.
- Grafana는 `ClusterIP`만 허용한다. Ingress·NodePort·LoadBalancer는 금지하고, 승인된 `ansible01(.10)` 또는 `cicd-runner01(.20)`에서 API LB `.109:6443`을 경유한 `kubectl port-forward`로만 관리 접근한다.
- Grafana Anonymous Access와 Sign-up을 비활성화하고 초기 관리자 자격정보는 Kubernetes Secret으로 주입·회전한다. 자격정보를 ConfigMap·Manifest·Evidence에 평문 기록하지 않는다.
- 모든 Monitoring Image는 승인된 Harbor Repository의 Digest로 고정하고, Trivy 결과와 적용 Digest를 Evidence로 보존한다.
- 실제 업무 Secret 생성 전 Control Plane 3대에 동일한 EncryptionConfiguration을 적용한다. P1 PoC는 `Secret` 리소스의 `secretbox` 암호화를 사용하고 key는 root-only·Git/Evidence 제외·백업/회전 대상으로 관리한다. 운영/P2 목표는 KMS v2다.
- Prometheus와 kube-state-metrics는 ServiceAccount와 ClusterRole을 공유하지 않는다. Prometheus에는 실제 Discovery 방식에 필요한 read 권한, `nodes/metrics get`, API Server non-resource `/metrics get`만 허용하고 `nodes/proxy`와 Secret 읽기를 금지한다.

---

# 9. DNS Design — P1 Supporting Service

## 9.1 Position

DNS는 Phase 1의 품질을 높이는 Supporting Service이나 **G1 Infrastructure Ready의 Blocker가 아니다**.

- Ticket: `P1-DNS-01`
- Priority: P1
- Lead: 이권욱
- Support: 이하영
- Start: 08-28
- Due: 09-07

## 9.2 Design

| Server | Role | IP |
|---|---|---:|
| dns01 / server01 | Primary BIND | `10.1.93.52` |
| dns02 / server08 | Secondary BIND | `10.1.93.53` |

Zone: `fds.internal`

핵심 Record:
- `k8s-api.fds.internal` → `.109`
- `control01~03` → `.102~.104`
- `worker01` → `.105`
- `worker02` → `.107`
- `worker03` → `.108`
- `edge` → `.50`
- `vpn-gw` → `.51`
- `dns01` → `.52`
- `dns02` → `.53`
- `harbor` → `.54`
- `db` → `.55`

Control Plane Bootstrap은 Ansible `/etc/hosts` 또는 IP Endpoint로 보장하고, DNS 지연이 Cluster 구축을 막지 않도록 한다.

## 9.3 Control

- Internal Query만 허용
- Open Resolver 금지
- UDP/TCP 53
- Zone Transfer는 dns01→dns02만
- 가능하면 TSIG
- Config/Zone File Git/Backup
- dns01 장애 시 dns02 Resolution Test
- CoreDNS는 `cluster.local`, BIND는 `fds.internal`

Hybrid DNS(Route 53 Resolver/Conditional Forwarding)는 Phase 2 P1이며 P0 Hybrid E2E는 IP Endpoint를 허용한다.

---

# 10. CI/CD / Supply Chain

```text
GitHub → Self-hosted Runner → Test → Image Build → Trivy
       → Harbor 10.1.93.54 → kubectl/Helm → Kubernetes
       → Health / E2E
```

- Ansible: `P1-ANS-01` Inventory / OS·Node Bootstrap / Drift·멱등성 검증
- Ansible은 Kubernetes 목표상태의 실행수단이며 Cluster 완료판정은 `P1-K8S-01`이 담당한다.
- GitHub Actions: Application Delivery
- Commit SHA와 Image Tag 추적
- Build 또는 Security Gate 실패 시 Deploy 금지
- `P1-SEC-01`은 `cicd-runner-sa`의 Role/RoleBinding, `resourceNames`, TokenRequest 정책을 소유한다.
- `P1-CICD-01`은 Self-hosted Runner 설치·등록·Service 운영, Workflow, 단기 Token 주입·만료·갱신, 승인 Digest patch와 이전 Digest rollback을 소유한다.
- `cicd-runner-sa`에는 기존 `transaction-api`, `fds-engine` Deployment의 `get/update/patch`만 허용하며 create/delete와 Secret 읽기를 금지한다. Deployment patch를 통한 Secret 우회 위험은 P1 Residual Risk로 기록하고 Admission Policy/서명 강제는 P2로 이관한다.

---

# 11. Monitoring P0 — Kubernetes-Integrated Hybrid Model

## 11.1 Architecture Decision

- Kubernetes 내부 `monitoring-api`: Prometheus, Alertmanager, Grafana, kube-state-metrics
- Kubernetes 내부 `monitoring-node`: node-exporter DaemonSet 전용
- Kubernetes 외부 `monitor01(.30)`: 최소 Prometheus + Blackbox Exporter, 외부 관점 Probe, 제한 heartbeat/self-metric 수신 및 Evidence 보관
- 전 구성요소를 Kubernetes에만 배치하는 단일 장애영역 구성은 금지한다.
- P0는 교육/PoC 제약상 Prometheus·Alertmanager·Grafana 단일 Replica를 허용하지만, 이는 금융 Production HA 수준이 아니다. HA 확장은 `P1-MON-02`에서 Prometheus 2 Replica, Alertmanager 3 Replica, PDB/TopologySpread와 함께 검증한다.

## 11.2 In-cluster Component Baseline

v19 승인 입력: 지정 Storage Worker는 worker03(.108), host path는 `/home/fds-local-pv/{prometheus,grafana,alertmanager}`다. PVC 초기값은 20Gi/5Gi/2Gi, Prometheus 15d 및 retention.size≤16GB이며 조정 가능하다. 생성·Persistence Runtime은 별도 인수다.


| Component | Namespace | Exposure | Storage / Identity | P0 Role |
|---|---|---|---|---|
| Prometheus | `monitoring-api` | `ClusterIP:9090` | PVC; 전용 `prometheus-sa`; 읽기 전용 ClusterRole | App/Kubernetes/Node Metrics, Rule Evaluation, 제한 Remote Write |
| Alertmanager | `monitoring-api` | `ClusterIP:9093` | PVC; 전용 `alertmanager-sa` | 기본 Alert Firing/Resolved 수신·그룹화 |
| Grafana | `monitoring-api` | `ClusterIP:3000`; Port-forward only | PVC; 관리자 Secret; Datasource/Dashboard Provisioning | P0 기본 Dashboard 및 검토 화면 |
| kube-state-metrics | `monitoring-api` | `ClusterIP:8080` | `kube-state-metrics-sa`; `get/list/watch`만 허용 | Node/Pod/Deployment/Replica 상태 |
| node-exporter | `monitoring-node` | Host TCP 9100; 외부 공개 금지 | `node-exporter-sa`; Kubernetes API 권한 없음 | CPU/Memory/Disk/Network/NTP 관련 Node Metrics |

P1 Monitoring Storage는 static local PV를 사용한다. `kubernetes.io/no-provisioner`, `WaitForFirstConsumer`, `Retain`, 전용 디렉터리, nodeAffinity를 적용하며 단일 지정 Worker의 비-HA 구성을 Known Limitation으로 기록한다. StorageClass/PV와 Host Directory는 `P1-K8S-01`, PVC/Mount/Retention/Persistence는 `P1-MON-01`, SecurityContext/fsGroup/writable path 검증은 `P1-SEC-01`이 소유한다. NFS 또는 동적 Provisioner로 변경할 때만 `P1-STO-01`과 별도 Network 영향도를 발행한다.

Prometheus Local TSDB는 PVC를 사용하고 `storage.tsdb.retention.size`를 PVC 용량의 최대 80%로 제한한다. P0 목표 보존기간은 15일이며, 실제 Cardinality·Scrape Interval·PVC 용량 검증 결과에 따라 더 짧은 값이 먼저 적용될 수 있다. 로컬 TSDB는 단일 노드 저장소이므로 Snapshot과 제한적 외부 Evidence 없이는 내구성 또는 HA를 주장하지 않는다.

Grafana Datasource와 Dashboard JSON은 Version-controlled Provisioning으로 배포한다. 기본 Datasource는 `http://prometheus.monitoring-api.svc:9090`이며 Browser Direct Access가 아닌 Server-side Access만 허용한다. Plugin은 P0에서 추가 설치하지 않으며, 필요 시 승인 목록·취약점 검토·Digest 고정 후 변경한다.

## 11.3 Metrics / Dashboard Baseline

- API Request Count / Error / Latency
- `transaction_save_success_total`
- `transaction_save_failure_total`
- `fds_detected_total{rule_id}`
- `missing_client_ip_total`
- Node Ready / Pod Restart / Desired·Available Replica
- Node CPU / Memory / Filesystem / Network / Time Offset 또는 NTP 상태
- Prometheus Target Health, Rule Evaluation Failure, TSDB/PVC 사용률
- Alertmanager Alert Firing / Resolved

Grafana P0 Dashboard는 `Application & FDS`, `Kubernetes Workload`, `Node & Monitoring Health`의 3개 View를 기본 제공한다. Loki, 장기 로그 보존, 고급 업무 Threshold, Dashboard 확장 및 HA는 `P1-MON-02` 또는 Phase 2다.

## 11.4 External Watchdog / Evidence Boundary

- monitor01의 기존 Prometheus는 전체 Cluster Metrics 수집 주체에서 외부 Watchdog으로 역할을 변경하고 Remote Write Receiver를 활성화한다.
- Blackbox Exporter는 edge01 `.50:443` HTTPS와 API LB `.109:6443` TCP 가용성을 외부 관점에서 확인한다.
- monitor01의 TLS Reverse Proxy는 `.30:443`에서 Remote Write Path만 수신해 localhost Prometheus Receiver로 전달한다. 프로젝트 Private CA가 서명한 monitor01 전용 Leaf와 IP SAN `.30`을 사용하며 Private Key는 monitor01 밖으로 반출하지 않는다.
- In-cluster Prometheus는 `fds_monitoring_heartbeat=1` 및 승인된 self/target-health 메트릭만 monitor01 HTTPS Remote Write Receiver로 전송한다. 업무 Payload, Label 내 개인정보, 전체 Application Metric 복제는 금지한다.
- monitor01은 `absent_over_time(fds_monitoring_heartbeat[5m])`에 해당하는 heartbeat 단절을 탐지한다. 판정 시간 5분은 P0 초기값이며 장애 시험 Evidence로 검증한다.
- monitor01 Prometheus/Blackbox UI는 관리망 내부로 제한하고 외부 Service Entry를 제공하지 않는다.

## 11.5 Network / Access Control

- `monitoring-api`와 `monitoring-node` 모두 Default Deny를 기본으로 한다.
- Prometheus만 Application `/metrics`, kube-state-metrics 8080, node-exporter 9100, kubelet 10250에 접근한다.
- Grafana는 Prometheus 9090에만 접근하고 Kubernetes API·Application·DB에 직접 접근하지 않는다.
- Alertmanager는 Prometheus와 승인 Receiver 경로만 허용한다.
- App `/metrics`는 Cluster 내부에서만 수집하며 edge01을 통한 Client 접근은 403/404로 차단하고 Negative Test를 남긴다.
- Remote Write는 monitor01 `.30:443` 단일 목적지로 제한하고 프로젝트 Private CA Trust, 서버 인증서, Kubernetes Secret 기반 인증을 적용한다.

## 11.6 P1-MON-01 Acceptance / Evidence

1. Prometheus Target 목록에서 App, kube-state-metrics, node-exporter, kubelet 및 self Target이 `UP`이다.
2. 거래 호출 후 Application/FDS/DB 저장 관련 Metric과 Kubernetes/Node Metric의 PromQL 결과를 확보한다.
3. Grafana 3개 기본 Dashboard가 Provisioning으로 로드되고, Datasource Health가 PASS다.
4. Grafana Service가 `ClusterIP`이며 외부 Ingress·NodePort·LoadBalancer가 존재하지 않는다.
5. 승인 관리 단말의 Port-forward 접근은 성공하고 비승인 외부 경로 접근은 실패한다.
6. node-exporter의 PSA 예외, Host Namespace, read-only HostPath, `privileged=false`, 적용 Image Digest와 Collector 목록을 Evidence로 확보한다.
7. Prometheus·kube-state-metrics RBAC에서 쓰기 Verb와 Secret 읽기 권한이 없음을 확인한다.
8. NetworkPolicy Positive/Negative Test와 TCP 9100 Node Host Firewall Allowlist를 함께 검증한다.
9. edge01을 통한 `/metrics` 접근은 차단되고, Cluster 내부 Prometheus Scrape는 성공한다.
10. Prometheus Pod 재시작 후 PVC 데이터와 Dashboard Query가 유지된다.
11. Test Alert의 Firing → Alertmanager 수신 → Resolved 전이를 Evidence로 확보한다.
12. In-cluster Prometheus를 중단했을 때 monitor01이 5분 이내 heartbeat 단절을 감지하고, 복구 후 상태가 정상 전환된다.
13. edge01 또는 API LB Probe 실패·복구가 monitor01에 기록된다.
14. Resource Request/Limit, PVC 사용률, Retention 설정 및 Known Single-Replica Limitation을 Runbook에 기록한다.

P1-MON-01 Done은 위 Evidence와 Rollback/Recovery Runbook이 모두 확보된 뒤 선언한다. Manifest 적용 전 상태는 `Design Fixed / In Progress`이며 `Verified`, `HA`, `금융 규제 준수`로 표현하지 않는다.

---


## 11.7 Acceptance 집계와 현재 실증 범위

Runtime Acceptance는 위 14개다. P1-MON-01의 기존 추가 2개 항목은 필수 보조통제로 별도 집계한다: (1) kube-state-metrics `/livez:8080`·`/readyz:8081` 및 Component Probe, (2) IF-06B Receiver flag·TLS/Auth·Payload/Return Route와 IF-24 부재. 이 구분은 항목을 면제하거나 새 PASS를 부여하지 않는다.

9/10 담당자 보고의 k3s `fds` Alert/Dashboard와 일부 kube-state-metrics 실행은 사전 실증이다. 정본 `monitoring-api`/`monitoring-node`, PVC, Default Deny, SA/RBAC, DaemonSet, monitor01 Watchdog/Remote Write와 전체 14개 AC는 미완료다. P1-MON-01은 In Progress / Runtime NOT VERIFIED로 유지한다.

P1-MON-02는 이미 승인된 P1 범위인 Prometheus 2 Replica·Alertmanager 3 Replica·PDB/TopologySpread·Dashboard/Alert·장기 보존 고도화를 담당한다. 기존 티켓의 기본 Dashboard/최소 Alert 중복 설명은 이 범위로 교정한다. 단일 Worker static local PV에 Replica 수만 늘려 HA를 주장하지 않는다. 저장소·네트워크 변경 시 별도 영향도·승인과 실제 장애/복구 검증이 필요하다. P1의 미완료는 P0 Gate를 자동 차단하지 않으며 Known Issue·Owner·Due로 추적한다.

# 12. HA / DR

## P0

- FDS Replica 3개 Worker 분산
- Worker Drain 중 Service 지속
- PostgreSQL `pg_dump` / `pg_restore`
- Restore 후 Final E2E
- Evidence / Runbook

## P1

- Rolling Update
- Control Plane 1대 장애
- PDB / TopologySpreadConstraint
- Harbor Restore
- etcd Snapshot/Restore

---

# 13. Phase 2 OCI / AWS / ROSA

Primary:

```text
On-Prem vpn-gw01 10.1.93.51
  → OCI VPN Relay Public Endpoint
  → AWS Site-to-Site VPN
  → VPC 10.20.0.0/16
  → ROSA
```

Hybrid P0:

- `P2-ARC-01` Phase 2 Architecture Freeze
- ROSA transaction-api/fds-engine
- ROSA → On-Prem DB `10.1.93.55:5432`
- ROSA → Harbor `10.1.93.54:443` 필요 시
- OADP → S3 `443`
- GitHub Actions / Runner → 승인 Registry → ROSA Delivery (`P2-CICD-01`)
- 10-02 OCI Go/No-Go

Hybrid P1 / Conditional:

- Hybrid DNS는 D23 결과에 따라 `P2-DNS-01` 구현 또는 N/A
- Operator 공급망은 D26 결과에 따라 `P2-OP-01` 구현 또는 N/A

Fallback:

1. Vendor Public Endpoint
2. AWS EC2 + EIP Relay
3. Overlay(E2E only)
4. Network/Switch Work

---

# 14. Gate Exit Criteria

## MS-G0-01 / G0 Design Freeze — 08-26 — DONE / FULL PASS

Required:
- `D-ARC-01`: Logical/Physical Architecture v3.1.2 최초 Freeze; D33 승인 Monitoring Change를 v3.1.3으로 반영
- `D-NET-01`: Network Baseline v2.3 및 검증 완료
- `D-WBS-01`: 3인 WBS / Backlog / Interface Freeze

Result:
- Milestone Lifecycle Status: `Done`
- Gate Result: `FULL PASS`
- Architecture / Network / WBS: `PASS`
- Security Ownership: `ASSIGNED` — Lead 이하영
- Security Scope / Exit Criteria: `PASS` — D17/D34 / `D-SEC-01`
- Open Governance Decision: `0`
- P1 DNS와 Reverse/PTR 제외는 G0 Non-blocker
- Freeze 이후 변경은 Change Request 적용
- D33 Monitoring Architecture와 D34 Security Design 변경은 승인·추적된 Freeze 이후 변경으로 정본에 반영됨

G0는 2026-09-01 D17/D34 승인과 D-SEC-01 정본 반영으로 종결한다. 이는 설계 Gate의 완료이며 P1-K8S/P1-SEC/P1-APP/P1-MON Runtime 검증 또는 G1/G2 통과를 의미하지 않는다.

## G1 Infrastructure Ready — 09-07

D36에 따라 이재환의 09-04 개인 휴가와 `P1-DB-01` 완료일을 정렬해 목표일을 다음 영업일인 09-07로 이동한다. 이는 G2·G3·Phase 1 Close의 목표일을 변경하지 않는다.

Required:
- CentOS 10 / containerd
- `P1-ANS-01`: Inventory/SSH `PASS=6`, 실패 0, 2차 실행 `changed=0`
- `P1-ANS-01` 상태: `Done` — 2026-08-31, HO-ANS-08·09 승인 완료
- CP×3 / Worker×3
- API LB / Calico
- Harbor / Runner / PostgreSQL
- Node Connectivity / Push/Pull

Not Required:
- DNS P1
- Rolling Update
- CP Failure
- Harbor Restore

선행 완료:
- `D-NET-01`: DONE — 2026-08-26
- `P1-LNX-01`: DONE — Kubernetes 서비스 Role Check 제외

## G2 Security / Feature Ready — 09-11

Required:
- transaction-api / fds-engine
- Internal REST Contract
- PostgreSQL 저장
- Security P0
- CI/CD
- Kubernetes 내부 Prometheus·Alertmanager·Grafana·kube-state-metrics, node-exporter 통제 예외, monitor01 External Watchdog 및 P1-MON-01 Evidence
- Initial E2E / Negative Test / Worker Drain

DNS P1은 완료 권장이나 Gate No-Go 조건이 아니다.

## G3 Review Ready — 09-18

Required:
- Final E2E / Regression
- Worker Drain Evidence
- PostgreSQL Restore Evidence
- Critical Issue 0
- Architecture / Test / Runbook

Rolling Update, CP Failure, Harbor Restore는 P1이며 미완료 시 Known Issue로 관리할 수 있다.

---

# 15. Decision Register

v19 추가 결정: DEC-CAL-P1-01은 09-22 오후 Review 일정 결정으로 Done이며 실제 Review 실행과 구분한다. DEC-P1-EGRESS-01은 .56 프록시 배치·정책·인계 결정으로 Done이다. 구현은 CR-P1-MON-01-01/#74와 CR-P1-MON-01-02/#75에서 In Progress로 유지한다. 새 D/IF 순번은 배정하지 않았다.


| ID | Decision | State |
|---|---|---|
| D01 | 3인 / 8 Server / CentOS 10 | Fixed |
| D02 | Kubernetes 3CP + 3Worker | Fixed |
| D03 | transaction-api + fds-engine 2-Service MSA | Fixed |
| D04 | External PostgreSQL / Harbor | Fixed |
| D05 | Bridged Node / Service Endpoint | Fixed, Site Validation |
| D06 | Windows Host IP `.22~.31` 현장 Fixed | Fixed |
| D07 | `.100/.101/.106` 사용 금지 | Fixed |
| D08 | DNS Primary/Secondary | P1 |
| D09 | DNS는 G1 Non-blocker | Fixed |
| D10 | OCI Primary Transit | Selected / Validation |
| D11 | Hybrid DNS | P1 |
| D12 | 실제 금융 규제 준수 완료 표현 금지 | Fixed |
| D13 | VMnet1 `10.250.10.0/24`, VMnet8 `192.168.10.0/24` 분리 | Fixed |
| D14 | Physical Return Route via `.58`, 내부 Source NAT 금지 | Fixed / Verified |
| D15 | `10.1.93.254` 프로젝트 비관리·변경 불가 | Fixed Constraint |
| D16 | 기존 `.56/.57/.59` Reserved 중 `.56`은 DEC-P1-EGRESS-01로 전용 프록시에 배정. `.57/.59` Reserved, `.100/.101/.106` DO_NOT_USE 유지 | PARTIALLY SUPERSEDED — .56 only |
| D17 | D-SEC-01 승인권자·범위·산출물·Exit Criteria 및 P1-SEC-01 경계 | Fixed / PASS — 2026-09-01 |
| D18 | edge01→transaction-api 노출 방식 | Fixed / PASS — 2026-08-31 |
| D19 | Harbor/edge TLS 인증서·Trust 배포 방식 | Fixed / PASS — 2026-08-31 |
| D20 | 2026-09-20 일요일 Phase 1 Review 일정 | Decision Required — 2026-09-18 |
| D21 | OCI Relay Go/No-Go 및 Fallback | Scheduled — 2026-10-02 |
| D22 | ROSA Image Source: Harbor 또는 Cloud Registry | Decision Required — 2026-10-16 |
| D23 | Hybrid DNS P1 적용 또는 P0 IP Endpoint 유지 | Decision Required — 2026-10-16 |
| D24 | 2026-10-24 토요일 Phase 2 Review 일정 | Decision Required — 2026-10-23 |
| D25 | v3.1.5 Backlog Integrity Correction 및 복원·통합·조건부 티켓 적용 | Fixed — 2026-08-27 |
| D26 | ROSA Operator 공급망 Direct Catalog 또는 Mirror 방식 확정 | Decision Required — 2026-10-16 |
| D27 | DEC-P1-ENTRY-01을 Application Exposure 선행조건으로 한정하고 API LB/Cluster Bootstrap 의존성에서 분리 | Fixed — 2026-08-28 |
| D28 | Ticket Lifecycle / Review 상태 표준화, Support Review 운영규칙 및 릴리즈 노트 동반 배포 | Fixed — 2026-08-28 |
| D29 | DEC-P1-ENTRY-01·DEC-P1-TLS-01 In Review 동기화, v3.1.6 이후 릴리즈 노트 보완 및 v3.1.8 정본 배포 | Fixed — 2026-08-28 |
| D30 | Phase 1 실행 착수 상태 동기화: P1-LB-01·P1-DNS-01·P1-DB-01·P1-APP-01·P1-MON-01을 In Progress로 관리 | Fixed — 2026-08-28 |
| D31 | P1-ANS-01 HO-ANS-08·09 PASS 종결 및 HO-ANS-01~04를 P1-K8S/P1-SEC/P1-LB/P1-APP Acceptance로 이관 | Fixed — 2026-08-31 |
| D32 | MS-G0-01을 Remaining Backlog와 Decision/Milestone Register에 정식 등록하고 Lifecycle `In Progress`와 Gate Result `CONDITIONAL PASS`를 분리 관리 | Fixed — 2026-08-31 |
| D33 | DEC-P1-MON-01: Grafana 포함 Kubernetes 내부 관측 스택 + monitoring-node 통제 예외 + monitor01 외부 Watchdog의 Hybrid Monitoring 구조 | Fixed / User Approved — 2026-08-31 |
| D34 | D-SEC-01 최종 승인: 6개 Node firewalld OFF + Calico HEP/GNP, BGP Disabled + VXLANCrossSubnet, kube-system PSA 예외, IF-06B 유지, Local PV, Secret encryption 및 Ticket Handoff | Fixed / User Approved — 2026-09-01 |
| D35 | Interface 전수점검 조치 및 IF-11A 승인: Node 6대→API LB `.109:6443`, IF-06A 보존, IF 중복 병합, Kubernetes/Calico/Monitoring/DNS 계약 보완, P1-HBR 복원, Design/Runtime 상태 분리 | Fixed / User Approved — 2026-09-02 |
| D36 | Team Availability / Phase 1 일정·상태 동기화: 이재환 09-04 개인 휴가, P1-DB/G1 09-07, P1-APP 09-10, P1-MON 09-07 착수, P1-DNS Done, P1-K8S In Progress, P1-LB Stage A PASS·Stage B Pending | Fixed / User Approved — 2026-09-03 |
| D37 | Private `321Team/fds-project-baseline` 저장소에서 `main` 정본, release branch, PR review, CODEOWNERS, SHA-256, immutable history를 적용하고 v3.1.17 무결성 보정을 발행 후보로 관리 | Fixed / User Approved — 2026-09-04; v3.1.17 RELEASED 2026-09-07 |


### 후속 종결 Decision — 2026-09-09

| Record ID | 선택 | 효력 |
| --- | --- | --- |
| DEC-P1-FDS-01 | A 현행 탐지·기록 유지 | Done / 신규 보류·운영 기능 확대 유예 |
| DEC-P1-TXN-01 | C 기존 계약 유지 | Done / 신규 상태·API·보류용 Migration 없음 |
| DEC-P1-ADMIN-01 | A 범위 축소 | Done / 기존 관측·합성 데이터 시연, 새 업무 정책값 유예 |

## 15.1 Interface Contract Register

v19 추가/구체화: IF-07의 관리 Source/identity는 .10/32 + svc_ansible이다. Alertmanager→egress-proxy01 .56:3128→discord.com:443 CONNECT는 DEC-P1-EGRESS-01과 #74/#75에 한정한다. 실제 client Source·selector·Secret·발송/거부/복구 인수는 미완료다. 다른 Pod 일반 인터넷 egress로 확대하지 않는다. 기존 IF-24 퇴역·IF-06B 계약은 유지한다.


`Design State=FROZEN`은 Endpoint/Protocol/Port/Owner/Acceptance의 설계 확정을 의미한다. `Runtime State=PASS`만 실제 구현·시험 완료를 의미한다. `PROVISIONAL` 또는 `DECISION REQUIRED`는 Allowlist·Manifest·방화벽 Permanent 반영 근거로 사용할 수 없다.

| ID | Source → Destination | Protocol / Port | Contract / Purpose | Owner | Implementing Ticket | Acceptance | Design State | Runtime State — 2026-09-04 |
|---|---|---|---|---|---|---|---|---|
| IF-01 | Client → edge01 `.50` | TCP 80/443 | External Service Entry | 이권욱 / 이재환 | P1-APP-01 / TLS 후속 구현 | Health, 80→443, 승인 Transaction 요청 | FROZEN | NOT TESTED |
| IF-02 | edge01 `.50/32` → Worker `.105/.107/.108` | TCP 30080 | HAProxy → 제한 NodePort | 이권욱 / 이하영 | P1-APP-01 / P1-SEC-01 / ICR | `/readyz`, Source `.50/32` Positive, 기타 Source Negative | FROZEN | NOT TESTED |
| IF-02A | transaction-api Service → Pod | TCP 80 → 8000 | ClusterIP Service Routing | 이재환 | P1-APP-01 | `/readyz`, `/livez`, Positive/Negative API | FROZEN | NOT TESTED |
| IF-03 | transaction-api → fds-engine | TCP 8001 | Internal REST Rule Evaluation | 이재환 | P1-APP-01 / P1-SEC-01 | R01/R02/R04/R07 Contract 및 비승인 Egress DENY | FROZEN | NOT TESTED |
| IF-04 | transaction-api → db01 `.55` | TCP 5432 | Transaction/FDS Result Persistence | 이재환 | P1-DB-01 / P1-APP-01 / P1-SEC-01 | Migration, Save/Query, Source 확인, fds-engine→DB DENY | FROZEN | IN PROGRESS |
| IF-05 | `monitoring-api/Prometheus` → transaction-api/fds-engine | TCP 9091/9090 | 분리된 Cluster 내부 `/metrics` Scrape | 이재환 | P1-APP-01 / P1-MON-01 / P1-SEC-01 | Target UP, Metric Query, edge01 `/metrics` DENY | FROZEN — D34 | NOT TESTED |
| IF-05A | `monitoring-api/Grafana` → Prometheus | TCP 9090 | Server-side Datasource Query | 이재환 | P1-MON-01 / P1-SEC-01 | Datasource Health, Grafana ClusterIP only | FROZEN — D33 | NOT TESTED |
| IF-05B | `monitoring-api/Prometheus` → kube-state-metrics | TCP 8080 | Object State Metrics | 이재환 / 이하영 | P1-MON-01 / P1-SEC-01 | Target UP, RBAC read-only | FROZEN — D33 | NOT TESTED |
| IF-05C | `monitoring-api/Prometheus` → Alertmanager | TCP 9093 | Alert Delivery | 이재환 / 이하영 | P1-MON-01 / P1-SEC-01 | Test Alert Firing→Resolved, Default Deny Positive/Negative | FROZEN — D35 | NOT TESTED |
| IF-06 | `monitoring-api/Prometheus` → node-exporter/kubelet | TCP 9100/10250 HTTPS | Node/Kubelet Metrics | 이재환 / 이하영 | P1-MON-01 / P1-SEC-01 / ICR | 실제 Source/SNAT, Target UP, CA/SA Auth, 비승인 Workload DENY | FROZEN — D33/D35 | SOURCE OBSERVATION PENDING |
| IF-06A | monitor01 `.30/32` → edge01 `.50` / API LB `.109` | TCP 443/6443 | External HTTPS/TCP Blackbox Probe | 이권욱 / 이재환 | P1-MON-01 / P1-LB-01 | LB `.30/32` Allowlist, Failure/Recovery Probe | FROZEN — D33/D35 | NOT TESTED |
| IF-06B | `monitoring-api/Prometheus` → monitor01 `.30` | TCP 443 HTTPS | 제한 Heartbeat/Self Metric Remote Write | 이재환 / 이하영 | P1-MON-01 / P1-SEC-01 / ICR | 5분 이내 Loss Detection, TLS/Auth, Payload Allowlist, Return Path | FROZEN — D33 | BLOCKED — ROUTE/RECEIVER/SOURCE |
| IF-07 | ansible01 `.10` → K8s Node `.102/.103/.104/.105/.107/.108` | TCP 22 | OS/Node Configuration | 이권욱 | P1-ANS-01 / P1-K8S-01 | SSH `PASS=6`, Source `.10`, 멱등성 | FROZEN — D35 scope correction | PASS=6 / DRIFT CHECK REQUIRED |
| IF-08 | runner `.20` → GitHub | TCP 443 | SCM / Workflow Outbound Session | 이권욱 | P1-CICD-01 | Clone/Workflow Poll 또는 승인 API | FROZEN | NOT TESTED |
| IF-09 | runner `.20` → harbor01 `.54` | TCP 443 | Image Push | 이권욱 / 이하영 | P1-HBR-01 / P1-CICD-01 | CA Trust, Authenticated Push, Source `.20` | FROZEN | NOT TESTED |
| IF-10 | Worker `.105/.107/.108` → harbor01 `.54` | TCP 443 | Workload Image Pull | 이하영 | P1-HBR-01 / P1-K8S-01 | CA Trust, Pull/Pod Start, Push DENY | FROZEN | NOT TESTED |
| IF-11 | runner `.20/32` → API LB `.109` | TCP 6443 | Kubernetes Deploy | 이권욱 / 이하영 | P1-LB-01 / P1-CICD-01 | Source `.20`, Authenticated API/Deploy | FROZEN | STAGE A TCP POSITIVE PASS / AUTHENTICATED DEPLOY PENDING |
| IF-11A | K8s Node `.102/.103/.104/.105/.107/.108/32` → API LB `.109` | TCP 6443 | kubeadm init/join 및 안정된 Control Plane Endpoint | 이권욱 / 이하영 | P1-LB-01 / P1-K8S-01 | Node 6대 Positive, 실제 Source, 비승인 Source Negative | FROZEN / APPROVED — D35 | STAGE A NODE POSITIVE 6/6 PASS; `.10` NEGATIVE PASS |
| IF-12 | API LB `.109/32` → CP `.102/.103/.104` | TCP 6443 | Kubernetes API HA | 이권욱 / 이하영 | P1-LB-01 / P1-K8S-01 | Pre-bootstrap Route, Backend Health, Auth API, Failover/Recovery | FROZEN | PREBOOTSTRAP REACHABILITY PASS / STAGE B PENDING |
| IF-12A | CP `.102/.103/.104` 상호 및 kube-apiserver → etcd | TCP 2379~2380 | etcd Client/Peer | 이하영 / 이권욱 | P1-K8S-01 / ICR / P1-SEC-01 | Listener, CP 상호 Positive, 비승인 Source DENY, Cluster Health | FROZEN — D35 | NOT TESTED |
| IF-12B | Control Plane `.102/.103/.104` → Node 6대 | TCP 10250 HTTPS | kubelet API for cluster operation | 이하영 / 이권욱 | P1-K8S-01 / ICR / P1-SEC-01 | CA/Auth, logs/exec/port-forward, 비승인 Source DENY | FROZEN — D35 | NOT TESTED |
| IF-12C | K8s Node `.102/.103/.104/.105/.107/.108` 상호 | UDP 4789 Bidirectional | Calico VXLANCrossSubnet Dataplane | 이하영 / 이권욱 | P1-K8S-01 / ICR | Cross-node Pod 통신, MTU, Reboot, TCP179·IP Protocol4 미허용 확인 | FROZEN — D35 | NOT TESTED |
| IF-13 | Physical Service/Node `.50/.51/.52/.53/.54/.55/.102/.103/.104/.105/.107/.108/.109` → dns01 `.52`, dns02 `.53` | UDP/TCP 53 | `fds.internal` Resolution / Recursion | 이권욱 | P1-DNS-01 | Known/Unknown/External Query, ACL/IPSet, 비승인 Source DENY | FROZEN — D35 source enumeration | PASS / SUPPORT REVIEW CLOSED — 2026-09-03 |
| IF-13A | Approved Kubernetes Workload → CoreDNS | UDP/TCP 53 | `cluster.local` 및 승인 Egress DNS | 이하영 | P1-K8S-01 / P1-SEC-01 / P1-APP-01 / P1-MON-01 | Pod DNS, Default Deny Positive/Negative, 비-DNS Egress DENY | FROZEN — D35 | NOT TESTED |
| IF-13M | Management `.10/.20/.30` → dns01 `.52`, dns02 `.53` | UDP/TCP 53 | Management Resolver | 이권욱 | P1-DNS-01 | Source별 필요성·ACL·Positive/Negative | P1 N/A / FUTURE CHANGE CONTROL — D36 | NOT IMPLEMENTED; `.10` EXCLUDED |
| IF-14 | dns01 `.52` → dns02 `.53` | TCP 53 + TSIG | Restricted Zone Transfer | 이권욱 | P1-DNS-01 | Authorized AXFR/IXFR, Unauthorized DENY | FROZEN | PASS / SUPPORT REVIEW CLOSED — 2026-09-03 |
| IF-15 | dns01/dns02 → `8.8.8.8` | UDP/TCP 53 | External Forwarding | 이권욱 | P1-DNS-01 | `forward only`, External Query, Other Node Direct Query DENY | FROZEN | PASS / SUPPORT REVIEW CLOSED — 2026-09-03 |
| IF-16 | Physical FDS VM → mgmt-gw01 `.58` | L3 Static Route | `10.250.10.0/24 via 10.1.93.58`, 내부 SNAT 금지 | 이권욱 | ICR-D-NET-01-01 | Route, 양방향 Source Preservation, Reboot/Regression | FROZEN | DRIFT — edge/harbor/db REMEDIATION PENDING |
| IF-17 | vpn-gw01 `.51` → OCI 및 OCI → AWS VPN | UDP 500/4500; IPsec | Hybrid Transit 후보 | 이권욱 | P2-ARC-01 / P2-VPN-01 | Peer별 Endpoint, Tunnel, Route, Approved TCP Path | PROVISIONAL — D21 PENDING | NOT TESTED |
| IF-18 | ROSA → db01 `.55` | TCP 5432 | Hybrid Persistence 후보 | 이권욱 / 이재환 | P2-ARC-01 / P2-HYB-01 | Source CIDR/SG/Route, DB ACL, Hybrid E2E | PROVISIONAL — D21 PENDING | NOT TESTED |
| IF-19 | ROSA → harbor01 `.54` | TCP 443 | Optional Image Pull 후보 | 이하영 | DEC-P2-REG-01 / P2-HYB-01 | D22 선택, Source/Trust, Pull 또는 N/A | PROVISIONAL — D22 PENDING | NOT TESTED |
| IF-20 | OADP → S3 | TCP 443 | Backup Object Storage 후보 | 이하영 | P2-DR / OADP 후속 티켓 | Endpoint/Region/Bucket/Auth, Backup/Restore | PROVISIONAL — P2 DESIGN PENDING | NOT TESTED |

### 15.1.1 Alias / Supersession Register

| 과거/로컬 ID | 처리 | Canonical Contract |
|---|---|---|
| ICR v1.3 IF-21 | MERGED / 신규 Interface 아님 | IF-02 edge01→Worker:30080 |
| ICR v1.3 IF-22 | MERGED / 신규 Interface 아님 | IF-06 Prometheus→node-exporter:9100 |
| ICR v1.3 IF-23 Prometheus 부분 | MERGED | IF-06 Prometheus→kubelet:10250 |
| ICR v1.3 IF-23 Control Plane 부분 | SPLIT / CANONICALIZED | IF-12B Control Plane→Node:10250 |
| IF-24 Alertmanager→monitor01 Webhook | RETIRED / P1 N/A | IF-06B Prometheus→monitor01 Remote Write만 유지 |
| D-NET v2.3 monitor01→CP/Worker:9100/10250 | SUPERSEDED BY D33/D34/D35 | IF-06, IF-06A, IF-06B 사용; monitor01→Cluster workload 신규 Ingress DENY |

### 15.1.2 Interface Decision / Runtime Boundaries

| Item | 미확정 내용 | 현재 통제 | Owner / Due |
|---|---|---|---|
| OID-01 Approved Admin → API LB | ansible01 10.250.10.10/32 + svc_ansible 결정 완료 | 내부 SNAT 금지·기존 Return Route 유지. HEP/GNP 실제 적용은 6/6 Ready 이후 별도 실행창; Runtime 미인수 | 이하영 / 이권욱 — APPROVED_INPUT 2026-09-16 |
| OID-02 Control Plane/System Image Registry | CP·Calico·kube-system Image를 Harbor에서 Pull할지 외부 Registry를 사용할지 | IF-10은 Worker만 허용 | 이하영 — P1-K8S Gate 1 전 |
| OID-03 Bootstrap Package/Registry Egress | 사전 반입 또는 HTTPS Egress Destination·Owner·Expiry | 미정의 Egress Permanent 허용 금지 | 이하영 / 이권욱 — 설치 실행 전 |
| OID-04 Management DNS | `.10/.20/.30`의 P1 DNS 사용 여부 | P1 범위 N/A로 종결; IF-13M 미구현 및 `.10` 제외 유지, 도입 시 Change Request | Closed by P1-DNS-01 Done — 2026-09-03 |

## 15.2 Interface Change Control

- Endpoint, Port, Protocol, Payload, Authentication 또는 Owner 변경은 Interface Change Request 대상이다.
- `FROZEN/APPROVED`는 설계 계약 상태이고 `PASS/FAIL/NOT TESTED`는 Runtime Evidence 상태다. 설계 승인만으로 Listener Ready·Bootstrap Release·Gate PASS를 선언하지 않는다.
- 중복 ID는 신규 구현 규칙으로 사용하지 않고 15.1.1의 Alias/Supersession Mapping을 통해 Canonical ID 하나에만 Evidence를 연결한다.
- 변경 전 Producer/Consumer, Network Allowlist, NetworkPolicy, Monitoring, Test Case 영향을 검토한다.
- 변경 후 Positive/Negative/Regression 결과와 Source/Configuration Version을 Evidence에 연결한다.
- 미정의 인터페이스는 기본 차단하며 임시 허용은 Owner, Expiry, 제거 조건을 기록한다.

---

# 16. Project Status Register — 2026-09-17 20:28 KST

> 역사 기록: 아래는 v3.1.20 당시 표다. v3.1.21의 현행 상태·일정·담당 기준은 이 문서 앞부분 §5 Current Record register다.

전체 67건 / 일정관리 58건 / 역사적 종결 9건 / Milestone 67/67건. 상태 집계: Done 18, In Progress 11, To Do 38.

GitHub lifecycle·계획·담당·Milestone을 동일 source snapshot에서 생성했다. 실제 Runtime은 각 티켓 원문·댓글·intake의 검증 범위를 따르며 문서 발행으로 변경하지 않는다.

| Record | Status | Plan Start | Plan End | Lead | Milestone | 인수 경계 |
|---|---|---|---|---|---|---|
| [DEC-P1-FDS-01](https://github.com/321Team/fds-project-baseline/issues/4) | Done | 2026-09-08 | 2026-09-09 | 이재환 | G2 Security / Feature Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-P1-TXN-01](https://github.com/321Team/fds-project-baseline/issues/5) | Done | 2026-09-08 | 2026-09-09 | 이재환 | G2 Security / Feature Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-P1-ADMIN-01](https://github.com/321Team/fds-project-baseline/issues/6) | Done | 2026-09-08 | 2026-09-09 | 이하영 | G2 Security / Feature Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [D-SEC-01](https://github.com/321Team/fds-project-baseline/issues/7) | Done | 2026-08-26 | 2026-09-01 | 이하영 | G0 Design Freeze | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-G0-01](https://github.com/321Team/fds-project-baseline/issues/8) | Done | 2026-08-26 | 2026-09-01 | 이권욱 | G0 Design Freeze | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-LB-01](https://github.com/321Team/fds-project-baseline/issues/9) | In Progress | 2026-08-27 | 2026-09-17 | 이권욱 | G1 Infrastructure Ready | Stage B 사전점검은 CP1 UP, CP2/CP3 연결 거절로 기록됨. infra-lb 이관과 코드·증적 편입을 Stage B Failover 인수와 구분한다. |
| [P1-K8S-01](https://github.com/321Team/fds-project-baseline/issues/10) | In Progress | 2026-08-27 | 2026-09-17 | 이하영 | G1 Infrastructure Ready | 3CP+3Worker/etcd/DNS/cross-node/Storage 및 재부팅·복구 최종 인수 미완료. OID-01·Storage·NTP downstream 결정은 수용하되 upstream 입력과 Runtime 승인 경계를 유지한다. |
| [P1-DB-01](https://github.com/321Team/fds-project-baseline/issues/11) | In Progress | 2026-08-28 | 2026-09-17 | 이재환 | G1 Infrastructure Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-DNS-01](https://github.com/321Team/fds-project-baseline/issues/12) | Done | 2026-08-28 | 2026-09-03 | 이권욱 | G1 Infrastructure Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-HBR-01](https://github.com/321Team/fds-project-baseline/issues/13) | In Progress | 2026-08-31 | 2026-09-17 | 이하영 | G1 Infrastructure Ready | HBR 수정 PR #2 병합은 코드 편입이다. Worker Pull-only Robot·유한 만료·인증서/Scanner·소비자별 Runtime 인수는 책임 티켓의 실제 증적으로 구분한다. |
| [ICR-D-NET-01-01](https://github.com/321Team/fds-project-baseline/issues/14) | In Progress | 2026-09-01 | 2026-09-21 | 이권욱 | G2 Security / Feature Ready | CP1 CNI 제한 진단·회수·인수와 6대 최종 HEP/GNP 보호 전환을 구분한다. 운영 후보·영수증 소비자·CP2/CP3 인수 미결을 보존하며 6/6 Ready로 확대하지 않는다. |
| [P1-APP-01](https://github.com/321Team/fds-project-baseline/issues/15) | In Progress | 2026-09-01 | 2026-09-18 | 이재환 | G2 Security / Feature Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-CICD-01](https://github.com/321Team/fds-project-baseline/issues/16) | In Progress | 2026-09-01 | 2026-09-18 | 이권욱 | G2 Security / Feature Ready | 공급 및 base probe 제출 Runtime PASS와 로그인 Git 수신 검증을 보존한다. 실제 앱 Test/Build/Scan·Push·Deploy 미실행, Delivery 미검증. 소스 CI/코드 병합은 앱 Runtime 인수가 아니다. |
| [P1-MON-01](https://github.com/321Team/fds-project-baseline/issues/17) | In Progress | 2026-09-07 | 2026-09-18 | 이재환 | G2 Security / Feature Ready | worker03 static local PV/PVC 초기값 20/5/2Gi 승인 입력 반영. 전용 metrics listener의 담당자 실행 보고와 정본 클러스터 통합 Runtime 인수를 구분한다. 14개 Runtime AC+필수 보조통제 2개 유지. |
| [MS-G1-01](https://github.com/321Team/fds-project-baseline/issues/18) | To Do | 2026-09-17 | 2026-09-17 | 이권욱 | G1 Infrastructure Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-SEC-01](https://github.com/321Team/fds-project-baseline/issues/19) | In Progress | 2026-09-04 | 2026-09-21 | 이하영 | G2 Security / Feature Ready | SEC PR #7 보완은 코드 검토 단계다. TLS 우회·key rotation reload 입증·mount assert 등 잔여 지적과 최신 독립 승인 미확인을 유지한다. Runtime PASS 상향 없음. |
| [P1-E2E-01](https://github.com/321Team/fds-project-baseline/issues/20) | To Do | 2026-09-11 | 2026-09-22 | 이재환 | G3 Review Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-DR-01](https://github.com/321Team/fds-project-baseline/issues/21) | To Do | 2026-09-11 | 2026-09-21 | 이재환 | G3 Review Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-HA-01](https://github.com/321Team/fds-project-baseline/issues/22) | To Do | 2026-09-11 | 2026-09-21 | 이재환 | G3 Review Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-G2-01](https://github.com/321Team/fds-project-baseline/issues/23) | To Do | 2026-09-21 | 2026-09-21 | 이하영 | G2 Security / Feature Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-DOC-01](https://github.com/321Team/fds-project-baseline/issues/24) | To Do | 2026-09-11 | 2026-09-22 | 이권욱 | G3 Review Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-MON-02](https://github.com/321Team/fds-project-baseline/issues/25) | To Do | TBD — P0 인수 후 재계획 | TBD — 구현 유예 권장 | 이재환 | Phase 1 Close | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-DR-02](https://github.com/321Team/fds-project-baseline/issues/26) | To Do | TBD — P0 인수 후 재계획 | TBD — 구현 유예 권장 | 이하영 | Phase 1 Close | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-HA-02](https://github.com/321Team/fds-project-baseline/issues/27) | To Do | TBD — P0 인수 후 재계획 | TBD — 구현 유예 권장 | 이하영 | Phase 1 Close | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-CAL-P1-01](https://github.com/321Team/fds-project-baseline/issues/28) | Done | 2026-09-11 | 2026-09-11 | 이권욱 | Phase 1 Review | 09-22 오후 평일 Review 일정 결정 Done. 실제 Phase 1 Review·G3·Close 수행/승인은 별도이며 초기 계획 날짜는 이력으로 유지한다. |
| [MS-G3-01](https://github.com/321Team/fds-project-baseline/issues/29) | To Do | 2026-09-22 | 2026-09-22 | 이권욱 | G3 Review Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-REV-01](https://github.com/321Team/fds-project-baseline/issues/30) | To Do | 2026-09-22 | 2026-09-23 | 이권욱 | Phase 1 Close | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-P1-REVIEW-01](https://github.com/321Team/fds-project-baseline/issues/31) | To Do | 2026-09-22 | 2026-09-22 | 이권욱 | Phase 1 Review | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-P1-CLOSE-01](https://github.com/321Team/fds-project-baseline/issues/32) | To Do | 2026-09-23 | 2026-09-23 | 이권욱 | Phase 1 Close | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-P2-START-01](https://github.com/321Team/fds-project-baseline/issues/33) | To Do | 2026-09-28 | 2026-09-28 | 이권욱 | Phase 2 Start | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-ARC-01](https://github.com/321Team/fds-project-baseline/issues/34) | To Do | 2026-09-28 | 2026-09-28 | 이권욱 | Phase 2 Start | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-IAC-01](https://github.com/321Team/fds-project-baseline/issues/35) | To Do | 2026-09-28 | 2026-10-08 | 이권욱 | G4 Cloud / VPN Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-OCI-01](https://github.com/321Team/fds-project-baseline/issues/36) | To Do | 2026-09-28 | 2026-10-02 | 이권욱 | G4 Cloud / VPN Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-VPN-01](https://github.com/321Team/fds-project-baseline/issues/37) | To Do | 2026-10-01 | 2026-10-08 | 이권욱 | G4 Cloud / VPN Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-ROSA-01](https://github.com/321Team/fds-project-baseline/issues/38) | To Do | 2026-10-06 | 2026-10-16 | 이하영 | G5 ROSA Application Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-G4-01](https://github.com/321Team/fds-project-baseline/issues/39) | To Do | 2026-10-08 | 2026-10-08 | 이권욱 | G4 Cloud / VPN Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-P2-DNS-01](https://github.com/321Team/fds-project-baseline/issues/40) | To Do | 2026-10-12 | 2026-10-16 | 이권욱 | G5 ROSA Application Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-P2-OP-01](https://github.com/321Team/fds-project-baseline/issues/41) | To Do | 2026-10-12 | 2026-10-16 | 이하영 | G5 ROSA Application Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-P2-REG-01](https://github.com/321Team/fds-project-baseline/issues/42) | To Do | 2026-10-12 | 2026-10-16 | 이하영 | G5 ROSA Application Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-APP-01](https://github.com/321Team/fds-project-baseline/issues/43) | To Do | 2026-10-12 | 2026-10-16 | 이재환 | G5 ROSA Application Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-OADP-01](https://github.com/321Team/fds-project-baseline/issues/44) | To Do | 2026-10-15 | 2026-10-22 | 이하영 | G6 Hybrid Integration Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-G5-01](https://github.com/321Team/fds-project-baseline/issues/45) | To Do | 2026-10-16 | 2026-10-16 | 이하영 | G5 ROSA Application Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-CICD-01](https://github.com/321Team/fds-project-baseline/issues/46) | To Do | 2026-10-16 | 2026-10-16 | 이권욱 | G5 ROSA Application Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-HYB-01](https://github.com/321Team/fds-project-baseline/issues/47) | To Do | 2026-10-16 | 2026-10-22 | 이재환 | G6 Hybrid Integration Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-DNS-01](https://github.com/321Team/fds-project-baseline/issues/48) | To Do | 2026-10-19 | 2026-10-20 | 이권욱 | G6 Hybrid Integration Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-DOC-01](https://github.com/321Team/fds-project-baseline/issues/49) | To Do | 2026-10-19 | 2026-10-23 | 이권욱 | Deliverable Freeze | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-E2E-01](https://github.com/321Team/fds-project-baseline/issues/50) | To Do | 2026-10-19 | 2026-10-22 | 이재환 | G6 Hybrid Integration Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-OP-01](https://github.com/321Team/fds-project-baseline/issues/51) | To Do | 2026-10-19 | 2026-10-20 | 이하영 | G6 Hybrid Integration Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-CAL-P2-01](https://github.com/321Team/fds-project-baseline/issues/52) | To Do | 2026-10-22 | 2026-10-22 | 이권욱 | Phase 2 Review | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-G6-01](https://github.com/321Team/fds-project-baseline/issues/53) | To Do | 2026-10-22 | 2026-10-22 | 이권욱 | G6 Hybrid Integration Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-DELIVERABLE-FREEZE-01](https://github.com/321Team/fds-project-baseline/issues/54) | To Do | 2026-10-23 | 2026-10-23 | 이권욱 | Deliverable Freeze | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-REV-01](https://github.com/321Team/fds-project-baseline/issues/55) | To Do | 2026-10-23 | 2026-10-26 | 이권욱 | Project Close | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-P2-REVIEW-01](https://github.com/321Team/fds-project-baseline/issues/56) | To Do | 2026-10-23 | 2026-10-23 | 이권욱 | Phase 2 Review | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-PROJECT-CLOSE-01](https://github.com/321Team/fds-project-baseline/issues/57) | To Do | 2026-10-26 | 2026-10-26 | 이권욱 | Project Close | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [CR-P1-ANS-01-01](https://github.com/321Team/fds-project-baseline/issues/58) | Done | 2026-09-04 | 2026-09-07 | 이권욱 | G1 Infrastructure Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [D-ARC-01](https://github.com/321Team/fds-project-baseline/issues/59) | Done | 2026-08-24 | 2026-08-26 | 이권욱 | G0 Design Freeze | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [D-NET-01](https://github.com/321Team/fds-project-baseline/issues/60) | Done | 2026-08-24 | 2026-08-26 | 이권욱 | G0 Design Freeze | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [D-WBS-01](https://github.com/321Team/fds-project-baseline/issues/61) | Done | 2026-08-24 | 2026-08-26 | 이권욱 | G0 Design Freeze | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-P1-ENTRY-01](https://github.com/321Team/fds-project-baseline/issues/62) | Done | 2026-08-27 | 2026-08-31 | 이권욱 | G2 Security / Feature Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-P1-MON-01](https://github.com/321Team/fds-project-baseline/issues/63) | Done | 2026-08-31 | 2026-08-31 | 이권욱 | G0 Design Freeze | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-P1-TLS-01](https://github.com/321Team/fds-project-baseline/issues/64) | Done | 2026-08-27 | 2026-08-31 | 이권욱 | G1 Infrastructure Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-ANS-01](https://github.com/321Team/fds-project-baseline/issues/65) | Done | 2026-08-27 | 2026-09-01 | 이권욱 | G1 Infrastructure Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-LNX-01](https://github.com/321Team/fds-project-baseline/issues/66) | Done | 2026-08-24 | 2026-08-26 | 이권욱 | G1 Infrastructure Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-NET-01](https://github.com/321Team/fds-project-baseline/issues/67) | Done | 2026-08-27 | 2026-08-27 | 이권욱 | G0 Design Freeze | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [CR-P1-MON-01-01](https://github.com/321Team/fds-project-baseline/issues/74) | In Progress | 2026-09-11 | TBD | 이하영 | G2 Security / Feature Ready | egress-proxy01 .56 배치·관리 계정 준비 및 Ansible 점검 증적과 Squid 서비스/Alertmanager 실제 Source·인수 후속을 구분한다. End TBD 유지. |
| [CR-P1-MON-01-02](https://github.com/321Team/fds-project-baseline/issues/75) | In Progress | TBD | TBD | 이하영 | G2 Security / Feature Ready | 프록시 #74 인수 후 실제 selector·NetworkPolicy·Secret·발송/거부/복구 인수. 초안 준비와 실제 운영 적용을 구분하며 Start/End TBD 유지. |
| [DEC-P1-EGRESS-01](https://github.com/321Team/fds-project-baseline/issues/78) | Done | 2026-09-14 | 2026-09-21 | 이권욱 | G2 Security / Feature Ready | Decision 범위 Done(2026-09-16): .56 전용 배치·정책·예약/자산·자원 영향·#74/#75 인계조건 확정. Squid/NetworkPolicy Runtime 및 G2 승인은 별도. |

## 16.1 배포와 인수 경계

STATIC: 정본 구조·속성·해시·Workbook 검증 대상. CI: 최신 후보 실행 결과 별도. RUNTIME: 이번 정본 통합에서는 미실행. REVIEW: 최종 HEAD 독립 리뷰 대기. MERGE/PUBLICATION: 미실행. 계획 목표 경과와 마일스톤 배정은 완료 승인이 아니다.

## 16.2 이력과 근거

- v18 원문과 태그는 보존한다. 원본 배포 ZIP과 Asset은 변경하지 않는다.
- 현재 본문·댓글 원문: tickets/v3.1.19/sources/
- 승인 입력·보류 입력·제출 증적: audit/v3.1.19/intake/
- 최신 관련 PR 관측: audit/v3.1.19/integration/repository-status.json
- v18 이후 속성 변화: audit/v3.1.19/integration/property-delta.json


</details>
