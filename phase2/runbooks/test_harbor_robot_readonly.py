import importlib.util, json, ssl, sys, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
from urllib import error
spec=importlib.util.spec_from_file_location("robot",str(Path(__file__).with_name("harbor-robot-readonly.py")))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def robot(i=1,name="robot$worker"):
    return dict(id=i,name=name,level="system",disable=False,expires_at=1792108800,duration=30,secret="SECRET_SENTINEL",description="SECRET_SENTINEL",permissions=[dict(kind="project",namespace="fds",access=[dict(resource="repository",action="pull",effect="allow",secret="SECRET_SENTINEL")])])
class Response:
    status=200
    def __init__(self,data): self.data=data
    def __enter__(self): return self
    def __exit__(self,*args): pass
    def read(self,n): return self.data
class Opener:
    def __init__(self,pages): self.pages=iter(pages);self.requests=[]
    def open(self,req,timeout):
        self.requests.append(req)
        return Response(next(self.pages))
def page(rows): return json.dumps(rows).encode()
class Tests(unittest.TestCase):
    def test_fqdn_endpoint(self):
        op=Opener([b"[]"])
        m.collect(op,"Basic TEST")
        self.assertEqual(op.requests[0].host,"harbor.fds.internal")
        self.assertEqual(op.requests[0].type,"https")
    def test_bad_ca_before_prompt_or_network(self):
        with tempfile.TemporaryDirectory() as root:
            ca=Path(root)/"ca.crt";ca.write_text("wrong CA")
            with patch.object(sys,"argv",["collector","--ca-file",str(ca)]),patch("builtins.input") as prompt,patch.object(m.request,"build_opener") as network:
                self.assertEqual(m.run(),2)
                prompt.assert_not_called();network.assert_not_called()
    def test_missing_ca(self):
        with tempfile.TemporaryDirectory() as root:
            with self.assertRaises(m.Stop):m.tls_context(Path(root)/"missing")
    def test_ca_path_and_strict_tls(self):
        payload=b"pinned public PEM"
        with tempfile.TemporaryDirectory() as root:
            ca=Path(root)/"custom-ca.pem";ca.write_bytes(payload)
            with patch.object(m,"CA_SHA",m.hashlib.sha256(payload).hexdigest()),patch.object(m.ssl.SSLContext,"load_verify_locations") as load:
                ctx=m.tls_context(ca)
                load.assert_called_once_with(cadata=payload.decode("ascii"))
                self.assertTrue(ctx.check_hostname)
                self.assertEqual(ctx.verify_mode,ssl.CERT_REQUIRED)
    def test_connection_failure_before_prompt(self):
        with patch.object(sys,"argv",["collector","--ca-file","/unused"]),patch.object(m,"tls_context"),patch.object(m.request,"build_opener") as build,patch("builtins.input") as prompt:
            build.return_value.open.side_effect=error.URLError("SECRET_SENTINEL")
            with patch("builtins.print") as out:
                self.assertEqual(m.run(),2)
                self.assertNotIn("SECRET_SENTINEL",str(out.call_args_list))
            prompt.assert_not_called()
    def test_pages_and_secrets(self):
        op=Opener([page([robot()]),page([robot(2,"robot$push")]),b"[]"])
        result=m.collect(op,"Basic TEST")
        self.assertEqual(set(result),set(m.TARGETS))
        self.assertNotIn("SECRET_SENTINEL",json.dumps(result))
        self.assertTrue(all(r.method=="GET" for r in op.requests))
    def test_missing(self):
        self.assertEqual(m.collect(Opener([b"[]"]),"x"),{})
    def test_duplicate(self):
        with self.assertRaises(m.Stop): m.collect(Opener([page([robot()]),page([robot()])]),"x")
    def test_bad_json(self):
        for data in [b"broken",b"{}",b"[null]"]:
            with self.assertRaises(m.Stop): m.collect(Opener([data]),"x")
    def test_missing_field(self):
        r=robot();del r["disable"]
        with self.assertRaises(m.Stop): m.select_robot(r)
    def test_boolean_as_integer(self):
        r=robot();r["expires_at"]=True
        with self.assertRaises(m.Stop):m.select_robot(r)
    def test_disabled_and_expired_preserved(self):
        r=robot();r.update(disable=True,expires_at=1)
        v=m.select_robot(r);self.assertTrue(v["disable"]);self.assertEqual(v["expires_at"],1)
    def test_never_preserved(self):
        r=robot();r.update(expires_at=-1,duration=-1)
        self.assertIsNone(m.select_robot(r)["expires_at_kst"])
    def test_redirect(self):
        with self.assertRaises(m.Stop):m.NoRedirect().redirect_request(None,None,302,"",{}, "https://elsewhere")
    def test_http_errors_safe(self):
        for status in [401,403]:
            with patch.object(m,"main",side_effect=error.HTTPError("https://example",status,"SECRET_SENTINEL",{},None)),patch("builtins.print") as out:
                self.assertEqual(m.run(),2)
                self.assertNotIn("SECRET_SENTINEL",str(out.call_args_list))
if __name__=="__main__": unittest.main()
