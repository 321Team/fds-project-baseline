# 이권욱 Phase 1 현황·착수 대장 — 2026-10-07

CODEX_ASSISTED. 14:15 KST 기준 저장소 조회 결과와 작업 준비 기록이다. Runtime 실행·AC 인수·위험 수용·일정 변경·정본 발행·티켓 종결 기록이 아니다.

## 현재 판정과 조회 범위

- org:321Team / assignee:GWONUK 검색: 전체 58건, OPEN 29 / CLOSED 29, incomplete_results=false. OPEN 중 Phase 1 직접 배정 13건, 나머지 16건은 Phase 2·프로젝트 종료 범위다.
- Phase 1 OPEN 13건은 실행/후속 업무 9건과 milestone 4건이다. 상위/하위 및 milestone이 중복되므로 이 건수로 구현 진척률을 계산하지 않는다.
- 발행 정본 [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21), 발행 커밋 979facb98de8ca1f1e2ce22f38b27ac3366f3fc3. 실제 Release API published_at=2026-10-04T05:49:12Z.
- baseline main c34ca9c12d7cb38d610829cc59460ec6a8d87b1a, infra-ansible main 61a77ad2f984cbf9e74a95f779691e2831a5a2a6, infra-cicd main 1320e17e9d7dd66455e65276267dc2b92517c4b5, infra-kubernetes main c3057906a6a8427a4b315b7e544e063efe0fecf2.
- [기존 10/5 대장](../gwonuk-work-queue-20261005/README.md)의 CI/CD 후순위와 종결 업무의 의존 순서를 유지한다. 선행 작업이 현장/타 Lead 입력으로 막힌 동안 독립적인 공급 소비 준비를 진행한다.
- GitHub 원본 assignee/state/labels, 담당 티켓 본문·전체 댓글, 관련 PR·review·CI·원본 log를 조회했다. GitHub Projects 비공개 Status 필드와 현장 SSH/전체 서버 상태는 이번 조회에서 확인하지 않았다.

## 권장 착수 순서와 완료조건

