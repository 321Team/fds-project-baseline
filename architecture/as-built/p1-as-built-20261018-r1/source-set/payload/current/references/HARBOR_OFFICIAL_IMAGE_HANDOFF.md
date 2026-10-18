# 중앙 인계 — 공식 manifest/config 결속

**조사 범위 완료. 결과는 검증된 config ID 불일치이며 Runtime HOLD 유지다.**

- 저장·현재 tag 모두 공식 manifest `bed040aef1073b3a8d516f782d449f4df7c0bb8d049f0b3c84ff65c085b29981`이다. 직접 schema2/linux-amd64이며 index는 없었다.
- manifest가 참조하는 config 원문은 **`701038c9f9cfed2052de8a458a820be7569df80f1e926f84e3509a0caa31d205`**. manifest/config 원문 digest·descriptor size·응답 header 대조 완료.
- 17:38 실제 Harbor image ID **`a22b58594cea54a78d1c670a81b9dfa3c5af8b4bdd1f89750fdf1c5876c72eab`**와 다르다. 앞선 manifest-vs-config 구분만의 미확인에서, 같은 config ID 기준의 불일치로 판단 근거가 구체화됐다.
- 공식 config label/history에서 정확 GitCommit/generated Access 결속은 확인되지 않았다. 다른 공식 배포분·설치 출처·바이너리 동일성·변조 여부는 미판정이다. 공식 tag와 같다는 주장을 수용할 근거가 없지만, 이를 비공식/침해 확정으로 표현하지 않는다.
- 다음 최소 확인은 **기존 설치 archive/공급 receipt의 위치와 hash → 그 안의 manifest/config가 실제 ID에 연결되는지**다. provenance가 부족하면 정확 artifact의 build 증거 또는 별도 격리 wire 동작 시험 중 필요한 범위를 정한다. 현재 profile·후보·실행 절차는 변경하지 않았다.

본문/제한/대안: [FINDINGS.md](FINDINGS.md). 정확 원문·HTTP/시각/hash: [COLLECTION_RESULT.json](COLLECTION_RESULT.json), [BINDING_RESULT.json](BINDING_RESULT.json), [INPUT_BINDINGS.json](INPUT_BINDINGS.json). 최종 입출력 고정: [FINAL_BINDING.json](FINAL_BINDING.json).

공개 metadata 응답3개만 회수했으며 layer/pull/build/run·서버접속·Harbor API·credential시험·발급·운영·게시0이다. 익명 token/Authorization/서명 redirect URL은 저장·출력하지 않았다. 후보·검사·metadata 재수집 및 만료 후 계획 재작성은 없다. 후속 범위 결정 전 추가 탐색을 종료한다.
