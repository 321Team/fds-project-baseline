# Phase 2 플랫폼·이미지 입력 연결 — 2026-10-05
AI usage: CODEX_ASSISTED. 사용자 후속 착수 지시. Phase 1 진행 중 공용 환경 변경 없이 소스/기존 기록을 대조했다.
기준 baseline PR137 입력 HEAD: 6e17e50e4def3a17abee2ec152c5eab1e704af8f.

## 1. 이번에 좁혀진 상태
| 대상 | 직접 조회한 기준 | 판정 |
|---|---|---|
| #35/#38 계정·HCP | 최신 댓글 각80/27건 | 앞선 조회 이후 새 exact version/offering/platform 예산 입력 없음. 기존 요청 반복하지 않음 |
| #43 APP | comment5980505812 | 22:26 현장 요약은 이미 capacity 파생값으로 소비. 원본 수신/최종 P2 digest 아님 |
| infra-rosa | main d5e6226d4e8eca45af757a16bfce5c0b89caf66a; PR2 f5f0db1c50e83b7c9bb5242de9090fdd15cf5720 OPEN | main은 초기 문서 범위. PR2 admission-only 후보, reviews 조회0건. 독립 승인/병합/현장 실행 미확인 |
| fds-msa | main5120b7df72d24ada3dbcf23fc0292fb58ae778af | 현재 소스 읽기 완료. 참조 Kubernetes YAML을 권위 portable base로 승격하지 않음 |
| infra-cicd | main07f7f26d306056203e057b43bdf5234a2de2b8ae | PR45/46 병합 확인. 입력 검증 계약이며 actual Push/Deploy adapter 통합 완료 아님 |

