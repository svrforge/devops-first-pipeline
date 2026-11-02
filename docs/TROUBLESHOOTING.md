# Troubleshooting

| Symptom | Likely cause | Fix / verification |
|---|---|---|
| `python` not found | Python missing or PATH issue | Install Python 3.11+; Windows users may use `py` |
| Address already in use | Another process owns port 8000 | Stop your other lab process or use `PORT=8001` for the local service |
| Docker cannot connect | Daemon is stopped / access missing | Start Docker Desktop; check `docker info` |
| Container exits immediately | Startup/configuration error | Read `docker logs <name>` before changing anything |
| Compose browser URL fails | App not healthy or wrong mapping | `docker compose ps`, then `docker compose logs app` |
| Permission denied for `.sh` | Script not executable | Use `bash scripts/smoke.sh` as documented |
| Shell reports CRLF issues | Windows line endings in shell files | Save `.sh` files with LF line endings; use Git Bash/WSL |
| Jenkins `docker` not found | Agent lacks Docker CLI | Use the dedicated agent described in the Jenkins guide |
| `ErrImageNeverPull` in kind | Image not loaded into this cluster | Follow the named-cluster image-load command |
| CI red | A real check or external dependency failed | Read the first failed step; reproduce its command |

## Glossary

**Repository:** versioned project files. **Commit:** a recorded change. **Branch:** a separate line of work. **Pull request:** a proposed merge for review. **CI:** automatic integration checks. **Artifact:** output of a build. **Image:** packaged runtime and application. **Container:** running instance of an image. **Port:** network endpoint number. **Health check:** a probe of service behavior. **Pipeline:** ordered automation stages. **Deployment:** desired set of Kubernetes pods. **Service:** stable access to selected pods.
