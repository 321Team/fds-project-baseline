# Phase 1 As-built 채택·발행 후보

**문서 PR 준비안 선택: p1-as-built-20261018-r1. 사람 최종 채택·게시·Freeze 미승인.**

승인 요구 정본은 [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21), 커밋979facb98de8ca1f1e2ce22f38b27ac3366f3fc3을 유지한다. 이 개정은 이후 As-built 설명·증적 연결을 별도 식별하기 위한 제안이다. Baseline/AC/일정/담당을 변경하지 않고 기존 Architecture v3.1.3의 폐기·대체를 선언하지 않는다.

## 읽는 순서

1. [현재 설명과 변경 상태](AS_BUILT.md): 10/16 고정 설명에서 제목·렌더 상태·상대경로와10/18 확정 보충을 정리한 뒤19:00~19:02 제한 관측의 영향 행만 반영했다. 이전 원문은 source-set에 그대로 있다.
2. [논리도 SVG](source-set/payload/current/render-validation-20261016/proposal-layout-constraints/logical.svg) · [물리도 SVG](source-set/payload/current/render-validation-20261016/physical.svg): 이전 시각 검토를 받은 그대로의 파생물이다. 구성 설명이며 현재 서버 health 화면이 아니다. 최신 제한 관측은 [별도 관측 결속](observations/20261018T1902.json)과 AS_BUILT.md의 해당 절을 따른다.
3. [편집 원본·렌더러·파생물의 버전 결속](DERIVATIVE_PROVENANCE.json) · [전체 파일 SHA256](MANIFEST.json).
4. [기존 렌더 실행 조건](source-set/RENDERER_DEPENDENCIES.md) · [렌더 상태 보충](source-set/RENDER_ADOPTION_ADDENDUM.md) · [기존 시각 검토](source-set/payload/current/render-validation-20261016/VISUAL_REVIEW.md).

## 권장 발행 단위

- 저장소: `321Team/fds-project-baseline`
- 디렉터리: `architecture/as-built/p1-as-built-20261018-r1/`
- 권위 원본: AS_BUILT.md + manifest가 선택한 논리/물리 MMD. source-set의 원본 설명은 비교·출처이며 AS_BUILT.md의 후속 보충으로 읽는다.
- 주 배포 형식: 기존 SVG2개와 이 README/manifest. PNG는 기존 시각 QA 참고 자료, PDF는 미생성·이번 발행 범위 제외.
- source-set은 이전71파일을 바이트 그대로 보존한 출처 묶음이다. 원본 비교 그림·옛 결정 양식·빌드 보조 스크립트·기존 receipt는 과거 이력이며 현재 승인/재실행 지시가 아니다. 원본의 옛 절대 경로·상대링크는 [출처 링크 지도](source-set/SOURCE_LINK_MAP.json)의 원래 문맥으로 읽는다.
- 새 GitHub Release/tag는 기본 발행안에 포함하지 않는다. 정확 HEAD 리뷰·병합 후 commit URL로 발행하고 docs-v3.1.21에 대한 보충 관계를 기록한다. 정본 전체의 새 Release는 별도 최종화 대상이다.

## 재현·중단·복구

현재 후보를 검토하는 데 새 렌더나 서버 작업은 필요 없다. 논리 MMD만 별도 Mermaid에 붙여 넣으면 라벨 위치가 달라질 수 있으므로 선택된 renderer/config와 결합해야 한다. 보존 묶음의 상대 구조를 유지한 별도 작업 사본에서만 기존 렌더 명령을 사용할 수 있다. 그 명령은 SVG·PNG·receipt를 다시 쓰므로 이 묶음에서 실행하지 않는다.

입력/자산 hash 또는 renderer 경로·버전이 다르면 해당 파생물 재사용을 중단한다. 향후 구성·도식 문구·렌더러를 바꾸면 영향 그림만 다시 검토한다. source-set·manifest 불일치나 기존 승인 범위 충돌이 생기면 발행을 보류하고 차이와 원본을 보존한다.

이번 후보에는19:00~19:02 읽기 결과만 연결했다. 발행 전에는 그 이후 실제 변경이 생긴 행의 반영, exact HEAD 리뷰·기존 필수 검증, manifest 재고정, DOC의 O01/문서 Critical0/Freeze 판단을 구분한다. 로컬 후보 폐기는 새 후보를 채택하지 않는 방식으로 충분하다. 이후 문서 PR을 되돌릴 필요가 생기면 해당 문서 변경만 후속 revert PR로 처리하고 기존 정본 tag/원본·서버 설정은 건드리지 않는다.
