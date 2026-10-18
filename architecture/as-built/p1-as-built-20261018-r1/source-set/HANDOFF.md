# DOC 채택 검토 인계 — 렌더 검증 결과 결속

2026-10-16 KST · CODEX_ASSISTED · **로컬 검토 묶음 준비 / 채택·발행 미결정**

권장안은 **설명 원본과 이 묶음의 렌더 보충, 배치만 조정한 논리 MMD, 기존 물리 MMD를 한 묶음으로 검토하고, 논리 렌더러와 검증된 SVG를 함께 관리하는 것**이다. 논리 MMD만 채택하면 검증된 SVG의 라벨 위치가 재현되지 않으므로 필수 렌더러를 분리해서 결정하지 않는다. 기존 아키텍처 값·승인 기준·증적 시점은 유지한다.

| 바로 검토할 대상 | 역할 |
|---|---|
| [채택 선택 카드](ADOPTION_DECISION_CARD.md) | 권장 범위와 한 번에 결정할 필드 |
| [설명 원본](payload/current/P1_AS_BUILT_CANDIDATE.md) + [렌더 보충](RENDER_ADOPTION_ADDENDUM.md) | 사실·실효·미확인 경계, 과거 렌더 미실행 표현의 정정 |
| [논리 MMD 제안](payload/current/render-validation-20261016/proposal-layout-constraints/P1_LOGICAL_LAYOUT_PROPOSAL.mmd) / [검증된 SVG](payload/current/render-validation-20261016/proposal-layout-constraints/logical.svg) | 기존 의미를 보존한 배치 수정안 |
| [물리 MMD](payload/current/candidate/architecture/P1_PHYSICAL_AS_BUILT_20261015.mmd) / [검증된 SVG](payload/current/render-validation-20261016/physical.svg) | 승인 설계 상속·관측 범위를 보존한 원본과 파생물 |
| [필수 렌더러·버전·배치 계약](RENDERER_DEPENDENCIES.md) | 재현 조건과 renderer 의존성 |
| [D-07 기존 대장 후보 연결](D07_LINKAGE.md) | 기존 행을 재작성하지 않고 남은 채택 판단만 연결 |
| [파일 역할·해시](ADOPTION_MANIFEST.json) / [검사 결과](PACKAGE_CHECKS.json) / [최종 결속](FINAL_BINDING.json) | 정확한 검토·선택 대상 식별 |

## 기존 카드의 상태 정정

[A1_UPDATED_DECISION_CARD 원문](../../A1_UPDATED_DECISION_CARD.md) SHA256 `fb0fa9219ccd1c3a423ec52ee1ae401a17ee434f9c8097ef3bef5bf3739ce75b`는 수정하지 않았다. 해당 카드 및 설명 원본의 “파생본 생성·렌더 QA 미실행”은 **2026-10-16 로컬 렌더·시각 검토 완료**로 보충해서 읽는다.

원본 논리도에서는 무관한 노드 뒤로 연결선이 가려지는 곳 4개와 라벨 경계 겹침 1쌍이 확인됐다. 별도 제안에서 해소했고 21개 노드·22개 표시 연결선·문구의 동일성 검사가 통과했다. 물리도도 확인 범위의 렌더·시각 검토를 통과했다. “그림을 아직 만들지 않음”은 해소됐지만, **어떤 원본과 배포 형식을 공식 채택할지는 여전히 미결정**이다.

기존 QA 결속 `ccd7a9e9129d4df7546777df12437f94d3fc5f9e887804673deaa12ef48142e7`에 포함된 54파일의 현재 해시가 모두 같다. 이번에는 그 결과를 소비하고 파일·링크·구성 무결성만 확인했다. Mermaid 실행, 시각 QA, 제품 시험, CI를 반복하지 않았다. 이 묶음의 57개 보존 사본은 원본/기존 영수증/선택한 QA 자료/D-07 자료의 최소 검토 구성으로, 기존 QA 54개를 전부 복제한 수가 아니다.

## 사실의 실효와 인수 경계

| 구분 | 이 묶음에서 확인·소비한 상태 | 남는 경계 |
|---|---|---|
| 아키텍처 | 고정 설명·MMD, 기존 증적의 논리 연결과 승인 설계 물리 배치 | 전체 Windows/VM/NIC/route/NAT 실효를 현재 다시 확인하지 않음. v3.1.3 원본 위치 미확인은 부재 판정이 아님 |
| 문서·자동화 | 고정 후보의 APP39 merge/CI 영수증, Ansible LOCAL/MOCK185/185·회수 결과, D02 문서·수행 인수 결과 | 제품 수정·현재 서버 동작·운영 자동화 채택·전체 인수로 확대하지 않음 |
| 보안·운영 한계 | D02 HTTPS NOT_MET·한정 조건, SEC30/Grafana 처분, Harbor 운영 HOLD·해당 시점 provenance/인증/건강 미확인 유지 | 고정 후보 이후 Harbor 등 다른 작업의 새 결과를 넣지 않음. 이 묶음의 현재 준비 시각을 서버 관측 시각으로 사용하지 않음 |
| D-07 | ID·기존 Owner·첫 재검토 조건 확정 및 기존 로컬 연결 수용 | 공식 대장 반영·제품 위험 해소·APP/E2E 전체 인수와 별도 |
| 렌더 | 기존 로컬 렌더·시각 검토 완료, 의미 보존·해시 결속 | 원본 채택·아키텍처 승인·공식 버전/경로·발행·DOC/O01 Freeze는 별도 |

## 검토와 채택 순서

1. 설명 원본을 [렌더 보충](RENDER_ADOPTION_ADDENDUM.md)과 함께 읽고 논리/물리 SVG를 확인한다. 원본 논리 MMD는 비교·보존용이며 채택 권장 대상은 별도 layout-only 제안이다.
2. [선택 카드](ADOPTION_DECISION_CARD.md)의 범위·버전·목적지·형식·판정 필드를 한 번에 기록한다. [DECISION_FIELDS.json](DECISION_FIELDS.json)은 현재 모두 미결정인 양식이며 승인 기록이 아니다.
3. D-07은 [기존 후보의 정확한 행](references/D07/D07_LEDGER_ROW.md)을 기존 #20 대장에 연결할지 별도로 결정한다. 새 행이나 새 이슈를 만드는 안을 작성하지 않았다.

원본 3파일·부모 binding·기존 QA·승인본·공통 기록은 변경하지 않았다. 이 묶음은 같은 workspace의 보존 출처와 연결된 **로컬 검토 패키지**다. 출처 사본의 오래된 문구·상대경로는 원문 증적으로 보존하며, 원래 위치 및 링크 해석은 [SOURCE_LINK_MAP.json](SOURCE_LINK_MAP.json)에 있다. 검토 진입 링크와 핵심 원본의 직접 링크는 확인했지만 모든 과거 증적을 새 배포물로 재포장하거나 외부 링크의 최신 상태를 재조회한 것은 아니다. 공식 발행 시 확정 목적지에 맞춘 링크·source version 결속은 발행 단계에서 처리한다.

남은 것은 위 선택과 별도의 승인·발행·Freeze 판단이다. 이번 작업에서 새 승인자·공식 버전·기한을 지정하거나 사용자 질문·외부 쓰기를 하지 않았다.
