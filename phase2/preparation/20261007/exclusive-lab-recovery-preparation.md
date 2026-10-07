# 독점 교육장 OCP 시험·복구 사전 설계

상태: PROPOSED / 문서 준비. CODEX_ASSISTED.
기준: 2026-10-07 KST, PR150 선행 HEAD `e9a0d13bdc191d572f4205c5f1bab51a1a54526b`.
소비: #34 환경 경계, #38 플랫폼 입력, #43 이식 입력, #49 증적 집계, #50 시험 실행.
기존 준비안 README·test-evidence-preparation.md의 후속이며 정본 사양·필수 AC를 추가하지 않는다.

## 환경과 실행 입력

사용자 전제는 팀 독점 가능한 교육장 OCP/RHOAI **테스트·검증 자원**이다. 팀 운영 자원 또는 On-Prem→AWS ROSA 본 경로로 편입하지 않는다.
기존 SHARED_OCP_LAB 전제와 다른 부분은 이 문서의 검토 입력으로 남긴다. 도구 ENV enum이나 실행 설정을 아직 변경하지 않는다.

| 실행에 필요한 입력 | 현재 확인 | 생산·소비 |
|---|---|---|
| 실제 cluster/API/context/version 및 대상 계정 | 미수신 | #38 환경 입력 → #43/#50 |
| 독점 사용 가능 기간·대상 자원·관리 권한 | 사용자 독점 전제 확인, 상세 범위 미수신 | 환경 제공 범위 → #38 |
| 초기 workload/operator/node inventory, 보존 대상 | 미수신 | 환경 입력 → 시험 실행자 |
| 백업·복구 수단, 접근 경로, 복구 책임과 성공 기준 | 미수신 | 제공 환경 책임 범위 → #38/#50 |
| 승인 앱 source·image digest·portable manifest SHA | 이번 Lab 실행용 pin 미확정 | #43 → #50/#46 |
| 실제 namespace·SCC·UID/GID·pull/trust 경로 | 미수신 | #38/#42 → #43 |
| fixture·DB 대상과 안전한 데이터 경계 | 미수신 | #43/#47/#50 |
| 시험·정리 작업창 및 중단/복구 담당 | 미확정 | 기존 Lead와 실행자 |

미수신은 새 상시 승인 절차가 아니라 구체 실행안을 만드는 입력 공백이다. 환경 identity가 없으므로 현재 context를 추정해서 oc 명령을 실행하지 않는다.
자격증명·kubeconfig·Secret 값은 이 문서에 수집하지 않는다.

## 권장 시험 순서

| 순서 | 사전 설계한 시험 | 기대 관측·증적 | 영향·복구 범위 |
|---|---|---|---|
| L0 | 대상 identity와 초기 상태 읽기 대조 | 계정 권한, version, 허용 범위 inventory, 앱 pin | 조회만. 접근·대상 불일치 시 후속 중단 |
| L1 | 기존 admission-only 도구 재사용 검토 | exact source, server-side dry-run RC, 적용 SCC/UID 조건 | dry-run 결과를 Running/Ready로 승격하지 않음 |
| L2 | 독립 시험 workload의 arbitrary UID 실행 | 승인 digest imageID, Running/Ready, health, non-root, RO rootfs·허용 volume 쓰기 | 시험 자원만 정리. 실제 P1 이미지·서버 설정 불변 |
| L3 | 같은 pin으로 시험 자원 삭제·재생성 재현성 | before/after identity, manifest/hash, health 및 동일 기대결과 | 자체 시험 자원만 대상. 공유 서비스·원본 데이터 삭제 금지 |
| L4 | 필요성이 확인된 cluster 단위 복구 시험안 작성 | 허용 장애 대상, 관측 기준, 초기 상태 복원, 잔여 자원 | Operator/node/cluster 변경은 대상·복구 계약 확정 후 별도 실행. 현재 미실행 |

L4는 독점 환경에서 가능한 **선택 시험 제안**이다. 필수 P0 AC·ROSA 전체 destroy/recreate 요구사항 또는 현재 착수 차단으로 추가하지 않는다.
실제 명령은 cluster identity·권한·source·복구 수단을 받은 뒤 해당 구현/실행 작업에서 작성한다. 임의 drain/reboot/delete 명령을 배포하지 않는다.

## 중단과 복구 기준

- 대상 context/API 또는 승인 image/source가 입력과 다르면 변경 전에 중단한다.
- 허용 자원 밖 영향, 비밀정보 출력, 예상하지 않은 권한/SCC 우회가 관측되면 후속 변경을 중단한다.
- health/Ready 또는 정리 실패는 성공으로 기록하지 않는다. 원본과 변경 대상 identity를 보존하고 기존 복구 책임으로 인계한다.
- 복구는 사전에 기록한 시험 자원·허용 초기 상태에 한정한다. Phase 1 DB/Harbor/Runner/DNS를 시험 복구 목적으로 변경하지 않는다.
- 종료 판정은 초기 보존 대상 유지, 자체 시험 자원 잔여 확인, 복구 후 health와 원본 로그를 함께 대조한다.
- 복구 시간 목표는 미정이다. 이전 제안의 30분/10분을 승인·실측 값으로 채택하지 않는다.

## 증적과 소비 경계

각 시험은 환경 identity, 실행자·호스트, KST 시작/종료, source/manifest SHA·image digest/imageID,
명령/종료코드·stdout/stderr, 변경 대상 UID와 before/after, 실패·복구·cleanup 원본을 연결한다.
최초 Lab 결과는 실제 Lab 범위만 판단한다. ROSA HCP 지원·AWS IAM 실효권한·VPN 실제 source/DB·Registry cold-pull은 본 경로에서 별도 검증한다.
해시는 수신 파일 무결성 확인이며 시험 성공 또는 인수 완료가 아니다.
실행 원본 편입은 기존 fds-project-evidence 독립 리뷰를 적용한다. 이 문서는 시험 설계여서 실행 증적으로 편입하지 않는다.

## 현재 수행 상태와 다음 행동

STATIC: 기존 PR150 8개 추가 파일과 준비 내용 대조, 이 후속 설계 작성.
MOCK/CI/RUNTIME: 이 문서의 시험은 모두 NOT_RUN. 기존 PR150 문서 CI 성공은 이전 HEAD 범위다.
REVIEW: AI 보조 검토, 타인 독립 승인 아님. 일반 문서 검토는 기존 Lead 위임 정책에 따른다.
MERGE/PUBLICATION/AC 인수: NOT_RUN.

다음 행동은 #38 환경 입력과 #43 승인 pin을 기존 책임 창구에서 수신해 L0~L3 실행안을 구체화하는 것이다.
#40/#42 Decision 자료와 #46 target adapter·#49/#50 시험 설계는 그 입력 수신 전에도 문서 준비를 병행할 수 있다.
