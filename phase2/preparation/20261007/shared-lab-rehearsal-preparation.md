# Shared OCP Lab 호환성·리허설 준비

상태: WORKING REVISION / 실행 NOT_RUN. CODEX_ASSISTED.
최신 사용자 지시와 [#95 2026-10-07 사전분석](https://github.com/321Team/fds-project-baseline/issues/95#issuecomment-6032524902)을 적용한다.
이전 PR150의 독점 교육장 OCP 전제와 cluster 복구 제안은 현재 실행 계획으로 사용하지 않는다. 변경 이력은 Git에 보존한다.

## 환경·인수 경계

```text
Kolon Benit OCP = LAB-PRECHECK / COMPATIBILITY / REHEARSAL
AWS/ROSA = P0 IMPLEMENTATION / RUNTIME / ACCEPTANCE
```

Shared/Test Lab은 실제 Target이 아니다. Lab PASS는 ROSA Runtime PASS·Migration Complete·P0 Acceptance·G5/G6 Exit를 대체하지 않는다.
OCP4.20.0/Kubernetesv1.33.5, Master3/Worker2, Worker각8vCPU/약8GiB는 #95 등록 관측의 소비이며 이번 작업의 직접 재조회 결과가 아니다.
RHOAI Operator 미설치, Catalog3.5.1 제공·기술적 권한/StorageClass 경로 확인. PVC/RHOAI Runtime은 NOT_RUN, RESOURCE_GATE=FAIL·Deferred 권고다. 설치권한이 있다고 설치하지 않는다.

## namespace-local 리허설 순서

| 순서 | 준비/관측 | 경계·중단·정리 |
|---|---|---|
| L0 | 실제 context/identity·Team namespace·Owner/Quota·초기 inventory 읽기 | 대상/허용 범위 불일치 시 중단 |
| L1 | 승인 source/digest의 server-side admission·SCC/UID 조건 | admission을 Running/Ready로 승격하지 않음 |
| L2 | 허용 시험 workload의 arbitrary UID·imageID·Ready/health·RO filesystem/필요 volume 쓰기 | broad SCC/root 우회 없음, 자기 시험 자원만 |
| L3 | 같은 pin의 자체 시험 자원 정리·필요 리허설 재생성 | 보존 대상/공유 자원 건드리지 않음, 삭제 전후 inventory·health 확인 |

APP source/digest·namespace/계정·권한·registry trust·fixture/data 경계·작업창·cleanup 담당은 #38/#42/#43/#50에서 기존 책임대로 고정한다.
공용 cluster/node 복구·drain/reboot·고부하·Operator 설치는 기본 범위에서 제외하며 기존 관리자 허용/별도 승인 범위를 확인하기 전 실행하지 않는다.
RHOAI는 read-only Catalog/support/compatibility만 유지한다. 향후 Go는 별도 CR·ROSA Task·자원/비용/Entitlement·설치/삭제 경로를 따른다.

## 증적·복구·상태

ENV=SHARED_OCP_LAB, Cluster/Version, namespace·실행자/호스트·KST, source/manifest SHA·digest/imageID,
명령/RC/raw·before/after·cleanup·허용범위를 기록한다. 해시는 파일 무결성이고 시험 성공이 아니다.
자체 시험 자원 범위 밖 영향·비밀 노출·권한/SCC 우회·health/정리 실패 시 후속 변경 중단, 원본 보존 후 책임 Lead에 인계한다.
실제 ROSA P0 재검증과 [Strategy](../../../../tests/FDS_Phase2_Test_Strategy_20261007.md)/[Plan](../../../../tests/FDS_Phase2_Test_Plan_20261007.md)을 별도 적용한다.

STATIC=문서 정합 검토 / 신규 MOCK·CI·LAB-PRECHECK·RUNTIME·ACCEPTANCE=NOT_RUN.
REVIEW는 자체 AI 보조 검토이며 사람 독립 승인 아님. MERGE/PUBLICATION은 실제 PR/Release 기록으로 확인한다.
