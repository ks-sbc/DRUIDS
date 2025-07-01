---
title: Reference
description: Complete reference documentation
icon: material/book-open-variant
---

# Reference Documentation

Complete reference documentation for all features, configurations, and APIs.

## Configuration Reference

### 🔧 **MkDocs Configuration**
- **Site Settings** - Basic site configuration options
- **Theme Configuration** - Material theme settings
- **Plugin Configuration** - Available plugins and their options
- **Extension Configuration** - Markdown extensions and settings

### 🎨 **Theme Reference**
- **Color Schemes** - Available colors and customization
- **Typography** - Font configuration and styling
- **Icons** - Icon sets and usage
- **Features** - Complete feature list and descriptions

### 📝 **Content Reference**
- **Markdown Syntax** - Supported Markdown features
- **Front Matter** - Page metadata options
- **Admonitions** - Available admonition types
- **Code Blocks** - Syntax highlighting and features

## Feature Reference

### 🧭 **Navigation**
- **Navigation Features** - Complete list of navigation options
- **Tab Configuration** - Setting up navigation tabs
- **Section Indexes** - Creating section landing pages
- **Breadcrumbs** - Navigation breadcrumb configuration

### 🔍 **Search**
- **Search Configuration** - Search plugin options
- **Search Boosting** - Improving search relevance
- **Search Exclusions** - Excluding content from search
- **Custom Search** - Advanced search customization

### 📱 **Social Features**
- **Social Cards** - Automatic social media card generation
- **Social Links** - Social media integration
- **Comments** - Comment system configuration
- **Sharing** - Content sharing options

## API Reference

### 🔌 **Plugin APIs**
- **Blog Plugin** - Blog functionality API
- **Search Plugin** - Search customization API
- **Social Plugin** - Social card generation API
- **Tags Plugin** - Tagging system API

### 🎯 **Hook APIs**
- **Template Hooks** - Available template hooks
- **Build Hooks** - Build process customization
- **Event Hooks** - Event-driven customization
- **Filter Hooks** - Content filtering and processing

### 🛠️ **Extension APIs**
- **Custom Extensions** - Creating custom Markdown extensions
- **Preprocessors** - Content preprocessing
- **Postprocessors** - Content postprocessing
- **Tree Processors** - AST manipulation

## Command Reference

### 📦 **MkDocs Commands**
```bash
# Basic commands
mkdocs serve          # Start development server
mkdocs build          # Build static site
mkdocs new            # Create new project
mkdocs --help         # Show help

# Advanced commands
mkdocs serve --dev-addr 0.0.0.0:8000  # Custom address
mkdocs build --clean                   # Clean build
mkdocs build --strict                  # Strict mode
```

### 🚀 **Mike Commands (Versioning)**
```bash
# Version management
mike deploy <version> [title]    # Deploy version
mike list                        # List versions
mike alias <version> <alias>     # Create alias
mike set-default <version>       # Set default
mike delete <version>            # Delete version
mike serve                       # Serve all versions
```

### 🎨 **Development Commands**
```bash
# Testing and validation
mkdocs build --strict           # Strict validation
mkdocs serve --livereload       # Live reload
python -m mkdocs serve          # Alternative serve

# Plugin development
pip install -e .                # Install in development mode
mkdocs build --verbose          # Verbose output
```

## Configuration Examples

### 📋 **Complete mkdocs.yml**
```yaml
site_name: My Documentation
site_description: Comprehensive documentation site
site_author: Your Name
site_url: https://yourdomain.com

theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - navigation.instant
    - search.highlight
    - search.share
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode

plugins:
  - material/search
  - material/social
  - material/tags
  - blog

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - attr_list
  - md_in_html

extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/yourusername
  analytics:
    provider: google
    property: G-XXXXXXXXXX
```

### 🎯 **Page Front Matter**
```yaml
---
title: Page Title
description: Page description for SEO
tags:
  - tag1
  - tag2
comments: true
search:
  boost: 2
  exclude: false
hide:
  - navigation
  - toc
---
```

### 🏷️ **Blog Post Front Matter**
```yaml
---
date: 2024-01-15
authors:
  - author1
  - author2
categories:
  - Category 1
  - Category 2
tags:
  - tag1
  - tag2
comments: true
readtime: 5
---
```

## Troubleshooting Reference

### ❗ **Common Issues**
- **Build Errors** - Common build problems and solutions
- **Plugin Conflicts** - Resolving plugin compatibility issues
- **Theme Issues** - Theme-related problems
- **Performance Issues** - Optimization and performance tuning

### 🔧 **Debug Commands**
```bash
# Debugging
mkdocs build --verbose          # Verbose output
mkdocs serve --dev-addr 127.0.0.1:8000 --livereload
python -c "import mkdocs; print(mkdocs.__version__)"

# Validation
mkdocs build --strict           # Strict validation
mkdocs config-check             # Check configuration
```

### 📊 **Performance Monitoring**
- **Build Times** - Monitoring and optimizing build performance
- **Bundle Size** - Analyzing and reducing bundle size
- **Loading Speed** - Optimizing page load times
- **Search Performance** - Search optimization techniques

## Version Compatibility

### 📅 **Version Matrix**
| Feature | MkDocs | Material | Python |
|---------|--------|----------|--------|
| Basic Features | 1.4+ | 8.0+ | 3.8+ |
| Advanced Search | 1.5+ | 9.0+ | 3.9+ |
| Social Cards | 1.5+ | 9.1+ | 3.9+ |
| Blog Plugin | 1.5+ | 9.2+ | 3.9+ |

### 🔄 **Migration Guides**
- **MkDocs 1.4 → 1.5** - Breaking changes and migration steps
- **Material 8.x → 9.x** - Theme migration guide
- **Plugin Updates** - Plugin-specific migration guides

---

*This reference documentation is continuously updated. Bookmark this page for quick access to all configuration options and features.*