#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "사용법: $0 vX.Y.Z [--candidate|--published]" >&2
  exit 2
}

version="${1:-}"
mode="${2:---candidate}"
[[ "${version}" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]] || usage
[[ "${mode}" == "--candidate" || "${mode}" == "--published" ]] || usage

release_dir="releases/${version}"
sha_file="${release_dir}/SHA256SUMS"
manifest="${release_dir}/FDS_Document_Distribution_Manifest_${version}.md"
wbs_path="wbs/FDS_${version}_WBS_and_Gantt_v1.0.xlsx"
zip_name="FDS_${version}_Canonical_Baseline_Release_Package.zip"

fail() {
  echo "WBS/Gantt 배포 검증: FAIL — $*" >&2
  exit 1
}

[[ -f "${wbs_path}" ]] || fail "저장소 원본 누락: ${wbs_path}"
[[ -f "${sha_file}" ]] || fail "SHA256SUMS 누락: ${sha_file}"
[[ -f "${manifest}" ]] || fail "Manifest 누락: ${manifest}"

wbs_sha="$(sha256sum "${wbs_path}" | awk '{print $1}')"
sha_record="$(awk -v p="${wbs_path}" '$2 == p {print $1}' "${sha_file}")"
[[ -n "${sha_record}" ]] || fail "SHA256SUMS에 WBS/Gantt 경로가 없음"
[[ "${sha_record}" == "${wbs_sha}" ]] || fail "저장소 원본과 SHA256SUMS 불일치"

grep -Fq "${wbs_path}" "${manifest}" || fail "Manifest에 WBS/Gantt 경로가 없음"
grep -Fiq "${wbs_sha}" "${manifest}" || fail "Manifest에 WBS/Gantt SHA-256이 없음"

verify_zip() {
  local path="$1"
  unzip -Z1 "${path}" | grep -Fxq "${wbs_path}" || fail "ZIP 내부 WBS/Gantt 누락"
  local zip_wbs_sha
  zip_wbs_sha="$(unzip -p "${path}" "${wbs_path}" | sha256sum | awk '{print $1}')"
  [[ "${zip_wbs_sha}" == "${wbs_sha}" ]] || fail "ZIP 내부 WBS/Gantt SHA-256 불일치"
}

zip_path="${FDS_RELEASE_ZIP:-}"
for candidate in "${release_dir}/${zip_name}" "${zip_name}"; do
  [[ -n "${zip_path}" ]] && break
  if [[ -f "${candidate}" ]]; then
    zip_path="${candidate}"
    break
  fi
done
if [[ -n "${zip_path}" ]]; then
  [[ -f "${zip_path}" ]] || fail "지정된 정본 배포 ZIP을 찾을 수 없음: ${zip_path}"
  verify_zip "${zip_path}"
elif [[ "${mode}" == "--candidate" ]]; then
  echo "WBS/Gantt ZIP 검증: NOT RUN — 배포 ZIP 생성 전 후보 단계"
fi

if [[ "${mode}" == "--published" ]]; then
  command -v gh >/dev/null 2>&1 || fail "published 검증에는 GitHub CLI가 필요함"
  gh auth status >/dev/null 2>&1 || fail "GitHub CLI 인증이 필요함"
  repo="${GITHUB_REPOSITORY:-321Team/fds-project-baseline}"
  tag="docs-${version}"
  asset_names="$(gh release view "${tag}" --repo "${repo}" --json assets --jq '.assets[].name')"
  grep -Fxq "$(basename "${wbs_path}")" <<<"${asset_names}" || fail "독립 WBS/Gantt Release Asset 누락"
  grep -Fxq "${zip_name}" <<<"${asset_names}" || fail "정본 배포 ZIP Release Asset 누락"

  tmp_dir="$(mktemp -d)"
  trap 'rm -rf "${tmp_dir}"' EXIT
  gh release download "${tag}" --repo "${repo}" --pattern "$(basename "${wbs_path}")" --dir "${tmp_dir}" --clobber
  gh release download "${tag}" --repo "${repo}" --pattern "${zip_name}" --dir "${tmp_dir}" --clobber
  asset_sha="$(sha256sum "${tmp_dir}/$(basename "${wbs_path}")" | awk '{print $1}')"
  [[ "${asset_sha}" == "${wbs_sha}" ]] || fail "독립 WBS/Gantt Release Asset SHA-256 불일치"
  verify_zip "${tmp_dir}/${zip_name}"
fi

echo "WBS/Gantt 배포 검증: PASS (${version}, ${mode#--})"