| 순서 | 이권욱 배정 대상 | 현재 상태·핵심 잔여 | 이번 착수 / 다음 완료조건 |
|---|---|---|---|
| 1 | [baseline #14](https://github.com/321Team/fds-project-baseline/issues/14) | In Progress, OID-02 전체 HOLD·OID-03 미해결 | preloaded 동일 digest 보충안의 준비 인계 작성. kube-controllers 5노드·CoreDNS Worker3노드의 입력·출처·복구·증적 연결 구체안 수신 후 심사 |
| 2 | [infra-ansible #62](https://github.com/321Team/infra-ansible/issues/62) → HBR #13 | OPEN, 소스 병합과 AC04 인수 구분. Docker persistence 조건부 1회 GO; Robot·임시 .50/.102 제거 HOLD | 기존 GO의 비중첩·fresh prestate·중단/복구/positive-negative·counter 기준을 인수 입력으로 연결. HBR Lead 이하영의 실제 실행 결과와 정리 기록 수신 |
| 3 | [infra-ansible #9](https://github.com/321Team/infra-ansible/issues/9) | OPEN, worker02 키 복원 읽기 사전검증 source ef5adb77 준비 branch, actual 수집/쓰기복원/wrapper Runtime/엔진 전환 미완료 | 기존 코드/14 MOCK 재작성·재시험 생략. PR66 필수 CI 해소 후 준비 branch의 main 정합·독립 리뷰·worker02 읽기 수집 순서. baseline ANS 종결을 다시 열거나 자동 Close blocker로 확대하지 않음 |
| 4 | [evidence #4](https://github.com/321Team/fds-project-evidence/issues/4) | OPEN, FUP09 수용·PR25 병합 완료. FUP04/05/06/07 원본·승인·열람 metadata 잔여 | 과거 출처 수신 항목을 DOC 인계표에 고정. 신규 시험·합성 자료로 과거 원본 대체 금지 |
| 5 | [baseline #18](https://github.com/321Team/fds-project-baseline/issues/18) | To Do, G1 필수 결과 판단 미완료 | 종결 LB/DNS/ANS 및 현재 K8S/HBR/ICR의 충족·잔여를 별도 대조, Gate 판단은 실제 AC/예외로 수행 |
| 6 | [baseline #24](https://github.com/321Team/fds-project-baseline/issues/24) | In Progress, Freeze/Publication 미완료 | 최신 source→시험→증적→수용/잔여 인계표 작성. As-built·Runbook·Known Issue의 Owner/Due·source 재현성 완료 후 Freeze 판단 |
| 7 | [baseline #29](https://github.com/321Team/fds-project-baseline/issues/29) | To Do, G3 Review Ready 미확정 | G1/DOC 및 각 Lead의 P0 인수·수신/승인된 예외 확인 |
| 8 | [baseline #30](https://github.com/321Team/fds-project-baseline/issues/30), [#31](https://github.com/321Team/fds-project-baseline/issues/31) | #30 In Progress / #31 To Do, Review·Demo·잔여 처분 미완료 | OID·MTU·SEC·HBR 등 Close 입력을 수용/미수용/제안으로 분리. 날짜 도래만으로 승인/이월/수신 책임을 확정하지 않음 |
| 9 | [baseline #32](https://github.com/321Team/fds-project-baseline/issues/32) | To Do, Phase1 Close 미완료 | 실제 Sign-off·필수 AC 또는 명시적 승인 예외·이월 수신 조건이 완결된 뒤 종결 판단 |
| 후순위 | [baseline #16](https://github.com/321Team/fds-project-baseline/issues/16), [infra-cicd #11](https://github.com/321Team/infra-cicd/issues/11) | OPEN, 생산자 공급 GREEN·소비 pin 9658255 유지·Delivery 미인수 | 새 source0494ca/공급 artifact11460655012의 소비 준비 기록 작성. exact source/test scope 확인→manifest/identity→config 독립 리뷰→현장 staging/Test/Build/Scan→별도 Push/native/Deploy Gate |
| 후순위 | [infra-ansible #61](https://github.com/321Team/infra-ansible/issues/61) | OPEN, PR66 exact0b0f99 독립 APPROVED, 필수 Linux CI QUEUED | run37462768493/job112266199324 재조회. queued1/in_progress0이지만 matching Runner·현장 세션은 미확인. 기존 v1.3 fresh preflight/세션 공급·CI/cleanup 인수 필요 |

## 새로 확인된 상태 변화

- APP 공급: [MSA PR21](https://github.com/321Team/fds-msa/pull/21) merged, main 0494ca279882d4e0cab24fb5a25a136a2e8f46c1. 리뷰 eea60c70과 Git tree 9a5f1a91c3428a4321ccc90ebf3999284f5b9f7b 동일. actual main source37569632325 / supply37569632028 SUCCESS. 생산자 준비가 해소됐으며 Runner staging·새 Harbor digest·Delivery AC는 별도다.
- PR66의 독립 리뷰는 이미 APPROVED5428521797이다. 승인 0건·새 독립 리뷰 대기라는 과거 표현을 현재 병합 차단으로 쓰지 않는다. 필수 CI QUEUED가 남았다. Runner id0만으로 서버 장애를 확정하지 않는다.
- [SEC #19](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-6031098692)는 AC05 1회 PASS 보고와 evidence#134 제출·exact43ad5a25 독립 APPROVED가 있다. 본 세션은 그 원본 archive를 재해시하지 않았으며 AC05 인수·Known Issue 해소를 선언하지 않는다.
- [MON #17](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-6030071485)의 대표 Source 정책 결속 1줄은 Lead가 수용 조건으로 체크했다. edge6행 INCONCLUSIVE·IF06B8443 귀속 등의 잔여는 해소되지 않았다.
- OID02 Owner 이하영은 [8개 조합·완료조건 및 10/8 12:00 실행안 초안 제출](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-6031201210)을 기록했다. 이는 원 Due10/7의 변경 승인·위험수용·APPROVED DEFERRED가 아니다.
- [MTU 종료 보고](https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-6031350840)를 14:15 최종 재조회에서 확인했다. 이하영 보고상 14:04:17 생성·14:06:45 종료, UID 결속 삭제/NotFound·tcpdump 잔존0·사후6/6 Ready/etcd 정상이다. 원본은 아직 서버 보관·수집/독립 증적 리뷰 전이며 본 세션이 archive를 검증한 결과는 아니다. SYN MSS1410·호스트 TCP payload8998 관측을 wire MTU 증거로 쓰지 않으며 VXLAN1450·DF/PMTU NOT_VERIFIED 유지. [APP14:40~15:40 조건부 GO](https://github.com/321Team/fds-project-baseline/issues/15#issuecomment-6030134751)의 실제 착수는 미확인이다.
- LB #9, DNS #12, LNX #66, NET #67, ANS #65와 설계/Decision 종결은 재사용한다. 새 결함/변경 근거 없는 재개·반복시험은 수행하지 않는다.

## 문서·Review 인계 공백

| 입력 | 현재 확인 | 필요한 다음 입력 / 기존 책임 |
|---|---|---|
| OID02/03 | partial REVIEW / 전체 HOLD, preloaded 공급8조합 잔여 | 이하영: 구체 source/index/child/layers·반입·복구안; 이권욱: #14/#30 심사 및 실행/처분 구분 |
| HBR AC04 | 승인 소스·원본 입력, restart 시험1회 조건부 GO | 이하영 실행·복구·positive/negative/persistence; 이권욱 지원/해당 소비 결과 대조. Robot·.50/.102는 기존 별도 HOLD |
| FUP04 | SOURCE GAP | 기존 최초 로그·Windows/VMware/관리VM gateway 원본 또는 정확한 보관 위치 |
| FUP05 | APPROVAL REFERENCE GAP | 당시 Reviewer/Approver·시각·대상·범위가 있는 기존 회신 |
| FUP06/07 | TRACEABILITY METADATA GAP | 개인별 회신/승인 시각·WBS 바이너리 실제 열람 확인. 정본 편입·한계 수용은 재승인 요구하지 않음 |
| MTU | 이하영의14:04~14:06 시험 종료/정리 보고 수신. VXLAN1450·DF/PMTU 미검증 | 서버 원본 수집·증적 PR와 이재환 독립 검토. #37 터널 MTU 수신은 다른 범위. Risk Accepted/유예/AC 확대는 미결정 |
| SEC AC05 | 원본 PR134·독립 리뷰, AC 판정 별도 | 해당 Lead/Review Owner의 원본/필수 조건·판정. AI 자체 검수를 새 독립 승인으로 계상하지 않음 |
| CI/CD | Producer GREEN / Consumer·Runtime 미완료 | 아래 소비 준비 기록과 기존 native preflight 패킷 재사용. 과거 scan을 새/이전 이미지에 전용하지 않음 |

## 수행·한계

이번 작업은 [Draft PR149](https://github.com/321Team/fds-project-baseline/pull/149)와 [infra-cicd Draft PR63](https://github.com/321Team/infra-cicd/pull/63)으로 준비 기록을 제출하고 #14/#30/#16·infra-cicd#11·infra-ansible#61에 실제 착수 댓글을 등록했다. 기존 source/증적의 무관한 MOCK·해시 검사를 반복하지 않는다. 현장 SSH·Runner 공급·token 발급·서버 변경·새 Runtime·AC/Status/Owner/Due 변경·위험수용·병합·정본 발행·종결은 미실행이다.

운영 명령은 기존 승인 source/런북과 해당 실행자의 fresh Gate를 사용한다. 비밀정보를 출력하거나 known_hosts/TLS/SELinux/방화벽 통제를 완화하지 않는다. 신규 코드는 이번 범위에 추가하지 않았다.
