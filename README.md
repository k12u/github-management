# github-management

This repository manages the configuration of GitHub repositories for the k12u organization.

## Repository Configuration

Repositories are defined in configuration files:

- `repositories.yaml` - YAML format configuration
- `repositories.json` - JSON format configuration

### Adding a New Repository

To add a new repository, update either configuration file with the repository specification:

```yaml
repositories:
  - name: repository-name
    description: "Repository description"
    private: true/false
    default_branch: main
    # ... other configuration options
```

### Current Repositories

- **ibi** - Private repository for ibi project
