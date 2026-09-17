<!-- v19-collection-latest:start -->
## 최신 수집 — CICD 증적 입력 결함 수정·추가 독립 리뷰 요청

- [CICD PR19](https://github.com/321Team/infra-cicd/pull/19) HEAD **20474c3d671fa19f8a2c718d6d10d429cc190994**, parentdcdb36c. FIFO 입력에서 파일 종류 검사 전 멈추는 문제를 수정했습니다. expected/archive/receipt/payload4개 CLI 경로의 수정 전 timeout·수정 후 rc1/FAIL과 export 미생성을 확인했습니다.
- 로컬 delivery91 PASS·skip0, [CI35210784201](https://github.com/321Team/infra-cicd/actions/runs/35210784201)/Job105167523809 원본 **166 PASS(17+11+47+91), skip0, SOURCE_VALIDATION PASS**. 원격 변경3파일 바이트 일치.
- [리뷰 대응 자료](https://github.com/321Team/infra-cicd/blob/20474c3d671fa19f8a2c718d6d10d429cc190994/docs/reviews/pr-18-19-followup-20260917.md): #18 미검토 수집기/Podman/bridge/bundle/OCI, #19 Workflow·공급 소비·Build/Scan·증적·인계 파일의 추가 검토 범위를 구체화했습니다. #18 기존 CI128 PASS 확인; 이번 로컬52 PASS·1 SKIP(socket 제한)은 별도 표기.
- #13~#17 현재 HEAD 본인 확인·최종 의견 요청, #18·#19 추가 독립 리뷰 요청을 이재환(supreme33-kr)에게 재등록했습니다. #5 나머지 문서 범위 전달·기존 요청/Draft 유지, #3 Draft 유지. **리뷰 접수됨 / 사람 확인 PENDING / 작성자 검증으로 대체하지 않음 / 미병합**.
- [Issue11](https://github.com/321Team/infra-cicd/issues/11) 최신 기록 갱신. 앱 main254b822·최종 Source/실행 승인/API Unit 인계 없음, config PENDING 유지. 성공한 공급/base probe/로그인 Git 점검 반복 불필요.
- [수집 JSON](https://github.com/321Team/fds-project-baseline/blob/6903f6e752941bf32096919cf7fc4caeaab8f52e/audit/v3.1.19/intake/updates/20260917T103444Z.json) SHA256 `9e53512dcc2c6d446a90c6e7dd575bd92d80290a225e81d3b6277ee2c06fa575`; checksum **57개(기존56개 보존)**, 원격2파일 바이트 일치.
- **APP_TEST_BUILD_SCAN·Push·Deploy NOT_EXECUTED / Runtime AC1/10 / Delivery NOT_VERIFIED / Publication NOT_READY / 정본 docs-v3.1.18 유지**. 후보 canonical-integrity의 기존 startup_failure는 해결하지 않았습니다.
<!-- v19-collection-latest:end -->

---

## 직전 수집 — Runner 로그인 Git·공급 접근·시작 용량 PASS

- 사용자 제출 **2026-09-17 13:53:10 KST** 결과: cicd-runner01/server01_cicd-runner/UID1000, Git2.52.0, 명령7개 rc0·timeout없음 기록, 고정 관측 Commit254b822/tree6ee93b5 bare fetch **PASS**. 준비 실행본 SHAffb7bfde와 원격 바이트 대조 일치.
- archive2,267bytes SHA256 `8bcd7f5688bccf86e8c672e33a606d4edeed602e8e65ea3545d30091067a6338`. 외부 sidecar·내부 result checksum1/1·허용 파일2개·context/Commit/tree 대조 PASS. [수신 result 원문·checksum·검증 기록](https://github.com/321Team/fds-project-baseline/tree/57a97a82f1cf9c6a175bb2f35ca260bb1faae0d7/audit/v3.1.19/intake/p1-cicd-runner-git-20260917T045310Z).
- 공급4프로필 metadata12hash가 고정 입력과 일치하고 wheel 접근 기록25/29/18/26개. 원본 OCI/wheel 전체 hash·Build를 반복 검증한 결과는 아니다.
- 가용 **70.82GiB**, inode42,691,023으로 기존 앱 시작 하한4GiB 충족. 전체 실행 완료에 충분한 용량이라는 보장은 아니다.
- 원본 Git 로그는 미포함. 명령 결과는 제출 영수증과 로그 hash 대조이며 7개 raw log를 독립 열람한 것으로 확대하지 않는다. 로그인 환경의 관측 SHA 수신은 최종 앱 실행 승인·Actions Job PASS와 별개다.
- [CICD PR19](https://github.com/321Team/infra-cicd/pull/19) HEAD **dcdb36c0f09b28e7b2accc098e32c3dc41f6607c** 변경 없음. [Issue11](https://github.com/321Team/infra-cicd/issues/11) 갱신. 이재환 리뷰 요청 유지·리뷰0건·미병합, 앱 main254b822·신규 최종 인계 없음. 성공한 이번 점검 재실행은 불필요하다.
- [수집 JSON](https://github.com/321Team/fds-project-baseline/blob/57a97a82f1cf9c6a175bb2f35ca260bb1faae0d7/audit/v3.1.19/intake/updates/20260917T045925Z.json) SHA256 `d317975b6e3ab880144fa9ad64199bac68984610b732ef6e07fd2d6eb9c093c9`; INTAKE_SHA256SUMS **56개(기존52개 보존)**, 원격5파일 바이트 일치.
- **RUNNER_GIT_PREFLIGHT PASS_SUBMITTED_RECEIPT / 기존 SUPPLY·BASE_PROBE Runtime PASS 유지 / APP_TEST_BUILD_SCAN NOT_EXECUTED / Runtime AC1/10 / Delivery NOT_VERIFIED / Publication NOT_READY / 정본 docs-v3.1.18 유지**. 최종 pin/lock Source SHA·승인·API Unit 인계 → config 대조 → 최신 독립 리뷰/main 반영 → 중앙 수동 앱 실행이 남는다. 후보의 기존 canonical-integrity startup_failure 해결을 주장하지 않는다.

---

## 직전 수집 — Runner Git·공급 접근·용량 선행점검 실행본 준비

- [CICD PR19](https://github.com/321Team/infra-cicd/pull/19) HEAD **dcdb36c0f09b28e7b2accc098e32c3dc41f6607c**, parentdcf9fa2. 새 단일 Python 점검기·11개 시험·[서버 실행 문서](https://github.com/321Team/infra-cicd/blob/dcdb36c0f09b28e7b2accc098e32c3dc41f6607c/docs/runner-git-preflight.md)3파일 추가. 고정 관측 앱 Commit254b822/tree6ee93b5의 로그인 계정 bare HTTPS fetch와 공급 metadata12hash·원본 읽기 접근·bytes/inode 관측이다.
- 실행본 runner_git_preflight_20260917.py, **13,419bytes**, SHA256 `ffb7bfde5f122a664fe45d21bae362f32a0499724a5f1e6798aaa2f12c0f3c61`. 새 실행 디렉터리만 쓰고 result JSON+checksum을 회수한다. 원본 로그/Source는 서버에 보존한다. 기존 공급/Podman/CA/네트워크/서비스/권한은 변경하지 않는다.
- [CI35181778429](https://github.com/321Team/infra-cicd/actions/runs/35181778429)/Job105075286245 원본 **165 PASS(17+11+47+90)**·skip0·SOURCE_VALIDATION PASS, 대상 HEAD/merge805d831 확인. 원격3파일 byte일치. 로컬 신규11시험은 실제 fixture Git을 이용하며 Runner 네트워크 성공과 구분한다.
- **RUNNER_GIT_PREFLIGHT Runtime NOT_EXECUTED**. 사용자 서버 결과 수신 후 판정한다. 관측 SHA 수신은 앱 승인이나 Actions Job 성공이 아니다. 이재환 최신 리뷰 요청 재등록. 앱 최종 pin/lock Source SHA·승인·API Unit 인계/최신 독립 리뷰/main 반영 조건 유지.
- [수집 JSON](https://github.com/321Team/fds-project-baseline/blob/c5b900c1d8c7a810700685949bf71edbafe1245c/audit/v3.1.19/intake/updates/20260917T042656Z.json), SHA256 `4069edbcfd400092a65e1e274a26b71ddb30e976b4ac47d084dec04001605963`; INTAKE_SHA256SUMS **52개(기존51개 보존)**, remote2파일 byte일치. [Issue11](https://github.com/321Team/infra-cicd/issues/11)에 준비/미실행 경계 기록.
- **기존 공급/base probe Runtime PASS 유지 / APP_TEST_BUILD_SCAN NOT_EXECUTED / Runtime AC1/10 / Delivery NOT_VERIFIED / Publication NOT_READY / 정본 docs-v3.1.18 유지**. 후보 기존 canonical-integrity startup_failure 해결을 주장하지 않는다.

---

## 직전 수집 — 앱 증적 도구 준비·PR #5 충돌 해소

- [CICD PR #19](https://github.com/321Team/infra-cicd/pull/19) HEAD **dcf9fa232f0f4ec5f347dc5dc67a02668664d20b**. 앱 종료 영수증 회수·수신 대조 도구, 외부 Run/Attempt/Source/config 기준 양식, 원본 보존·허용 JSON/hash 목록 export, 압축 해제 전체 크기 제한 준비. 증적 검사 PASS와 앱 PASS/BLOCK/FAIL 및 독립 리뷰를 구분한다. 실제 앱 실행은 아직 없다.
- [CI35180034060](https://github.com/321Team/infra-cicd/actions/runs/35180034060)/Job105069978424 원본 **154 PASS(17+11+47+79)**·skip0·SOURCE_VALIDATION PASS, 대상 HEAD 확인. 신규 증적15개 시험은 합성 실행 영수증/임시 OCI·tar 바이트 기반이다. 수신 archive에는 raw 로그·이미지·DB·report를 포함하지 않아 수신자가 원본 실행을 독립 재검사한 증거로 확대하지 않는다.
- [PR #5](https://github.com/321Team/infra-cicd/pull/5) HEAD **6715fe58801c217b2ed7bc1221241eb134b88e05**, 기존 PR0c3f01b/main90f2f37의 실제 두 부모 merge로 충돌 해소. main의 실행 코드·Workflow를 보존하고 문서/설명 config9파일만 변경. 09-15 관측과 이후 Runner DB/공급/base probe PASS를 분리했다. [CI35179805539](https://github.com/321Team/infra-cicd/actions/runs/35179805539)/Job105069311205 **97 PASS**·mergeable=true·Draft 유지.
- 두 PR 모두 이재환(supreme33-kr) 최신 리뷰 요청 재등록, 제출 리뷰0건·미병합. 앱 main254b822 변경 없음. 최종 pin/lock Source SHA·승인·API Unit 범위 인계 → config 대조 → 최신 독립 리뷰/main 반영 → 중앙 수동 Runtime 실행·증적 회수 순서다.
- [수집 JSON](https://github.com/321Team/fds-project-baseline/blob/708523d5b6903db06a0df5d1593b739eb0db9987/audit/v3.1.19/intake/updates/20260917T035902Z.json) SHA256 `b467d7a62c7cee92ee8071dc0a99c6ebcd40bd80c07b9c95dd868b178e4b13f3`. INTAKE_SHA256SUMS **51개(기존50개 보존)**, 원격 바이트 대조 완료. [Issue #11](https://github.com/321Team/infra-cicd/issues/11)에 결과 기록.
- **SUPPLY_RUNTIME PASS / BASE_PROBE_RUNTIME PASS 유지 / APP_TEST_BUILD_SCAN NOT_EXECUTED / Runtime AC1/10 / DELIVERY_GATE NOT_VERIFIED / Publication NOT READY / 정본 docs-v3.1.18 유지**. main·서버 자원 변경은 없으며 후보의 기존 CI startup_failure 원인 해결을 주장하지 않는다. 이번 HEAD의 [canonical-integrity Run35180227039](https://github.com/321Team/fds-project-baseline/actions/runs/35180227039)도 **startup_failure**로 종료됐다. CICD 두 PR의 소스 CI 성공과 구분하며 후보 발행 준비 완료로 판정하지 않는다.

---

## 직전 수집 — 앱 반영용 검증 patch·최종 인계 양식 준비

- [CICD PR19](https://github.com/321Team/infra-cicd/pull/19) HEAD **9dce4e59d2341affdbf94928bbeea7a20d7f2514**. 이번 변경은 인계 문서/patch4파일이며 실행기·Workflow·config는 그대로다.
- 현재 앱 main254b822·신규 인계 없음, CICD 제출 리뷰/일반/인라인댓글0건. 앱 repo의 현재 연결 계정 권한은 **pull=true/push=false**이므로 앱 브랜치/PR 직접 반영 대신 [단일 패치와 회신 양식](https://github.com/321Team/infra-cicd/tree/9dce4e59d2341affdbf94928bbeea7a20d7f2514/handoff/offline-app-20260917)을 준비했다.
- patch12,492bytes SHA256 `eee3869cb0135769d7da2f3929455aa46ac19b8e185b5770b4cf6e00b782bb02`. 원본6파일 Git blob/requirements4 hash 일치, 격리 Git apply-check/적용·후보6파일 바이트 일치·requirements4 불변·중복 적용 차단·역적용 원상복귀·다른 Dockerfile 기준 차단 PASS. 앱 실제 저장소나 Runtime을 변경한 검증은 아니다.
- [CI35178136350](https://github.com/321Team/infra-cicd/actions/runs/35178136350)/Job105064283285 원본 **139 PASS(17+11+47+64)**·skip0·SOURCE_VALIDATION PASS, merge f6a21b1의 대상 HEAD 확인. 원격 변경4파일 바이트 일치.
- [수집 JSON](https://github.com/321Team/fds-project-baseline/blob/31aa9a103f5317ed49ae8ebe13fcf881b33f7317/audit/v3.1.19/intake/updates/20260917T032700Z.json), SHA256 `a140944176cec391be77510c23a12499558c80b8f4ff0468ccf71dcec7e83910`; INTAKE_SHA256SUMS **50개(기존49개 보존)**. [Issue11](https://github.com/321Team/infra-cicd/issues/11) 기록 갱신.
- 앱 담당이 patch 검토/반영 후 최종40자리 SHA·실행 승인·API Unit 범위를 회신하고, CICD 담당이 실제값 config 대조·최신 전체 리뷰/main 병합 후 중앙 수동 Runtime을 수행한다. 리뷰 요청은 이재환 유지.
- **SUPPLY_RUNTIME PASS / BASE_PROBE Runtime PASS 유지 / APP_TEST_BUILD_SCAN NOT_EXECUTED / Runtime AC1/10 / DELIVERY_GATE NOT_VERIFIED / Publication NOT READY / 정본v3.1.18 유지**. 후보의 기존 CI startup_failure 해결을 주장하지 않는다.

---

## 직전 수집 — CICD 중앙 Workflow·Source 인수 준비 및 CI139 PASS

- 사용자 선행작업 지시에 따라 [infra-cicd PR19](https://github.com/321Team/infra-cicd/pull/19) HEAD **65d2cc8aca147b0b9929905b27c7189becd4cbc8**로 갱신. main/workflow_dispatch 전용 중앙 Workflow, 고정40자리 SHA의 익명 HTTPS bare Git 인수, 최종 Dockerfile2·lock4·기존 requirements4개 검사와 기존 Test→Build→Scan 호출을 연결했다.
- 로컬 **139 PASS(17+11+47+64)**, 새17개 시험. [CI35177513645](https://github.com/321Team/infra-cicd/actions/runs/35177513645)/Job105062360112 원본 **139 PASS·skip0·SOURCE_VALIDATION PASS**, 실제 대상 HEAD/merge 확인. 원격 변경6파일 바이트 일치. Git transport 시험은 로컬 fixture이고 앱 Runtime과 구분한다.
- 기존 config는 PENDING_APP_HANDOFF·승인값null·API Unit null 유지. 우리 구현 준비는 완료됐으며 앱 담당의 최종 pin/lock Source SHA·시험 범위 인계, 해당 config 포함 최신 독립 리뷰·main 병합, 중앙 Workflow의 실제 실행이 남는다. 이재환 리뷰 요청 재등록·제출 리뷰0건·미병합.
- 앱 repo 현재 public을 확인해 앱 Token 없는 읽기를 구현했으며 공개 설정 변경/승인은 아니다. Private SCM 목표와 차이를 남기고 Private 전환 시 별도 읽기 전용 인증을 요구한다. 실제 Runner GitHub fetch는 아직 미검증이다.
- [수집 기록](https://github.com/321Team/fds-project-baseline/blob/0f788a7f29e24d03222409cd043871099743a62a/audit/v3.1.19/intake/updates/20260917T031805Z.json) SHA256 `674bd481197f9af6afbe5c4c7c1b6bbc0e2508081537b9962acb54908dc73c09`. INTAKE_SHA256SUMS **49개(기존48개 보존)**. [Issue11](https://github.com/321Team/infra-cicd/issues/11)·[구현/실행 경계](https://github.com/321Team/infra-cicd/blob/65d2cc8aca147b0b9929905b27c7189becd4cbc8/docs/app-workflow.md).
- **SUPPLY_RUNTIME PASS / BASE_PROBE Runtime PASS 유지 / APP_TEST_BUILD_SCAN NOT_EXECUTED / Runtime AC1/10 / DELIVERY_GATE NOT_VERIFIED / Publication NOT READY / 정본v3.1.18 유지.** 새 운영 dispatch·Push/Deploy·main/Release 변경 없음. 후보의 기존 CI startup_failure 원인 해결을 주장하지 않는다.


---

## 직전 수집 — 고정 digest 조회·최소 Build Runtime PASS

- 사용자 제출 probe 증적: **2026-09-17 11:41:25~30 KST, 약4.52초**, archive5,158bytes SHA256 `db6c4a18857aa5ecb1f9a923888268193d7653932b9b0eeb0174116fe07f7831`. 외부sidecar·내부7개 checksum·일반파일8개·명령6개 rc0/로그 hash/argv/시간 순서 대조 PASS.
- 기존 cefcaeaa 번들의 절대경로 재개로 공급 복사 검사 → 새 rootless VFS store load/tag → **repository@manifest 직접 조회** → 고정 digest FROM의 Python 최소 Build 성공. RepoDigests·config ID·RootFS4개·linux/amd64·Build COMMIT ID 정합 확인.
- **해소:** 새 CI 저장소의 repository@digest 해석과 최소 base Build Runtime 차단. 앱 전체 Test/Build/Scan 성공으로 확대하지 않는다. 실제 실행 Source cefcaeaa와 코드 수정602e376/CI122 PASS는 구분한다.
- [제출 원본8파일과 설명](https://github.com/321Team/fds-project-baseline/tree/90d914f8c3efc7aa5e8416654e053fd987fe8b47/audit/v3.1.19/intake/p1-cicd-offline-probe-20260917T024125Z) · [검증 수집 JSON](https://github.com/321Team/fds-project-baseline/blob/90d914f8c3efc7aa5e8416654e053fd987fe8b47/audit/v3.1.19/intake/updates/20260917T024654Z.json) · [Issue11](https://github.com/321Team/infra-cicd/issues/11). INTAKE_SHA256SUMS48개(기존38개 보존), 원본 OCI/wheel/probe image는 서버에 있다.
- **남은 작업:** 앱 담당 최종 pin/lock SHA·API Unit 범위/승인, CICD 최신 독립 리뷰, 승인 main/중앙 수동 Workflow·읽기 전용 checkout 연결, 실제 앱 Test→Build→Scan. PR19 HEAD602e376 변경 없음·이재환 요청·리뷰0건·미병합. 앱 main254b822 유지.
- **SUPPLY_RUNTIME PASS / OFFLINE_PROBE Runtime PASS(제출 증적 기준) / APP_TEST_BUILD_SCAN NOT_EXECUTED / Runtime AC1/10 / DELIVERY_GATE NOT_VERIFIED / Publication NOT READY / 정본v3.1.18 유지**. 기존 probe 초기 실패는 이력으로 보존하며 성공한 수집/probe 반복은 필요하지 않다. 후보 CI의 기존 startup_failure 원인은 별도 미확인이다.


---

## 직전 수집 — probe 상대경로 오류 수정·재개 안내

- 기존 probe는 사용자 화면에서 파일 SHA검사 성공 후 준비 단계 FAIL, EVIDENCE_DIR 미출력이다. `./bundle.pyz` 실행 시 Path 정규화로 zipimport prefix가 달라지는 입력 읽기 결함을 재현했다.
- [CICD PR19](https://github.com/321Team/infra-cicd/pull/19) HEAD `602e376adb321190f9143c5358afd5c31ec7d7a9`: prefix 보존·오류 단계 표시·실제 번들의 ./상대/상대/절대 경로 입력 hash 회귀시험 추가. [CI35175073989](https://github.com/321Team/infra-cicd/actions/runs/35175073989)/Job105054876044 원본 **122 PASS(17+11+47+47)**, 변경2파일 원격 바이트 일치.
- 기존 SHA082d800b... 번들은 **절대경로 명령**으로 내장 입력 읽기 통과를 확인하고 재개 안내했다. 수정 번들 `offline_probe_602e376.pyz` SHA256 `47568a505023ada5aae749fdf24c914e9f8e6714ccec28922becd4673c7cd6fa`도 준비했다. 실제 서버 전체 probe 성공 결과는 아직 미수신이다.
- [수집 JSON](https://github.com/321Team/fds-project-baseline/blob/608be6356e836eeb14f1e1dc9e0fc238d82d720c/audit/v3.1.19/intake/updates/20260917T023956Z.json): screenshot SHA·기존/수정 번들·원인 재현·출처 본문 hash·CI·미검증 범위를 기록했다. INTAKE_SHA256SUMS38개, 이전37개 보존.
- 이재환 리뷰 요청 유지·최신 코드 리뷰0건·미병합. **SUPPLY_RUNTIME 기존 PASS / OFFLINE_PROBE 최초 FAIL·재개 결과 미수신 / 앱 Test-Build-Scan NOT_EXECUTED / Runtime AC1/10 / DELIVERY_GATE NOT_VERIFIED / Publication NOT READY / 운영 정본v3.1.18 유지**. 후보 CI의 기존 startup_failure 원인은 여전히 미확인이다.


---

## 직전 수집 — 2026-09-17 오프라인 소비 PR19·PR3/5 리뷰 인계

- [CICD PR19](https://github.com/321Team/infra-cicd/pull/19) HEAD `cefcaeaa74f6bb96de4df1d5bf915f2b00ebf24f`: 실행별 OCI/wheel 복사 검사·repository@manifest 조회·오프라인 host 설치/runtime wheel Build context·기존 Scan 연결 코드 준비.
- [CI35173303483](https://github.com/321Team/infra-cicd/actions/runs/35173303483) / Job105049421327 원본 로그 **121 PASS(17+11+47+46)**, 실제 대상 HEAD·SOURCE_VALIDATION 확인. 새20개 시험에는 실제 합성 wheel offline pip 설치 포함; Podman/Trivy는 대역.
- 실서버 공급 소비 probe `offline_probe_cefcaea.pyz` SHA256 `082d800be1b3e368809eb61349a1a66905da59a743607d8cf175a0c859a412e4` 준비. 실행 결과 미수신이며 앱 실행 승인과 별개다. [앱 Dockerfile2개·원본 lock4개 인계 후보](https://github.com/321Team/infra-cicd/tree/cefcaeaa74f6bb96de4df1d5bf915f2b00ebf24f/handoff/offline-app-20260917).
- PR3/5는 전체 이관 근거가 없어 유지했다. 각 PR에 부분 인계·잔여 범위를 기록하고 이재환 리뷰어 등록. PR19도 이재환 요청 확인; 신규 코드 리뷰0건·미병합.
- [이번 수집 JSON](https://github.com/321Team/fds-project-baseline/blob/a22877701be70c3ef3de688f4cee893326757718/audit/v3.1.19/intake/updates/20260917T021343Z.json): 원본 출처/본문 hash4건, 코드 hash15건, CI·번들·이전/이후 상태를 기록했다. INTAKE_SHA256SUMS37건(기존36건 보존), 기존 공급 증적/인계 파일 유지.
- **실행 조건:** 실서버 digest probe → 앱 pin/lock 최종 SHA·Unit 범위/승인 → 최신 CICD 독립 리뷰·승인 main/중앙 Workflow 연결 → 실제 앱 Test→Build→Scan. 기존 공급 collect는 재실행하지 않는다.
- **SUPPLY_RUNTIME PASS 유지 / OFFLINE_PROBE 결과 미수신 / APP_TEST_BUILD_SCAN NOT_EXECUTED / Runtime AC1/10 / DELIVERY_GATE NOT_VERIFIED / Publication NOT READY / 운영 정본v3.1.18 유지.** 후보의 기존 canonical-integrity startup_failure 원인은 미확인이다.


---

## 직전 수집 — 2026-09-17 CICD 공급 Runtime PASS·앱 인계 후보 보존

- 사용자 제출 공급 증적: 실행 **10:07:57~10:09:09 KST(약71.8초)**, archive SHA256 `6ae2fe28d2ab8eef0d4cf2e92a48b469b7a60fed3b59b8070461e61db2367403`, 외부sidecar·내부59개 checksum·일반 파일60개 MATCH.
- 고정 layer4개 서버 hash/size/DiffID 검사, Podman load/inspect identity, native target4개 offline install/pip check 및22개 명령 rc0를 대조했다. API runtime25/test29, engine runtime18/test26, 총98 profile 항목·중복 제외29 wheel.
- roots/lock/inventory·다운로드 영수증 hash·대상 tag·실제 설치 로그 정합 PASS. 67개 요청은 승인03의5개 host와10:07:59~11:07:59 KST 작업창 안에 기록됐다.
- [앱 인계 후보12파일 및 안내](https://github.com/321Team/fds-project-baseline/tree/7636a609989a91d6f107353b199ebe0857396132/audit/v3.1.19/intake/p1-cicd-supply-20260917T010757Z) · [검증 수집 JSON](https://github.com/321Team/fds-project-baseline/blob/7636a609989a91d6f107353b199ebe0857396132/audit/v3.1.19/intake/updates/20260917T012302Z.json) · [Issue11](https://github.com/321Team/infra-cicd/issues/11). 원본12파일 바이트 보존, INTAKE_SHA256SUMS36건(기존22건 보존).
- **남은 연결:** RepoDigests/RepoTags 비어 있음; 각 CI storage의 repository@manifest 해석, offline build_scan/앱 Dockerfile 연결, 앱 최종 Source 승인·독립 리뷰·실제 Test/Build/Scan.
- 큰 OCI/wheel은 서버에 남아 있고 Codex에는 미제출이다. 서버 수집기의 기록과 제출 로그를 검증했으며 패킷/방화벽 독립 증명은 아니다. 원본 archive의 GitHub evidence 편입 NOT_INGESTED.
- PR18 코드 HEAD73db58f·CI128 PASS 유지, 리뷰0건·미병합. **SUPPLY_RUNTIME PASS(제출 증적 검증) / APP_TEST_BUILD_SCAN NOT_EXECUTED / DELIVERY_GATE NOT_VERIFIED / Runtime AC1/10 / v19 Publication NOT READY / 운영 정본v3.1.18 유지.**


---

## 직전 수집 — 2026-09-17 P1-CICD config Runtime·전체 metadata 대조 PASS

- 실제 수집 증적: 06:25:26~27 KST, auth200→registry 고정 config307→승인 CDN200, 5,664 bytes 수신. 승인02 작업창06:25:26~06:40:26 KST 내 완료, **COLLECTION=PASS**. archive3,263 bytes SHA-256 `5b70aa9316e42fc73b7eb1132005ce9cb67ff322c7019a673c4d1b1438c9e27a`, 외부·내부 checksum/수집기 Source 일치.
- 기존 index·manifest와 합쳐 PR16 고정 HEAD `fb1493b4ef19686a2d050a5f14daad27e7cb3362`에서 Codex 오프라인 검사 **BASE_MANIFEST_CHECK=PASS**. linux/amd64, digest/size/mediaType·4개 layer descriptor/rootfs diff_ids 형식 연결 확인. layer bytes는 미수신·미검증입니다.
- [Issue11 인계안](https://github.com/321Team/infra-cicd/issues/11)에 두 Dockerfile의 FROM 수정 후보를 기록했습니다. 최신 앱 main254b822는 아직 가변 태그이며 **pin 변경·최종 Source 승인·이미지/의존성 공급 확정**이 남았습니다. 이번 metadata 승인을 Build/PyPI 접속으로 확대하지 않습니다.
- PR16·17 HEAD 변경 없음, 이재환 리뷰 요청 유지·리뷰0건·미병합. 수집 당시 BASE_MANIFEST_CHECK=NOT_EXECUTED 및 최초 부분 수집 FAIL은 원본대로 보존하고 후속 검증 PASS를 분리합니다.
- [새 수집 JSON](https://github.com/321Team/fds-project-baseline/blob/f7491ee49d401faa92cac147420e98ccc1fe3d4e/audit/v3.1.19/intake/updates/20260916T213204Z.json) · Manifest20개, 기존19개 hash 보존. 원본 archive의 GitHub evidence 편입은 NOT_INGESTED이며 식별값·검증 결과를 수집했습니다.
- **Runtime AC1/10·IMAGE_SCAN NOT_EXECUTED·전체 Delivery NOT_VERIFIED / v19 Publication NOT READY / 운영 정본v3.1.18 유지**.

---

## 직전 수집 — 2026-09-17 P1-CICD config 보완 범위 채택

- 사용자 이권욱의 **“권장안으로 채택 후 수행”**에 따라 직전 CDN 제안을 **APPROVED_INPUT / ADOPTED_BY_USER**로 수집했습니다. 같은 Runner .20·이권욱, auth/registry와 production.cloudfront.docker.com:443, 기존 관측 config digest 한 개(5,664 bytes), 첫 실제 보완 실행부터 최대15분입니다.
- 기존 index·manifest와60분 기록은 보존합니다. registry307→정확한 HTTPS CDN의1회 redirect, Bearer token 비전달·추가 redirect 중단. layer/PyPI/Build/Scan/Push/Deploy·네트워크 정책 변경은 제외합니다.
- [infra-cicd PR #17](https://github.com/321Team/infra-cicd/pull/17) HEAD `8c3a4d32a799ede50cded2af50a571b3371374cf`, 로컬47 PASS / [GitHub-hosted CI122 PASS](https://github.com/321Team/infra-cicd/actions/runs/35150466858), 원격3파일 바이트 대조 완료. 이재환 리뷰 요청 유지·독립 리뷰0건·미병합.
- [채택·실행 안내](https://github.com/321Team/infra-cicd/issues/11) · [수집 JSON](https://github.com/321Team/fds-project-baseline/blob/2c6fd117c76f334f1aaef7fbcb3da56756ec8e41/audit/v3.1.19/intake/updates/20260916T210814Z.json). Manifest19개, 기존18개 hash 보존. 직전 캡처의 PENDING_USER_ADOPTION은 당시 상태이며 본 수집이 후속 채택을 기록합니다.
- 보완 Runtime **NOT_EXECUTED**, T1/만료 아직 미생성, config 원본 미수신. 최초 부분 수집의 FAIL/REDIRECT_STOPPED는 유지하며 이후 PR16 전체 검증이 필요합니다.
- **Runtime AC1/10·전체 Delivery NOT_VERIFIED / v19 Publication NOT READY / 운영 정본v3.1.18 유지**.

---

## 직전 수집 — 2026-09-17 P1-CICD 실제 metadata 부분 수집

- 05:39:10~13 KST 실제 Runner 수집: auth/index/linux-amd64 manifest HTTP200, config HTTP307에서 production.cloudfront.docker.com 이동을 차단했습니다. **PARTIAL_COLLECTION / CONFIG_REDIRECT_BLOCKED**, 전체 base 검증은 config 미수신으로 미완료입니다.
- 원본 archive3,167 bytes SHA-256902b84c2…9f3bebf, 외부·내부 체크섬/배포 Source 및 index→manifest digest·size·mediaType 연결 일치. 실제 작업창05:39:10~06:39:10 KST 확인. 기존 원본 재사용, layer bytes/앱 실행/Delivery 미검증 유지.
- 고정 config5,664 bytes 보완을 위한 CDN 한 host·단발 최대15분 제안은 **PENDING_USER_ADOPTION**입니다. 기존 작업창을 자동 연장하거나 새 목적지를 승인으로 처리하지 않습니다.
- [원본 식별값·판정·구체적인 후속 범위](https://github.com/321Team/infra-cicd/issues/11) · [수집 JSON](https://github.com/321Team/fds-project-baseline/blob/df620634088f2e42b90ef07217a03b79ae09c4e3/audit/v3.1.19/intake/updates/20260916T204604Z.json). Manifest18개, 기존17개 hash 보존.
- PR17 코드HEAD1fb5ef3·기존CI111·리뷰 대기와 분리합니다. **Runtime AC1/10·전체 Delivery NOT_VERIFIED / v19 Publication NOT READY / 운영 정본v3.1.18 유지**.

---

## 직전 수집 — 2026-09-17 P1-CICD OID-03 metadata 공급 범위 채택

- 사용자 이권욱의 “착수” 지시로 Runner .20 → auth.docker.io/registry-1.docker.io:443, library/python:3.12-slim index·linux/amd64 manifest·config 원본 수집, **실제 첫 실행부터 최대60분**을 APPROVED_INPUT / ADOPTED_BY_USER로 수집했습니다. 실제 작업창 시각은 아직 생성하지 않았습니다.
- 기존 resolver·mgmt-gw01 경로, TLS 검증, 모든 redirect/오류/만료에서 중단. DNS/NAT/방화벽 변경·.56 프록시 재사용·layer/PyPI 공급 확대는 포함하지 않습니다. 클라이언트 제한을 실제 방화벽 집행 증적으로 대신하지 않습니다.
- [infra-cicd PR #17](https://github.com/321Team/infra-cicd/pull/17) HEAD1fb5ef3, 신규14+기존Delivery22 로컬36 PASS / GitHub-hosted CI111 PASS. 이재환 독립 리뷰 요청 등록·미병합. 실제 registry 수집은 NOT_EXECUTED입니다.
- 사용자 04:07:56 KST 화면의 홈 UID1000/0700/접근, 기존 CICD service active/running, 기본 경로·도구 버전을 인수했습니다. 홈 전체 복원·신규 Job 수신·앱 Runtime으로 확대하지 않습니다.
- [수집 문서](https://github.com/321Team/fds-project-baseline/blob/910b157b4b819a8dfef0d5ad00a9ef16c7c7318a/audit/v3.1.19/intake/p1-cicd-base-metadata-supply-20260917.md) · [수집 JSON](https://github.com/321Team/fds-project-baseline/blob/910b157b4b819a8dfef0d5ad00a9ef16c7c7318a/audit/v3.1.19/intake/updates/20260916T200949Z.json). Manifest17개, 기존15개 hash 보존.
- **v19 전체 묶음 NOT BUILT / Publication NOT READY / 운영 정본 v3.1.18 유지**. Runtime AC1/10·전체 Delivery NOT_VERIFIED 유지.

---

## 직전 수집 — 2026-09-16 CP1 인수 연계 준비 보완

- 기존 사용자 채택 절차의 후속으로 배포 인수 양식의 오래된 생산자 pin을 수정했습니다. [infra 변경 ed53205](https://github.com/321Team/infra-kubernetes/commit/ed53205fb142c86715281cbe4eca6a44b0171c90): 양식·runbook·source manifest·회귀시험과 영수증 연계 명세.
- 변경 전 양식 불일치를 재현했고 관련 2개 시험 파일 **61/61 STATIC/MOCK PASS**. 미검증 양식·구 source 거부 유지, Runtime 실행 코드·정책·원 영수증·상태 비교 변경 없음.
- 원 CP1 영수증 → 새 변경 before/after → 실제 인수 → 후속 소비자 및 만료/회수 명세를 묶었습니다. 새 운영 규칙·보호·유지 기간·회수 종료 상태와 이에 맞는 소비자 구현은 남아 있습니다.
- 제한 진단의 2개 /32·TCP8080·20분·같은 창 완전 회수를 운영 허용으로 전용하지 않습니다. 추가 VM 시험·반입·증적 업로드 요청 없이 기존 자료를 재사용합니다.
- [수집 문서](https://github.com/321Team/fds-project-baseline/blob/48b8d836e74a723ea145360f63456de0d4183f96/audit/v3.1.19/intake/icr-cni-simplification-20260916.md) · [수집 JSON](https://github.com/321Team/fds-project-baseline/blob/48b8d836e74a723ea145360f63456de0d4183f96/audit/v3.1.19/intake/updates/20260916T145056Z.json). Manifest 15개 항목, 기존 비대상 12개 해시 유지.
- 분류는 **PREPARATION_FIX_IMPLEMENTED / OPERATIONAL_SCOPE_PENDING**입니다. 기존 절차 채택 APPROVED_INPUT_WORKFLOW_ONLY는 유지하되 새 실행 승인으로 확대하지 않습니다.
- HEP/GNP는 기존 Lead 입력대로 6/6 Ready 이후 별도 실행창, NTP control01 upstream 미정 유지. **v19 전체 묶음 NOT BUILT / 발행 NOT READY / 운영 정본 v3.1.18 유지**. Runtime 인수·AC·Gate 상향 없음.

---

## 직전 수집 — 2026-09-16 P1-K8S / P1-MON Lead 결정 입력

- 사용자 요청에 따라 [P1-K8S-01 #10](https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-5697547621), [ICR #14](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5697384866), [P1-MON #17](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-5696869601), [infra-kubernetes PR #7](https://github.com/321Team/infra-kubernetes/pull/7)의 최신 의견을 대조했습니다.
- **APPROVED_INPUT:** OID-01=`ansible01 10.250.10.10/32 + svc_ansible`, 내부 SNAT 금지/기존 Return Route 유지, HEP Runtime은 6/6 Ready 이후 별도 승인.
- **APPROVED_INPUT:** Monitoring designated Storage Worker=`k8s-worker03(.108)`, `/home/fds-local-pv/{prometheus,grafana,alertmanager}`, static local PV의 `no-provisioner + WaitForFirstConsumer + Retain + PV nodeAffinity` 유지.
- **APPROVED_CONFIG_DEFAULT:** PVC `Prometheus 20Gi / Grafana 5Gi / Alertmanager 2Gi`, Prometheus 15d 목표와 `retention.size<=16GB`. 사용률 증적에 따라 조정 가능한 초기값입니다.
- 사용자 제출 worker03 자료의 SHA-256은 `d7bef0ef1c413dd7e85a221fe8db1563de2b48f2aae4bf4a0e23b812df12287a`, `/home` XFS 가용 약 163G입니다. 아직 GitHub evidence archive에 편입된 원본으로 표현하지 않습니다.
- **NTP:** Lead가 `control01` 단일 내부 chronyd, UDP/123, offset<=100ms, 60초×6, sync lost>=5m FAIL, reboot<=5m 재동기화를 선택했습니다. 다만 control01 자체 upstream/time authority가 결정 원문에 없어 `APPROVED_DECISION / INPUT_INCOMPLETE / RUNTIME_HOLD`로 수집합니다. dns01/dns02 Relay 제안은 현 범위에서 기각됐습니다.
- Worker `ens160`은 별도 의견이 존재하지만 K8S/SEC Lead #10 최종 결정에 NIC 값이 포함되지 않아 `AS_BUILT_CANDIDATE / OWNER_CONFIRMATION_PENDING`으로 한정합니다.
- [후보 입력 문서](https://github.com/321Team/fds-project-baseline/blob/release/v3.1.19/audit/v3.1.19/intake/p1-k8s-mon-lead-inputs-20260916.md), [수집 JSON](https://github.com/321Team/fds-project-baseline/blob/release/v3.1.19/audit/v3.1.19/intake/updates/20260916T123819Z.json), `INTAKE_SHA256SUMS` 갱신 완료.
- **infra-kubernetes PR #7 구현은 승인 입력과 분리해 PENDING_REVIEW 유지.** DNS `.52/.53` 제한, 9091/9090 계약 복귀, Grafana port-forward-only 복귀, Storage 객체 추가는 확인했지만 기존 SEC-01/02/07/08 오류 경로와 최신 NTP 정책 반영/독립 리뷰/Runtime은 별도 해소가 필요합니다.
- **v19 전체 묶음 NOT BUILT / 발행 NOT READY / 운영 정본 v3.1.18 유지.**


---

## 직전 수집 — 2026-09-16 P1-CICD Trivy 운영안

- 사용자 채택 Trivy 운영안을 **APPROVED_INPUT / ADOPTED_BY_USER**로 수집했습니다.
- 바이너리 버전·SHA-256 고정, 실제 이미지 Scan 전 DB 준비/유효성 검사, HIGH/CRITICAL 및 스캐너/DB 오류 Push·Deploy 차단을 유지합니다.
- [운영안 상세](https://github.com/321Team/fds-project-baseline/blob/release/v3.1.19/audit/v3.1.19/intake/p1-cicd-trivy-update-policy-20260916.md), [수집 JSON](https://github.com/321Team/fds-project-baseline/blob/release/v3.1.19/audit/v3.1.19/intake/updates/20260916T033933Z.json).
- DB 준비 Runtime PASS와 실제 앱 Delivery 미검증을 구분하며, v19 발행 상태를 상향하지 않습니다.

---

v18 발행 이후 승인된 운영 변경과 후속 검토 자료를 한 곳에 수집해 v19 정본을 준비합니다. 현재는 **COLLECTING / DRAFT / NOT RELEASED**이며 운영 정본은 v3.1.18입니다.

## 최초 수집

- PR #72 승인·병합: 게시 상태 교정, WEB 필수 배포, 일정 유연성, #59/#61/#46 날짜 정정.
- 초기 현행 티켓 **64건**, Milestone **64/64건 배정**. 이후 #74/#75 추가 및 메타데이터 갱신 이력은 `audit/v3.1.19/intake/updates/`에서 보존합니다.
- 관련 저장소의 미승인·미병합·Runtime 미검증 자료는 검토 대기로 구분합니다.

## 수집 위치

- [수집 안내](https://github.com/321Team/fds-project-baseline/blob/release/v3.1.19/audit/v3.1.19/README.md)
- `audit/v3.1.19/intake/initial-snapshot.json`
- `audit/v3.1.19/intake/repository-sources.json`
- `audit/v3.1.19/intake/updates/`
- `audit/v3.1.19/COLLECTION_POLICY.md`
- `releases/v3.1.19/FDS_Project_Implementation_Baseline_Release_Notes_v3.1.19.md`

최초 수집 시각: 2026-09-11T09:58:49.550Z

## 발행 전 조건

- [ ] 승인 입력·검토 대기·Runtime 미결 범위 판정
- [ ] Baseline·Ticket Pack·개별 Description·Interface/Decision/CR·Milestone Map 동기화
- [ ] WBS/Gantt·WEB·Release Notes·Manifest·SHA-256·ZIP 및 필요한 아키텍처 v19 구성
- [ ] CURRENT·이력·버전·상태·일정·담당·Gate 및 파일 무결성 검증
- [ ] 이하영의 최종 HEAD 독립 리뷰
- [ ] 이권욱의 병합·발행 승인

자동 수집은 같은 Draft PR에 의미 있는 변경만 누적합니다. 신규 HEAD가 생기면 해당 HEAD의 검토가 필요하며, 일정·설계 승인·코드 병합·Runtime·Gate·Publication을 각각 분리 판정합니다.