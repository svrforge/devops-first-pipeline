# Contributing

Fork if you do not have write access. Create a focused branch and open a pull request to main. Explain the learner problem and final behavior. Run:

```bash
python -m unittest discover -s tests -v
python scripts/validate_course.py
bash -n scripts/*.sh
docker build -t devops-first-pipeline:local .
bash scripts/container-check.sh devops-first-pipeline:local
```

Keep English the default, retain Tamil concept parity, and update lesson evidence when behavior changes. No secrets, private logs, copied proprietary material, or claims of production validation without evidence. Reviewers should verify the CI commit matches the latest PR commit. See [language scope](docs/LANGUAGES.md).
