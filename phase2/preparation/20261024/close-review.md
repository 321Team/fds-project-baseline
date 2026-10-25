# #55 최종 정리 검토·미확정 결정 — 2026-10-24

기준: 2026-10-25 13:03 KST 조회. 기존 담당자 회신·PR201/202·ev252를 재사용하고 #46 PR145~147 병합·PR148 검토와 P2 실제 환경 준비·회수 담당을 반영했다. 이권욱 / CODEX_ASSISTED.
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
| 1 #55 목록 정합화 | 하영·재환이 기존 회수와 VM/공용 자원 전체폐기 분리 및 권한 회수 순서에 동의 | 정확한 당일 시작·복구 가용, egress-proxy 인계 동의와 PKI 볼륨 실위치/폐기 기준만 미확인. 신규 계정해지/전체폐기 결정 별도 |
| 2 #49 원본 집계 | SCC·UID 수신과 창 C ev252 편입 완료를 접수 대장에 반영 | 큰 원본5개·DB DR백업 보존. 미실행/절차 한계와 Full 인수는 별도 |
| 3 #46 운영 연결 | PR145·146까지 MERGED·통합 검사2 SUCCESS, source/store/private parser 실제 준비·재조회. PR147 MERGED99e10efc·재환 독립 APPROVED·검사2 SUCCESS. 기존 공급/native 대응은 [Draft PR148](https://github.com/321Team/infra-cicd/pull/148) | 실제 RUN grant·인계 후 새 baseline·본인 메모리 인증/실효 권한·actual helper/READY·finish scope. 확인한 과거 SSH/경로/UID를 재제출 대상으로 되돌리지 않음 |
| 4 D7·공개 준비 | 19개 저장소의 가시성·보관상태 대조, 범위별 정리/공개 판정표 준비 | 실제 Runner/Secret/키/Hook 소유 목록과 마지막 소비. Public 방식에 대한 사용자 결정 |
| 5 #57 인수 | 실제 완료/미실행·Known Issue·Owner/Due·잔존 책임을 모아 Sign-off 후보로 연결 | #54/#56 실제 결과와 최종 정리 readback. 문서 준비로 AC/Close를 완료하지 않음 |

#46의 고정 선택은 ansible01/server01_ansible → 기존 Runner, 개인 actor gwonuk,
native job checkout의 helper, 종료 후 object/rollout 관측이다.
선택된 값은 현재 host 인증·설치·권한 검증 결과가 아니다.
10/24~25 읽기 원본의 SSH port/alias·계정/UID/netns와 P2 source/store·private Python 경로를 재사용한다. 이 관측이 미래 native job의 실제 workspace/helper/READY나 본인 인증·실효 권한을 보증하지 않는다. control 구성은 채택됐지만 실제 RUN grant와 역할 원문의 최종 결속은 남는다.
현재 `SITE=None`, dispatch false, `RUNTIME=NOT_RUN`. 관리자 역할 부여 보고가 연결 완료나 시험 GO를 대신하지 않는다.
#46 finish 관측 완료도 DB·Robot·VPN·클라우드 정리 완료가 아니다.
PR132 이후의 helper/종료 관측 보강은 기존 병합 이력으로 추적한다. PR135의 비차단 로그인 입력·수동 OAuth 회수 안내는 다음 코드/문서 변경으로 연결하며 Runtime 선행 승인으로 확대하지 않는다.
관리 SSH JSON helper의 `/usr/bin/python3`과 consumer의 준비된 private Python3.12/PyYAML6.0.3을 구분한다. 같은 UID의 다른 job이 변경하지 않는 기존 비중첩 조건을 유지하며 interpreter 위치 검사만으로 파일 무결성을 주장하지 않는다.

## 10/24 담당자 회신 반영·회수 순서

