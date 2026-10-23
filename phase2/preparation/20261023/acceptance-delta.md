# 10/23 인수·증적·최종 정리 변경분

이권욱 / CODEX_ASSISTED. 기준: 2026-10-23 KST, 10/23 19:20 KST 원본 검토·담당자 보고까지. 검토 후보이며 새 정본 발행·Runtime GO·AC 인수·Issue 종결이 아니다.

## #33·#39·#42 인수 준비

| 항목 | 확정·편입 근거 | 남은 담당·완료조건 |
|---|---|---|
| #33 Phase 2 Kick-off | [기존 Start 인계표](../20261020/start-relay-handoff.md)의 #32 Close/KI·Approved Deferred, #34 Freeze/docs-v3.1.22, 계정·기반·P0 범위·단일 Review 시간·Risk 근거를 재사용. 실제 소비는 ROSA `fds-app`, 공용 Lab 제약은 해당 Lab을 실제 사용할 때 적용 | 권욱: 공식 Entry/Exit 판단 결과와 WBS/Notion 추적 잔여를 #49/Review에 연결. 과거 실행을 소급 Start GO·완료일로 만들지 않으며 #34/#36/#52 Done/closed를 다시 열지 않음 |
| #39 G4 | [ev250](https://github.com/321Team/fds-project-evidence/pull/250) merge `eadec9f53cb9f1e13877f2e9a02779ef785aa366`: T3/T3-R·원복/정리 원본과 공개 정제 경로 편입 | 권욱 인수, 하영·재환 생산: T6 INCONCLUSIVE·#7 B/A/N3 등 실제 미실행의 원 AC 처분 근거 연결. 병합만으로 Gate PASS 처리하지 않으며 같은 원본 재제출/전체 시험 반복은 요구하지 않음 |
| #42 D22 | [FINAL6337537087](https://github.com/321Team/fds-project-baseline/issues/42#issuecomment-6337537087), 창 B 실제 원본 검토·Harbor Primary, [MSA42](https://github.com/321Team/fds-msa/pull/42) merge `69e28c494a120c388afe18d901043d05333d7c7c`의 IF-19/strict clean render·2앱6객체 | 권욱 인수/추적, 하영 Registry·재환 소비: 기존 IF-19/WBS의 선택·정상 URI·인증 갱신/실패/복구 연결을 최신 운영 결정과 대조. D22를 미선택으로 돌리거나 ECR 실제 전환 시험·세 번째 이미지 생산을 새 필수조건으로 추가하지 않음. 실제 최종 자격 회수는 별도 |

