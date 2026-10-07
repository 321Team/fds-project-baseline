# #49/#50 시험·증적 사전 준비

상태: **16개 case 초안 작성 / 결과 전부 NOT_RUN**. test-case-draft.tsv는 설계 자료이며 실행 로그가 아니다.
#50 실행·AC 인수 Lead는 이재환. #49 최종 집계 Lead는 이권욱. 이번 지원은 역할 재배정이 아니다.

## 기존 기대결과 연결

- 최신 [#15](https://github.com/321Team/fds-project-baseline/issues/15) AC와 [#119 승인](https://github.com/321Team/fds-project-baseline/issues/119#issuecomment-5928210700):
  - 외부 DB 장애: transaction-api /readyz503와 Endpoint 제외. Liveness 재시작 루프를 만들지 않음.
  - fds-engine 장애: API Ready 유지·거래 fail-open(HTTP201, fds_evaluation_skipped=true).
- [#47](https://github.com/321Team/fds-project-baseline/issues/47)/[#50](https://github.com/321Team/fds-project-baseline/issues/50) 인터페이스: API→engine8001 평가, API→DB5432 저장. engine→DB는 DENY.
- Rule R01/R02/R04/R07은 승인 fixture·사전 기대값을 재사용한다. 이 문서에서 threshold·새 평가 규칙을 만들지 않는다.
- 정상/Rule의 Transaction ID는 API·FDS 결과·DB row와 연결한다. metrics에 transaction-id label을 새 AC로 추가하지 않는다.

## 동일 계약과 환경별 검증

| 환경 | 가능한 준비·시험 | 수용 한계 |
|---|---|---|
| STATIC / MOCK / CI | source/manifest·입력·unit/contract/adapter 오류 제거 | 실제 image pull·SCC·DB·Route·복구 증명이 아님 |
| Shared/Test Kolon Benit OCP Lab | LAB-PRECHECK / COMPATIBILITY / REHEARSAL, 허용 namespace의 admission/UID/health·자체 자원 정리 | 실제 Target 아님. ROSA Runtime/Acceptance·Migration Complete·G5/G6로 승격 금지. RHOAI는 read-only·RESOURCE_GATE=FAIL·Deferred 권고 |
| 실제 ROSA / 승인 Hybrid | #38/#43/#46/#47/#50 Runtime과 실패·복구·최종 회귀 | exact identity·원본·해당 단계 승인·증적 검토에서만 PASS |

Lab identity/version/resource 관측은 [#95 최신 댓글](https://github.com/321Team/fds-project-baseline/issues/95#issuecomment-6032524902)에 있다. APP pin·namespace·허용 작업창/정리는 별도 입력이며 이번 시험계획 갱신에서 admission/Runtime을 실행하지 않았다.
공용 cluster 복구·Operator 설치는 기본 리허설 범위가 아니다. full ROSA recreate·추가 복합장애는 기존 승인 범위 확인 없이 P0 AC로 추가하지 않는다.

전체 범위·P0/P1·Gate는 [최신 Strategy](../../../tests/FDS_Phase2_Test_Strategy_20261007.md)와 [Test Plan](../../../tests/FDS_Phase2_Test_Plan_20261007.md)을 따른다. 16개 초안은 부분 집합이다.

## 실행 시 수집할 추적값

1. 대상 ticket/AC, Case/Window ID, KST start/end, 실행자·호스트·환경.
2. app/source/manifest/IaC commit, 승인 image digest와 actual runtime imageID, Cluster/API/Namespace/Route identity.
3. 승인 fixture 버전·기대값, Transaction ID, API/FDS/DB raw 연결, schema/migration 상태.
4. VPN/route/selector·actual source·firewall/pg_hba·Registry/trust 상태. Credential은 reference만.
5. 명령·종료코드·stdout/stderr 원본, 실패 조건/관측·복구·before/after inventory.
6. 원본 파일/아카이브 해시, 수신·독립 심사·병합 참조, Known Issue와 실행/인수 단계.
7. 유료 작업창은 교육장 리포트의 사용액·예상 총비용·기준시점과 teardown/잔여를 연결. 별도 자체 견적을 필수로 요구하지 않음.

해시 일치는 무결성 판정이다. 템플릿과 합성 자료는 실행 증적으로 편입하지 않는다.
fds-project-evidence 편입에는 기존 독립 리뷰 정책을 적용한다. 이번 준비 파일은 그 저장소에 넣지 않았다.

## #50 일정 쟁점의 처리

[이재환 요청](https://github.com/321Team/fds-project-baseline/issues/50#issuecomment-6013423361): #50 본문의 10-22 하루와 전략의 10-21 대부분 시험/10-22 최종 회귀가 충돌한다.
권장 입력은 #47의 필수 handoff 전체를 먼저 고정한 뒤 같은 승인 Runtime 창에서 주요 시험을 이어서 실행하고 최종 회귀 시간을 확보하는 것이다. 양성 경로 1건만으로는 부족하다. [최신 검토](https://github.com/321Team/fds-project-baseline/issues/50#issuecomment-6041378478)와 [구체 일정안](../20261008/decision-packet.md)을 사용한다.
최종 작업창·기한·일정 속성은 기존 책임자가 이 요청에서 판단하며, 이번 tsv에는 날짜를 고정하지 않는다.

## 다음 단계

#43/#47 actual handoff와 승인 fixture를 받아 초안 case의 입력·명령·기대값·복구를 구체화한다.
source/환경 변경 없는 준비 작업 때문에 기존 P1 Runtime 또는 중앙 prepare 시험을 반복하지 않는다.

