# #46 ROSA Delivery 사전 준비

기준: [#46 현행 계약](https://github.com/321Team/fds-project-baseline/issues/46), infra-cicd main `1320e17e9d7dd66455e65276267dc2b92517c4b5`.
상태: **P2 adapter 변경 지점 정리 / 구현·workflow 연결·ROSA deploy 미실행**.
작성 이권욱 지원 / CODEX_ASSISTED.

## 재사용과 분리 지점

| 영역 | latest P1 source에서 확인 | P2 준비 / 적용 전 조건 |
|---|---|---|
| Test→Build→Scan | [.github/workflows/app-test-build-scan.yml](https://github.com/321Team/infra-cicd/blob/1320e17e9d7dd66455e65276267dc2b92517c4b5/.github/workflows/app-test-build-scan.yml)은 manual dispatch, P1 Runner/host/user를 고정 | build/test/scan source와 결과를 재사용 가능한지 실제 lineage를 검토. 현재 workflow 자체는 수정하지 않음 |
| 대상 Deployment | [deploy-adapter-core.md](https://github.com/321Team/infra-cicd/blob/1320e17e9d7dd66455e65276267dc2b92517c4b5/docs/deploy-adapter-core.md)는 fds-app의 두 workload만 허용 | #43의 base/overlay/UID/container/namespace·previous digest를 별도 P2 입력으로 인계 |
| API·인증 | [deploy-binding.md](https://github.com/321Team/infra-cicd/blob/1320e17e9d7dd66455e65276267dc2b92517c4b5/docs/deploy-binding.md)는 P1 API .109:6443·SA/audience/TTL·policy pin을 고정 | ROSA 실제 API/port/context·CA/TLS·short-lived credential reference를 #38에서 받아 target adapter 설계 |
| 변경·복구 | core의 UID/RV/image test, UNKNOWN 수동 대조, 별도 복구 범위 | P2 client에서도 조건부 변경·실패 시 중단 intent를 유지. 새 host/client/API 지원을 검증하기 전 구현 완료로 표시하지 않음 |
| 잠금·승인·증적 | P1 core 문서는 runtime 미연결과 HEALTH_E2E/POD_IMAGE_ID 미검증을 명시 | P1 모듈을 바로 ROSA 실행기로 호출하지 않음. 기존 Runtime 통합 수준은 별도 P1 업무에서 해결 |
| Registry | D22 final 값이 필요 | push/pull path·trust·credential owner/expiry·digest/rollback image 재Pull은 #42 결과 소비 |
| GitOps | #120 Go/CR 전 Runner-direct가 현행 P0 경로 | Argo CD/새 Operator는 이번 준비 경로에 추가하지 않음 |

## 실행 입력 체크리스트

| 항목 | 현재 준비 상태 | 실제 생산자 |
|---|---|---|
| ROSA API·context·cluster identity·target namespace | PENDING | #38 |
| portable base + OpenShift overlay path/SHA | PENDING | #43 |
| app Source SHA·Scan/PASS·registry digest | 실행 회차 pin 필요 | #42/#46 |
| 실제 Deployment UID/container/current image와 previous approved digest | PENDING | #43 / 실행 직전 readback |
| credential reference·issuer/audience·expiry·회수 | PENDING, 값 저장 없음 | #38/#46 |
| health/readiness/Rule fixture 계약 | 기존 계약 참조 가능, target endpoint PENDING | #43/#50 |
| 정상 run·실패 차단·복구의 실행 범위와 원본 증적 | NOT_RUN | #46 |

## 기존 AC에 연결한 실행 계획 초안

1. RUN-A: exact source의 Test→Build→Scan→승인 Registry Push→ROSA Deploy→health/Rule 및 runtime imageID 대조.
2. RUN-B: Test 또는 Scan 실패를 만들고 Deploy가 실제 실행되지 않은 원본을 수집.
3. Rollback: 승인된 이전 digest로 복원하고 실제 health를 확인.

기존 #46 계약의 rollback을 정상/실패 2종만으로 누락하지 않는다. CI가 0건이면 NOT_RUN이다.
Build/Push/Deploy Run ID·Attempt를 구분하고 Source SHA→scan→pushed digest→manifest SHA→runtime imageID→health/rollback 체인을 연결한다.

성공/중단/복구의 상세 실행 명령은 exact target과 구현 리뷰가 완료된 기존 책임 작업에서 만든다.
지금 작성한 표를 자격증명 발급·Runtime 승인·workflow_dispatch 허용 입력으로 사용하지 않는다.

