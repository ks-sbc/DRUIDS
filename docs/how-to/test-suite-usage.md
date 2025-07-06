---
title: "How to Use the Test Suite for Link Validation"
description: "Step-by-step guide for running comprehensive link validation and quality tests"
created: 2025-01-22
updated: 2025-01-22
type: "docs/how-to"
security: "L0"
version: "1.0.0"
document_id: "HOW-TEST-2025-001-L0"
tags: ["testing", "validation", "links", "workflow", "mkdocs"]
draft: false
author: ["Test Development Team"]
---

# How to Use the Test Suite for Link Validation

## Quick Start

### Run All Link Validation Tests

```bash
just test-comprehensive
```

This command runs the complete test suite including:
- Build quality analysis
- Link validation 
- Static analysis
- Content structure validation

### Check Specific Issues

```bash
# Test only link-related issues
just test-links

# Check build warnings and errors
just test-build-quality

# Validate markdown syntax
just test-static

# Check content organization
just test-structure
```

## Detailed Usage

### 1. Diagnose Current Issues

Before fixing links, understand what's broken:

```bash
# Get comprehensive issue report
just test-build-quality
```

**Expected Output:**
```
Build Quality Report
====================
Total issues: 58
  Critical: 14
  High: 32
  Medium: 12
  Low: 0

CRITICAL Severity Issues:
- Missing nav file: blog/index.md
- Missing nav file: tutorials/customization-guide.md
[...]
```

### 2. Analyze Link Problems

Run detailed link analysis:

```bash
# Full link validation with detailed output
pytest tests/test_links.py -v -s
```

**What it checks:**
- Navigation configuration links
- Internal markdown links
- Wikilinks (`[[target]]` format)
- Anchor links (`#heading`)
- Cross-file references

### 3. Fix Navigation Issues

**Problem**: `A reference to 'blog/index.md' is included in the 'nav' configuration, which is not found`

**Solution**: Either create the missing file or update mkdocs.yml:

```yaml
# Option 1: Remove from navigation
nav:
  - Home: index.md
  # - Blog: blog/index.md  # Comment out missing file

# Option 2: Create the missing file
# Create docs/blog/index.md with content
```

### 4. Fix Broken Internal Links

**Problem**: `Doc file 'tutorials/index.md' contains a link '../features-demo.md', but the target 'features-demo.md' is not found`

**Solution**: Update the link to point to existing file:

```markdown
<!-- Before (broken) -->
[Feature Demo](../features-demo.md)

<!-- After (fixed) -->
[Feature Demo](../website/features-demo.md)
```

### 5. Convert Absolute to Relative Links

**Problem**: `Doc file '_templates/proposal-template.md' contains an absolute link '/tutorials/your-first-revolutionary-commit.md'`

**Solution**: Convert to relative path:

```markdown
<!-- Before (absolute) -->
[Tutorial](/tutorials/your-first-revolutionary-commit.md)

<!-- After (relative) -->
[Tutorial](../tutorials/your-first-revolutionary-commit.md)
```

## Workflow Integration

### During Development

1. **Before making changes**:
   ```bash
   just test-links
   ```

2. **After adding content**:
   ```bash
   just test-static
   ```

3. **Before committing**:
   ```bash
   just test-comprehensive
   ```

### Continuous Integration

Add to your CI pipeline:

```yaml
# .github/workflows/test.yml
- name: Run comprehensive tests
  run: just test-comprehensive
```

### Pre-commit Hook

