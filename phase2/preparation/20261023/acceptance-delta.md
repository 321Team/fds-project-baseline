# 인수·증적·최종 정리 변경분 — 10/25 갱신

이권욱 / CODEX_ASSISTED. 기준: 2026-10-25 15:43 KST. 사용자 요청의 #46 운영 입력 대조와 #33·#42 관리 기록 마감을 병행했다. PR201/202·ev251/252·PR150의 기존 검증을 재사용한다. 아래 관리 범위 인수 기록과 실제 Runtime·전체 Gate·정본 발행은 구분한다.

## #33·#39·#42 인수 준비

| 항목 | 확정·편입 근거 | 남은 담당·완료조건 |
|---|---|---|
| #33 Phase 2 Kick-off | [기존 Start 인계표](../20261020/start-relay-handoff.md)의 #32 Close/KI·Approved Deferred, #34 Freeze/docs-v3.1.22, 계정·기반·P0 범위·단일 Review 시간·Risk 근거를 재사용. 실제 소비는 ROSA `fds-app`, 공용 Lab 제약은 해당 Lab을 실제 사용할 때 적용 | 권욱: 아래 10/25 관리 인수 결과와 운영 WBS에 연결. GitHub 이관 후 Notion 미사용 결정 적용. 과거 Start GO·완료일 합성 및 #34/#36/#52 재개 없음 |
| #39 G4 | [ev250](https://github.com/321Team/fds-project-evidence/pull/250) merge `eadec9f53cb9f1e13877f2e9a02779ef785aa366`: T3/T3-R·원복/정리 원본과 공개 정제 경로 편입 | 권욱 인수, 하영·재환 생산: T6 INCONCLUSIVE·#7 B/A/N3 등 실제 미실행의 원 AC 처분 근거 연결. 병합만으로 Gate PASS 처리하지 않으며 같은 원본 재제출/전체 시험 반복은 요구하지 않음 |
| #42 D22 | [FINAL6337537087](https://github.com/321Team/fds-project-baseline/issues/42#issuecomment-6337537087), 창 B 실제 원본 검토·Harbor Primary, [MSA42](https://github.com/321Team/fds-msa/pull/42) merge `69e28c494a120c388afe18d901043d05333d7c7c`의 IF-19/strict clean render·2앱6객체 | 권욱 인수/추적, 하영 Registry·재환 소비: 기존 IF-19/WBS의 선택·정상 URI·인증 갱신/실패/복구 연결을 최신 운영 결정과 대조. D22를 미선택으로 돌리거나 ECR 실제 전환 시험·세 번째 이미지 생산을 새 필수조건으로 추가하지 않음. 실제 최종 자격 회수는 별도 |

