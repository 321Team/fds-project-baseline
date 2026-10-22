# Phase 2 P1 ToDo 범위 정리·종결 판단 후보

기준: 2026-10-22 KST. 사용자 이권욱의 “Phase2 Priority P1~ / ToDo(open)를 담당 확인·범위 분석 후 닫을 수 있도록 PR 작성, 본인 보류 이슈는 일정 리스크로 잔여를 남기고 Close” 지시. 이전의 보류/open 유지 결정은 역사로 보존하며 이번 변경 범위만 새 판단으로 기록한다.

## 조회 범위와 판정 원칙

- 19개 저장소의 실제 이슈153건(PR 제외)을 재조회하고 현행 Phase2/기존 이월 범위74건을 대조했다. 현행 상단17속성표의 `Phase=Phase 2`, `Priority=P1 이상 숫자`, `Status=To Do`, 실제 `state=open`을 선정 기준으로 사용했다. P0보다 낮은 우선순위라는 뜻으로 숫자1이상을 선택하며 현재 결과는 P1 **11건**, 라벨/속성 충돌0이다.
- 이권욱 Lead 3건은 이번 직접 지시로 미도입/범위 제외를 확정한다. 이하영7건·이재환1건은 현재 담당 확인 후 종결 판단한다. 과거 보류·미착수 회신을 새 Close 동의로 바꾸거나 무응답을 동의로 처리하지 않는다.
- Decision의 미도입/유예 선택 완료는 `Done / closed / completed`, 미구현 Task를 이번 범위에서 제외하는 종결은 `Cancelled / closed / not_planned`로 구분한다. [현행 상태 매핑](../../../governance/TICKET_SYNC_POLICY.md#3-상태와-종결)을 따르며 기능 구현/Runtime PASS를 뜻하지 않는다. 보드에 Cancelled 옵션이 없으면 기존 정책에 따라 Done으로 보이더라도 원 Issue 사유와 구현 미완료는 보존한다.
- 원 AC·기술 위험·기존 인계·Record ID·담당·Priority·계획일·과거 정본/Release를 보존한다. 결정/제외에 실제 해당하는 체크만 반영할 수 있고 도입 시에만 해당하는 조건을 시험 PASS로 체크하지 않는다.
- P0 #35/#37/#38/#42/#43/#45/#46/#47/#49/#55·G4/G5/G6·Project Close 잔여는 이 PR의 종결 대상이 아니다. P1 미도입이 P0 필수 보안/관측/보호/복구/실행·정리 AC를 면제하지 않는다.

## 대상별 판단

| 티켓 | Record ID | Lead | 이번 판단/후보 | 권한 상태 | 종결 시 표현 |
|---|---|---|---|---|---|
| [#25](https://github.com/321Team/fds-project-baseline/issues/25) | P1-MON-02 | 이재환 | 고도화 미구현 잔여로 제외 검토 | 담당 확인 대기 | Cancelled / not_planned |
| [#26](https://github.com/321Team/fds-project-baseline/issues/26) | P1-DR-02 | 이하영 | 격리 Backup/Restore 미수행 잔여로 제외 검토 | 담당 확인 대기 | Cancelled / not_planned |
| [#27](https://github.com/321Team/fds-project-baseline/issues/27) | P1-HA-02 | 이하영 | 추가 HA/장애 검증 미수행 잔여로 제외 검토 | 담당 확인 대기 | Cancelled / not_planned |
| [#40](https://github.com/321Team/fds-project-baseline/issues/40) | DEC-P2-DNS-01 | 이권욱 | 이번 프로젝트 추가 Hybrid DNS 미도입 결정 확정 | 사용자 확정 | Done / completed |
| [#41](https://github.com/321Team/fds-project-baseline/issues/41) | DEC-P2-OP-01 | 이하영 | 추가 Operator Mirror 미도입/유예 결정 후보 | 담당 확인 대기 | Done / completed |
| [#44](https://github.com/321Team/fds-project-baseline/issues/44) | P2-OADP-01 | 이하영 | OADP/S3 도입 미수행 잔여로 제외 검토 | 담당 확인 대기 | Cancelled / not_planned |
| [#48](https://github.com/321Team/fds-project-baseline/issues/48) | P2-DNS-01 | 이권욱 | 이번 프로젝트 추가 Hybrid DNS 구현 범위 제외 확정 | 사용자 확정 | Cancelled / not_planned |
| [#51](https://github.com/321Team/fds-project-baseline/issues/51) | P2-OP-01 | 이하영 | 조건부 Operator Mirror 구현 미수행 잔여로 제외 검토 | 담당 확인 대기 | Cancelled / not_planned |
| [#95](https://github.com/321Team/fds-project-baseline/issues/95) | DEC-P2-RHOAI-01 | 이하영 | 이번 프로젝트 RHOAI 미도입/유예 결정 후보 | 담당 확인 대기 | Done / completed |
| [#120](https://github.com/321Team/fds-project-baseline/issues/120) | DEC-P2-GITOPS-01 | 이권욱 | 이번 프로젝트 추가 GitOps/Argo CD 미도입 결정 확정 | 사용자 확정 | Done / completed |
| [#121](https://github.com/321Team/fds-project-baseline/issues/121) | DEC-P2-COMP-01 | 이하영 | 이번 프로젝트 Compliance Operator 미도입/유예 결정 후보 | 담당 확인 대기 | Done / completed |

현재 실제 적용·담당 요청 링크는 [적용 기록](p1-scope-closeout-state.json), 기술 미완료·위험·재개 조건은 [잔여 대장](p1-remaining-register.md)을 함께 본다. 표의 후보를 실제 종결로 읽지 않는다.

## 권욱 담당 확정 범위

1. **#40 D23:** 이번 프로젝트에서는 추가 Hybrid DNS를 도입하지 않는다. DB/Harbor의 기존 IP endpoint와 ROSA public API/Route의 기존 DNS·엄격 TLS 계약을 유지한다. 새 Resolver·조건부 전달·hosted zone·hosts override·53포트 허용을 자동 부여하지 않는다. 이 선택이 기존 DNS 가용성/접속 Runtime PASS를 새로 선언한 것은 아니다.
2. **#48 조건부 구현:** #40 미도입 선택에 따라 추가 Hybrid DNS 구현은 이번 범위에서 제외하고 `not_planned`로 정리한다. 원 Query/거부/fallback 검증은 실행 완료로 바꾸지 않는다. 취소 표기는 이번 구현 범위의 제외라는 관리 상태이며 기술 검토 이력·향후 도입 가능성은 잔여로 남긴다.
3. **#120 GitOps:** Argo CD 추가 도입은 이번 프로젝트 범위 밖 잔여로 확정하고 Decision을 종결한다. #46 기존 Runner direct Delivery Contract와 생산/소비 경계는 그대로다. 이 결정은 #46 실제 운영 구성·배포·권한 인수 완료를 의미하지 않는다.

미도입 사유는 남은 일정과 P0 통합·현장 연결·증적 인수/회수 작업의 위험이다. 과거 비용 추정이나 임시 상한을 현재의 도입 차단으로 재사용하지 않는다. 비용은 교육장 리포트 기반 이권욱 중앙 판단이며 새 상세 재견적·중복 비용 GO를 요구하지 않는다.

## 타 담당 확인과 종결 순서

기존 보류/인계 자료를 재작성하지 않는다. 각 Issue 댓글/이 PR에서 **① 이번 범위 제외 또는 Decision 종결 판정 ② 기존 보고 이후 실제 변경·잔존 자원 유무 ③ P0 필수 영향과 남는 위험**만 현재 delta로 확인한다. 구현을 유지해야 한다면 필요한 최소 범위/담당과 현실적 여유를 제시하며 새로운 무조건 마감을 만들지 않는다.

- 재환: #25의 관측 고도화 미구현 잔여와 기존 P0 관측 경로 영향 확인.
- 하영: #26/#27의 이미 수신된 이월 위험을 재사용하고, #41의 실제 공급 경로 선택과 #51 조건부 Mirror 구현 제외를 결합 판단. #44/#95/#121의 미도입/유예 및 이후 변경·잔존 자원을 확인.
- 권욱: 담당 회신의 범위·P0 영향·잔여 수용을 통합한다. 실제 생성물이 있으면 기존 소유/안전 정리·원본 인계가 확인될 때까지 해당 종결을 보류한다. Issue Close가 자원 삭제/권한 회수 GO는 아니다.
- 조건 충족 시 원본 직전 재조회→판정 댓글→현재 Status/Schedule Note·해당 체크 최소 치환→관리 라벨·state/state_reason→사후 비대상 필드/본문 대조 순으로 반영한다. 타인의 회신 전 자동 Close하지 않는다.

## 후속·완료의 한계

이 자료는 검토용 운영 변경 후보이며 정본 Tag/Release/원 WBS·Ticket Pack 재발행이 아니다. 원본 증적 저장소 편입의 독립 리뷰 의무도 유지한다. P1을 다시 수행하려면 원 Issue를 재개하거나 별도 승인 범위로 연결하고 현행 source/version·실제 입력·권한·정상/실패·원복·정리·증적 요건과 가용을 확인한다. 재검토일은 미배정이며 Project Close 뒤 자동 실행하지 않는다.

STATIC/REVIEW·담당 확인·실제 Issue Close·MERGE/PUBLICATION·RUNTIME은 별도로 기록한다. 실제 서버/클러스터/Runner/DB 접속·token 발급·IAM/Apply/Deploy/삭제0이며 공개 원본 Plan/state/credential은 포함하지 않는다. AI 사용: CODEX_ASSISTED; 외부 AI의 기술 의견은 사람의 확인·승인으로 대체하지 않는다.
