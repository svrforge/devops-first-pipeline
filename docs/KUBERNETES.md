# Optional local Kubernetes lab

Prerequisites: Docker running, `kind`, `kubectl`. This creates a named **local learning cluster**. Do not run these commands against a workplace/production cluster.

```bash
kind create cluster --name devops-learning
kubectl config current-context
```

Confirm the output is `kind-devops-learning` before continuing. All commands below explicitly select that context.

```bash
docker build -t devops-first-pipeline:local .
kind load docker-image devops-first-pipeline:local --name devops-learning
kubectl --context kind-devops-learning apply -f k8s/app.yaml
kubectl --context kind-devops-learning rollout status deployment/devops-first-pipeline --timeout=120s
kubectl --context kind-devops-learning get pods
kubectl --context kind-devops-learning port-forward service/devops-first-pipeline 8000:8000
```

Open <http://localhost:8000/health>. Stop port forwarding with Ctrl+C. Readiness decides whether a pod receives traffic; liveness decides whether it needs restarting. Both use `/health` for this simple process-only example.

The image uses `imagePullPolicy: Never` because you load it directly into kind. `ErrImageNeverPull` means you missed the load step or changed the image tag. This manifest is not a registry-backed cloud deployment.

After rebuilding the same local image tag, load it again, then restart and verify:

```bash
kind load docker-image devops-first-pipeline:local --name devops-learning
kubectl --context kind-devops-learning rollout restart deployment/devops-first-pipeline
kubectl --context kind-devops-learning rollout status deployment/devops-first-pipeline --timeout=120s
```

Cleanup only this lab's resources:

```bash
kubectl --context kind-devops-learning delete -f k8s/app.yaml
kind delete cluster --name devops-learning
```

Kubernetes manifests are an optional manual exercise; the default CI does not provision a cluster or claim to validate a Kubernetes rollout.
