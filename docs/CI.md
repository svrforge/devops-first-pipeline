# CI you can trust

CI means **Continuous Integration**: automatically check proposed code changes. This project implements CI, not automated deployment (CD).

## What must pass

1. Compile Python source and run the five real HTTP tests on Python 3.11, 3.12 and 3.13.
2. Check Bash syntax.
3. Validate Compose configuration.
4. Build the Docker image.
5. Start that image and verify its health, root response and non-root UID.

The Docker job is independent of the three Python jobs; the run is green only if all four succeed. Jobs have time limits. The workflow has read-only repository permissions and no credentials. A pull request may trigger both a push and a PR run: this is intentional so each event is checked.

## Before each push

```bash
python -m compileall -q app.py tests
python -m unittest discover -s tests -v
bash -n scripts/*.sh
docker compose config -q
docker build -t devops-first-pipeline:local .
bash scripts/container-check.sh devops-first-pipeline:local
```

## When CI is red

Open Actions → failed run → failed job → failed step. Reproduce that exact command locally. Fix the cause and push a commit. Rerun unchanged code only for a demonstrated temporary runner, network or image-registry failure. Never add `continue-on-error`, remove checks, or change assertions merely to make the badge green.

Weekly Dependabot PRs propose action and Docker base-image updates; they do not auto-merge. Review them and confirm CI passes. This is a maintenance aid, not a promise of permanent compatibility.

## Optional merge protection

Repository owner: Settings → Rules → Rulesets (or Branches) → protect `main` and require pull requests plus the three Python checks and Docker check after their first run. Availability depends on GitHub plan/repository settings. This repo does not claim protection is enabled. Requiring checks prevents accidental merges of known failing PRs; owners can still change settings. Direct pushes are checked after they arrive.
