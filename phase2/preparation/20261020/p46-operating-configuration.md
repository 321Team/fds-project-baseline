# #46 운영 구성 연결표 — 코드 필드와 실제 채택 경계

이권욱 / CODEX_ASSISTED · 2026-10-22 00시대 KST. PR109까지 main 편입, PR110 `aebc03bbaa849f0b9660f66d29e480e0ce092e65` 검토본 기준이다.
이 문서는 기존 운영 준비를 실제 코드 필드에 대응시킨 **미채택 구성 명세**다. `delivery_job_site.SITE=None`을 유지하며 실행 설정/승인 JSON 로더·기본 운영값·실제 자격을 추가하지 않는다.

## 구성 순서와 책임

| 순서·코드 소비점 | 현재 재사용 가능한 근거 | 미확정/실행 중 생성 항목·담당·완료조건 |
|---|---|---|
| 1 `JobSite.runner` / `JobContext` | 기존 Runner 등록 label·P1 workflow identity는 후보. P2 workflow는 native Run/Attempt=1·main·workflow SHA를 직접 대조 | 권욱+재환: 실제 Runner 일반 계정/UID·도구/고정 경로·이전 job의 비신뢰 잔여 인수. `JobContext` RUN은 실행 중 생성값이므로 사전 제출/합성하지 않음. 정상 Runner/Worker를 일괄 kill하지 않음 |
| 2 `SiteConfiguration` / `Binding` | 승인 `fds-app`/overlay·Route host·두 current digest·최초 previous 명시적 없음을 재사용. 과거 API/cluster UUID/namespace UID와 관측 contract hash는 출처가 있는 후보 | 권욱 통합, 재환 clean source/render: 실제 RUN/action/기간·full image URI·render/contract/source·receipt hash와 input/Git/store root·소유권/단일 writer 결속. 이미지 source SHA·workflow SHA·manifest source SHA를 서로 대입하지 않음 |
| 3 `RuntimeAuthorityPlan` / `AdoptedGrant` / `plan_source_roles` | 기존 source pin 인덱스는 조회 후보. PR110은 각 original/control의 정확한 저장소 reader와 선택 Actions reader를 연결 | 권욱: 실제 원문 의미·Binding·principal/기간·control 수정/철회 의미를 검토 코드로 채택. creator ID·body hash·리뷰 승인/병합을 Runtime GO로 쓰지 않음. 저장소/원본이 다르면 대체 탐색하지 않음 |
| 4 `IssuerFacts` / `ExpectedSubject` / `SourceHandoff` | 배포 SA 이름·900초 정책·기존 #5 관측은 재사용. 개인 D-11d와 SA UID/실제 issuer 인증은 별개 | 하영+권욱/재환: 실제 CA/IP·issuer/audience·subject UID/groups·RBAC 근거, named admin→Runner 부모 메모리의 인증된 전달 경로 선택. token/fingerprint/발급·만료는 실제 job 준비 후 실행 직전 생성. source 자격은 ROSA와 별도·선택 저장소 최소 읽기 범위. 자격 원문을 새 제출 자료로 요구하지 않음 |
| 5 `ProducerFacts` / 선택 Actions 정책 | 이미 수신한 TBS Run38395350748·Push Run38404449622·공급 원본/current2개 재사용. workflow SHA와 앱 이미지 source SHA는 다름 | 재환: D22 FINAL 뒤 최종 clean render/source/contract·full URI와 test/build/scan/push 의미·scan 최신성을 결속. native wrapper step 성공만으로 내부 개별 검사를 인증하지 않음. 9/3 코드는 지원돼도 세 번째 실제 image·명시 채택 없이는 현재2앱 계약에 자동 추가하지 않음 |
| 6 `FinishObservationConfig` 또는 `FinishCollectorConfig` | post-close 객체/rollout 관측 생성부와 native 원본 locator/collector가 구현돼 있음. 둘을 모두 새 의무 절차로 요구하지 않음 | 권욱 통합+재환/하영: 실제 종료 scope와 생성 위치/해석 책임 선택. 해당 GO가 정확히 core 배포/객체 readback에서 독점을 끝낸 경우에만 제한된 관측 완료를 채택. 같은 독점 범위에 #47 C-STOP 쓰기가 남으면 조기 완료하지 않음 |