이미 정리한 [PR197 대상11건](https://github.com/321Team/fds-project-baseline/pull/197#issuecomment-6339659621)은 Decision5 Done·Task6 Cancelled를 유지한다. P1 미구현 잔여/재개 Owner·조건을 기록한 관리 정리이며, 이를 P0 신규 구현으로 복원하거나 Runtime 완료로 표시하지 않는다.

## #33·#42 원 AC별 정리와 관리 잔여

| 티켓·원 AC | 근거와 현재 판정 | 남은 단독 작업 / 종료 조건 |
|---|---|---|
| #33 선행조건·착수 승인 | 기존 Start 입력표, #32 Close/KI·Approved Deferred, #34 Freeze, #36 D21, #52 일정 연결. 준비·구현 진행 사실로 과거 착수 승인일을 만들어 넣지 않음 | 아래 10/25 기록에 기존 선행조건·Decision/Risk·후속 Action을 연결했다. 과거 착수 승인 시각은 합성하지 않음 |
| #33 Decision/Risk·KI | 위 확정 기록과 PR197의 Decision5/Task6 관리 정리 재사용. 공용 Lab 제약은 실제 Lab 사용 시에만 적용 | 기존 Risk/Owner·후속 Action을 인수 결과와 연결. Runtime 미실행을 PASS로 바꾸지 않음 |
| #33 관리 시스템 일치 | 10/25 사용자 확인: GitHub 이관 후 Notion 미사용·연결 금지. 옛 Notion 동기화는 현행 완료조건으로 적용하지 않음 | 운영 WBS A22:H22와 본 인수 기록을 대조. 발행 원본·보관 AC 문구는 이력으로 보존 |
| #42 소스·Fallback 승인 | [D22 FINAL](https://github.com/321Team/fds-project-baseline/issues/42#issuecomment-6337537087) Harbor Primary, ECR 수동 A 조건 유지. 현재 ECR 운영 준비 미확인, 실패 시 신규 rollout STOP·previous=NONE | 선택 완료. 다시 Registry를 고르거나 ECR 구축·전환 시험을 현재 필수조건으로 추가하지 않음 |
| #42 Pull Route/TLS/Credential 시험 정의 | 실제 창 B cold-pull·strict TLS·승인 digest와 ev251, Robot 유한 연장 보고가 연결됨 | 정의/수신 범위는 재사용. 최종 Robot·Secret 회수는 #12/#55 책임으로 추적하며 이를 D22 재선택/새 선행시험으로 만들지 않음 |
| #42 P2-APP/HYB WBS·IF-19 | MSA42 병합의 소비 계약과 아래 IF-19 운영 행·운영 WBS A23:H25에 동일 선택/후속 책임 반영 | 권욱 관리 반영, 하영 Registry/자격·재환 앱/Hybrid 소비. 최종 회수 #12/#55와 전체 앱/G5 인수는 별도 |

관리 문서·WBS 반영과 GitHub 티켓의 Status/AC/종결 반영은 각각 확인한다. 아래 기록은 #33 Start 입력·인계와 #42 D22 Decision 범위이며 #39/G4·#46 실행·#55 최종 회수의 인수를 대신하지 않는다.

## 10/25 관리 마감·IF-19

사용자 이권욱의 “2, 4번 먼저 병행” 지시 범위로 기존 확정 기록을 정리했다. **관리 기준은 GitHub 저장소·티켓·WBS·Interface 단일 경로**다. 사용자 추가 확인에 따라 Notion은 GitHub 이관 후 사용하지 않으며 연결·수정을 중단했다. 과거 발행본/보관 입력본의 Notion 문구는 이력으로 보존하고 Notion 동기화 완료를 주장하지 않는다.

### #33 Start 입력·인계 인수 기록

- 책임/기록 주체: **이권욱 / CODEX_ASSISTED**, 관리 기록일 2026-10-25 KST. 기존 확정 판단을 모은 현재 인계 기록이며 과거 실제 착수일·당시 승인자·회의 실시일을 새로 만들지 않았다.
- Entry 대조: [기존 Start 입력표6270090544](https://github.com/321Team/fds-project-baseline/issues/33#issuecomment-6270090544)·[Start 인계표](../20261020/start-relay-handoff.md)의 Phase1 Close/KI·Approved Deferred, #34 Freeze·정본, 계정/기반·P0 범위·일정, [#36 D21 최종 인수6330828733](https://github.com/321Team/fds-project-baseline/issues/36#issuecomment-6330828733), #52 단일 회의계획을 재사용한다.
- 관리 범위 결과: **선행조건·Decision/Risk·KI 인계 기록 수용**. D21은 EC2 Relay FINAL이며 새 OCI 시험/선택을 요구하지 않는다. PR197의 미구현 잔여와 재개 Owner/조건은 그대로 인계한다.
- 후속 Action: #39 권욱 인수/하영·재환 증적(미실행·INCONCLUSIVE 처분), #46 권욱 실제 grant/baseline/인증/finish, #49 집계, #55 각 담당 최종 회수, #57 Lead Sign-off. 이들 미완료를 Start 관리 범위 완료 때문에 PASS로 바꾸지 않는다.
- 관리 추적: [운영 WBS](../20261022/FDS_Phase2_Review_Operating_WBS_20261022.xlsx) `WBS!A22:H22`에 동일 결과·책임·기록일 반영. 원 계획일/과거 Completed Date는 변경하지 않는다. 새 Runtime 실행 GO는 없다.

### #42 D22·IF-19 현행 운영 행

| 항목 | 현행 결정·후속 책임 |
|---|---|
| IF-19 경로/소스 | ROSA **node image pull** → Harbor `10.1.93.54:443`; Primary `FINAL_GO_HARBOR`. [D22 FINAL6337537087](https://github.com/321Team/fds-project-baseline/issues/42#issuecomment-6337537087) 재사용. Pod NetworkPolicy를 node pull 경계로 해석하지 않음 |
| TLS·이미지 | strict TLS·기존 CA, 승인 immutable digest 2개. MSA42 merge `69e28c494a120c388afe18d901043d05333d7c7c`의 동일2앱6객체·IF-19 계약 유지. 창 B 실제 cold-pull/TLS/digest와 [ev251](https://github.com/321Team/fds-project-evidence/pull/251) 편입을 근거로 삼으며 앱 기동/정책 AC는 별도 |
| 자격·갱신 | P2 pull-only Robot 1개·지정 pull Secret/SA 참조. 하영이 기존 동일 Robot의 유한 연장·readback을 관리. 만료·회수·pull 실패 시 rollout STOP. 갱신 시 Secret 참조/readback·strict TLS/digest를 유지하며 token 원문은 비공개. 새 무기한 자격이나 재발급을 이 기록으로 승인하지 않음 |
| Fallback·복구 | ECR 수동 A는 기존 조건부 대안이며 현재 운영 준비 미확인·미활성. 자동 ECR 전환이나 추가 이미지 생산 없음. 현재 신규 rollout STOP·`previous=NONE`; 실제 별도 전환/복귀가 필요하면 그 경로·자격·digest와 수동 승인 계약을 적용 |
| APP/HYB WBS | `WBS!A23:H25`: D22 선택·P2-APP-01 소비 계약·P2-HYB-01 IF-19 연결을 같은 근거로 기록. 선택과 시험 정의의 인수이며 #43/#47 전체 AC·G5/G6 PASS가 아님 |
| Owner·마감 | Decision/관리 추적 권욱, Registry·TLS·Robot/Secret 하영, 앱/Hybrid 소비 재환. 실제 최종 SA/Secret·Robot/경로 회수는 #12/#55에서 10/26 12:00 완료로 별도 확인. 정상 소비 종료 계획08:30과 회수 결과를 혼합하지 않음 |

### #46 확인된 입력 연결·미수신 원본

코드 기준 [PR150 HEAD6c76311d](https://github.com/321Team/infra-cicd/pull/150): 발급측 `ansible01/server01_ansible`, 실행측 `cicd-runner01/server01_cicd-runner` UID1000, 관리 SSH key/known_hosts·22/tcp·host-key alias, 날짜가 있는 API/OAuth/TLS 관측, source69e28c49·render/contract·P2 root/private Python 준비를 재사용한다. 기존 `build_observed_run_inputs`·native job 선언과 로그인 공급부가 같은 config/context·repository 순서로 연결되는 코드/통합시험은 이미 이 PR에 모여 있다. helper는 과거 workspace에 고정하지 않고 실제 native job의 exact checkout에서 선택한다.

control은 전용 ref `heads/codex/p46-operating-control-20261025`, commit `6531ba8e301858c0e180c377d06908f895158a70`, `docs/phase2/operating-handoff.md` body SHA256 `4bbac06d284a7d8c68ff867a5fb6f69ead4881ba56973bd7bcbb6f20c4e9311b`다. 이는 기존 채택 pin이며 준비댓글6385867126을 실행 grant로 쓰지 않는다. 상시 시간대와 실제 grant의 유한기간은 구분한다.

| 남은 입력/행위 | 담당·완료조건 |
|---|---|
| 실제 RUN/action의 5역할 grant·기간/control 및 별도 finish scope | 권욱. 실제 원본의 대상·행위·유효기간을 CODE 선택에 명시. 코드 승인·준비댓글·자원 유지기한/과거 수동 C GO로 대체하지 않음 |
| replicas 인계 후 새 full6 baseline metadata·실물·명시 staging | 권욱. 기존 하영·재환 인계 재사용 후 새 현재 상태/UID/spec/owner/previous와 동일 RUN을 결속. 오래된 archive·SCC/UID 투영 대체 금지 |
| 양호스트 동일 config/context·source 채널 및 본인 메모리 인증 | 권욱. 실제 native context와 source 자격 순서 결속. 확인된 경로를 재요청하지 않으며 password/token을 파일·환경·argv·채팅에 넣지 않음 |
| 실효 권한·인증된 READY·실제 finish/복구 인수 | 권욱. 실행 승인 후 검증/생성. 미래 nativeID/nonce/발급receipt/finish hash는 사전 제출 입력이 아님 |

이번에는 기존 구성 함수의 무I/O 조립 상태를 **12개 오프라인 assertion**으로 대조했다. 선택 상태·기간/control·Runner/준비 경로·미수신 인증/finish 구분을 확인했으며 `SITE=None`, 실제 호스트 접속·자격 발급·권한 변경·배포/dispatch는 0이다. PR150의 기존 Windows1235=1036PASS199SKIP/Linux1235=1230PASS5SKIP·필수2SUCCESS를 재사용한다. 새 원본 없이 같은 시험이나 기능 PR을 추가하지 않는다.

PR150 최신 확인: 두 담당자(하영·재환)의 정확한 HEAD `6c76311d623bf707004b858da7cbfbb36303e203` APPROVED와 필수 검사2 SUCCESS를 확인했다. 이번 요청은 운영 입력 정리/관리 기록 마감이며 실제 배포 또는 도구 Runtime을 수행하지 않았다. PR150 병합 결과와 Runtime 입력 채택 결과는 각각 추적한다.

## #49·Review 인계

[현행 접수 대장](../20261020/evidence-roster.md)을 단일 집계표로 사용한다. 수신·재해시·내용 검토·증적 PR 병합·AC 인수는 별개다. 창 C TGZ는 양측 모두 수신·내용 검토를 마쳤다. **하영 묶음 ev251과 재환 묶음 ev252가 모두 병합됐다.** 재환 텍스트58개는 byte 동일하며 큰 원본5개는 비공개 보관소 참조로 유지한다. 수신·검토 완료를 공개 편입으로 확대하지 않는다. Pod↔node 귀속 미확인·A5 미실행과 절차 이탈은 그대로 남긴다. 앱 SCC·UID 투영 JSON은 중앙 10/23 23:53 수신·재해시·6/6 대응 검토 완료로 반출 대기를 해제했다. full Pod 객체/6객체 baseline과는 다르다. #46 운영 선택은 10/24 사용자 채택이며 PR145·146까지 병합됐다. P2 전용 source/store·private parser 환경은 실제 준비·재조회했고 PR147의 private 파일 수신 연결도 merge99e10efc로 편입됐다. 기존 공급 JSON·TBS/Push native 대응은 확인해 [Draft PR148](https://github.com/321Team/infra-cicd/pull/148)로 연결 중이다. 실제 grant·인계 후 새 baseline·본인 인증/READY·finish scope와 최종 SITE는 아직 미완료이며 `SITE=None`·도구 Runtime NOT_RUN이다.

#54 제출 후보→#56 실제 Review 결과/#55 Action→10/26 #55/#57 실제 정리·Close 순서다. #52의 10/23 18:00~19:30은 확정된 계획 이력이며 실제 회의 개최 증적은 별도다. 회의 일정 Decision 완료와 실제 회의·최종 Sign-off는 구분한다. 월요일12:00은 정리 시작이 아닌 완료 목표이며 실제 삭제창/복구 가용은 아직 미확정이다.

## 삭제안 추가 검토

- 대상: [zone3 exact-ID6337296113](https://github.com/321Team/infra-rosa/issues/8#issuecomment-6337296113)·[Namespace 세션6337436035](https://github.com/321Team/infra-rosa/issues/8#issuecomment-6337436035). 고정 비공개 공유의 v8 manifest23/23·override2/2 파일 해시가 일치했다. 생성 원본 TGZ SHA256 `d46c9b0988d5b5c835fa032ff22a66b69fd45295254183df1c83a7ff2ac31219`에서 exact-ID·Name·PrivateZone·전체 CallerReference 3개를 대조했고 모두 일치했다. checker 정상 입력rc0/CallerReference 변조rc1의 오프라인 판정을 확인했다. 기존284 MOCK은 재실행하지 않았다.
- 이 원본 일치는 소유 근거 초안 수용이며, 실제 삭제 당일 inventory/final hash·DELETED 상태·참조·record 소유권·saved Plan·실제 실행 권한은 별도다. 실패 뒤 이전 final.json을 새 성공 결과로 쓰지 않고 새 RUN 출력 경로/rc를 확인한다. private raw는 GitHub에 게시하지 않는다.
- A안(기존 일반 계정)을 먼저 사용한다. 기존 제안의 `oc auth can-i delete namespaces/<정확한 이름> -n <같은 이름>`을 대상3개 각각 확인하는 방법을 재사용한다. namespace 객체의 cluster scope만으로 이 검사를 namespace=""로 바꾸거나 관리자 필요로 단정하지 않는다. [Kubernetes 요청 해석 소스](https://github.com/kubernetes/kubernetes/blob/v1.35.0/staging/src/k8s.io/apiserver/pkg/endpoints/request/requestinfo.go#L175-L187)는 `/api/v1/namespaces/{name}`에도 Namespace 속성을 해당 이름으로 설정한다. SSAR를 직접 쓸 때도 실제 DELETE와 같은 group="", resource="namespaces", verb="delete", name=namespace=정확한 이름으로 대조한다. 최종 허용은 실제 API/사용자의 현재 응답이며, 이 인가 확인은 삭제 실행이 아니다. 05의 core Namespace 경로를 Project API로 임의 변경하지 않는다.
- B안(임시 cluster-admin)은 A에서 불가할 때의 별도 권한/실행 후보다. 기존 검토된 always-revoke/watchdog를 재사용해 중단·화면 유실 시에도 회수하고 실제 revoke/readback까지 예산에 포함한다. 로그인/MFA·inventory/삭제·회수·보고를 포함한 창을 연결하며 이 문서가 새 임시 관리자/삭제 GO는 아니다.
- 05는 UID precondition DELETE·다른 UID/응답 불명 STOP·bounded NotFound poll을 유지한다. 부분 삭제 후 전체05를 다시 실행하지 말고 실제 잔존 UID/receipt를 읽어 남은 대상만 정리 인수한다. force finalizer 제거/자동 재시도는 추가하지 않는다. [v8.1](https://github.com/321Team/infra-rosa/issues/8#issuecomment-6360894119)에서 현재 호출 전용 임시 디렉터리 정리로 보완됐고 집중24 MOCK을 확인했다. 이전 임시파일 권고는 해소됐으며 SIGKILL 잔존 한계는 유지한다.

## 현재 유지 결정의 소비

[10/22 22:46 결정6342339344](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-6342339344)과 [유지표](../20261022/resource-retention-to-20261026.md)를 따른다. 새 유지 DB_RUN·NP4+앱 NP2/새 연결 검증·미사용 앱0·같은 Robot 유한 만료 편집1회·현재 DB Secret UID의 회수 상한10/26 12:00을 연결한다. 실제 DB 유지 RUN·NP6·Robot 유한 TTL 편집 보고는 수용됐다. 오늘 앱0/DB세션0·SCC/UID는 담당자 보고와 중앙 원본 수신을 구분해 [접수 대장](../20261020/evidence-roster.md)에 반영했다. 최종 회수는 미실행이다. 원 담당자 회신 대기 중에도 #46 구현·#49 접수·Review 준비는 독립 진행한다.