[하영 6379995948](https://github.com/321Team/fds-project-baseline/issues/55#issuecomment-6379995948), [재환 6380250868](https://github.com/321Team/fds-project-baseline/issues/55#issuecomment-6380250868) 및 [큰 원본 보존 정정](https://github.com/321Team/fds-project-baseline/issues/55#issuecomment-6381489077)을 수신했다. 같은 확인 요청을 반복하지 않는다.

| 순서·의존성 | 실행 책임 | 완료조건 / 현재 상태 |
|---|---|---|
| 최종 앱 소비·DB 소비 중지 | 권욱·재환·하영 각 소비 범위 | 앱0·P2 DB세션0와 마지막 소비 인계. 유지 RUN 10/24 16:33 관측은 신규 세션/거래0 보고이며 월요일 최종 조회를 대신하지 않음 |
| DB·Registry 예외/자격 회수 | DB 재환, Registry·SA/Secret 하영 | 같은 DB_RUN `20261023T1248` A2-OFF 및 자기 추가분 원복. SA 자기 참조→Secret/Robot·Harbor guard/반환 경로의 기존 절차·readback. 현재 최종 회수 NOT_RUN |
| P8→V9·MSS 정리 | P8 하영, vpn-gw01/V9 재환 및 Relay 기존 담당 | 기존 P8 saved Plan 3 delete·state/ID 불변 등 유효 조건 확인 후 처리, 같은 VPN_RUN `20261022T1500` V9와 MSS2 제거. 새로운 Apply/재실행 허용을 만들지 않음 |
| #46 마지막 소비·본인 OAuth 인수→RoleBinding2 회수→namespace 삭제 | 권욱 인계, 하영 회수/삭제 | `gwonuk-p2-admin-temp` 2개 삭제·부재/기존 `can-i=no` readback을 namespace 삭제 전에 확보. #46 finish는 전체 자원 정리 증거가 아님 |
| 비공개 원본 보존·최종 readback·보고 | 각 생산자→권욱 집계 | 기존 10/26 12:00 완료 유지. backend·SSM·관리망·DNS·Runner 등 필요한 수단을 그 전에 없애지 않음. 실제 시작·복구 가용은 당일 확인 |
| 발표 뒤 VM 전체폐기·계정 해지·Public | 별도 범위 결정 뒤 원 소유자 | 12:00 필수 작업으로 추가하지 않음. 명확한 대상·의존성·보존 인수와 별도 GO 전 실행 없음 |

표의 독립 행은 전체 직렬 일정으로 강제하지 않는다. 소비 종료와 각 의존성을 기준으로 기존 담당자가 순서를 연결한다. ROSA/namespace 삭제는 검토된 키트와 당일 범위·권한/GO를 따르며, 이 표가 삭제 승인은 아니다.

- 재환의 VM 전 원본 편입 선행조건은 **ev252 병합으로 해소**됐다. 원문58개만 Git에 편입됐고 큰 원본5개는 공유 보관소 참조이므로 유지한다. 계정/VM 삭제나 공유 원본 일괄 삭제 허용으로 확대하지 않는다.
- db01의 P1 DR백업 `fdsdb_backup_20260903.dump`는 재환 PC 사본 재해시 일치 보고가 있다. 장기 보존 결정 전에는 기존 사본을 유지하는 준비안으로 남기며 이번에 이동·삭제하지 않는다. DB 시험 데이터이므로 공개 저장소에 넣지 않는다.
- edge01 담당은 재환 확인 완료. egress-proxy01의 재환 인수는 하영 동의 전까지 제안이다. Alertmanager 소비 종료 뒤 처리한다. 정본 배치 목록은 현재 host inventory 조회로 표시하지 않는다.
- D4 앱 중지(edge01→Worker)와 db01 전체 폐기는 별도 VM 창에서 연결한다. mgmt-gw01·DNS는 마지막 관리/이름해석 소비 후, Runner는 마지막 #46/CI·반출 뒤 등록 해제→VM 순서다. PKI 실제 볼륨 위치·폐기 방법은 NOT VERIFIED.

## 검토 범위

GitHub 원문·고정 소스·기존 중앙 수신 기록 및 AWS/GitHub 공식 문서를 대조했다.
Claude Code·Grok CLI·Antigravity CLI에는 비공개 원문 없이 각각 종료 의존성·공개 위험·표현 구조의
일반 설계 자문을 병행 요청했다. 요청 강도 high, 실제 응답 모델은 각 수신 기록에 보존한다.
자문에서 backend 삭제까지 기존 승인으로 분류한 내용은 원 승인과 달라 기각했다.
Grok의 “모든 Package가 함께 공개” 주장은 일반화하지 않았다.
새 Runtime·권한 변경·계정 해지·공개 전환·정본 발행·티켓 종결은 수행하지 않았다.

### 권욱의 P2 전용 파일 회수

[#55 인계](https://github.com/321Team/fds-project-baseline/issues/55#issuecomment-6382548801)에 따라
`/home/server01_cicd-runner/fds-p2-delivery`의 private Python·source cache·inputs·state는 권욱이 맡는다.
마지막 #46 소비·앱/claim/fence·메모리/프로세스 세션 상태 확인과 필요한 증적 보존/반출 뒤
자기 P2 파일만 회수·부재 readback한다. 기존 Runner HOME/workspace/다른 job은 제외한다.
사용 중 state·해제되지 않은 fence·보존 전 원본은 지우지 않는다. 10/26 12:00 이전 완료 조건이며
하영의 ROSA/RoleBinding 회수, 발표 뒤 별도 GO의 Runner 등록 해제→VM 폐기는 별개다.
