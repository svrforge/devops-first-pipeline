#!/usr/bin/env bash
set -euo pipefail
image="${1:-devops-first-pipeline:local}"
name="devops-learner-${RANDOM}-$$"
cleanup() { docker logs "$name" || true; docker rm -f "$name" >/dev/null || true; }
trap cleanup EXIT
docker run -d --name "$name" --read-only --cap-drop ALL --security-opt no-new-privileges:true "$image"
for attempt in $(seq 1 40); do
  state=$(docker inspect --format '{{.State.Health.Status}}' "$name")
  if [ "$state" = healthy ]; then
    docker exec "$name" python -c "import os; assert os.getuid() == 10001"
    docker exec "$name" python -c "import json,urllib.request; r=urllib.request.urlopen('http://127.0.0.1:8000/'); assert json.load(r)['message']=='Hello, DevOps learner!'"
    echo 'Container health, response and non-root checks passed'
    exit 0
  fi
  if [ "$state" = unhealthy ]; then exit 1; fi
  sleep 2
done
echo 'Container did not become healthy before timeout' >&2
exit 1
