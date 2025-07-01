---
title: Customization Guide
description: Complete guide to customizing MkDocs Material theme
tags:
  - customization
  - theming
  - css
  - partials
---

# MkDocs Material Customization Guide

This guide covers all aspects of customizing your MkDocs Material site, from simple color changes to advanced template overrides.

## Color Customization

### Using Built-in Color Schemes

MkDocs Material comes with several built-in color schemes:

```yaml
# mkdocs.yml
theme:
  name: material
  palette:
    # Palette toggle for light mode
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    # Palette toggle for dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
```

### Available Colors

**Primary Colors**: `red`, `pink`, `purple`, `deep purple`, `indigo`, `blue`, `light blue`, `cyan`, `teal`, `green`, `light green`, `lime`, `yellow`, `amber`, `orange`, `deep orange`, `brown`, `grey`, `blue grey`, `black`, `white`

**Accent Colors**: `red`, `pink`, `purple`, `deep purple`, `indigo`, `blue`, `light blue`, `cyan`, `teal`, `green`, `light green`, `lime`, `yellow`, `amber`, `orange`, `deep orange`

### Custom CSS Colors

Create custom colors in `docs/assets/css/extra.css`:

```css
:root {
  /* Custom primary colors */
  --md-primary-fg-color: #2563eb;
  --md-primary-fg-color--light: #3b82f6;
  --md-primary-fg-color--dark: #1d4ed8;

  /* Custom accent colors */
  --md-accent-fg-color: #10b981;
  --md-accent-fg-color--transparent: #10b98110;
}

/* Dark theme overrides */
[data-md-color-scheme="slate"] {
  --md-primary-fg-color: #60a5fa;
  --md-accent-fg-color: #34d399;
}
```

## Typography Customization

### Font Configuration

```yaml
# mkdocs.yml
theme:
  font:
    text: Inter
    code: JetBrains Mono
```

### Custom Fonts

```css
/* Load custom fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
  --md-text-font: "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
  --md-code-font: "JetBrains Mono", "Consolas", monospace;
}
```

### Typography Styles

```css
/* Heading customization */
.md-typeset h1 {
  font-weight: 800;
  color: var(--md-primary-fg-color);
  font-size: 2.5rem;
}

.md-typeset h2 {
  font-weight: 700;
  border-bottom: 2px solid var(--md-accent-fg-color--transparent);
  padding-bottom: 0.5rem;
}

/* Body text */
.md-typeset {
  font-size: 1rem;
  line-height: 1.7;
}

/* Code styling */
.md-typeset code {
  background-color: var(--md-accent-fg-color--transparent);
  color: var(--md-accent-fg-color);
  font-weight: 500;
  padding: 0.2em 0.4em;
  border-radius: 4px;
}
```

## Template Overrides (Partials)

### Directory Structure

```
overrides/
├── partials/
│   ├── header.html          # Custom header
│   ├── footer.html          # Custom footer
│   ├── comments.html        # Comments system
│   ├── content.html         # Main content area
│   ├── nav.html            # Navigation
│   └── toc.html            # Table of contents
├── 404.html                # Custom 404 page
├── base.html               # Base template
└── main.html               # Main template
```

### Custom Header Example

```html
<!-- overrides/partials/header.html -->
{% extends "base.html" %}

{% block header %}
<header class="md-header" data-md-component="header">
  <nav class="md-header__inner md-grid">

    <!-- Custom logo with link -->
    <a href="{{ config.site_url }}" class="md-header__button md-logo">
      <img src="{{ config.theme.logo }}" alt="{{ config.site_name }}">
    </a>

    <!-- Custom navigation -->
    <div class="md-header__title">
      <div class="md-header__ellipsis">
        <span class="md-ellipsis">{{ config.site_name }}</span>
      </div>
    </div>

    <!-- Custom buttons -->
    <div class="md-header__option">
      <a href="/contact" class="md-button md-button--primary">
        Contact Us
      </a>
    </div>

  </nav>
</header>
{% endblock %}
```

### Custom Footer Example

```html
<!-- overrides/partials/footer.html -->
<footer class="md-footer">
  <div class="md-footer-meta md-typeset">
    <div class="md-footer-meta__inner md-grid">

      <!-- Custom footer content -->
      <div class="md-footer-copyright">
        <div class="md-footer-copyright__highlight">
          © 2024 {{ config.site_name }}. All rights reserved.
        </div>

        <!-- Additional links -->
        <div class="md-footer-links">
          <a href="/privacy">Privacy Policy</a> •
          <a href="/terms">Terms of Service</a> •
          <a href="/contact">Contact</a>
        </div>
      </div>

      <!-- Social links -->
      {% if config.extra.social %}
      <div class="md-footer-social">
        {% for social in config.extra.social %}
        <a href="{{ social.link }}" target="_blank" class="md-footer-social__link">
          {% include ".icons/" ~ social.icon ~ ".svg" %}
        </a>
        {% endfor %}
      </div>
      {% endif %}

    </div>
  </div>
</footer>
```

## Advanced CSS Customization

### Component Styling

