---
title: Navigation Setup Guide
description: Complete guide to setting up navigation in MkDocs Material
tags:
  - navigation
  - setup
  - configuration
comments: true
---

# Navigation Setup Guide

Learn how to create intuitive, powerful navigation for your MkDocs Material site.

## Navigation Features

### Basic Navigation Features

```yaml
theme:
  features:
    # Core navigation
    - navigation.instant      # Instant loading
    - navigation.tracking     # Anchor tracking
    - navigation.tabs         # Top-level tabs
    - navigation.sections     # Section grouping
    - navigation.expand       # Expand all sections

    # Advanced features
    - navigation.path         # Show path in header
    - navigation.indexes      # Section index pages
    - navigation.top          # Back to top button
    - navigation.footer       # Previous/next links
```

### Instant Loading

Makes your site feel like a single-page application:

```yaml
theme:
  features:
    - navigation.instant
    - navigation.instant.prefetch  # Prefetch on hover
    - navigation.instant.progress  # Show progress bar
```

**Benefits:**

- ⚡ Faster page transitions
- 🔄 Preserves scroll position
- 📱 Better mobile experience
- 🎯 Improved user engagement

### Navigation Tabs

Perfect for organizing large sites:

```yaml
theme:
  features:
    - navigation.tabs
    - navigation.tabs.sticky  # Tabs stay visible when scrolling
```

**Example structure:**

```yaml
nav:
  - Home: index.md
  - Getting Started: getting-started.md
  - Documentation:
      - Overview: docs/index.md
      - Tutorials: docs/tutorials/
  - Blog: blog/index.md
```

### Section Indexes

Create landing pages for sections:

```yaml
theme:
  features:
    - navigation.indexes
```

**File structure:**

```
docs/
├── tutorials/
│   ├── index.md          # Section landing page
│   ├── basic-setup.md
│   └── advanced-config.md
└── reference/
    ├── index.md          # Section landing page
    ├── api.md
    └── configuration.md
```

**Navigation config:**

```yaml
nav:
  - Tutorials:
      - tutorials/index.md    # This becomes the section index
      - Basic Setup: tutorials/basic-setup.md
      - Advanced: tutorials/advanced-config.md
```

## Advanced Navigation

### Navigation Path

Shows the current page path in the header:

```yaml
theme:
  features:
    - navigation.path
```

### Navigation Pruning

Hide navigation for large sites:

```yaml
theme:
  features:
    - navigation.prune  # Hide navigation items not related to current page
```

### Navigation Expansion

Control section expansion:

```yaml
theme:
  features:
    - navigation.expand  # Expand all sections by default
```

## Table of Contents

### TOC Features

```yaml
theme:
  features:
    - toc.follow    # Highlight current section
    - toc.integrate # Integrate TOC into navigation
```

### TOC Configuration

```yaml
markdown_extensions:
  - toc:
      permalink: true
      title: "On this page"
      toc_depth: 3
      baselevel: 1
      separator: "-"
```

## Navigation Structure Examples

### Simple Site

```yaml
nav:
  - Home: index.md
  - About: about.md
  - Contact: contact.md
```

### Documentation Site

```yaml
nav:
  - Home: index.md
  - Getting Started:
      - Installation: getting-started/installation.md
      - Quick Start: getting-started/quick-start.md
      - Configuration: getting-started/configuration.md

  - User Guide:
      - user-guide/index.md
      - Basic Usage: user-guide/basic-usage.md
      - Advanced Features: user-guide/advanced.md

  - API Reference:
      - api/index.md
      - Authentication: api/auth.md
      - Endpoints: api/endpoints.md

  - Blog: blog/index.md
```

### Complex Site with Tabs

```yaml
nav:
  - Home: index.md

  - Documentation:
      - docs/index.md
      - Getting Started:
          - Installation: docs/installation.md
          - Configuration: docs/configuration.md
      - User Guide:
          - docs/user-guide/index.md
          - Basics: docs/user-guide/basics.md
          - Advanced: docs/user-guide/advanced.md
      - API Reference:
          - docs/api/index.md
          - REST API: docs/api/rest.md
          - GraphQL: docs/api/graphql.md

  - Tutorials:
      - tutorials/index.md
      - Beginner:
          - First Steps: tutorials/beginner/first-steps.md
          - Basic Concepts: tutorials/beginner/concepts.md
      - Advanced:
          - Custom Plugins: tutorials/advanced/plugins.md
          - Performance: tutorials/advanced/performance.md

  - Community:
      - Blog: blog/index.md
      - Contributing: community/contributing.md
      - Support: community/support.md
```

