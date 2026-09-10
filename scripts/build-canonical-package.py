#!/usr/bin/env python3
"""Build a deterministic ZIP from a reviewed SHA256SUMS. Does not publish."""
from pathlib import Path,PurePosixPath
import hashlib,re,sys,zipfile
R=Path(__file__).resolve().parents[1]
if len(sys.argv)!=3 or not re.fullmatch(r'v\d+\.\d+\.\d+',sys.argv[1]):
 raise SystemExit('usage: build-canonical-package.py vX.Y.Z OUTPUT_DIR')
v=sys.argv[1];out=Path(sys.argv[2]).resolve();sf=f'releases/{v}/SHA256SUMS';entries={}
for line in (R/sf).read_text().splitlines():
 expected,path=line.split('  ',1);p=PurePosixPath(path)
 if p.is_absolute() or '..' in p.parts:raise SystemExit('unsafe manifest path')
 data=(R/path).read_bytes()
 if hashlib.sha256(data).hexdigest()!=expected:raise SystemExit('checksum mismatch: '+path)
 entries[path]=data
entries[sf]=(R/sf).read_bytes();out.mkdir(parents=True,exist_ok=True)
name=f'FDS_{v}_Canonical_Baseline_Release_Package.zip';target=out/name
with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_STORED) as z:
 for path,data in sorted(entries.items()):
  info=zipfile.ZipInfo(path,date_time=(2026,1,1,0,0,0));info.create_system=3
  info.external_attr=(0o100644<<16);info.compress_type=zipfile.ZIP_STORED
  z.writestr(info,data)
sha=hashlib.sha256(target.read_bytes()).hexdigest();(out/(name+'.sha256')).write_text(f'{sha}  {name}\n')
print(f'{sha}  {target}')
