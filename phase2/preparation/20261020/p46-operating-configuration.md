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
