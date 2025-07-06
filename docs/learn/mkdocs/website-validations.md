# MkDocs Validation System

This project includes a comprehensive validation system to prevent common MkDocs configuration and content issues.

## 🛡️ What It Prevents

- **Configuration errors**: Invalid YAML, missing files, broken plugin configurations
- **Blog post issues**: Missing frontmatter, invalid authors, incorrect categories
- **Template errors**: Broken Jinja2 syntax, unsafe variable access
- **Icon issues**: Invalid icon references that cause build failures
- **Build failures**: Catches issues before they break the build process

## 🔧 Tools Included

### 1. Validation Scripts

- `tests/validate_config.py` - Validates MkDocs configuration
- `tests/validate_blog_posts.py` - Validates blog post frontmatter and content
- `tests/test_mkdocs_config.py` - Comprehensive pytest test suite
- `scripts/validate-all.sh` - Runs all validations with colored output

### 2. Just Commands

Use [Just](https://github.com/casey/just) for easy command running:

```bash
# Install dependencies and set up validation
just init

# Run all validation checks
just validate

# Run comprehensive checks (validate + test + build)
just check-all

# Quick development check
just dev-check

# Create a new blog post with proper template
just new-post "My New Post Title"

# Validate a specific blog post
just validate-post docs/blog/posts/my-post.md
```

### 3. Git Hooks

Install git hooks to run validation automatically:

```bash
# Install pre-commit and pre-push hooks
./scripts/install-hooks.sh

# Or use pre-commit (recommended)
pip install pre-commit
pre-commit install
```

### 4. GitHub Actions

Automated validation runs on every push and pull request:

- YAML validation
- Configuration validation
- Blog post validation
- Build testing
- Optional link checking

## 🚀 Quick Start

1. **Install dependencies:**

   ```bash
   just init
   ```

2. **Run validation:**

   ```bash
   just validate
   ```

3. **Install git hooks:**

   ```bash
   ./scripts/install-hooks.sh
   ```

4. **Test everything:**

   ```bash
   just check-all
   ```

## 📋 Validation Checklist

### Configuration Validation

- ✅ MkDocs configuration loads successfully
- ✅ All referenced files exist
- ✅ Blog plugin configuration is valid
- ✅ Theme icons are valid
- ✅ Template overrides have correct syntax

### Blog Post Validation

- ✅ All posts have valid frontmatter
- ✅ Required fields (date) are present
- ✅ Authors configuration matches plugin settings
- ✅ Categories are in allowed list
- ✅ Excerpt separators are present

### Build Validation

- ✅ MkDocs builds without errors
- ✅ Strict mode passes
- ✅ No template rendering errors
- ✅ All plugins load correctly

## 🔍 Common Issues Caught

### 1. Authors Configuration Mismatch

**Problem:** Authors enabled in config but no `.authors.yml` file
**Solution:** Either disable authors or create the authors file

### 2. Invalid Icon References

**Problem:** Using non-existent FontAwesome icons
**Solution:** Use valid icon names from supported icon sets

### 3. Missing Blog Post Frontmatter

**Problem:** Blog posts without proper YAML frontmatter
**Solution:** Ensure all posts have required fields

### 4. Template Variable Access

**Problem:** Unsafe access to `page.meta` without checking if `page` exists
**Solution:** Use safe access patterns: `page and page.meta and page.meta.field`

## 🛠️ Customization

### Adding New Validations

1. **Add to validation scripts:**

   ```python
   # In tests/validate_config.py
   def validate_custom_feature(config):
       # Your validation logic
       pass
   ```

2. **Add to pytest:**

   ```python
   # In tests/test_mkdocs_config.py
   def test_custom_feature(self, config):
       # Your test logic
       assert condition, "Error message"
   ```

3. **Add to justfile:**

   ```bash
   # Custom validation command
   validate-custom:
       @echo "🔍 Running custom validation..."
       python tests/validate_custom.py
   ```

### Configuring Pre-commit

Edit `.pre-commit-config.yaml` to add or modify hooks:

```yaml
- repo: local
  hooks:
    - id: custom-validation
      name: Custom Validation
      entry: python tests/validate_custom.py
      language: python
      files: ^(mkdocs\.yml|docs/.*\.md)$
```

## 📊 Performance

The validation system is designed to be fast:

- Configuration validation: ~0.1s
- Blog post validation: ~0.2s
- Full build test: ~2-5s
- Complete validation suite: ~5-10s

## 🔗 Integration

### VS Code

Add to `.vscode/tasks.json`:

```json
{
    "label": "Validate MkDocs",
    "type": "shell",
    "command": "just validate",
    "group": "build",
    "presentation": {
        "echo": true,
        "reveal": "always"
    }
}
```

### IDE Integration

Most IDEs can run Just commands directly or you can create run configurations for the validation scripts.

## 🆘 Troubleshooting

### Validation Fails But Build Works

This usually means the validation is too strict. Check the specific error and adjust the validation rules if needed.

### Git Hooks Not Running

Ensure hooks are executable:

```bash
chmod +x .git/hooks/pre-commit
chmod +x .git/hooks/pre-push
```

### Missing Dependencies

Install all required dependencies:

```bash
pip install -r dependencies/requirements.txt
```

## 📚 Further Reading

- [MkDocs Configuration](https://www.mkdocs.org/user-guide/configuration/)
- [MkDocs Material Setup](https://squidfunk.github.io/mkdocs-material/setup/)
- [Pre-commit Hooks](https://pre-commit.com/)
- [Just Command Runner](https://github.com/casey/just)
