# D22 Lead 선행 검토·선택안 — 2026-10-08

CODEX_ASSISTED. 권욱 담당 #42/#46 준비 문서. 검토 대상은 [하영 제안 6053923723](https://github.com/321Team/fds-project-baseline/issues/42#issuecomment-6053923723)이다. `PREPARATION_REVIEW=COMPLETE / REGISTRY_MODE=PENDING / FALLBACK=PENDING / D22=PENDING`. 이 문서는 ECR 생성·IAM 부여·이미지 복사·Harbor 변경·D22 Final을 승인하지 않는다.

## 검토 판정과 권고

**Harbor Primary + P2 전용 pull-only의 준비 방향은 기존 후보와 정합한다. A(ECR 수동 전환)를 우선 상세화하되, 아래 수용조건을 충족하기 전 실제 fallback으로 선언하지 않는다.** B(복구 대기)는 자동 채택하지 않는다. A를 준비할 수 없는 경우 B의 배포 중단 영향을 명시해 Lead가 최종 선택한다. 신규 상시 Support 승인 단계를 만들지 않는다.

| 비교 | A: ECR 수동 전환 | B: 대체 Registry 없음 |
|---|---|---|
| Harbor 단독 장애 | 사전에 보존한 승인 digest를 확인하고 대상 이미지 참조를 제한적으로 전환 | 신규 rollout·cold-pull을 중단하고 Harbor 복구 대기 |
| VPN 장애 | ECR 경로가 정상이라면 이미지 취득 경로는 독립적으로 사용 가능. On-Prem DB 업무 복구는 보장하지 않음 | Harbor pull·DB 경로 모두 VPN 복구 의존 |
| 기존 실행 Pod | 기존 건강한 workload 유지 우선. 새 rollout은 별도 판단 | 캐시가 있다는 가정으로 재생성 성공을 선언하지 않음 |
| 추가 작업 | repository/IAM·push 및 node-pull 인증·digest 보존·만료 대응·전환/복귀·정리 | Harbor/Robot 복구 담당·중단/재개 조건·정리 |
| 선택 조건 | 지원 인증/경로, 승인 source·scan·digest, 실제 cold-pull, 회귀/복구 및 작업창 확보 | 배포 지속성 제한을 #42/#47 결정·Known Issue에 명시하고 기존 AC 충족 여부 판단 |

## 원제안 보완 사항

1. **VPN 장애를 Registry 비교에서 제외하지 않는다.** #42는 Hybrid 장애 시 배포 지속성 비교를 요구한다. 이미지 취득/배포 가능성과 DB 의존 업무 가능성을 따로 기록한다. A가 DB를 복구하지 않는다는 이유만으로 이미지 공급 효과까지 없다고 판정하지 않는다. ECR 자체의 DNS/egress/인증 실패도 별도 실패 경로다.
2. **“단방향”은 연결 개시 방향이다.** worker→Harbor TCP443의 응답/return 경로를 포함한다. stateful SG와 stateless ACL/현장 방화벽의 반환 조건을 각각 검토한다. worker subnet 후보를 DB 허용 source-set이나 전체 VPC 허용으로 확대하지 않는다. node pull과 Pod egress/NetworkPolicy는 분리한다.
3. **비용 $1 미만·차이 없음은 확정 근거가 아니다.** 원제안의 가정 단가를 그대로 쓰면 이미지 1개 0.2GB×$0.10/GB-month=$0.02/month다. $0.12는 6개 사본 등 별도 가정이 있어야 한다. 0.2GB×3노드×$0.059/GB=$0.0354이며 $0.07은 2개 이미지 등을 가정한 값이다. 이는 단위/가정 대조일 뿐 최신 단가 검증이나 프로젝트 견적이 아니다. 실제 이미지 수·크기·캐시·재시도·보존·경로·과금항목이 미결이므로 총액 상한으로 소비하지 않는다. 사용액·예상 총비용 판단은 교육장 리포트만 사용한다.
4. **복사 후 digest 일치를 실제로 확인한다.** 승인 source/build/scan→Harbor manifest/index→ECR manifest/index와 platform별 child digest를 연결한다. 재빌드·미검토 형식 변환·tag 자동 대체는 허용하지 않는다. ECR은 digest pull 시 manifest 변환을 제공하지 않으므로 클라이언트의 형식 지원도 확인한다. [AWS manifest 문서](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-manifest-formats.html).
5. **ECR 인증 수명을 설계한다.** 일반 ECR authorization token은 12시간 유효하다. 수동으로 한 번 넣은 pull Secret을 프로젝트 기간 내내 유효하다고 취급하지 않는다. 선택 ROSA/HCP의 지원 인증 방식·IAM principal·갱신/전달/회수·만료 시 STOP을 #38/#46에서 확인한다. [AWS 인증 문서](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html). ECR 공인 CA는 사설 CA 추가가 불필요하다는 뜻이며 인증 불필요라는 뜻은 아니다.
6. **Robot 사전 교체는 가용성 보장과 다르다.** 기존 10/16·10/18 만료는 생산자 과거 보고다. P2가 소비할 실제 pull-only scope/expiry/reference를 확인한다. 이 작업에서 Phase 1 Robot 변경·rotation을 실행하지 않는다. 기존 이전 digest가 Harbor에만 있으면 Harbor 장애 시 rollback도 실패할 수 있으므로 A에는 승인 previous digest도 보존 후보로 포함한다.

