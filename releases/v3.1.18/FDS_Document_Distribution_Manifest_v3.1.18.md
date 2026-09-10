# FDS v3.1.18 Document Distribution Manifest

> CANDIDATE / 2026-09-10 · 이 후보는 아직 발행되지 않았다.

## 배포 범위

- Baseline·WBS/Gantt·Ticket Pack·64개 Description·원본 스냅샷·감사·Release Notes·WEB·기존 속성 정책 및 검증 도구를 함께 배포한다.
- `CURRENT.md`는 현재 발행 정본 v3.1.17의 검토 맥락이다. v3.1.18의 RELEASED 표시는 승인된 finalization 단계에서 별도 확정한다.
- Architecture 자체의 변경은 없다. 기존 Baseline 내 Architecture/Interface 계약과 `architecture/README.md`의 관리 규칙을 유지한다. 과거 외부 산출물 참조는 이번 ZIP에 새 원본을 만든 것으로 간주하지 않는다.
- `governance/ticket-sync-map.json`은 이전 동기화의 고정 맵이다. Description 최신화 이후 재작성해야 하며 이 후보에서 apply하지 않는다.
- ZIP에는 아래 파일, 이 Manifest와 `releases/v3.1.18/SHA256SUMS`가 들어간다. Manifest 자신의 해시는 SHA256SUMS로 검증한다. SHA256SUMS는 자신을 해싱하지 않는다.
- ZIP sidecar는 ZIP 바깥에서 전체 바이트를 검증한다. ZIP/sidecar는 Git에 추가하지 않는다. `python3 scripts/build-canonical-package.py v3.1.18 OUTPUT_DIR`로 동일 ZIP을 재생성한다.
- 후보 검증: 저장소·Manifest·SHA256SUMS·ZIP의 WBS 바이트를 대조한다. 게시 후 독립 WBS Release Asset은 `--published` Gate에서 추가 대조한다. 미게시 Asset은 PASS가 아니다.

- K8S 최신 이력 편입 문서·고정 원문·보존 검증 결과를 포함한다. PR #3 보완 PASS/병합과 PR #2/#4 최신 구현·리뷰 상태를 구분한다.

## 파일별 SHA-256

