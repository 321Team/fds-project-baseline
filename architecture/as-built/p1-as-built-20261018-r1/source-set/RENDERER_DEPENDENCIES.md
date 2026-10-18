# 필수 렌더 계약과 재현 의존성

2026-10-16 KST · 기존 QA 결과 재사용 / 이번 렌더 미실행

| 구성 | 기존 검증 버전·내용 |
|---|---|
| Mermaid | 11.17.0, VS Code 1.138.0에 포함된 로컬 ESM 번들 |
| 실행기 | Node v24.19.0, Playwright 1.62.1 |
| 브라우저·글꼴 | Chrome 155.0.8059.80, Windows Arial |
| 기본 설정 | strict / default theme, Arial16, deterministic IDs, `htmlLabels=false`, `curve=basis`, nodeSpacing50/rankSpacing50/padding15 |
| 필수 후처리 | PM→MGW remote-write 라벨 1개에 SVG `translate(160 12)` 적용. 문자열·연결선 경로 변경 없음. 해당 라벨이 정확히 1개가 아니면 중단 |

[실행 가능한 제안 renderer](payload/current/render-validation-20261016/proposal-layout-constraints/render-proposal.cjs) SHA256 `439f766a97e65e7c87c2dbe9f81cbaaa7be706ee0aaa0d5a44705f030f7b4569`와 [config](payload/current/render-validation-20261016/proposal-layout-constraints/RENDER_CONFIG.json)을 함께 보존한다. [renderer receipt](payload/current/render-validation-20261016/proposal-layout-constraints/RENDER_RECEIPT.json)의 실제 실행 경로·시각·rc0와 [자산 manifest](payload/current/render-validation-20261016/proposal-layout-constraints/RENDERER_ASSET_MANIFEST.json)의 로컬 JS 28개 hash를 재사용했다. 이번에는 설치된 28개 자산의 hash가 같은지만 확인했다.

필요한 설치 경로:

```text
C:/Users/soldesk/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe
C:/Users/soldesk/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright
C:/Program Files/Google/Chrome/Application/chrome.exe
C:/Users/soldesk/AppData/Local/Programs/Microsoft VS Code/7debcd0e2a/resources/app/extensions/markdown-language-features/markdown-editor-out/
```

향후 재현이 필요할 때의 실행 위치는 `payload/current/render-validation-20261016/proposal-layout-constraints/`이며 명령은 다음과 같다. **이번 작업에서는 실행하지 않았다.**

```powershell
& 'C:/Users/soldesk/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe' './render-proposal.cjs'
```

스크립트는 같은 폴더의 SVG/PNG/config/receipt를 다시 쓴다. 결속된 묶음을 보존하려면 상대 구조를 유지한 새 검토 사본에서만 실행한다. 로컬 논리 제안, 두 단계 위의 원본 논리·물리·설명·부모 binding이 필요하며 이 묶음에 들어 있다. Mermaid 번들은 설치 위치에서 읽고, 전용 headless 브라우저와 일회성 127.0.0.1 서버를 사용한다. 해당 브라우저의 외부 요청은 차단하며 운영 서버나 사용자 브라우저 세션을 사용하지 않는다.

정상 기준은 rc0, 정확한 입력/자산 hash, 21개 노드·22개 표시 연결선과 문구 보존, 그림의 가림/잘림/라벨 충돌 회귀 없음이다. 입력·설치 경로·버전이 달라졌으면 임의 설치·버전 교체로 계속하지 않고 해당 파생물 사용을 보류한다. 실패 산출물을 공식 파생물로 사용하지 않으며 원본은 유지한다. 운영 변경이 없어 서버 복구 절차는 필요하지 않다.

이 제안은 특정 source·renderer·글꼴 조합에 대한 보정이다. MMD만 다른 Mermaid 화면에 붙여 넣거나 renderer 위치/설정을 바꾼 결과에는 기존 시각 판정이 자동 적용되지 않는다. 공식 채택에서는 source version과 renderer hash를 SVG의 출처로 함께 기록해야 한다.
