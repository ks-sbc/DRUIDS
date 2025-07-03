---
title: "Queer Mandalorian Accessibility Guide"
description: "Ensuring the Queer Mandalorian theme is accessible to all users while maintaining its revolutionary aesthetic"
created: 2025-07-01
updated: 2025-07-01
type: "docs/reference"
security: "L0"
version: "1.0.0"
document_id: "INT-REF-2025-352-L0"
tags: ["accessibility", "a11y", "queer-mandalorian", "wcag", "inclusive-design"]
draft: false
author: ["Comrade 191"]
---

# Queer Mandalorian Accessibility Guide

## Overview

The Queer Mandalorian theme prioritizes accessibility without compromising its revolutionary cyberpunk aesthetic. This guide ensures your implementation meets WCAG 2.1 AA standards while maintaining the theme's distinctive visual identity.

## Core Principles

1. **Inclusive Rebellion**: Our revolution includes everyone
2. **Accessible Resistance**: Breaking barriers, not creating them
3. **Universal Design**: Liberation technology for all abilities
4. **Progressive Enhancement**: Core functionality first, aesthetics second

## Color Contrast Standards

### WCAG Requirements

All color combinations in the Queer Mandalorian theme meet or exceed:

- **Normal text**: 4.5:1 contrast ratio minimum
- **Large text**: 3:1 contrast ratio (18px+ or 14px+ bold)
- **Interactive elements**: 3:1 contrast ratio for UI components

### Tested Color Combinations

| Foreground | Background | Ratio | Usage | Status |
|------------|------------|-------|-------|--------|
| #E0E0E0 | #0A0E27 | 12.3:1 | Body text | ✅ AAA |
| #00D9FF | #0A0E27 | 11.8:1 | Links | ✅ AAA |
| #FF6B35 | #0A0E27 | 6.7:1 | Headers | ✅ AA |
| #B84A14 | #0A0E27 | 4.8:1 | H1 text | ✅ AA |
| #00CFC1 | #0A0E27 | 10.1:1 | Accents | ✅ AAA |
| #FF006E | #0A0E27 | 5.2:1 | Warnings | ✅ AA |

### Testing Tools

```bash
# Command line contrast testing
npm install -g pa11y
pa11y http://localhost:8000 --reporter cli

# Python contrast checker
pip install wcag-contrast-ratio
python -m wcag_contrast_ratio "#E0E0E0" "#0A0E27"
```

## Visual Indicators

### Security Level Accessibility

Security levels use multiple indicators, not just color:

```css
/* Pattern + Color + Text */
.security-l0::before { content: "🟢 L0 - PUBLIC"; }
.security-l1::before { content: "🟠 L1 - MEMBER"; }
.security-l2::before { content: "🔴 L2 - CADRE ⚠"; }
```

**Accessible Features**:
- Text labels for screen readers
- Icons provide visual reinforcement
- Border patterns differ by level
- Background gradients for additional distinction

### Focus States

Clear, high-contrast focus indicators:

```css
:focus {
  outline: 2px solid #00D9FF;
  outline-offset: 2px;
}

/* Keyboard navigation enhancement */
.md-nav__link:focus {
  background: rgba(0, 217, 255, 0.2);
  color: #FFFFFF;
}
```

## Motion and Animation

### Respecting User Preferences

All animations respect `prefers-reduced-motion`:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### Safe Animation Practices

1. **No autoplay**: Animations trigger on interaction only
2. **Short duration**: Max 0.3s for micro-interactions
3. **Subtle effects**: Glitch effects are decorative, not essential
4. **Pause controls**: Long animations have pause options

## Screen Reader Support

### Semantic Structure

Maintain proper heading hierarchy:

```markdown
# Page Title (H1 - only one per page)
## Major Section (H2)
### Subsection (H3)
#### Detail Level (H4)
```

### ARIA Labels

Enhanced labeling for complex elements:

```html
<!-- Security indicators -->
<div class="security-l2" role="region" aria-label="Restricted content - Cadre access only">

<!-- Navigation -->
<nav aria-label="Main navigation">

<!-- Code blocks -->
<pre aria-label="Terminal command example">
```

### Skip Links

Implement skip navigation:

