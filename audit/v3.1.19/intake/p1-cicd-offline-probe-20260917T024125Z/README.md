# 고정 digest 공급 소비 Runtime 수신

실행: 2026-09-17 11:41:25.886870~11:41:30.409717 KST, 약4.52초.
원본 archive `offline-probe-evidence.tar.gz` 5,158bytes / SHA256 `db6c4a18857aa5ecb1f9a923888268193d7653932b9b0eeb0174116fe07f7831`.
이 폴더의 result·명령 로그6개·원래 SHA256SUMS, **8개 파일은 제출 archive 원본 바이트**다.

외부 sidecar/내부7개 체크섬, 고정 번들 SHA082d800b...·내장 입력 SHA0cdf9165..., 명령6개의 argv/순서/시간/rc0/log hash를 대조했다. 새 rootless VFS store의 load/tag와 **repository@manifest 직접 조회**가 성공했고, inspect의 config ID·Digest·RepoDigests·RootFS4개·linux/amd64가 일치한다. 최소 Build log의 digest FROM·Python print(123)·출력123·COMMIT·최종 ID가 result와 일치한다.

**OFFLINE_PROBE Runtime PASS(제출 증적 기준)**. 과거 상대경로 초기 오류와 별개로 기존 cefcaeaa 번들을 절대경로로 재개한 실행이다. 코드 수정602e376의 CI122 PASS와 이번 실행 Source cefcaeaa를 구분한다.

원본 OCI/wheel·생성 probe image는 서버에 있으며 이 폴더에 포함하지 않는다. `offline-base-resolve.log`의 History는 base 이미지 제작 이력으로, 이번 probe에서 실행한 명령이 아니다. 공급 사본/wheel 검사는 고정 서버 도구의 결과를 수신한 것이며 Codex가 원본 payload를 다시 계산한 것은 아니다.

실행 폴더: `/home/server01_cicd-runner/FDS_CICD_OfflineProbe.9r4g0goy`.
기존 공급 폴더: `/home/server01_cicd-runner/FDS_CICD_Supply.20260917T010757Z.974fb972`.
성공한 collect/probe를 같은 목적 때문에 반복하지 않는다.

앱 pip 설치·Unit/Contract·앱 Build·Trivy Scan은 이번 범위에 없다. 앱 최종 pin/lock SHA와 범위 승인, 최신 CICD 독립 리뷰/중앙 Workflow 연결이 남는다. Runtime AC1/10, DELIVERY_GATE NOT_VERIFIED, 정본v3.1.18을 유지한다.

[Issue11](https://github.com/321Team/infra-cicd/issues/11) · [PR19](https://github.com/321Team/infra-cicd/pull/19).
