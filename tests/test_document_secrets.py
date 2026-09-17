import importlib.util,pathlib,tempfile,unittest
P=pathlib.Path(__file__).resolve().parents[1]/'scripts/verify-document-secrets.py'
s=importlib.util.spec_from_file_location('scanner',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class ScanTests(unittest.TestCase):
 def test_missing_input_fails(self):
  with tempfile.TemporaryDirectory() as d:self.assertTrue(m.scan([pathlib.Path(d)/'missing'])[2])
 def test_synthetic_token_fails(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d);(p/'x.txt').write_text('gh'+'p_'+'A'*30);self.assertTrue(m.scan([p])[2])
 def test_placeholder_only_is_not_secret(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d);(p/'x.txt').write_text('--docker-'+'password='+"'<Harbor에서 발급받은 토큰>'");self.assertEqual(m.scan([p])[1:],(1,[]))
 def test_placeholder_does_not_hide_other_secret(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d);(p/'x.txt').write_text('--docker-'+'password='+"'<Harbor에서 발급받은 토큰>'"+'\n'+ 'gh'+'p_'+'A'*30);self.assertTrue(m.scan([p])[2])
 def test_credential_extension_fails(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d);(p/'empty.key').write_text('');self.assertTrue(m.scan([p])[2])
 def test_invalid_utf8_fails(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d);(p/'x.txt').write_bytes(bytes([255]));self.assertTrue(m.scan([p])[2])
if __name__=='__main__':unittest.main()