위 표는 기존 여섯 입력 묶음의 코드 대응이다. 새 팀 제출 양식·추가 서명·새 승인 단계가 아니다. 기존 원본을 재사용하고 새 변경/실제 미확정 항목만 담당자에게 연결한다.

## 권욱이 정리한 운영 권고와 아직 선택하지 않은 것

- 현재 2앱/6객체 소비 계약을 연결 준비의 기준으로 재사용한다. end-page의 실제 image·clean render·9/3 Binding 채택은 별도이며, 기존 전체 사양/AC를 면제하거나 축소하지 않는다.
- job 준비 뒤 실행 직전 발급 → 검토된 비공개 경로 → 부모 메모리 → PR110 별도 익명 pipe 순서를 권고한다. 실제 교차 호스트 전달 수단·주체 인증은 아직 미정이다. workflow 입력/환경변수/argv/로그·공유 폴더에 token 원문을 두지 않는다. 여러 허용 저장소의 동일 GitHub token 사용은 기존 최소 범위가 맞으면 허용하며 저장소별 발급을 강제하지 않는다.
- 900초는 token 수명이고 영속 claim 자동 만료가 아니다. rollout/readback 후에도 실제 finish 검증이 끝나기 전에는 claim을 자동 해제하지 않는다. 실패/응답 불명확은 기존 checkpoint/fence를 남기고 실제 원본으로 인수한다.
- #47 v1.1의 245분은 준비 제안이며 승인된 창이 아니다. C-STOP을 나중 별도 writer로 넘길지는 실제 GO의 독점 범위·인수 책임으로 정한다. 그 시점의 유효 권한/자격이 필요하며 70~80분 뒤 만료된900초 배포 token을 재사용·자동 갱신하지 않는다. 같은 기존 GO가 두 단계의 대상·행위·기간을 실제 포함하면 중복 GO를 요구하지 않는다.
- Runner→ROSA API443/GitHub 경로는 아직 현장 관측으로 확인하지 않았다. ROSA→사내 DB/Harbor의 VPN 결과로 대체하지 않는다. 공유 Runner의 다른 TBS/Push/Deploy 쓰기와의 비중첩은 실제 창을 정할 때 소비한다.

## 실행 전 수신할 기존 선행 결과

- 하영: C1C3 실제 캡처/적용 readback·TLS/인증/cold-pull·회수, 정상 pull Secret과 앱 SA2개 연결, 필요한 NP/플랫폼 receipt. (가) SA 결정만으로 실제 patch/readback 완료가 아니다.
- 하영/재환: DB Secret v2의 B1 인코딩·B2 receipt 실패·B3 trace/격리 환경 정리 보완본. 실제 v2 동일 원본이면 생성 HOLD를 유지한다. 비밀번호는 기존 비공개1:1로만 전달한다.
- 권욱: 위 원본과 실제 D22 FINAL·source/control·finish 범위를 같은 운영 구성에 채택한 뒤, 해당 단계의 독립 검토와 유효 실행 범위로 판단한다. 준비 문서 때문에 동일 시험·원본 반출·비용 승인을 반복하지 않는다.

## 상태·수명과 검증

코드 STATIC/MOCK/CI·사람 REVIEW·MERGE와 운영 채택/RUNTIME/AC 인수를 구분한다. PR110의 현 HEAD CI708=704 PASS/4 SKIP는 재사용하며 이 문서 작업에서 제품 시험을 반복하지 않았다. 코드 채택·자격 발급·서버 접속·새 GO·티켓 상태/AC·정본 발행은 변경하지 않았다.

10/23 Review 18:00~19:30·10/26 Close와, 기존 VPN/route의10/23 00:00 전 정리·Robot/정상 pull Secret의10/23 23:59 수명은 별개다. 승인 규모의 자원을 프로젝트 종료일까지 유지하는 비용 결정만으로 보안 수명이 자동 연장되지 않는다.