근거: [#35](https://github.com/321Team/fds-project-baseline/issues/35), [#38](https://github.com/321Team/fds-project-baseline/issues/38), [#43 입력](https://github.com/321Team/fds-project-baseline/issues/43#issuecomment-5980505812), [infra-rosa PR2](https://github.com/321Team/infra-rosa/pull/2), [CI PR45](https://github.com/321Team/infra-cicd/pull/45), [CI PR46](https://github.com/321Team/infra-cicd/pull/46).

## 2. APP 소스에서 확인한 것과 실제 이미지의 경계
다음 파일은 fds-msa 위 SHA를 고정해 읽었다.
- [transaction-api Dockerfile](https://github.com/321Team/fds-msa/blob/5120b7df72d24ada3dbcf23fc0292fb58ae778af/transaction-api/Dockerfile), [engine Dockerfile](https://github.com/321Team/fds-msa/blob/5120b7df72d24ada3dbcf23fc0292fb58ae778af/fds-engine/Dockerfile): USER10001:999, /venv/bin/python3 + run.py, PYTHONDONTWRITEBYTECODE=1. 소스에 새 UID 호환 패치를 적용하지 않았다.
- [runtime apko](https://github.com/321Team/fds-msa/blob/5120b7df72d24ada3dbcf23fc0292fb58ae778af/ci/apko/wolfi-python313-runtime.apko.yaml): fdsapp UID10001/GID999, amd64. arbitrary UID 파일권한/실제 기동은 미검증.
- [TA run.py](https://github.com/321Team/fds-msa/blob/5120b7df72d24ada3dbcf23fc0292fb58ae778af/transaction-api/run.py), [engine run.py](https://github.com/321Team/fds-msa/blob/5120b7df72d24ada3dbcf23fc0292fb58ae778af/fds-engine/run.py): 각각 업무8000/8001 및 metrics9091/9090의 두 uvicorn listener를 같은 프로세스에서 구성한다. metrics만 다른 프로세스로 분리하는 임의 overlay를 만들지 않는다.
- engine service 이름 grpc만으로 전송 프로토콜을 결정하지 않는다. 현장 HTTP 보고와 현재 uvicorn 소스는 일관되지만 해당 live digest와 현재 source의 provenance를 증명한 것은 아니다.

현재 소스가 P1 live a7093136…/5e2a081c…를 만들었다고 주장하지 않는다. Dockerfile USER가 고정이라는 사실만으로 arbitrary UID 실행 실패를 확정하지 않으며, 제거만 하면 성공한다고도 판단하지 않는다. 이미지 파일권한·쓰기경로와 실제 SCC/namespace/SA 조건을 분리 검증한다.

## 3. 기존 precheck의 소비 범위
[PR2 script](https://github.com/321Team/infra-rosa/blob/f5f0db1c50e83b7c9bb5242de9090fdd15cf5720/precheck/portability/uid-scc-admission.sh)는 fixed10001:999와 UID/GID 생략 Pod를 server dry-run으로 비교한다. 이미지 실행·pull·Runtime 시험은 없다.
현재 template에는 명시 serviceAccountName이 없고 /tmp emptyDir가 있다. 이것은 generic admission 비교 범위다. 실제 앱 SA/Secret 참조·현장 volumes 없음 조건과 같다고 가정하지 않는다. 최종 portable workload의 admission/실행 결과로 재사용하려면 승인 namespace/SA 및 spec 차이를 연결해야 한다.
Shared OCP admission PASS를 ROSA version/SCC·actual Running/Ready·cold-pull 승인으로 사용하지 않는다. PR2의 기존 MOCK을 이번에 반복하거나 독립 리뷰가 있었다고 표시하지 않았다. 사전입력/검토가 없는 공용 OCP 접속·dry-run도 수행하지 않았다.

## 4. 이미지 공급과 CI Delivery handoff
[Decision110 후속](https://github.com/321Team/fds-project-baseline/issues/110#issuecomment-5980434985)은 현행 P1 이미지 유지와 운영 전환 후속 이관을 보고한다. 수신 #43/#46은 #30에서 확정할 제안이며 P2 최종 인수 완료가 아니다.
- Actions 최근20건 조회: fds-msa main5120b7d의 [Source validation36689255552](https://github.com/321Team/fds-msa/actions/runs/36689255552) SUCCESS. 이는 최종 운영 이미지 공급 성공이 아니다.
- 목록의 apko main368786c [공급36415939069](https://github.com/321Team/fds-msa/actions/runs/36415939069)는 SUCCESS, PR14의 [36512252795](https://github.com/321Team/fds-msa/actions/runs/36512252795)는 FAILURE. 서로 다른 SHA/event이다. 로그/artifact를 이번에 재검증하지 않았으며 실패 원인 또는 전체 실행 이력을 재판정하지 않는다.
- PR45 merge b3d3f15ab4b5877a51d9fa75f00a45edf597e3f0, PR46 merge07f7f26d306056203e057b43bdf5234a2de2b8ae: source receipt·Run/SHA·scan/push digest·rollback·target 계약을 구현한 상태. Token audience는 PRESENCE_ONLY_NO_PINNED_APPROVED_VALUE이고 Runtime adapter는 NOT_INTEGRATED라는 PR 경계를 유지한다.
- P2에서 이 P1 gate를 그대로 복사하지 않는다. 고정 P1 API/namespace/SA/audience·Harbor endpoint 차이를 #46 adapter 계약으로 연결한다. 승인된 기대 audience가 없는 상태를 통과시키려고 값을 발명하지 않는다.

P2 최종 이미지 수신 시 필요한 최소 묶음:
1. 저장소·source commit + build workflow SHA/Run/attempt.
2. exact builder/runtime/lock/wheel 공급 근거 및 image config/manifest 관계.
3. 같은 이미지의 scan 결과·기준·검토 기록.
4. 실제 remote repository@sha256 및 push receipt.
5. P2 승인 namespace/SA·pull-secret reference·trust/endpoint·UID 실행 조건, 이전 승인 digest 및 rollback.
6. 이후 actual imageID·Ready/health·업무 및 negative/cleanup 증적.
1~5의 준비/선택과6의 생성 후 실제 결과를 구분한다. Secret 값/토큰은 handoff에 넣지 않는다. 기존 P1 재빌드·Push·Deploy·rotation을 중복 실행하지 않는다.

## 5. 플랫폼 입력은 생성 전/후로 분리
| 시점 | 기존 producer에서 소비할 입력 | P2에서 할 일 |
|---|---|---|
| 생성 전 | 선택 HCP version·region·private model·지원 type/AZ/pool 조건과 조회시각/근거 | 기존 3×m5.xlarge 후보와 비교; 지원값 발명 금지 |
| 생성 전 | 선택 모델의 platform/DaemonSet·예약/여유 가정과 근거, APP rollout·배치/PDB 조건 | 기존 capacity JSON 앱 소계에 결합한 설계 예산; 가정/측정 구분 |
| 생성 전 | 계정 linkage/권한·named quotas 및 reviewed IaC plan, 비용 한도·가동창 | 기존 #35/#38 입력 소비; Create/Apply 승인 아님 |
| 생성 후 | 실제 worker allocatable/platform requests·node/AZ/Pod 배치 | 설계 예산과 대조하고 N-1/surge 실제 검증 |
| 생성 후 | 실제 endpoint/ENI/route/SG·pull source·imageID·업무 결과 | DNS/TLS/auth/cold-pull/복구 인수 연결 |

실제 allocatable/endpoint가 없다는 이유로 생성 전 논리 설계를 순환 차단하지 않는다. 반대로 예산/지원이 미확인인 채 gross 사양만으로 생성 GO를 선언하지 않는다.
비용은 기존 합의대로10-06 사용자 텍스트 대기. null을0으로 바꾸지 않는다.

## 6. 완료 범위와 다음 trigger
이번 완료: source5개(Dockerfile2/run.py2/apko1) 및 admission script/README 대조, 관련 PR 병합/리뷰 상태·Actions20건·Decision 기록 확인, handoff와 pre/post-create 경계 정리.
실제 빌드·기동·SCC·AWS 조회·지원/비용 측정·독립 리뷰·공용 환경 변경은 수행하지 않았다.
새 입력이 없는 #35/#38/#42에 같은 요청을 추가하지 않는다. 다음 trigger는 기존 producer의 support/budget 또는 최종 supply/delivery 결과 수신이다. 그때 달라진 입력만 반영한다.
STATIC_SOURCE_RECONCILIATION=RECORDED / PLATFORM_INPUT=PARTIAL / FINAL_P2_IMAGE=PENDING / SHARED_RUNTIME_CHANGE=NOT_RUN / FREEZE=HOLD.
