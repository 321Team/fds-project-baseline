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

| 출력 | 검토 가능한 후보 / 남은 입력 | 책임·소비 |
|---|---|---|
| 1 Registry mode | Harbor Primary 후보, A 우선 상세화. 최종 mode/fallback 미선택 | #42 권욱 |
| 2 endpoint/naming | Harbor 10.1.93.54 또는 harbor.fds.internal 중 실제 image host와 TLS/CA 일치 필요. ECR repository 이름/URI 미정 | #11 하영 / #35·#46 |
| 3 principal/최소권한 | Runner push와 P2 pull 분리. ECR 선택 시 push/pull 및 token 취득·갱신 범위 제출 | #35·#38·#46 |
| 4 trust | Harbor 공개 Root 참조 SHA256 20ddfa5e92c346aaf46fc30179fbc0b069e256effd2615a9f4308a8fe719053f. HCP CLI 지원 확인, pinned rhcs/provider 입력 검증 잔여 | #11 하영 |
| 5 digest/tag | 승인 current/previous manifest·index/child digest를 원본과 연결. 값 미수신 | #43 재환 / #46 권욱 |
| 6 push path | 기존 공급망 소비. ECR 채택 시 repository별 최소권한과 연결 경로 추가안 필요 | #46 권욱 + #35 입력 |
| 7 pull path | private_a→Relay→Harbor443 후보, return·host/DNS·허용 source 확정 필요. A의 ECR 경로도 별도 | #38·#37 / #11 |
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
