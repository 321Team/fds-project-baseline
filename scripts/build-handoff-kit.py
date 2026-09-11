#!/usr/bin/env python3
"""Build only the reviewed handoff allowlist; never include workspaces or credentials."""
import argparse
import hashlib
from pathlib import Path
import stat
import zipfile
from shared_context import Blocked, require, safe_path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = "handoff/KIT_SHA256SUMS"


def build(root, output):
    root = root.resolve()
    require(not (root / MANIFEST).is_symlink(), "manifest must not be a symlink")
    manifest = (root / MANIFEST).read_bytes()
    files = {}
    for line in manifest.decode().splitlines():
        expected, path = line.split("  ", 1)
        safe_path(path)
        require(path not in files and path != MANIFEST, "duplicate/recursive kit member")
        source = root / path
        require(all(not x.is_symlink() for x in [source, *source.parents] if x != root.parent),
                "symlinks are not kit inputs")
        require(source.is_file() and source.resolve().is_relative_to(root), "kit input outside root")
        require(source.resolve() != output.resolve(), "output would overwrite kit input")
        data = source.read_bytes()
        require(hashlib.sha256(data).hexdigest() == expected, "kit checksum mismatch: " + path)
        files[path] = data
    require(files, "empty kit manifest")
    require(output.resolve() != (root / MANIFEST).resolve(), "output would overwrite manifest")
    files[MANIFEST] = manifest
    with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_STORED) as archive:
        for path, data in sorted(files.items()):
            info = zipfile.ZipInfo(path, (2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(info, data)
    checksum = hashlib.sha256(output.read_bytes()).hexdigest()
    sidecar = output.with_name(output.name + ".sha256")
    with sidecar.open("x") as handle:
        handle.write(checksum + "  " + output.name + "\n")
    return checksum


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    try:
        print(build(ROOT, args.out))
    except (Blocked, ValueError, OSError) as exc:
        parser.exit(2, "BLOCKED: " + str(exc) + "\n")
