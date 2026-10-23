# D21 최종 인수·D24 일정 운영 반영·증적 인계

**현행 안내(10/23):** 아래11:07 및 저녁 절은 당시 기록이다. 최신 인수 잔여는 [10/23 변경분](../20261023/acceptance-delta.md)·[접수 대장](../20261020/evidence-roster.md)을 우선 소비한다. PR111/112·ev250·MSA42는 병합됐고 D22 FINAL/기존 발급 권한 입력은 확인됐다. DB/자격의 이전 기한은 [현재 유지표](resource-retention-to-20261026.md)로 대체한다. 과거 미수신·Draft·각 사용 DB 원복 문구를 현재 새 게이트로 재요구하지 않는다.

이권욱 / CODEX_ASSISTED · 2026-10-22 11:07 KST. 사용자 “#36 최종 인수·종결 판단·#52 일정 반영부터 진행”, 기존 한계 확인 후 “이미 협의된 내용이라면 수용하고 편입” 지시에 따른 운영 기록이다.

## #36 D21 — 기존 한계를 수용한 Decision 종결

[최종 인수·종결 기록](https://github.com/321Team/fds-project-baseline/issues/36#issuecomment-6330828733)을 반영한다.
OCI Primary는 project-suitability NO-GO, **AWS EC2+EIP self-managed Libreswan Relay 단일 FINAL**이다.
교육장 UDP/IKE/NAT-T 경로 관측과 프로젝트 선택 판정을 분리한다. 실제 인증 성공·Child SA·업무 터널 전체 PASS를 주장하지 않는다.

- final responder는 [ev161](https://github.com/321Team/fds-project-evidence/pull/161) 독립 검토·CI 후 `277893c7865bd2af9751ca73ee00985370c9eaf2` 편입으로 재사용한다.
- Phase-A UDP 별도 원본·일부 initiator/cleanup raw·정확한 전체 capture 명령/RC/도구 버전은 **수용된 미수집 증적 한계**로 보존한다. 확보했다고 기록하거나 전체 publication PASS로 바꾸지 않는다.
- 한계 관리 책임은 권욱. 추가 실제 원본 발견·선택 adapter 변경·자료 모순 발생 때만 차이를 재검토한다. 같은 원본/전체 OCI 시험을 다시 요구하지 않는다.
- #34 Freeze→#35/#37의 선택 adapter 입력 인계를 소비한다. #35 Full IaC·#37 Tunnel/TCP/거부/복구/정리·#39 G4·Project Close 자원 정리는 각 원 AC와 담당 책임을 유지한다. 이 후속 책임을 #36의 새 선택 미결 전제로 복제하지 않는다.
- GitHub Status Done·closed/completed·현재 AC4개를 반영했다. 과거 PENDING/HOLD/미수집 이력과 핵심 요구사항의 다른 체크는 보존한다.

## #52 D24 — 승인된 회의계획을 운영 WBS/Calendar로 사용

**10/23(금) 18:00~19:30 KST / 90분**, 권욱 진행·PMO/QA/Gate/Close, 하영·재환 기존 담당 영역 인계.
10/23 집계→Freeze→Review→Action, 10/24~25 비근무, 10/26 잔여 Action·자원 정리·Close를 유지한다.

- [운영 WBS·Calendar](FDS_Phase2_Review_Operating_WBS_20261022.xlsx)의 `Calendar`가 현행 회의/일자 보기이며, `WBS`의 **DEC-CAL-P2-01 / P2-REV-01 / MS-P2-REVIEW-01** 세 레코드가 같은 시작·종료 셀을 참조한다.
- 관련 Freeze/Close를 포함한 기존5개 Record의 계획 시작·종료·Lead는 발행 v3.1.22 WBS에서 그대로 가져왔다. #55 전체 실행기간10/23~26을 90분으로 줄이지 않았고, Freeze/Close의 미확정 시각은 빈 값으로 보존했다.
- [기존 회의계획](../20261020/review-plan.md)과 [기존 ICS](../20261020/review-20261023.ics)를 같은 일정의 Calendar 가져오기용 파일로 사용한다. 새 UID·중복 ICS·아무 외부 계정의 행사를 만들지 않았다.
- 원 증적 요건은 **“Review Invite 또는 회의 계획”**이다. 실제 초대 발송·새 정본 재발행·회의 실시를 일정 Decision 종결의 별도 필수조건으로 추가하지 않는다. 이전 기록의 미실행 사실은 보존하되 그 사실을 추가 게이트로 해석했던 안내는 정정한다.
- 이 운영 반영은 발행 v3.1.22 WBS/Tag/Assets를 덮어쓰지 않는다. 다음 정본의 동기화 책임은 기존 Release Policy대로 유지한다. 회의 실시·G6/Deliverable Freeze 인수·#55/#56/#57 완료와 구분한다.
- 근거: [PR194 병합](https://github.com/321Team/fds-project-baseline/pull/194), [일정 AC3개 반영](https://github.com/321Team/fds-project-baseline/issues/52#issuecomment-6294690721), 기존 회의계획의 양측 참석 회신·사용자18시 이후 가능 결정. 새 참석 재확인·Support 전원 서명은 요구하지 않는다.

## #46 — 운영 연결의 현재 코드와 실제 입력

[PR110](https://github.com/321Team/infra-cicd/pull/110) HEAD `aebc03bbaa849f0b9660f66d29e480e0ce092e65`는 하영·재환 담당 범위의 exact HEAD 승인과 `p2-intake` SUCCESS를 확인해 merge **`05e97b559b16ff441e8956a1e02f250de337cba2`**로 편입했다. 기존 base와 main의 tree 동일·retarget7파일/HEAD 보존·미해결thread0, 병합 tree=검토 HEAD tree·base 이력 보존을 확인했다. 같은 코드 시험을 다시 실행하지 않았다.

[PR111](https://github.com/321Team/infra-cicd/pull/111) HEAD `96b483b5ff8c7d77eb80bc6b6ee03cc134af54a8`의 재환 job/Runner 소유권·실패/회귀 범위 APPROVED는 새로 확인했다. issuer/peer·자격 core에 대한 하영 범위 검토는 별도다. 이 승인 범위를 확대하지 않으며 PR111 Draft/open을 유지한다.

현재 구현에는 exact job/Binding/nonce ingress, owned Linux pipe 송수신, `ParentJobBuilder`와 기존 driver/source/factory/finish 연결이 있다. 아직 실제 SSH peer·정확한 대기 job rendezvous·issuer 작업 위치/기존 발급 권한·운영 source/control/finish 채택이 없다. **`SITE=None` 유지**. 이미 구현된 helper를 중복 작성하거나, 기존 관리 SSH 관측을 현재 인증·채널 성공으로 승격하지 않는다.

| 기존 책임 | 다음 실제 입력·완료조건 | 새로 요구하지 않는 것 |
|---|---|---|
| 권욱·재환: 정확한 부모 job 연결 | 실제 Runner 계정/UID·검토된 ready/open_channel 구현·현재 관리 peer/host-key와 부모 소유권 인계 | 미래 Run/nonce 사전 합성, 정상 Worker 일괄 종료, 같은 Runner 공급 시험 반복 |
| 하영·권욱: issuer/자격 | 실제 issuer 작업 위치/기존 발급 권한·UID/CA/IP·900초 자격을 부모 메모리로 전달하는 채널 | raw token/암호를 GitHub·공유폴더·argv/env/log로 전달, 자동 재발급 |
| 권욱: authority/finish 통합 | 실제 GO 원문/control 의미·Binding/source pin·독점 쓰기 종료 범위와 C-STOP 분리 여부를 명시적으로 채택 | D21/일정/코드 병합을 새 실행 GO로 간주, 실제 finish 없이 claim 자동 반납 |

확인된 원본과 운영 채택값이 들어오는 차이만 [기존 구성 연결표](../20261020/p46-operating-configuration.md)에 반영한다. 이 인계의 Runtime은0이며 실제값을 합성하지 않았다.

## #49 — 접수·검토 완료와 최종 인수의 분리

[기존 증적 대장](../20261020/evidence-roster.md)을 재사용한다. 이번 조회에서 ev161/239/249·ROSA51·Terraform33·PR194/195 편입 상태를 다시 확인하고 D21 종결·일정 운영본·PR110 병합만 delta로 연결했다.

남은 주요 묶음은 창 A 기수신 원본의 증적 PR 편입(재환), C1C3·앱 SA/cold-pull/D22(하영), #46 실제 운영 입력/현장 배포(권욱 통합), 최종 공급/clean render(재환), PG-03 Pod/Route/삭제·DB A2/Secret·종료 증적(각 기존 Lead)이다. 이미 받은 파일·해시·같은 시험을 재요구하지 않는다. 10/23 Review에는 실제 수용/미실행/한계를 그대로 전달하며 이를 #49/#54 전체 완료로 만들지 않는다.

STATIC/MOCK/CI·사람 REVIEW·MERGE·RUNTIME·정본 PUBLICATION·최종 인수를 구분한다. 실제 서버/Runner/ROSA/DB 접속·Token 발급/IAM/Apply/Deploy·새 GO는 수행하지 않았다. 비공개 원본 Plan/state/credential은 이 문서·운영 WBS에 포함하지 않았다.


## 10/22 저녁 추가 변경 — 자원 유지·최종 정리10/26 12:00

[사용자 변경 결정](https://github.com/321Team/fds-project-baseline/issues/37#issuecomment-6338609757)과 [자원 유지 운영표](resource-retention-to-20261026.md)를 적용한다. 기존 Review10/23 18:00~19:30·#55 실행기간/10/26 Close 계획은 유지하고, 자원 최종 정리를 Review 전에 끝내야 한다는 결합만 해제했다. 각 C 회차 소비 중지·DB 원복/보고는 늦추지 않으며, 최종 P8/V9·ROSA/AWS·Harbor 연결 구성 정리는10/26 12:00 완료 목표로 재배치한다. DB90/120분·S Secret10/23 16:30·Robot 자연 만료·임시 권한/토큰 수명은 별개다. SITE 실제 채택 대기/오늘1회 GO 범위·정확 saved Plan별 Apply는 유지한다. 현재 보관/최종 정리 미실행과 실제 Cleanup PASS를 구분해 #49/#55 인수에 연결한다. 월요일 가용/실제 삭제창은 미확정이며 자원 보관을 주말 근무나 새 Runtime GO로 표시하지 않는다. 발행본/WBS/Tag·기존 AC/Status는 보존하고, 이 절 이전의 시점별 상태는 이력으로 유지한다.


## 10/23 변경분 통합

#46은 기존 PR113에 자격 수신 후 1회 계획 완성 경로를 추가하는 검토 후보를 준비했다. public ready는 상관관계 표식이며 발급/원본 인증을 대신하지 않는다. 원본10/10·기존 ci-cd 발급 인가는 재사용하고, 실제 parent/peer/메모리 전달 채널·control/finish 의미·수동 C 이후6객체 기준선은 아직 운영 채택이 필요하다. `SITE=None`과 Runtime 미실행을 유지한다.

#49에는 ev250 편입·창 B 원본 검토·D22 FINAL/MSA42·ROSA52/53 병합·C 종료 owner 보고·10/22 22:46 유지 RUN/자격 기한 결정을 반영했다. C raw/Pod↔node·A5 잔여, T6 INCONCLUSIVE를 PASS로 바꾸지 않는다. #33/#39/#42는 [담당별 최종 인수 정리](../20261023/acceptance-delta.md)에서 기존 요건·정리 책임을 연결하며 자동 AC 체크/종결은 하지 않는다.

삭제 v8은 기존284 MOCK을 재사용하고 새 zone override만 생성 원본과 비교했다. Namespace 계정 A는 기존 제안의 대상별 `-n <같은 이름>` 인가 확인을 재사용한다. Namespace 객체의 cluster scope만으로 실제 요청의 namespace 속성을 비우거나 관리자 필요로 단정하지 않는다. 계정 B 임시 권한/실제 삭제창·새 inventory·saved Plan별 실행은 별도이며 이번 기록은 삭제 GO가 아니다.
