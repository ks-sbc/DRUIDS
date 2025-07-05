---
title: "Queer Mandalorian Implementation Guide"
description: "Step-by-step guide for implementing the Queer Mandalorian theme in your DRUIDS documentation"
created: 2025-07-01
updated: 2025-07-01
type: "docs/how-to"
security: "L0"
version: "1.0.0"
document_id: "INT-HTG-2025-351-L0"
tags: ["theme", "implementation", "queer-mandalorian", "css", "mkdocs", "how-to"]
draft: false
author: ["Comrade 191"]
---

# Queer Mandalorian Implementation Guide

## Overview

This guide walks you through implementing the Queer Mandalorian theme in your DRUIDS documentation system. The theme transforms the standard MkDocs Material appearance into a revolutionary cyberpunk guerilla aesthetic.

## Prerequisites

- Working DRUIDS documentation system
- MkDocs Material theme installed
- Basic understanding of CSS
- Access to modify `mkdocs.yml`

## Implementation Steps

### Step 1: Create File Structure

Create the following directory structure in your `docs` folder:

```
docs/
├── stylesheets/
│   ├── qm-overrides.css      # Material theme overrides
│   ├── queer-mandalorian.css # Main theme file
│   ├── qm-syntax.css         # Syntax highlighting
│   └── qm-components.css     # Component styling
```

### Step 2: Update MkDocs Configuration

Add the theme CSS files to your `mkdocs.yml`:

```yaml
# mkdocs.yml
extra_css:
  - stylesheets/qm-overrides.css    # Load first
  - stylesheets/queer-mandalorian.css
  - stylesheets/qm-syntax.css
  - stylesheets/qm-components.css
```

**Important**: Order matters! `qm-overrides.css` must load first to properly override Material defaults.

### Step 3: Critical Overrides

The `qm-overrides.css` file handles Material-specific overrides:

```css
/* Example structure for qm-overrides.css */
/* Navigation overrides */
.md-nav { /* styles */ }

/* Header overrides */
.md-header { /* styles */ }

/* Content overrides */
.md-content { /* styles */ }
```

### Step 4: Component Implementation

#### Navigation Enhancement

The navigation should reflect the cyberpunk aesthetic:

- Uppercase text with letter spacing
- Cyan hover effects with translateX animation
- Orange active states with arrow indicators
- Sharp edges (no border radius)

#### Code Block Styling

Terminal-inspired code blocks require:

- Transparent backgrounds with cyan borders
- Terminal prompt ($) prefixes
- Monospace fonts (JetBrains Mono preferred)
- Syntax highlighting in theme colors

#### Security Indicators

Implement three-tier visual security:

- L0 (Public): Green with gradient background
- L1 (Member): Orange with gradient background  
- L2 (Cadre): Pink/Red with warning icon

### Step 5: Typography Configuration

Configure the typography system:

1. **Headers**: Impact or Arial Black, uppercase
2. **Body**: Inter or system fonts, 19px base
3. **Code**: JetBrains Mono or Fira Code
4. **Line Height**: 1.75 for readability

### Step 6: Color Implementation

Apply the Dark Pride color palette consistently:

```
Primary Orange: #FF6B35 (inverted blue)
Rust: #B84A14 (H1 headers)
Cyan: #00D9FF (bright accents)
Dark Blue: #0A1628 (backgrounds)
Purple: #BD10E0 (accents)
Pink: #FF006E (warnings)
Teal: #00CFC1 (inverted pink)
Magenta: #FF00FF (glitch effects)
```

### Step 7: Testing

#### Create Test Pages

Create comprehensive test pages:

```markdown
# docs/test-qm-all.md
---
title: "Queer Mandalorian Theme Test"
---

## Typography Test
[Include all heading levels, paragraphs, lists]

## Component Test  
[Security indicators, code blocks, tables]

## Color Test
[All color combinations for contrast]
```

#### Accessibility Testing

1. Run contrast checker on all color combinations
2. Test with screen readers
3. Verify keyboard navigation
4. Check reduced motion preferences

#### Browser Testing

Test in:
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers

### Step 8: Performance Optimization

1. **Minimize Animations**: Keep glitch effects subtle
2. **Optimize Fonts**: Use system fonts as fallbacks
3. **Reduce Repaints**: Use transforms over position changes
4. **Lazy Load**: Heavy effects only on interaction

### Step 9: Documentation

Document your implementation:

1. Color choices and rationale
2. Component modifications
3. Accessibility decisions
4. Browser-specific fixes

## Common Pitfalls

### 1. Green-on-Green Contrast

**Problem**: Poor readability with similar colors
**Solution**: Always use complementary colors (orange/blue, purple/yellow)

### 2. Excessive Border Radius

**Problem**: Material's rounded corners persist
**Solution**: Use `!important` sparingly but effectively:

```css
* { border-radius: 0 !important; }
/* Allow specific exceptions */
.pill { border-radius: 4px !important; }
```

### 3. Code Block Readability

**Problem**: Solid backgrounds too harsh
**Solution**: Use transparent backgrounds (0.2-0.3 opacity)

### 4. Navigation Hover States

**Problem**: Hover effects not visible
**Solution**: Combine color change with transform

## Integration Checklist

- [ ] File structure created
- [ ] CSS files added to mkdocs.yml
- [ ] Color variables defined
- [ ] Typography configured
- [ ] Navigation styled
- [ ] Code blocks themed
- [ ] Security indicators implemented
- [ ] Tables styled
- [ ] Accessibility tested
- [ ] Browser compatibility verified
- [ ] Performance optimized
- [ ] Documentation complete

## Debugging

### Debug Mode

Add debug class for development:

```css
.qm-debug * {
  outline: 1px solid magenta !important;
}
```

### Common Issues

1. **Styles not applying**: Check CSS file load order
2. **Colors incorrect**: Verify CSS variable definitions
3. **Animations janky**: Check GPU acceleration
4. **Mobile issues**: Test responsive breakpoints

## Maintenance

### Updating the Theme

When updating:

1. Test changes in isolation
2. Document what changed and why
3. Update test pages
4. Re-run accessibility tests
5. Notify team of changes

### Version Control

Track theme versions:

```css
/* queer-mandalorian.css v1.0.0 */
/* Last updated: 2025-07-01 */
/* Author: Trans Hacker Collective */
```

## Resources

- [CSS Architecture Best Practices](https://example.com)
- [MkDocs Material Customization](https://squidfunk.github.io/mkdocs-material/customization/)
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Trans Pride Flag Colors](https://example.com)

---

> "Code is poetry, rebellion is art, and our theme is both." - Queer Mandalorian Collective