## D22 12개 출력의 현재 준비 상태

17:40 [#10 검토](https://github.com/321Team/infra-rosa/issues/10#issuecomment-6056067704)·[#11 검토](https://github.com/321Team/infra-rosa/issues/11#issuecomment-6056068014)를 수신했다. evidence main `9472f17f13dd6828b6895a47552dcdb9778fb25d`의 leaf·Robot 목록 증적은 각각 PR163·165로 병합됐다. 공개 Root SHA 재대조, leaf 7파일·목록 이미지 1파일 해시 일치 및 FQDN/IP 오프라인 인증서 검증 PASS는 저장된 자료 검증 범위다. 현재 서버 IP TLS·ROSA key 동작·cold-pull 성공은 미검증이다. Runner의 OS/CI/Podman trust 및 실제 principal은 부분 입력이며 날짜만을 위한 P1 재시험은 요청하지 않는다.

| 출력 | 검토 가능한 후보 / 남은 입력 | 책임·소비 |
|---|---|---|
| 1 Registry mode | Harbor Primary 후보, A 우선 상세화. 최종 mode/fallback 미선택 | #42 권욱 |
| 2 endpoint/naming | Harbor 10.1.93.54 또는 harbor.fds.internal 중 실제 image host와 TLS/CA 일치 필요. ECR repository 이름/URI 미정 | #11 하영 / #35·#46 |
| 3 principal/최소권한 | Runner push와 P2 pull 분리. ECR 선택 시 push/pull 및 token 취득·갱신 범위 제출 | #35·#38·#46 |
| 4 trust | Harbor 공개 Root SHA256 20ddfa5e92c346aaf46fc30179fbc0b069e256effd2615a9f4308a8fe719053f 후보 수용. exact image host/key·JSON/정규화 map·해시·생성 방법·소스 SHA·CLI/provider pin 잔여. PEM 해시만으로 key/실행 설정 무결성을 대신하지 않음 | #11 하영 |
| 5 digest/tag | 승인 current/previous manifest·index/child digest를 원본과 연결. 값 미수신 | #43 재환 / #46 권욱 |
| 6 push path | 기존 공급망 소비. ECR 채택 시 repository별 최소권한과 연결 경로 추가안 필요 | #46 권욱 + #35 입력 |
| 7 pull path | private_a→Relay→Harbor443 후보, source 보존/return·host/DNS·허용 source 계약 필요. P0 IP 후보는 D23 전체 DNS 결정을 무조건 기다리지 않음. 승인된 최소 경로 구현·cold-pull은 Basic Ready 판정 전, Final은 그 결과를 소비. A의 ECR 경로도 별도 | #38·#37 / #11 |
| 8 fallback | 아래 전환/복귀 절차 후보. 자동 mirror 설정은 미선택 | #42 권욱 |
| 9 비용 | 교육장 사용액/예상 총비용 리포트 미수신, NOT_ASSESSED. 400/450/500·자부담0·예비50 유지 | #34/#42 권욱 |
| 10 credential reference | owner/scope/expiry/전달·회수 reference 필요. 원문 토큰/Secret 금지 | #38·#46 |
| 11 evidence/source refs | 원제안, [ROSA 설계 승인](https://github.com/321Team/infra-rosa/issues/3#issuecomment-6054292320), #11 raw/지원 결과, 이후 실제 cold-pull/negative/복구 | 각 생산자 → 권욱 |
| 12 D22 결과 | PENDING. Basic Ready 후 실제 자료로 GO:<mode> 또는 NO_GO와 IF-19·소비조건 기록 | #42 권욱 |

## 전환·복귀 절차 후보와 중단조건

실제 실행 전 대상 Cluster/Namespace/Deployment/container와 current/previous 승인 digest, credential reference, 관리 경로, 확인 시간상한/원복 범위를 고정한다. 아직 없는 endpoint·Secret·명령 인자는 만들지 않는다.

1. 장애를 Harbor/TLS/auth, VPN, ECR egress/auth, DB로 분류하고 기존 workload/rollout 상태를 수집한다. 원인 불명·credential 만료·관리 경로 불가면 변경 STOP.
2. A가 최종 선택됐고 ECR에 승인 current/previous digest가 존재하며 실제 pull 권한·경로가 확인된 경우에만 전환한다. 허용 workload/container의 image reference만 변경하고 source·config·DB 변경은 섞지 않는다.
3. rollout·actual imageID·health 확인. DB가 불가한 경우 이미지 pull 성공과 업무 실패를 분리하며 업무 PASS를 선언하지 않는다. 캐시 hit만으로 cold-pull을 대체하지 않는다. 기존 #42 시험에 연결하며 승인 없이 별도 장애주입을 하지 않는다.
4. 실패/UNKNOWN이면 상태를 재조회하고 검증된 이전 경로·digest로 복구 가능한 경우에만 복귀한다. Harbor 장애 중 Harbor로 무조건 되돌리는 절차를 만들지 않는다. 안전한 이전 이미지도 가져올 수 없으면 추가 변경 중단·가용 Pod 보존·장애 기록.
5. Harbor 복구 후 strict TLS/권한/pull을 확인하고 Lead의 재개 판단으로 primary 복귀한다. image rollback이 DB 데이터 복구를 의미하지 않는다. 임시 권한/credential·불필요 복제본 정리는 보존·증적 확인 후 수행한다.

생성 전에는 trust/경로/principal·실패복구 계약까지만 준비한다. actual ROSA cold-pull은 생성 후 Basic Ready 단계에서 확보하며 이를 생성 전 Gate로 당기지 않는다. 현재 Runtime·ECR 생성/복사·Secret 등록·D22 Final 모두 NOT_RUN/PENDING이다.

## 10/13 보완 — 미결 인증·전환·복귀의 결정 카드

CODEX_ASSISTED. 10/13 17:48 KST까지의 접수 기록을 소비한다. 기존 A/B 비교·12개 출력·5단계 전환 절차는 유지하며 아래는 미결을 닫기 위한 입력이다. **REGISTRY_MODE/FALLBACK/D22 Final=PENDING**, 실제 Secret 발급·갱신·전환 미실행.

### 이미 닫힌 준비 입력

[infra-rosa#11](https://github.com/321Team/infra-rosa/issues/11)은 CA/경로 준비 입력으로 CLOSED다. CA JSON 4,114 bytes, SHA256 `4d86507ecd81789e376669940f68b2dbb27f5989e6fd4315238c9f61a2401da4`, key `10.1.93.54`와 `harbor.fds.internal` 및 [evidence PR170](https://github.com/321Team/fds-project-evidence/pull/170)·[PR186](https://github.com/321Team/fds-project-evidence/pull/186)의 기존 편입/독립 검토를 재사용한다. 이는 위 12개 출력 중 4번의 **준비 입력 잔여**를 갱신한다. 이번 문서 작성에서 원본 재해시나 실제 trust 적용을 수행한 것은 아니다.

Harbor 반환 경로 `10.20.0.0/16 via 10.1.93.51` 및 worker `10.20.10.0/24 → 10.1.93.54:443`는 준비 계약의 후보이며 실제 반영/통신 증적과 구분한다. 경로 준비 → 생성 시 승인 CA 입력 → 생성 후 cold-pull → Basic Ready → D22 Final 순서를 유지한다. CA 자료·기존 A/B 원본의 재제출을 요구하지 않는다.

### 인증 갱신 입력 — 실제 값은 해당 생산자가 한 번 인계

| 대상 | 필요한 최소 필드 | 책임 / 지금의 상태 | 갱신 실패·권한 부족 시 |
|---|---|---|---|
| Harbor P2 pull | 승인 image host/project 범위, credential reference·owner·만료 KST, 갱신/폐기 담당, 안전 전달 위치 | #38 이하영·Registry 생산 이재환 → #42/#46; 실제 principal/만료 미수신 | 신규 rollout STOP, 기존 Pod·증적 보존. Phase1 Robot을 이 작업으로 교체하지 않음 |
| Harbor Runner push | push 대상 project/repository·principal 범위, pull과 분리 여부, current/previous digest receipt | #46 이권욱, 기존 Build/Scan·Registry 생산 입력 소비; 실제 remote digest 미수신 | push 실패를 build/scan 성공으로 대체하지 않음. tag/rebuild로 승인 digest 변경 금지 |
| ECR fallback A | 지원 ROSA HCP 버전의 pull 인증 방식 근거, token 발급 principal/범위·reference·만료, 갱신 주체·방법·실패 STOP | #38 이하영의 플랫폼 지원 입력 + #46 이권욱의 공급 인계; 방식 PENDING | 지원/갱신 증명 전 A를 “즉시 전환 가능”으로 표시하지 않음. 새 IAM/Secret 발급은 별도 실행 판단 |
| 공통 검증권한 | 승인 대상·최소 범위와 마지막 필요한 시험/재시험·증적 검토 종료조건 | 기존 결정 재사용; 새 정책 부여/재부착 승인 아님 | 파일 전송/작업창 종료만으로 반복 회수하지 않음. 검증 종료 후 전용 권한 정리, 운영 최소권한 구분 |

ECR authorization token은 발급 IAM principal의 권한 범위를 따르며 12시간 유효하다. Docker credential helper 자체는 MFA를 지원하지 않는다. 이것만으로 ROSA HCP에서 사용 가능한 자동 갱신 방식이나 본인 MFA 예외가 입증되지는 않는다. [AWS 인증 문서](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html), 10/13 조회.

인증 receipt에는 `issued/expires/last_verified KST`, 비밀값 없는 reference, 검증 대상, 갱신 책임, 실제 결과 링크만 남긴다. 갱신 시점은 **남은 작업창과 복구·증적 수집에 필요한 유효시간을 확보하는 조건**으로 정하고 근거 없이 고정 주기나 장기 자격증명을 추가하지 않는다. 실제 지원 방식이 확인되기 전 갱신 자동화 코드를 배포하지 않는다.

### 상태별 권장 판단표 — A/B 최종 선택 아님

| 관측 조건 | 다음 행동 | 재개/복귀 완료조건 |
|---|---|---|
| Harbor 정상·승인 current/previous pull 가능 | 선택 Primary 유지, 기존 시험 결과 재사용 | exact host/TLS/principal/digest와 Runtime imageID·health 대응 |
| Harbor 장애, A 최종 선택 및 ECR 입력 완비 | 기존 5단계 절차의 한정 전환 판단 | 승인 index/child digest 보존, ECR 실제 pull/TLS/권한, 복구 가능한 이전 이미지 확인 |
| Harbor 장애, A 미선택 또는 auth/이미지 미비 | 신규 rollout 중단·가용 workload 유지 | Harbor 회복 또는 A 계약/해당 실행 승인 충족; 임의 B 최종 선택으로 기록하지 않음 |
| VPN 장애, ECR pull 성공 | 이미지 경로 결과만 수용; DB 업무 상태 별도 판정 | #47 DB 경로·업무 증적 없으면 Hybrid PASS 금지 |
| token 갱신 실패/만료 또는 전환 응답 UNKNOWN | 자동 재시도·추가 rollout 중단, 실제 상태 확인 | 기존 승인 범위 내 유효 인증·상태 대조. 재실행은 별도 RUN/대상으로 판단 |
| Harbor 복구 | strict TLS·정상 pull·이전 digest·업무 영향 확인 후 Lead 복귀 판단 | 양쪽 Registry 원본/변경·복구 기록 수신. 실패하면 추가 변경 중단, 건강한 Pod 보존 |

ECR의 digest pull에는 manifest 형식 자동 변환이 없다. 복사 시 원본 index/child digest와 소비자 지원 형식을 확인하며 변환·재빌드·tag 대체로 같은 이미지라고 간주하지 않는다. [AWS manifest 문서](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-manifest-formats.html), 10/13 조회.

**후속 조건:** #38 지원 인증/경로 계약 → #43/#46 실제 current/previous 공급 → 승인 창의 cold-pull/negative·복구 → #42 D22 Final. 하영·재환은 기존 인계에 누락 필드만 보완한다. 이권욱은 교육장 리포트로 비용을 중앙 판단하며 추가 단가표·중복 비용 승인이나 지금의 ECR 생성을 요구하지 않는다.

10/13 18:28 추가 수신: [Harbor 운영 후속 기록](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-6142413961)은 Harbor10개 healthy·restart=always 유지, 자동복구 관리자 활성화 실패 후 HOLD/정책 원복 완료를 보고한다. **Registry 서비스 상태와 자동복구 관리자 인수 상태를 분리**해 D22에 소비한다. 이번 작성자가 원본/실제 서버를 검증한 것은 아니며 P1 관리자 재활성화·H6·SELinux/lock 수정 시험을 이 준비 범위로 가져오지 않는다. 이 보고만으로 Harbor 서비스 전체 장애 또는 P2 cold-pull/복구 PASS를 선언하지 않는다.
