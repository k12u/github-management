# Usage Guide

This repository manages GitHub repositories through configuration files.

## Adding a New Repository

To add a new repository, update `repositories.yaml` or `repositories.json`:

### YAML Example:
```yaml
repositories:
  - name: ibi
    description: "ibi repository"
    private: true
    default_branch: main
    has_issues: true
    has_projects: false
    has_wiki: false
    
  # Add another repository:
  - name: my-new-repo
    description: "My new public repository"
    private: false
    default_branch: main
    has_issues: true
    has_projects: true
    has_wiki: true
    topics: ["example", "demo"]
```

## Validation

Before committing changes, validate the configuration:

```bash
python3 validate-config.py
```

## Deployment

The GitHub Actions workflow will automatically:
1. Validate configurations on pull requests
2. Apply changes when merged to main branch

## Manual Deployment with Terraform

```bash
# Initialize Terraform
terraform init

# Plan changes
terraform plan

# Apply changes (requires GITHUB_TOKEN environment variable)
terraform apply
```

## Current Repositories

- **ibi**: Private repository for ibi project