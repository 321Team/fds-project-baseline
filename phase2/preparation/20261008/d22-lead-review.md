# D22 Lead 선행 검토·선택안 — 2026-10-08

## 10/19 12:21 KST — CASE2 최소 변경 준비

이권욱 / CODEX_ASSISTED. [D22 A 채택](https://github.com/321Team/fds-project-baseline/issues/42#issuecomment-6207939448)은 유지한다. [cold v5 STATIC 수용](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6258893270)은 원본13/13·Judge18 PASS이며 실제 node pull/FINAL과 다르다.

[S1 보고](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6258748604)는 승인된 P2 principal·Harbor 허용 적용 증적을 연결하지 못했다는 기록 조사다. Harbor 실계정 부재를 독립 확인한 결과는 아니다. 현재 CASE2/새 준비·cold 실행 HOLD로 소비한다. P1 robot$worker 소비 확대, robot$push 목적 외 사용, P1 CA/암호 회전으로 우회하지 않는다.

| #13 기존 실행 카드에 넣을 내용 | 최소 범위·완료조건 |
|---|---|
| P2 인증 | 이미 승인된 객체가 실제 확인되면 재사용 판단. 새 발급 시에만 P2 Robot1개/fds 프로젝트 pull-only/유한 만료·소유/갱신/회수 담당. 비공개 원문, 공개는 reference/scope/expiry만 |
| Harbor 허용 | 필요한 source10.20.10.0/24→10.1.93.54:443 추가분과 반환 경로. 기존 적용분은 중복 반영 안 함, 기존 P1 허용·운영 접근 보존 |
| Runtime 경계 | 하영/Harbor 소관 Lead가 대상·변경·기간·복구/P1 기준선 영향을 연결. STATIC 수용은 승인 대체 아님. root/새 IAM/DB 변경을 끼워 넣지 않음 |
| 정리/회수 | 변경 전 기준선과 추가 객체/규칙 식별→기존 P1 동작 보존→해당 추가분만 회수/원복→reference/허용 readback. 모르는 현재값을 삭제 근거로 쓰지 않음 |
| cold 진입 | 별도 승인 후 v5의 privileged debug·도구·identity/UID·strict TLS·counter/config 근거·안전 정리를 해당 창에 연결. 키트가 Robot/Secret/Harbor/경로를 만드는 것은 아님 |

endpoint·기존 CA·D7 current2/previous=NONE 재사용. 갱신은 새 reference/expiry만 전달. auth/TLS/digest 실패는 신규 rollout STOP·정상 Pod 보존; 준비된 ECR A만 기존 수동 전환/복귀 계약으로 소비한다. 새 ECR 생성/비용 GO·자동 fallback 없음.

보수적 가용시간 후보: v5 앱1개62분×2=124 + 개폐·준비60 + 실패/복구60 + 반출/검토30 = **274분, 약5시간**. 실측/예약이 아니며 담당·실제 범위로 조정한다. IAM 최대3시간·실제 credential/OAuth 수명·DB runtime120분을5시간과 혼합하지 않는다. DB 예외는 cold 창에 자동 포함되지 않는다. 날짜/시각·겹침·운영 담당은 미배정이다.

권욱의 다음 판단: 정확 최소 변경/실제 유효 입력→해당 Runtime/cold GO→node pull/negative·복구·앱 소비→D22 FINAL. 추가 단가표·중복 비용 승인·이미지 재빌드는 요구하지 않는다.

## 10/16 18:25 D7 원본 소비 완료

이권욱 / CODEX_ASSISTED. [재환 D7 전달](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6209302835)과 [하영 수신·SEC 사후 수용](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6209352775)을 확인한 뒤, 고정 비공개 공유 경로의 `d7-manifest-20261016` 6파일을 직접 수신했다. `SHA256SUMS` SHA256은 `27c38649f135b927305d0543d9b996bacc9dc67d61f6430828ff0910527280f6`, 내부 **5/5 일치**다. 작성자 전달·하영 수신·이번 권욱 수신/재해시/내용검토를 구분한다. 공개 저장소에는 raw·헤더·credential을 추가하지 않는다.

| 앱 | 이번 수신 manifest SHA256 = P2 current digest | 내용 검토 |
|---|---|---|
| transaction-api | `338b8a2871507ce8b42deedc916b26e350577ee6efd18df23d7ff2dd4b17dff0` | 1,168B, OCI image manifest, 4 layers, 최대25,903,816B·합계48,917,992B |
| fds-engine | `8b257adb08b6d381f72b66d3386efea6112a8f072ecfafcbcd463bcd1c3be89d` | 1,167B, OCI image manifest, 4 layers, 최대25,903,816B·합계38,487,502B |

두 원문은 index가 아니므로 이 입력에 별도 child manifest를 요구하지 않는다. 최대 layer는 모두 키트의4MiB 기준을 충족한다. 이는 수신 manifest의 선언 크기 확인이며 layer 다운로드·압축 해제·이미지 실행 확인이 아니다. redacted 헤더의 HTTP200·Content-Length/Type·Docker-Content-Digest 대응 및 sid 가림을 확인했다. live TLS·인증·쿠키/토큰 삭제 실측을 뜻하지 않는다.

추적 경로는 기존 source `affbc69` → TBS38395350748 → Push38404449622 → [P2 채택 PR37의 병합된 계약](https://github.com/321Team/fds-msa/blob/c9c42cc1cc0c135320b81480984941f2a118f592/deploy/DELIVERY-CONTRACT-rosa.md) → 이번 raw digest로 연결한다. 최초 **previous=NONE**을 유지한다. manifest 자체에는 플랫폼 필드가 없다. config digest `ab34196b…ffee`/`b82d35a6…f4fc`를 기존 공급 [api-image.json](https://github.com/321Team/fds-project-evidence/blob/7ec3d5e162b5042b8201b107b0fd5142e182f714/evidence/P1-APP-01/d03-isolated-runtime-20261014T2110/received/supply/FDS_D03_Supply_202610142110/api-image.json)·[engine-image.json](https://github.com/321Team/fds-project-evidence/blob/7ec3d5e162b5042b8201b107b0fd5142e182f714/evidence/P1-APP-01/d03-isolated-runtime-20261014T2110/received/supply/FDS_D03_Supply_202610142110/engine-image.json)의 Id와 대조해 **linux/amd64 기록**에 연결했다. 두 참조 파일 SHA256은 각각 `98101108302bf5f758cc444e9aeefe4b00de4c2ffca13914e8a8f13cc0752cfc`, `8eefe814efa468c9d85631c0edae3e4deb12c59b7e91cdbe5655933169ef36f9`다. 실제 ROSA SCC/UID 실행은 미검증이다.

`robot$push` 사용은 생산자가 사전 HBR 확인 없이 수행했다고 보고했고, 하영은 해당2GET에 한해 사후 수용했다. 이를 사전 승인·새 용도 허용·권욱의 실제 정리 검증으로 바꾸지 않는다. 다음 원문 조회/cold-pull은 기존 #13의 P2 pull-only 계약을 따른다. 이번 준비를 이유로 P1 Robot·CA·Harbor 설정을 변경하거나 이미 받은 manifest를 재수집하지 않는다.

**해소:** 기존12출력 중5/11의 current 원문·형식·선언 크기·공급 연결 및 #12 D7 소비 입력. **잔여:** 하영의 P2 실제 endpoint·pull 인증 reference/수명·승인 경로/cold-pull, 재환의 승인 host/Registry를 반영한 clean render, 권욱 #46의 actual provider/CLI와 소비 검증. ECR 사본의 digest 보존·인증·전환/복귀는 해당 실행 시 확인한다. `D7_INPUT=ACCEPTED / D22_FINAL=PENDING_RUNTIME / 새 RUNTIME=NOT_RUN`; 생성 전에 cold-pull·중복 빌드/전체 시험을 요구하지 않는다.

## 10/16 A안 채택과 소비 완료조건

2026-10-16 17:02 KST · CODEX_ASSISTED. [#42 채택6207939448](https://github.com/321Team/fds-project-baseline/issues/42#issuecomment-6207939448)에 따라 **REGISTRY_DIRECTION=HARBOR_PRIMARY_ECR_MANUAL_A / D22_FINAL=PENDING_RUNTIME**이다. 아래 과거 미선택 문구를 현재 미결로 재사용하지 않는다. A 방향 재선택은 필요 없고 지원 인증·실측·완료조건은 남는다.

| 기존 출력 | 현재 소비 계약 / 완료조건 |
|---|---|
| 1 mode / 8 fallback | Harbor Primary + P2 pull-only + ECR 수동 A 채택. 자동 전환/복귀 없음. A 미준비면 신규 rollout STOP, B 자동 선택 아님 |
| 2 endpoint / 4 trust / 7 path | 기존 CA/map·IP/경로 준비 접수 재사용. 하영 actual endpoint·동일 source의 CA/config/지원 버전·승인 경로 strict TLS/node cold-pull은 생성 후 연결. P1 CA/route 임의 변경 없음 |
| 3 principal / 10 credential | 하영 지원 P2 pull 방식·owner/scope/expiry/갱신·폐기 reference → 권욱 소비. 만료/갱신 실패면 신규 rollout STOP·기존 Pod/증적 보존. 실제 비밀/추가 IAM은 이 문서에 없음 |
| 5 digest / 6 push | [#43 P2 current 채택 수용](https://github.com/321Team/fds-project-baseline/issues/43#issuecomment-6186106346)과 기존 source/build/scan/push 원본 재사용. **앱별 최초 previous=NONE**. ECR 사본 index/child digest·형식·지원 pull 확인. 재빌드/재Push 중복 요구 없음 |
| 9 비용 | 교육장 리포트 기반 권욱 중앙 판단. 지원·자부담0·400/450/500 유지. 10/16 표 $7.95/₩10,860, 기간/예상 미확인. 방향 채택은 ECR 자원/추가 비용 실행 GO가 아님 |
| 11 원본 / 12 Final | 공유→수신→재해시→내용검토 분리. 생성 후 승인 경로/cold-pull→Basic Ready→전환/실패/복귀 및 기존12출력 검토로 Final 판단. 문서/해시만으로 Final 아님 |

첫 배포 실패·부분 적용·timeout/UNKNOWN은 STOP·readback·원본 보존이며 가짜 previous/P1 롤백 이미지를 사용하지 않는다. 검증·승인된 첫 P2 배포를 다음 previous로 쓸 때 source/render/contract/digest/설정·승인 reference를 함께 결속한다. 재환은 Registry/host 확정 후 clean render를 연결하고 권욱은 #46에서 소비한다. PENDING host/actual UID 합성 금지.

아래 전환/복귀5단계를 재사용한다. Harbor 장애 중 복구 불가한 Harbor로 자동 복귀하지 않으며 A는 이미지 공급만 대체한다. VPN/DB 업무 복구와 실제 ECR/IAM/복사/Secret/Harbor 변경은 별도 판단이다. [전체 Gate·인계 갱신](readiness-handoff-20261016.md)을 함께 소비한다.

## 10/15 미결 선택을 위한 소비 순서

기존12출력·인증 갱신·A/B 비교·앱별 current/previous 표를 재검토했다. **권고는 Harbor Primary 준비 + A 수동 ECR 대안의 조건 검토를 유지**한다. D22 Final/실제 A 채택은 아직 PENDING이며 권욱의 새 선택으로 기록하지 않는다. 이번에는 새 Registry 설정이나 P1 인증 갱신을 수행하지 않았다.

| 지금 판단 가능한 것 | 준비 판단 | 최종 판단을 바꾸는 실제 입력 |
|---|---|---|
| P0 IP와 D23 관계 | #40/#48 보류가 기존 IP 기반 CA/경로 검토를 막지 않음 | 실제 선택 endpoint의 TLS/CA·node pull 계약. DNS 보류를 해제하지 않음 |
| 인증 갱신 실패 | 신규 rollout STOP·기존 정상 workload 보존, 지원된 동일 범위 복구 후 재개 판단 | 하영 P2 pull 방식·owner·만료/갱신 reference 및 권한, 비밀값 제외. 이미 받은 CA 재제출 없음 |
| A 전환/복귀 | 자동 전환·자동 복귀 없음. current와 previous 공급을 먼저 보존해야 복구 후보가 됨 | 재환 app별 P2 채택/previous·원본 receipt, 하영 지원 auth/경로. 권욱 C3 비용 변경분 판단은 기존 ROSA Cost GO와 분리 |
| A 미준비 | 신규 rollout 중단은 안전 조치이고 B 최종 선택이 아님 | B 채택 시 배포 지속성 제한·기존 AC 영향/승인 대안을 권욱이 결정 |
| 완료 시점 | 생성 전 계약 → 승인 생성 → cold-pull → Basic Ready → D22 Final | 실제 Runtime 및 실패/복귀 원본이 필요. cold-pull을 생성 전 새 차단으로 요구하지 않음 |

지금의 생산자 요청 범위는 기존 인계의 **실제 P2 인증 방식/갱신 책임, 앱별 P2 채택 current/previous** 미결뿐이다. 재빌드/Push·상세 단가 재계산·전체 재시험은 요구하지 않는다. 10/15 08:57 KST 지정 비용 세션 재조회에서도 최신 입력은10/14 $2.85이고 기간/cutoff/예상은 미확인이다. 새 비용/Runtime 승인을 발행하지 않았다.

아래10/08~10/14 비교·증적은 해당 시점 자료로 재사용한다.

**10/14 현재 소비 기준:** 아래 A 우선 상세화·B 대안은 그대로이며 D22 Final은 PENDING이다. 최신 P1 Push 증적·P2 인증 경계는 문서 끝 10/14 보완을 따른다. 과거 “remote Push 미확인”은 작성 당시 이력이며 P2 cold-pull 미실행과 구분한다.

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
| 2 endpoint/naming | 아래 인계 원본의 실제 image host는 `10.1.93.54`. CA JSON의 IP/FQDN 두 key 접수는 완료. P2 채택/실제 TLS·pull 결과는 별도이며 ECR repository 이름/URI는 미정 | #11 하영 / #35·#46 |
| 3 principal/최소권한 | Runner push와 P2 pull 분리. ECR 선택 시 push/pull 및 token 취득·갱신 범위 제출 | #35·#38·#46 |
| 4 trust | 아래 #11 CLOSED 인계의 exact CA JSON 4,114B·SHA·IP/FQDN key 및 지원/경로 준비 접수 완료를 재사용. 실제 생성 config와 버전/실행 source 결속·trust 적용/cold-pull은 잔여. 이미 받은 JSON/map/hash를 다시 요청하지 않음 | #11 하영 → #38 실제 구현/관측 |
| 5 digest/tag | 앱2종의 새 P1 Push digest 원본은 아래10/14 대조로 접수. 각 앱의 P2 current 채택·previous와 필요한 index/child 대응은 미확인 | #43 재환 / #46 권욱 |
| 6 push path | 기존 공급망 소비. ECR 채택 시 repository별 최소권한과 연결 경로 추가안 필요 | #46 권욱 + #35 입력 |
| 7 pull path | #11의 private_a→Relay→Harbor443·source 보존/return 경로 준비는 재사용. 실제 node-source/반환 경로 구현·allow/deny·cold-pull은 미확인. D23=DEFERRED여도 기존 IP/public DNS 준비는 진행 가능. Basic Ready 전 실제 최소 경로 검증 후 Final에 소비. A의 ECR 경로는 별도 | #38·#37 / #11 |
| 8 fallback | 아래 전환/복귀 절차 후보. 자동 mirror 설정은 미선택 | #42 권욱 |
| 9 비용 | [ROSA Cost GO](https://github.com/321Team/infra-rosa/issues/4#issuecomment-6143326582)는 명시 범위 승인. **C3 ECR은 제외**이므로 D22의 ECR 선택/비용으로 자동 승계하지 않음. cutoff·전체 예상 총비용 미확인, 400/450/500·자부담0 유지 | #34/#42 권욱. 같은 ROSA 범위 재승인·구축 담당자 재견적 요구 없음 |
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

## 10/14 공급 증적·인증 수명·복구 소비 보완

00:25 KST GitHub 조회에서 [새 Push PR218](https://github.com/321Team/fds-project-evidence/pull/218) HEAD `9647a83724dea442c9e8238e60d68bfe2602dc8d`와 [Deploy PR219](https://github.com/321Team/fds-project-evidence/pull/219) HEAD `e7859e3256cfc1cae311a0ae1c897ae7ce8683c3`의 병합·CI1씩 SUCCESS를 확인했다. [실행 보고](https://github.com/321Team/infra-cicd/issues/11#issuecomment-6147808781)를 읽기 자료로 소비한다. 이번 작성자는 실제 Harbor/Runner 접속·raw 독립 검증·P1 재시험을 하지 않았다.

| 구분 | 이번 정리 | 남은 담당·완료조건 |
|---|---|---|
| image source | 기존 승인 Test/Build/Scan→Push remote digest/receipt를 재사용할 후보로 연결 | 재환이 P2 current/previous로 채택할 두 이미지 원본·승인 reference 인계, 권욱이 D22/렌더에 결속. P1 deploy digest를 자동 채택하지 않음 |
| P1 Push 인증 | 보고의 Actions Secret2개 회수와 Harbor Robot 보존은 해당 P1 회차 결과 | P2 pull 권한·Secret이 생성/수용됐다는 뜻이 아님. 현재 P1 Robot/CA/Secret 변경·재발급 없음 |
| P2 pull 인증 | 기존 owner/scope/expiry/지원 전달/갱신 계약을 P2 플랫폼 identity에 결속 | 하영 기존 handoff에서 실제 방식/만료·갱신 책임 확인. 재환·권욱은 갱신 전후 cold-pull/negative 원본 소비. 토큰 원문/중복 단가표 요청 없음 |
| 만료·갱신 실패 | 새 rollout/pull 진입 STOP, 기존 건강한 workload와 실패 증적 보존 | 정책 확대·P1 credential 차용·TLS 해제로 해결하지 않음. 지원 방식으로 복구 후 별도 유효 창·원본 연결 |
| A 수동 ECR 전환 | 기존 후보 유지. source/previous digest 보존과 인증/경로·비용 판단 필요 | C3 비용은 ROSA 기승인 범위 밖. 권욱의 변경분 판단 전 실제 repository/IAM/복사 없음 |
| B 복구 대기 | A 미충족 때 검토할 대안이며 자동 선택 아님 | Harbor/VPN 복구까지 신규 rollout 중단 영향과 기존 AC 충족 여부를 권욱이 판단. cache만으로 복구 가능 판정 금지 |

복구 완료는 인증 갱신 성공만으로 판정하지 않는다. 선택한 exact host/CA·current 또는 previous 승인 digest·지원 pull 경로·필요 cold-pull·실패/복귀 원본이 같은 P2 대상/RUN에 연결돼야 한다. 기존 CA 자료와 P1 공급 시험은 변경 없는 범위에서 재사용하며, 이번 준비 때문에 원본 전체나 성공한 P1 시험을 다시 요구하지 않는다.

## 10/14 생산 원본 대조 — 앱별 current/previous

병합된 evidence PR218의 고정 커밋 `7e6bb13dafad1e5f60887880576364fe02a461de`에서 [인계 원본](https://github.com/321Team/fds-project-evidence/blob/7e6bb13dafad1e5f60887880576364fe02a461de/evidence/P1-CICD-01/push-run-38404449622-20261013/NEXT_DEPLOY_HANDOFF.json)과 [Push 결과 원본](https://github.com/321Team/fds-project-evidence/blob/7e6bb13dafad1e5f60887880576364fe02a461de/evidence/P1-CICD-01/push-run-38404449622-20261013/execute-originals/result.json)을 이번에 읽었다. 두 파일의 앱별 repository/digest·TBS Run38395350748·Push Run38404449622·workflow `147f760298dd4a683ea58f2a887483769352b97d`가 일치한다. 인계의 APP source는 `affbc69beef9967f7977d09a6fec14f7fb6c0e94`와 기존 승인 reference를 명시한다.

| 앱 | P1 공급 원본의 current 후보 | P2에서 아직 필요한 것 |
|---|---|---|
| transaction-api | `10.1.93.54/fds/transaction-api@sha256:338b8a2871507ce8b42deedc916b26e350577ee6efd18df23d7ff2dd4b17dff0` | 이 후보의 P2 채택·clean render 결속, 이 앱의 승인 previous digest·복구 적합성 |
| fds-engine | `10.1.93.54/fds/fds-engine@sha256:8b257adb08b6d381f72b66d3386efea6112a8f072ecfafcbcd463bcd1c3be89d` | 이 후보의 P2 채택·clean render 결속, 이 앱의 승인 previous digest·복구 적합성 |

여기서 **앱2종과 current/previous 두 역할은 별개**다. 한 앱을 current, 다른 앱을 previous로 매핑하지 않는다. 각 앱마다 current·previous를 연결하며, 값이 같다는 가정도 하지 않는다. P1 롤백 이미지의 기능/보안 경계를 검토하지 않고 P2 previous로 복제하지 않는다. 생산자가 기존 승인 원본에 소비 지정만 보완하면 되며 재빌드/Push/전체 자료 재제출을 요구하지 않는다.

선택한2파일의 [동일 커밋 manifest](https://github.com/321Team/fds-project-evidence/blob/7e6bb13dafad1e5f60887880576364fe02a461de/evidence/P1-CICD-01/push-run-38404449622-20261013/SHA256SUMS) 대조는2/2 일치했다. SHA256은 각각 `79f4f056290b953912dcb229604ea0fc20d3a2412ed8a66ff13e764ef33996f1`, `8be5cef6cc47e0afcd5236f031bc7c180cdec40ba34039729741114c46f38276`다. 이는 이번 조회 파일 무결성/상호 대응 확인이며 전체 archive 재검증·현재 Harbor 실조회·P2 pull/배포 성공·새 독립 승인으로 확대하지 않는다.

### D22에서 다시 받지 않을 것과 남은 최소 입력

- **재사용:** #11 CLOSED의 CA JSON·host key·경로 순서·생산자 인계 수용, 위 앱별 P1 공급 원본, 기존 A/B 비교·실패/복구 절차. 정적 인증서/기존 공급 시험을 새 날짜만을 위해 반복하지 않는다.
- **생성/경로 준비:** 하영의 실제 HCP 지원 버전·적용 경로·P2 pull credential reference/owner/scope/expiry/갱신 책임. token 원문 없이 기존 handoff의 누락 필드만 연결한다. CA 입력 접수 완료와 실제 설정/통신 완료를 구분한다.
- **P2 소비 지정:** 재환의 앱별 current/previous 채택·승인 reference·clean render와 권욱의 실행 입력 결속. 새로운 manifest/index 형식을 임의 변환하지 않는다.
- **생성 후:** 승인 창의 actual node-source·strict TLS·cold-pull/digest·negative·복구 결과 → Basic Ready → D22 Final. 생성 전 실제 cold-pull을 선행조건으로 요구하지 않는다.
- **A 선택 시에만:** 지원 ECR 인증/갱신·경로·current/previous 보존·전환/복귀·C3 비용의 권욱 중앙 판단. A 미완비는 신규 rollout 중단 조건이며 B 최종 선택을 자동 뜻하지 않는다.

따라서 준비 검토는 진행 가능하고, D22 Final·실제 전환은 미완료다. 기존12출력 중 준비 입력이 수용된 항목을 다시 PENDING 전체로 되돌리지 않는다.
