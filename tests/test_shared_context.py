"""Negative gates and reproducibility checks; no GitHub credentials or writes."""
import copy
import datetime as dt
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import shared_context as sc
spec = importlib.util.spec_from_file_location("kit", ROOT / "scripts/build-handoff-kit.py")
kit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kit)


def fixture():
    repo = "test/baseline"
    p = "repos/" + repo
    head = "a" * 40
    approved = "b" * 40
    task = {"schema_version": 1, "record_id": "TEST-01", "purpose": "verify isolation",
            "target": {"repository": repo, "base_ref": "main"},
            "allowed_paths": ["scripts/"], "acceptance_criteria": ["same source"],
            "checks": ["unit tests"], "watch_repositories": [],
            "watch_issues": [{"repository": repo, "number": 1}],
            "watch_prs": [{"repository": repo, "number": 2}],
            "evidence": {"repository": repo, "path": "evidence/TEST-01", "receipt_commit": ""},
            "runtime": "NOT_AUTHORIZED_BY_THIS_HANDOFF"}
    lock = {"repository": repo, "tag": "docs-v1.0.0", "tag_commit": head, "release_id": 10,
            "assets": [{"id": 7, "name": "kit.zip", "sha256": "d" * 64}],
            "protected_files": {"CURRENT.md": {"git_blob": "c" * 40, "mode": "100644"}},
            "approval_prs": [{"number": 3, "head": approved, "merge": head,
                              "review_id": 30, "reviewer": "reviewer"}]}
    release = {"id": 10, "tag_name": lock["tag"], "draft": False, "prerelease": False,
               "published_at": "2026-01-01T00:00:00Z", "body": "release"}
    data = {f"{p}/releases/10": release,
            f"{p}/releases?per_page=100&page=1": [release],
            f"{p}/git/ref/tags/docs-v1.0.0": {"object": {"type": "commit", "sha": head}},
            f"{p}/releases/10/assets?per_page=100&page=1": [
                {"id": 7, "name": "kit.zip", "digest": "sha256:" + "d" * 64, "state": "uploaded"}],
            f"{p}/branches/main": {"commit": {"sha": head}},
            f"{p}/git/trees/{head}?recursive=1": {"truncated": False, "tree": [
                {"type": "blob", "path": "CURRENT.md", "sha": "c" * 40, "mode": "100644"}]},
            f"{p}/pulls/3": {"merged": True, "head": {"sha": approved},
                              "merge_commit_sha": head, "user": {"login": "author"}},
            f"{p}/pulls/3/reviews?per_page=100&page=1": [
                {"id": 30, "state": "APPROVED", "commit_id": approved, "user": {"login": "reviewer"}}],
            f"{p}/issues/1": {"number": 1, "state": "open", "body": "AC: test", "updated_at": "fixed"},
            f"{p}/issues/1/comments?per_page=100&page=1": [],
            f"{p}/pulls/2": {"number": 2, "state": "open", "head": {"sha": approved, "ref": "work"},
                              "base": {"sha": head, "ref": "main"}},
            f"{p}/issues/2/comments?per_page=100&page=1": [],
            f"{p}/pulls/2/comments?per_page=100&page=1": [],
            f"{p}/pulls/2/reviews?per_page=100&page=1": []}
    return lock, task, data


class FakeLive(sc.ExportAPI):
    """Test double only; the production ExportAPI always remains SNAPSHOT_ONLY."""
    provenance = "GH_LIVE"


