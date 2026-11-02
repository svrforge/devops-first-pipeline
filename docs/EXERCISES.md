# Learn by doing: seven labs

Do each lab on a branch. Record the command, expected result, actual result and what you learned in your own notes.

| Lab | Task | Acceptance check |
|---|---|---|
| 1 — HTTP | Run the service and call `/`, `/health`, `/missing` | Explain why the last request returns 404 |
| 2 — Red / green | Change the greeting without changing its test | Observe test failure, then update behavior and test intentionally; do not merge the failing branch |
| 3 — Configuration | Set `APP_VERSION=2.0.0` when starting the app | `/` shows the new version; no code edit required |
| 4 — Containers | Run the Docker verification script | Explain image vs container, health vs running, and why UID is not 0 |
| 5 — Pull requests | Push a branch, open a PR, inspect all four CI jobs | Identify the exact commit tested and the commands executed |
| 6 — Jenkins | Run the optional pipeline on a dedicated agent | Explain checkout, test, build and verify stages |
| 7 — Kubernetes | Complete the kind walkthrough | Two pods ready, service reachable through port forwarding |

## A real next feature

Add `/ready` returning `{"ready": true}`. Write a real HTTP test, preserve the unknown-route test, run tests locally, and open a PR. Explain why this is different from changing `/health` without updating container probes.

## Interview practice

- Why can a container be running but unhealthy?
- What does `EXPOSE` do, and why do we still need a port mapping?
- What should happen when a test fails in a PR?
- Why does this project use no cloud credentials in CI?
- Why does a green run prove only the checks that actually ran?
- Which changes would you need before exposing this service to real users?

