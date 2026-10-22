# D24 / #52·#55·#56 Review 운영계획

이권욱 / CODEX_ASSISTED, 2026-10-20 KST. 기존 10/23 Review·Freeze / 10/26 Close 날짜를 유지한다.
**회의 시간은 10/23(금) 18:00~19:30 KST, 90분으로 통합한다.** 권욱의 18시 이후 가능 회신과
[하영 참석 가능](https://github.com/321Team/fds-project-baseline/issues/52#issuecomment-6291486067),
[재환 종료까지 참석 가능](https://github.com/321Team/fds-project-baseline/issues/52#issuecomment-6291989324)을 근거로 한다.
과거 14:00~15:30 제안·참석 미정은 당시 이력이며 이번 단일 시간안으로 대체한다.

| 역할 | 참석·책임 |
|---|---|
| 이권욱 / Lead·PMO/QA | 진행, Decision/Gate·미결·최종 인수/Close 판단. 18시 이후 가능 |
| 이하영 / 기존 담당 Lead | ROSA/IaC/Network·Harbor·자원/정리·증적의 자기 영역 인계. 18:00~19:30 가능 |
| 이재환 / 기존 담당 Lead | VPN/DB/App·공급·원복/원본의 자기 영역 인계. 종료까지 가능 |

[기존 Review Authority](../../../governance/REVIEW_AUTHORITY_POLICY.md)를 유지한다. 각 담당 영역의 Lead 판단과 PMO Gate/Close 판단을 구분하며,
Support 전원 재서명이나 새로운 만장일치 승인을 추가하지 않는다. AI 보조 검토를 참석자 승인으로 표시하지 않는다.

| KST | 의제·기존 책임 | 기록할 결과 |
|---|---|---|
| 18:00~18:10 | 권욱: #49→#54 동일 후보·manifest·실제 Freeze 판정 | 후보 버전/원본, 미충족·실제 승인 범위 |
| 18:10~18:30 | 하영·재환: G4/G5/G6·정상/거부/복구 | 실행 환경/RUN, PASS/PARTIAL/INCONCLUSIVE/NOT_RUN 구분 |
| 18:30~18:45 | 재환·권욱: 기록 기반 Hybrid Demo·source/digest 추적 | 실제 기록 재생과 현장 Live 구분 |
| 18:45~19:00 | 권욱: Decision/Known Issue/Deferred·P0 잔여 | 수용/보류·근거·Owner/완료조건 |
| 19:00~19:15 | 하영·권욱: 자원·비용·보존/정리 | 최신 리포트 시각, 실제 잔존·후속 조치 |
| 19:15~19:30 | 권욱: #55 Action readback·10/26 Close 입력 | 담당·Due/미정·완료 증거·수용 책임 |

기본은 **검증된 기록 기반 시연**이다. Review만을 위해 VPN을 재개하거나 새 관리자 권한을 만들지 않는다.
기존 운영 최소 권한으로 조회하는 선택지는 해당 유효 승인/범위가 있는 경우만 사용하며 이 계획 자체가 Runtime GO가 아니다.
ROSA 삭제는 Review 이후 별도 실제 삭제 판단으로 연결한다. 회의 개최·자료 누락 수용을 G4/G5/G6 또는 #54/#56 자동 PASS로 바꾸지 않는다.
권한·Secret·VPN의 기존 만료/원복은 회의일까지 자동 연장하지 않는다. DB 원복을 미결 자료 보완 때문에 지연시키지 않는다.

[schedule-sync.tsv](schedule-sync.tsv)는 기존 WBS Record ID에 대한 운영 delta이며 발행 xlsx/Tag를 덮어쓰지 않는다.
[ICS](review-20261023.ics)는 같은 시간의 Calendar 가져오기용 회의 계획이다. 파일 생성/게시와 실제 Calendar 등록·초대 발송은 구분한다.
#52의 WBS/Calendar 동기화 완료는 후보 편입과 실제 사용 기록을 확인한 단계까지만 체크한다. 현시점 티켓 In Progress 유지, 완료일·AC를 합성하지 않는다.

10/23 #49 집계→#54 Freeze→#56 Review→#55 Action, 주말 자동 배정 없음, 10/26 잔여/Sign-off→#57 Close 순서를 유지한다.
선행 Gate가 미완료이면 해당 상태와 후속을 회의에서 다루며 인수 완료로 올리지 않는다.


## 10/22 운영 WBS/Calendar 반영·종결요건 정정

[현행 운영 WBS/Calendar](../20261022/FDS_Phase2_Review_Operating_WBS_20261022.xlsx)에 승인된 10/23 18:00~19:30·세 Record 연결과 10/26 Close/비근무를 반영했다. 기존 ICS의 UID/일정은 재사용한다.
원 증적은 **Review Invite 또는 회의 계획**이므로 실제 초대 발송·새 정본 재발행을 #52의 별도 필수조건으로 추가하지 않는다. 위 미실행 기록은 사실 이력으로 보존하며, 그 미실행 자체가 원 요건 밖의 종결 차단이라는 안내는 이 정정으로 대체한다. 외부 계정 행사 생성·초대는 하지 않았다.
[D24 운영 반영/후속 분리](../20261022/owner-closeout.md)를 기준으로 하며 #55/#56 실제 Review·#57 Close는 여전히 별도다.
