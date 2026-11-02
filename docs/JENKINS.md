# Optional Jenkins lab

Use a dedicated **Linux learning agent** with Git, Python 3.11+, Bash and a working Docker CLI/daemon. A plain Jenkins controller container does not automatically have Docker or Python installed. Do not run builds on a production controller. Docker daemon access is effectively privileged; never grant it to untrusted contributors or a shared agent casually.

1. In Jenkins, create a **Pipeline** job.
2. Choose **Pipeline script from SCM → Git**.
3. Repository URL: `https://github.com/svrforge/devops-first-pipeline.git`.
4. Branch: `*/main`; Script Path: `Jenkinsfile`.
5. Save → Build Now.
6. Read Checkout → Test → Build → Verify in the stage view.

No GitHub token is needed to clone this public repo. This manual lab does not configure webhooks, credentials or public Jenkins access.

The pipeline tags images using the build number and removes its image afterward. Its container check removes only the container it starts. Cleanup may use `|| true`; tests and verification never ignore errors. If an agent lacks a dependency, install it on your dedicated agent and rerun. Do not disable tests to work around a missing tool.
