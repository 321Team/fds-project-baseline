# #49 증적·산출물 접수 대장

기준: 2026-10-24 18:21 KST. PR201·ev252·#46 PR135 병합과 #55 담당자 회신·유지 RUN 관측을 추가했다. 다른 행의 관측 시점·한계는 유지한다. 수집 보고 시각과 중앙의 원본 수신 시각은 구분한다. 기존 [하영 회신](https://github.com/321Team/fds-project-baseline/issues/49#issuecomment-6291485599), [재환 회신](https://github.com/321Team/fds-project-baseline/issues/49#issuecomment-6291988326)과 접수 자료를 재사용하며 변경분만 갱신한다.
생산·공유·수신/재해시·내용 검토·증적 편입·AC 인수를 각각 구분한다. 원본 전체 재제출이나 동일 시험 반복은 요구하지 않는다.

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
| #46 소비 구현 / 권욱 | 기존 PR100~134 편입 기록 유지. [PR135](https://github.com/321Team/infra-cicd/pull/135) HEAD `40355f49c370d2bde2003ac9dd72f69d8e5d65a1`의 READY 뒤 메모리 로그인·단회 발급·회수 연결을 하영/재환 각 담당 범위 APPROVED·검사2 SUCCESS 후 병합. merge `f65ae9c35ef23a91f106e6903277553f3aed1b55`, 10/24 18:13 KST. 해당 HEAD Linux1057=1053 PASS/4 SKIP, Windows1057=888 PASS/169 SKIP. 코드·CI 결과만 편입 | 운영 선택 채택과 실제 배치/인증은 분리. 실제 workspace/Python/SSH/UID·netns/READY/store·원본/control/finish 연결 잔여. replicas 인계 후 fresh baseline 필요. 사후 TokenRequest 원문을 사전 platform 원본으로 자동 대입하지 않음. `SITE=None`, Runtime NOT_RUN. [현재 준비·종료 연결](../20261024/close-review.md) 참조 |
| 앱·공급 / 재환 | current2개·TBS/Push 원본 재사용. [MSA42](https://github.com/321Team/fds-msa/pull/42) MERGED `69e28c494a120c388afe18d901043d05333d7c7c`, Harbor Primary·2앱/6객체의 strict clean render/contract/source 수신 | [MSA41](https://github.com/321Team/fds-msa/pull/41)은 실제 end-page 이미지 digest·생산 근거 대기로 Draft. D22 재선택·같은 두 이미지 재빌드/Push를 요구하지 않음. 9객체 지원 코드를 실제 세 번째 이미지 인수로 확대하지 않음 |
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
