# 구축 세션용 Phase 1 수집 정보와 현장 입력 인계

이권욱 / CODEX_ASSISTED · 2026-10-11 KST. GitHub 상태 조회 19:28 이후, 원본 보관 메타데이터 19:34 KST. 사용자 요청은 다른 세션의 구축과 병행하여 필요한 정보를 수집·정리하고 인계하는 것이다. 이 기록은 Phase 1 잔여만 소비하며 서버 실행·신규 정책·계정/권한·AC 변경을 수행하지 않는다.

## 먼저 소비할 결론

- PR160~162와 CICD74/Harbor41/APP30은 병합됐다. **U01~U03 답변도 모두 수신**했으므로 다시 요청하지 않는다. U03의 답변 내용은 관리 접근 미확인이다.
- 구축 세션은 기존 개발·모의검증을 계속할 수 있다. 실제 설치/배포의 현재값·복귀점·비중첩은 실행 세션에서 수집한다. 지원 세션이 같은 서버를 따로 조회·변경하거나 이전 상태를 현재값으로 채우지 않는다.
- 이 인계는 코드 리뷰·Runtime·증적 리뷰·AC 인수를 대신하지 않는다. 원문 출처가 없다는 사실과 미회신, 문서의 작성 당시 상태와 현재 GitHub 상태를 구분한다.
- 현황은 [INTAKE_STATUS](../phase1-remaining-20261009/INTAKE_STATUS.md)와 최신 원회신을 기준으로 하고, [전체 ID 대응표](README.md)·[검증안](MINIMUM_VALIDATION.md)·[회차 카드](SESSION_AND_HANDOVER.md)는 그 소비 지도를 제공한다. 실제 상태 갱신 근거는 [10/11 통합 기록][sync]이다.

## 1. 이번에 확보·정합화한 사실

| 항목 | 확인된 정보·근거 | 소비 범위와 남는 한계 |
|---|---|---|
| U01 / D01 | [이재환 직접 회신][ureply]: 10/8 db01 콘솔 server08+sudo 붙여넣기 실사용, 10/10 콘솔 입력 문제 해소 | 기존 경로 재질문 없음. 당일 전달·정확한 비중첩 창·수신 대조는 별도. 오래된 runbook의 scp 문구를 실제 전달 이력으로 사용하지 않음 |
| U02 / H05 | 같은 회신: 10/10 23시경 조직 관리자 UI Actions Secrets0건 확인 보고 | 사람이 확인한 시점·범위의 회신. 이 지원 세션의 UI 직접 검증이 아님. CLI403은 이력 보존, Variables/Dependabot/Codespaces까지0건으로 확대하지 않음 |
| U03 / H05 | 같은 회신: 당시 harbor-log만 Up·80/443 리스너 없음, 로그인·Robot 메뉴 미확인 | 정상 기동 후 기존 관리 접근 확인 필요. PC timeout을 특정 방화벽 규칙의 직접 증거로 사용하지 않음 |
| C01 / 보관6묶음 | 10/11 19:34 KST 현재 계정으로 기존6파일 메타데이터 읽기 성공. 이름·크기는 아래와 같고 reparse flag는 모두 false | 새 content hash·내부 검사·SMB ACL·허용자 배타성은 미검증. 메타데이터 읽기는 지정 보관자 사람 인수나 실효 권한 증거가 아님 |
| OID-02 도구 | [K8S68][k68] v2 HEAD `85939569b491aa4b89010a38f108cc8ab6c4ad18`의 이하영 독립 승인, merge `80f39bd5339474fc4dc6ceada7c66d8b3d2288b5` 확인 | 고정 문서의 `v2 독립 리뷰 PENDING`은 작성 당시 기록. 실제 metadata 수집·export/import·출처·OID03 해결을 의미하지 않음 |
| I01 판정 | [APP 실행 준비][app]의 기존 기준: 유효22건, I01이201이면 총23행·save/evaluated+23,422이면22행·+22 | INFO 결과에 따라 분리. Rule 증가는 I01 실제 결과로 판단하며 5xx/연결 실패를 INFO 성공으로 바꾸지 않음 |
| 운영자 참여 | [이재환 PR162 리뷰][jreview]: 구체 회차 카드 확정 뒤 참여 가능 범위 회신 | 이권욱이 먼저 대상·정상 접근·시간·복귀를 제시. 현재 미지정은 참여 거부가 아니며 새 대기 요청을 반복하지 않음 |

### C01 관측한 기존 파일 — 내용 비수집