```css
/* Navigation styling */
.md-nav__title {
  font-weight: 600;
  color: var(--md-primary-fg-color);
}

.md-nav__link--active {
  color: var(--md-accent-fg-color);
  font-weight: 600;
}

/* Search styling */
.md-search__input {
  border-radius: 20px;
  background-color: rgba(255, 255, 255, 0.1);
}

/* Button styling */
.md-button {
  border-radius: 6px;
  font-weight: 600;
  transition: all 0.2s ease;
}

.md-button:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

/* Table styling */
.md-typeset table:not([class]) {
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.md-typeset table:not([class]) th {
  background: linear-gradient(135deg, var(--md-primary-fg-color--light), var(--md-primary-fg-color));
  color: white;
  font-weight: 600;
}
```

### Animations

```css
/* Fade in animation */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.md-content__inner > * {
  animation: fadeInUp 0.6s ease-out;
}

/* Hover effects */
.md-social__link {
  transition: transform 0.2s ease;
}

.md-social__link:hover {
  transform: scale(1.1);
}
```

### Responsive Design

```css
/* Mobile optimizations */
@media screen and (max-width: 76.1875em) {
  .md-content__inner {
    padding: 0 1rem;
  }

  .md-typeset h1 {
    font-size: 1.8rem;
  }

  .md-typeset h2 {
    font-size: 1.4rem;
  }
}

/* Tablet optimizations */
@media screen and (max-width: 60em) {
  .md-nav--primary .md-nav__title {
    display: block;
  }
}
```

## Custom Components

### Utility Classes

```css
/* Custom utility classes */
.text-gradient {
  background: linear-gradient(135deg, var(--md-primary-fg-color), var(--md-accent-fg-color));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.card {
  background: var(--md-default-bg-color);
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border: 1px solid var(--md-default-fg-color--lightest);
  margin: 1rem 0;
}

.highlight-box {
  background: var(--md-accent-fg-color--transparent);
  border-left: 4px solid var(--md-accent-fg-color);
  padding: 1rem;
  border-radius: 0 8px 8px 0;
  margin: 1rem 0;
}
```

### Usage in Markdown

```markdown
<!-- Using custom classes -->
<div class="card">
  <h3 class="text-gradient">Custom Card</h3>
  <p>This is a custom styled card component.</p>
</div>

<div class="highlight-box">
  <strong>Important:</strong> This is a highlighted information box.
</div>
```

## JavaScript Customization

### Custom JavaScript

Create `docs/assets/js/extra.js`:

```javascript
// Custom JavaScript functionality
document.addEventListener('DOMContentLoaded', function() {

  // Add custom behavior to buttons
  const buttons = document.querySelectorAll('.md-button');
  buttons.forEach(button => {
    button.addEventListener('click', function(e) {
      // Add ripple effect
      const ripple = document.createElement('span');
      ripple.classList.add('ripple');
      this.appendChild(ripple);

      setTimeout(() => {
        ripple.remove();
      }, 600);
    });
  });

  // Custom scroll behavior
  window.addEventListener('scroll', function() {
    const header = document.querySelector('.md-header');
    if (window.scrollY > 100) {
      header.classList.add('md-header--scrolled');
    } else {
      header.classList.remove('md-header--scrolled');
    }
  });

});
```

### Include in Configuration

```yaml
# mkdocs.yml
extra_javascript:
  - assets/js/extra.js
```

## Icon Customization

### Using Custom Icons

```yaml
# mkdocs.yml
theme:
  icon:
    logo: material/library
    repo: fontawesome/brands/github
    edit: material/pencil
    view: material/eye
```

### Custom Icon Sets

```html
<!-- In templates -->
{% set icon = "custom/my-icon" %}
{% include ".icons/" ~ icon ~ ".svg" %}
```

## Advanced Features

### Custom Admonitions

```css
/* Custom admonition types */
.md-typeset .admonition.tip {
  border-color: var(--md-accent-fg-color);
}

.md-typeset .admonition.tip > .admonition-title {
  background-color: var(--md-accent-fg-color--transparent);
}

.md-typeset .admonition.tip > .admonition-title::before {
  background-color: var(--md-accent-fg-color);
  mask-image: var(--md-admonition-icon--tip);
}
```

### Custom Search

```javascript
// Custom search behavior
document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.querySelector('.md-search__input');

  if (searchInput) {
    searchInput.addEventListener('input', function(e) {
      // Custom search logic
      console.log('Search query:', e.target.value);
    });
  }
});
```

## Testing Customizations

### Local Development

```bash
# Serve with live reload
mkdocs serve

# Build and check
mkdocs build

# Serve built site
cd site && python -m http.server 8000
```

### Browser Testing

1. **Chrome DevTools** - Inspect elements and test CSS
2. **Responsive Design Mode** - Test mobile layouts
3. **Lighthouse** - Performance and accessibility testing
4. **Cross-browser Testing** - Firefox, Safari, Edge

## Best Practices

### 1. Organization

- Keep custom CSS organized in logical sections
- Use CSS custom properties for consistency
- Comment your customizations

### 2. Performance

- Minimize custom CSS and JavaScript
- Optimize images and fonts
- Use efficient selectors

### 3. Maintainability

- Follow Material Design principles
- Test across different screen sizes
- Document your customizations

### 4. Accessibility

- Maintain proper contrast ratios
- Ensure keyboard navigation works
- Test with screen readers

---

_This customization guide covers the most common scenarios. For advanced use cases, refer to the [MkDocs Material documentation](https://squidfunk.github.io/mkdocs-material/customization/) and [Material Design guidelines](https://material.io/design)._
