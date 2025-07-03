# Linting and Formatting Setup

This project uses a comprehensive linting and formatting setup to ensure code quality and consistency across all file types.

## 🛠️ Tools Used

### Prettier

- **Purpose**: Format YAML, Markdown, JSON, JavaScript, CSS, and HTML files
- **Config**: `.prettierrc.json`
- **Ignore**: `.prettierignore`
- **Commands**: `npm run format`, `npm run format:check`

### Python Tools

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting and style checking
- **Config**: `pyproject.toml`, `.flake8`

### YAML Tools

- **yamllint**: YAML linting
- **Config**: `.yamllint.yml`

### Pre-commit Hooks

- **Tool**: pre-commit
- **Config**: `.pre-commit-config.yaml`
- **Auto-runs**: All formatters and linters before commits

## 📋 What Gets Checked

### ✅ Formatting Issues Caught

- **YAML**: Indentation, trailing spaces, line length
- **Python**: PEP 8 compliance, import sorting, line length
- **Markdown**: Consistent formatting, line wrapping
- **JSON**: Proper indentation and structure
- **JavaScript/CSS**: Standard formatting rules

### ✅ Code Quality Issues Caught

- **Python**: Unused imports, complexity, syntax errors
- **YAML**: Invalid syntax, inconsistent structure
- **General**: Trailing whitespace, missing newlines, large files

### ✅ MkDocs-Specific Issues Caught

- **Configuration**: Invalid plugin settings, missing files
- **Blog Posts**: Missing frontmatter, invalid authors, wrong categories
- **Templates**: Unsafe variable access, syntax errors
- **Icons**: Invalid icon references

## 🚀 Usage

### Quick Commands (using Just)

```bash
# Format all files
just format

# Format specific file types
just format-python
just format-yaml
just format-markdown
just format-json

# Run all linting checks
just lint

# Run comprehensive validation
just check-all
```

### NPM Scripts

```bash
# Format all files with Prettier
npm run format

# Check formatting without fixing
npm run format:check

# Format specific file types
npm run format:yaml
npm run format:md
npm run format:json
```

### Direct Tool Usage

```bash
# Python formatting
black tests/ scripts/ --line-length 88
isort tests/ scripts/ --profile black
flake8 tests/ scripts/

# YAML linting
yamllint -c .yamllint.yml mkdocs.yml

# Prettier formatting
npx prettier --write .
npx prettier --check .
```

## 🔧 Configuration Details

### Prettier Configuration (`.prettierrc.json`)

```json
{
  "printWidth": 88,
  "tabWidth": 2,
  "useTabs": false,
  "overrides": [
    {
      "files": "*.md",
      "options": {
        "printWidth": 80,
        "proseWrap": "always"
      }
    },
    {
      "files": ["*.yml", "*.yaml"],
      "options": {
        "printWidth": 120
      }
    }
  ]
}
```

### Python Configuration (pyproject.toml)

```toml
[tool.black]
line-length = 88
target-version = ['py311']

[tool.isort]
profile = "black"
line_length = 88
```

### Flake8 Configuration (`.flake8`)

```ini
[flake8]
max-line-length = 88
extend-ignore = E203, W503, E501
max-complexity = 10
```

## 🔄 Pre-commit Integration

### Installation

```bash
pip install pre-commit
pre-commit install
```

### Manual Run

```bash
# Run on all files
pre-commit run --all-files

# Run specific hook
pre-commit run prettier --all-files
pre-commit run black --all-files
```

### Hooks Included

1. **Prettier**: Formats YAML, Markdown, JSON, JS, CSS, HTML
2. **Black**: Formats Python code
3. **isort**: Sorts Python imports
4. **flake8**: Lints Python code
5. **yamllint**: Lints YAML files
6. **Custom MkDocs validators**: Check configuration and content

## 🧪 Testing the Setup

### Automated Tests

```bash
# Test that all linting tools work
python -m pytest tests/test_linting.py -v

# Test MkDocs-specific validation
python -m pytest tests/test_mkdocs_config.py -v
```

### Manual Testing

```bash
# Test formatting detection
npm run format:check

# Test Python linting
flake8 tests/ scripts/

# Test YAML linting
yamllint -c .yamllint.yml mkdocs.yml

# Test comprehensive validation
./scripts/validate-all.sh
```

## 🚨 Common Issues and Fixes

### Issue: Prettier and yamllint conflict

**Solution**: Configure yamllint to be less strict about formatting that Prettier handles:

```yaml
# .yamllint.yml
rules:
  line-length:
    max: 120
    level: warning
```

### Issue: Black and flake8 conflict

**Solution**: Configure flake8 to ignore Black-handled issues:

```ini
# .flake8
extend-ignore = E203, W503, E501
```

### Issue: Pre-commit hooks fail

**Solution**: Run formatters first, then commit:

```bash
just format
git add .
git commit -m "Fix formatting"
```

### Issue: YAML formatting breaks MkDocs

**Solution**: Use `--unsafe` flag for YAML checking:

```yaml
# .pre-commit-config.yaml
- id: check-yaml
  args: ['--unsafe']
```

## 📊 Performance

### Typical Run Times

- **Prettier check**: ~1-2 seconds
- **Python linting**: ~2-3 seconds
- **YAML linting**: ~0.5 seconds
- **Full pre-commit**: ~5-10 seconds
- **Complete validation**: ~10-15 seconds

### Optimization Tips

1. **Use `.prettierignore`** to exclude large generated files
2. **Configure flake8** to skip complex legacy code
3. **Run formatters** before linters to reduce iterations
4. **Use caching** in CI/CD pipelines

## 🔗 Integration

### VS Code Integration

Add to `.vscode/settings.json`:

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "python.formatting.provider": "black",
  "python.linting.flake8Enabled": true,
  "python.linting.enabled": true
}
```

### GitHub Actions Integration

```yaml
- name: Check formatting
  run: |
    npm run format:check
    black --check tests/ scripts/
    flake8 tests/ scripts/
    yamllint -c .yamllint.yml mkdocs.yml
```

### IDE Integration

Most modern IDEs support these tools through plugins:

- **PyCharm**: Built-in Black, flake8 support
- **VS Code**: Prettier, Python extensions
- **Vim/Neovim**: ALE, CoC plugins
- **Emacs**: LSP mode, format-all

## 📚 Further Reading

- [Prettier Documentation](https://prettier.io/docs/en/)
- [Black Documentation](https://black.readthedocs.io/)
- [flake8 Documentation](https://flake8.pycqa.org/)
- [Pre-commit Documentation](https://pre-commit.com/)
- [yamllint Documentation](https://yamllint.readthedocs.io/)
