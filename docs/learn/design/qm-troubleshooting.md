---
title: "Queer Mandalorian Theme Troubleshooting"
description: "Common issues and solutions when implementing the Queer Mandalorian theme"
created: 2025-07-01
updated: 2025-07-01
type: "docs/reference"
security: "L0"
version: "1.0.0"
document_id: "INT-REF-2025-354-L0"
tags: ["troubleshooting", "debugging", "queer-mandalorian", "css", "fixes"]
draft: false
author: ["Comrade 191"]
---

# Queer Mandalorian Theme Troubleshooting

## Overview

This guide addresses common issues encountered when implementing the Queer Mandalorian theme and provides tested solutions based on real-world implementations.

## Common CSS Issues

### Green-on-Green Contrast Problems

**Symptom**: Poor readability when similar colors overlap, especially in code blocks or highlighted sections.

**Solution**:
```css
/* Use complementary colors instead */
.highlight {
  background: rgba(10, 22, 40, 0.3); /* Dark transparent */
  color: var(--qm-cyan);             /* Bright cyan text */
}

/* Avoid */
.bad-example {
  background: #00FF41;
  color: #00D9FF; /* Too similar in brightness */
}
```

**Best Practice**: Always test color combinations with a contrast checker.

### Rounded Corners Persisting

**Symptom**: Material Design's rounded corners appear despite overrides.

**Root Cause**: CSS specificity issues or late-loading Material styles.

**Solution**:
```css
/* Force sharp edges with high specificity */
.md-typeset *,
.md-nav *,
.md-header * {
  border-radius: 0 !important;
}

/* Allow specific exceptions */
.md-tag,
.pill,
.badge {
  border-radius: 4px !important;
}
```

### Excessive Negative Space

**Symptom**: Large padding makes content feel disconnected and wastes screen space.

**Solution**:
```css
/* Tighten spacing */
.md-typeset {
  line-height: 1.75; /* Instead of 2+ */
}

.md-content__inner {
  padding: 1rem 2rem; /* Reduced from defaults */
}

/* Increase font sizes proportionally */
.md-typeset {
  font-size: 1.1875rem; /* 19px base */
}
```

### Icon Contrast in Dark Theme

**Symptom**: Dark icons disappear on dark backgrounds.

**Solution**:
```css
/* Add glow effects for visibility */
.md-icon {
  filter: drop-shadow(0 0 2px var(--qm-cyan));
}

/* Or use bright colors */
.icon-class {
  color: var(--qm-primary-orange);
  opacity: 0.9;
}
```

### Code Highlighting Too Harsh

**Symptom**: Solid background colors in code blocks are jarring.

**Solution**:
```css
/* Use transparent gradients */
.highlight {
  background: linear-gradient(
    90deg,
    rgba(10, 22, 40, 0.3) 0%,
    rgba(10, 22, 40, 0.2) 100%
  );
}

/* Syntax colors with reduced opacity */
.highlight .k { /* Keywords */
  color: rgba(255, 107, 53, 0.9);
}
```

## Navigation Issues

### Orange Navigation Bar Text Visibility

**Symptom**: White text on orange background is unreadable.

**Solution**:
```css
.md-tabs__link {
  color: #2C3E50 !important; /* Dark gray instead of white */
}

.md-tabs__link:hover {
  color: var(--qm-cyan) !important;
}
```

### Active Navigation State Not Clear

**Symptom**: Users can't tell which page they're on.

**Solution**:
```css
.md-nav__link--active {
  color: var(--qm-primary-orange);
  font-weight: 700;
  position: relative;
}

.md-nav__link--active::before {
  content: "▶";
  position: absolute;
  left: -1.5rem;
  color: var(--qm-magenta-glow);
}
```

## Component-Specific Issues

### Mermaid Diagrams Background

**Symptom**: Mermaid diagrams have white backgrounds that clash with dark theme.

**Solution**:
```css
.mermaid {
  background: transparent !important;
}

.mermaid * {
  fill: var(--qm-text-primary) !important;
  stroke: var(--qm-cyan) !important;
}
```

### Table Readability

**Symptom**: Tables blend into background or have poor contrast.

