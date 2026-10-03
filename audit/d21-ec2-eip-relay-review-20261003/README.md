# D21 후보 심층 리뷰 — AWS EC2 + EIP Relay 설계 성립성 — 2026-10-03 KST

사용자 요청: "OCI Relay를 사용하고자 하였으나 기술적 제약으로 EC2+EIP Relay 구조로 알아보고 있어, 심층 리뷰로 설계적으로 성립되는지 확인." 읽기 전용 검토 결과다. **D21 판정, Status·AC 변경, 리소스 생성·변경은 하지 않았다.** D21 결정권자는 담당 Lead다.

- 검토 대상: [#36 D21 candidate contract v1](https://github.com/321Team/fds-project-baseline/issues/36#issuecomment-5964496677)(2026-10-03 11:15 KST), [#37 runtime handoff draft](https://github.com/321Team/fds-project-baseline/issues/37#issuecomment-5964501246)
- 대조 기준: 정본 `docs-v3.1.20`(Baseline §1.4·§6·§13·§15, IF-17~IF-20, D10·D21), #36·#37 코멘트 전체(2026-10-03 02:15 UTC까지)
- 검토 시점 main: `67ba6cf`

## 1. 결론

**조건부 성립(Design-Feasible with conditions).** 토폴로지 자체는 표준 구성이다. VPC 안의 self-managed IPsec 장비, EIP 고정 endpoint, source/dest check 해제, VPC route의 ENI target, 동적 peer를 받는 Libreswan responder(`right=%any` + 명시 ID) 조합에 설계상 모순은 없다.

다만 계약 v1에 아래 4건이 빠져 있거나 미검증이다. 이 4건이 해소돼야 "D21 decision-ready"라고 할 수 있다.

| # | 항목 | 성격 | 계약 v1 반영 |
|---|---|---|---|
| B1 | 교육장 다중 WAN에서 IKE 포트 전환(UDP 500→4500) 때 Public IP가 바뀔 위험 | **차단 후보** — Runtime 검증 전 성립 여부 미정 | 없음 |
| B2 | MTU/PMTUD — AWS VPC 9001 MTU와 IPsec 인터넷 구간 1500의 불일치 | 기능 결함 위험 | 없음 |
| B3 | Route target 내구성 — 인스턴스 교체 시 ENI route blackhole | 복구·재현성 결함 | 없음 |
| B4 | On-Prem 복귀 경로 + vpn-gw01 masquerade/forward 정합 | 기능 차단 | 일부(복귀 route만 PENDING으로 명시) |

설계 결함은 아니지만 결정 전에 필요한 거버넌스 항목이 별도로 있다(§5). 정본은 Primary를 `OCI Relay → AWS S2S VPN`으로 고정해 두었다. EC2 Relay를 채택하면 AWS 관리형 Site-to-Site VPN을 아예 쓰지 않게 되므로 Baseline §1.4·§13, D10, IF-17, P2-VPN-01 문구와 어긋난다.

## 2. 전제 정정 — "OCI는 기술적으로 불가"는 증거와 다르다

#36 기록 기준으로, OCI 경로를 접게 만든 것은 기술적 불가가 아니라 **복잡도·지속성·일정의 불리함**이다. D21 기록에 사유를 이렇게 적어야 추적성이 유지된다.

| 관측 | 근거 | OCI 경로에 미치는 영향 |
|---|---|---|
| DRG는 on-prem attachment 간 transit을 하지 않음 | #36 09-29 공식문서 조사 | Managed DRG Relay는 불가. **Compute Relay로 우회했고 성공** |
| Always Free A1/E2 Osaka OHC | #36 10-02 Capacity Report | 무과금 지속 운영은 불가. E5(Trial credit) 경로로 대체 |
| E5 Relay local prerequisite·reboot persistence | evidence #95 merged `d2791df` | **OCI Relay VM 자체는 동작 확인** |
| 교육장 Public IPv4 회전(`121.160.42.93`↔`180.80.107.14`) | #36·#37 10-03, evidence #104(리뷰 대기) | **OCI·EC2 양쪽에 똑같이 적용된다.** 이 제약이 제외시키는 것은 IP 기반 Direct AWS CGW다 |

따라서 EC2 Relay를 고르는 정당한 이유는 다음과 같다. OCI 2-leg(On-Prem↔OCI↔AWS S2S)의 터널 2개·route 2단·장애 지점 2개를 1-leg로 줄인다. 클라우드 공급자를 AWS 하나로 모은다. 30일 Trial credit 의존을 없앤다. "OCI가 안 돼서"가 아니라 "더 단순하고 재현 가능해서"로 기록해야 한다.

## 3. 차단 후보·결함 상세

### B1. 다중 WAN 회전과 IKE/NAT-T 포트 전환 — 최우선 검증

**관측:** vpn-gw01에서 5초 간격 HTTPS 12회 중 두 IP가 6:6으로 나왔다. 새 연결마다 WAN을 고르는(per-connection) 부하분산과 일치하는 패턴이다. 단, HTTPS 표본만으로는 UDP 동작을 증명할 수 없다. #36 10-03 코멘트도 같은 한계를 명시했다.

**위험 메커니즘:**
1. IKEv2 initiator는 `IKE_SA_INIT`을 UDP 500으로 보낸다. NAT를 감지하면 `IKE_AUTH`부터 UDP 4500으로 바꾼다. 5-tuple이 달라지므로 per-flow 부하분산에서는 **다른 WAN, 다른 Public IP로 나갈 수 있다.** 이 패턴이 그대로라면 약 50% 확률이다.
2. responder가 `IKE_SA_INIT`과 다른 IP에서 온 `IKE_AUTH`를 받아들이는지는 구현에 달렸다. RFC 7296 §2.23은 NAT 뒤 peer의 주소 갱신을 허용한다. Libreswan 5.4의 실제 동작은 **이 세션에서 확인하지 못했다**.
3. 수립 뒤에도 NAT 매핑이 만료되거나, rekey 또는 DPD 뒤 재수립이 새 flow로 나가면 peer IP가 바뀐다. 이 경우 Child SA의 outer 주소가 갱신돼야 한다.

**판정:** UDP 4500 flow 하나가 keepalive로 유지되면 대체로 고정되므로 성립할 가능성은 있다. 그러나 **실측 전에는 "성립"이라고 쓸 수 없다.**

**권장 검증 — AWS 리소스 생성 전에 할 수 있다.** 이미 있는 OCI Relay(`129.225.204.87`, tcpdump 가능)를 NAT 특성 관측 대상으로 재사용한다. 클라우드 종류와 무관하게 교육장 NAT의 동작만 측정하는 시험이다.

```text
전제: OCI NSG에 관측 기간 한정 UDP/500·4500 ingress 임시 추가(관측 후 즉시 제거·read-back)
OCI relay:  sudo tcpdump -ni enp0s5 'udp and (port 500 or port 4500)'   # Pluto 중지 상태 또는 별도 포트 사용
vpn-gw01:   sudo systemctl stop ipsec
            for i in $(seq 1 20); do
              echo p500-$i  | nc -u -w1 -s 10.1.93.51 -p 500  129.225.204.87 500
              echo p4500-$i | nc -u -w1 -s 10.1.93.51 -p 4500 129.225.204.87 4500
            done
            sudo systemctl start ipsec
정상 판정: 같은 회차(i)의 500/4500 source IP가 20회 모두 동일 → B1 위험 낮음
실패 판정: 불일치 1회 이상 → 아래 완화책 중 하나를 D21 계약에 필수로 넣는다
추가 관측: 4500 flow를 20초 keepalive로 30분 유지하면서 source IP·port 변화 여부 확인
```

**완화책(불일치 시, 우선순위 순):**
1. **IKEv2 over TCP(RFC 8229).** Libreswan의 `enable-tcp=` / `tcp-remoteport=`를 쓴다. TCP 연결 하나로 묶이므로 WAN이 고정된다. 처리량은 줄지만 PoC 범위의 DB·이미지 트래픽에는 수용 가능하다. 설치된 5.4의 `man ipsec.conf`로 키 이름과 동작을 확정해야 한다.
2. responder 주소 갱신 동작을 Runtime으로 확인하고, IKE 수립 성공률·재수립 시간을 측정해 수용 기준을 정한다.
3. 교육장 NAT에서 `.51`의 출구를 고정(source-based policy)한다. 시설 협조가 필요하므로 P0 전제로 두지 않는다.

### B2. MTU/PMTUD 불일치

- AWS VPC 내부 ENI 기본 MTU는 9001(jumbo)이고, Relay가 인터넷으로 내보내는 outer 경로는 1500이다. NAT-T ESP overhead(약 60~80B)가 더해진다. TCP encapsulation(B1 완화책 1)을 쓰면 더 늘어난다.
- ROSA 노드가 큰 패킷을 Relay로 보내면 Relay가 ICMP Fragmentation Needed를 돌려보내야 한다. ROSA 노드 SG나 경로에서 ICMP가 막히면 **PMTUD black hole**이 생긴다. 그러면 TCP 연결은 맺어지지만 큰 쿼리 응답이나 이미지 layer에서 멈춘다. IF-18(PostgreSQL)·IF-19(Harbor)의 전형적 장애 패턴이다.
- **권장:** 양쪽 게이트웨이에서 터널로 가는 TCP SYN의 MSS를 고정 clamp한다. 계약에 "MTU/MSS 값과 근거"를 Interface 항목으로 추가하고, #37 Positive 시험에 대용량 응답 시험(예: 1MB 이상 SELECT 결과, 이미지 pull)을 포함한다.

```text
# 후보값 — 실측(ping -M do -s) 후 확정. firewalld와 별도 nft table로 관리, 파일 SHA256 증적화
table inet fds_vpn_mss {
  chain forward {
    type filter hook forward priority mangle; policy accept;
    ip daddr 10.20.0.0/16 tcp flags syn tcp option maxseg size set 1300   # vpn-gw01
    # Relay 측: ip daddr <승인 On-Prem 대상> … 동일 규칙
  }
}
```

### B3. Route target 내구성 — 인스턴스 교체 시 blackhole

- 계약 v1의 AWS route는 "approved On-Prem prefix → Relay ENI"다. 인스턴스 생성 때 자동으로 만든 primary ENI는 인스턴스와 함께 삭제된다. 그러면 Terraform 재적용이나 AMI 교체 때 route가 **blackhole**이 되고, EIP 연결도 풀린다.
- **권장:** ENI를 독립 리소스로 만든다(`delete_on_termination = false`). EIP association과 route target을 모두 **그 ENI ID**에 건다. 인스턴스는 그 ENI를 device index 0으로 붙인다. 이렇게 하면 인스턴스를 교체해도 EIP·route·SG가 유지된다. single Relay SPOF의 복구 절차도 "인스턴스만 재생성"으로 단순해진다.

```hcl
# 후보 패턴 — #35 Stage-A 모듈 반영 대상, 값은 Stage-A exact allocation으로 확정
resource "aws_network_interface" "relay" {
  subnet_id         = aws_subnet.transport.id
  security_groups   = [aws_security_group.relay.id]
  source_dest_check = false
}
resource "aws_eip" "relay" {
  domain            = "vpc"
  network_interface = aws_network_interface.relay.id
}
resource "aws_instance" "relay" {
  # ami, instance_type …
  network_interface {
    network_interface_id  = aws_network_interface.relay.id
    device_index          = 0
    delete_on_termination = false
  }
}
resource "aws_route" "to_onprem_db" {
  route_table_id         = aws_route_table.rosa_private.id
  destination_cidr_block = "10.1.93.55/32"   # 승인 대상만. /24 전체 아님
  network_interface_id   = aws_network_interface.relay.id
}
```

### B4. On-Prem 복귀 경로와 vpn-gw01 NAT/forward 정합

계약 v1은 db01의 `10.20.0.0/16 via 10.1.93.51`을 PENDING으로 명시했다. 다음 두 가지가 더 필요하다.
1. **vpn-gw01에서 masquerade 금지 확인.** Linux는 POSTROUTING SNAT 뒤에 XFRM policy lookup을 한다. 따라서 zone에 masquerade가 켜져 있으면 inner source가 `.51`로 바뀌어 selector 불일치로 터널을 타지 않는다. 정본의 "내부 SNAT 금지"(D14)도 위반한다. Baseline §6.4의 "외부 비내부 목적지 조건부 Masquerade"가 vpn-gw01에 적용되지 않음을 read-back으로 고정한다.
2. **단일 NIC hairpin forward.** db01 → `.51` → (ens160로 다시 나가는) ESP 경로다. firewalld zone `forward=yes`(intra-zone)와 policy가 이 흐름을 허용하는지 확인한다. 현재 #37 read-back에는 services·ports·rich rules만 있고 forward/masquerade 항목은 없다.
3. db01의 `pg_hba.conf`·firewall은 ROSA **노드 subnet** 기준으로 연다. OVN-Kubernetes 기본 SNAT 때문에 Pod IP가 아니라 노드 IP가 source로 보인다. #37 09-30 코멘트의 "실관측 후 확정" 원칙과 같다.

## 4. 조건부 수용 항목 — Lead 명시 수용이 필요

| 항목 | 리뷰 판단 | 수용 조건(권고) |
|---|---|---|
| SG UDP/500·4500 `0.0.0.0/0` | 동적 peer에는 불가피하다. 노출 대상은 IKE 2포트뿐이다 | IKEv2 전용, 명시 `leftid/rightid`, 32바이트 이상 난수 PSK(비밀저장소 보관, Git·state·증적에 남기지 않음), Libreswan DoS cookie 기본값 유지, VPC Flow Logs 또는 Pluto 로그로 비인가 시도 관측. **같은 VM 안에서는 Libreswan NSS의 프로젝트 자체 CA 인증서 인증도 추가 비용 없이 쓸 수 있다**(AWS Private CA와 무관). PSK 유출 위험이 수용 불가로 판단되면 이 경로로 전환한다 |
| Relay SG의 forwarded 트래픽 | 계약 v1에 없음 | source/dest check를 꺼도 SG는 Relay ENI에 적용된다. inbound는 ROSA 노드 subnet → `10.1.93.55:5432`(D22 선택 시 `.54:443`)만 허용한다. 이것이 AWS 계층의 "승인 TCP Path / 미승인 DENY" 통제점이 된다 |
| Traffic selector 범위 | 계약 v1의 AWS 측 `10.20.0.0/16` 전체는 과대하다 | `leftsubnet`을 ROSA private subnet으로, `rightsubnet`을 `10.1.93.55/32`(+D22 시 `.54/32`)로 최소화한다. route·selector·SG·pg_hba의 값을 같은 manifest 하나에서 생성해 drift를 검출한다(계약 v1 §6 취지와 일치) |
| Single Relay SPOF | PoC 범위에서 합리적 | 복구 시간(RTO) 측정을 #37 recovery 시험에 넣는다. B3 패턴과 EC2 auto-recovery 사용 여부를 기록한다 |
| 관리 경로 SSM | 적절 | instance profile(최소 권한)과 SSM endpoint 도달 경로(public subnet은 IGW)를 계약에 넣는다. 공인 TCP/22는 열지 않는다 |
| 인스턴스 `t3.medium` | 동작에는 충분 | t3 기본값은 Unlimited라 크레딧 초과 시 추가 과금이 생길 수 있다. `standard` 크레딧 모드로 설정하거나 `t3.small`로 낮출지 결정한다. 처리량 요구가 작으므로 실측 후 정한다 |

## 5. 정본·티켓 정합 — D21 채택 시 함께 처리할 변경

설계 결함은 아니지만, 이 항목들을 기록하지 않고 구현하면 정본과 실제가 갈라진다.

| 위치 | 현재 정본 | EC2 Relay 채택 시 필요 조치 |
|---|---|---|
| Baseline §1.4, §13 Primary | OCI VPN Relay → **AWS Site-to-Site VPN** → VPC | AWS 관리형 VPN을 쓰지 않는 구조로 바뀐다. 차기 정본 CR로 Primary 재정의 |
| §13 Fallback 순서 | 1 Vendor Public Endpoint → **2 AWS EC2+EIP Relay** → 3 Overlay | 1순위를 건너뛴 근거를 D21에 기록한다(IP 기반 CGW는 동적 IP로 제외, 인증서 기반 CGW는 AWS Private CA 비용·PKI lifecycle로 제외). Private CA 월 고정비는 이 세션에서 공식 가격표를 재조회하지 못했으므로 D21 전에 실제 금액으로 확인한다 |
| D10 "OCI Primary Transit — Selected/Validation" | 유효 | Superseded by D21 처리 |
| IF-17 "vpn-gw01 → OCI 및 OCI → AWS VPN" | PROVISIONAL | Producer/Consumer/Port를 vpn-gw01 ↔ AWS Relay EIP 단일 leg로 재정의(UDP 500/4500, B1 결과에 따라 TCP 4500 포함 가능) |
| IF-18/19 Acceptance | Source CIDR/SG/Route | 복귀 route(B4), MSS(B2)를 Acceptance 항목으로 추가 |
| P2-VPN-01 제목·AC | "OCI Relay / AWS Site-to-Site VPN", "Route 전파와 Static Route 권위 Source" | 제목 문구와 AWS VPN 전용 AC(route propagation)의 적용 범위를 Lead가 정리한다. **AI 도구는 본문을 직접 수정하지 않는다**(AGENTS.md). 교체 본문이 필요하면 plan으로 넘긴다 |
| 비용(DEC-P2-COST-01) | Target ≤$400 | EC2·EIP(Public IPv4 시간 과금)·인터넷 egress를 Cost-to-Complete에 추가. 규모는 기간 3주 기준으로 수십 달러 이하로 추정되지만 Seoul 단가는 이 세션에서 재조회하지 못했다 |
| OCI 잔존 자원 | E5 RUNNING, Reserved IP, 임시 SSH /32 | D21 확정 시 정리 시점을 정한다. 단, B1 NAT 관측에 OCI Relay를 쓸 계획이면 관측 완료 후 정리한다. 현재 비용은 Trial credit에서 차감되고 있다(SGD 0.09 사용, 10-02 기준) |

## 6. 미검증·한계

- 이 세션의 egress 정책상 `docs.aws.amazon.com`, `aws.amazon.com`, `libreswan.org` 접근이 차단돼 공식 문서를 재조회하지 못했다. 다음 사항은 계약 v1에 인용된 출처와 일반 지식에 기댄 것이고, 이 세션에서 원문으로 대조하지 않았다.
  - AWS EIP/ENI route target/source-dest check 동작
  - 인증서 기반 CGW의 IP 선택사항 여부
  - AWS Private CA 가격
  - Libreswan `enable-tcp`·`tcp-remoteport`·`right=%any` 동작
  - 5.4의 DPD/liveness 키 이름
- evidence #104(vpn-gw01 pre-VPN, IP 회전 원본)는 리뷰 대기이며 병합되지 않았다. B1의 근거 관측은 아직 독립 리뷰를 거치지 않았다.
- #34(P2-ARC-01)·#35(P2-IAC-01) 코멘트 전체와 PR #112 후보 문서는 이번에 정독하지 않았다. 계약 v1의 transport subnet `10.20.110.0/24`가 기존 설계값이라는 주장은 확인하지 않았다.
- 실제 AWS 계정 상태(AZ, AMI, offering, EIP quota)는 계약 v1과 마찬가지로 PENDING이다.

## 7. D21 decision-ready 체크리스트(권고)

| 순서 | 항목 | 판정 기준 | 현재 |
|---|---|---|---|
| 1 | B1 NAT 특성 관측(OCI Relay 재사용 가능) | 500/4500 source 일치 20/20 또는 완화책 확정 | 미실행 |
| 2 | 공식 문서·가격 재확인(§6 목록) | 원문 URL·확인 시각 기록 | 미실행 |
| 3 | 계약 v2 반영: B2 MSS, B3 독립 ENI, B4 masquerade/forward, §4 SG·selector 최소화 | #36 코멘트 또는 #34 설계 문서에 반영 | 미반영 |
| 4 | AWS account read-only inventory | AZ, AMI owner/ID, instance offering, EIP quota | PENDING(계약 v1과 동일) |
| 5 | Lead 명시 수용 | `0.0.0.0/0` UDP 2포트, single Relay SPOF, 인증 방식(PSK/자체 CA) | PENDING |
| 6 | 정본 CR 범위 확정 | §5 표의 항목별 처리 주체·시점 | 미착수 |
| 7 | evidence #104 독립 리뷰·병합 | exact-head APPROVED | REVIEW PENDING |

1~5가 충족되면 기술 판단으로는 EC2+EIP Relay를 D21 Primary로 올릴 근거가 갖춰진다. 6~7은 추적성 조건이다. 일정은 D21 목표 10-08, #37 10-08~10-13이므로 1·2·4는 10-06 전에 끝내야 버퍼가 남는다.

_AI 사용: Claude Code가 정본·티켓 코멘트 대조와 리뷰 문서 작성을 수행했다. 판정 권한은 담당 Lead에게 있다._
