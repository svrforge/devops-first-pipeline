# OCI architecture planning lab

This is a design exercise, not an OCI deployment script. No account, credit card or credentials are required to complete it. Do not assume any shape or resource is free: eligibility, capacity and pricing vary.

Trace a request: client → DNS → HTTPS endpoint → private application network → service. For each hop record owner, address/port, allowed source, failure mode and observable signal.

| Area | Design question | Evidence to collect before provisioning |
|---|---|---|
| IAM | Which identity can deploy, read logs, change networking? | Minimal policy and compartment scope |
| Network | Which ports are reachable from the Internet? | Subnet, route, gateway, NSG/security-list diagram |
| Compute | VM or Kubernetes, and why? | Capacity estimate and operational burden |
| Registry | Where is the image, and how is it authenticated? | Digest and pull identity strategy |
| TLS | Where is encryption terminated and renewed? | Certificate ownership and renewal process |
| Cost | What continues billing when the app stops? | Current official estimates for compute, disk, LB, egress |
| Recovery | How do you return to a known version? | Immutable version, rollout verification, rollback decision |
| Cleanup | Which resources must be removed? | Resource inventory and teardown order |

Deliver a one-page proposal. Explain why a single VM might be a better first learning deployment than Kubernetes. Never commit API signing keys, kubeconfigs or Terraform state.

Official starting points: [OCI documentation](https://docs.oracle.com/en-us/iaas/Content/home.htm), [Terraform language](https://developer.hashicorp.com/terraform/language), [Kubernetes concepts](https://kubernetes.io/docs/concepts/).
