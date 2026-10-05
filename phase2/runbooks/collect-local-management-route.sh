#!/usr/bin/env bash
# One-shot LOCAL metadata only. No packets, sudo, SSH, config writes or credentials.
(
set -u
set -o pipefail
umask 077
role="${1:-}"
case "$role" in
  runner) expected=10.250.10.20; targets=(10.1.93.51 10.1.93.52 10.1.93.53 10.20.110.10) ;;
  vpn-gw) expected=10.1.93.51; targets=(10.250.10.20 10.1.93.52 10.1.93.53 10.20.110.10) ;;
  *) printf 'Usage: bash %s runner|vpn-gw\n' "$0" >&2; exit 2 ;;
esac
for dependency in ip python3 timeout mktemp sha256sum; do
  command -v "$dependency" >/dev/null 2>&1 || { printf 'STOP missing tool: %s\n' "$dependency" >&2; exit 2; }
done
addresses="$(timeout 10 ip -j -4 address show)" || { printf 'STOP address query failed\n' >&2; exit 2; }
if ! printf '%s' "$addresses" | python3 -c 'import json,sys; rows=json.load(sys.stdin); sys.exit(0 if any(a.get("local")==sys.argv[1] for row in rows for a in row.get("addr_info",[])) else 2)' "$expected"; then
  printf 'STOP expected local address absent or invalid address JSON: %s\n' "$expected" >&2
  exit 2
fi
out="$(mktemp -d "$HOME/p2-local-route.XXXXXX")" || exit 2
log="$out/local-route.txt"
failed=0
io_fail() {
  printf 'RESULT_DIR=%s\nSTATE=INCOMPLETE_LOG_WRITE\n' "$out" >&2
  exit 2
}
run() {
  {
    printf '\nCOMMAND' &&
    printf ' %q' "$@" &&
    printf '\n'
  } >>"$log" || io_fail
  timeout 10 "$@" >>"$log" 2>&1
  rc=$?
  printf 'RC=%s\n' "$rc" >>"$log" || io_fail
  if [ "$rc" -ne 0 ]; then failed=1; fi
}
{
  printf 'SCOPE=LOCAL_METADATA_ONLY\nROLE=%s\nEXPECTED_ADDRESS=%s\n' "$role" "$expected" &&
  printf 'SOURCE_FILE_SHA256=' &&
  sha256sum -- "$0" | cut -d ' ' -f 1
} >"$log" || exit 2
run date -u +%Y-%m-%dT%H:%M:%SZ
run env TZ=Asia/Seoul date +%Y-%m-%dT%H:%M:%S%:z
run hostname
run id -un
run ip -j -4 address show
run ip -4 rule show
run ip -4 route show table all
run cat /etc/resolv.conf
run cat /proc/sys/net/ipv4/ip_forward
for target in "${targets[@]}"; do run ip -4 route get "$target"; done
run ip -4 route get "${targets[0]}" from "$expected"
if [ "$failed" -eq 0 ]; then state=CAPTURED_REVIEW_REQUIRED; else state=PARTIAL_REVIEW_REQUIRED; fi
printf '\nSTATE=%s\nNOT_PROVEN=connectivity,forwarding,TLS,DNS_answer,VPN_or_ROSA_readiness\n' "$state" >>"$log" || io_fail
(cd "$out" && sha256sum local-route.txt >SHA256SUMS) || exit 2
printf 'RESULT_DIR=%s\nSTATE=%s\n' "$out" "$state"
printf 'SOURCE-SENSITIVE: private review only; do not post to public repository.\n'
[ "$failed" -eq 0 ]
)
