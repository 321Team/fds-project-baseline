# Phase 2 확정 사양 — 정본 편입 후보

기준 **2026-10-19 18:42:43 KST**. 설계 Lead 이권욱 / AI 사용 CODEX_ASSISTED. 현재 docs-v3.1.21과 이후 승인 결정을 통합하는 **미발행 후보**다. 새 사양을 제안하거나 Runtime GO를 발급하지 않는다.

## 1. 효력·정확한 원본

[최종 Freeze 결정](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-6259117130)은 **2026-10-19 12:38:18 KST DESIGN_FREEZE=FROZEN**이며 [불변 승인 사양](https://github.com/321Team/fds-project-baseline/blob/38a6512aec35cb5e94b339a41ba506fc37113b01/phase2/preparation/20261008/architecture-freeze-candidate-20261018.md)의 **§2~§8 전체**를 채택했다. source commit `38a6512aec35cb5e94b339a41ba506fc37113b01`, blob `6a62d6935ae0e97ed9f988bf33ea33ad041cdbd1`, UTF-8 원문 SHA256 **`aa36c2723cbbdd20ffd5d89407c93641ed984e89306dd167da5cb157fc76101e`**. 실제 merge `acc513cf5c9f3e07e58d818a18e4b8fcf1e0cf70`와 이 후보 브랜치의 해당 blob 일치를 확인했다.

원본의 READY_FOR_LEAD_DECISION/CANDIDATE/권고는 최종 결정 전 작성 스냅샷 표기다. 최종 결정이 채택한 사양·변경통제에는 그 결정을 우선하며, actual UID/credential·시험 결과 부재를 설계 미결로 다시 분류하지 않는다. 이 후보 편입과 설계 Freeze를 docs-v3.1.21 재발행/새 Release·실제 인수로 확대하지 않는다.

## 2. 고정 구성

| 영역 | 확정 사양·경계 |
|---|---|
| 계정/위치 | AWS774055931866/ap-northeast-2, VPC10.20.0.0/16 |
| subnet | private_a10.20.10.0/24(2a/apne2-az1), private_b10.20.20.0/24(2b/apne2-az2), private_c10.20.30.0/24(2c/apne2-az3), public_transport_a10.20.110.0/24(2a/apne2-az1). worker는private_a·publicIngress는public_transport_a, public b/c 신설 없음 |
| D21 Transit | AWS EC2+EIP Libreswan Relay FINAL. Relay10.20.110.10/t3.medium/encrypted gp3 40GiB/EIP1, 일반 egress NAT1과 역할 분리. OCI는 비교 이력/비선택이며 새 OCI 구축 아님 |
| ROSA | HCP/fds-rosa-hcp/4.22.17/public API·public default Ingress. worker 단일AZ3대가 managed control-plane 단일AZ 보장을 의미하지 않음 |
| worker | workers pool/m5.xlarge×3/root300GiB(실측gp3·암호화)/IMDSv2 required/autoscaling=false/auto_repair=true/max_surge1·max_unavailable0. 무중단/실제Ready 보장 아님 |
| cluster CIDR | Pod10.128.0.0/14·Service172.30.0.0/16·host prefix/23. 기존On-Prem10.1.93.0/24와 설계 비중복이며 전체현장route실측 보장 아님 |
| actual endpoint | API https://api.fds-rosa-hcp.khht.p3.openshiftapps.com:443 · Ingress apps.rosa.fds-rosa-hcp.khht.p3.openshiftapps.com. 임의6443/고정hosts로 치환 금지 |
| app host | fds-api.apps.rosa.fds-rosa-hcp.khht.p3.openshiftapps.com. MSA PR40의 두 Route host 기록은 소스 병합됐지만 실제TLS/SAN·Route PASS 아님 |
| namespace/identity | fds-app=앱,ci-cd=배포SA,monitoring-api=예약. rosa-app은overlay. 배포SA ci-cd/fds-deployer→fds-app Role. 실제UID/CA/identity/RBAC receipt는 후속실측 |
| 앱/용량 | transaction-api3 + fds-engine3, Pod당 request250m/256Mi·limit500m/512Mi. 정상합계request1.5CPU/1536Mi·limit3CPU/3072Mi, surge포함8Pod예산request2CPU/2048Mi·limit4CPU/4096Mi. 실제quota/allocatable·플랫폼사용량과 구분, N-1 실측 후 인수 |
| 호출 | 외부TLS443→두 Route /api·/readyz(edge TLS/HTTP Redirect)→transaction-api8000→fds-engine8001. engine/metrics/catch-all 외부공개 없음. router→Pod는HTTP이며종단간TLS로표현하지 않음 |
| DB | 기존db01 10.1.93.55:5432, transaction-api만허용/engine DB DENY. 앱stateless·초기P2 PVC/새DB 없음 |
| runtime state | network/vpn/rosa-prereq/rosa-runtime 소유 분리, runtime key phase2/rosa-runtime/terraform.tfstate, S3 use_lockfile=true/암호화. 다른state/lineage합성 금지 |
| 삭제/재생성 | delete_protection=true 기본. 최종승인창 해제→실제삭제/잔존확인은 유지. F5 재생성 생략은 이번교육회차 한정 위험수용, RECREATE=NOT_RUN이며 시험PASS아님 |
| D1/IAM | FDS-IaC-Operator 최대10800초 고정, 실제발급세션TTL·작업창 별개. 일반작업은본인MFA·담당역할. 정책원문관리 위임 후보 NOT_APPLIED를 전체위임완료로 바꾸지 않음 |
| D22 | Harbor Primary+P2 pull-only+승인digest ECR 수동전환 A. 자동미러/자동전환 없음. A미준비면해당배포STOP. FINAL=PENDING_RUNTIME, ECR은VPN/DB복구대안이아님 |
| CA/digest | 기존CA JSON SHA4d86507ecd81789e376669940f68b2dbb27f5989e6fd4315238c9f61a2401da4/D7 승인current2개재사용. 재수집·재빌드·P1 Robot차용/자동회전 금지. 최초previous=NONE유지 |
| D23/D26/P1 | 추가Hybrid DNS #40/#48·GitOps#120 보류, public DNS/IP·strictTLS 유지. Operator추가공급#41/#51·OADP#44는기존보류/조건부범위 유지. 취소/구현완료/자동재개 아님 |
| 배포코어 | Runner direct/단기credential·정확Deployment2/Service2/Route2·source/render/claim/checkpoint결속. SA/NP/Secret/RBAC/delete/exec/cluster쓰기제외. 실제site/provider/CLI 정상·실패차단은별도증적 |
| Secret/보안 | restricted-v2호환·임의UID/RunAsNonRoot/RuntimeDefault·권한상승금지/ALLdrop/readOnlyRootFS·앱SA token automount=false. DB값생산전달=재환, ROSA Secret객체생성/SEC=하영, 소비검증=권욱. Secret원문은공개/receipt에넣지않음. HCP기본etcd AES와EBS암호화구분, 추가customerKMS/FIPS P0추가없음 |

## 3. IF17~20·원복/실패 계약

| IF | Producer→Consumer·포트 | 책임·완료조건 |
|---|---|---|
| IF17 | vpn-gw01 .51↔Relay EIP, IKEv2/IPsec UDP500/4500 NAT-T | 설계권욱/VPN재환/AWS하영. On-Prem initiator·explicit IKE ID. 창단위ON→정리/원복,24/7아님. exactRUN의터널/selector/허용·거부/회복증적 |
| IF18 | ROSA transaction-api→db01 .55 TCP5432, source private_a10.20.10.0/24 | 원복·인수권욱/앱시험재환/플랫폼·routeSGNP하영. node개별allowlist아님, C7 Pod/Node/UID/imageID↔ENI·시각과앱NP/DB인증으로귀속. VPC전체허용금지/engineDENY |
| IF19 | **node image pull**→Harbor .54 TCP443 또는승인ECR endpoint443 | D22권욱/Trust플랫폼하영/이미지공급재환·권욱. PodNP를nodepull통제로주장하지않음. 승인P2 principal/reference/expiry·strictTLS/digest·실제coldpull/갱신·전환복귀후D22Final |
| IF20 | OADP→S3 TCP443 | 하영, P1보류/조건부. bucket/role/retention/restore actual합성없음·BackupRestorePASS아님 |

#37 TCP 사전시험의한정runtime예외와 #47 A2를 구분한다. **A2는창안에도P1 영구 NM route/permanentFW/reload/pg_hba hostssl을 실제변경**하므로별도exact대상/RUN/codeSHA/시간/원복·P1복구대응승인후에만 apply→E2E→동일RUN receipt rollback. #37의DB120분상한·이번Freeze로대체하지않는다.

Registry/TLS/auth/digest오류는신규rolloutSTOP·기존정상Pod보존, unknown/부분적용/credential만료·claim불명은자동재시도금지·readback/checkpoint대조. 실제값수신/단순문구는새전원승인Gate를만들지않고CIDR·공개범위·용량·권한상한·Registry방향·P1영향·AC delta만기존Lead변경통제로판단한다. 변경전후/이유/interface·AC/sourceSHA/delta검증/실행창/원복/Lead판정을기록한다.

## 4. 사양 완료와 실행 잔여

create-only G4순서예외는별도정확CreateGO에한정, 전체G4/BasicReady/Full/G5면제아님. 실Namespace/Node UID·identity/CA/RBAC·Secret principal/ref/expiry·nodepull·cleanrender·RUN-A정상/RUN-B차단·Hybrid/복구·최종삭제는기존생산자/소비책임으로인수한다. source체크/해시일치/STATIC/MOCK/CI/REVIEW/MERGE/PUBLICATION과 RUNTIME을구분한다. 검사0/SKIP/queued는CI PASS아니다.

최근실행/코드상태는[운영스냅샷](operational-snapshot.md)이며위불변설계값과별개다. 특히#5 3회차STOP/이른착수/자동회수보고는원본검토전이고, 그GO는소진됐다. 새4회차요청은새승인으로만판단하며이번정본문서가GO를부여하지않는다.

## 5. 비용·권한·Phase1/발행 경계

교육장지원확정/자부담0·목표400/중단450/상한500USD, 교육장리포트기반권욱중앙판단. 담당자상세재견적·중복CostGO요구없음. 최신지정세션10/19 사용자표17.97USD/24362KRW는period/cutoff/예상총액미확인이며예상누적총비용으로확대하지않음. 검증최소권한은준비→시험/결함재시험→반출·검토완료까지유지, 파일전송때마다회수재부여하지않고완료후검증전용과운영최소권한을나눠정리한다. 분리정책자동재부착/포괄신규권한승인아님.

**Phase1 DB/pg_hba/영구FW/NM/route/HarborCA/공용OCP/기존Runner/DNS/LB/AC 변경승인은없다.** C1/C2/C3나A2는해당exact예외가별도로있어야한다. 공유원본/Plan/state/credential은고정비공개공유경로로만취급, 공개GitHub에올리지않는다.

이PR은Draft후보이며현재발행docs-v3.1.21/CURRENT/Tag/Asset·DOC exactd8f55d81동결입력은보존한다. P1 workbook은기검증7행바이트를보존하고 **P2 상태12건은 status-delta.json/Description으로편입**한다. 최종통합WBS/TicketPack/Baseline/Release전체세트재생성과WEB/ZIP/Manifest/Asset검증은정본Lead가최종화할잔여다. 지금전체78건최신화/새Release/전체Phase1·Phase2종결로표시하지않는다.
