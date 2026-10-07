# Phase 2 시험계획 정합화 — 2026-10-07

상태: WORKING REVISION / 기존 PR150 재사용. CODEX_ASSISTED.
원본 기준과 조회 snapshot은 [sources.json](sources.json)에 기록한다. Issue AC text는 조회 당시 원문 부분이며 신규 승인/실행 증적이 아니다.

## 발견 사항과 반영

| 원본 문제 | 반영 |
|---|---|
| v3.1.21 TS01~16에 P0/P1/미결/Phase1 인계가 혼재 | 새 Strategy §5에서 ID 보존 및 AC 적용경계 mapping, Test Plan TP0-01~15/TP1-01~07 |
| PR150의 OCP 독점 전제·cluster 복구 제안 | 최신 Shared/Test Lab 경계로 README·이식/시험 준비 정정, exclusive 문서를 shared-lab-rehearsal-preparation으로 대체 |
| #95 10/7 RHOAI Resource Gate FAIL 미연결 | P1/Deferred-first 유지, 설치 미실행·Catalog/StorageClass와 PVC/Runtime 구분 |
| #46 정상/실패 중심 설명에서 rollback 누락 위험 | 기존 Required runs의 RUN-A/RUN-B/rollback·raw chain 모두 유지 |
| #40/#48 P1과 private 관리 DNS subset 시점 충돌 | 신규 사양 확정 없이 미결 책임/완료조건·실제 P0 접근 AC 경계 기록 |
| TS03 N-1/AZ·TS15 복합장애, #38 recreate 문구 | 승인 AC/기존 전략으로 구분, 미결을 새 P0 필수로 확정하지 않음 |
| #35 PR148 OPEN/미생성인 과거 preparation snapshot | merge40ac664b 및 #35 6031865288 PASS_USER_READBACK 수신을 연결, full IaC/Stage-A·직접 raw 검증과 분리 |
| Catalog CPU-only RAG 가능성 주장 | 공식 3.5 OGX/RAG 요구와 실제 선택 기능 지원성 미확인을 분리; P1 내부 검토로 유지 |

## 변경·보존 범위

- 추가: [Strategy](../../tests/FDS_Phase2_Test_Strategy_20261007.md), [Test Plan](../../tests/FDS_Phase2_Test_Plan_20261007.md), tests 색인, 본 변경기록·source snapshot.
- PR150의 기존 preparation를 정합화하고 APP/E2E/Delivery 16 case에 verification stage/acceptance boundary를 추가했다.
- 기존 sources.json/verification.json은 이전 수집/검증 이력으로 그대로 보존한다.
- 발행 v3.1.21 strategy·Baseline·WBS·Description·Manifest·SHA256SUMS·Tag/Release 변경0.
- 기존 Issue 본문/AC·Status·Owner·일정 변경0, 신규 구현 코드/정책/runtime 설정 변경0.
- 열린 PR137(비공개 설계 이전),147(중앙 입력 수신),149(P1 인계), infra-cicd63(새 공급물 소비 준비), infra-kubernetes65/68(P1 배치/OID), infra-ansible66(Runner 감지)은 관련 입력/경계로만 소비한다. 새 source/digest·미승인 설계를 자동 채택하지 않는다.

## 검증 범위·후속

문서 STATIC: UTF-8/LF·상대링크·case ID/행·NOT_RUN·단계/환경·P0/P1/AC mapping·secret patterns·diff를 확인한다.
전체 canonical verifier의 실제 CI Run/Job 결과와 최종 원격 파일/HEAD readback은 PR150의 최신 기록에서 확인한다.
AI 자체 검토는 사람 독립 승인과 다르며, 일반 문서 검토 권한은 기존 Lead 위임 정책을 유지한다.

신규 MOCK/LAB-PRECHECK/RUNTIME/ACCEPTANCE=NOT_RUN. MERGE/PUBLICATION 미수행.
차기 정본 통합 시 #49 이권욱이 Baseline·WBS Test Strategy 시트·Ticket Pack·Manifest/체크섬에 승인 개정안을 연결한다. Runtime 증적을 대신하지 않는다.
원복은 이번 문서 변경 commit revert 검토이며 서버 원복 대상이 없다. PR의 기존 준비 이력은 Git으로 추적한다.