| 기존 원본 | bytes |
|---|---:|
| k8s-tool-backup-20261009T091654.tar.gz | 162981 |
| app-supply-37859961937.zip | 109786915 |
| app-tbs-37890963668-metadata.tar.gz | 8213 |
| ansible-ci76-11602757338.zip | 512208 |
| ansible-ci76-host-evidence.tar.gz | 6334 |
| app-raw-37890963668.tar.gz | 326294507 |

비공개 위치는 기존 증적195 보관 영수증을 사용한다. 새 위치를 만들거나 추가 원본을 전송하지 않았다. 위 크기는 기존 수신표와 같지만 bytes 동일성을 새로 입증하지 않는다. 원 해시/사람 인수/retention은 기존 기록을 재사용하며 실행에 소비할 때 필요한 실제 파일 해시를 대조한다. 공유 접근통제 C01은 **그 SMB 공유**에 한정되고 D01 db01 수신의 공통 선행조건이 아니다.

## 2. 바로 재사용할 소스와 이미 확정된 값

고정 문서9개의 Git blob와 SHA256을 직접 대조했다. 파일별 저장소·40자리 revision·경로·Git blob·SHA256은 [수집 소스 대장](COLLECTED_SOURCE_INDEX_20261011.json)에 있다. 이 대장은 소스 문서 무결성 기록이며 서버 실행 증적이 아니다.

| 묶음 | 고정 소스/이미 확보한 값 | 다시 만들지 않을 것 |
|---|---|---|
| Harbor S02 | main `a3caf48b49320edff2d89e61c8a996f0e34b70eb`; [패키지 생성][hpackage]·[수신 검사][hreceipt]. source11개+bootstrap/unit/bundle/launch/INSTALL_PLAN 총16파일, 외부 보존 plan SHA와 유한 검사 예산 필요 | #41은 게스트 installer가 아님. 합성 package를 실제 입력으로 바꾸지 않음. H6·늦은 stop·세대 변경·부분 policy 실패 복구의 구현/검증은 별도 개발 잔여 |
| Delivery S01 | main `2d8a14c55ea4b61f53b7ac6d682cd5e97575dda7`; [Token 계약][token] 요청/최대900초, 실제 수명은 더 짧을 수 있음. 기존 시작 예산630초와629초 차단 유지 | 3600초 Token 정책 재질문·동일 코드 재구현 없음. 과거 승인/plan hash를 자동 수정하지 않음. 새 Push receipt는 성공한 Push 뒤 Deploy에 결속 |
| APP V08 | 도구 main `c2372da3fd5ed01a01374b9ea57e34a58f86d3eb`. APP 후보 `affbc69beef9967f7977d09a6fec14f7fb6c0e94`, 공급 source `8eac4c982076e3c219840a13686b15c46879981f`; criteria SHA `8aad7cc215137b97168230926d0e9655eba4dd3386944bf6efc06bfc83aae8d8` | 도구의 새 HEAD를 APP image/source로 대체하지 않음. 기본 시간 fixture는 KST01:00~05:00 밖에서 수행하도록 기존 준비안을 사용. 과거24PASS를 새 회차에 복제하지 않음 |
| K8S V01 | main `c42ea6cc3ccd197d12993823bed439d40946a54c`; PR78 PLAN의5호스트45파일, 변경17/유지28, control02 제외. 목표 root:root0750·`system_u:object_r:usr_t:s0` | 기대 metadata와 실패 복귀 metadata를 합치지 않음. 실제 호출자·fresh backup/임시 restore는 구축 세션이 해당 회차에서 확인 |
| MON V04/V05 | main `0dd0235b07d44ba7965490e3808e0a67a3bd903b`; [접근 원장][grafana]·기존 MON42 최소안. 과거 PF/401/Discord·Secret 참조 증적 재사용 | Secret 참조 위치를 인적 보유자·유효 암호로 추정하지 않음. 승인 단말만 접근 가능하다는 배타성은 미입증. 이미 모른다고 회신한 과거 생성자/감사를 재요청하지 않음 |

## 3. OID-02/03 — 이미 수집한 분포와 진짜 부족한 정보

[10/7 16:26 읽기 원본 회신][oid-observation]과 [후속 대조][oid-gap]을 구분해 소비한다. 아래는 **과거 관측**이며 현재 배치/캐시의 자동 확정값이 아니다.

