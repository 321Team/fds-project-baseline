# Phase 2 사전 준비·인계 갱신 — 2026-10-16

조회 기준: 2026-10-16 17:02 KST. 이권욱 / CODEX_ASSISTED. 기존 준비표의 최신 인계이며 실행 승인·정본·As-built가 아니다. 과거 문서/댓글은 당시 이력으로 보존한다. #34/#39/#42/#46/#49/#52/#55와 관련 milestone·선행 #30~#33을 재조회했다.

## 순차 수행 결과와 잔여

| 순서 | 실제 결과 | 다음 담당·완료조건 |
|---|---|---|
| 1 IAM 소스 리뷰 | [Terraform PR33 답변](https://github.com/321Team/infra-terraform/pull/33#issuecomment-6210747849), `de5e1666`: 실제 부착 snapshot 대조. 기존31검사에는 MFA 조회/실제 AssumeRole 미포함 | 재환: probe 포함 변경 독립 리뷰. 하영: 10/17 실제05·Expiration·실패 시 키 정리. IAM 재적용·10/18 확대 없음 |
| 2 ROSA 코드 | [PR40](https://github.com/321Team/infra-rosa/pull/40) `7e609540` 전체 승인·merge `3742118e` 완료. [PR41](https://github.com/321Team/infra-rosa/pull/41#pullrequestreview-5544602545) `4db908d1` R1~R5 해결, 기존 delta15 MOCK 재사용 | 재환: PR41 권욱 제안 반영분 독립 확인. 하영: rev4.1 시간/권한 문구 정합화. 첫 설정/정책 Apply·DB 창은 별도 |
| 3 #46 | [CICD Draft PR87](https://github.com/321Team/infra-cicd/pull/87) `fb30d01f`: verifier/session/차단 CLI·객체 대조. Windows154 PASS/41 SKIP, Linux184 PASS/11 SKIP, CI2 SUCCESS | 하영·재환 독립 코드 리뷰. 권욱: 원본 인증/철회·bounded I/O·actual provider/CLI·완료 관측 연결. 아직 실제 배포 불가 |
| 4 #42 | [A 방향 채택](https://github.com/321Team/fds-project-baseline/issues/42#issuecomment-6207939448)을 [기존12출력](d22-lead-review.md#1016-a안-채택과-소비-완료조건)에 연결 | 하영 플랫폼/auth/cold-pull·재환 공급 원본 → 권욱 Final/전환 판단. 방향 재선택·중복 빌드 요구 없음 |
| 5 #34/#39/#33 | 아래 7입력 및 공식 Start 경계 정합화 | 권욱은 실제 원본 수신/검토 부분만 갱신. 생성·PR 병합으로 Gate 완료 처리하지 않음 |
| 6 #49/#55 | 아래 candidate·위험/정리/Review 대응표 준비 | 기존 생산자 원본 → 권욱 수신·검토/고정 → 해당 단계 승인. Freeze/Review/Close 미완료 |
| 7 #52 | 10/23 날짜·14:00~15:30 제안·권욱 참석 미정 유지 | 실제 회신 후 시간/참석/대체·Demo 확정. 준비 작업의 차단 아님 |

PR40/41/33의 CI0은 NOT_RUN이며 PR87의 CI2와 구분한다. PR40 권욱 작성분의 독립 확인은 [재환5542425469](https://github.com/321Team/infra-rosa/pull/40#pullrequestreview-5542425469)·[5542886163](https://github.com/321Team/infra-rosa/pull/40#pullrequestreview-5542886163), 최종 전체 승인은 [5544582691](https://github.com/321Team/infra-rosa/pull/40#pullrequestreview-5544582691)이다. PR87 자체 검토를 타인의 독립 승인으로 표시하지 않는다.

## #34 / #39 G4의 7개 입력

| 입력 | 수용된 사실·현재 판정 | 완료조건 / 담당 |
|---|---|---|
| 1 Architecture Freeze | [#34 결정](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-6207926205)의 public/public·생성 입력/인터페이스, D22 A·추가 DNS 보류. 전체 Freeze 미완료 | 권욱: 사양/실행 입력/As-built 차이를 변경결정에 연결. 미생성 UID 합성 금지 |
| 2 Full IaC | [Stage-A 정정 수용](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6207104552). 기반·태그·이전 readback 재사용, STAGE_A_READY=NO·Full 미완료 | 하영 #35: route/SG 생산·별도 Plan/검토/GO·실측/원복·최종 인계. Create GO로 자동 승인하지 않음 |
| 3 D21 | OCI NO-GO / AWS Relay 결정·기편입 원본 재사용 | 권욱 #36: 기존 결과/잔여 연결. 새 OCI 시험·재선택 없음 |
| 4 VPN | [#37 rev4.1 수용](https://github.com/321Team/fds-project-baseline/issues/37#issuecomment-6207955685), 기수용 터널 단계와 생성 후 C/D 분리 | 하영 actual worker/ENI/시험 Pod, 재환 분류표·관측/T3·원복, 권욱 정확 DB 창. 전체260분 후보와 DB120분 상한 구분·생성 중 비중첩 |
| 5 ROSA 준비 | v6 검토·[10/17 lead 위임 조건부 Create GO](https://github.com/321Team/infra-rosa/issues/4#issuecomment-6209744491)·[본인 키 IAM 반영](https://github.com/321Team/infra-rosa/issues/4#issuecomment-6210075843) 연결 | 하영: 05 실제3시간/잔여150분, 30 직전 fresh session·preflight15분·승인 범위 최초1회. 실패 HOLD·키 정리·원본 보존. 생성/Ready 미실행 |
| 6 비용 | 지정 비용 채팅의 10/16 사용자 표 $7.95/₩10,860. 교육장 지원·자부담0·400/450/500 유지 | 권욱 중앙 판단. 동일 청구기간·예상 총액 미확인, 하루 사용료/전체 누적/잔여예산으로 임의 확대하지 않음 |
| 7 Critical/예외 | [Create-only G4 예외](https://github.com/321Team/fds-project-baseline/issues/39#issuecomment-6207939140), G4 NOT_READY. [F5 위험 수용](https://github.com/321Team/fds-project-baseline/issues/38#issuecomment-6207939779) 별도 | 권욱: 대상·잔여·소유/완료조건 보존. 재생성 NOT_RUN을 PASS로 바꾸지 않고 나머지 Full/P0 충족 판단 |

D1은 최신 사용자 결정으로 **10800 고정**이며 예전 생성 후3600 원복 문구는 적용하지 않는다. [#35 IAM 기록](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6209035655)은 설정값과 실제 세션 발급을 구분한다. 10/17 최초 실행·관찰/정리·반출 경계는 GO 원문을 따른다. 10/18 새 키/30 재시도·기한 연장을 이 표에서 허용하지 않으며, 조건 충족 시 권욱의 추가 실시간 GO 대기를 일률 요구하지 않는다.

### 공식 Start와 Phase1 인계

[#33 공식 Start HOLD·선행 예외](https://github.com/321Team/fds-project-baseline/issues/33#issuecomment-6120258410)를 유지한다. #30 최신 [D02 통제 수행 인수·문서 반영](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6208668917)은 대기 한 항목 해소이며 전체 P1 인수/Sign-off가 아니다. #31/#32에서 이를 대체할 전체 완료/서명은 이번 조회로 확인하지 못했다.

권욱은 기존 P1 Review/Close Action·P0 판정·Known Issue/Deferred/Residual Risk의 Owner/Due/수신처·Close Sign-off가 확정되면 #33에 소비한다. P2 준비를 위해 Phase1을 재구축/재시험하거나 D02 기술 미충족을 삭제하지 않는다. 열린 이슈 개수만으로 Gate를 판정하지 않는다.

## #49 / #55 후속 인수 준비

기존 [I01~I16 인수표](evidence-handoff.md)와 [생성·정리·90분 Review 운영안](lifecycle-review-preparation.md)을 재사용한다. 같은 자료를 새 양식으로 전수 재작성하지 않는다.

| 단계 | 현재 연결한 준비 | 이후 완료조건 |
|---|---|---|
| #49 rolling → #54 Freeze | Architecture/IaC/ROSA/VPN/App/CICD/Test/Decision/Known Issue와 위 source·단계 연결 | 생산자 실제 원본 식별/버전·해시·수신·내용검토·승인/병합·미확인을 같은 immutable candidate에 고정. stale 링크/미병합 evidence/source 불일치/manifest 누락 확인 후 권욱 Freeze 판단 |
| #53 G6 | DB/Registry·E2E/회귀·Critical0과 승인 예외 분리 | 실제 #47/#50·Registry/복구 증적. Lab/STATIC/MOCK을 ROSA Runtime으로 승격 금지. P1 OADP는 실행 결과 또는 Deferred/N/A 근거 |
| #55/#56 Review | G6·Freeze candidate·P0/위험·Demo/비용/잔존·Review Action 연결 | 승인 일정/참석·실제 수행·결정/Action/담당/Due. 준비 완료를 회의·승인 완료로 표시하지 않음 |
| 삭제·보존 | exact 자원/소유·의존성·보존 state/원본·전용/운영 권한 분리 | 검증·재시험·증적 검토/필요 Demo 종료 후 별도 삭제 판단. D2 보호 해제와 새 D3 destroy Plan·실제 삭제/readback/잔존·비용 기록. 날짜만으로 삭제/회수 금지 |
| #57 Close | Review Action·P0/예외·후속 P1/Known Issue·자원/비용·Source/Deliverable 인계 준비 | 실제 완료/미완료·수신/책임과 Project Close Sign-off. 준비 PR 병합으로 자동 종결하지 않음 |
| 발표 #25 | [정정 수용](https://github.com/321Team/fds-project-baseline/issues/25#issuecomment-6210784433), Discord 예외 철회·P1 영상 재사용 | 재환 최종본·식별/해시·구간·노출/재생 검수 → 권욱 장면 검수. 현재 영상 미수신·미검수, ROSA Runtime/AC 아님 |

검증 전용 권한은 승인된 준비→시험→결함 재시험→증적 반출·검토 완료까지 유지한다. 작업창/파일 전송마다 회수하지 않으며 검증 종료 후 운영 최소권한과 구분해 정리한다. 분리 정책 재부착/새 부여 승인이 아니다.

## 일정·보류·실행 경계

- #52/#56 Review/Freeze10/23, #57 Close10/26 유지. 14:00~15:30은 제안, 권욱 참석 미정. 하영·재환 참석/대체·live Demo 필요 미확정. 같은 질문·초대·확정 기록을 반복하지 않았다.
- #40/#48/#120 우선순위 P1은 Deferred 유지, 취소 아님. 타 담당 선택을 대신 확정하지 않는다. 우선순위 P1과 Phase1 운영 경계를 구분한다.
- Phase1 DB/pg_hba/영구 방화벽/NetworkManager/route/Harbor CA/Runner/공용 OCP/DNS/LB/AC 변경 없음. namespace는 `fds-app`, `rosa-app`은 overlay다.
- 준비 문서 외 AC/정본/일정 속성 변경 없음. 복구는 문서 커밋 revert이며 실제 서버 원복 대상은 없다. 비공개 raw Plan/state/credential 공개 없음.

STATIC=문서/링크/범위 대조. MOCK/CI는 각 PR의 명시 범위만 소비한다. 이 문서 REVIEW/병합은 준비 기록 처리이며 RUNTIME·정본 PUBLICATION·종결과 구분한다.
