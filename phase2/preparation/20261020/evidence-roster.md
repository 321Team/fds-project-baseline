# #49 증적·산출물 접수 대장

기준: 2026-10-25 13:03 KST. PR145~147 병합·PR148 producer 연결 검토, 실제 P2 환경 준비와 기존 공급 원본/native 대응을 추가했다. 다른 행의 관측 시점·한계는 유지한다. 생산·공유·수신/재해시·내용 검토·증적 편입·AC 인수는 별개이며 변하지 않은 원본/시험은 재요구하지 않는다.
기존 [하영 회신](https://github.com/321Team/fds-project-baseline/issues/49#issuecomment-6291485599)·[재환 회신](https://github.com/321Team/fds-project-baseline/issues/49#issuecomment-6291988326)을 재사용한다. 생산·공유·수신/재해시·내용 검토·증적 편입·AC 인수를 각각 구분한다. 원본 전체 재제출이나 동일 시험 반복은 요구하지 않는다.

| 대상·생산 책임 | 현재 확인 범위 | 편입·인수 상태 / 다음 완료조건 |
|---|---|---|
| D21 / 권욱 | [#36 사용자 한계 수용·최종 인수/종결](https://github.com/321Team/fds-project-baseline/issues/36#issuecomment-6330828733), ev161 기존 독립 편입 재사용 | Done/closed. 미수집 원본·명령/RC/version은 수용된 한계이며 전체 tunnel/G4/후속 AC PASS가 아님 |
| D24 Review 일정 / 권욱 | [운영 WBS/Calendar](../20261022/FDS_Phase2_Review_Operating_WBS_20261022.xlsx)와 기존 PR194 계획/ICS 사용 | 10/23 18:00~19:30·세 Record 동일 시간. 초대 또는 회의계획 요건을 적용하며 실제 회의/Freeze/Close는 별도 |
| D-11d 원본 / 권욱·재환, 편입 하영 | 권욱 공유·재해시·내용 검토, 교차 독립 검토 연결 완료 | [ev249](https://github.com/321Team/fds-project-evidence/pull/249) MERGED `04464931ae70fc4d78fb2601d6cc2c384487b317`. 18파일 편입이며 전체 ROSA AC 완료와 구분 |
| Stage-B VPN / 재환 | 10/15 기존 수용·원본 편입 재사용 | [ev239](https://github.com/321Team/fds-project-evidence/pull/239) 기존 병합. 현재 창 A/B/C 전체 PASS로 확대하지 않음 |
| 창 A / 재환·하영 | T1/T3 PASS, T3-R 성공, T6 INCONCLUSIVE 유지. DB W4·P9/P8·양쪽 V9 원복·정리의 기존 원본/한계 재사용 | [ev250](https://github.com/321Team/fds-project-evidence/pull/250) MERGED `eadec9f53cb9f1e13877f2e9a02779ef785aa366`. 38변경 blob·manifest35/35·공개 archive 내부22+1파일 대조. SPI 포함2원본은 비공개, 공개 정제본은 치환6곳 외 동일. T6·수집/절차 한계를 보존했으며 전체 AC PASS로 확대하지 않음 |
| G4 후속 / 하영·재환→권욱 | #7 B/A·N3, C7 일부 미실행. [#39 입력](https://github.com/321Team/fds-project-baseline/issues/39#issuecomment-6288503072) | 기존 원 AC의 잔여와 처분 근거 필요. T6를 PASS로 변경하거나 보류만으로 G4 완료 처리하지 않음 |
| PG-03 / 하영 | 6-1 기존 관측과 코드 수정 이력 재사용. [앱 SA Pod6 보고](https://github.com/321Team/fds-project-baseline/issues/38#issuecomment-6361610081): 10/23 18:15:32 restricted-v2·runAsUser1000840000, 두 앱 SA·Ready6/6. [공유 반출](https://github.com/321Team/fds-project-baseline/issues/38#issuecomment-6366473628) 뒤 중앙 10/23 23:53 기록에서 수신·해시·의미 검토 완료 | **반출/중앙 수신 대기 해제**. SHA256 `f0c6fe2444362bc64d55d7dfaa1e0043222b508b0e57d0a96787329acf22628e`, 앱 SA·승인 image/imageID·Ready·restricted-v2·UID 대응 6/6. 원본은 필드 투영 6행이며 full Pod API JSON이나 #46 6객체 baseline이 아님. ev251 편입·Full Security·전체 #38 AC 완료로 확대하지 않음 |
| Harbor C1C3·창 B / 하영·재환 | [C1C3 결과](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6332703908), [B 종료](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6336767294), [실제 원본 수신/내용 검토](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6337348436). B TGZ 내부1496/1496·Apply TGZ6/6 검토, 양 앱 cold-pull imageID·strict TLS·digest 및 관리자 회수 확인 | API cold-pull 수용과 기동/DB는 분리. [D22 FINAL](https://github.com/321Team/fds-project-baseline/issues/42#issuecomment-6337537087) 확정, MSA42와 ROSA52·53 병합. [SA LINK_PASS](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6337348436) 수신·실행 시각 이력 보존. [ev251](https://github.com/321Team/fds-project-evidence/pull/251) MERGED `7942d005a9c6913a64037ed2901d7e8fecc45384`로 공개 증적 편입. Robot·SA/Secret·guard·반환 경로 최종 회수는 미실행이며 B 전체를 #47/#46 인수로 확대하지 않음 |
| IaC live/source 정합 / 하영·권욱 | [tf33](https://github.com/321Team/infra-terraform/pull/33) MERGED `ef74f689df6ebf53e495f6c2b6fd9a715baca05a` | 소스 편입·독립 검토, CI0=NOT_RUN. 이 병합으로 실제 IAM 변경을 다시 수행하지 않음 |
| #46 소비 구현 / 권욱 | PR100~144 기존 편입 기록 재사용. [PR145](https://github.com/321Team/infra-cicd/pull/145) merge `d58e1701019f8cca25a707462efddc109acc06f2`와 [PR146](https://github.com/321Team/infra-cicd/pull/146) merge `dd592c2be236455df75bebc32bcd763ff442fb3d`: 양측 담당 독립 APPROVED·필수2 SUCCESS, 통합 main Linux1164=1160 PASS/4 SKIP. 실제 native context 기반 SITE 조립과 P2 private parser 경로 연결. [PR147](https://github.com/321Team/infra-cicd/pull/147)은 HEAD32226270·재환 exact-HEAD 독립 APPROVED·필수2 SUCCESS/미해결thread0 후 merge `99e10efcbba8667c50d9a90e121bfef5a6b6161b` | 실제 RUN grant·인계 후 새 baseline·본인 메모리 인증/실효 권한·actual helper/READY·finish scope 연결 잔여. 원문 단회 인증/원본-control 전후 검증·producer native gate·post-close finish 코드 재사용. `SITE=None`, Runtime NOT_RUN. 자격 발급/앱 배포 미실행 |
| 앱·공급 / 재환→권욱 | [MSA42](https://github.com/321Team/fds-msa/pull/42) merge69e28c49·Harbor Primary·2앱6객체/strict render 재사용. [기존 공급 원본](https://github.com/321Team/fds-project-evidence/blob/7e6bb13dafad1e5f60887880576364fe02a461de/evidence/P1-CICD-01/push-run-38404449622-20261013/NEXT_DEPLOY_HANDOFF.json) SHA79f4f056…·sourceaffbc69 → 실제TBS38395350748/1 → Push38404449622/1 확인. 제작source와 render69e의 앱2·ci·ci/apko subtree 일치 | producer 원문/native 대응을 더 이상 전체 미수신으로 두지 않음. 후속 code 선택은 아래 참조. 이 원본은 NOT_DEPLOY_AUTHORIZATION·baseline NOT_REFRESHED를 명시하며 실제 grant·새 baseline·현재 scan을 대신하지 않음. [MSA41](https://github.com/321Team/fds-msa/pull/41) 세 번째 이미지 실제 digest/공급 근거 대기는 별개. 기존 두 이미지 재빌드/Push 요구0 |
| ROSA Route·삭제 / 하영 | ROSA50 소스 병합 재사용. [삭제 v8.1 검토](https://github.com/321Team/infra-rosa/issues/8#issuecomment-6360894119): manifest23/23, v8 대비 자기 임시파일 정리 변경·집중 MOCK24 PASS. [재환 독립 검토](https://github.com/321Team/infra-rosa/issues/8#issuecomment-6361699558) 코드 차단 없음 | STATIC/MOCK 수용과 삭제 Runtime GO 분리. 당일 inventory·zone exact-ID·UID·saved Plan/해시·소유 범위 확인, 소비 종료·DB 원복·#12 회수 원본 보존을 선행. SIGKILL 잔존 한계 보존. 최종 정리·복구·반출/보고 10/26 12:00 완료 |
| DB A2/I4·10/22 수동 창 C / 재환·하영 | [원본 수신 검토](https://github.com/321Team/fds-project-baseline/issues/49#issuecomment-6357013764): 하영 TGZ29파일/D manifest10/10, 재환 manifest47/47. 최초 API rollout 실패와 두 차례 restart·2차 성공, C-STOP22:00:55 Pod0 원본 대조. **하영 묶음 ev251, 재환 묶음 [ev252](https://github.com/321Team/fds-project-evidence/pull/252) 편입 완료**. ev252 merge `38c959950b908e2d016b1d4f84040cae1160fe78`, 10/24 17:58 KST. 텍스트58개 byte 일치·폴더 manifest59/59·원본 manifest47/47·CI43시험/구조 검사 재사용. 큰 원본5개는 저장소에 복사한 것이 아니라 비공개 공유 위치·SHA로 참조 | 원본 수신 대기 표시는 해제. **A5 NOT_RUN**, 초기 NotReady·승인/실행 시각 이력은 유지. Pod↔node/pcap 귀속은 해당 원본에 없어 미확인. 수동 D 결과를 #46 도구 Runtime PASS로 바꾸지 않음 |
| 유지·자격·최종 회수 / 각 원 Lead | [유지 RUN 검토](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-6357126663): DB_RUN20261023T1248·NP6·Ready/A4/A5 차단 보고. [Robot 유한 만료 연장 보고](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6356929624)는 기존 승인 내 수용. 주말12시 전후1회 관측·무인앱0 유지 | 실제 적용/연장 보고가 없는 상태로 되돌리지 않음. 담당자 보고와 중앙 원본 대조 범위는 분리. [앱0·DB세션0](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-6361720013)은 아래 시각표 참조. 실제 최종 회수는 미실행. P8은 [지정 Plan 1회 GO](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6357457266) 발행/Apply 미실행. 새 삭제 GO·최종 Cleanup PASS 아님 |
| P1 범위 정리 / 각 원 Lead·권욱 | [PR197](https://github.com/321Team/fds-project-baseline/pull/197) MERGED, [11건 결과](https://github.com/321Team/fds-project-baseline/pull/197#issuecomment-6339659621) 재사용: Decision5 Done/Task6 Cancelled | 선택 기능을 재착수하거나 P0 Gate의 새 필수 구현으로 복원하지 않음. 기존 미구현·재개 Owner/조건·Known Issue 보존 |

증적 private 원본은 고정 공유 `02차 프로젝트`에서 검토하고, 최종 승인 산출물만 `02 프로젝트 결과물`로 넘긴다.
원본 Plan/state/credential은 공개 GitHub에 올리지 않는다. 이 대장은 #54 제출 후보이며 Deliverable Freeze·정본 발행·인수 완료가 아니다.

## 10/24 편입·유지 관측 추가

- [PR201](https://github.com/321Team/fds-project-baseline/pull/201) merge `43dd808df3c1dc2e62ba95aded1cb565d322baff`(17:54 KST): SCC·UID 수신 대기 해제와 #55 정리 검토가 준비 문서에 편입됐다. 기존 검증의 반복이나 정본 발행은 아니다.
- [재환 16:33 유지 관측](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-6381507212): P2 DB세션·새 거래0, 기존 pg_hba/방화벽 지문·경로 유지, VPN 카운터 증분0 보고. 12시 전후 예정 대비 지연 사실을 보존한다. 담당자 보고 수신이며 중앙의 host 조회·새 raw 검증은 미실행이다.
- [ev252 보존 회신](https://github.com/321Team/fds-project-baseline/issues/55#issuecomment-6381489077)의 큰 원본5개(바깥 묶음·db01 묶음·pcap·영상2)는 계속 비공개 보존한다. PR 병합으로 공유 원본 전체 삭제 조건이 충족된 것이 아니다. 10/22 A4 승인/실행 시각 이탈·늦은 녹화·21:13 결과 미확인·A5 NOT_RUN은 유지한다.
- SCC·UID 투영 JSON의 중앙 수신/의미 검토 완료는 그대로 유지한다. ev252의 창 C 편입을 그 JSON의 별도 편입이나 full Pod/6객체 baseline 검증으로 확대하지 않는다.

## 인수 준비의 다음 순서

권욱은 #46 준비 순서·실제 연결 코드→새 결과만 접수→#33/#39/#42 최종 판정 자료 정리와 IF-19/WBS 추적→#49 집계·#54 Freeze 후보→#56 실제 Review 결과/#55 Action 연결→10/26 최종 회수·#57 Sign-off 순으로 처리한다. #34/#36/#52 Done/closed는 재개하지 않는다. 회신 대기를 이유로 독립 구현·문서 작업을 멈추지 않는다.

## 10/23 오후 수신·보고·편입 구분

| 대상 | 생산/보고 | 중앙 원본·내용 검토 | 증적 편입·최종 판정 |
|---|---|---|---|
| ev251 하영 창 B·C 원본 | 하영 공유 TGZ3개(재환 묶음 제외) | 17:35 검토: 수신 해시·내부 manifest1520항목 일치, 내용·공개 민감정보 점검. Haye C 묶음의 내부 manifest 범위는 D 시점10파일로 한정 | 18:37:45 병합. 원본 재압축 불필요. README 출처/미실행/원인 추정 등 비차단6건은 후속 문구 보완이며 AC 전체 인수 아님 |
| 앱 SA Pod SCC·UID JSON | [하영 18:15:32 수집](https://github.com/321Team/fds-project-baseline/issues/38#issuecomment-6361610081)·[반출 보고](https://github.com/321Team/fds-project-baseline/issues/38#issuecomment-6366473628). SHA256 `f0c6fe2444362bc64d55d7dfaa1e0043222b508b0e57d0a96787329acf22628e` | **중앙 10/23 23:53 기록에서 수신·재해시·의미 검토 완료**. 6개 앱 SA Pod의 필드 투영 JSON, Ready/승인 image·imageID/SA/SCC/UID 6/6 대응. 19:1x 반출 대기였던 과거 상태는 해제 | ev251에 이 새 JSON이 편입됐다고 표시하지 않음. full Pod API 객체·전체 AC·후속 현재값 보증이 아님. 동일 원본 재수집 불필요 |
| 무인 앱0 | [하영](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-6361606970): C-STOP18:15:49, Pod0/replicas0 18:15:56, UID불변 | 담당자 보고 대조. 중앙 원본 미수신, 실제 환경 조회 미실행 | 18:00 전환 상한보다 C-STOP15분49초 지연. 기한을 소급 수정하지 않음 |
| P2 DB세션0 | [재환](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-6361694287): 18:19:35 세션0·pg_hba after 동일·새 행0 | 담당자 보고 대조. 중앙 원본 미수신. 17시 관측을18:02에 했다는 지연 사실 보존 | 무인 관측 기준점18:19:35. 앱0 시각과 구분하며 다음 주말12시 전후 관측은 기존 Lead가 담당 |

오늘 유지 RUN A5 차단 보고는 10/22 수동 창 C의 A5 NOT_RUN을 사후 PASS로 바꾸지 않는다. 마찬가지로 Robot TTL 편집 보고 수용과 최종 Robot/Secret 회수 완료는 다른 단계다. 누락 원본은 미수신으로 표시하며, 내용 검토/인수 칸을 추정으로 채우지 않는다.

## 10/25 #46 원본·코드·CI·Runtime 증분

| 구분 | 이번 확인·편입 후보 | 남은 단계 |
|---|---|---|
| 원본 | 기존 ev218 공급 JSON·2개 native run/attempt/jobs/step, 이미지 제작affbc69·배포render69e의 관련 subtree 동일성 대조. 두 공급 digest는 기존 승인값과 일치 | native 성공 step 하나로 내부 Test/Build/Scan 각각의 의미를 새로 만들지 않음. 기존 공급 원문 의미와 함께 검증. 10/13 scan은 해당 시점 결과이지 현재 취약점 보증이 아님 |
| 실제 호스트 준비 | 권욱이 기존 Runner UID1000 HOME 아래 P2 root/inputs/source/state를 mode700으로 준비, 입력600·state empty·claim0 재조회. 고정 source69e bare-shallow 원본·render/contract·private Python3.12.15/PyYAML6.0.3을 확인. [준비 기록](https://github.com/321Team/fds-project-baseline/issues/46#issuecomment-6385867126) | 관측 시점의 파일·환경 준비이며 actual RUN·helper/READY·OAuth 인증 성공·현재 OCP 권한이 아님. 시스템 PyYAML6.0.1 유지. 같은 UID 프로세스 변조 방지/파일 무결성 검사로 interpreter 위치 검사를 확대하지 않음 |
| 코드·CI | PR145/146 병합·통합 Linux1164, PR147 private baseline 연결 Linux1180=1176 PASS/4 SKIP·필수2 SUCCESS·merge99e10efc 검사2 SUCCESS. 기존 공급 원본/native 단계의 후속 선택 구현은 [Draft PR148](https://github.com/321Team/infra-cicd/pull/148) | PR147은 재환의 새 코드 전체·Runner/인증/정리 경로 검토로 저장소 최소1인 기준 충족 후 병합. 실제 원본 의미/Runtime 인수는 별도. 후속 PR148은 exact HEAD4860b298에서 Linux1190=1186 PASS/4 SKIP·필수2 SUCCESS, 새 코드 범위 독립 리뷰 대기. 외부 AI 보조 검토는 사람 독립 승인 아님 |
| Runtime | 실제 SITE·발급·앱 배포 미실행. 원본 생성/권한 변경0. 인계 후 새 6객체 raw와 완료 보고는 확인하지 못함 | 기존10/23 archive·SCC UID 투영 JSON·인계 검토 ZIP을 새 baseline으로 승격하지 않음. 실제 유한 grant/원본 의미·새 baseline·actual 인증/READY·finish scope를 연결해야 함. 미래 RUN/nonce/token/finish hash는 사전 제출 대상 아님 |
| 인수·회수 | SCC·UID 중앙 수신/6행 의미 대조, ev251·252 편입 및 한계 재사용. #55 권욱 P2 자기파일 회수 담당 인계 | 소비 종료 계획10/26 08:30, 최종 정리·복구·반출·보고12:00. 앱/claim/fence·메모리 세션과 증적 보존 뒤 P2 자기파일만 회수. ROSA/RoleBinding 회수 및 나중 Runner 등록 해제/VM 폐기는 별도 |

현재 G4 T6 INCONCLUSIVE·NetworkPolicy 일부 미실행, 창 C A5 NOT_RUN·시각 이탈/귀속 한계는 보존한다.
이 집계는 #54 제출 후보이며 #49→#54→#56→#55→#57의 Status/AC·Freeze·Sign-off를 올리지 않는다.
최신 source/SSH/환경 근거를 재사용하며 기존 확인값을 미확정으로 되돌리거나 같은 파일 재제출을 요구하지 않는다.
