# Phase 1 전체 인계 대조와 실행 준비

**10/13 저녁 최신 진입점:** [Phase 1 잔여·병행 작업과 새 이미지 재검증 카드](REMAINING_AND_PARALLEL_20261013_EVENING.md). §6에20:10 TBS 결과, §7에 PR78·증적 PR215 병합과 PR216 대장 충돌 해소 재검토·수정본 새 실행 잔여를 기록했다. 아래 오전/과거 기록은 해당 시점 이력이다.

이권욱 / CODEX_ASSISTED · 작성 2026-10-10 KST, 회신·소스 현행화 2026-10-11 KST. 사용자 요청: 권장한 전체 항목 대조 → 최소 검증안 → 작업 순서 → DR 수령 → 운영 인수 준비를 순서대로 처리한다.

## 적용 기준과 현재 단계

2026-10-13 추가 관측·남은 실행 순서는 [병행 실행·인수안](PARALLEL_EXECUTION_20261013.md)을 함께 본다. 아래 현재 반영표를 우선 사용하고, §1의 24개 ID 표는 10/11 당시 인계·준비 기록으로 읽는다. 기존 AC·판정·담당은 변경하지 않는다.

| 연결 ID | 10/13까지 확보한 후속 근거 | 실제 남은 범위 |
|---|---|---|
| H02/H04/J05/S03 | [증적207](https://github.com/321Team/fds-project-evidence/pull/207)·[208](https://github.com/321Team/fds-project-evidence/pull/208) 병합: IF06B, K8S17파일, OID02 반입, 앱 배치 복구 | 각 미충족 AC·부팅/OID03·최종 형상 회귀. 위 실행 재수행은 요구하지 않음 |
| J03/U01/D01/S05 | 10/11 dump 수령 및 [10/13 D1 비공개 대장 연결 회신](https://github.com/321Team/fds-project-baseline/pull/164#issuecomment-6135167475) 확보 | DR 인수 기록. D01 공유 ACL 미조회·보존 조건 유지 |
| J06/J04 | [DB·DR·관리 접근 인수안](DB_DR_ACCESS_CLOSEOUT_20261012.md)에 W4 사실 확인과 G1/G2 회신 연결 | W4 한계 수용, DB 전체 요구 대조, Grafana 보관·회수 책임/감사 공백 판단 |
| C01 | SEC 팀3명 기준 + 이권욱의 “승인받은 인원만 접근 가능” 확인 수신 | 관리자 추가 질문 종료. 기술적 실효 ACL 직접 대조는 미수행으로 구분 |
| J08/O02/S04 | [증적209](https://github.com/321Team/fds-project-evidence/pull/209)·[210](https://github.com/321Team/fds-project-evidence/pull/210) 병합: 이재환 실습·정리, 알림 활성화 | 실제 정기 실행·경고 수신/처리는 기존 Ansible61에서 후속 확인. O01 제3자 재현·전역 엔진 전환은 별도 |
| S01/J02/J07 | 07:51 Push·receipt·두 remote digest 확보, 증적208 병합 | Deploy/복귀 → 최종 형상에서 필요한 HA·APP 회귀. [APP/HA 카드](APP_HA_EXECUTION_CARD_20261013.md) 사용 |

병행 범위는 서버 작업창을 사용하지 않는 인수안·회신/증적 연결이다. Harbor 구현과 Runner 후속 확인은 기존 작업에서 계속하며, 이번 현행화가 새 실행·인수 승인·티켓 종결은 아니다.

범위는 [PR160][p160]의 인수 대상 전체에 [PR161][p161]의 정정·추가 회신을 반영한 **Phase 1 잔여**다. #161의 U01~U03만 처리하는 범위가 아니다. [#30 이관 결정][transfer]에 따라 이권욱이 실행·검증·결과 수용을 통합하고 원 담당자의 사실 제공·기존 독립 리뷰를 유지한다. 새 Lead GO, 전체 회신 완료 Gate, Phase 2/ROSA/IF19 사전 작업을 추가하지 않는다.

이 문서는 기존 인계 원문·sealed 증적·AC·Status·Due를 덮어쓰지 않는 실행 준비 대조본이다. `회신 수신`, `자료 수령`, `코드 병합`, `Runtime`, `AC 인수`를 구분한다. 조건부 계획의 작성 완료를 현장 준비 완료로 표시하지 않는다. 최종 실행값은 해당 회차 직전에 확인한다.

2026-10-10 20:32 KST부터 GitHub API로 baseline #10/#11/#13/#14/#15/#16/#17/#19/#20/#21/#22/#24/#30 및 infra-ansible #9/#61의 본문·전체 댓글을 확보했다. 최신 AC/Status 갱신절·관련 결정 및 아래 고정 소스를 대조했다. 과거 본문에 남은 중단 지시·미수령·3600초 설명은 작성 당시 기록이며 최신 사용자 요청과 후속 근거를 함께 적용한다. 프로젝트의 모든 티켓·현장 전체를 재검증한 것은 아니다.

| 근거 | 확인 버전과 적용 범위 |
|---|---|
| PR160 | 승인 HEAD `151a60536e6c18a9f6f3b0a1d20bf61db950b763`, merge `068411bd3bef2747587933a2b0b137810affb903` |
| PR161 | HEAD `21e7e6626159dc5e23b49fe6ac5d344bbb4f62fa`, merge `6e7b94ab8739038f25a006e2a55daaca92c36617`; 두 담당자 승인 후 MERGED. [U01~U03 회신][ureply] 수신, U03 실제 관리 접근은 미확인 |
| Token 정책 구현 | [CICD74][c74] merge `2d8a14c55ea4b61f53b7ac6d682cd5e97575dda7`; 독립 승인·CI 후 병합. 실제 발급·소비는 별도 |
| Harbor 수신 검사 | [Harbor41][h41] merge `a3caf48b49320edff2d89e61c8a996f0e34b70eb`; 패키지 검사이며 installer·H6·Runtime 완료 아님 |
| APP 판정 도구 | [APP30][a30] merge `c2372da3fd5ed01a01374b9ea57e34a58f86d3eb`; 기존 APP Source `affbc69`/공급 `8eac4c` 및 이미지 후보를 교체하지 않음 |
| K8S 형상 준비 | [PR78 PLAN][kplan], main `c42ea6cc3ccd197d12993823bed439d40946a54c` |
| MON 준비 | [MON42 최소 검증안][monplan], main `0dd0235b07d44ba7965490e3808e0a67a3bd903b` |

개발3건의 단계별 결과·현장 잔여는 [#161 후속 기록][progress]을 재사용한다. 10/11의 [수집·인계본](COLLECTED_INPUTS_20261011.md)에 최신 회신·고정 소스·현장 수집 항목을 연결했다. 개별 H/J/U 질문·원회신의 기준은 [INTAKE_STATUS](../phase1-remaining-20261009/INTAKE_STATUS.md)와 이후 실제 원회신이며, 아래 표는 실행 카드에 연결한 요약이다. 과거 원본/승인을 새 판정으로 바꾸지 않는다.

## 1. 전체 항목 대응 — 24개 ID

상위 H/J 입력과 하위 S 실행 묶음은 같은 작업을 다른 관점에서 참조한다. 24개를 24개 독립 시험·공수·승인으로 합산하지 않는다. 실행 책임은 모두 이권욱이며 표의 제공자는 사실/자료의 생산·보유 주체다. 완료된 인계 자료는 다시 요청하지 않는다.

| ID | 연결 AC/근거·확인한 단계 | 남은 최소 작업·완료조건 | 제공자 / 실행안 |
|---|---|---|---|
| H01 | #10 보관/형상; [실제 보관 인수][custody] 수신, 증적195 | 보관 인수 대기 해소. C01 접근통제와 실제 서버 backup/restore는 별도 | 이하영 수신 완료 / V01 |
| H02 | #10 AC4e·17파일, 별도 AC4c/d②/g·T14/T15; [H 회신][hreply] | 기대값과 복귀값 분리, 호출 배제·fresh backup/임시 복원·17/28 대조. 별도 미충족 처분 유지 | 현장값 이권욱 / V01·V02 |
| H03 | #19 AC02/04/05/06, #16 AC07/08; [R1][r12] 최대/요청900초 | 코드 정합화는 c74 병합. 실제 SA/CA/audience/TokenReview·소비·만료/회수 한계와 SEC 남은 행은 잔여 | 이하영 정책 수신 / V03·S01 |
| H04 | #14 AC12/15~18·OID02/03, #17 IF06B; [H 회신][hreply] | gateway 구간 귀속으로 준비. canary·관측 계정·회수 및 기존 SYN 기준과의 대응, OID 공급 근거와 reboot 조건 | 알려진 사실 수신 / V04·V06 |
| H05 | #13 AC04~06·#16; [R2][r12], [정정][jcorrect] | legacy 삭제 완료 유지. 조직/Harbor/edge 소비·Robot/CA/scan 유효성·.50/.102/IPv6/INPUT 처분은 실제 원본으로 판단 | U02/U03 해당 부분 / S01·S02 |
| H06 | #13 인수한 자동복구; [H 회신][hreply] | h41은 수신 검사. installer·H6·늦은 stop/세대 변경·부분 정책 복구, fresh UUID/10ID/예산/복귀점·private 원본 보존 | 미기록 제약·미확인 회신 수신 / S02 |
| H07 | #24 제3자 재현·Ansible61 운영 인수 | 문서 리뷰를 실제 재현으로 집계하지 않음. 적격 참여자·접근·회차·실제 정리 결과 | 참여 가능 여부만 추가 / O01·O02 |
| J01 | #15/#16 공급 ZIP·증적195; [J 회신][jreply] 보관 수령 완료 | 재전송/재수령 요청 없음. 사용 시점 scan/TLS/Robot·원 공급물 참조 검증 | 이재환 수신 완료 / S01 |
| J02 | #20 Final Regression·#15 metrics; [고정 회신][jreply]·증적68 | 새 RUN과 실제 운영 digest의 HTTP/DB/metrics·실패/복귀 결과. APP30의 도구 버전과 공급 Source 분리 | 기준 수신 완료 / V08·S01 |
| J03 | #21 DR 원본 인수; [10/11 후보][jcorrect] | U01의 기존 콘솔 전달 실사용 확인. 당일 경로·정확한 비중첩 창·5,206B 원본 수신/해시/권한/보존. 수신을 Restore 성공으로 표시하지 않음 | 이재환 원본 전달 / D01 |
| J04 | #17 Grafana 관리 접근; [J 회신][jreply]·MON42 | 알려진 과거 사용/회수와 미확인 앱 credential 보관/감사를 구분. 참조 위치를 실보유/유효 암호로 추정하지 않음 | 추가로 생긴 사실만 / V05 |
| J05 | #17 IF06B/Probe·#14 ICR-AC18 | Source/401/Discord/Probe 기존 증적 유지. 8443 귀속·해당 현장 관측. Node reboot는 ICR에 연결 | 운영 입력 이권욱 / V04·V06·V08 |
| J06 | #11 W4·관련 FUP; [J 회신][jreply] | 20:26:49~20:27:52 등 미측정 범위·원본 공백의 영향/유효 처분. 새 시험으로 과거 5xx0 생성 금지 | 없는 자료 재요청 없음 / V09 |
| J07 | #22 HA·증적92; [J 회신][jreply] | 10/2 worker02 1회 GET 범위 보존, 9/27 NOT_VERIFIED. 10/7 배치 변경 영향과 최소 재시험/한계 판단 | 비교·판정 이권욱 / V07 |
| J08 | #24·Ansible61; [J 회신][jreply] | 제3자/두 번째 운영자 실제 참여·공급/인증/회수 원본. 이름만 지정해 완료 처리하지 않음 | 참여 가능 여부만 추가 / O01·O02 |
| C01 | 증적195 보관6묶음 접근통제 | SMB 공유 ACL·허용 계정/그룹·NTFS 실효 권한과 보관자 접근. 로컬 해시/읽기 성공은 권한 증거 아님 | 실제 공유 관리자 미확정 / C01 절차 |
| S01 | #15/#16/#20 Delivery·최종 회귀 | 승인 Source/최신 workflow·대상/복귀 digest·정상/Negative/rollback/최종형상 결과. 새 Push receipt를 이후 Deploy에 결속 | 이권욱, 기존 후속 작업 계속 / E01 |
| S02 | #13 복구·자동복구 | 현재 구현 재사용. 실제 package/installer·H0/metadata/context/원 policy/복귀점·H6를 단계별 입증 | 이권욱, 기존 후속 작업 계속 / E02 |
| S03 | #10/#14/#19/#17/#22 | V01~V07의 미입증/미충족 행만 구체화. 기존 승인·위험수용을 새로 만들거나 낮추지 않음 | 이권욱 / 최소 검증안 |
| S04 | Ansible9/61 | 기존 PR76 회차의 worker02 apply/reapply/rollback·별도 운영 엔진 전환, 상시 queue/알림과 운영자 실습 | 이권욱 / V10·O02 |
| S05 | #11/#21/#24/#30 | D01 수신·V09 처분·C01·O01/O02·최종 형상/하위 AC를 최종 인수에 연결 | 이권욱 / D01·O01~O03 |
| U01 | J03 전달 경로 | [회신][ureply] 수신: 10/8 db01 콘솔 붙여넣기 실사용 및 10/10 입력 문제 해소. 실제 dump 수신·당일 경로·비중첩 창은 별도 | 이재환 전달 / 이권욱 수신, D01 |
| U02 | H05 조직 Secret | [조직 관리자 이재환의 UI Actions Secrets0건 회신][ureply] 수신. 기존 CLI403 보존, Variables/Dependabot/Codespaces 미조회. 전체 credential 부재로 확대하지 않음 | 이권욱 범위 대조 / E03 |
| U03 | H05 Harbor 접근 | [미확인 사유 회신][ureply] 수신: 10/10 서비스 미기동 보고. 정상 기동 후 실제 로그인·Robot 메뉴 확인 필요. timeout만으로 특정 규칙 귀속 확정 금지 | 이재환 접근 확인 / 이권욱 회차, E03 |

[V01~V10 최소 검증안](MINIMUM_VALIDATION.md)과 [E/D/O 실행·인수 순서](SESSION_AND_HANDOVER.md)가 위 표의 실행 상세다. `전체 ID 대응`은 24/24이며 전체 AC MET 또는 현장 실행 완료율이 아니다.

## 2. 이미 해소된 대기와 유지할 미확인

- H01/J01 보관 수령과 R1 900초 정책 의미는 수신됐다. Token 코드도 병합됐으므로 다시 개발하거나 정책 승인을 요청하지 않는다.
- 10/1 legacy Secret 삭제를 다시 수행하지 않는다. 조직 403·실제 Harbor/edge 소비는 별도다.
- #10의 AC3/5, #19의 AC01/03, #144/#157/#152/#173/#177/#180의 각 수용 범위는 유지한다. 과거 성공을 새 환경 전체 성공으로 확대하지 않는다.
- U01~U03 답변은 [수신][ureply]했다. U01 전달 실사용·U02 관리자 UI 관측 회신과 U03 실제 관리 접근 미확인을 구분한다. C01의 로컬 SMB 연결 메타데이터 조회도 10/10 이번 작업에서 `Access denied`였다. 이는 공유 공개/폐쇄 판정이 아니다. 권한을 높이거나 공유 ACL을 수정하지 않았다.
- 개발3건 병합 후에도 실제 회귀·H6·현장 복구·DOC Freeze는 미실행/미완료다. 기존 APP 원본은 그 회차에서 쓴 도구로 해석하며 새 검증기에 맞춰 수정하지 않는다.

## 3. 리뷰와 필요한 회신을 한곳에서 처리

이하영은 H02/H03/H04/H06 및 V01~V04/V06의 기존 기준·원복 경계, 이재환은 J02~J08 및 V05/V07~V09/D01/O01/O02의 기존 기준과 알려진 사실을 검토한다. 이권욱이 준비·실행을 통합하며 원 담당자에게 시험 결과 전체를 다시 만들도록 요구하지 않는다.

추가 회신은 다음 최소 항목으로 한정한다.

1. **기존 U01~U03:** #161의 [실제 회신][ureply]을 사용한다. 같은 질문은 다시 하지 않고 당일 변동·실제 수행 결과만 연결한다.
2. **C01:** 10/13 이권욱의 승인 인원만 접근 가능 확인을 수신했다. 관리자·조회 경로 추가 질문은 종료하고 사용자 확인과 기술적 실효 ACL 직접 미검증을 구분한다. [상세 범위](DB_DR_ACCESS_CLOSEOUT_20261012.md)를 사용한다.
3. **O01/O02:** O02 제2운영자 실습은 이재환의 실제 공급·인증·회수 결과로 확보됐다. 같은 참여 질문·실습을 반복하지 않고 실제 알림 수신 잔여를 #61에서 연결한다. O01 제3자 재현은 적격성·대상·정상 접근·정리 조건을 갖춘 별도 회차 판단이며 O02 완료로 자동 대체하지 않는다.

회신은 `항목 ID / 확인 사실·근거 또는 미확인 / 제공·참여 가능한 범위 / 가능한 시점이나 선행조건`만 받는다. 새 정책·예외·기한을 승인한 것으로 처리하지 않는다. 담당자가 이미 모른다고 답한 과거 원본/credential 이력을 반복 요구하지 않는다.

## 4. 준비 완료와 현장 잔여

이번 산출물은 전체 대응표·최소 검증 조건·자원 충돌표·DR 수령 절차·운영 인수 카드다. 새 서버 실행·계정/Secret 삭제·권한 확대·DB 쓰기·서비스 재시작·AC 체크/종결·정본 발행은 수행하지 않았다. 실제 리뷰 지정·CI 결과는 발행 PR의 정확 HEAD와 함께 기록한다.

실행 입력 미확정으로 조건부인 V01/V04/V06/V07/V08/V10/E01/E02는 해당 값이 채워져야 실행 가능하다. V02/V09는 기존 한계의 처분 검토이며 자동 시험/자동 예외 승인이 아니다. 회신 대기 중에는 비의존 문서·코드 검토를 계속한다.

[p160]: https://github.com/321Team/fds-project-baseline/pull/160
[p161]: https://github.com/321Team/fds-project-baseline/pull/161
[transfer]: https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6082618226
[r161]: https://github.com/321Team/fds-project-baseline/pull/161#pullrequestreview-5477670195
[custody]: https://github.com/321Team/fds-project-baseline/pull/160#issuecomment-6083078172
[hreply]: https://github.com/321Team/fds-project-baseline/pull/160#issuecomment-6083293377
[jreply]: https://github.com/321Team/fds-project-baseline/pull/160#issuecomment-6082572533
[r12]: https://github.com/321Team/fds-project-baseline/pull/160#issuecomment-6084886811
[jcorrect]: https://github.com/321Team/fds-project-baseline/pull/160#issuecomment-6084948949
[progress]: https://github.com/321Team/fds-project-baseline/pull/161#issuecomment-6096980417
[c74]: https://github.com/321Team/infra-cicd/pull/74
[h41]: https://github.com/321Team/infra-harbor-trivy/pull/41
[a30]: https://github.com/321Team/fds-msa/pull/30
[kplan]: https://github.com/321Team/infra-kubernetes/blob/c42ea6cc3ccd197d12993823bed439d40946a54c/ops/p1-k8s-01-v4/reconciliation/PLAN.md
[monplan]: https://github.com/321Team/infra-monitoring/blob/0dd0235b07d44ba7965490e3808e0a67a3bd903b/docs/MON_MINIMUM_TEST_PREPARATION_20261009.md

[ureply]: https://github.com/321Team/fds-project-baseline/pull/161#issuecomment-6098286300
