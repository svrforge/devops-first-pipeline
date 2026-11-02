# DevOps First Pipeline

[![CI](https://github.com/svrforge/devops-first-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/svrforge/devops-first-pipeline/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Your first working DevOps project — understand it, run it, break it, fix it.**

A small Python HTTP service you can take from your laptop to a tested Docker image. No Python packages, cloud account, paid tools or deployment credentials required. Built for learners by **SVR Forge · Vignesh Raja Sundararajan**.

> Tamil learners: app code theriyalanaalum start pannalaam. First local-la run pannunga; next tests, Docker, CI order-la learn pannunga. Green tick mattum goal illa — failure reason purinju fix panradhu thaan real learning.

## What you will learn

| Stage | What you do | Proof you understand it |
|---|---|---|
| Git | Clone, branch, commit, open a pull request | Your own change appears in a PR |
| Linux / HTTP | Run a process, read logs, call endpoints | Explain 200, 404 and ports |
| Tests | Check real HTTP responses with unittest | Break a response and see a test fail |
| Docker | Build an image and run a non-root container | Container becomes healthy |
| CI | Run tests on Python 3.11, 3.12 and 3.13, plus Docker checks | All four jobs pass on your commit |
| Jenkins (optional) | Run the same checks on your learning agent | Pipeline stages succeed |
| Kubernetes (optional) | Run two replicas in a local kind cluster | Rollout and health probes succeed |

## 1. Start here: run locally

Install Git and Python 3.11 or newer. Docker Desktop is only needed for stage 3. On Windows, use `py` if `python` is unavailable; use Git Bash or WSL for `.sh` scripts.

```bash
git clone https://github.com/svrforge/devops-first-pipeline.git
cd devops-first-pipeline
python -m unittest discover -s tests -v
python app.py
```

Open <http://localhost:8000/> and <http://localhost:8000/health>. Stop with **Ctrl+C**.

Expected home response (JSON key order is irrelevant):

```json
{"message": "Hello, DevOps learner!", "version": "1.0.0"}
```

In a second terminal, while the app runs:

```bash
bash scripts/smoke.sh
```

Configuration: `PORT` defaults to `8000`; `APP_VERSION` defaults to `1.0.0`. Example for Bash: `APP_VERSION=2.0.0 PORT=8001 python app.py`. In PowerShell: `$env:APP_VERSION="2.0.0"; $env:PORT="8001"; python app.py`. No secrets belong in these variables.

## 2. Make a change and see CI work

If you are a visitor, **fork this repository first** and clone your own fork to get push permission.

```bash
git switch -c learning/my-first-change
# Edit a message and its matching test together.
python -m unittest discover -s tests -v
git add app.py tests/test_app.py
git commit -m "Update greeting and its HTTP test"
git push -u origin learning/my-first-change
```

Open a pull request and inspect its **Checks** tab. `CI` runs on every push and pull request, and can also be started manually from **Actions → CI → Run workflow**. It does not deploy, publish images or need secrets.

**A green build is earned.** Failed tests and container checks fail the workflow; nothing masks failures. External runner outages or broken future changes can still turn it red. See [the CI guide](docs/CI.md) for maintenance and recovery.

## 3. Build and verify Docker

Start Docker Desktop (Linux containers), or a Docker Engine daemon on Linux.

```bash
docker build -t devops-first-pipeline:local .
bash scripts/container-check.sh devops-first-pipeline:local
docker compose up --build -d
docker compose ps
docker compose logs app
```

Open <http://localhost:8000/health>. Compose binds to loopback so this exercise is not exposed on your LAN. Stop the app when finished:

```bash
docker compose down
```

The verification script starts an isolated container, waits for health, checks the response and UID, then removes its own container. Docker runs the app as UID `10001`, with a read-only filesystem and dropped capabilities.

`PORT` is configurable for the local Python process. The Docker health check and provided manifests intentionally use port `8000`; keep that port inside the container and change the host mapping if needed.

## 4. Optional extensions

- [Jenkins walkthrough](docs/JENKINS.md): use the included `Jenkinsfile`.
- [Kubernetes walkthrough](docs/KUBERNETES.md): local kind cluster, no cloud charges.
- [Seven practical exercises](docs/EXERCISES.md): learn by changing and troubleshooting.
- [Troubleshooting and glossary](docs/TROUBLESHOOTING.md).

## Repository map

```text
app.py                       HTTP service
 tests/test_app.py           Real HTTP tests (5 cases)
Dockerfile                   Non-root learning image
compose.yaml                 Local container run
scripts/smoke.sh             HTTP endpoint verification
scripts/container-check.sh   Container health + UID verification
.github/workflows/ci.yml     Automated tests and container build
.github/dependabot.yml       Weekly action/base-image update PRs
Jenkinsfile                  Optional Jenkins pipeline
k8s/app.yaml                 Local Kubernetes deployment + service
docs/                        Guided labs and explanations
```

## Scope and security

This uses Python's `http.server` **for education only**. It is not a production API server. There is no authentication, TLS, database, public deployment, vulnerability scan or automatic release in this project. Do not put real user data or secrets into it. Docker tags and action major versions receive upstream updates; review Dependabot PRs and their CI before merging. For production, use an appropriate web server, immutable image digests, full action SHA pins, monitoring and deployment controls.

## Contributing

Keep changes beginner-friendly, add tests for changed behavior, and run the checks documented above. Explain **why** a change is useful. Do not submit credentials or unrelated generated files. MIT licensed; you may learn from and adapt this project with the included license notice.

## Official references

- [GitHub Actions: Python builds](https://docs.github.com/en/actions/tutorials/build-and-test-code/python)
- [Dockerfile instructions](https://docs.docker.com/reference/dockerfile/)
- [Jenkins Pipeline](https://www.jenkins.io/doc/book/pipeline/)
- [kind quick start](https://kind.sigs.k8s.io/docs/user/quick-start/)
