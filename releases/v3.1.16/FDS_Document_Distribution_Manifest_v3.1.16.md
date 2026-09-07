# FDS Document Distribution Manifest v3.1.16

> **Release Date:** 2026-09-03  
> **Decision:** D36 — Fixed / User Approved  
> **Active Baseline:** `FDS_Project_Implementation_Baseline_v3.1.16.md`  
> **Distribution Unit:** `FDS_v3.1.16_Team_Availability_and_Status_Release_Package.zip`

---

## 1. 배포 파일 및 SHA-256

| File | Version | SHA-256 | State |
|---|---|---|---|
| `FDS_Project_Implementation_Baseline_v3.1.16.md` | v3.1.16 | `623f37afee182befc79d88400574f0f49678d11d360a3dacfdcbcae2edaf8d38` | RELEASED |
| `D36_Team_Availability_and_Status_Update_Record_v1.0.md` | v1.0 | `99d9b51efd7f4d8a3b23a6d686cf6601ac8b934032365b396c1dcd3c4ae32b4e` | APPROVED |
| `FDS_v3.1.16_WBS_and_Gantt_v1.0.xlsx` | v1.0 | `b7df98c051658c6be58a146ccf6eec2909a33eb1be80cb09f383b5e61d4ab306` | RELEASED |
| `FDS_v3.1.16_Canonical_Ticket_Update_Pack_v1.0.md` | v1.0 | `bd43a05118dbd37571eb984c58d1cc886e345a68f59be41b2c40906c167b0893` | RELEASED |
| `FDS_Project_Implementation_Baseline_Release_Notes_v3.1.16.md` | v3.1.16 | `56a703f87d53f2eefde73d112e20bbf3fef19ef1a2812b9f9acb6cb6f1655e4f` | RELEASED |

본 Manifest는 자기참조 Hash를 포함하지 않는다. 배포 ZIP의 무결성은 동명 `.sha256` Sidecar에서 통제한다.

## 2. 배포 판정

| Control | Result |
|---|---|
| D36 사용자 승인 | PASS |
| WBS record count 51 / unique IDs 51 | PASS |
| Status 집계 3 / 6 / 0 / 42 | PASS |
| 09-04 개인 부재와 Global Non-working Date 분리 | PASS |
| Phase 1 Gantt Leave Marker 3개 | PASS |
| Formula Error 0 | PASS |
| P1-DNS Done / P1-K8S In Progress / P1-LB In Progress | PASS |
| G2/G3/Phase 1 Close 불변 | PASS |

## 3. 수신자 적용 지침

1. ZIP Sidecar 또는 개별 파일 SHA-256을 확인한다.
2. v3.1.15는 이력으로 보존하고 v3.1.16을 Active Baseline으로 전환한다.
3. WBS/Notion에는 `FDS_v3.1.16_Canonical_Ticket_Update_Pack_v1.0.md`의 영향 티켓만 Upsert한다.
4. 09-04를 공통 휴무일로 추가하지 않는다.
5. P1-LB-01은 Stage B 완료 전 `Done`으로 변경하지 않는다.

**DISTRIBUTION_MANIFEST_VERDICT=RELEASED**
