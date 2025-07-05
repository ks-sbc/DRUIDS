# Project Slash Commands Usage Guide

This guide explains how to use the three high-priority project automation commands we've implemented.

## Overview

The project includes three powerful automation commands:

1. **`/project:act-test`** - Local GitHub Actions workflow testing
2. **`/project:deployment-ready`** - Comprehensive deployment validation
3. **`/project:test-debug`** - Intelligent test failure debugging

## Command 1: `/project:act-test`

**Purpose**: Execute comprehensive local GitHub Actions workflow testing using Act

### Basic Usage

```bash
# Check prerequisites only
python scripts/project-act-test.py --check-only

# Test all workflows (test-only mode)
python scripts/project-act-test.py

# Test specific workflow
python scripts/project-act-test.py deploy.yml

# Different execution modes
python scripts/project-act-test.py deploy.yml --mode dry-run    # Show execution plan
python scripts/project-act-test.py deploy.yml --mode test-only # Skip deployment
python scripts/project-act-test.py deploy.yml --mode full      # Full simulation
python scripts/project-act-test.py deploy.yml --mode debug     # Verbose debugging
```

### Advanced Usage

```bash
# Save detailed report
python scripts/project-act-test.py deploy.yml --save-report act_report.json

# Use with unified command interface
python scripts/project-commands.py act-test deploy.yml --mode debug
```

### What It Does

- ✅ Checks prerequisites (Act, Docker, workflow files)
- 🔍 Lists and validates available workflows
- 🚀 Executes workflows locally with environment detection
- 📊 Analyzes execution output and performance
- 💡 Provides recommendations and troubleshooting guidance

## Command 2: `/project:deployment-ready`

**Purpose**: Validate complete deployment readiness with automated checks and remediation

### Basic Usage

```bash
# Check production deployment readiness
python scripts/project-deployment-ready.py

# Check staging environment
python scripts/project-deployment-ready.py --env staging

# Check and attempt auto-fixes
python scripts/project-deployment-ready.py --auto-fix
```

### Advanced Usage

```bash
# Save detailed report
python scripts/project-deployment-ready.py --save-report deployment_report.json

# Use with unified command interface
python scripts/project-commands.py deployment-ready --env production --auto-fix
```

### What It Checks

- 📁 **Configuration Files**: mkdocs.yml, requirements.txt, workflow files
- 🐍 **Dependencies**: Python packages and installation status
- ⚙️ **MkDocs Configuration**: Valid YAML and required sections
- 🔨 **Build Process**: Successful site generation and performance
- 🔄 **Deployment Workflow**: Act-based workflow simulation
- 📋 **Git Repository**: Clean working tree and branch status
- 🧪 **Comprehensive Tests**: Full test suite execution

### Output Example

```
🎉 DEPLOYMENT READY for PRODUCTION
✅ Confidence Score: 95/100
⚠️ Warnings: 2

📋 DEPLOYMENT CHECKLIST:
⚠️ WARNINGS - Recommended to fix:
   • Missing recommended file: README.md
   • Build process is slower than recommended

💡 RECOMMENDATIONS:
   • Monitor deployment process
   • Verify site functionality after deployment
```

## Command 3: `/project:test-debug`

**Purpose**: Intelligent debugging for failing tests with context-aware troubleshooting

### Basic Usage

```bash
# Debug specific test file
python scripts/project-test-debug.py tests/test_act_integration.py

# Debug with verbose output
python scripts/project-test-debug.py tests/test_deployment_readiness.py --verbose

# Debug and attempt auto-fixes
python scripts/project-test-debug.py tests/ --auto-fix
```

### Advanced Usage

```bash
# Debug specific test patterns
python scripts/project-test-debug.py -k "test_workflow"

# Save debug report
python scripts/project-test-debug.py tests/ --save-report debug_report.json

# Use with unified command interface
python scripts/project-commands.py test-debug test_act_integration.py --verbose
```

### What It Analyzes

- 🔍 **Environment Information**: Python, OS, Git, Docker versions
- 📝 **Test Execution**: Captures detailed test output and timing
- 🎯 **Failure Patterns**: Recognizes common failure types:
  - Import/dependency errors
  - File not found issues
  - Permission problems
  - Network connectivity
  - Docker/Act tooling issues
  - YAML configuration errors
- 🩺 **Diagnostic Commands**: Runs relevant diagnostics based on failure type
- 💡 **Recommendations**: Provides specific, actionable solutions

### Failure Pattern Examples

**Import Error Detection**:
```
❌ Detected: Import Error
   Category: dependency, Severity: high
   Solutions:
   1. Install missing dependencies: pip install -r dependencies/requirements.txt
   2. Check if package is in requirements.txt
   3. Verify Python path and virtual environment
```

**Docker Error Detection**:
```
❌ Detected: Docker Error  
   Category: environment, Severity: high
   Solutions:
   1. Start Docker daemon: sudo systemctl start docker
   2. Add user to docker group: sudo usermod -aG docker $USER
   3. Check Docker installation
```

## Unified Command Interface

Use the unified interface for slash-command style execution:

```bash
# Slash command style (simulated)
python scripts/project-commands.py act-test deploy.yml debug
python scripts/project-commands.py deployment-ready production --auto-fix  
python scripts/project-commands.py test-debug test_act_integration.py --verbose
```

## Integration with Existing Tools

These commands integrate seamlessly with existing project infrastructure:

### With Test Runner
```bash
# Use alongside existing test runner
python run_tests.py comprehensive
python scripts/project-deployment-ready.py

# Debug if tests fail
python scripts/project-test-debug.py tests/ --auto-fix
```

### With Act Testing
```bash
# Manual Act usage
bash scripts/test-workflow-locally.sh check

# Automated Act usage
python scripts/project-act-test.py --check-only
```

### In CI/CD Pipeline
```bash
# In GitHub Actions workflow
- name: Check deployment readiness
  run: python scripts/project-deployment-ready.py --env production

- name: Test workflows locally
  run: python scripts/project-act-test.py --mode test-only
```

## Best Practices

### Development Workflow
1. **Before coding**: Run `project-deployment-ready` to ensure environment is clean
2. **During development**: Use `project-test-debug` when tests fail
3. **Before deployment**: Run `project-act-test` to validate workflows
4. **For deployment**: Run `project-deployment-ready` with `--auto-fix`

### Troubleshooting Workflow
1. **Test fails**: Run `project-test-debug` with the failing test
2. **Environment issues**: Check output of diagnostic commands
3. **Workflow issues**: Use `project-act-test` with `--mode debug`
4. **Deployment issues**: Run `project-deployment-ready` for comprehensive check

### Automation Integration
- Add commands to `justfile` or `Makefile` for easy access
- Use in pre-commit hooks for quality gates
- Integrate with IDE for one-click debugging
- Add to CI/CD pipelines for comprehensive validation

## Command Performance

- **`act-test`**: 30-60 seconds (depending on workflow complexity)
- **`deployment-ready`**: 2-5 minutes (comprehensive checks)
- **`test-debug`**: 30-120 seconds (depending on test scope)

## Error Handling

All commands provide:
- ✅ Clear success/failure indicators
- 📊 Detailed progress information
- 🔍 Specific error messages and solutions
- 📄 Optional detailed reports in JSON format
- 🚨 Appropriate exit codes for automation

These commands transform manual debugging and validation processes into automated, intelligent workflows that save significant development time and improve deployment confidence.