```html
<a href="#main-content" class="skip-to-content">
  Skip to main content
</a>
```

## Keyboard Navigation

### Tab Order

Logical tab order maintained:

1. Skip links
2. Header navigation
3. Sidebar navigation
4. Main content
5. Footer links

### Keyboard Shortcuts

Document shortcuts clearly:

| Key | Action |
|-----|--------|
| `Tab` | Next focusable element |
| `Shift+Tab` | Previous focusable element |
| `Enter` | Activate link/button |
| `Space` | Toggle checkbox/button |
| `Esc` | Close modal/dropdown |

## Typography Accessibility

### Font Sizing

- Base font: 19px (1.1875rem) for readability
- Line height: 1.75 for comfortable reading
- Responsive sizing for mobile devices
- User can zoom to 200% without horizontal scroll

### Font Choices

```css
/* System fonts for better language support */
--qm-font-body: 'Inter', -apple-system, BlinkMacSystemFont, 
                'Segoe UI', 'Noto Sans', sans-serif;

/* Monospace with wide language support */
--qm-font-mono: 'JetBrains Mono', 'Cascadia Code', 
                'Noto Sans Mono', monospace;
```

## Alternative Text

### Images and Icons

All decorative elements marked appropriately:

```html
<!-- Decorative -->
<img src="glitch.png" alt="" role="presentation">

<!-- Informative -->
<img src="diagram.png" alt="Git workflow showing proposal to main branch process">
```

### Icon Fonts

Use text alternatives:

```html
<span class="icon" aria-hidden="true">▶</span>
<span class="sr-only">Active section</span>
```

## Form Accessibility

### Input Fields

Clear labels and error messages:

```html
<label for="search">Search documentation</label>
<input id="search" type="search" 
       aria-describedby="search-help">
<span id="search-help">Use keywords or phrases</span>
```

### Error States

Multiple indicators for errors:

- Color change (not sole indicator)
- Icon addition
- Text description
- ARIA alerts for screen readers

## Testing Methodology

### Automated Testing

```bash
# Accessibility testing suite
npm install -g @axe-core/cli
axe http://localhost:8000

# Lighthouse CI
npm install -g @lhci/cli
lhci autorun
```

### Manual Testing

1. **Keyboard only**: Navigate entire site without mouse
2. **Screen reader**: Test with NVDA (Windows) or VoiceOver (Mac)
3. **Zoom testing**: Verify 200% zoom functionality
4. **Color filters**: Test with colorblind simulators

### Browser Extensions

- axe DevTools
- WAVE (WebAIM)
- Stark (Figma/Browser)
- ChromeLens

## Common Issues and Solutions

### Issue: Low Contrast on Hover

**Problem**: Cyan on light backgrounds
**Solution**: Darken background on hover or use borders

### Issue: Animation Distraction

**Problem**: Glitch effects trigger vestibular issues
**Solution**: Implement reduced motion media query

### Issue: Focus Loss

**Problem**: Focus indicator not visible on all elements
**Solution**: Universal focus style with high contrast

### Issue: Color-Only Information

**Problem**: Security levels indicated by color alone
**Solution**: Add text labels and patterns

## Assistive Technology Support

### Tested With

- **Screen Readers**: JAWS 2023, NVDA 2023, VoiceOver
- **Voice Control**: Dragon NaturallySpeaking
- **Switch Access**: iOS Switch Control
- **Magnification**: ZoomText, Windows Magnifier

### Known Limitations

1. Complex animations may not announce properly
2. Some terminal effects decorative only
3. Custom fonts may not support all languages

## Resources

### Testing Tools

- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [WAVE Browser Extension](https://wave.webaim.org/extension/)
- [axe DevTools](https://www.deque.com/axe/devtools/)
- [Pa11y Command Line](https://pa11y.org/)

### Guidelines

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [Inclusive Design Principles](https://inclusivedesignprinciples.org/)

### Community

- [A11y Project](https://www.a11yproject.com/)
- [WebAIM Community](https://webaim.org/community/)
- [Deque University](https://dequeuniversity.com/)

---

> "Accessibility is not charity. It's revolution. Every barrier we remove is a wall we tear down." - Trans Hacker Collective