# Start here — your Day 1 setup

[Open the animated classroom](https://svrforge.github.io/devops-first-pipeline/) · [All 30 text lessons](docs/en/README.md)

## Learn in your browser

Open the classroom and choose Day 1. Click **Play walkthrough**, or use the four step buttons at your own pace. Read the explanation and familiar example. The animation illustrates a concept; it does not execute shell commands.

Move to **Try it yourself** for the real commands, success evidence and recovery drill. Use **Checkpoint** to test understanding. Confirm practical evidence and pass the checkpoint before recording completion. Progress and notes are saved in this browser; Export progress downloads a backup, not an account sync. There is no import feature in this edition.

## Prepare for hands-on work

Install [Git](https://git-scm.com/downloads/) and [Python 3.11+](https://www.python.org/downloads/). Start with only these tools. Docker, Jenkins, kind and Terraform come later.

```bash
git clone https://github.com/svrforge/devops-first-pipeline.git
cd devops-first-pipeline
python learn.py doctor
python -m unittest discover -s tests -v
```

Expected: tests end with OK. Windows may use `py`; macOS/Linux may use `python3`. Bash commands need Linux, macOS, Git Bash or WSL. Run commands from the repository root and use only your own local learning systems.

## Open the classroom offline

Double-click `academy/index.html`, or serve the classroom locally:

```bash
python -m http.server 8080 --bind 127.0.0.1 --directory academy
```

Open http://localhost:8080. This is the course viewer, separate from `python app.py`, the sample HTTP service. All classroom assets are local; no package installation is needed. Browser file-mode storage behavior varies, so use the local server for consistent saved progress.

## Prefer a terminal?

```bash
python learn.py lesson 01
python learn.py quiz 01
python learn.py complete 01
python learn.py next
```

The CLI uses `.day-progress.json`; the browser uses its own local storage. They do not synchronize. The older module progress file is retained but is not reused because days have different meanings.

## If you are stuck

Read the exact error and expected evidence. Missing optional tools do not block early days. A busy port means another listener may exist: stop only the process you started. Include your OS, day, command and sanitized error in a learning-help issue. Never post credentials or private logs.
