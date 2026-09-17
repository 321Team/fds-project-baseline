"""Exercise the real shell entrypoint, including its scan-root wiring."""
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]


class CanonicalSecretGateTests(unittest.TestCase):
    def run_gate(self, filename=None, content=b''):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name in ['baseline', 'wbs', 'tickets', 'web', 'audit',
                         'releases/v0.0.1', 'governance', 'scripts', '.github']:
                (root / name).mkdir(parents=True)
            for name in ['verify-canonical-release.sh', 'verify-document-secrets.py']:
                shutil.copyfile(REPO / 'scripts' / name, root / 'scripts' / name)
            data = b'fixture document\n'
            (root / 'baseline/document.md').write_bytes(data)
            (root / 'releases/v0.0.1/SHA256SUMS').write_text(
                hashlib.sha256(data).hexdigest() + '  baseline/document.md\n')
            if filename:
                (root / 'wbs' / filename).write_bytes(content)
            return subprocess.run(
                ['bash', 'scripts/verify-canonical-release.sh'], cwd=root,
                env={**os.environ, 'RELEASE_VERSION': 'v0.0.1'},
                capture_output=True, text=True, timeout=10)

    def test_clean_entrypoint_passes(self):
        result = self.run_gate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('canonical-integrity: PASS', result.stdout)

    def test_wbs_credential_extensions_stop_entrypoint(self):
        for suffix in ['pem', 'key', 'p12', 'pfx', 'kubeconfig']:
            with self.subTest(suffix=suffix):
                result = self.run_gate('fixture.' + suffix)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('credential-like extension', result.stderr)
                self.assertNotIn('canonical-integrity: PASS', result.stdout)

    def test_wbs_text_secret_stops_entrypoint(self):
        result = self.run_gate('fixture.txt', ('gh' + 'p_' + 'A' * 30).encode())
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('pattern at line', result.stderr)
        self.assertNotIn('canonical-integrity: PASS', result.stdout)


if __name__ == '__main__':
    unittest.main()
