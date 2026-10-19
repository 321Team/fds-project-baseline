# Phase2 Ticket Pack·WBS 상태 델타 후보

2026-10-19 18:42:43 KST · 상단필수속성Status/관리status라벨만실제정합화. #34만설계Lead의기확정Freeze를Done/closed로연결, 다른11건은사전진행/InProgress·open이다. 원AC/Exit체크·Owner·계획일·보관원문·Runtime판정은그대로다.

| 티켓/Record | 상태 | 근거/잔여 |
|---|---|---|
| [#34 P2-ARC-01](https://github.com/321Team/fds-project-baseline/issues/34) | To Do→Done / closed | [상태기록](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-6264223768) · Lead 확정 설계 Freeze/IF17~20·변경통제 채택 완료. 실제 플랫폼/G4/배포·정본발행은 완료 아님. |
| [#35 P2-IAC-01](https://github.com/321Team/fds-project-baseline/issues/35) | To Do→In Progress / open | [상태기록](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6264225353) · 기반 IaC/Stage-A 인계 진행. STAGE_A_READY=NO와 runtime route/SG 잔여 유지. |
| [#36 P2-OCI-01](https://github.com/321Team/fds-project-baseline/issues/36) | To Do→In Progress / open | [상태기록](https://github.com/321Team/fds-project-baseline/issues/36#issuecomment-6264227043) · D21 AWS Relay FINAL 사양을 반영하는 선행 검토 진행. OCI 새 구축/이전 원AC 전체 MET·종결은 선언하지 않음. |
| [#37 P2-VPN-01](https://github.com/321Team/fds-project-baseline/issues/37) | To Do→In Progress / open | [상태기록](https://github.com/321Team/fds-project-baseline/issues/37#issuecomment-6264228990) · VPN 실측/회수 증적과 v1.2 Plan 키트 검토 진행. 새 Plan/Apply·Route ON GO 아님. |
| [#38 P2-ROSA-01](https://github.com/321Team/fds-project-baseline/issues/38) | To Do→In Progress / open | [상태기록](https://github.com/321Team/fds-project-baseline/issues/38#issuecomment-6264230348) · ROSA 생성 이후 첫 설정3회 STOP/자동회수는 실행자 보고. BASIC_READY/보안·인계 완료 아님. |
| [#42 DEC-P2-REG-01](https://github.com/321Team/fds-project-baseline/issues/42) | To Do→In Progress / open | [상태기록](https://github.com/321Team/fds-project-baseline/issues/42#issuecomment-6264231857) · Harbor Primary/ECR 수동 A 방향 확정·D7수용. D22 FINAL=PENDING_RUNTIME 유지. |
| [#43 P2-APP-01](https://github.com/321Team/fds-project-baseline/issues/43) | To Do→In Progress / open | [상태기록](https://github.com/321Team/fds-project-baseline/issues/43#issuecomment-6264233431) · 앱 전달 계약/승인 host 소스 병합. 실제 Registry/clean render/배포·RouteTLS/Health 미완료. |
| [#46 P2-CICD-01](https://github.com/321Team/fds-project-baseline/issues/46) | To Do→In Progress / open | [상태기록](https://github.com/321Team/fds-project-baseline/issues/46#issuecomment-6264234866) · 운영 provider/CLI 구현·독립리뷰/CI/병합과 원본 연결 준비 진행. 실제site/인증원본5종/정상·실패차단 Runtime 잔여. |
| [#47 P2-HYB-01](https://github.com/321Team/fds-project-baseline/issues/47) | To Do→In Progress / open | [상태기록](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-6264236520) · IF18/IF19·A2 창 단위 원복/Secret 분담 계약과 Hybrid 실행 준비 진행. DB/Harbor Runtime/P1예외·통합PASS 아님. |
| [#49 P2-DOC-01](https://github.com/321Team/fds-project-baseline/issues/49) | To Do→In Progress / open | [상태기록](https://github.com/321Team/fds-project-baseline/issues/49#issuecomment-6264238133) · 인수·산출물 준비와 이번 PR191 사양 후보 편입 착수. 최종 Deliverable Freeze/발행 아님. |
| [#52 DEC-CAL-P2-01](https://github.com/321Team/fds-project-baseline/issues/52) | To Do→In Progress / open | [상태기록](https://github.com/321Team/fds-project-baseline/issues/52#issuecomment-6264239681) · Review 시간·참석자 운영안 사전 준비. 10/23 14:00~15:30은 제안/권욱 참석 미정, 확정·초대 발송 아님. |
| [#55 P2-REV-01](https://github.com/321Team/fds-project-baseline/issues/55) | To Do→In Progress / open | [상태기록](https://github.com/321Team/fds-project-baseline/issues/55#issuecomment-6264241276) · 인수표/증적/Review·자원 정리 인계 준비 착수. 실제Review/Sign-off/Project Close 미실행. |

기존 P1 XLSX는7건부분후보로유지한다. P2 상태의최종WBS/TicketPack/Description 전체세트편입은 status-delta.json을입력으로재생성·대조한다. 그전까지기존78행집계는현재프로젝트완료율이아니다. 보류/미실행/Gate티켓은이12건밖의상태를자동승격하지않는다. GitHub ProjectsV2는read:project권한없어별도필드조회/동기화미확인.