**Solution**:
```css
.md-typeset table {
  border: 1px solid var(--qm-cyan);
}

.md-typeset table th {
  background: var(--qm-dark-blue);
  color: var(--qm-primary-orange);
  font-weight: 700;
}

.md-typeset table tr:hover {
  background: rgba(0, 217, 255, 0.1);
}
```

### Security Indicators Overlapping

**Symptom**: Security level badges overlap with content.

**Solution**:
```css
.security-l0,
.security-l1,
.security-l2 {
  position: relative;
  padding-right: 8rem; /* Space for badge */
}

.security-l2::before {
  position: absolute;
  right: 0.5rem;
  top: 0.5rem;
}
```

## Performance Issues

### Glitch Effects Causing Lag

**Symptom**: Page stutters when hovering over headers.

**Solution**:
```css
/* Use GPU acceleration */
@keyframes glitch {
  0% { transform: translate3d(0, 0, 0); }
  /* ... */
}

/* Reduce animation frequency */
h1:hover {
  animation: glitch 0.3s ease-in-out;
  animation-iteration-count: 1; /* Run once */
}
```

### Large CSS File Size

**Symptom**: Theme CSS is too large, causing slow loads.

**Solution**:
1. Split CSS into component files
2. Use CSS custom properties to reduce repetition
3. Minify production CSS
4. Remove unused styles

## Browser-Specific Issues

### Firefox Gradient Rendering

**Symptom**: Gradients appear banded in Firefox.

**Solution**:
```css
/* Add more color stops */
background: linear-gradient(
  90deg,
  rgba(255, 107, 53, 0.1) 0%,
  rgba(255, 107, 53, 0.08) 25%,
  rgba(255, 107, 53, 0.05) 50%,
  rgba(255, 107, 53, 0.02) 75%,
  transparent 100%
);
```

### Safari Focus Outline

**Symptom**: Focus outlines don't appear in Safari.

**Solution**:
```css
/* Force webkit focus */
*:focus {
  outline: 2px solid var(--qm-cyan) !important;
  outline-offset: 2px !important;
  -webkit-appearance: none;
}
```

## Mobile Issues

### Touch Targets Too Small

**Symptom**: Links and buttons hard to tap on mobile.

**Solution**:
```css
@media (max-width: 768px) {
  .md-nav__link {
    padding: 1rem; /* Increase from 0.5rem */
    min-height: 44px; /* iOS minimum */
  }
}
```

### Horizontal Scroll

**Symptom**: Page scrolls horizontally on mobile.

**Solution**:
```css
/* Prevent overflow */
body {
  overflow-x: hidden;
}

/* Check for absolute positioned elements */
.problem-element {
  position: relative; /* Change from absolute */
  width: 100%; /* Constrain width */
}
```

## Debug Techniques

### Visual Debugging

Add debug mode to see element boundaries:

```css
.qm-debug * {
  outline: 1px solid magenta !important;
}

.qm-debug *::before,
.qm-debug *::after {
  outline: 1px solid cyan !important;
}
```

### CSS Variable Inspection

Check if variables are loading:

```javascript
// In browser console
getComputedStyle(document.documentElement)
  .getPropertyValue('--qm-primary-orange');
```

### Specificity Calculator

When overrides aren't working:

1. Use browser inspector to see applied styles
2. Check specificity score
3. Increase specificity or use `!important` sparingly

## Testing Checklist

Before deploying, verify:

- [ ] All text meets contrast requirements
- [ ] Navigation states are clear
- [ ] Code blocks are readable
- [ ] Tables have proper borders
- [ ] Security indicators don't overlap
- [ ] Mobile experience is usable
- [ ] Animations respect reduced motion
- [ ] Focus states are visible
- [ ] No horizontal scroll on mobile
- [ ] Page loads under 3 seconds

## Getting Help

If you encounter issues not covered here:

1. Check browser console for CSS errors
2. Validate CSS with online tools
3. Test in multiple browsers
4. Create minimal reproduction
5. Document with screenshots
6. Share in community forums

---

> "Every bug is a learning opportunity. Every fix makes the revolution stronger." - Trans Hacker Collective