## Navigation Customization

### Custom Navigation Icons

```yaml
theme:
  icon:
    logo: material/library
    repo: fontawesome/brands/github
    edit: material/pencil
    view: material/eye
```

### Hide Navigation Elements

Hide navigation on specific pages:

```yaml
# In page front matter
---
hide:
  - navigation
  - toc
---
```

### Custom Navigation CSS

```css
/* Custom navigation styling */
.md-nav__title {
  font-weight: 600;
  color: var(--md-primary-fg-color);
}

.md-nav__link--active {
  color: var(--md-accent-fg-color);
  font-weight: 600;
}

/* Custom tab styling */
.md-tabs__item {
  height: 48px;
}

.md-tabs__link {
  font-weight: 500;
  opacity: 0.7;
}

.md-tabs__link--active {
  opacity: 1;
  color: var(--md-accent-fg-color);
}
```

## Search Integration

### Enhanced Search

```yaml
plugins:
  - material/search:
      separator: '[\s\u200b\-_,:!=\[\]()"`/]+|\.(?!\d)|&[lg]t;|(?!\b)(?=[A-Z][a-z])'
      lang: en
      pipeline:
        - stemmer
        - stopWordFilter
        - trimmer
```

### Search Features

```yaml
theme:
  features:
    - search.highlight  # Highlight search terms
    - search.share     # Share search results
    - search.suggest   # Search suggestions
```

## Mobile Navigation

### Mobile-Specific Features

The navigation automatically adapts to mobile devices with:

- 📱 **Collapsible sidebar** - Swipe or tap to open/close
- 🔍 **Mobile search** - Optimized search interface
- 👆 **Touch-friendly** - Large touch targets
- ⚡ **Fast transitions** - Smooth animations

### Mobile Customization

```css
/* Mobile navigation customization */
@media screen and (max-width: 76.1875em) {
  .md-nav--primary .md-nav__title {
    background-color: var(--md-primary-fg-color);
    color: white;
  }

  .md-nav__source {
    background-color: var(--md-primary-fg-color--dark);
  }
}
```

## Accessibility

### Keyboard Navigation

- **Tab** - Navigate through links
- **Enter** - Activate links
- **Escape** - Close mobile navigation
- **Arrow keys** - Navigate search results

### Screen Reader Support

```yaml
# Automatic ARIA labels and roles
theme:
  features:
    - navigation.instant  # Announces page changes
```

### Custom ARIA Labels

```html
<!-- In custom templates -->
<nav aria-label="Main navigation">
  <!-- Navigation content -->
</nav>
```

## Performance Optimization

### Navigation Performance

```yaml
theme:
  features:
    - navigation.instant.prefetch  # Prefetch on hover
    - navigation.prune            # Reduce DOM size
```

### Lazy Loading

```yaml
# Only load navigation sections when needed
theme:
  features:
    - navigation.sections
    - navigation.expand
```

## Best Practices

### 1. **Logical Hierarchy**

- Use clear, descriptive section names
- Limit nesting to 3-4 levels maximum
- Group related content together

### 2. **Consistent Structure**

- Use consistent naming conventions
- Maintain parallel structure across sections
- Include index pages for major sections

### 3. **User-Friendly Labels**

- Use action-oriented labels ("Getting Started" vs "Introduction")
- Avoid technical jargon in navigation
- Keep labels concise but descriptive

### 4. **Mobile Considerations**

- Test navigation on mobile devices
- Ensure touch targets are large enough
- Consider navigation depth on small screens

### 5. **Performance**

- Use navigation.prune for large sites
- Enable instant loading for better UX
- Optimize navigation structure for search

## Troubleshooting

### Common Issues

**Navigation not showing:**

```yaml
# Check that navigation is properly configured
nav:
  - Home: index.md  # Must have at least one item
```

**Tabs not appearing:**

```yaml
# Ensure you have top-level sections
nav:
  - Section 1: page1.md
  - Section 2: page2.md  # Need multiple top-level items
```

**Mobile navigation issues:**

```css
/* Ensure proper mobile styles */
@media screen and (max-width: 76.1875em) {
  .md-nav--primary {
    /* Mobile navigation styles */
  }
}
```

### Debug Navigation

```bash
# Check navigation structure
mkdocs build --verbose

# Validate configuration
mkdocs config-check
```

---

_A well-designed navigation system is crucial for user experience. Take time to plan your information architecture before implementing._
