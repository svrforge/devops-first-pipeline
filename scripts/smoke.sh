#!/usr/bin/env bash
set -euo pipefail
base="${1:-http://127.0.0.1:8000}"
python - "$base" <<'PYTHON'
import json
import sys
from urllib.request import urlopen
from urllib.error import HTTPError
base = sys.argv[1].rstrip("/")
with urlopen(base + "/health", timeout=3) as response:
    assert response.status == 200
    assert json.load(response) == {"status": "ok"}
with urlopen(base + "/", timeout=3) as response:
    assert json.load(response)["message"] == "Hello, DevOps learner!"
try:
    urlopen(base + "/missing", timeout=3)
except HTTPError as exc:
    assert exc.code == 404
else:
    raise AssertionError("Missing route must return 404")
print("Smoke checks passed")
PYTHON