```bash
# Install pre-commit hook
echo "just test-links" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Interpreting Test Results

### Test Status Meanings

| Status | Symbol | Meaning | Action Required |
|--------|--------|---------|-----------------|
| PASSED | ✅ | No issues found | None |
| FAILED | ❌ | Critical/High issues | Must fix |
| SKIPPED | ⚠️ | Warning level issues | Should fix |

### Common Error Patterns

#### Navigation Reference Errors
```
FAILED tests/test_build_quality.py::TestBuildQuality::test_no_broken_navigation_links
```
**Cause**: mkdocs.yml references non-existent files  
**Fix**: Update navigation or create missing files

#### Broken Internal Links
```
FAILED tests/test_links.py::TestLinkValidation::test_internal_markdown_links
```
**Cause**: Markdown links point to non-existent targets  
**Fix**: Update link URLs or create target files

#### Malformed Wikilinks
```
FAILED tests/test_static_analysis.py::TestStaticAnalysis::test_link_syntax_validation
```
**Cause**: Incorrect wikilink syntax `[[target]` (missing close bracket)  
**Fix**: Correct syntax to `[[target]]`

### Warning vs Error Thresholds

The test suite uses severity-based failure:

- **Critical/High**: Immediately fail tests
- **Medium**: Generate warnings (may skip tests)
- **Low**: Informational only

## Advanced Usage

### Test Specific Files

```bash
# Test only files matching pattern
pytest tests/test_links.py -k "navigation" -v

# Test specific directory
pytest tests/test_static_analysis.py::TestStaticAnalysis::test_markdown_structure_quality -v
```

### Debugging Failed Tests

```bash
# Get detailed failure information
pytest tests/test_build_quality.py -v -s --tb=long

# Show all test output
pytest tests/ -v -s --tb=short
```

### Custom Test Configuration

Create `pytest.ini` in project root:

```ini
[tool:pytest]
markers = 
    unit: fast unit tests
    integration: integration tests requiring full environment
    slow: tests that take a long time

# Run only fast tests by default
addopts = -v -x --tb=short
testpaths = tests
```

### Generate Test Reports

```bash
# HTML coverage report
pytest tests/ --cov=tests --cov-report=html

# JUnit XML for CI
pytest tests/ --junitxml=test-results.xml

# JSON report for automation
pytest tests/ --json-report --json-report-file=test-report.json
```

## Troubleshooting

### Test Discovery Issues

**Problem**: `ImportError: No module named 'test_utils'`

**Solution**: Ensure you're running from project root:
```bash
cd /path/to/project
python -m pytest tests/
```

### Path Resolution Errors

**Problem**: Tests can't find docs directory

**Solution**: Verify directory structure:
```bash
ls -la docs/  # Should show markdown files
pytest tests/ --collect-only  # Verify test discovery
```

### Performance Issues

**Problem**: Tests run slowly on large documentation sets

**Solutions**:
```bash
# Run tests in parallel
pip install pytest-xdist
pytest tests/ -n auto

# Run only modified files
pytest tests/ --lf  # last failed
pytest tests/ --ff  # failed first
```

### Unicode/Encoding Errors

**Problem**: `UnicodeDecodeError` during file reading

**Solution**: Ensure all markdown files are UTF-8 encoded:
```bash
# Check file encodings
file -bi docs/**/*.md

# Convert if necessary
iconv -f ISO-8859-1 -t UTF-8 file.md > file_utf8.md
```

## Integration with Existing Tools

### With MkDocs serve

```bash
# Test before starting development server
just test-links && mkdocs serve
```

### With Pre-commit

Add to `.pre-commit-config.yaml`:
```yaml
repos:
  - repo: local
    hooks:
      - id: test-links
        name: Test link validation
        entry: bash -c 'just test-links'
        language: system
        pass_filenames: false
```

### With VS Code

Add to `.vscode/tasks.json`:
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Test Links",
            "type": "shell",
            "command": "just test-links",
            "group": "test",
            "presentation": {
                "reveal": "always",
                "panel": "new"
            }
        }
    ]
}
```

## Best Practices

### Regular Testing Schedule

1. **Daily**: Run `just test-links` on modified content
2. **Weekly**: Full `just test-comprehensive` validation
3. **Pre-release**: Complete test suite with manual review

### Link Maintenance

1. **Use relative links** whenever possible
2. **Test external links** separately (not covered by this suite)
3. **Document intentional broken links** with comments
4. **Update navigation** when moving or renaming files

### Content Organization

1. **Follow Diátaxis structure** for better test compliance
2. **Use consistent frontmatter** across similar content types
3. **Maintain heading hierarchy** (H1 → H2 → H3)
4. **Include meaningful metadata** in frontmatter

## Getting Help

### Command Reference

```bash
# Show all available test commands
just --list | grep test

# Show pytest help
pytest --help

# Show test documentation
pytest --markers
```

### Test Module Documentation

```bash
# View test docstrings
python -c "import tests.test_build_quality; help(tests.test_build_quality.TestBuildQuality)"
```

### Debugging Support

```bash
# Enable debug logging
pytest tests/ --log-cli-level=DEBUG

# Show test collection
pytest --collect-only tests/

# Dry run (show what would be tested)
pytest --collect-only tests/ -q
```

---

*This guide covers the most common use cases for the test suite. For complete technical details, see the [Test Suite Reference](../reference/testing/test-suite-reference.md).*