이미 정리한 [PR197 대상11건](https://github.com/321Team/fds-project-baseline/pull/197#issuecomment-6339659621)은 Decision5 Done·Task6 Cancelled를 유지한다. P1 미구현 잔여/재개 Owner·조건을 기록한 관리 정리이며, 이를 P0 신규 구현으로 복원하거나 Runtime 완료로 표시하지 않는다.

## #49·Review 인계

[현행 접수 대장](../20261020/evidence-roster.md)을 단일 집계표로 사용한다. 수신·재해시·내용 검토·증적 PR 병합·AC 인수는 별개다. 창 C TGZ는 수신·내용 검토를 마쳤고 ev251에 편입됐다. Pod↔node 귀속 미확인·A5 미실행과 절차 이탈은 그대로 남긴다. 오늘 앱 SCC·UID JSON은 수집 보고가 있지만 공유 반출 대기다. #46은 실제 입력이 일부 수용됐지만 도구 Runtime0·SITE 미채택이다.

#54 제출 후보→10/23 18:00~19:30 #52 Review/#55 Action→#56 Review 결과→10/26 #55/#57 실제 정리·Close 순서다. 회의 일정 Decision 완료와 실제 회의·최종 Sign-off는 구분한다. 월요일12:00은 정리 시작이 아닌 완료 목표이며 실제 삭제창/복구 가용은 아직 미확정이다.

## 삭제안 추가 검토

- 대상: [zone3 exact-ID6337296113](https://github.com/321Team/infra-rosa/issues/8#issuecomment-6337296113)·[Namespace 세션6337436035](https://github.com/321Team/infra-rosa/issues/8#issuecomment-6337436035). 고정 비공개 공유의 v8 manifest23/23·override2/2 파일 해시가 일치했다. 생성 원본 TGZ SHA256 `d46c9b0988d5b5c835fa032ff22a66b69fd45295254183df1c83a7ff2ac31219`에서 exact-ID·Name·PrivateZone·전체 CallerReference 3개를 대조했고 모두 일치했다. checker 정상 입력rc0/CallerReference 변조rc1의 오프라인 판정을 확인했다. 기존284 MOCK은 재실행하지 않았다.
- 이 원본 일치는 소유 근거 초안 수용이며, 실제 삭제 당일 inventory/final hash·DELETED 상태·참조·record 소유권·saved Plan·실제 실행 권한은 별도다. 실패 뒤 이전 final.json을 새 성공 결과로 쓰지 않고 새 RUN 출력 경로/rc를 확인한다. private raw는 GitHub에 게시하지 않는다.
- A안(기존 일반 계정)을 먼저 사용한다. 기존 제안의 `oc auth can-i delete namespaces/<정확한 이름> -n <같은 이름>`을 대상3개 각각 확인하는 방법을 재사용한다. namespace 객체의 cluster scope만으로 이 검사를 namespace=""로 바꾸거나 관리자 필요로 단정하지 않는다. [Kubernetes 요청 해석 소스](https://github.com/kubernetes/kubernetes/blob/v1.35.0/staging/src/k8s.io/apiserver/pkg/endpoints/request/requestinfo.go#L175-L187)는 `/api/v1/namespaces/{name}`에도 Namespace 속성을 해당 이름으로 설정한다. SSAR를 직접 쓸 때도 실제 DELETE와 같은 group="", resource="namespaces", verb="delete", name=namespace=정확한 이름으로 대조한다. 최종 허용은 실제 API/사용자의 현재 응답이며, 이 인가 확인은 삭제 실행이 아니다. 05의 core Namespace 경로를 Project API로 임의 변경하지 않는다.
- B안(임시 cluster-admin)은 A에서 불가할 때의 별도 권한/실행 후보다. 기존 검토된 always-revoke/watchdog를 재사용해 중단·화면 유실 시에도 회수하고 실제 revoke/readback까지 예산에 포함한다. 로그인/MFA·inventory/삭제·회수·보고를 포함한 창을 연결하며 이 문서가 새 임시 관리자/삭제 GO는 아니다.
- 05는 UID precondition DELETE·다른 UID/응답 불명 STOP·bounded NotFound poll을 유지한다. 부분 삭제 후 전체05를 다시 실행하지 말고 실제 잔존 UID/receipt를 읽어 남은 대상만 정리 인수한다. force finalizer 제거/자동 재시도는 추가하지 않는다. [v8.1](https://github.com/321Team/infra-rosa/issues/8#issuecomment-6360894119)에서 현재 호출 전용 임시 디렉터리 정리로 보완됐고 집중24 MOCK을 확인했다. 이전 임시파일 권고는 해소됐으며 SIGKILL 잔존 한계는 유지한다.

## 현재 유지 결정의 소비

[10/22 22:46 결정6342339344](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-6342339344)과 [유지표](../20261022/resource-retention-to-20261026.md)를 따른다. 새 유지 DB_RUN·NP4+앱 NP2/새 연결 검증·미사용 앱0·같은 Robot 유한 만료 편집1회·현재 DB Secret UID의 회수 상한10/26 12:00을 연결한다. 실제 DB 유지 RUN·NP6·Robot 유한 TTL 편집 보고는 수용됐다. 오늘 앱0/DB세션0·SCC/UID는 담당자 보고와 중앙 원본 수신을 구분해 [접수 대장](../20261020/evidence-roster.md)에 반영했다. 최종 회수는 미실행이다. 원 담당자 회신 대기 중에도 #46 구현·#49 접수·Review 준비는 독립 진행한다.
