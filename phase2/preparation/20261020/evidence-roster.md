# #49 증적·산출물 접수 대장

기준: 2026-10-23 KST. 10/22 야간까지의 최신 원본 검토·병합·변경 결정을 반영했다. 기존 [하영 회신](https://github.com/321Team/fds-project-baseline/issues/49#issuecomment-6291485599), [재환 회신](https://github.com/321Team/fds-project-baseline/issues/49#issuecomment-6291988326)과 접수 자료를 재사용하며 변경분만 갱신한다.
생산·공유·수신/재해시·내용 검토·증적 편입·AC 인수를 각각 구분한다. 원본 전체 재제출이나 동일 시험 반복은 요구하지 않는다.

| 대상·생산 책임 | 현재 확인 범위 | 편입·인수 상태 / 다음 완료조건 |
|---|---|---|
| D21 / 권욱 | [#36 사용자 한계 수용·최종 인수/종결](https://github.com/321Team/fds-project-baseline/issues/36#issuecomment-6330828733), ev161 기존 독립 편입 재사용 | Done/closed. 미수집 원본·명령/RC/version은 수용된 한계이며 전체 tunnel/G4/후속 AC PASS가 아님 |
| D24 Review 일정 / 권욱 | [운영 WBS/Calendar](../20261022/FDS_Phase2_Review_Operating_WBS_20261022.xlsx)와 기존 PR194 계획/ICS 사용 | 10/23 18:00~19:30·세 Record 동일 시간. 초대 또는 회의계획 요건을 적용하며 실제 회의/Freeze/Close는 별도 |
| D-11d 원본 / 권욱·재환, 편입 하영 | 권욱 공유·재해시·내용 검토, 교차 독립 검토 연결 완료 | [ev249](https://github.com/321Team/fds-project-evidence/pull/249) MERGED `04464931ae70fc4d78fb2601d6cc2c384487b317`. 18파일 편입이며 전체 ROSA AC 완료와 구분 |
| Stage-B VPN / 재환 | 10/15 기존 수용·원본 편입 재사용 | [ev239](https://github.com/321Team/fds-project-evidence/pull/239) 기존 병합. 현재 창 A/B/C 전체 PASS로 확대하지 않음 |
| 창 A / 재환·하영 | T1/T3 PASS, T3-R 성공, T6 INCONCLUSIVE 유지. DB W4·P9/P8·양쪽 V9 원복·정리의 기존 원본/한계 재사용 | [ev250](https://github.com/321Team/fds-project-evidence/pull/250) MERGED `eadec9f53cb9f1e13877f2e9a02779ef785aa366`. 38변경 blob·manifest35/35·공개 archive 내부22+1파일 대조. SPI 포함2원본은 비공개, 공개 정제본은 치환6곳 외 동일. T6·수집/절차 한계를 보존했으며 전체 AC PASS로 확대하지 않음 |
| G4 후속 / 하영·재환→권욱 | #7 B/A·N3, C7 일부 미실행. [#39 입력](https://github.com/321Team/fds-project-baseline/issues/39#issuecomment-6288503072) | 기존 원 AC의 잔여와 처분 근거 필요. T6를 PASS로 변경하거나 보류만으로 G4 완료 처리하지 않음 |
| PG-03 / 하영 | 6-1 관측 수용, 6-2 NOT_RUN, PG-03 HOLD 및 기존 GO 이탈 이력 보존 | [rosa51](https://github.com/321Team/infra-rosa/pull/51) MERGED `70e5dc8cc52e44919c2390feb71d1631111a6e1b`. 수집기 코드 수정이며 새 실행/AC PASS 아님 |
| Harbor C1C3·창 B / 하영·재환 | [C1C3 결과](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6332703908), [B 종료](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6336767294), [실제 원본 수신/내용 검토](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6337348436). B TGZ 내부1496/1496·Apply TGZ6/6 검토, 양 앱 cold-pull imageID·strict TLS·digest 및 관리자 회수 확인 | API cold-pull 수용과 기동/DB는 분리. [D22 FINAL](https://github.com/321Team/fds-project-baseline/issues/42#issuecomment-6337537087) 확정, MSA42와 ROSA52·53 병합. [SA LINK_PASS](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6337348436) 수신·실행 시각 이력 보존. Robot·SA/Secret·guard·반환 경로 최종 회수는 미실행이며 B 전체를 #47/#46 인수로 확대하지 않음 |
| IaC live/source 정합 / 하영·권욱 | [tf33](https://github.com/321Team/infra-terraform/pull/33) MERGED `ef74f689df6ebf53e495f6c2b6fd9a715baca05a` | 소스 편입·독립 검토, CI0=NOT_RUN. 이 병합으로 실제 IAM 변경을 다시 수행하지 않음 |
| #46 소비 구현 / 권욱 | PR100~112 MERGED. [PR113](https://github.com/321Team/infra-cicd/pull/113)은 실제 고정 입력·부모 연결과 자격 수신 후 계획 완성 경로의 검토 후보. [원본10/10 수신·기존 발급 인가 검토](https://github.com/321Team/fds-project-baseline/issues/46#issuecomment-6339413996)는 재사용 | 독립 리뷰·실제 Runner/job/peer·자격 채널·원본/control/finish 채택, 수동 C 기존6객체 기준선 연결은 별도 잔여. `SITE=None`·도구 Runtime0. 하영 입력을 다시 미수신/권한 없음으로 되돌리거나 수동 C를 도구 AC로 바꾸지 않음 |
| 앱·공급 / 재환 | current2개·TBS/Push 원본 재사용. [MSA42](https://github.com/321Team/fds-msa/pull/42) MERGED `69e28c494a120c388afe18d901043d05333d7c7c`, Harbor Primary·2앱/6객체의 strict clean render/contract/source 수신 | [MSA41](https://github.com/321Team/fds-msa/pull/41)은 실제 end-page 이미지 digest·생산 근거 대기로 Draft. D22 재선택·같은 두 이미지 재빌드/Push를 요구하지 않음. 9객체 지원 코드를 실제 세 번째 이미지 인수로 확대하지 않음 |
| ROSA Route·삭제 / 하영 | [ROSA50](https://github.com/321Team/infra-rosa/pull/50) 시험 Route 소스 병합. 삭제 키트는 v8로 진전, [zone3 exact-ID 초안](https://github.com/321Team/infra-rosa/issues/8#issuecomment-6337296113)·[Namespace 실행 세션안](https://github.com/321Team/infra-rosa/issues/8#issuecomment-6337436035) 검토 완료: v8 manifest23/23·override2/2 일치, 생성 원본과 zone3 exact-ID/전체 CallerReference 일치, 정상·변조 입력 오프라인 판정 확인 | Route 실제 시험·전체 삭제는 미실행. 10/23 삭제로 자동 진행하지 않고 유지/최종 정리10/26 12:00과 소비 종료·Harbor 회수를 연결. 검토한 파일과 최종 inventory/saved Plan 실행 승인은 구분 |
| DB A2/I4·창 C / 재환·하영 | [C-STOP](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-6341388160)·[재환 종료 보고](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-6341600008): 앱0·P2세션0·A2-OFF22:02:57/W0일치, A4 B1/B2 DB23행·녹화11행 대조 보고 | 보고 내부 산술/순서 검토와 원본 독립 검증을 구분. raw/Pod↔node 대조 미수신, A5 미실행, A4 승인 전·녹화 착수 지연 이력 보존. 수동 D·S 재생성/재시작 이력을 #46 도구 실행이나 소급 승인으로 바꾸지 않음 |
| 유지·자격·최종 회수 / 각 원 Lead | [PR198](https://github.com/321Team/fds-project-baseline/pull/198) MERGED `5c7756fe73ea9ea5a52fa17a8aeb84756715899b`; [10/22 22:46 변경 결정](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-6342339344)으로10/23 새 DB_RUN·동일 Robot 유한 만료/DB Secret 회수 상한을10/26 12:00까지 통합 승인 | NP4+앱 NP2·새 연결 실측과 미사용 앱0·변경 비중첩/원복 가드 조건. 이후 실제 연장/새 RUN 결과는 미수신. 매 사용 DB 재개방/원복·중앙 재GO는 반복하지 않음. 승인 유지와 최종 Cleanup PASS는 구분 |
| P1 범위 정리 / 각 원 Lead·권욱 | [PR197](https://github.com/321Team/fds-project-baseline/pull/197) MERGED, [11건 결과](https://github.com/321Team/fds-project-baseline/pull/197#issuecomment-6339659621) 재사용: Decision5 Done/Task6 Cancelled | 선택 기능을 재착수하거나 P0 Gate의 새 필수 구현으로 복원하지 않음. 기존 미구현·재개 Owner/조건·Known Issue 보존 |

증적 private 원본은 고정 공유 `02차 프로젝트`에서 검토하고, 최종 승인 산출물만 `02 프로젝트 결과물`로 넘긴다.
원본 Plan/state/credential은 공개 GitHub에 올리지 않는다. 이 대장은 #54 제출 후보이며 Deliverable Freeze·정본 발행·인수 완료가 아니다.

## 인수 준비의 다음 순서

권욱은 #46 준비 순서·실제 연결 코드→새 결과만 접수→#33/#39/#42 최종 판정 자료 정리와 IF-19/WBS 추적→#49 집계·#54 Freeze 후보→10/23 18:00~19:30 Review/#55 Action→10/26 최종 회수·#57 Sign-off 순으로 처리한다. #34/#36/#52 Done/closed는 재개하지 않는다. 회신 대기를 이유로 독립 구현·문서 작업을 멈추지 않는다.
