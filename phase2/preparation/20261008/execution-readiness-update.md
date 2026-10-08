# Phase 2 최신 변경 수신·시험 실행 준비

최초 조회 2026-10-08 13:40 KST, 소스/리뷰 수신 갱신 14:50 KST. 최신 잔여와 Plan 준비는 [착수 목록](prework-next.md)을 따른다. CODEX_ASSISTED. 이번 결과는 준비 자료이며 Runtime GO·AC 인수·정본 발행이 아니다. Phase 1 구현/실행/Close는 제외하고 생산자가 P2에 인계한 계약만 소비한다.

## 직전 준비 이후 실제 업데이트

| 대상 | 확인된 실제 결과 | 남은 조건 |
|---|---|---|
| Terraform PR6 | HEAD `77c63247d2a1cc8e6c920b80e66d42ffef5545b6`, [이재환 승인](https://github.com/321Team/infra-terraform/pull/6#pullrequestreview-5450726246), merge `cfe59194cabc37fd9506a0776fe502d9627a0631` (10-08 11:57:31 KST) | 준비/읽기 수집기 병합. accepted_execution_sha는 별도 결정 전 null |
| Terraform PR7 | HEAD `127921559e41f9667ccaf855bf6a3d3c2876fd5d`, [이재환 승인](https://github.com/321Team/infra-terraform/pull/7#pullrequestreview-5450725959), merge `93d71500e3e881c55f1814cd144ca41f43e77f3d` (11:58:38 KST) | RPM import 지적 해소. 실제 Stream9 설치는 리뷰어가 비차단 후속으로 분리. CI 0/NOT_RUN, first boot·Agent Online·VPN 미검증 |
| #35 Lead 준비 수용 | [이하영 6049616674](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6049616674), 대상 이전 HEAD `37f5c8c`의 문서/읽기 수집기 수용 | full permissions/trust JSON·중앙 검증·grant/readback·본인 MFA/권한/lock·Plan은 미완료. 준비 수용을 전체 IAM 승인으로 확대하지 않음 |
| CICD PR68 | HEAD `a466370ed9fcec724b4c5fe4f61f2e71f28d7298`, [하영 APPROVED](https://github.com/321Team/infra-cicd/pull/68#pullrequestreview-5451830074), merge `8658c332fb5803ca1e53d3b8aefc4d4da179fdf6` (14:47:36 KST). 동일 HEAD CI2 SUCCESS | 입력 진단만 구현. 실제 adapter/credential/API/배포 미연결. 실제 #38/#42/#43 입력 잔여 |
| #47→#50 작업창 | [이재환 계획](https://github.com/321Team/fds-project-baseline/issues/50#issuecomment-6051395052), [PMO/QA PARTIAL ACCEPT](https://github.com/321Team/fds-project-baseline/issues/50#issuecomment-6051518639) | 10/20 준비·10/21 H1 뒤 본시험·10/22 영향 회귀 구성 동의. 도구/장애 절차 보완 전 Runtime GO 없음. 시각은 실행 조건 미충족 시 자동 연기 |
| MSA PR24 시험 도구 | HEAD `85b20f45ba4e2a4b3afb55d1ab41c970938374ca`, [R1~R4 해소/APPROVED](https://github.com/321Team/fds-msa/pull/24#pullrequestreview-5452014671), 생산자 merge `6a95e1a5d7e7e25ac83694ca932ea1be65699053` (14:41:49 KST) | 코드 차단 해소. tool SHA 수신·바이트 대조 완료. 실제 Route/CA/fixture/criteria/H1·DB 입력과 B2 보완·Runtime 잔여 |
| #50 장애 패킷 | [B2 초안 6051891259](https://github.com/321Team/fds-project-baseline/issues/50#issuecomment-6051891259) 접수 | [이번 초안 검토](fault-packet-review.md)의 실행 전 보완 및 H1/Relay live 입력 필요 |
| #43 실패 경로 수신 | [D-03 수신 기록](https://github.com/321Team/fds-project-baseline/issues/43#issuecomment-6052024894): engine read timeout·오류 응답·DB 저장 실패 rollback/HTTP500, Owner 이재환·Due10/19 | ROSA 실제 원본 미수신. engine 0개/DB 경로 차단만으로 이 세 경우를 대체하지 않음. Phase1 Close 예외 승인으로 해석하지 않음 |

baseline PR152/153은 병합 완료다. 14:50 준비 기준 main은 baseline PR155 merge `b46e31e613de270db47cbd0699acf9a3a77c91c6`, Terraform `93d71500e3e881c55f1814cd144ca41f43e77f3d`, CICD `8658c332fb5803ca1e53d3b8aefc4d4da179fdf6`, MSA `6a95e1a5d7e7e25ac83694ca932ea1be65699053`. 후속 [병합 소스 무결성 기록](merged-source-receipt.json)은 최초 조회 기록과 분리한다. CICD의 별도 P1 후속 PR66/67을 이번에 수정·실행하지 않는다. 원 조회 메타데이터는 [sources](execution-update-sources.json)에 보존한다.

## 다음 권장 순서와 책임

1. 하영의 full IAM JSON/trust·source SHA·Action/Resource/Condition·AMI/PassRole/backend·회수 입력을 받아 중앙 변경 전 검증한다. 아직 없어 grant/Plan을 시도하지 않았다.
2. 병합된 Terraform 코드를 실행 후보로 대조하되 PR HEAD, merge SHA, 실행 수용 SHA/manifest를 구분한다. 자동으로 accepted_execution_sha를 채우지 않는다. Stream9 package-only 시험은 허용 호스트가 있으면 수행할 수 있으나 이번에 수행하지 않았다.
3. #38/#37/#40/#42/#43의 topology·관리/DB/Registry 경로·보안 계약을 #34에 취합한다. 실제 생성 후 ID/Agent Online/cold-pull을 생성 전 새 순환 Gate로 추가하지 않는다.
4. MSA PR24 R1~R4 해소·승인·병합 수신은 완료했다. 이재환의 B2 F1/F2 보완과 실제 시험 입력을 수신한다. 권욱은 [기존16case 실행 자료](test-execution-matrix.tsv)로 누락/원본/복구를 대조한다. 현재 모두 NOT_RUN이다.
5. CICD PR68 독립 승인·병합은 완료했다. 실제 P2 adapter 연결은 해당 입력·실행 계약과 검토 SHA를 고정해 진행한다. 입력 검사 RC0을 배포 승인으로 소비하지 않는다.

## 시험 실행 공통 Record

실행자는 한 세션·한 장애 원칙을 유지한다. 실행 직전에 대상 계정/host/cluster/namespace·권한·작업 경로·승인 범위·actual tool SHA·imageID·H1 revision·criteria와 CA SHA를 고정한다. 정보가 없으면 값을 합성하지 말고 해당 case를 NOT_RUN으로 유지한다.

각 case는 실행 start/end KST·단조 경과시간, 명령/RC·stdout/stderr, 기준/관측의 대상 UID·run/attempt·Transaction ID, DB schema/source, 원본 파일 해시, 종료 판정/잔여 Owner, 복구 전후·정리 결과를 연결한다. Secret은 reference만 기록한다. 비인가 접근 거부는 timeout 하나로 정상 DENY 판정하지 않는다.

`test-execution-matrix.tsv`는 기존 P2-PREP-01~16을 확장한 비실행 추적표다. 새 AC나 실행 결과가 아니다. 행 번호와 MSA 도구 그룹은 일대일이 아니며, 도구 밖의 SCC/Route·NP·장애·runtime imageID·Delivery 증적은 별도로 수집한다. 도구의 병합본/명령은 PR24 merge `6a95e1a5`와 수신한 tool SHA를 기준으로 하며 이번 표가 미리 실행을 승인하지 않는다.

## H1·작업창·재실행

10/20 준비, 10/21 A1~A7 전체 필수조건→H1→#50 정상/음성/장애, 10/22 영향 회귀 순서를 적용한다. H1에는 cluster/API/namespace/Route·두 앱 source/imageID, VPN route/selector/SG/source, DB 승인 source·pg_hba/firewalld/schema, 선택 Registry·D22/D23, A7 복구 거래, 원본·Known Issue가 필요하다. H1 실패나 남은 복구시간 부족 시 예약 시각만으로 다음 case를 시작하지 않는다.

같은 A7 원본→복구 거래→H1→#50 회귀를 재사용한다. 변경이 있으면 H1 revision과 영향 범위를 추가하고 DB/Probe/NP/Route/터널/장애 처리에 영향 받은 A7·장애 case도 재검증한다. 정상/음성만 재실행한 결과를 장애 회귀까지 완료했다고 표시하지 않는다. 재전송은 기존 ledger 우회나 같은 RUN 삭제로 하지 않고 새 승인 회차와 격리된 fixture를 사용한다.

## #43 D-03 수신의 시험 구분

| 수신한 실패 경로 | 연결 case / 반드시 구분할 증적 |
|---|---|
| engine read timeout | P2-PREP-03·11의 #43 수신 하위 관측. 실제 timeout 경로 원본, API fail-open 응답/DB 저장과 복구. engine 0개 결과만으로 완료 아님 |
| engine 오류 응답 | 동일 수신 관측에서 오류 응답 원본·API fail-open/DB 저장·복구. HTTP 오류와 timeout은 별도 표기 |
| DB 저장 실패 rollback/HTTP500 | P2-PREP-03의 #43 수신 하위 관측. 저장 시도 실패·HTTP500·트랜잭션 rollback/저장 없음 원본. `/readyz=503` 또는 연결 전 실패와 구분 |

이 세 경로의 안전한 재현 방식·정확한 승인 대상과 복구는 #43 생산자가 실행본으로 제출한다. 다른 환경의 승인·공유 DB 장애·운영 schema 변경을 여기서 추가 허용하지 않는다.

## 검증·한계

새 수행은 GitHub 원본/리뷰 변경 조회, 문서 정합 및 B2 초안 정적 검토, 표 형식/링크/민감정보 검사다. 서버·AWS·SSM·DB·ROSA 접속/변경, 새 장애주입, 기존 도구 MOCK 재실행은 하지 않았다. 발행 정본·Issue 본문/AC·날짜 필드는 변경하지 않으며 문서 복구는 해당 커밋 revert다.
