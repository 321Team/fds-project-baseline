# As-built 렌더 시각 검토

2026-10-16 19:29 KST · CODEX_ASSISTED · LOCAL RENDER / VISUAL REVIEW

논리·물리 MMD는 모두 Mermaid 11.17.0 문법 해석과 SVG/PNG 생성에 성공했다(rc 0). 원본 논리도 렌더는 연결선 가림으로 배포용 시각 판정을 보류한다. 물리도와 별도 논리도 배치 제안은 아래 범위에서 시각 검토를 통과했다. 이 판정은 아키텍처 승인이나 실제 환경 검증이 아니다.

| 대상 | 크기 | 노드 / 표시 연결선 | 시각 판정 |
|---|---:|---:|---|
| 원본 논리도 `logical.svg` | 3502 × 1466 | 21 / 22 | 가림 4곳, 라벨 경계 겹침 1쌍 |
| 원본 물리도 `physical.svg` | 3778 × 520 | 17 / 16 | 확인 범위 통과 |
| 별도 논리도 제안 `proposal-layout-constraints/logical.svg` | 2932 × 1680 | 21 / 22 | 확인 범위 통과, 원본 미반영 |

## 원본에서 확인한 문제

| ID | 위치 / 발생 조건 | 영향 | 별도 제안에서의 처리 |
|---|---|---|---|
| R1 | `LB --> CP`가 Harbor 노드 뒤를 통과 | API LB–Control Plane 경로가 Harbor에 연결된 것으로 오독 가능 | Harbor를 LB보다 앞 단계에 배치 |
| R2 | `API --> ENG`가 exporter 노드 뒤를 통과 | API–Engine 통신 경로 추적 방해 | exporter를 API보다 앞 단계에 배치 |
| R3 | `PM --> MGW`가 Worker와 GitHub 노드 뒤를 통과(2곳) | remote-write 경로가 끊기거나 중간 노드를 경유하는 것으로 오독 가능 | runner를 Prometheus보다 앞 단계에 배치 |
| R4 | `6443 deploy` / `Blackbox TCP6443` 라벨 경계가 약 4.25 × 21px 겹침 | 가까운 두 연결선의 라벨 식별이 불편함 | 배치 변경 후 겹침 해소 |

R1–R3은 도식 연결 관계의 판독을 방해하는 렌더 차단사항이다. R4는 부수 가독성 문제이며 동일 제안에서 함께 해소됐다. 원본 MMD의 아키텍처 내용이 틀렸다는 판정은 하지 않았다.

실제 확인 이미지: `logical.png`, `physical.png`, 원본 `logical-left/right-inspection.png`, `physical-left/right-inspection.png`, 최종 제안 `logical.png`와 `final-label-inspection.png`, `final-left-inspection.png`, `final-right-inspection.png`. 전체 이미지에서 경계·클러스터·노드·방향을 확인하고 확대 이미지에서 가려진 경로와 라벨을 확인했다. 검사 crop의 경계에서 잘리는 부분은 원본 이미지의 잘림이 아니다.

## 최종 별도 제안

원본 문구와 표시 연결선을 그대로 두고 보이지 않는 배치 제약 4개만 추가했다: `EXP ~~~ API`, `HBR ~~~ LB`, `RUN ~~~ PM`, `DB ~~~ HBR`. 이 제약은 네트워크 연결이 아니며 화면에 표시되지 않는다. 제안 MMD와 원본의 차이는 `LAYOUT_ONLY_PROPOSAL.patch`에 있다.

배치 후 `30080`과 `remote write` 라벨이 겹치는 회귀가 나타났다. 간격 조정 2회로는 해소되지 않았고, 세 번째 추가 조정에서 렌더 스크립트가 remote-write 라벨만 SVG 좌표 `(160, 12)`만큼 같은 연결선을 따라 옮기도록 했다. 문자열·표시 연결선·아키텍처 값은 바꾸지 않았다. `RENDERER_LAYOUT_PROPOSAL.patch`와 실행 가능한 `proposal-layout-constraints/render-proposal.cjs`에 정확한 처리를 남겼다. **MMD 패치만 적용하면 라벨 이동이 재현되지 않으므로 렌더 스크립트와 함께 검토해야 한다.**

최종 제안의 표적 재검증 결과:

- 문법·렌더 rc 0, 21개 노드와 22개 표시 연결선 유지.
- 노드 문구·표시 연결선 ID·라벨 문구 일치(`SOURCE_SEMANTICS_CHECK.json`).
- 실제 확대 이미지에서 기존 4곳의 가림, 새 라벨 겹침, 잘림이 해소됨을 확인.
- 보조 기하 검사에서 무관한 노드–연결선 교차 0, 연결선 라벨–노드 겹침 0, 서로 다른 연결선 라벨끼리 겹침 0(`PROPOSAL_GEOMETRY_REVIEW.json`).
- 노드 내부 라벨 넘침 0. 전체 SVG 범위 안에 도식이 포함됨을 이미지로 확인.

기하 검사는 브라우저 SVG 경로를 1px 간격으로 표본화하고 노드 내부 2px 여유를 적용한 보조 검사다. 시각 검토를 대체하거나 수학적 무교차를 증명하지 않는다. 연결선끼리의 교차는 남지만 접점으로 표시하지 않았고 경로와 끝점을 추적할 수 있다. 기본 테마의 반투명 라벨 배경 뒤로 선이 보이는 부분은 남아 있어 100% 확대 또는 SVG 확대 열람을 권장한다. 축소 overview는 전체 배치 파악용이다.

`proposal-check/`의 LR 방향 시도, `pre-spacing-logical.svg`, 이전 `label-inspection.png`, `PRE_SPACING_BASELINE.json`, `SPACING_TRIAL_1/2.json`은 검토 이력이다. 최종 제안은 위 표의 경로와 FINAL_BINDING에 지정한 해시로만 식별한다. 초기 RENDER_RECEIPT의 `VISUAL_REVIEW_PENDING`은 렌더 당시 상태이며 최종 시각 판정은 이 문서와 FINAL_BINDING에 있다.

## 판정의 한계

고정 후보에 있는 값의 렌더·표기만 검토했다. 서버 조회, 제품 테스트, CI, GitHub 변경, 공식 채택·발행·Freeze·최종 인수는 수행하지 않았다. 고정 후보 이후 Harbor 18:11 등 새 상태를 반영하지 않았다. 다른 Mermaid/Chrome/글꼴 버전에서 같은 배치를 보장하지 않으며, 해당 환경 변경 시 배치 재검토가 필요하다.
