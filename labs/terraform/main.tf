terraform {
  required_version = ">= 1.4.0, < 2.0.0"
}

variable "service_name" {
  type    = string
  default = "devops-learning"
}

variable "replicas" {
  type    = number
  default = 2
  validation {
    condition     = var.replicas >= 1 && var.replicas <= 5 && floor(var.replicas) == var.replicas
    error_message = "Use an integer from 1 through 5 for this local lab."
  }
}

resource "terraform_data" "service" {
  input = {
    name     = var.service_name
    replicas = var.replicas
  }
}

output "service" {
  value = terraform_data.service.output
}
