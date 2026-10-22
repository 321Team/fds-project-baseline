# Phase 2 자원 유지·최종 정리 기한 변경 — 10/26 월요일 12:00 KST

상태: 사용자 결정 반영 / 운영 변경 기록. AI 사용: CODEX_ASSISTED.

이권욱은 2026-10-22에 프로젝트 자원(클라우드 포함)을 월요일 오전까지 유지하도록 지시했고, **최종 정리·복구·원본 반출·보고 완료를 2026-10-26(월) 12:00 KST**로 직접 확인했다. 이것은 자원 보관 기한 결정이며, 새 자원 생성·증설·배포·DB 개방·IAM/RBAC 변경·삭제 Apply의 포괄 승인이 아니다. PR 편입과 실제 Runtime·최종 인수·정본 발행을 구분한다.

최신 운영 결정: [#37 유지 기한 변경](https://github.com/321Team/fds-project-baseline/issues/37#issuecomment-6338609757). [티켓 반영 감사](../../../audit/phase2-retention-20261022/ticket-update-record.json). [#47 요청 심층 검토·기한 반영](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-6338617976).

## 1. 근거와 변경 범위

- 이전 [#37 유지 결정6333766969](https://github.com/321Team/fds-project-baseline/issues/37#issuecomment-6333766969)은 최종 정리10/23 16:30, 그날15:00까지 소비 중지·DB 원복으로 정했다. [창 C 카드 v1.1](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-6315050301)의245분에 장애 인수60분을 더하고, Harbor 회수·Review 전 인계를 역산한 일정이다. 서비스 자체의 자동 TTL 또는 기술적으로 고정된 만료시각이 아니다.
- [10/23 Review 확정6331048901](https://github.com/321Team/fds-project-baseline/issues/52#issuecomment-6331048901)의18:00~19:30은 유지한다. 자원 최종 정리를 Review 전 필수조건으로 묶었던 연결만 해제한다. #55의10/23~26 실행기간·10/26 Close 계획도 그대로이며, 12:00은 자원 정리 입력의 마감이지 Sign-off 자동 완료시각이 아니다.
- [하영 전체 C 요청6338085219](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-6338085219)은 이미 [통합 사전 범위 GO6338326769](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-6338326769)로 검토·수용했다. 미확정 SITE와 현재 발급/전달·C-STOP 권한은 여전히 실제 착수 조건이다. 새 내용 없는 같은 코드/시험은 반복하지 않는다.
- 현재 조회한 main의 `SITE=None`으로 실제 G는 HOLD이다. P8은 정확3delete saved Plan 게시·확인 후 그 Plan1회 Apply를 유지한다. 과거 댓글·카드의10/23 15:00·16:30 문구는 원문 이력으로 보존하고, 이번 새 결정 링크로 **자원 유지·최종 정리 기한만** 대체한다. S/자격 등의 별도 기한은 아래2절대로 구분한다.

| 대상 | 이번에 바꾸는 유지·정리 기준 | 유지하는 제한 |
|---|---|---|
| 현 ROSA HCP/Worker 및 그 종속 AWS 자원 | 현재 승인된 구성·수량을10/26 오전까지 보관, 최종 정리/검증/반출/보고12:00 완료 목표로 재배치 | 실제 삭제 당일 inventory·소유/의존성·UID/exact-ID·새 saved Plan·해당 Apply GO. ROSA 삭제 키트가 제외한 network/vpn/rosa-prereq 등 root를 함께 삭제하지 않음 |
| 같은 B VPN_RUN `20261022T1500`의 Relay/vpn-gw01 구성, 승인 route1·DB5432 SG1·Harbor443 SG1, 자기 MSS2줄 | 최종 P8/V9를10/23 16:30에서10/26 12:00으로 연기. 승인된 동일 자원/규칙만 연속 유지, 창 사이에 내렸다 재Apply하지 않음 | CIDR·목적지·포트·guard/NP·실제 소유권 유지, 새 RUN/같은 RUN 재적용/이미 지운 probe 재생성 없음. 조기 중단·복구 조건 유지 |
| Harbor C2/C3 자기 guard P2줄·반환 경로, 앱 SA pull 참조/정상 pull Secret의 비밀 아닌 연결 구성 | 기존 최종 소비·회수 계약의 외곽 기한을10/26 12:00으로 정합화. 같은 실제 RUN/own-ACK·UID를 보존 | Secret 값·Robot 토큰·관리자 권한 수명은 별개. 마지막 소비 뒤 자기 추가분만 회수; 다른 worker/push/기존 참조/공용 규칙 보존 |
| db01·harbor01·vpn-gw01 등 기존 On-Prem 서버/공용 기반 서비스 | 필요한 프로젝트 기반을 보존 | 프로젝트 보관 종료를 서버/공용 DB/기존 Registry/Shared OCP 전체 삭제·종료 명령으로 해석하지 않음 |

자원 ID는 기존 승인 Plan·Apply readback·owner RUN에서 소비한다. 위 표는 새 전수 inventory나 실제 현재 상태 실측이 아니며 미확정 ID를 합성하지 않는다. 이미 정리된 자원을 유지 명목으로 다시 만들지 않는다. 새 Worker/ELB/NAT/IP·용량 증설은 포함하지 않는다.

## 2. 자원 유지와 예외·자격 수명은 다름

- **DB runtime 예외는 각 승인 C 회차 안에서만** 사용한다. A2-ON 끝→A2-OFF 시작90분, DB 실제 개방→원복 완료 기존120분 상한을 연장하지 않는다. W0의 SYN `listening`·rollback 준비 없이 열지 않는다. 각 시험 후 자기 앱 소비 중지·Pod0·P2 출발지 DB 세션0 확인과 같은 DB_RUN 원복을 수행한다. C-STOP 확인 불명으로 DB 원복 상한을 넘기지 않는다. pg_hba·DB 허용을 주말 내내 열어 두는 승인이 아니다.
- **S DB Secret v3.1의 현재 생성/receipt-UID 회수 범위와10/23 16:30 외곽 회수 상한은 유지**한다. 실제 최종 소비 종료가 더 이르면 그때 정리한다. Secret 생성·유효기간을 자동 연장하지 않는다. 이후 별도 승인 소비가 필요하면 바뀌는 Secret 수명/생성 부분만 연결하며 같은 검토를 처음부터 반복하지 않는다.
- Harbor Robot의 실제 자연 만료 **10/23 약13:2x**는 변경하지 않았다. 10/26까지 보관한다고 인증이 유효해지는 것이 아니다. 만료 후 새 pull/재시작은 성공한다고 가정하지 않는다. 필요하면 기존 pull-only/namespace·UID·비공개 전달 계약 안의 정확한 교체·회수안을 연결한다. 이번 기록에는 새 Robot 발급/수명 연장·Secret 값 교체가 없다.
- Robot 교체·재발급이나 Secret 값 교체는 이번 보관 결정에 포함된 실행 GO가 아니다. 만료는 인증 수명이며 기존 실행 승인의 유무·소비 종료 여부와도 다르다. 실제 마지막 소비가 일찍 끝나면 소유권이 확인된 연결 구성·자격은 먼저 회수할 수 있다.
- 900초 배포 토큰·MFA 세션·임시 cluster-admin/SCC 등의 실행 권한은 기존 수명을 따른다. 검증 전용 최소권한 유지 결정과 세션/토큰 만료를 구분한다. 이미 회수한 cluster-admin을 유지 명목으로 다시 부여하지 않는다.
- 목적지/출발지 제한·SELinux·TLS 검증·SSM 최소권한은 그대로다. 다음 작업 인수 때 실제 구성·카운터/소유권·관리 접근을 확인하며, 상시 tcpdump·새24시간 감시·매일 teardown/reApply를 추가하지 않는다. 소실/드리프트 발견 시 승인된 복구 범위만 처리하고 예상 밖 변경은 STOP/인수한다.

## 3. C 회차 종료와 프로젝트 자원 최종 종료의 분리

1. **이번 C 실행:** SITE 채택·팀원 가용/비중첩·실제 T0 기록 뒤 기존1회 통합 GO를 소비한다. 단계별 재승인은 반복하지 않는다.245분은 실행·원복·정리/보고를 안전하게 배정한 회차 예산이지 월요일까지 계속 DB를 열거나 활동하는 시간이 아니다. 이번 유지 결정이 오늘1회 GO를 여러 날/여러 회차의 실행 GO로 늘리지 않는다. 오늘 미착수로 유효 실행일이 지나면 그1회 GO가 주말 유지로 되살아나지 않는다.
2. **회차 종료:** C-STOP·A2-OFF·당일 결과 원본/보고는 늦추지 않는다. P8/V9·최종 Harbor 회수가 연기된 항목은 `승인된 유지 / 최종 정리 미실행 / 담당·RUN·기한`으로 인계한다. 전체 Cleanup PASS·C 전체 완료로 표현하지 않는다. 이미 성공한 자기 소비 중지·DB 원복을 월요일에 재개/재시험할 필요는 없다.
3. **마지막 승인 소비 종료 후 회수:** SA own-ACK revert→정상 pull Secret UID 조건 삭제→P2 Robot·자기 guard/반환 경로 회수를 기존 계약에 연결한다. S는 위 별도 기한을 먼저 지킨다. 소비 중인 자격을 먼저 지우거나 다른 UID/공용 규칙을 지우지 않는다. **이 회수의 readback/원본 보존을 마친 뒤 v8 namespace 삭제로 넘어간다.** namespace를 먼저 없앤 뒤 사라진 SA/Secret을 실제 revert한 것처럼 보고하지 않는다.
4. **P8/V9:** 정확3delete 새 saved Plan을 실제 게시·권욱 확인한 뒤 바로 그 Plan1회 Apply/readback. V9는 같은 VPN_RUN과 자기 MSS2줄까지 회수/absent를 확인한다. 오래된 Plan·다른 state/대상·소유 불명 자원을 시간만 맞추려 강제 삭제하지 않는다.
5. **ROSA·AWS 최종 정리:** 수용된 삭제 키트 v8의 inventory→exact-ID/UID 승인→namespace receipt→unprotect saved Plan/Apply→destroy saved Plan/Apply→ID별 부재 판정 순서를 따른다. v8 정적 수용·MOCK284/284의 기존 검증을 재사용하며, 아직 생산되지 않은 Plan·삭제 권한·Runtime GO를 완료로 표시하지 않는다. 각 다른 root는 그 root의 검토된 Plan/소유·의존성 기준으로 정리한다. 증적·Terraform state/lock과 교육장 공용 기반은 삭제 대상과 구분해 보존한다.
6. **마감 인수:** 실제 삭제/미삭제·잔존 자원·후행 청구·원복·원본 반출/재해시 결과를 모아10/26 12:00에 보고한다. 실패/불명은 잔여·Owner/복구 상태 그대로 인계하며, 정리 실패를 시간 때문에 PASS나 강제 삭제로 바꾸지 않는다.

최종 정리 대상에는 **P2 전용 소유가 확인된** network/vpn/rosa-prereq 및 operator/OIDC 종속 자원도 포함한다. ROSA 키트의 OUT_OF_SCOPE는 보존 결정이 아니라 **그 키트의 삭제 범위 밖**이라는 뜻이므로, 각 root의 정확한 Plan/기존 삭제 절차와 하영의 owner 인계로 처리한다. 공용 Terraform backend/state·lock·증적·공용 SSM 문서·교육장/기존 서비스는 기존 보존 범위를 유지한다. 소유 미확정 또는 삭제 실패한 P2 자원은 임의로 KEEP/PASS로 재분류하지 않고 잔여로 보고한다. 담당자 부재/복구 미완료도 미실행·잔여로 남겨 이권욱이 인수한다.

12:00는 사용자 확인한 최종 완료 목표다. **모든 자원을12:00까지 켠 뒤 그때부터 삭제하라는 뜻은 아니다.** 마지막 소비 종료와 삭제·복구·검증·보고 시간을 역산해 앞서 정리한다. 월요일 가용/삭제 시작시각은 아직 확정하지 않았다. 창 C의245분을 ROSA/전체 AWS teardown까지 끝나는 예산으로 재사용하지 않는다. P8/V9·보고에는 기존40+20+30분, Harbor 회수에는45+15분 여유가 있고, ROSA destroy 키트는 별도로120분 credential 여유를 요구한다. 이120분은 실제 삭제 완료시간 보장이 아니다. 단계 의존성·실제 소요/가능한 병행과 장애 여유를 담당자가 한 카드에 연결한 뒤 실제 삭제창을 확정한다. 월요일09:00~12:00이면 충분하다고 미리 판정하지 않는다.

## 4. 담당·티켓 연결과 비용

| 담당 | 연결할 최소 완료조건 | 티켓 |
|---|---|---|
| 이권욱 | 자원 유지 결정·C SITE/권한 채택·P8 정확 Plan 검토·STOP/인수·최종 비용/Close 집계 | baseline#46/#47/#49/#55 |
| 이하영 | ROSA/Worker·종속 AWS 및 IaC root 인계/삭제창, S·Harbor/SA/Secret 정리, P8 saved Plan 게시·그 Plan1회 Apply/readback·반출, UID별 원본 | baseline#35/#38, infra-rosa#8/#12 |
| 이재환 | 같은 VPN_RUN/자기 MSS·DB 원복·소비 종료·V9·기존 Runner 원본 인계 | baseline#37/#47 |

[비용 중간 기록6329645656](https://github.com/321Team/fds-project-baseline/issues/38#issuecomment-6329645656) 및 지정 `[클라우드] 비용 통제 정보 입력` 세션의10/22 사용자 자료를 재사용한다. 실제 누적은 **$127.15 / ₩172,378**이며 월요일09:00 예상 약$300/관리범위$290~315는 당시의 **추정**이다. 현재 구성·수량이 같다는 전제에서 유지에 비용 여유가 있다는 판단이다. 새로운 실시간 Billing 조회·12:00 exact 견적·새 비용 상한/종료 기준을 만들지 않고, 교육장 리포트에 따른 비용 판단은 이권욱이 중앙 관리한다. 구축 담당자에게 상세 재견적/중복 비용 GO를 요구하지 않는다.

#52 Review 일정·#49 집계/Freeze는 이번 변경으로 완료/연기되지 않는다.10/23 Review에는 그 시점의 실제 검증·미실행/유지 자원·미수집 한계를 제시하고10/26 실제 정리 결과는 #49/#55/#57 후속에 연결한다. 주말은 기존 비근무 계획이며 자원 보관 허용이 당사자 주말 근무·STOP 상시 대기를 확정하지 않는다.

운영 기록만 변경했다. STATIC=문서/근거 대조, MOCK=새 시험 불필요·기존 수용 결과 재사용, CI=해당 PR 결과를 별도 조회, RUNTIME=미실행. Status/AC/담당·실제 완료일과 발행 정본/Tag/Assets는 변경하지 않는다.
