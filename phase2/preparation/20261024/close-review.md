# #55 최종 정리 검토·미확정 결정 — 2026-10-24

기준: 2026-10-24 13:15 KST 조회. 이권욱 / CODEX_ASSISTED.
[하영 삭제 목록](https://github.com/321Team/fds-project-baseline/issues/55#issuecomment-6379305046),
[담당별 확인 요청](https://github.com/321Team/fds-project-baseline/issues/55#issuecomment-6379606167),
[기존 인계표](../20261020/cleanup-handoff.md)를 대조했다.

**목록은 준비 자료로 수용 가능하다. 기존 10/26 12:00 완료 기한을 유지하되,
계정 해지·공용 자원 보존 결정 변경·교육장 VM 전체 폐기·저장소 공개를 승인한 문서는 아니다.**
이번 PR은 문서·수신 기록 정합화다. 실행 명령이나 자동화가 읽는 설정을 추가하지 않는다.

## 1. 유지할 기준과 새 판단

| 구분 | 현재 기준 | 다음 처리 |
|---|---|---|
| 기존 A1~A5 회수 | 원래 승인 대상·RUN·조건을 재사용. P8은 지정 saved Plan 1회 GO이며 무조건적 재실행 허용이 아님 | 당일 소비 종료·state/ID 불변과 남은 유효 조건 확인, 실제 원복·부재 readback 접수 |
| A6~A7 ROSA 삭제 | v8.1 STATIC/MOCK 검토 수용. 10/26 09:00~12:00은 담당자 제안이며 삭제 Runtime GO는 별도 | 당일 inventory·namespace UID·zone exact-ID·saved Plan/해시 및 실행/복구 가용을 연결 |
| B1~B3 기반 정리 | 기존 범위의 정확한 root·소유자·다른 소비 종료·승인된 Plan에 한정 | 아래 소유권 정정 후 검토. 목록의 순번은 실행 순서가 아님 |
| B4~B7 공용 IAM/backend/SSM·계정 해지 | 기존 기본 보존 결정이 유효. 전체 삭제는 신규 제안 | 권욱이 계정 소유·유형·의존성과 복구/보존 근거를 검토한 뒤 범위·시점을 결정 |
| C1~C2 OCM·개인 token/pull secret | 클러스터 전용 연결과 개인/조직 공용 자격을 구분 | 하영이 실제 소비자를 확인. 다른 클러스터/업무의 자격을 일괄 폐기하지 않음 |
| D1~D7 전체 On-Prem·GitHub 등록 | 프로젝트 임시 변경 원복과 VM/DB/백업 전체 폐기는 서로 다름 | 재환/하영의 담당 범위 회신과 교육장 소유·반납 기준 확인. D4·D7 중앙 조정은 권욱의 준비 업무 |
| Public 전환 | 19개 중 Public2/Private17을 GitHub 조회로 확인. 공개 적합성 전수 검사는 미실시 | 기존 비공개 기록은 보존하고 정제한 공개용 snapshot을 별도 만드는 안을 우선 권고. 아직 공개 결정·생성·전환 없음 |

12:00는 정리 시작이 아닌 기존 자원 정리·복구·반출·보고 완료 기준이다.
09:00~12:00 제안에 계정 해지·모든 VM 폐기까지 넣을 근거는 없다.
담당자의 월요일 가용과 실제 단계별 소요·복구 여유는 아직 이 검토에서 확정하지 않았다.
소비를 계속하거나 다른 작업이 필요하면 기존 마감을 묵시적으로 연장하지 않는다.
비용 재견적·작업별 새 비용 상한은 추가하지 않는다.

## 2. 실제 소스에서 확인한 정정

### B2 Relay 역할·프로파일은 별도 CloudFormation 소유

infra-terraform `366e176805b885d20d34a76ed9fa02f0d6eb7a03`의
[vpn/main.tf](https://github.com/321Team/infra-terraform/blob/366e176805b885d20d34a76ed9fa02f0d6eb7a03/terraform/vpn/main.tf)는
`FDS-Relay-SSM`을 data source로만 참조한다.
[stage-a/bootstrap-references.tf](https://github.com/321Team/infra-terraform/blob/366e176805b885d20d34a76ed9fa02f0d6eb7a03/terraform/stage-a/bootstrap-references.tf)는
소유자를 `CloudFormation:FDS-Central-Bootstrap-v1`로 명시한다.
따라서 VPN destroy가 역할까지 삭제한다고 쓰지 않는다. Relay/SSM 소비 종료 뒤 원 소유 경로로 별도 판정한다.
Network는 이를 사용하는 Relay/ROSA 등 종료 후 정리한다.

### B5 SSM·state·관리 권한은 끝까지 필요한 수단

[session-document.tf](https://github.com/321Team/infra-terraform/blob/366e176805b885d20d34a76ed9fa02f0d6eb7a03/terraform/vpn/session-document.tf)는
`create_session_document=false` 기본값과 `prevent_destroy=true`를 갖는다.
현재 state 편입·실제 Owner/리전·다른 소비자는 이 검토에서 미조회다.
이름만으로 AWS 소유 또는 프로젝트 전용이라고 단정하지 않으며, “계정 해지 예정”만으로 보호를 제거하지 않는다.

모든 해당 root의 정리·잔존 판정, 최종 state/로그의 비공개 보존과 수신,
남은 작업/lock 없음 및 읽기·복호화 가능성을 확인하기 전 backend·관리 접근·복호화 수단을 없애지 않는다.
버전이 있는 S3라면 현행 객체만 지워서는 삭제/부재 증명이 되지 않으므로 버전·delete marker와 실제 보존 정책을 처리안에 포함한다.
이 문서는 버킷 삭제나 KMS 변경을 승인하지 않는다. 데이터 사본에 state·자격이 포함될 수 있으므로 공개하지 않는다.

### #8 임시 RoleBinding 회수는 namespace 삭제와 순서 정합화

[10/26 제안](https://github.com/321Team/infra-rosa/issues/8#issuecomment-6378716458)의
5번 namespace/클러스터 삭제 뒤 6번에 namespace RoleBinding을 다시 지우는 순서는 그대로 실행할 수 없다.
권욱 마지막 소비 후, namespace 삭제 전에
`gwonuk-p2-admin-temp` 두 개를 회수·readback하고 기존 삭제 실행자의 필요한 권한은 유지하는 안을 권고한다.
namespace 종속 삭제로 함께 사라진 경우에는 그 실제 경로와 namespace 부재를 기록하며 별도 DELETE 성공으로 만들지 않는다.
annotation은 자동 만료가 아니다. API 소멸/연결 실패를 `can-i=no`나 회수 성공으로 판정하지 않는다.

### D5~D6 inventory 범위

infra-ansible `7f04e18371f5d10aec678460f5dcd6e28d98d7d3`의
[hosts.yml](https://github.com/321Team/infra-ansible/blob/7f04e18371f5d10aec678460f5dcd6e28d98d7d3/inventory/hosts.yml)에
control3·worker3·edge01·egress-proxy01이 있고,
[hbr.yml](https://github.com/321Team/infra-ansible/blob/7f04e18371f5d10aec678460f5dcd6e28d98d7d3/inventory/hbr.yml)의 harbor01과
[lb-stageb.yml](https://github.com/321Team/infra-ansible/blob/7f04e18371f5d10aec678460f5dcd6e28d98d7d3/inventory/lb-stageb.yml)의 k8s-api-lb01도 확인했다.
이 10개 호스트의 코드상 존재를 실제 VM 생존/삭제 권한 확인으로 확대하지 않는다.
ansible01·cicd-runner01·DB·VPN·DNS·PKI·monitoring의 전체 목록 및 VM/물리 호스트 매핑은 담당 회신과 기존 자산대장으로 보완한다.

D7은 Runner 등록과 해당 머신의 서비스/작업 경로를 구분한다.
#46 시험·증적 반출·필요 CI가 끝나기 전에 Runner·배포키·공용 자격을 먼저 회수하지 않는다.
repo/org/environment Secret·deploy key·webhook·GitHub App·PAT은 서로 다른 자원이며 실제 소유/사용처를 확인한 대상만 정리한다.
개인 Claude/Grok/Antigravity 계정은 프로젝트 인프라 삭제 범위가 아니다.

## 3. 계정 해지·Public 검토 의견

권장안: **기존 프로젝트 자원 정리 → 잔존/비용·보존 인수 → 계정 해지 별도 결정**.
AWS 계정 유형·소유/교육장 책임과 결제·Support/Marketplace·조직 연결 확인 전 날짜를 확정하지 않는다.
[AWS 계정 해지 안내](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-closing.html)에 따르면
해지는 즉시 전 자원의 영구 삭제가 아니며 통상 90일의 post-closure 기간이 있다.
청구/구독 의무가 남을 수 있고, MFA·root 연락 수단을 함께 폐기해서는 안 된다.
AWS가 계정 해지 전 모든 자원의 수동 삭제를 필수로 요구하는 것은 아니다.
우리의 exact-ID 부재·복구·증적 요구는 프로젝트의 정리 인수 기준과 구분한다.
“90일간 root 로그인만으로 재개”라는 표현은 피하고 AWS 재개 절차를 따른다.

Public 권고안은 **기존 Private17개 유지 + 허용한 파일만 새 공개 snapshot**이다.
현재 전환을 승인한 것은 아니다. 이미 Public인 두 저장소도 기존 공개 상태가 안전성 인증은 아니다.
기존 저장소 전환은 전체 history/branch/tag 및 Issue·PR·첨부·Release·Wiki·Actions 로그/산출물 등 공개되는 표면을 검토해야 한다.
Package는 종류별 별도 공개 설정이 있으므로 repo 전환과 자동으로 같다고 가정하지 않는다.
[GitHub visibility 안내](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)는
Actions history/log 공개와 공개 후 fork 가능성을 명시한다.

현재 파일의 패턴 적중 수를 확정 유출 건수나 전체 검사 통과로 사용하지 않는다.
공개 후보에 대해 secret 검사와 적중 분류, 개인정보 동의/가림, 제3자 자료·라이선스 확인,
원본/공개본 대응 해시를 남긴다. 실제 비밀값은 가림만 하지 않고 유효 자격 회수/교체 여부도 확인한다.
[GitHub sensitive-data 안내](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)에 따라
history 정리도 외부 clone·fork·참조의 사본 회수를 보장하지 않는다.
새 snapshot도 내용 검사 없이는 안전하지 않다. 공개를 위해 기존 증적 이력과 해시를 일괄 다시 쓰지 않는다.

## 4. 권욱 후속 작업과 인계

| 다음 순서 | 권욱이 지금 진행한/진행할 준비 | 회신·실행이 필요한 부분 |
|---|---|---|
| 1 #55 목록 정합화 | 승인 범위·소유권·기한·실행 순서를 위와 같이 검토 | 하영·재환의 실제 삭제/복구 창, D4~D6 전체 소유 목록. 신규 계정해지/전체폐기 결정 |
| 2 #49 원본 집계 | 6-2 SCC·UID 수신·검토 완료를 접수 대장에 반영 | 증적 저장소 편입·Full 인수는 별도. 재환 창 C 증적 PR 최신 제출 근거 |
| 3 #46 운영 연결 | [PR132](https://github.com/321Team/infra-cicd/pull/132) HEAD `12717ede9c1452eed1325f59ad547eb0aab38ff2`: 하영 영역 APPROVED, 검사2 SUCCESS, Draft/재환 영역 대기 | 실제 배치값·본인 인증/발급/서버회수·원본/control/finish 결속 및 replicas 인계 후 fresh baseline |
| 4 D7·공개 준비 | 19개 저장소의 가시성·보관상태 대조, 범위별 정리/공개 판정표 준비 | 실제 Runner/Secret/키/Hook 소유 목록과 마지막 소비. Public 방식에 대한 사용자 결정 |
| 5 #57 인수 | 실제 완료/미실행·Known Issue·Owner/Due·잔존 책임을 모아 Sign-off 후보로 연결 | #54/#56 실제 결과와 최종 정리 readback. 문서 준비로 AC/Close를 완료하지 않음 |

#46의 고정 선택은 ansible01/server01_ansible → 기존 Runner, 개인 actor gwonuk,
native job checkout의 helper, 종료 후 object/rollout 관측이다.
선택된 값은 현재 host 인증·설치·권한 검증 결과가 아니다.
실제 workspace/Python/SSH port·alias/현재 UID·netns·READY/store와 승인 원본/control은 미확정으로 남긴다.
현재 `SITE=None`, dispatch false, `RUNTIME=NOT_RUN`. 관리자 역할 부여 보고가 연결 완료나 시험 GO를 대신하지 않는다.
#46 finish 관측 완료도 DB·Robot·VPN·클라우드 정리 완료가 아니다.

## 검토 범위

GitHub 원문·고정 소스·기존 중앙 수신 기록 및 AWS/GitHub 공식 문서를 대조했다.
Claude Code·Grok CLI·Antigravity CLI에는 비공개 원문 없이 각각 종료 의존성·공개 위험·표현 구조의
일반 설계 자문을 병행 요청했다. 요청 강도 high, 실제 응답 모델은 각 수신 기록에 보존한다.
자문에서 backend 삭제까지 기존 승인으로 분류한 내용은 원 승인과 달라 기각했다.
Grok의 “모든 Package가 함께 공개” 주장은 일반화하지 않았다.
새 Runtime·권한 변경·계정 해지·공개 전환·정본 발행·티켓 종결은 수행하지 않았다.
