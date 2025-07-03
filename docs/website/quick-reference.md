---
title: Quick Reference
description: Quick reference for common MkDocs tasks and commands
tags:
  - reference
  - commands
  - quickstart
---

# Quick Reference

Essential commands and configurations for working with our MkDocs setup.

## Essential Commands

### Development
```bash
just serve          # Start dev server (localhost:8000)
just watch          # Auto-rebuild on changes
just validate       # Run all validations
just build          # Build site
just clean          # Clean build artifacts
```

### Content Creation
```bash
just new-post "Title"     # Create new blog post
just format               # Format all files
just lint                 # Check formatting
```

### Deployment
```bash
just deploy               # Deploy to GitHub Pages
just deploy-version 1.0   # Deploy versioned docs
```

## Page Frontmatter

### Basic Page
```yaml
---
title: Page Title
description: SEO description
---
```

### Full Options
```yaml
---
title: Page Title
description: SEO description
tags:
  - tag1
  - tag2
comments: true
hide:
  - navigation
  - toc
---
```

## Markdown Quick Reference

### Formatting
```markdown
**Bold** or __Bold__
*Italic* or _Italic_
~~Strikethrough~~
==Highlight==
^Superscript^
~Subscript~
```

### Links
```markdown
[External Link](https://example.com)
[Internal Link](../page.md)
[[Wikilink]]
[[Wikilink|Custom Text]]
```

### Admonitions
```markdown
!!! note "Title"
    Content here

!!! warning
    Warning content

??? tip "Collapsible"
    Hidden by default
```

### Code
````markdown
`inline code`

```python
# Code block
print("Hello")
```

```python title="file.py" linenums="1" hl_lines="2"
def function():
    return True  # (1)
```

1. Annotation
````

### Lists
```markdown
- Unordered item
  - Nested item

1. Ordered item
2. Second item

- [x] Completed task
- [ ] Pending task
```

## Configuration Snippets

### Enable Comments
```yaml
# In page frontmatter
---
comments: true
---
```

### Custom CSS
```css
/* In docs/assets/css/extra.css */
:root {
  --md-primary-fg-color: #2563eb;
  --md-accent-fg-color: #10b981;
}
```

### Navigation Structure
```yaml
# In mkdocs.yml
nav:
  - Home: index.md
  - Guides:
      - Quick Start: quick-start.md
      - Advanced: advanced.md
```

## File Structure

```
project/
├── mkdocs.yml         # Main config
├── justfile           # Task runner
├── docs/
│   ├── index.md       # Homepage
│   ├── assets/        # Static files
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── website/       # This section
├── overrides/         # Theme overrides
└── tests/             # Validation
```

## Common Tasks

### Add a New Page
1. Create `.md` file in `docs/`
2. Add to `nav:` in `mkdocs.yml`
3. Add frontmatter
4. Write content

### Customize Theme
1. Add CSS to `docs/assets/css/`
2. Reference in `mkdocs.yml`:
   ```yaml
   extra_css:
     - assets/css/custom.css
   ```

### Enable Feature
1. Check available features in docs
2. Add to `mkdocs.yml`:
   ```yaml
   theme:
     features:
       - feature.name
   ```

### Debug Issues
```bash
just validate          # Check configuration
just build --strict    # Strict build
mkdocs serve -v       # Verbose output
```

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Search | ++ctrl+k++ or ++cmd+k++ |
| Navigate | ++tab++ |
| Copy code | Click copy icon |
| Toggle theme | Click sun/moon |

## Getting Help

- Run `just validate` for configuration checks
- Check [Validation Guide](website-validations.md)
- Review [Configuration Reference](configuration-reference.md)
- See [MkDocs Material Docs](https://squidfunk.github.io/mkdocs-material/)

---

_Keep this reference handy for quick lookups!_