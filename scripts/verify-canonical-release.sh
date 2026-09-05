#!/usr/bin/env bash
set -euo pipefail
release_dir="releases/v3.1.17"; sha_file="${release_dir}/SHA256SUMS"
test -f "${sha_file}"; sha256sum -c "${sha_file}"
if find baseline wbs tickets web audit releases -type f \( -iname '*.pem' -o -iname '*.key' -o -iname '*.p12' -o -iname '*.pfx' -o -iname '*.kubeconfig' \) -print -quit | grep -q .; then echo "Forbidden credential-like file extension found" >&2; exit 1; fi
if rg -n --hidden --glob '!*.xlsx' --glob '!*.zip' --glob '!SHA256SUMS' '(-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|Authorization:[[:space:]]*Bearer[[:space:]]+[A-Za-z0-9._-]{12,}|password[[:space:]]*[:=][[:space:]]*[^[:space:]#]{8,})' baseline tickets web audit releases governance scripts .github; then echo "Credential-like content found" >&2; exit 1; fi
echo "canonical-integrity: PASS"
