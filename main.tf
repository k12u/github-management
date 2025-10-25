# GitHub repository management with Terraform
# This file demonstrates how the repository configurations could be implemented

terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

# Configure the GitHub Provider
provider "github" {
  # Configuration can be set via environment variables:
  # GITHUB_TOKEN or GITHUB_OWNER
}

# Load repository configurations
locals {
  repositories_config = yamldecode(file("repositories.yaml"))
}

# Create repositories based on configuration
resource "github_repository" "repositories" {
  for_each = { for repo in local.repositories_config.repositories : repo.name => repo }

  name        = each.value.name
  description = each.value.description
  visibility  = each.value.private ? "private" : "public"

  has_issues   = each.value.has_issues
  has_projects = each.value.has_projects
  has_wiki     = each.value.has_wiki

  auto_init          = each.value.auto_init
  gitignore_template = each.value.gitignore_template
  license_template   = each.value.license_template

  allow_squash_merge     = each.value.allow_squash_merge
  allow_merge_commit     = each.value.allow_merge_commit
  allow_rebase_merge     = each.value.allow_rebase_merge
  delete_branch_on_merge = each.value.delete_branch_on_merge

  topics               = each.value.topics
  archived             = each.value.archived
  vulnerability_alerts = each.value.vulnerability_alerts
}