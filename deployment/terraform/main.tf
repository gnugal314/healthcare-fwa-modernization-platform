# Placeholder Terraform scaffold for Azure SQL / storage / Key Vault deployment.
terraform {
  required_version = ">= 1.5.0"
}

variable "environment" {
  type    = string
  default = "dev"
}
