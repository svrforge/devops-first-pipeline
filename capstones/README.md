# Three capstones: prove what you can operate

Progress is self-reported. These rubrics are evidence requirements, not certifications or employment promises.

## A. Ship a verified service

1. Add `/ready` with a documented JSON contract and real HTTP tests.
2. Build a non-root image and prove it becomes healthy.
3. Open a PR; show the commit SHA and all required CI checks passing.
4. Explain why your tests would detect a regression.

Pass: no failing tests, no embedded secrets, documented startup/stop commands, reviewable diff.

## B. Operate and recover locally

1. Deploy to the named kind learning cluster using the Kubernetes guide.
2. Demonstrate two ready pods and service access.
3. Introduce a wrong image tag in a branch and diagnose the pod event.
4. Restore the working configuration and prove rollout recovery.
5. Complete the incident template with timestamps and evidence.

Pass: explain readiness vs liveness, image availability, context choice and recovery. Never use a work cluster.

## C. Design the cloud path

1. Complete the local Terraform lab including a no-change second plan.
2. Draw a proposed OCI route from client to service, naming IAM and network boundaries.
3. Produce a cost worksheet and teardown plan before provisioning anything.
4. Document credential handling, image registry, rollout/rollback and monitoring.
5. Separate demonstrated facts from proposed architecture.

Pass: no invented production claims or costs, least-privilege reasoning, clear remaining risks. See [cloud design guide](../docs/CLOUD.md).

## Evidence rubric (0–2 each)

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Reproducibility | Missing commands | Partial setup | Another learner can repeat it |
| Correctness | No checks | Happy path only | Success and failure behavior verified |
| Recovery | Restart guesses | Fix without proof | Evidence, mitigation, verified recovery |
| Security | Secrets / broad access | Risks listed | Practical least-privilege controls |
| Explanation | Tool names only | Describes actions | Explains tradeoffs and limits |

Aim for 8/10 with no zero in security. Ask another learner to reproduce your notes; self-scoring alone cannot establish competence.
