#!/usr/bin/env bash
set -euo pipefail

if [[ -n "${RELEASE_VERSION:-}" ]]; then
  release_version="${RELEASE_VERSION}"
else
  release_version="$(find wbs -maxdepth 1 -type f -name 'FDS_v*_WBS_and_Gantt_v1.0.xlsx' -printf '%f\n' \
    | sed -E 's/^FDS_(v[0-9]+\.[0-9]+\.[0-9]+)_WBS_and_Gantt_v1\.0\.xlsx$/\1/' \
    | sort -V | tail -n1)"
fi
[[ -n "${release_version}" ]] || { echo "릴리즈 버전을 결정할 수 없음" >&2; exit 1; }
release_dir="releases/${release_version}"
sha_file="${release_dir}/SHA256SUMS"

test -f "${sha_file}"
sha256sum -c "${sha_file}"

if find baseline wbs tickets web audit releases -type f \( -iname '*.pem' -o -iname '*.key' -o -iname '*.p12' -o -iname '*.pfx' -o -iname '*.kubeconfig' \) -print -quit | grep -q .; then
  echo "Forbidden credential-like file extension found" >&2
  exit 1
fi

if rg -n --hidden --glob '!*.xlsx' --glob '!*.zip' --glob '!SHA256SUMS' '(-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|Authorization:[[:space:]]*Bearer[[:space:]]+[A-Za-z0-9._-]{12,}|password[[:space:]]*[:=][[:space:]]*[^[:space:]#]{8,})' baseline tickets web audit releases governance scripts .github; then
  echo "Credential-like content found" >&2
  exit 1
fi

# v3.1.18부터 변경 유무와 관계없이 WBS/Gantt를 저장소·Manifest·SHA256SUMS·ZIP에서 검증한다.
# GitHub Release 발행 후에는 같은 스크립트를 --published로 실행해 독립 Asset까지 검증한다.
version_number="${release_version#v}"
if [[ "$(printf '%s\n' '3.1.18' "${version_number}" | sort -V | head -n1)" == "3.1.18" ]]; then
  bash scripts/verify-wbs-gantt-distribution.sh "${release_version}" --candidate
fi

echo "canonical-integrity: PASS"