근거: [PR109](https://github.com/321Team/infra-cicd/pull/109), [PR110](https://github.com/321Team/infra-cicd/pull/110), [#42 D22](https://github.com/321Team/fds-project-baseline/issues/42#issuecomment-6293161531), [#47 v1.1](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-6315050301), [앱 SA 결정](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6315085580), [기존 증적 대장](evidence-roster.md).

## 10/22 01시대 자격 전달 경로 검토 이력 — 기존 SSH 운반부 재사용 우선 권고

**권고이며 실제 채택/구현 완료가 아니다.** [#82 10/20 실행 보고](https://github.com/321Team/infra-ansible/issues/82#issuecomment-6283088910)와 당시 배치 helper의 동일 SHA 원본을 대조했다. 실제 관측 방향은 **B `ansible01` → A `cicd-runner01`**이며 역방향 성공을 추정하지 않는다.

| 기존 근거 | 재사용 가능 범위 | #46에 그대로 가져오지 않는 부분 |
|---|---|---|
| 검증 SSH key/known_hosts를 사용하는 관리 전송, 코드의 `StrictHostKeyChecking=yes`·`IdentitiesOnly=yes`·`BatchMode=yes` | 새 외부 중계 서비스·SSH key·root 작업을 먼저 만들기보다 기존 관리 SSH 운반부를 후보로 검토 | 당시 경로 성공을 현재 접속/host key·ROSA named admin 권한/issuer 위치·TokenRequest 허용으로 확대하지 않음 |
| 기존 Runner host/account·UID의 10/20 배치/readback | 기존 P1 workflow의 문자열 후보 외에 역사적 호스트 관측 출처가 있음. 현재 P2 채택값과는 분리 | 지금 실제 호스트를 다시 접속·인수했다고 쓰지 않음. 다른 회차의 등록/삭제 token·sudo 예외·GO를 재사용하지 않음 |
| `release-ci88.py`의 packet 전송/삭제·회수 보고 | SSH 운반과 당시 절차의 추적 근거만 참고 | 이 helper는 SCP로0600 packet 파일을 전달한다. **#46 메모리 전달에는 그대로 호출/복사하지 않음**. 임시 파일도 같은 제한이며 현재 별도 실행0 |

### 연결 순서와 실제 구현 공백

1. 자격을 발급하기 전에 실제 issuer 위치/기존 권한, 운반 경로, 정확한 대기 job의 연결점을 정한다. 현재 named admin이 어디에서 작업하는지 확인되지 않았으므로 CloudShell/ansible01 중 하나로 단정하거나 관리 호스트에 ROSA 로그인·권한을 추가하지 않는다.
2. 검토된 Runner/구성에서 해당 job의 native repository·Run/Attempt·workflow SHA와 실제 Binding을 대조하고 ready 상태를 만든다. 이 실행 식별값·1회 준비 식별자는 그 실행에서 생성되며 지금 값이나 미래 hash를 만들지 않는다. ready/식별자는 Runtime GO를 대체하지 않는다.
3. 준비된 job을 대상으로 기존 named admin 절차에서 실행 직전 자격을 발급한다. source token은 실제 original/control pin의 저장소와 기존 reader 기능에 필요한 최소 범위로 별도 전달한다. 저장소별 발급이나 새 GitHub App 설치를 의무화하지 않는다.
4. **당시 미구현은 교차 호스트 수신을 정확한 job 부모에 결속하는 1회 ingress였다. 아래 09시대 구현 delta와 구분한다.** SSH remote process stdin은 그 job의 stdin/부모 메모리가 아니며 `PipeCredentialReceiver(fd>=3)`도 아니다. 원격 명령 하나로 연결됐다고 처리하지 않는다. 실제 SSH peer/정확 job rendezvous·수신 소유권 채택은 여전히 잔여다. 새로운 socket/FIFO/daemon·수신 경로를 설치하거나 기존 anonymous-pipe 계약을 변경하지 않았다.
5. 실제 자격이 모두 부모 메모리에 들어온 뒤에만 PR110 `build_owned_invocation`을 호출한다. 이때 `config/plan/finish_slot`·ROSA token·`SourceHandoff` tuple·`wire`를 명시적으로 넘기며 내부의 별도 익명 pipe·EOF·소유권 인계로 연결한다. **공동10초는 이 내부 준비/수신 예산**이므로 사람 대기·SSH 협상·발급을 이 안에 넣거나 매 저장소 갱신하지 않는다. 그렇다고 교차 호스트 준비 시간을 무제한 허용하는 것은 아니다. 실제900초 수명·승인 종료·최초 쓰기 잔여 예산은 계속 소비된다.

최소 후속 확인은 **하영의 실제 issuer 작업 위치/기존 발급 권한**과 **권욱·재환의 정확한 대기 job에 연결할 수신 소유권/관리 경로**다. 이미 수용한 Route host/current/원본·개인 D-11d·기존 Runner 시험 전체를 다시 제출받는 절차가 아니다. 후속 peer/직렬화/수신부를 선택하기 전에는 `SITE=None`을 유지한다.

### 실패 인수와 검증 범위

- 오접속·옛 Run/Attempt·잘못된 Binding은 자격 전달 전에 차단해야 한다. 교차 호스트 ingress의 replay/정확 job 결속은 **당시 미구현/미시험**이었다. 아래 새 구현의 오프라인 결과와 실제 현장 인증을 구분한다.
- 발급 뒤 지연·만료 임박, 부분 source 수신·전달 중복·EOF 누락·용량/문법 오류·ROSA/source bytes 재사용은 자동 재발급/재전송으로 넘기지 않는다. 기존 handoff의 오류·FD 정리 시험은 재사용하고, 아직 없는 ingress의 실패 시험을 실행했다고 쓰지 않는다.
- 응답 불명확/정리 실패는 해당 회차의 소유 자원과 책임을 인계한다. 로컬 close/프로세스 종료는 서버 자격 회수나 전체 배포 원복의 증명이 아니다. 정상 Runner/Worker·다른 job을 광범위하게 종료하지 않는다.

이번에는 기존 소스/보고의 읽기·정적 대조만 수행했다. 실제 SSH/서버 접속·named admin 로그인·token 발급/전달·수신 경로 설치·운영 SITE 채택·Runtime은 모두 미실행이다.

## 10/22 09시대 구현 delta — 운영 입력과 분리된 전송부·부모 helper

[PR111](https://github.com/321Team/infra-cicd/pull/111) HEAD `96b483b5ff8c7d77eb80bc6b6ee03cc134af54a8`에 strict UTF-8 프레임·정확 job/Binding/nonce·1회 수신 core, 명시한 owned Linux pipe FD의 송수신 adapter, `ParentJobBuilder`를 구현했다. 공개 ready→새 요청/마감 재확인→검토된 channel 수신→PR110 별도 익명 pipe→기존 driver 순서다. peer receipt/nonce는 인증·GO가 아니며 실제 SSH 프로세스·listener·issuer를 기본으로 설치하지 않는다.

- [Linux hosted CI](https://github.com/321Team/infra-cicd/actions/runs/39698307687) **763=759 PASS/4 SKIP**, 실제 로컬 pipe→부모 helper→수신 core→기존 pipe/driver/factory/finish 연결 포함. Windows **763=663 PASS/100 SKIP**. 첫 Linux 실패 1건은 재사용 거부 시험 helper의 잘못된 요청을 수정한 뒤 통과했으며 제품 코드는 그 수정에서 불변이다.
- 미확정 운영 입력 없이 구현한 core/helper 범위다. 실제 두 호스트의 SSH 인증·현재 host key·정확한 job rendezvous, 하영 issuer 위치/권한·UID/CA/IP·운영 자격, 권욱의 source/control·Binding·finish/경로 채택은 여전히 잔여다. monotonic 숫자를 다른 호스트의 절대 시각으로 보내거나900초 수명을 갱신하지 않는다.
- PR111은 독립 코드 리뷰·병합 전이다. PR110의 하영 명시 범위 승인을 남은 재환 영역으로 확대하지 않는다. 문서 PR195는 실행 입력이 아닌 준비 기록이므로 [REVIEW_AUTHORITY_POLICY §2](../../../governance/REVIEW_AUTHORITY_POLICY.md)에 따라 Lead 검토로 병합 가능하며 별도 이중 승인을 추가하지 않는다. 이 기록의 병합은 코드/Runtime GO·정본 발행·티켓 완료가 아니다.
