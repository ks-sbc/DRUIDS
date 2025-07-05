---
title: Configuration Reference
description: Complete reference for MkDocs configuration options
tags:
  - configuration
  - reference
  - mkdocs
---

# Configuration Reference

This page provides a complete reference for all configuration options used in our MkDocs setup.

## Core Configuration (mkdocs.yml)

### Site Information

```yaml
site_name: DRUIDS Wiki
site_description: Democratic Revolutionary Unified Information & Documentation System
site_author: KS Socialist Book Club
site_url: https://druids.kssocialistbookclub.com

# Repository
repo_name: ks-sbc/DRUIDS
repo_url: https://github.com/ks-sbc/DRUIDS
edit_uri: edit/main/docs/
```

### Theme Configuration

```yaml
theme:
  name: material
  custom_dir: overrides
  favicon: assets/favicons/favicon.ico
  logo: assets/images/logo.svg
  
  # Color palette
  palette:
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: custom
      accent: custom
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
```

### Features

All available Material theme features:

```yaml
theme:
  features:
    # Announcements
    - announce.dismiss
    
    # Content features
    - content.action.edit
    - content.action.view
    - content.code.annotate
    - content.code.copy
    - content.code.select
    - content.footnote.tooltips
    - content.tabs.link
    - content.tooltips
    
    # Header
    - header.autohide
    
    # Navigation
    - navigation.expand
    - navigation.footer
    - navigation.indexes
    - navigation.instant
    - navigation.instant.prefetch
    - navigation.instant.progress
    - navigation.path
    - navigation.prune
    - navigation.sections
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.top
    - navigation.tracking
    
    # Search
    - search.highlight
    - search.share
    - search.suggest
    
    # Table of contents
    - toc.follow
    - toc.integrate
```

### Plugins

```yaml
plugins:
  # Search functionality
  - search
  
  # Obsidian compatibility
  - pub-obsidian:
      obsidian_dir: .obsidian
      templates_dir: _templates
      backlinks:
        enabled: true
      callouts:
        enabled: true
        indentation: spaces
      comments:
        enabled: false
      links:
        wikilinks_enabled: true
  
  # Git information
  - git-revision-date-localized:
      enable_creation_date: true
      type: timeago
      timezone: UTC
      locale: en
      fallback_to_build_date: false
  
  # Content tagging
  - tags
  
  # Blog (when enabled)
  # - blog:
  #     enabled: true
  #     blog_dir: blog
  #     post_dir: posts
  #     categories: true
  #     archive: true
```

### Markdown Extensions

```yaml
markdown_extensions:
  # Standard extensions
  - abbr
  - admonition
  - attr_list
  - def_list
  - footnotes
  - md_in_html
  - meta
  
  # Table of contents
  - toc:
      permalink: true
      title: On this page
      toc_depth: 2-3
  
  # PyMdown extensions
  - pymdownx.arithmatex:
      generic: true
  - pymdownx.betterem:
      smart_enable: all
  - pymdownx.caret
  - pymdownx.critic
  - pymdownx.details
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.keys
  - pymdownx.mark
  - pymdownx.smartsymbols
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.tilde
```

## Extra Configuration

### JavaScript and CSS

```yaml
extra_javascript:
  - assets/js/mathjax.js
  - assets/js/giscus.js
  - https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js

extra_css:
  - assets/css/druids-theme.css
  - assets/css/druids-layout.css
  - assets/css/druids-components.css
  - assets/css/druids-utilities.css
  - assets/css/giscus.css
```

### Comments (Giscus)

```yaml
extra:
  comments:
    enabled: true
    provider: giscus
    giscus:
      repo: ks-sbc/DRUIDS
      repo-id: R_kgDOOsxCLA
      category: General
      category-id: DIC_kwDOOsxCLM4CsOJY
      mapping: pathname
      strict: 0
      reactions: 1
      emit-metadata: 0
      input-position: top
      theme: preferred_color_scheme
      lang: en
      loading: lazy
```

### Analytics (Optional)

```yaml
extra:
  analytics:
    provider: google
    property: !ENV [GOOGLE_ANALYTICS_KEY, ""]
    feedback:
      title: Was this page helpful?
      ratings:
        - icon: material/emoticon-happy-outline
          name: This page was helpful
          data: 1
          note: Thanks for your feedback!
        - icon: material/emoticon-sad-outline
          name: This page could be improved
          data: 0
          note: Thanks! Help us improve by filing an issue.
```

### Social Links

```yaml
extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/ks-sbc/DRUIDS
      name: GitHub Repository
    - icon: fontawesome/brands/mastodon
      link: https://kolektiva.social/@kssbc
      name: Follow on Mastodon
    - icon: fontawesome/solid/rss
      link: /feed_rss_created.xml
      name: RSS Feed
```

## Environment Variables

Supported environment variables:

```bash
# Giscus configuration
GISCUS_REPO_ID="your-repo-id"
GISCUS_CATEGORY_ID="your-category-id"

# Analytics (optional)
GOOGLE_ANALYTICS_KEY="your-analytics-key"

# Build environment
CI=true  # Disables certain features in CI
```

## File Structure

Required directory structure:

```
project/
├── mkdocs.yml                  # Main configuration
├── dependencies/
│   ├── requirements.txt       # Python dependencies
│   └── package.json          # Node.js dependencies
├── config/
│   ├── pyproject.toml        # Python tooling config
│   └── .prettierrc.json      # Code formatting config
├── justfile                   # Task automation
├── docs/                      # Documentation content
│   ├── index.md              # Homepage
│   ├── assets/               # Static assets
│   │   ├── css/              # Custom CSS
│   │   ├── js/               # Custom JavaScript
│   │   ├── images/           # Images
│   │   └── fonts/            # Custom fonts
│   └── website/              # This documentation
├── overrides/                 # Theme overrides
│   └── partials/             # Template overrides
└── tests/                    # Validation scripts
```

## Validation

Use these commands to validate configuration:

```bash
# Validate YAML syntax
just validate-yaml

# Validate MkDocs configuration
just validate-config

# Run all validations
just validate

# Test build
just build --strict
```

## Common Customizations

### Custom Colors

In `docs/assets/css/druids-theme.css`:

```css
:root {
  --md-primary-fg-color: #your-color;
  --md-accent-fg-color: #your-accent;
}
```

### Custom Fonts

```css
:root {
  --md-text-font: "Your Font", sans-serif;
  --md-code-font: "Your Code Font", monospace;
}
```

### Navigation Structure

```yaml
nav:
  - Home: index.md
  - Documentation:
      - Getting Started: getting-started.md
      - User Guide: user-guide.md
  - API Reference: api.md
  - Blog: blog/index.md
```

## Best Practices

1. **Use environment variables** for sensitive data
2. **Enable strict mode** for production builds
3. **Validate configuration** before deploying
4. **Test locally** with `mkdocs serve`
5. **Keep plugins minimal** for performance
6. **Document customizations** for maintainability

## Troubleshooting

See the [Validation Guide](../../implement/mkdocs/website-validations.md) for common issues and solutions.