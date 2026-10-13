# D21·Gate·최종 정리 증적 인계 준비

CODEX_ASSISTED. 실제 원본을 대신하는 문서가 아니다. Phase 1 작업은 제외한다.

## D21 publication 접수

[#36 권위 기록](https://github.com/321Team/fds-project-baseline/issues/36)의 결정은 FINAL / OCI Primary NO-GO / AWS EC2+EIP Libreswan Relay 선택이다. 재선택이나 새 OCI 시험은 불필요하다.

| 접수 대상 | 알려진 기준 | 이번 실제 상태 |
|---|---|---|
| canonical responder raw | d21-ike-observer-20261003T042646Z.log / 8706 bytes / SHA256 e5f754a3d66c6fe452605ff914a6294e87aa85bf6a345ec0fadb981f18745cb0 | 사용자 파일 수신·크기/해시 대조 완료. [PR161](https://github.com/321Team/fds-project-evidence/pull/161) HEAD `162892f99a4d779a4f452be2bcf38b8e90bbbe6f`로 독립 승인·CI 후 병합 완료 |
| 결정·인계 | #36 final 블록과 #34/#35/#37 연결, source/시각/실행자/명령/RC, cleanup 근거 | 기존 기록을 참조. source 없는 실행 필드는 추정하지 않음 |
| candidate 변경 | D21 당시 AMI와 PR7 최종 Stream9 후보/merge93d7150은 별개 | 원본 역사 AMI를 바꾸지 않고 새 검토/수용 기록으로 연결 |
| publication | evidence/P2-OCI-01/received-20261008T061032Z-d21-final-responder/ | PR161 MERGED, 10-08 17:05:38 KST, merge `277893c7865bd2af9751ca73ee00985370c9eaf2`. [편입 기록](https://github.com/321Team/fds-project-baseline/issues/36#issuecomment-6055596216). 원본 편입과 정본 publication/티켓 Done을 구분 |

원본 무변경 편입과 size/SHA 대조는 [수신 기록](https://github.com/321Team/fds-project-baseline/issues/36#issuecomment-6053629791)에 연결했다. 불일치/민감정보가 있으면 공개 게시를 멈추고 원본·공개용 사본을 구분한다. 실제 IKE_AUTH 도달/불일치 PSK 응답은 production SA·Tunnel 인수 증적이 아니다. 권욱 실행/생산 결과의 독립 증적 심사는 하영/재환 등 기존 정책에 따른다.

initiator/cleanup 별도 raw는 미확인이다. 사용자 Desktop.zip의 local-route/base 기록을 final initiator/cleanup으로 대체하지 않는다. base는 기존 편입 원본과 중복이며 local-route는 연결 성공이나 SA 검증이 아니다. 새 OCI 시험이나 존재가 확인되지 않은 파일의 재제출을 요구하지 않는다.

## Gate 소비표

| Gate | 필수 실제 입력 | 지금의 준비 / 최종 판단 책임 |
|---|---|---|
| G4 #39 / 10-14 | #35 Full IaC 실제 ID·Plan/Apply, D21, #37 Relay/SA/route/security/승인 TCP/negative/recovery, #38 생성 선행 입력·비용 | 기존 [PR152](https://github.com/321Team/fds-project-baseline/pull/152)의 G4 표 재사용. 이권욱. ROSA Cluster Ready를 G4 전에 요구하지 않음 |
| G5 #45 / 10-20 | #38 Full security/SCC·UID/RBAC/NP, #43 App, #46 정상 Delivery·실패차단, #42 D22 Final, P1 결정상태 | 기술 Lead 이하영, PMO/QA 이권욱. source→remote digest→runtime imageID, evidence review/merge 대조 |
| G6 #53 / 10-22 | #47 exact Hybrid handoff와 #50 Final E2E/Regression | 이권욱. 실제 ROSA→On-Prem 증적, Critical·Known Issue·미충족을 구분 |
| #49/#54/#56 / 10-23 | 동일 immutable candidate set, Decision/Known Issue·source/evidence/manifest·비용/정리 상태 | 이권욱. Lab/ROSA 분리, 미병합 evidence·미승인 CR을 완료로 올리지 않음 |

새로운 시험 없이 'PASS'를 채우는 체크리스트가 아니다. 생산 티켓의 최신 raw/commit을 소비하고 hash 무결성·STATIC/MOCK/CI/Runtime·REVIEW/MERGE/PUBLICATION을 구분한다.

## 운영·삭제·Review 준비의 최소 완료조건

기존 [Terraform 운영·정리안](https://github.com/321Team/infra-terraform/blob/93d71500e3e881c55f1814cd144ca41f43e77f3d/docs/preflight-20261007/operating-teardown-plan.md)과 [이벤트 기준 생성/삭제·Review 준비](lifecycle-review-preparation.md)를 사용한다. 실제 작업창은 미정이며 문서에 적힌 시작/종료 시간은 제안이다.

1. 자원별 owner·실제 ID/state·삭제/보존·의존 순서·복구 가능 상태와 증적 수신 여부를 정한다.
2. ROSA 정상 삭제 및 의존 자원 확인 → 승인된 vpn/network 삭제 plan 순서. CFn bootstrap/backend/state/evidence·공용 IAM/SLR은 기본 삭제 대상이 아니다.
3. account Session document의 prevent_destroy/중앙 소유를 존중한다. 일괄 destroy·임의 state rm/target 우회 없음.
4. 실제 삭제 완료시각과 EIP/EBS/snapshot/ENI/LB/NAT/endpoint 등 잔존 사유·Owner를 연결한다. 교육장 리포트의 후행 사용액/예상 총비용으로 비용을 추적한다.
5. 10-23 Review 시간·참석자 미정. 10-26 Close에는 승인된 Review Action·정리·잔여 Owner/Due·sign-off를 소비한다. 이 패킷이 Freeze/Review/Close를 승인하지 않는다.

조건부 DNS/Operator/OADP/GitOps/Compliance/RHOAI는 해당 Lead의 Go/No-Go/Deferred·근거/Owner·재검토 조건을 연결한다. 실제 구현 완료가 P0 필수인 것처럼 Gate를 추가하지 않는다.

## 10/13 보완 — G4 exact 입력별 수신·잔여 연결

기준: [#39 Gate Data / Review Contract](../../../tickets/v3.1.21/descriptions/MS-G4-01.md)의 7개 입력. 외부 PR 상태는 **10/13 17:48 KST** 스냅샷이다. 아래는 Gate 검토 준비이며 `G4=PASS`나 공식 `NO_GO` 발행 기록이 아니다. 실제 판정 직전 변경된 HEAD/입력만 재대조한다.

| 기존 필수 입력 | 현재 소비 가능한 근거와 검증 범위 | 아직 닫히지 않은 조건 / 생산→판단 책임 |
|---|---|---|
| 1. #34 Freeze current values | [PR29 source 승인](https://github.com/321Team/infra-terraform/pull/29#pullrequestreview-5500767150), HEAD `3079ddcb8712a761c7c1c3fe59189689eb2e38fe`, public/public·Plan/Apply 승인 경계. OPEN, CI0=NOT_RUN | 생성 전 전체 네트워크·IAM·보안·용량 계약과 변경결정의 정합 수용: 이하영 입력 → #34 이권욱. source 승인만으로 Freeze 완료 아님 |
| 2. #35 Full IaC + actual identity | [PR28 수정요청](https://github.com/321Team/infra-terraform/pull/28#pullrequestreview-5500767746), HEAD `d46b50fac65ec5368b3502072ea0de5aa5b922c3`. [PR31](https://github.com/321Team/infra-terraform/pull/31) `bd155bb32bac42fa9cd5975c25369b395cff2683` source 승인·OPEN, CI0 | actual VPC/Subnet/Route/IAM/OIDC/State와 단계별 승인·readback. BoolIfExists 후보 source 승인은 실제 IAM 반영·SSM 정상/거부 검증 아님: #35 이하영 → 이권욱 |
| 3. #36 D21 | 위 PR161 원본 편입·독립 승인·MERGE 및 OCI Primary NO-GO/AWS Relay 결정 재사용 | D21 결정을 새 OCI 시험으로 재개하지 않음. 미확인 initiator/cleanup raw는 미확인 그대로 유지. D21 결과와 #35/#37 actual 연결: 이권욱 |
| 4. #37 VPN/보안/승인 TCP·복구 | [#13 종료 보고](https://github.com/321Team/infra-terraform/issues/13#issuecomment-6141223429): PR30 merge `6847d906f974136a5a4aad5ffe47d45930f142e7`, Plan16:50:42~58 KST rc0/No changes 보고. [evidence PR214](https://github.com/321Team/fds-project-evidence/pull/214) `8b0bf20fc2e863f22fd959ff32902bbfc73f2124`, 별도 작업의 독립 편입 승인·OPEN·CI1 SUCCESS | 기존 manifest/source 검토 재사용; 이 작성자가 비공개 tar/Plan/JSON 전체 수신·재해시했다고 표시하지 않음. 실제 단계 B·ALLOW/DENY·복구와 db01 script 절대경로/RUN/원복 인계: 이재환 → #37 수용 → #39 이권욱. Plan은 전체 AC-5/G4/재Apply GO 아님 |
| 5. ROSA 생성 준비 | PR29 설계 source, [#12 A1/A2 확인](https://github.com/321Team/infra-terraform/issues/12#issuecomment-6141247655), [ROSA#11](https://github.com/321Team/infra-rosa/issues/11) CA/경로 준비 CLOSED | Region/Topology/Version/Quota·계정/OCM/user-role·단계별 권한 실제 충족. A1/A2 창과 완료, A3 Apply/Create 승인 구분: 이하영/중앙 권욱 → #38. G4 전에 Cluster Ready 요구하지 않음 |
| 6. 비용 잔여 여력 | 교육장 리포트 기반 중앙 판단, 목표400/중단450/상한USD500·자부담0 유지 | 10/12 사용량0 사용자 보고는 전체 누적/현재 예상 총비용0 또는 Cost GO가 아님. 최신 보고의 기간·as-of·사용액/예상 총비용: 이권욱. 구축 담당자 재견적 요구 없음 |
| 7. Critical 잔여 | 위 미충족을 담당자·단계와 함께 기록. 준비 코드/문서 및 부분 증적 수용은 전체 인수 아님 | 각 생산 Lead의 현재 잔여를 소비하여 이권욱이 Gate 판정. 미해결을 지우거나 일정만으로 PASS 금지 |

Network 원본 `p37-netop-jaehwan-20261012T121250Z.tgz`의 기존 수신·SHA/manifest20/20·내용 검토는 [독립 검증 기록](https://github.com/321Team/infra-terraform/issues/11#issuecomment-6126479035)을 재사용한다. `SSM_START=BLOCKED / FULL_T1_T6=PARTIAL / FIRST_HOST_READBACK=NOT_RUN`을 보존한다. 명령·도구/당시 정책 버전 미수집은 다음 시험부터 보완하며 전체 시험 재요구 사유로 삼지 않는다. N7b StateDeny 기대표 정정은 IAM 권한 확대 사유가 아니다.

### 10/13 18:30 수신 보완 — 위 17:48 스냅샷 이후

- [A1 성공/A2 STOP 보고](https://github.com/321Team/infra-terraform/issues/12#issuecomment-6142354704)를 수신했다. Subscribe attach는 VERIFIED/RC0, A1은 18:11 KST 활성 상태 확인으로 **보고**됐다. 이 문서 작성자가 AWS·현장 ledger·비공개 캡처를 직접 검증한 것은 아니므로 `A1_RUNTIME=SUCCESS_REPORTED`, 원본 수신/독립 수용은 별도다.
- A2의 현재 기술 차단은 `servicequotas:ListServiceQuotas` identity-based Allow 부재다. 할당량 자체의 충분 여부는 미확인. [별도 후속 판단 기록](https://github.com/321Team/infra-terraform/issues/12#issuecomment-6142452170)은 하영 본인 MFA IAM 사용자 기존 권한으로 같은 계정·기존 조직 연결만 조건부 1회, 신규 쓰기 착수 종료20:00 KST를 명시한다. **A2 완료·Subscribe 분리 완료는 아직 미확인**이다. 새 권한 확대·A1 재활성화·자동 재부착·OCM/A3/Create GO로 해석하지 않는다. 이 외부 기록은 이번 문서 작성자의 실행 권한이 아니다.
- [PR28 수정 회신](https://github.com/321Team/infra-terraform/pull/28#issuecomment-6142399307), HEAD `8a80d82b023b9a9b49b42ea96f1dc9e3bc537b2d`: [별도 작업의 18:27 APPROVE](https://github.com/321Team/infra-terraform/pull/28#pullrequestreview-5501472422) 후 **18:29:07 KST MERGED**, merge `a7081810484e8a3141ad060410d093c8d4e1919a`. B2 유지/회수4경로 및 초기/재개 지적 해소를 소비한다. 전체 문서/diff 자체 대조에서도 P2의 `D1~D7 승인`과 현행 A2 identity/시각의 표기 차이를 확인했으며, 별도 리뷰의 처분대로 **비차단 정합화**로 남긴다. 실행은 명시된 단계별 조건·최신 #12 후속 판단·fresh 상태를 우선하며 A1을 다시 실행하지 않는다. CI0=NOT_RUN. 이번 작성자는 해당 PR 승인/병합을 수행하지 않았다.
- #46의 [PR75](https://github.com/321Team/infra-cicd/pull/75)는 `39fd173b4fd22e1ca2b4e430cc984ace01947bd1`로 갱신됐다. 기존 source/시험 변화 없이 중단 RUN 복구 검토 문서2개만 보완했으며 새 HEAD CI2 SUCCESS·104중94PASS/10SKIP, 독립 리뷰0·Draft·미병합이다. 운영 재시작 후 journal/active 조정 기능은 미구현 잔여로 명시했다.
- P2 공급 입력의 관련 상태만 소비한다: [CICD PR76](https://github.com/321Team/infra-cicd/pull/76) `f78033511b542d6241064ca7be3e17b4100be8ad`와 [PR77](https://github.com/321Team/infra-cicd/pull/77) `f323dfc1eaa4c491042d0655dc840e5b1a57920d`는 이미지 권한/격리 기동 검사 후보이며 OPEN이다. 이 채팅은 P1 코드 리뷰·수정·실행을 하지 않는다. P2는 실제 새 이미지/승인 digest·공급 결과가 인계된 뒤 소비하며 후보 수정/CI를 실제 새 이미지 기동 PASS로 올리지 않는다.

### #49 rolling 집계와 #54 Freeze 연결 — 계속

10/07~22에는 생산자가 기존 티켓/증적에 결과를 누적하고 이권욱은 **변경된 링크·판정만** 갱신한다. 10/23에 처음 자료 작성을 시작하지 않는다. 다음 묶음을 동일 candidate 목록으로 #54→#56→#55에 전달한다.

| 집계 묶음 | 현재 연결 / 다음 입력 | #49에서 닫는 조건 |
|---|---|---|
| Cloud/VPN·Architecture | 위 G4 7개 행, #34/#35/#37/#39 | As-built와 승인 기준 차이·actual ID·기존 Runtime 원본/리뷰/병합 범위 대응 |
| App/Delivery·Hybrid 시험 | [PR75](https://github.com/321Team/infra-cicd/pull/75) `df7c01c4ad0a5e8aa884cba1a4cb50ecac8ebbaf`: Draft, 리뷰0, CI2 SUCCESS; Linux104 중94PASS/10SKIP. #43/#47/#50 actual 원본은 후속 | source→remote digest→runtime imageID/업무 결과, 실패차단·복구·미실행 분리. PR75 MOCK은 실제 TLS/API/배포 증적 아님 |
| Decision·Known Issue | #36 결정, [D22](d22-lead-review.md), [D23](decision-packet.md), 조건부 P1/P2 결정 | 확정/제안·Deferred의 이유/Owner/기한/재검토 조건 구분. 미결 결정값 합성 금지 |
| 비용·정리·Review | [운영·Review 준비](lifecycle-review-preparation.md) | 원본 보존/수신, 삭제·보존 inventory, 교육장 리포트·잔여 Owner/Due, #52 실제 시간/참석자 기록 |

각 기존 증적 항목에 필요한 연결은 `ticket/AC · producer · source SHA/RUN/대상/관측 KST · 원본 위치 · 공유/수신/재해시/내용검토 각각의 상태 · STATIC/MOCK/CI/RUNTIME · REVIEW/MERGE/PUBLICATION · 잔여 Owner/완료조건`이다. 이미 있는 필드는 링크로 소비하며 새 양식 재제출을 요구하지 않는다. 비공개 원본 Plan/state/credential은 공개 집계에 넣지 않는다.

**집계 중 결함 처리:** 깨진 링크·SHA 불일치·서로 다른 RUN 결합이면 해당 행 수용을 보류하고 원본 생산자에게 누락/차이만 확인한다. 다른 행은 계속 검토한다. Critical 문서 결함0과 기존 #49 AC를 확인하기 전 #54 Freeze 완료로 표시하지 않는다. 증적 저장소 편입/정정은 기존 독립 리뷰 정책을 따른다.
