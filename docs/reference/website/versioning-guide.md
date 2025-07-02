---
title: Versioning Guide
description: How to set up and manage documentation versions with Mike
tags:
  - versioning
  - mike
  - deployment
---

# Documentation Versioning with Mike

This guide explains how to set up and manage multiple versions of your documentation using Mike, a versioning tool for MkDocs.

## What is Mike?

Mike is a Python utility that makes it easy to deploy multiple versions of your MkDocs documentation to GitHub Pages or other hosting platforms. It creates a separate branch (`gh-pages`) with all your documentation versions.

## Features

✅ **Multiple Versions** - Deploy and maintain multiple documentation versions  
✅ **Version Aliases** - Create aliases like "latest" and "stable"  
✅ **Default Version** - Set which version users see by default  
✅ **GitHub Pages Integration** - Works seamlessly with GitHub Pages  
✅ **Automatic Deployment** - Integrated with CI/CD workflows

## Quick Start

### 1. Initial Setup

The first time you deploy, use our helper script:

```bash
# Deploy your first version
./scripts/deploy-version.sh 1.0.0

# Or manually:
mike deploy --push --update-aliases 1.0.0 latest
mike set-default --push latest
```

### 2. Deploy New Versions

```bash
# Deploy a new version
./scripts/deploy-version.sh 2.0.0

# Deploy with custom title
./scripts/deploy-version.sh 2.0.0 "Version 2.0 - Major Update"
```

### 3. Manage Versions

```bash
# List all versions
mike list

# Set version aliases
mike alias --push 2.0.0 latest
mike alias --push 1.9.0 stable

# Set default version (what users see at root URL)
mike set-default --push latest

# Delete a version
mike delete --push 1.0.0
```

## Version Strategy

### Recommended Approach

1. **Semantic Versioning**: Use semantic versioning (e.g., 1.0.0, 1.1.0, 2.0.0)
2. **Aliases**: Use meaningful aliases:
   - `latest` - Most recent version
   - `stable` - Latest stable release
   - `dev` - Development/preview version
3. **Default**: Set `latest` or `stable` as default

### Example Workflow

```bash
# Release workflow
mike deploy --push 1.0.0 "v1.0.0"           # Deploy specific version
mike alias --push 1.0.0 stable              # Mark as stable
mike alias --push 1.0.0 latest              # Mark as latest
mike set-default --push stable              # Set as default

# Development workflow
mike deploy --push dev "Development"         # Deploy dev version
# (don't set as latest or stable)
```

## GitHub Actions Integration

Create `.github/workflows/docs.yml`:

```yaml
name: Deploy Documentation

on:
  push:
    branches: [main]
    tags: ['v*']
  pull_request:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    if: github.event_name == 'push'

    steps:
    - uses: actions/checkout@v4
      with:
        fetch-depth: 0

    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        pip install -r requirements.txt

    - name: Configure Git
      run: |
        git config user.name github-actions
        git config user.email github-actions@github.com

    - name: Deploy latest
      if: github.ref == 'refs/heads/main'
      run: |
        mike deploy --push --update-aliases dev latest

    - name: Deploy version
      if: startsWith(github.ref, 'refs/tags/v')
      run: |
        VERSION=${GITHUB_REF#refs/tags/v}
        mike deploy --push --update-aliases $VERSION stable
        mike set-default --push stable
```

## Manual Commands

### Basic Commands

```bash
# Build and serve locally (no versioning)
mkdocs serve

# Deploy current version
mike deploy [version] [title]

# Deploy and set as latest
mike deploy --push --update-aliases 1.0.0 latest

# Serve all versions locally
mike serve
```

### Advanced Commands

```bash
# Deploy without pushing to remote
mike deploy 1.0.0

# Push all changes
mike deploy --push 1.0.0

# Update aliases when deploying
mike deploy --update-aliases 1.0.0 latest stable

# Deploy to custom branch
mike deploy --branch custom-branch 1.0.0

# Deploy to custom remote
mike deploy --remote upstream 1.0.0
```

## Configuration

### MkDocs Configuration

Your `mkdocs.yml` should include:

```yaml
extra:
  version:
    provider: mike
    default: latest
    alias: true
```

### Custom Styling

The version selector is automatically added to your site. You can customize it with CSS:

```css
/* Version selector styling */
.md-version {
  /* Custom styles */
}

.md-version__current {
  /* Current version styling */
}

.md-version__list {
  /* Version dropdown styling */
}
```

## Troubleshooting

### Common Issues

**Mike command not found**

```bash
pip install mike
```

**Permission denied**

```bash
# Make sure you have write access to the repository
git remote -v
```

**No versions found**

```bash
# Check if gh-pages branch exists
git branch -r | grep gh-pages

# If not, deploy your first version
mike deploy --push 1.0.0 latest
```

**Version not showing**

```bash
# Check mike configuration
mike list

# Verify GitHub Pages settings in repository settings
```

### GitHub Pages Setup

1. Go to repository **Settings** → **Pages**
2. Set **Source** to "Deploy from a branch"
3. Select **Branch**: `gh-pages` and **Folder**: `/ (root)`
4. Save settings

## Best Practices

### 1. Version Naming

- Use semantic versioning: `1.0.0`, `1.1.0`, `2.0.0`
- Include patch versions for documentation fixes
- Use descriptive titles: `"Version 2.0 - New Features"`

### 2. Alias Management

- Keep `latest` pointing to the newest version
- Use `stable` for production-ready versions
- Consider `dev` or `preview` for development versions

### 3. Default Version

- Set `stable` as default for production sites
- Set `latest` as default for development/preview sites
- Update default when releasing major versions

### 4. Cleanup

- Regularly remove old versions that are no longer supported
- Keep at least 2-3 recent versions available
- Archive very old versions rather than deleting

## Integration with CI/CD

### Automatic Deployment

```bash
# In your CI/CD pipeline
if [[ $GITHUB_REF == refs/tags/* ]]; then
  VERSION=${GITHUB_REF#refs/tags/v}
  mike deploy --push $VERSION stable
  mike set-default --push stable
elif [[ $GITHUB_REF == refs/heads/main ]]; then
  mike deploy --push dev latest
fi
```

### Testing Versions

```bash
# Test locally before deploying
mike serve --dev-addr localhost:8001

# Build without deploying
mike deploy --no-push test-version
```

---

_For more information, see the [Mike documentation](https://github.com/jimporter/mike) and [MkDocs Material versioning guide](https://squidfunk.github.io/mkdocs-material/setup/setting-up-versioning/)._