| 경로 | SHA-256 |
|---|---|
| `CURRENT.md` | `7b85e4e4f2e2adc5809dab129a2011f4945fadef2d59af7979207b5855ea42e7` |
| `README.md` | `2bc3b2e303516103f263121df6a03ab9bdeefa025f29e277c0a7d75cdbef51e5` |
| `architecture/README.md` | `ece5d836bdcfdc6093635dd9cdfd4a966b014fb6c027a091f37d8fe1ddcddf48` |
| `audit/FDS_Canonical_Integrity_Audit_v3.1.18.md` | `c169a5729a8455ba010210ee7f92f833b2bd4d9b9ededc9c5b56005a0a46b349` |
| `audit/v3.1.18/fast-track-plan.json` | `ee757ce6102650b59cf367be3bf1ba8128768f4bb850cac81511f9c31b40a1d6` |
| `audit/v3.1.18/followup-20260910.json` | `10cb146fc4b2bcbf99129f88fdda9284c4fd8922eb1d1d45694c8b9b0e694102` |
| `audit/v3.1.18/k8s-intake-20260910.json` | `3fa7b0d26dbe2af31d610600d3c0111cbbb4044e35c843f7907534a1214858f7` |
| `audit/v3.1.18/k8s-intake-validation.json` | `df7bf23c276d10e13552b44fb29f63573bc18ab481e57cd97fd93c09f575fe24` |
| `audit/v3.1.18/property-delta.json` | `dd8d95d7b80a2cde9016bf9478432b752a0f5eec62f31bd00b7f55b29ff2dfde` |
| `audit/v3.1.18/validation.json` | `d89c4d3a637f163db05a6cae383c849a62a81943eabfe76d9a1a8c35bc61cc6a` |
| `baseline/FDS_Project_Implementation_Baseline_v3.1.18.md` | `cdaab94849e29f8210600f55933df903aa3cd9e8e06d6dd7162fb2fdc2b6bd37` |
| `governance/GITHUB_IDENTITY_MAP.md` | `162910ee52843352aa5a868cb79bc76bf7b6ea5ddde35f022d1a7ba34c3ba2bc` |
| `governance/GITHUB_LABEL_SCHEMA.md` | `9d07c160d20b8e43b90ca1047b0c263ddcad2f3d2af968c3a583c6a69e9bd8ff` |
| `governance/GITHUB_MILESTONE_MAP.md` | `bfe9087c24df0938df1e0f777e26fb6c4f0f3444de7f257ab2b17e8e1757625b` |
| `governance/RELEASE_POLICY.md` | `dfe7643b67542724cdc904b957c64d7f5f8f345eb5c857498f8d42bf7b679ca6` |
| `governance/TICKET_SYNC_POLICY.md` | `69cb9277e31b74358b6c6ea53e99251609186584e7289068310b91d8a60f3a68` |
| `governance/TICKET_SYNC_RUNBOOK.md` | `eae4da7f455e01c52ed3a0ccee5e66334f4a7443240568da5cc25010728a073e` |
| `governance/ticket-sync-map.json` | `deae909490f3259120618ce1f2516ab8303ed54c94a2d6c78efdbaaa874a95e7` |
| `releases/v3.1.18/FDS_Canonical_Consolidation_Record_v3.1.18.md` | `77ae040ec8f46d4c44d31b4f589b9dd82dedf1e51ba6b02bd34a3f8601b1acaa` |
| `releases/v3.1.18/FDS_K8S_Candidate_Integration_20260910.md` | `e34b9717e21de0493df0c08daee6ada2ae84e7cceab26cb359b09282c6a5b2d6` |
| `releases/v3.1.18/FDS_Phase1_Fast_Track_Schedule_Recommendation_v1.0.md` | `54479010be0777e3e5743871bdf048a9bd09176bad8d22f7c16fc8cf35b3a023` |
| `releases/v3.1.18/FDS_Project_Implementation_Baseline_Release_Notes_v3.1.18.md` | `5675937b293be5476518668be032d7e287d47e4edd82bb743b64eef6341c2194` |
| `scripts/build-canonical-package.py` | `3cd8825ae9a84e680aae361728833c80f1e17bc60f70127d4f3d19f19a5cb299` |
| `scripts/publish-canonical-release-assets.sh` | `509e61e15ee1a5681730f559838f36b0c3fdd0cbcf3b1f8cc43db15b2a72752a` |
| `scripts/ticket-sync.py` | `f4440607707cbb466f85903369cb3caede820983e11f6386a99cf8622278ae85` |
| `scripts/verify-canonical-release.sh` | `072a4296ec923edb676c1afeb81a5695fced25da0430e3903600241b0c45b3ad` |
| `scripts/verify-v18-candidate.py` | `aac7bf1e5f8ff117211be2981f269cb0c2f752fdc28e0ae01022da51caddc60a` |
| `scripts/verify-wbs-gantt-distribution.sh` | `139e45ba113d08df98bd58f7b4ad864822b459dd10e04422e6fe12ff63c7c774` |
| `tests/test_ticket_sync.py` | `e2d030151ade38c0e0506f2b0f64a69f19d7f561bbb8072a8d7b8c57a7ca1bef` |
| `tickets/CR-P1-ANS-01-01_Notion_Description_v1.1.md` | `bdfefae5c63040286b03810acefbeb2d94a02bb4da2eb54cee8a14bb0d249d64` |
| `tickets/FDS_v3.1.18_Canonical_Ticket_Update_Pack_v1.0.md` | `9784319fbf52c76feb72412151afb5e3432e2133afeab849df346640d8a47365` |
| `tickets/v3.1.18/canonical-records.json` | `4f624bfaabbb5dfd2b87f56f8757cdb1c77f6dc5a82bb28fd91ed75e5e74211e` |
| `tickets/v3.1.18/descriptions/CR-P1-ANS-01-01.md` | `7de7244faceb3e2701103b38efcc7db29db5e38516dea220d50e5115fa773b4f` |
| `tickets/v3.1.18/descriptions/D-ARC-01.md` | `e3a445a6e12c757cdc7b1bf4e9f1811a16c0ce1c317a73f41da1403538274aa3` |
| `tickets/v3.1.18/descriptions/D-NET-01.md` | `208df5f4567473b735d2ee35930f216cb20c8b28e84330380a53bc389a1992d4` |
| `tickets/v3.1.18/descriptions/D-SEC-01.md` | `c2788ef64e060dbc2c78044f08f899ad5efc8867b95bfd8344a9c15639a5bb60` |
| `tickets/v3.1.18/descriptions/D-WBS-01.md` | `324f02659dc614644377110466917670bc20743059b925a272b7e0516e3f0a2e` |
| `tickets/v3.1.18/descriptions/DEC-CAL-P1-01.md` | `e61866e38932e5c5d3e03f100c27551125206e8d2e38360dbdbe5c1fb8fe562c` |
| `tickets/v3.1.18/descriptions/DEC-CAL-P2-01.md` | `696f57e58cf760cffeecbbd037724b0401b85e18261c4fe8328bad2973c1ab97` |
| `tickets/v3.1.18/descriptions/DEC-P1-ADMIN-01.md` | `fcb8ccf03c6d9675f6fd678b68cc426b2f33b887458aeabe22f22b5eae59e86a` |
| `tickets/v3.1.18/descriptions/DEC-P1-ENTRY-01.md` | `a56a3e1e1632dfecc5883aa9b65af3ab7e66b8072f69314a7988f7aa988dad88` |
| `tickets/v3.1.18/descriptions/DEC-P1-FDS-01.md` | `2c72437d61d0dfa684bc64483f279379f77ca527bfab142c6ca14f76adb7a40e` |
| `tickets/v3.1.18/descriptions/DEC-P1-MON-01.md` | `bed9a5110b61d1112fb87c0c1d1dd5533bf14801f5a4d20877e8e3319b4db706` |
| `tickets/v3.1.18/descriptions/DEC-P1-TLS-01.md` | `3ab45a7ac66c24f3cec0d795f8d1d061dd2645263cde2645dd119cc47de47388` |
| `tickets/v3.1.18/descriptions/DEC-P1-TXN-01.md` | `a5f5ca661fa8cb531331ac2cb4847763073ee640c36cfb831d566be16ba179e2` |
| `tickets/v3.1.18/descriptions/DEC-P2-DNS-01.md` | `5b0830b1ae42812f5f3f1203ed0eca070b4c5cf5b60f5a3b08f3701f8292266a` |
| `tickets/v3.1.18/descriptions/DEC-P2-OP-01.md` | `5c96b3dd6356564490cc6c20bb8137b59b472832ca26ef9a3ae01eb10f2fc778` |
| `tickets/v3.1.18/descriptions/DEC-P2-REG-01.md` | `a0aca1b92318e5b972504a9ee05b0759c154ce999327c9f43faab631007a9a22` |
| `tickets/v3.1.18/descriptions/ICR-D-NET-01-01.md` | `e7578d5f540ad0abbf3793008b42473c25f2187d378719a916ba8c12994827a5` |
| `tickets/v3.1.18/descriptions/MS-DELIVERABLE-FREEZE-01.md` | `3f7f150a643e37015138288513a3df780afe851a18c7028ab321b9c369388895` |
| `tickets/v3.1.18/descriptions/MS-G0-01.md` | `46aefe8b2cb7187017614f2b61bb7f09ead82ea9ebe3f83493d5366eea753f10` |
| `tickets/v3.1.18/descriptions/MS-G1-01.md` | `c5f6dcde2da6560340d0d49d2e0230b7160c7f9d62901e65a941e2e913f56774` |
| `tickets/v3.1.18/descriptions/MS-G2-01.md` | `4b3a6d9d1b44c15ed0877ede85908a08e8d2daf12da60220ad2a1bca3aa281fb` |
| `tickets/v3.1.18/descriptions/MS-G3-01.md` | `f9dcd8513c9838fb16f548cb89dfc6b0a7a3a1cf9be1c96c7c721a0c3630f893` |
| `tickets/v3.1.18/descriptions/MS-G4-01.md` | `68cdff098b24e11bb1e3bd5d312b8c801513284855885b07afc2ab7bfddd6fea` |
| `tickets/v3.1.18/descriptions/MS-G5-01.md` | `a77b5e2b864cad1b36bba3bb78e27bfdb258273f4c7768c7749109df22f414b8` |
| `tickets/v3.1.18/descriptions/MS-G6-01.md` | `5d99113e6c9ac6bd5f226ab7880c2240d3d7434fd9298843dd1f3f9f37756359` |
| `tickets/v3.1.18/descriptions/MS-P1-CLOSE-01.md` | `f4c029ff4a1499f32e0f53f0a4c82aa56721e78182589a3bc04df8e00d6f8ca2` |
| `tickets/v3.1.18/descriptions/MS-P1-REVIEW-01.md` | `21b43a8f9d31468b74f7cbe11d03eef7f09276484d209a6ce436ff40706013bf` |
| `tickets/v3.1.18/descriptions/MS-P2-REVIEW-01.md` | `fda81eb9fb9218cf63dd198059d98ba78c4be168f5de9f685ebbe19bfba7b9ca` |
| `tickets/v3.1.18/descriptions/MS-P2-START-01.md` | `934a3a59ca99eb809de2b98cb4d837a791dfa6a4346483dfb794fac1f6af6930` |
| `tickets/v3.1.18/descriptions/MS-PROJECT-CLOSE-01.md` | `96ed6b0af1384c1e4abcec623f803c71c4c2383e4cf47752b8a432fb7b966b36` |
| `tickets/v3.1.18/descriptions/P1-ANS-01.md` | `93b74b6e27abb077d7839e10c6978722644668f08de1e031cfc3224518d700f5` |
| `tickets/v3.1.18/descriptions/P1-APP-01.md` | `163e1351847882bfbd85c58d002f1172339c06efac138bc45b24b9cc102c4f19` |
| `tickets/v3.1.18/descriptions/P1-CICD-01.md` | `a68bb4ae1a864a7e61828aea466348a1533d69273d5bceaa6a78354620858096` |
| `tickets/v3.1.18/descriptions/P1-DB-01.md` | `536402077bd2be72e81141a54f1670d29154e0bcb2def334a4dd4585c85add80` |
| `tickets/v3.1.18/descriptions/P1-DNS-01.md` | `5936ce5409e79a824ce94cb4552e3a118b76f5db5519d9bdf44192f6e600bc5c` |
| `tickets/v3.1.18/descriptions/P1-DOC-01.md` | `c1524e6df8f59e6cc570e20f1f38a3f720e4e2452a67b1d71725c05a3c7276a5` |
| `tickets/v3.1.18/descriptions/P1-DR-01.md` | `d8ca7f809919e94e18756706f2c6b81a7de9a9e5543d0b7c723bdde49307ac0a` |
| `tickets/v3.1.18/descriptions/P1-DR-02.md` | `e296cd9ac234688463ebad562f537c532c78a1c8244fb4b2de0d76c8a9207d83` |
| `tickets/v3.1.18/descriptions/P1-E2E-01.md` | `9fd96bf5a175800a657f41cac11a475cd8a6bee549dc70bfe118f413de7372c3` |
| `tickets/v3.1.18/descriptions/P1-HA-01.md` | `409c24c6794c69d187783773fd52427b6d37b00f698aee064a633e4781c2c3a0` |
| `tickets/v3.1.18/descriptions/P1-HA-02.md` | `6757ed92cfe9e7104015fad898abb774425bfd6e92f4523c0c66e7c9048545cb` |
| `tickets/v3.1.18/descriptions/P1-HBR-01.md` | `ac61d9088d428764052d2addfb0f7719a17f3a5a7b0e61431b5aca0820f4643b` |
| `tickets/v3.1.18/descriptions/P1-K8S-01.md` | `604fe801857b3bb21583d26f91855b51becde07af16e58c3a228e0dc1d993fef` |
| `tickets/v3.1.18/descriptions/P1-LB-01.md` | `f2ab959376b6bef6b24f11bc883ab60815aec15a13755170b691bf0d2c72f515` |
| `tickets/v3.1.18/descriptions/P1-LNX-01.md` | `285152b947ac3ec15a1ef2d6da13ea43343a54e84c5012407b98a75b65d9d908` |
| `tickets/v3.1.18/descriptions/P1-MON-01.md` | `5228564546d61ade4547a35ef8272b9396711c1c5e942d42f4bdbba576d7a597` |
| `tickets/v3.1.18/descriptions/P1-MON-02.md` | `06e49a761bcc3b3fccc0c4159b4f68dada36623596cfab42da84691dc7958967` |
| `tickets/v3.1.18/descriptions/P1-NET-01.md` | `7bd048b9b528dda29d992706b7befcde882940dcaf18c45fd43cd2c924e2a39a` |
| `tickets/v3.1.18/descriptions/P1-REV-01.md` | `869995fddc19b5fb7d06ad5a3c97b66a0e28b4109bf8ff132d8524ad5a338bc7` |
| `tickets/v3.1.18/descriptions/P1-SEC-01.md` | `7c16a6498d6b2c3051680c7da4efba5de3ed294fda2f96495ff9d182a4d5c46e` |
| `tickets/v3.1.18/descriptions/P2-APP-01.md` | `25186f986668ef56e404ff5b6e88db96fd4fca502725f030ce806308975b70cb` |
| `tickets/v3.1.18/descriptions/P2-ARC-01.md` | `7ee5047c8062d904038811ba2906eb476af0aa4758ac5a97797a2b5dcf1d2587` |
| `tickets/v3.1.18/descriptions/P2-CICD-01.md` | `a7c3b16b491b416781479ba654f888a2a28995a68595e4d4e74b01e676d9ae83` |
| `tickets/v3.1.18/descriptions/P2-DNS-01.md` | `beb1650669b0884b4110a8a093b533c9028385b6f84e6d49c72db5a6a6a19bd0` |
| `tickets/v3.1.18/descriptions/P2-DOC-01.md` | `07299af8ce2caf912e1addb42602e61b28618947b1506a05cd9235e195b16ed4` |
| `tickets/v3.1.18/descriptions/P2-E2E-01.md` | `e5ea8e5af0fcc562ee337fb47d855833d54328b66b65ff09b16ac495728105d4` |
| `tickets/v3.1.18/descriptions/P2-HYB-01.md` | `fb43d9c80d52563e6b606ede22141eeee5b9acc3c4f82ca0f57589aa380d1ad4` |
| `tickets/v3.1.18/descriptions/P2-IAC-01.md` | `d7f778692ed8d8bdad8abc188c69d6d56b54e5d39128220bafb5ec58a8845691` |
| `tickets/v3.1.18/descriptions/P2-OADP-01.md` | `5c310d6034498e2bb63faea02cc44e31518a267a56cd3da32397fc6cc21883d5` |
| `tickets/v3.1.18/descriptions/P2-OCI-01.md` | `74feb615cd70660a4e2825d7e7d510f18b845c96e0c4c2984ceafa63f4193f97` |
| `tickets/v3.1.18/descriptions/P2-OP-01.md` | `e11ba2311a72c732e1bd5b9422fe5a5e0721b6a4d263a515972cc22bf2ed3c35` |
| `tickets/v3.1.18/descriptions/P2-REV-01.md` | `20572a5a245aab419791a70477a89162e3649875cffb46e15e16574d00c8ba7b` |
| `tickets/v3.1.18/descriptions/P2-ROSA-01.md` | `cbbf361749b7c3ff4cb78a2ba004852907c56df410d24204a3391691a5f76463` |
| `tickets/v3.1.18/descriptions/P2-VPN-01.md` | `856e5a8f7eee25bd24e27c37626694276a731eb7654f44a123e2488b6d659cc1` |
| `tickets/v3.1.18/source-snapshot.json` | `9afcc11674292dadc9ac6c1f58c8e39d99cd2abd5aae9220d4226f59d9bdaf8e` |
| `wbs/FDS_v3.1.18_WBS_and_Gantt_v1.0.xlsx` | `38b0737b7718a8c5b271537f0c10a2d7c226dd850269fbf7b058bc376a446287` |
| `web/FDS_v3.1.18_Canonical_Status.html` | `3ba1de4c726cdde10894f2c0680aa3aef3aa9835c2f26f9595d9b85926d376c8` |
