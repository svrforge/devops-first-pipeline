# Start here — one small win at a time

[Course home](README.md) · [English](docs/en/README.md) · [தமிழ்](docs/ta/README.md)

## What you need today

- A computer, a terminal, Git and Python 3.11 or newer.
- Windows: PowerShell works for Python and Git; use `py` instead of `python` if needed. Git Bash or WSL is needed only for Bash exercises.
- macOS/Linux: use `python3` if your system does not provide `python`.
- Docker, Jenkins, Kubernetes and Terraform can wait until their modules.

Use official downloads: [Python](https://www.python.org/downloads/), [Git](https://git-scm.com/downloads/), [Docker](https://docs.docker.com/get-started/get-docker/). Install tools yourself; this course does not run installers.

## 1. Get the course

```bash
git clone https://github.com/svrforge/devops-first-pipeline.git
cd devops-first-pipeline
python learn.py doctor
```

Doctor checks tool availability on PATH only. Missing optional tools do not prevent the foundation lessons. No account token is required to clone the public course.

## 2. Complete your first lesson

```bash
python learn.py lesson 01
python -m unittest discover -s tests -v
python learn.py quiz 01
```

Expected: tests end in OK. Read a failed assertion before changing anything. The quiz is in English and explains its answer. Tamil concept version: `python learn.py --lang ta lesson 01`.

## 3. Record evidence, then continue

Write down the command, result and why it matters. Only after completing the practical work:

```bash
python learn.py complete 01
python learn.py next
```

Progress is stored in `.learning-progress.json`, ignored by Git. To move computers, copy that file yourself. To reset, back it up then remove only that file. Invalid JSON produces an error rather than silently losing progress.

## If you get stuck

- `python` missing: try `py` on Windows or `python3` on macOS/Linux.
- Import error: run from the cloned repository root.
- Port busy: stop the earlier local app using Ctrl+C; do not kill unknown processes.
- Docker unavailable: continue modules 1–5 first.
- Need help: include OS, module, command and sanitized error in a learning-help issue.

You are ready when you can explain what a test checked. Speed is not the goal. Continue with [module 02](docs/en/02.md).
