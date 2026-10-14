# G4 후속 준비 — 실행 결과 수용과 다음 실행 경계

이권욱 · CODEX_ASSISTED. GitHub·공유폴더 조회 **2026-10-14 15:35~15:47 KST**. 기준 baseline main `9b68b1ad4324595fa94c2af11a2fd10fbd0e95e3`, infra-terraform main `f1f8adf66d3b3c9348ebb919fe0dbb4f8fa54fe2`, infra-vpn main `f473ffb87b38ac863d650548694b4ad3af2c9ec7`. 기존 Plan·정책 검토는 재사용하고, 이번에는 새 실행 키트2개를 직접 수신·해시/내용 검토했다. 사후 스크립트의 실패 경로만 오프라인 MOCK으로 재현·수정안 검증했으며 AWS/RH/서버 실행은 없다. 기존14시 준비본의 변경 이력은 PR171에 보존한다.

**현재 판단: 사전 준비를 계속할 수 있으나 G4 PASS를 뒷받침할 전체 입력은 아직 없다.** 증적 PR226 편입 완료와 Stage2 키트의 새 결함·미확인 의존성, Apply 미승인, VPN 실제 증적 잔여를 서로 구분한다. 정본·AC·티켓 상태·담당자·일정·권한을 변경하지 않는다.

## 이전 준비 이후 실제 달라진 것

