import json
import os
import threading
import unittest
from http.server import ThreadingHTTPServer
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import urlopen

from app import Handler


class ServiceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=5)

    def get(self, path):
        return urlopen(self.base + path, timeout=3)

    def test_home(self):
        with self.get("/") as response:
            self.assertEqual(response.status, 200)
            self.assertEqual(response.headers["Content-Type"], "application/json")
            payload = response.read()
            self.assertEqual(int(response.headers["Content-Length"]), len(payload))
            self.assertEqual(json.loads(payload)["message"], "Hello, DevOps learner!")

    def test_health_with_query(self):
        with self.get("/health?probe=ci") as response:
            self.assertEqual(json.load(response), {"status": "ok"})

    def test_version_from_environment(self):
        with patch.dict(os.environ, {"APP_VERSION": "test-release"}):
            with self.get("/") as response:
                self.assertEqual(json.load(response)["version"], "test-release")

    def test_unknown_path(self):
        with self.assertRaises(HTTPError) as caught:
            self.get("/missing")
        self.assertEqual(caught.exception.code, 404)
        self.assertEqual(json.load(caught.exception), {"error": "not found"})

    def test_post_is_not_supported(self):
        from urllib.request import Request
        with self.assertRaises(HTTPError) as caught:
            urlopen(Request(self.base + "/", data=b"hello"), timeout=3)
        self.assertEqual(caught.exception.code, 501)


if __name__ == "__main__":
    unittest.main()
