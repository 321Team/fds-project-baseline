# DOC 원본·렌더 제안 채택 선택 카드

2026-10-16 KST · CODEX_ASSISTED · 모든 결정 미기록

**권장:** 고정 설명 원본+렌더 보충, layout-only 논리 MMD, 기존 물리 MMD를 함께 검토하고, 필수 렌더러·config·검증된 SVG를 같은 source 묶음에 결속한다. 원본 논리도의 가림이 그대로 있는 SVG는 배포 후보로 선택하지 않는다. 기존 원본을 덮어쓰라는 실행 지시가 아니다.

정확한 파일은 [ADOPTION_MANIFEST.json](ADOPTION_MANIFEST.json)의 SHA256로 식별한다. 파일명의 날짜·CURRENT-FACTS-CANDIDATE 주석은 로컬 식별자이고 공식 Release 번호가 아니다.

| 결정 필드 | 권장안 / 기록할 값 | 현재 상태 |
|---|---|---|
| `source_scope` | manifest의 설명+보충 / layout-only 논리 / 기존 물리 / 필수 렌더 계약을 한 묶음으로 선택. 보류할 경우 사유와 제외 항목 기록 | 미채택 |
| `official_source_version` 및 `release_relation` | 승인 요구 기준 `docs-v3.1.21` 유지. 채택 원본의 정확한 개정 식별자와 기존 정본 Release와의 관계를 함께 기록. 다음 버전 번호를 자동 생성하지 않음 | 값 미확정 |
| `destination` | 기존 Architecture 규칙에 따라 `321Team/fds-project-baseline`의 `architecture/`를 권장. 논리·물리·설명/보충·renderer/config·SVG/manifest의 **각 최종 파일명과 경로**를 함께 확정 | 저장소/폴더 권장안만 있음 |
| `distribution_format` | SVG 우선, source hash/version 및 renderer 계약 동반. PNG를 공식 배포에 포함할지 별도 표시. PDF는 미생성 | 형식 미선택 |
| `adoption_review_record` | 실제 채택 결정자·근거·시각·대상 manifest 해시를 기록. 기존 A1은 이권욱 DOC Lead 판단용이었으며 여기서 새 승인자를 지정하지 않음 | 미기록 |
| `D07_ledger_linkage` | 기존 [대장 행](references/D07/D07_LEDGER_ROW.md)을 #20 기존 대장에 채택/연결할지와 정확한 반영 위치·수신 기록만 결정. 새 이슈·새 행 재작성 없음 | 공식 연결 미실행 |
| `publication_and_freeze` | 원본 채택과 실제 게시·source/파생물 결속 확인·DOC/O01·Critical 문서결함0·Freeze 판단을 구분해 각각 기록 | 모두 별도 미판정 |

경로 선택은 공식 발행 전 남은 값이다. 권장 디렉터리 내부에서 MMD·설명은 편집 원본, SVG/PNG/PDF는 해당 source version을 가리키는 파생물이라는 [기존 관리 규칙](references/ARCHITECTURE_RULE.md)을 유지한다. renderer를 현재 구조와 다른 곳으로 옮길 때에는 상대 입력 경로를 새 목적지에 맞게 묶어야 하며, 의미·배치를 바꾸는 renderer 변경을 이번 검증이 자동 승인하지 않는다.

[DECISION_FIELDS.json](DECISION_FIELDS.json)에 위 7개 판단 단위를 모았다. 빈 값은 미결정이며 동의·승인·배포 허가로 해석하지 않는다. 실제 제품·서버·보안 미확인 사항은 [인계 경계](HANDOFF.md)에 그대로 남긴다.
