# 1. 새 APP Push 인계 입력 대조

책임: [infra-cicd#11](https://github.com/321Team/infra-cicd/issues/11), 이권욱. CODEX_ASSISTED.

## 실제 판정

- evidence147 이전 승인 HEAD d54512ec4f7959e17b7cdc719d249196417369e7 → 현재 dbc5ce9ca5fa097b6016fcf989c8985ab19288be.
- 추가 commit 제목은 main 병합이며 APP 회차 폴더의 **42개 blob 전부 동일**하다. 다른 회차 편입을 APP 원본 변경으로 오인하지 않는다.
- PR65 현재 3f247aec7a3b027ba2dceb445fb85bc5f8bb7f2c의 BUILD_SCAN_HANDOFF/push.draft를 직접 읽었다.
- archive SHA256 d0762a96741f69ac0fab14f116bdd84b95330d5eb9fe65889ad96853df47b6b4 일치.
- APP/Build/Scan 원문 hash3개와 receipt 연결, Source/Workflow/Run/Attempt/config, 두 이미지 archive/manifest/config 및 소비되는 Scan 필드의 **26개 대조 모두 MATCH**.
- Scan은 소비 자료에 있는 scan/exit_code/counts/manifest_digest/report_sha256을 대조했다. 원본의 추가 platform/diff_ids까지 같은 객체라고 주장하지 않는다.

따라서 **PR65 입력 재작성 불필요**다. 이전 PR147 승인은 이전 HEAD에 결속돼 있고,
현재 HEAD 병합/승인 적용 판단은 독립 리뷰 세션이 담당한다. 이 대조는 APPROVE가 아니다.

## 재현 순서

1. evidence 저장소 Git Trees API의 위 두 ref를 recursive=1로 조회, truncated=false 확인.
2. evidence/P1-CICD-01/app-adc90410-run37642123031-20261008/ 아래 전체 blob 경로/oid 집합 비교.
3. PR65 고정 SHA의 handoff/push-review-37642123031/ 두 JSON과 증적 archive를 Contents API로 읽는다.
4. 수신 blob의 Git 객체 hash를 확인하고 archive SHA256을 BUILD_SCAN_HANDOFF와 비교.
5. archive에서 result.json, build-scan/result.json, build-scan/scan/result.json만 메모리로 읽어 원문 hash/필드 연결 대조.
6. [결과 JSON](push-input-comparison.json)의 각 true와 기대값/원문을 비교한다. 압축 해제 실행·원본 로그 변경 없음.

## 아직 필요한 입력

| 입력 | 생산 책임/기존 근거 | 현재 소비 조건 |
|---|---|---|
| CI Robot 권한·만료·세대·안전한 인계/회수 | HBR 이하영 / baseline13 | 새 값 미확정. 재발급 HOLD를 기존 계정 전면 불가로 단정하지 않음 |
| 새 Push 승인·유효 창 | CICD 책임 범위 / issue11 | 옛 회차 만료 승인 재사용 금지 |
| TLS/공급/Scan 신선도 | 기존 Runner 실행안 | 이전 Test/Build/Scan PASS를 미래 fresh 점검으로 대체하지 않음 |
| 새 Push Run/원격 digest/정리 receipt | 다음 승인된 Push 회차 | 현재는 NOT_EXECUTED. 로컬 OCI digest를 원격 값으로 채우지 않음 |

다음 절차는 최종 입력 확정 → 기존 execute=false 검사 → 허용된 비중첩 창의 fresh Scan/Push/원격 digest/자격증명 정리다.
이번에 Secret 등록, Robot 변경, Workflow dispatch, Push나 서버 재검증은 하지 않았다.
