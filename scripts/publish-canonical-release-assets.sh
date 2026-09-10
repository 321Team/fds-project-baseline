#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "사용법: $0 vX.Y.Z /path/to/FDS_vX.Y.Z_Canonical_Baseline_Release_Package.zip" >&2
  exit 2
}

version="${1:-}"
zip_path="${2:-}"
[[ "${version}" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]] || usage
[[ -f "${zip_path}" ]] || usage

repo="${GITHUB_REPOSITORY:-321Team/fds-project-baseline}"
tag="docs-${version}"
release_dir="releases/${version}"
wbs_path="wbs/FDS_${version}_WBS_and_Gantt_v1.0.xlsx"
sha_file="${release_dir}/SHA256SUMS"
sidecar="${zip_path}.sha256"

[[ -f "${wbs_path}" ]] || { echo "WBS/Gantt 원본 누락: ${wbs_path}" >&2; exit 1; }
[[ -f "${sha_file}" ]] || { echo "SHA256SUMS 누락: ${sha_file}" >&2; exit 1; }

sha256sum "${zip_path}" | sed "s#  .*#  $(basename "${zip_path}")#" > "${sidecar}"
FDS_RELEASE_ZIP="${zip_path}" bash scripts/verify-wbs-gantt-distribution.sh "${version}" --candidate

command -v gh >/dev/null 2>&1 || { echo "GitHub CLI가 필요함" >&2; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "GitHub CLI 인증이 필요함" >&2; exit 1; }
gh release view "${tag}" --repo "${repo}" >/dev/null

# --clobber로 동일 이름의 잘못된 Draft Asset만 교체한다. 발행된 과거 Release에는 사용하지 않는다.
gh release upload "${tag}" \
  "${zip_path}" \
  "${sidecar}" \
  "${sha_file}" \
  "${wbs_path}" \
  --repo "${repo}" \
  --clobber

bash scripts/verify-wbs-gantt-distribution.sh "${version}" --published
echo "정본 Release Asset 업로드·검증: PASS (${version})"