- kube-controllers 기준 top digest: `sha256:df00967cbd6d88e1ff3123e1598895845622e2987928b4ebd9d8ac49aefe00c3`. 당시 ref는 control01에만 있었다.
- CoreDNS 기준 top digest: `sha256:e7e6440cfd1e919280958f5b5a6ab2b184d385bba774c12ad2a9e1e4183f90d9`. 당시 ref는 control01~03에 있었고 Worker3대에는 없었다.
- 이미 수집한6노드 분포를 처음부터 다시 요청하지 않는다. image ref 미관측을 모든 content 부재로 확대하지 않는다. control01 drain/reboot·관련 Pod 삭제/재시작 제한과 preloaded 경계는 기존 기록대로 유지한다.
- 실제 미수신은 고정 top digest에 연결된 linux/amd64 child manifest·config/platform·layer descriptor/size 관계, 공급 원본·출처, 원 ref/전체 플랫폼 보존 방식, export/archive 검증·대상별 반입/복귀안, OID03 경로 처분이다. 코드 승인·cache complete가 이 공백을 해소하지 않는다.
- [v2 읽기 도구][oid-tool]는 위 metadata 관계의 보완 수단이다. 승인 source와 실제 전달 bytes·host/권한/소켓·비중첩을 결속한 회차에서만 소비한다. 이 지원 작업에서는 실행하지 않았다. 성공하더라도 layer 본체 검증·archive 크기·최초 출처·OID02 AC/OID03 완료가 아니다.
- 출처가 없다고 이미 회신한 자료를 다시 만들어 달라고 요청하지 않는다. 이후 새 기존 원본이 발견되면 위치·hash·노드·시각만 연결한다. 확보 불가 항목은 한계와 기존 Decision/CR의 처리 대상으로 남기며 승인된 것으로 추정하지 않는다.

## 4. 구축 세션에 넘길 현장 수집 항목

아래 값은 저장소만으로 수집 완료할 수 없다. 이미 작업 중인 실행 세션이 자신의 현재 대상에서 기존 계정·승인 범위의 읽기 확인을 묶어 수행한다. 지원 세션은 SSH/VM/컨테이너/DB/credential 조작을 병행하지 않았다. 새 수집기는 만들지 않고 위 기존 runbook과 [최소 검증안](MINIMUM_VALIDATION.md)을 사용한다.

| 순서·소비 시점 | 수집할 실제 값 | 성공·중단·원복 경계 |
|---|---|---|
| F01 복구 package 입력 전 | 정확한 대상 hostname/product UUID/boot ID·NIC/HGFS·주소/라우트/마운트, 정상 Console/기존 권한, 원 policy·현재 복귀점/보존 위치 | 원본/clone을 섞거나 과거 snapshot을 현재 backup으로 대체하지 않음. 단일 대상/복귀점 불명확 시 해당 위험 회차만 중단 |
| F02 설치 구현/시험 전 | 실제 Python3.10+ 공급/실행 경로, SELinux Enforcing와context, Engine/InvocationID·Compose/10exact ID/health/원 정책/StopSignal·logger1514, 도구/units/ACL/xattr·경로 충돌·새 Store·실측 시작/종료 예산 | package 생성 전 필요한 입력. 현재값 자동 승인·통제 해제·샘플 입력 금지. 설치/정책 쓰기는 코드 리뷰·해당 회차와 별도 결속 |
| F03 Push/Deploy 전 | 현행 Robot ID/권한/세대/만료·CA/TLS/scan, workflow·source·정확 target/복귀 digest, SA UID/audience/CA/RBAC·fresh TokenReview/실제 잔여시간, 비중첩/Console | 비밀값은 비공개 경로. 과거 Ready/rollback_approved=false를 새 health/복귀 승인으로 사용하지 않음. 만료·drift면 다음 쓰기 중단 |
| F04 필요한 기반 검증 전 | K8S 호출 배제·fresh backup/복귀 metadata, MON 관측 계정/현재 route와 canary 독립 만료, HA 변경 형상/PDB/local PV, Ansible source/engine·snapshot·현재 DNS/서비스 | 같은 노드·Registry·정책을 동시에 바꾸지 않음. 필요한 AC 행만 수행하고 기존 성공을 전수 반복하지 않음 |
| F05 Harbor 정상 기동 후 | 이재환의 기존 관리 로그인·Robot 메뉴 가능 여부, 실제 consumer/참조·정리 영향과 보존/오판 대응 | U03 답변은 수신됨. 아직 접근/삭제 성공은 아님. 이 세션이 서비스 기동·삭제를 실행하지 않음 |
| F06 D01 전달 직전 | 이재환과 정확한 시작·db01 비중첩·당일 콘솔/수신 경로·기존 파일 충돌 여부 | 10/11 19:00 이후는 후보 시간. 경과했다고 실행/수신한 것으로 표시하지 않음. 전달 입력 이재환, 수신·hash/권한 확인 이권욱 |

