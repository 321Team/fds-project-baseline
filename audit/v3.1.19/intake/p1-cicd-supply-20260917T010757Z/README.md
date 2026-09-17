# P1-CICD 공급 Runtime 수신과 앱 인계 후보

2026-09-17 10:07:57~10:09:09 KST cicd-runner01 실행의 사용자 제출 증적을 검증했다.
출처: [infra-cicd Issue11](https://github.com/321Team/infra-cicd/issues/11), [PR18 source73db58f](https://github.com/321Team/infra-cicd/pull/18).
원본 `supply-evidence.tar.gz` SHA256: `6ae2fe28d2ab8eef0d4cf2e92a48b469b7a60fed3b59b8070461e61db2367403`.
외부 sidecar 일치, 내부59개 체크섬·일반 파일60개 일치. 아래12개 파일은 이 원본에서 바이트 그대로 옮긴 인계 후보다.
원본 archive와 전체60개 파일의 GitHub evidence 편입은 NOT_INGESTED다.

| 대상 | wheel 항목 | 설치 환경 | 결과 |
|---|---:|---|---|
| [transaction-api-runtime](transaction-api-runtime/) |25|고정 Python 이미지|offline install/pip check PASS|
| [transaction-api-test](transaction-api-test/) |29|Runner host venv|offline install/pip check PASS|
| [fds-engine-runtime](fds-engine-runtime/) |18|고정 Python 이미지|offline install/pip check PASS|
| [fds-engine-test](fds-engine-test/) |26|Runner host venv|offline install/pip check PASS|

98개 profile 항목은 **중복 제외29개 wheel**이다. 각 디렉터리에 roots.txt, requirements.lock, inventory.json이 있다.
원본 requirements Source는 `supreme33-kr/fds-msa@254b82231f8af79a06419b581174647bbccbe2bc`.
roots·extras·전체 version/hash lock·inventory·download hash·wheel tag·설치 로그를 대조했다.
host Python3.12.14/pip23.3.2/glibc2.39, image Python3.12.14/pip25.0.1/glibc2.41에서 각각 설치했다.
lock 파일의 source/target을 구분하고 공급 성공을 패키지 보안 Scan이나 앱 시험 성공으로 해석하지 않는다.

## base 및 보존 위치

Dockerfile FROM 인계 후보:
```dockerfile
FROM docker.io/library/python@sha256:2fe5997d249a808b8eeea52c58a1dbffbba28754dc11699ef5c029f2d818ce79
```

config ID `sha256:ec7d6c95cd3692a2e2d228a8b1ca74e4025b54121fcc4c5da6f09cfa473315ad`,
서버가 기록한 OCI archive hash `c8fa45563815bd6a3de3a8b115103cbb3c838229bcda68ca255b70a9f2202d8c`.
고정 layer4개·압축46,175,163bytes의 서버 blob/DiffID 검사와 Podman load 성공, inspect의 manifest/config/rootfs 일치를 확인했다.
**RepoDigests=[] / RepoTags=[]**이므로 후속 Build의 repository@digest 해석은 아직 미검증이다.

서버 경로: `/home/server01_cicd-runner/FDS_CICD_Supply.20260917T010757Z.974fb972`.
큰 base.oci.tar 및 wheel·venv·storage는 서버에 남아 있다. 이 폴더의12개 파일에는 wheel/OCI 실물이 없다.
Codex는 제출 영수증을 검증했으며 큰 OCI/wheel 원본 자체를 다시 해시하지 않았다.
요청67개가 승인03의5개 host와10:07:59~11:07:59 KST 작업창 안에 기록됐다. 패킷·방화벽 독립 검증은 아니다.

## 후속 순서

1. 앱 담당은 runtime/test별 lock을 구분해 반영하고 base pin·시험을 포함한 최종40자리 Source와 명시적 실행 승인을 인계한다.
2. CICD는 매 실행의 새 storage에 동일 OCI를 검증/import하고, repository@digest 해석을 검증하며 원격 pull fallback을 제거한다.
3. 별도 wheel build context 및 host/image의 offline hash 설치를 실제 실행기에 연결한다. 현재 앱 Dockerfile의 일반 pip install은 그대로라 본 파일 인계만으로 offline Build가 되지 않는다.
4. 최신 변경의 독립 리뷰 후 승인된 내부 앱 Test→Build→Scan을 실행한다.

실제 공급 Runtime PASS, PR18 코드 HEAD73db58f 유지/리뷰0건/미병합.
APP_TEST_BUILD_SCAN NOT_EXECUTED, DELIVERY_GATE NOT_VERIFIED, Runtime AC1/10, 정본v3.1.18 유지.
