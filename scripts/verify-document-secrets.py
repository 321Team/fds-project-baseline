#!/usr/bin/env python3
"""Fail closed on missing/unreadable inputs; report locations without secret values."""
import pathlib,re,sys,json
PATTERNS=[r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',r'gh[pousr]_[A-Za-z0-9_]{20,}',r'AKIA[0-9A-Z]{16}',r'Authorization:\s*Bearer\s+[A-Za-z0-9._-]{12,}',r'password\s*[:=]\s*[^\s#]{8,}']
FORBIDDEN={'.pem','.key','.p12','.pfx','.kubeconfig'}
def scan(roots):
 errors=[];count=0;placeholders=0
 for root in roots:
  if not root.exists():errors.append((str(root),'missing input'));continue
  for path in sorted(root.rglob('*')):
   if path.is_symlink():errors.append((str(path),'symlink input'));continue
   if not path.is_file():continue
   if path.suffix.lower() in FORBIDDEN:errors.append((str(path),'credential-like extension'));continue
   if path.suffix.lower() in {'.xlsx','.docx','.zip','.png','.jpg','.pdf','.pyc'}:continue
   try:text=path.read_text(encoding='utf-8')
   except (OSError,UnicodeError):errors.append((str(path),'unreadable text'));continue
   count+=1
   # Exact human-readable placeholder in the preserved Issue #19 example.
   example="--docker-"+"pass"+"word='<Harbor에서 발급받은 토큰>'"
   placeholders+=text.count(example)
   text=text.replace(example,'PLACEHOLDER_REMOVED')
   for pattern in PATTERNS:
    for m in re.finditer(pattern,text):errors.append((str(path),'pattern at line '+str(text[:m.start()].count('\n')+1)))
 return count,placeholders,errors
if __name__=='__main__':
 if len(sys.argv)<2:raise SystemExit('usage: verify-document-secrets.py DIR...')
 count,placeholders,errors=scan([pathlib.Path(x) for x in sys.argv[1:]])
 for path,reason in errors:print(path+': '+reason,file=sys.stderr)
 print(f'document-secret-scan: files={count}, literal_placeholders={placeholders}, findings={len(errors)}')
 raise SystemExit(1 if errors else 0)