F01~F06은 새 AC나 승인 단계가 아니라 기존 회차 입력의 위치를 모은 목록이다. 현재 사실을 수집한 원본·rc·시각·source/hash·제한을 해당 회차 기록에 연결하고, 수집 불가면 그 값의 소비 작업만 대기한다. 읽기 확인 중 생성한 원본은 신규 비공개 경로에 보존하며 과거 원본·claim을 지우지 않는다.

## 5. 사람/접근 경로가 필요한 잔여와 요청 방식

- **C01:** 실제 공유 관리자 또는 기존 정상 조회 경로는 미확정이다. 기존 요청의 후속으로 알고 있는 경로가 확인되면 연결한다. 이번6개 파일 읽기 성공으로 공유 ACL 검증을 생략하지 않는다. 관리자 권한 부여·계정 생성·ACL 변경을 요청하지 않는다.
- **D01:** 파일명·5,206B·외부 SHA256·db01 위치와 postgres:postgres0700/0600은 기존 카드대로 확보됐다. 실제 dump 원본과 전달 결과는 이재환 입력/이권욱 수신 회차에서 확보한다. 새 Restore를 수신 조건으로 추가하지 않는다.
- **O01/O02:** 구축 세션이 실제 대상/접근/시간/비중첩/정리 기준이 있는 카드를 먼저 완성해 참여를 확인한다. 이름만 지정하거나 코드 리뷰를 실제 재현으로 합산하지 않는다.
- **과거 W4/FUP·출처 한계:** 이미 없는/모른다고 수신한 사실은 보존한다. 새 현재 시험으로 과거 공백을 채우지 않고 기존 AC의 영향·처분을 연결한다.

미수집 값에는 확인 주체·방법·소비 시점을 명시했지만, 주체가 답했거나 실서버 값이 확인된 것으로 표시하지 않았다. 신규 사실 요청/리뷰는 이 후속 PR 한곳에서 연결하며 U01~U03 재질문이나 모든 답변의 일괄 대기를 만들지 않는다.

## 6. 실제 수행 범위

STATIC/SOURCE: 병합·회신·책임 티켓 최신 기록 대조, 고정 문서9개의 blob/해시 확인. 보관 파일6개는 메타데이터 읽기만 수행. 문서의 U 상태·R1 코드 통합·H06 표현·I01 판정·C01/D01 범위·참여 회신 순서를 정합화했다.

RUNTIME/서버 source 설치·DB 전송/쓰기·계정/Secret 변경·ACL 변경·독립 제3자 수행·AC/Status 변경·종결은 미실행이다. 파일 수정·PR/리뷰 요청·실제 인계 전달 결과는 후속 PR과 세션 전달 기록으로 구분한다. 자동 병합이나 새 작업창을 생성하지 않는다.

[ureply]: https://github.com/321Team/fds-project-baseline/pull/161#issuecomment-6098286300
[sync]: https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6099088195
[jreview]: https://github.com/321Team/fds-project-baseline/pull/162#pullrequestreview-5479168907
[k68]: https://github.com/321Team/infra-kubernetes/pull/68#pullrequestreview-5440153422
[oid-observation]: https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-6033151808
[oid-gap]: https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-6034027526
[oid-tool]: https://github.com/321Team/infra-kubernetes/blob/85939569b491aa4b89010a38f108cc8ab6c4ad18/docs/change/ICR-D-NET-01-01/OID02_CACHE_METADATA_READONLY_20261007.md
[token]: https://github.com/321Team/infra-cicd/blob/2d8a14c55ea4b61f53b7ac6d682cd5e97575dda7/docs/token-policy-900-20261010.md
[hpackage]: https://github.com/321Team/infra-harbor-trivy/blob/a3caf48b49320edff2d89e61c8a996f0e34b70eb/docs/runbooks/harbor-recovery-review-package.md
[hreceipt]: https://github.com/321Team/infra-harbor-trivy/blob/a3caf48b49320edff2d89e61c8a996f0e34b70eb/docs/runbooks/harbor-recovery-package-receipt.md
[app]: https://github.com/321Team/fds-msa/blob/c2372da3fd5ed01a01374b9ea57e34a58f86d3eb/docs/p1-final-regression-readiness-20261010.md
[grafana]: https://github.com/321Team/infra-monitoring/blob/0dd0235b07d44ba7965490e3808e0a67a3bd903b/docs/GRAFANA_ACCESS_LEDGER_20261009.md