| 항목 | 확인한 최신 사실 | 남은 범위 |
|---|---|---|
| 배포 준비 코드 | [PR80](https://github.com/321Team/infra-cicd/pull/80) `eeadfd256b5360fb414569e15f0e32c2efd9ea39`, 이하영 독립 승인·HEAD CI 2 SUCCESS, 13:04:33 병합 `b183fddb9c65e7119bf008214c34bef3ca4066d2` | 실제 승인 진위·identity/RBAC verifier와 운영 연결·ROSA Runtime |
| 준비 문서 | PR170 이후 [PR171](https://github.com/321Team/fds-project-baseline/pull/171) `585ddd10d710c1eeb5c2a9a8ee3ea8157c4843bb`, 하영 동일 HEAD 승인·권욱 Lead 검토, 14:42:58 병합 `9b68b1ad4324595fa94c2af11a2fd10fbd0e95e3` | 이번 회차가 병합한 것이 아님. 아래 최신 실행/검토 기록을 기존 준비본에 연결 |
| OCM / A3 Stage1 | [실행 결과 수용](https://github.com/321Team/infra-terraform/issues/12#issuecomment-6160187548): OCM 생성·Linked Yes/Admin No, A3 9 create·검증 Plan No changes. [12:29~12:30 보완 원본 검토](https://github.com/321Team/infra-terraform/issues/12#issuecomment-6160425675)에서 역할·OCM permission Document·issuer 대조 | [관리정책4개 본문·전체 해시 보완 수용](https://github.com/321Team/infra-terraform/issues/12#issuecomment-6161897527)은 완료. RHCS thumbprint 출처·정확한 조직 대응/인증 정리·Subscribe 최종 스냅샷만 잔여. 전체 재시험 불필요 |
| Subnet 태그 | [원본 독립 검토 수용](https://github.com/321Team/infra-terraform/issues/11#issuecomment-6160427524): 승인 Plan 1회·2 update, readback·No changes. private_a/internal-elb와 public_transport_a/elb만 변경 | 재Apply 대기에서 제외. 다음 Plan/Apply 직전 actual 태그·IP 여유는 해당 실행에서 다시 확인 |
| Stage2 saved Plan | [수집14:27:51~14:30:28 종료·같은 JSON 수정 checker187/187](https://github.com/321Team/infra-terraform/issues/12#issuecomment-6161897527), [saved Plan 소스/state·16 create/기존9 no-op 검토 수용](https://github.com/321Team/infra-terraform/issues/12#issuecomment-6162072284) | 새 Plan 수집 대기 해소. [PR32](https://github.com/321Team/infra-terraform/pull/32) `ba0f0c9` 승인 후15:48:27 KST 병합 완료(`038c490e79f80237b43f6bb04cef34edd26bc820`), 병합본 검사 결과는 별도 확인 잔여(병합 전 현황 보완). 아래 실행 키트 수정·의존성 확인 후 별도 Apply GO. DEFERRED16은 실제 readback 잔여 |
| Relay B0/B1 | [패키지·후속 조회 원본 수용](https://github.com/321Team/infra-terraform/issues/11#issuecomment-6160185014), 준비안 기술 차단 없음 | [15:40~16:10 KST 동일1회 승인](https://github.com/321Team/infra-terraform/issues/11#issuecomment-6162400235), 기존16:30 창 대체. [재환15:40 착수 보고](https://github.com/321Team/infra-terraform/issues/11#issuecomment-6162515661) 수신, 완료/실측 원본 미수신. T5 API 성공은 실제 Resume 셸 재연결 성공이 아님 |
| 증적 편입 | [evidence PR226](https://github.com/321Team/fds-project-evidence/pull/226) 최종 `025302ac41edf0344d880c45dc383b18ee4cf30d`, 권욱 독립 승인·HEAD CI1 SUCCESS, 14:46:39 병합 `a4108700b99f479a0fa6572f65145cafa937af84` | 기존 문구 차단·편입 대기는 해소. 이번 새 승인/원본 재검증 아님. Stage1 최종 증적·Stage2 Runtime까지 완료한 것으로 확대하지 않음 |

원본 해시 일치는 무결성이다. 예를 들어 Stage1 오전 manifest는 설명된 ledger 한 줄 추가로 8/9이며 이를 9/9로 바꾸지 않는다. 보완 원본은 현재 시각의 조회이며 오전 실행 시점으로 소급하지 않는다. 위 기존 수용 기록을 이 문서 작성자가 새로 수행한 독립 검증으로 표시하지 않는다.

## G4의 기존 7개 입력 대조

[G4 #39의 Gate Data Contract](https://github.com/321Team/fds-project-baseline/issues/39)를 유지한다. [12시대 현황표](https://github.com/321Team/fds-project-baseline/issues/39#issuecomment-6160062554)의 태그 미착수·Stage1 원본 미검토는 위 후속으로 갱신한다. 그 표의 “Critical blocker 없음”만으로 아래 미완료 필수 입력을 충족 처리하지 않는다.

| 입력 | 이번 소비 판단 | 다음 담당·완료조건 |
|---|---|---|
| 1. #34 Freeze | [version4.22.17·name fds-rosa-hcp 고정](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-6162036785). public/public 계약 재사용. 두 입력 고정은 전체 Freeze 아님 | 권욱: 나머지 topology·보안/관측/복구 계약 대조. 하영: 실제 ROSA 제공 목록을 실행 직전 확인. 생성 후 API/UID를 Freeze 선행조건으로 요구하지 않음 |
| 2. #35 Full IaC | Stage1/OCM 실행 수용 + 태그 완료를 반영한 부분 충족 | 하영: 키트 수정·의존성/병합본 검사→권욱 검토·별도 Apply GO→실행/readback, 위 최종 증적 보완. Stage1 재Apply·Subscribe 재부착으로 해결하지 않음 |
| 3. #36 D21 | FINAL OCI NO-GO / AWS Relay 결정 재사용 | 권욱: 기존 결정·원본 편입 링크 소비. 새 OCI 시험·선택 요구 없음 |
| 4. #37 VPN | SSM 접근·첫 호스트 읽기와 B0/B1 준비는 부분 수용 | 재환: 승인된 B0/B1 원본을 먼저 인계하고 별도 승인 단계의 터널/Route/security·승인 TCP canary·negative/recovery 원본. SSM 성공·패키지 해시로 터널 PASS 대체 금지 |
| 5. ROSA 생성 준비 | account roles/OIDC·subnet 태그·CA와 public/public 코드 준비 | 하영→권욱: Stage2 실제 outputs와 고정 version/name을 합친 최종 tfvars·생성 준비 자료. ROSA Cluster Ready를 G4 전에 요구하지 않음 |
| 6. 비용 | [기존 Cost GO](https://github.com/321Team/infra-rosa/issues/4#issuecomment-6143326582) 유효. 지정 비용 세션 최신 사용자 값은 $2.85, 새 값 없음 | 권욱: 동일 중앙 리포트로 사용액/예상·headroom 추적. 기간/cutoff 미확인 금액을 전체누적/잔액으로 계산하거나 기존 Cost GO를 다시 미승인 처리하지 않음 |
| 7. Critical 잔여 | saved Plan 기술 수용·새 실행 키트 차단과 전체 Gate 충족은 별개 | 권욱: 필수 미충족·Known Issue·Approved Fallback을 구분한 최종 판정. PR226 편입 차단은 해소. 새 키트 결함은 해당 Apply 전 해결하며 기존 Stage1 실행 실패로 소급하지 않음 |

**준비상 `G4=NOT_READY`이며 공식 PASS/NO_GO·AC 체크를 새로 등록한 것은 아니다.** N1은 실재 다른 대상 부재로 `NOT_RUN_NO_OTHER_REAL_INSTANCE`를 유지한다. 시험용 자원 생성·없는 ID·시뮬레이션 PASS로 메우지 않는다. G4 목표일 도래는 PASS 근거가 아니다.

## 실행 회차와 후속 인계

**Plan 수집은 종료, B0/B1은15:40~16:10 승인, Stage2 Apply는 HOLD**다. [두 담당자 AWS 작업창](https://github.com/321Team/infra-terraform/issues/11#issuecomment-6162400235)만 직렬화한다. Harbor/온프레미스 창 반납을 조건으로 추가하지 않는다.17:15~19:15는 하영 Apply의 후보안이며 실행 GO가 아니다. 아래 Plan 계약은 완료 회차 추적용으로 보존하고 재실행 지시로 사용하지 않는다.

### A. 하영 Stage2 saved Plan — 종료 회차의 계약

- **대상·주체:** 계정 `774055931866`, 서울/default workspace, `phase2/rosa-prereq/terraform.tfstate`. 하영 본인 MFA `FDS-IaC-Operator` + 본인 Red Hat 인증. source `f1f8adf66d3b3c9348ebb919fe0dbb4f8fa54fe2`, Terraform1.16.4/AWS6.66.0/rhcs1.7.9 및 기존 lock. root 사용·IAM 권한 변경은 이 준비안에 없다.
- **직전 조건:** caller/조직/issuer·현재 state 식별·lock·다른 writer·미관리 동명 역할 확인. Stage1 인계 lineage/serial1은 비교 기준이며 현재 state를 강제로 되돌릴 값이 아니다. 예전 잠금404를 현재 writer 부재로 재사용하지 않는다.
- **순서·기대:** [검토된 Plan 수집 계약과 checker 명령](https://github.com/321Team/infra-terraform/issues/12#issuecomment-6160189356)을 재사용. `execution_enabled=true`, `create_operator_roles=true`; saved Plan rc2, **16 create/기존9 no-op/update·delete·replace0**, checker rc0. operator prefix/ARN map output 변경은 기대값이다. 실제 Plan binary/JSON·source/lock 해시, 명령/RC·시각·state 식별·종료 lock을 기존 증적 묶음으로 제출한다.
- **영향·중단·복구:** backend lock 임시 쓰기와 로컬 Plan 파일 생성이 있다. IAM/RH 리소스 생성·변경은 없다. 조회 거부·예상 외 action·동시 writer·state 차이면 보존 후 STOP. 자동 재시도·`-lock=false`·`-target`·force-unlock/import/state 수정·Apply 및 manual의 create/attach는 제외한다. 남은 lock은 진단 후 별도 판단하며 강제 해제를 복구로 사용하지 않는다.
- **현재:** 이 계약의 수집·Plan 검토는 완료됐다. 기존 동일 Plan을 다시 수집하지 않는다. 실행 키트 수정·의존성·PR32 병합본 검사와 직전 actual 유효성을 확인한 뒤 exact Stage2 Apply/작업창을 별도 판단한다. 기존 Cost GO는 IAM Apply를 대신하지 않는다.

### B. 재환 Relay B0 전달·B1 읽기

- **대상·주체:** 계정 `774055931866`, 서울 Relay `i-05e4b63d31d8d5ac5`; 재환 본인 MFA netop → `ssm-user`. infra-vpn main `f473ffb87b38ac863d650548694b4ad3af2c9ec7`의 검증된 패키지 `p2-vpn-01-relay-b0.tgz`, SHA256 `880a0df51d74ec178add3bdfbdb026596f4353ccd2f66dfc790f5d193458bc31`.
- **승인창:** 10/14 15:40~16:10 KST, 동일1회. 이전16:30~17:00은 대체됐으며 자동 이월/추가 회차 아님. 하영 AWS 실행은 재환 실제 종료·정리 후이며, 비공개 원본 전달 완료와 호스트 작업 종료를 구분한다. [하영15시 전달 회신](https://github.com/321Team/infra-terraform/issues/12#issuecomment-6162563808)에서도 재환 창 중 AWS 작업 없음·Apply HOLD를 명시했다. 재환 착수 보고를 완료/검증 성공으로 확대하지 않는다.
- **직전 조건:** [기존 검토](https://github.com/321Team/infra-terraform/issues/11#issuecomment-6160185014)의 같은 SessionId/Owner/Target에 대해 History/Active를 현재 시각으로 확인. 조회 실패·Active 재등장·대상 불일치는 STOP. Terminating 지속은 미해소 정리 조건으로 기록하고 임의 재부팅·Agent 재시작·IAM 확대를 하지 않는다.
- **순서·기대:** 새 홈 폴더에 일반 사용자 전달·해시/manifest 확인(B0) 후 검토된 `relay check`와 unit별 상태·trafficstatus·firewalld/sysctl 개별 RC 및 Libreswan4.15 지원 옵션 읽기(B1). sudo 읽기에서는 `P2VPN_PREFIX`/`LIBRESWAN_MAJOR` 제거. 내부 manifest는 해제한 상위에서 `sha256sum -c p2-vpn-01/SHA256SUMS`로 확인한다. RC0 하나로 B1 전체 PASS를 선언하지 않는다.
- **영향·중단·복구:** 홈 파일/증적만 생성; 시스템 경로 설치·PSK·render/apply/up/probe/rollback·VPN 단계 B/C·AWS route/SG·Phase1 변경 제외. 패키지/대상 불일치 시 실행하지 않고 해당 폴더를 격리·기록한다. inactive/trafficstatus 실패를 고치기 위해 daemon을 시작하지 않는다. 자기 시험 세션만 종료하고 Active/History 정리 원본을 남긴다.
- **수집 후:** 재환 원본·RC·한계 인계 → 권욱 소비. 실제 터널·TCP canary·DB 예외 및 원복은 정확한 대상/창/승인 범위로 별도 연결한다.

### C. 새 수신 실행 키트 — Apply 전 필요한 수정

[원본 수신·검토 및 적용 가능한 수정안](https://github.com/321Team/infra-terraform/issues/12#issuecomment-6162560382). 원본 두 파일은 요청 해시와2/2 일치하며 Bash 구문 통과. `h-s2-post.sh`의 ROSA API 오류가 rc0으로 종료되는 두 경로를 MOCK으로 재현했고 제안 수정안 정상1/실패4의 기대 결과를 확인했다. 네트워크·실제 AWS/ROSA 호출0, binary hash/도구 응답/Windows 파일모드는 mock이며 실제 CLI 호환 시험은 아니다.

| 구분 | 근거·영향 | 해결·완료조건 / 담당 |
|---|---|---|
| 기술 차단 | `h-s2-post.sh:15~23` 조회 RC/OIDC 실패를 마지막 역할 개수 조건이 덮어 성공으로 인계 | 하영: 제공 diff 반영·새 해시 → 권욱: 변경 실패 경로 재검토. 원본 전체 시험 반복 불필요 |
| 증적 차단 | `30-s2-apply.sh:58~63,73` GetRole trust/태그 원문과 API stderr/RC의 역할별 파일·manifest 누락 | 하영: 기존 API 호출 결과만 비공개 파일로 보존·최종 manifest 연결 → 권욱: 정상/조회오류 때 보존·판정 검증 |
| 확인 필요 | 실제 common.sh/MANIFEST 미포함으로 caller·ABSENT·pipefail·실패 정리 구현 미확인 | 하영: 기존 파일 위치 또는 실제 파일·해시 연결 → 권욱 내용 검토. common 결함으로 단정하거나 토큰/기존 Plan 재제출을 요구하지 않음 |

이 키트 잔여는 재환 B0/B1의 차단조건이 아니다. 기존 Plan·관리정책 수용과 기승인 검증권한 유지 결정도 되돌리지 않는다. root 실행 방식의 채택과 실제 위임/Apply GO는 계속 분리한다.

## #42 / #46 — 지금 재사용할 입력과 생성 후 입력

[실제 입력 MOCK 보고](https://github.com/321Team/infra-rosa/issues/4#issuecomment-6160198144)와 [소비 범위 리뷰](https://github.com/321Team/infra-rosa/issues/4#issuecomment-6160430902)를 연결한다. 1회차3/3은 실행자 MOCK 보고다. [r2](https://github.com/321Team/infra-rosa/issues/4#issuecomment-6161915781)는14:53:12 실행·test/명령/RC 원본 보존 보고이며 공유 수신·독립 재현은 이번에 하지 않았다. 이 보고의 “Stage2 Plan 재수집/Freeze 대기”는 이후 Plan 수용·입력 결정으로 대체됐고 재수집을 요구하지 않는다.

| 구분 | 재사용 / 인계 조건 |
|---|---|
| 이미 받은 것 | Stage1 OIDC/account roles, VPC/subnet·태그 수용, 기존 Registry CA JSON·공개 인증서/경로 계약. 같은 CA·전체 TBS/Push 원본 재요구 없음 |
| 생성 전 미결 | `operator_role_prefix=fds-rosa`는 아직 Plan 기대값이며 Stage2 실제 output으로 결속. [4.22.17 / fds-rosa-hcp 입력 결정](https://github.com/321Team/infra-rosa/issues/4#issuecomment-6162036371)은 완료. r2 해시를 최종 생성 입력으로 재사용하지 않고 actual output과 결합한 tfvars SHA 고정 |
| 생성 후 하영 | 실제 API/CA/cluster identity, `fds-app` namespace UID·승인 host·지원 인증/최소 RBAC 원본. `rosa-app`은 overlay이며 P1/공용 OCP identity 복사 금지 |
| 재환 공급 | 앱별 P2 채택 current와 previous-approved digest·clean render·원격 receipt. P1 성공을 P2 채택 승인으로 바꾸지 않음 |
| 권욱 소비 | 기존 D22 A/B·인증 갱신/복구 계약에 actual을 연결하고 해당 단계 결정. 실제 입력 수신 후 PR80의 BoundAuthorizer에 진위·권한 검증 provider/운영 수명주기 연결 및 독립 코드 검토. 임의 호스트·승인 boolean·합성 Lease로 Runtime 경계 우회 금지 |

## #49 / #55 — 편입·정리·Review 후속

1. **PR226 정정·편입 완료:** 최신 `025302ac`의 독립 APPROVED·CI1 SUCCESS·14:46:39 MERGED를 확인했다. 기존 README 정정/해시 갱신/편입 대기를 해소하며 같은 수정·리뷰를 요구하지 않는다. 기존 원본 수용을 이 문서 작성자의 새 독립 검증으로 복제하지 않는다.
2. **#49 집계는 권욱:** [기존 I01~I16/4묶음](evidence-handoff.md#1014-입력표와-현재-증적의-대조)에 정책4개 보완·Stage2 Plan 수용·PR226 편입을 연결했다. 키트 차단·B0/B1 실제 원본·Stage1 최종 잔여는 각각 별도로 남긴다.
3. **삭제 준비는 기존 리뷰 재사용:** [ROSA 생성·삭제 순서표 리뷰](https://github.com/321Team/infra-rosa/issues/4#issuecomment-6160430902). D2 delete_protection만 update1/나머지2 no-op → 적용/readback → 갱신 state의 D3 destroy Plan 검토/별도 결정. 한 창이어도 자동 연쇄 실행 없음. actual inventory는 infra-rosa#4, 삭제/보존 receipt는 #8, 비용 판단 소비는 #34. 조회·대기 중에도 운영 자원 과금은 계속된다.
4. **Review 제안 유지:** 10/23 14:00~15:30·권욱 참석 미정, #40/#48/#120 보류 유지. 정본 발행·회의 개최·삭제·Close를 준비 문서로 완료 처리하지 않는다. 검증 전용 권한은 재시험·원본 검토 종료 후 정리하며 운영 최소권한과 구분한다.

이번 문서에는 기존 REVIEW/MERGE 기록과 새 키트 STATIC/MOCK 결과를 구분해 연결했다. 새 RUNTIME·실행 GO·MERGE·PUBLICATION·티켓 종결은 이 문서 갱신의 완료 범위가 아니다. Phase1 DB/pg_hba/영구 방화벽/NetworkManager/route/Harbor CA/Runner/공용 OCP/DNS·LB/AC 보호, `sources/` 읽기 전용, 10/13 종료 자동 작업 PAUSED 유지. 준비 문서 복구는 해당 커밋 revert다.