class ContextTests(unittest.TestCase):
    def setUp(self):
        self.lock, self.task, self.data = fixture()
        self.api = FakeLive({"responses": self.data})

    def test_identical_source_matches(self):
        saved = sc.receipt(self.api, self.lock, self.task)
        self.assertEqual(sc.check_receipt(saved, self.api, self.lock), saved["context"])

    def test_offline_never_satisfies_live_gate(self):
        offline = sc.ExportAPI({"responses": self.data})
        saved = sc.receipt(offline, self.lock, self.task)
        self.assertEqual(saved["provenance"], "SNAPSHOT_ONLY")
        with self.assertRaisesRegex(sc.Blocked, "SNAPSHOT_ONLY"):
            sc.check_receipt(saved, self.api, self.lock)

    def test_changed_issue_comment_pr_or_review_stops_handoff(self):
        mutations = [
            lambda d: d["repos/test/baseline/issues/1"].update(body="different AC"),
            lambda d: d["repos/test/baseline/issues/1/comments?per_page=100&page=1"].append({"id": 90, "body": "new gate"}),
            lambda d: d["repos/test/baseline/pulls/2"]["head"].update(sha="e" * 40),
            lambda d: d["repos/test/baseline/pulls/2/reviews?per_page=100&page=1"].append({"id": 91, "state": "CHANGES_REQUESTED"}),
        ]
        for mutate in mutations:
            with self.subTest(mutation=mutations.index(mutate)):
                data = copy.deepcopy(self.data)
                api = FakeLive({"responses": data})
                saved = sc.receipt(api, self.lock, self.task)
                mutate(data)
                with self.assertRaisesRegex(sc.Blocked, "context drift"):
                    sc.check_receipt(saved, api, self.lock)

    def test_new_release_or_moved_tag_or_replaced_asset_stops(self):
        mutations = [
            lambda d: d["repos/test/baseline/releases?per_page=100&page=1"].append(
                {"tag_name": "docs-v1.1.0", "draft": False, "prerelease": False, "published_at": "later"}),
            lambda d: d["repos/test/baseline/git/ref/tags/docs-v1.0.0"]["object"].update(sha="e" * 40),
            lambda d: d["repos/test/baseline/releases/10/assets?per_page=100&page=1"][0].update(id=8),
            lambda d: d["repos/test/baseline/git/trees/" + "a" * 40 + "?recursive=1"]["tree"][0].update(sha="e" * 40),
            lambda d: d["repos/test/baseline/pulls/3/reviews?per_page=100&page=1"][0].update(state="DISMISSED"),
        ]
        for mutate in mutations:
            data = copy.deepcopy(self.data)
            mutate(data)
            with self.subTest(mutation=mutations.index(mutate)), self.assertRaises(sc.Blocked):
                sc.collect(FakeLive({"responses": data}), self.lock, self.task)

    def test_base_change_stops_even_when_spec_same(self):
        saved = sc.receipt(self.api, self.lock, self.task)
        self.data["repos/test/baseline/branches/main"]["commit"]["sha"] = "f" * 40
        self.data["repos/test/baseline/git/trees/" + "f" * 40 + "?recursive=1"] = self.data[
            "repos/test/baseline/git/trees/" + "a" * 40 + "?recursive=1"]
        with self.assertRaisesRegex(sc.Blocked, "context drift"):
            sc.check_receipt(saved, self.api, self.lock)

    def test_second_read_detects_race(self):
        original = self.api.get
        count = 0
        def changed(endpoint):
            nonlocal count
            if endpoint == "repos/test/baseline/issues/1":
                count += 1
                if count == 2:
                    self.data[endpoint]["body"] = "changed during collection"
            return original(endpoint)
        self.api.get = changed
        with self.assertRaisesRegex(sc.Blocked, "during observation"):
            sc.receipt(self.api, self.lock, self.task)

    def test_pagination_fetches_second_page(self):
        api = sc.ExportAPI({"responses": {"items?per_page=100&page=1": list(range(100)),
                                           "items?per_page=100&page=2": [100]}})
        self.assertEqual(sc.pages(api, "items"), list(range(101)))
        del api.responses["items?per_page=100&page=2"]
        with self.assertRaises(sc.Blocked):
            sc.pages(api, "items")

    def test_incomplete_or_truncated_inputs_fail(self):
        del self.data["repos/test/baseline/issues/1/comments?per_page=100&page=1"]
        with self.assertRaises(sc.Blocked):
            sc.collect(self.api, self.lock, self.task)
        self.setUp()
        self.data["repos/test/baseline/git/trees/" + "a" * 40 + "?recursive=1"]["truncated"] = True
        with self.assertRaises(sc.Blocked):
            sc.collect(self.api, self.lock, self.task)

    def test_auth_failure_does_not_fall_back_or_print_response(self):
        result = subprocess.CompletedProcess([], 1, "sensitive-response", "sensitive-error")
        with patch.object(sc.subprocess, "run", return_value=result):
            with self.assertRaisesRegex(sc.Blocked, "no cached fallback") as error:
                sc.GitHubAPI().get("repos/test/baseline")
            self.assertNotIn("sensitive", str(error.exception))

    def test_stale_or_tampered_receipt_fails(self):
        saved = sc.receipt(self.api, self.lock, self.task)
        saved["observed_at"] = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=9)).isoformat()
        with self.assertRaisesRegex(sc.Blocked, "expired"):
            sc.check_receipt(saved, self.api, self.lock)
        saved = sc.receipt(self.api, self.lock, self.task)
        saved["task"]["purpose"] = "different task"
        with self.assertRaisesRegex(sc.Blocked, "task changed"):
            sc.check_receipt(saved, self.api, self.lock)

    def test_empty_template_or_scope_escape_fails(self):
        with self.assertRaises(sc.Blocked):
            sc.validate_task(json.loads((ROOT / "handoff/task.template.json").read_text()))
        for path in ("../secret", "/absolute", ".git/config", "scripts/../outside", "scripts\\outside"):
            with self.subTest(path=path), self.assertRaises(sc.Blocked):
                sc.safe_path(path)

    def test_worktree_wrong_repo_and_out_of_scope_edits_fail(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            def git(*args):
                return subprocess.check_output(["git", "-C", temp, *args], stderr=subprocess.DEVNULL).decode().strip()
            git("init", "-q")
            git("config", "user.name", "test")
            git("config", "user.email", "test@invalid.local")
            (root / "original.txt").write_text("original")
            git("add", ".")
            git("commit", "-qm", "initial")
            git("remote", "add", "origin", "https://github.com/test/baseline.git")
            saved = {"task": self.task, "context": {"heads": {"test/baseline@main": git("rev-parse", "HEAD")}}}
            self.assertEqual(sc.check_worktree(root, saved)["changed_paths"], [])
            (root / "outside.txt").write_text("out of scope")
            with self.assertRaisesRegex(sc.Blocked, "outside task scope"):
                sc.check_worktree(root, saved)
            (root / "outside.txt").unlink()
            git("remote", "set-url", "origin", "https://github.com/test/different.git")
            with self.assertRaisesRegex(sc.Blocked, "repository differs"):
                sc.check_worktree(root, saved)


class KitTests(unittest.TestCase):
    def setup_root(self, root):
        (root / "handoff").mkdir()
        (root / "file.txt").write_bytes(b"same bytes\n")
        checksum = hashlib.sha256((root / "file.txt").read_bytes()).hexdigest()
        (root / kit.MANIFEST).write_text(checksum + "  file.txt\n")
        return checksum

    def test_identical_inputs_identical_zip_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.setup_root(root)
            a = kit.build(root, root / "one.zip")
            b = kit.build(root, root / "two.zip")
            self.assertEqual(a, b)
            with self.assertRaises(FileExistsError):
                kit.build(root, root / "one.zip")

    def test_modified_bytes_symlink_traversal_duplicate_fail(self):
        for variant in ("bytes", "symlink", "traversal", "duplicate"):
            with self.subTest(variant=variant), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                checksum = self.setup_root(root)
                if variant == "bytes":
                    (root / "file.txt").write_text("different")
                elif variant == "symlink":
                    (root / "file.txt").rename(root / "real.txt")
                    (root / "file.txt").symlink_to(root / "real.txt")
                elif variant == "traversal":
                    (root / kit.MANIFEST).write_text(checksum + "  ../file.txt\n")
                else:
                    (root / kit.MANIFEST).write_text((checksum + "  file.txt\n") * 2)
                with self.assertRaises(sc.Blocked):
                    kit.build(root, root / "bad.zip")


if __name__ == "__main__":
    unittest.main()
