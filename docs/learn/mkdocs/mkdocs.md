---
title: MkDocs Configuration Guide
description: Complete guide to our MkDocs setup and configuration
tags:
  - mkdocs
  - configuration
  - setup
---

# MkDocs Configuration Guide

This guide explains our MkDocs setup, configuration, and how to use it effectively.

## Overview

Our documentation uses **MkDocs Material** - a powerful, feature-rich theme that provides:
- Modern, responsive design
- Advanced navigation features
- Built-in search functionality
- Extensive customization options

## Project Structure

```
mkdocs/
├── mkdocs.yml           # Main configuration file
├── docs/                # Documentation content
│   ├── index.md        # Homepage
│   ├── assets/         # CSS, JS, images
│   └── website/        # This documentation
├── overrides/          # Theme customizations
├── dependencies/
│   ├── requirements.txt  # Python dependencies
│   └── package.json     # Node.js dependencies
├── config/
│   ├── pyproject.toml   # Python tooling config
│   └── .prettierrc.json # Code formatting config
├── justfile           # Task automation
└── tests/             # Validation scripts
```

## Key Configuration (mkdocs.yml)

Our MkDocs configuration includes:

### Site Information
```yaml
site_name: DRUIDS Wiki
site_description: Democratic Revolutionary Unified Information & Documentation System
site_url: https://druids.kssocialistbookclub.com
repo_url: https://github.com/ks-sbc/DRUIDS
```

### Theme Configuration
- **Theme**: Material with custom overrides
- **Color Scheme**: Dark mode with custom colors
- **Features**: 20+ enabled features for enhanced UX

### Plugins
- **Search**: Built-in search functionality
- **Obsidian**: Wikilinks and Obsidian compatibility
- **Git Revision Date**: Shows last update times
- **Tags**: Content tagging system

## Quick Start Commands

Using our `justfile` task runner:

```bash
# Install dependencies
just init

# Start development server
just serve

# Run validation checks
just validate

# Build site
just build

# Deploy to GitHub Pages
just deploy
```

## Working with Content

### Creating Pages

1. **Add Markdown files** to the `docs/` directory
2. **Use YAML frontmatter** for metadata
3. **Link pages** using standard Markdown or wikilinks
4. **Organize content** in logical folders

### Markdown Features

Our setup supports all standard Markdown plus:
- **Admonitions** for callout boxes
- **Code blocks** with syntax highlighting
- **Tables** with advanced formatting
- **Task lists** for checklists
- **Footnotes** for references
- **Abbreviations** with tooltips

See the [Features Demo](../../test-features.md) for examples.

## Development Workflow

### 1. Local Development
```bash
# Start dev server with live reload
just serve

# Open http://localhost:8000
```

### 2. Making Changes
- Edit Markdown files in `docs/`
- Modify CSS in `docs/assets/css/`
- Override templates in `overrides/`

### 3. Validation
```bash
# Run all checks before committing
just validate

# Specific validations
just validate-yaml
just validate-blog
```

### 4. Building
```bash
# Build site
just build

# Build and serve locally
just build-serve
```

## Features Overview

### Navigation System
- Instant loading with prefetch
- Sticky navigation tabs
- Collapsible sections
- Breadcrumb navigation
- Table of contents integration

See [Navigation Guide](../../implement/mkdocs/configuration-reference.md) for setup details.

### Customization
- Custom color schemes
- Typography settings
- Component styling
- Template overrides

<!-- See [Customization Guide](customization-guide.md) for details. -->

### Advanced Features
- **Giscus Comments** - GitHub Discussions integration
- **Offline Support** - PWA functionality
- **Versioning** - Multi-version documentation
- **Search** - Built-in full-text search

## Best Practices

### Content Organization
- Use clear, descriptive filenames
- Group related content in folders
- Create index pages for sections
- Maintain consistent navigation structure

### Writing Guidelines
- Write clear, concise content
- Use headings for structure
- Include code examples
- Add visual elements (diagrams, screenshots)

### Performance
- Optimize images before adding
- Use lazy loading for large assets
- Enable caching for static content
- Monitor build times

## Troubleshooting

Common issues and solutions:

### Build Errors
- Check YAML syntax in frontmatter
- Validate Markdown formatting
- Ensure all linked files exist
- Review plugin configurations

### Styling Issues
- Clear browser cache
- Check CSS file paths
- Verify theme overrides
- Test in multiple browsers

See [Validation Guide](../../implement/mkdocs/website-validations.md) for comprehensive testing.

## Next Steps

1. Review the [Test Features](../../test-features.md)
2. Customize using the [CSS Aesthetic Reference](../../implement/mkdocs/css.md)
3. Set up [Giscus Comments](../../implement/mkdocs/setup-giscus.md)
4. Enable [Offline Support](../../implement/mkdocs/offline-usage-guide.md)

For questions, check our validation system or file an issue on GitHub.
