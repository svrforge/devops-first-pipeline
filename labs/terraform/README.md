# Local Terraform lab — no cloud account

Prerequisite: Terraform >=1.4 and <2.0. The built-in terraform_data resource stores a desired input in local state; it creates no server, network or cloud charge.

```bash
terraform -chdir=labs/terraform init
terraform -chdir=labs/terraform fmt -check
terraform -chdir=labs/terraform validate
terraform -chdir=labs/terraform plan
terraform -chdir=labs/terraform apply
terraform -chdir=labs/terraform plan
```

Read the plan before typing yes. After applying, the second plan should show no changes. Compare `plan -var="replicas=3"` with the default. Try `plan -var="replicas=0"` and confirm validation rejects it. State remains local and is ignored by Git.

Clean up this lab's state-managed resource interactively:

```bash
terraform -chdir=labs/terraform destroy
```

This demonstrates plan/apply/state, not real OCI provisioning. Real remote state requires access control, locking, encryption and a team workflow.
