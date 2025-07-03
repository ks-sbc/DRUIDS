# MkDocs Configuration Guide

## Overview

This document explains the simplified configuration setup for the MkDocs project. We've reduced complexity while maintaining all essential functionality.

## Configuration Files

### Primary Configuration
- **mkdocs.yml** - Main MkDocs configuration
- **config/pyproject.toml** - Python tooling (Black, isort, pytest)
- **dependencies/package.json** - Node.js dependencies and scripts
- **config/.prettierrc.json** - Code formatting for Markdown, YAML, JSON

### Supporting Files
- **.yamllint.yml** - YAML linting rules
- **.markdownlint-cli2.yaml** - Markdown linting configuration
- **.pre-commit-config.yaml** - Pre-commit hooks (simplified)
- **justfile** - Primary task runner

## Line Length Standards

We use consistent line lengths across all tools:
- **Python code**: 100 characters (Black, isort)
- **Markdown/YAML/JSON**: 120 characters (Prettier)
- **YAML linting**: 120 characters (yamllint)

## Task Runners

We primarily use **justfile** for all tasks. Common commands:

```bash
# Development
just serve          # Start dev server
just build          # Build site
just test           # Run tests
just format         # Format all files
just validate       # Validate configuration

# Deployment
just deploy         # Deploy to GitHub Pages
```

## Git Hooks

Simplified hooks focus on deployment readiness:

### Pre-commit
- Checks YAML/JSON syntax
- Prevents large files
- Catches merge conflicts
- Quick build test (non-strict)

### Pre-push
- Runs clean build test
- No strict mode enforcement

## Testing Structure

Simplified test suite in `tests/`:
- **test_mkdocs_core.py** - Core functionality (config, build, plugins)
- **test_blog.py** - Blog-specific tests
- **test_giscus_integration.py** - Giscus commenting (with skips for future features)
- **test_markdown_validation.py** - Markdown validation
- **test_deployment_readiness.py** - Comprehensive deployment checks

## Validation

The simplified validation focuses on "will it deploy?":

1. **Essential checks only**:
   - Required files exist
   - YAML is valid
   - Site builds successfully

2. **Skip style checks in automation**:
   - Run formatting manually with `just format`
   - Use `just lint` for detailed checks

## Best Practices

1. **Before committing**: Run `just validate` 
2. **Before pushing**: Run `just test`
3. **For formatting**: Run `just format`
4. **For deployment**: Run `just deploy`

## Removed Redundancies

We removed:
- Duplicate Prettier config (`.prettierrc`)
- Redundant pytest.ini (consolidated into config/pyproject.toml)
- Complex validation scripts
- Strict mode enforcement in hooks
- Overlapping test files
- Style enforcement in pre-commit

## Future Additions

After initial deployment:
- Complete Giscus integration
- Add missing CSS/JSON files
- Configure theme overrides
- Add more comprehensive tests

## Quick Reference

```bash
# Most common commands
mkdocs serve              # Start dev server
mkdocs build              # Build site
just format               # Format all files
just test                 # Run tests
pytest tests/ -v          # Run specific tests
git commit --no-verify    # Skip hooks if needed
```