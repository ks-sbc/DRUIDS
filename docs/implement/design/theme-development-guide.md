---
title: "DRUIDS Theme Development Guide"
description: "Comprehensive guide for creating accessible, revolutionary themes for DRUIDS with a focus on disability justice and inclusive design"
created: 2025-07-02
updated: 2025-07-02
type: "docs/reference"
security: "L0"
version: "1.0.0"
document_id: "INT-REF-2025-400-L0"
tags: ["theme", "accessibility", "design", "customization", "wcag", "disability-justice"]
draft: false
author: ["Comrade 191"]
---

# DRUIDS Theme Development Guide

## Overview

This guide consolidates all theme development documentation for DRUIDS, with **accessibility as the primary focus**. Every theme must prioritize disability justice and inclusive design while maintaining revolutionary aesthetics.

## Core Principles

### Accessibility First

1. **Disability Justice**: Our revolution must be accessible to all comrades
2. **WCAG 2.1 AA Compliance**: Minimum standard for all themes
3. **Progressive Enhancement**: Core functionality without CSS/JS
4. **Multiple Indicators**: Never rely solely on color for information

### Revolutionary Aesthetics

1. **Anti-Oppression Design**: Visual resistance to corporate aesthetics
2. **Community Identity**: Themes express organizational values
3. **Security Visualization**: Clear L0/L1/L2 indicators
4. **Cultural Significance**: Honor revolutionary traditions

## Quick Start

### Creating Your First Theme

1. **Start with Accessibility**
   ```css
   /* Base your theme on proven accessible foundations */
   @import url('/stylesheets/accessibility-enhancements.css');
   ```

2. **Test Early and Often**
   ```bash
   # Use automated testing tools
   npm run test:a11y
   axe-devtools  # Browser extension
   ```

3. **Follow the Queer Mandalorian Example**
   - Study `/stylesheets/queer-mandalorian.css` for best practices
   - Review `qm-accessibility.md` for detailed testing

## Accessibility Requirements

### Color Contrast

All themes MUST meet these contrast ratios:

| Element Type | Minimum Ratio | Preferred |
|-------------|---------------|-----------|
| Body text | 4.5:1 | 7:1 (AAA) |
| Large text | 3:1 | 4.5:1 |
| UI components | 3:1 | 4.5:1 |
| Focus indicators | 3:1 | 4.5:1 |

### Security Level Indicators

Never use color alone. Combine multiple indicators:

```css
/* Example: L2 (Cadre) Security */
.L2 {
  /* Visual indicators */
  color: var(--l2-text);
  background: var(--l2-bg);
  border: 2px solid var(--l2-border);
  
  /* Pattern overlay for colorblind users */
  background-image: repeating-linear-gradient(
    45deg,
    transparent,
    transparent 10px,
    rgba(255,0,0,0.1) 10px,
    rgba(255,0,0,0.1) 20px
  );
  
  /* Icon indicator */
  &::before {
    content: "🔒";
    margin-right: 0.5em;
  }
  
  /* Screen reader text */
  .sr-only::before {
    content: "Cadre Level Security: ";
  }
}
```

### Keyboard Navigation

- All interactive elements must be keyboard accessible
- Visible focus indicators (not just browser defaults)
- Logical tab order
- Skip links for navigation

### Motion and Animation

```css
/* Respect user preferences */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Theme Structure

### Required Files

```
theme-name/
├── theme.css           # Main theme file
├── accessibility.css   # Accessibility overrides
├── variables.css      # CSS custom properties
├── README.md          # Documentation
└── test-results.md    # Accessibility test results
```

### CSS Architecture

1. **CSS Custom Properties First**
   ```css
   :root {
     /* Colors with semantic names */
     --text-primary: #e0e0e0;
     --bg-primary: #0a0e27;
     
     /* Spacing scale */
     --space-xs: 0.25rem;
     --space-sm: 0.5rem;
     --space-md: 1rem;
     
     /* Type scale */
     --text-sm: 0.875rem;
     --text-base: 1rem;
     --text-lg: 1.25rem;
   }
   ```

2. **Component-Based Structure**
   ```css
   /* Base components */
   @import 'components/buttons.css';
   @import 'components/forms.css';
   @import 'components/navigation.css';
   
   /* Security levels */
   @import 'security/l0-public.css';
   @import 'security/l1-member.css';
   @import 'security/l2-cadre.css';
   ```

## Implementation Guide

### Step 1: Research and Planning

1. **Understand Your Users**
   - Survey community accessibility needs
   - Consider various disabilities (visual, motor, cognitive)
   - Plan for assistive technology compatibility

2. **Define Visual Identity**
   - Choose colors that meet contrast requirements
   - Select readable fonts (avoid thin weights)
   - Design clear iconography

### Step 2: Build Accessible Foundation

```css
/* Start with accessibility */
* {
  /* Ensure text is readable */
  line-height: 1.5;
  letter-spacing: 0.02em;
}

/* Focus styles */
:focus {
  outline: 3px solid var(--focus-color);
  outline-offset: 2px;
}

/* Skip links */
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: var(--bg-primary);
  color: var(--text-primary);
  padding: 8px;
  z-index: 100;
  text-decoration: none;
}

.skip-link:focus {
  top: 0;
}
```

### Step 3: Add Revolutionary Aesthetics

Build visual identity on top of accessible foundation:

```css
/* Example: Cyberpunk aesthetic with accessibility */
.header {
  /* Accessible base */
  color: var(--text-primary);
  background: var(--bg-primary);
  
  /* Aesthetic enhancement */
  background-image: 
    linear-gradient(45deg, transparent 30%, rgba(0,217,255,0.1) 50%, transparent 70%);
  text-shadow: 0 0 20px rgba(0,217,255,0.5);
  
  /* Ensure contrast maintained */
  position: relative;
  z-index: 1;
}
```

### Step 4: Test Thoroughly

1. **Automated Testing**
   ```bash
   # Run accessibility tests
   npm run test:a11y
   
   # Check contrast ratios
   npx color-contrast-checker
   ```

2. **Manual Testing**
   - Navigate with keyboard only
   - Test with screen readers (NVDA, JAWS, VoiceOver)
   - Verify with browser zoom at 200%
   - Check with Windows High Contrast mode

3. **Real User Testing**
   - Recruit testers with disabilities
   - Gather feedback on actual usage
   - Iterate based on findings

## Best Practices

### Do's ✅

- Start with accessibility, add aesthetics after
- Test with real assistive technologies
- Provide multiple ways to perceive information
- Document all accessibility features
- Include disabled comrades in design process

### Don'ts ❌

- Don't use color as the only indicator
- Don't remove focus indicators
- Don't use fonts smaller than 14px
- Don't create seizure-inducing animations
- Don't assume your users' abilities

## Theme Examples

### Queer Mandalorian (Accessibility Exemplar)

- Full WCAG 2.1 AA compliance
- Revolutionary cyberpunk aesthetic
- Multiple security indicators
- Excellent keyboard navigation
- See: `/stylesheets/queer-mandalorian.css`

### Cyberpunk Guerrilla

- High contrast design
- Reduced motion options
- Clear visual hierarchy
- See: `/stylesheets/cyberpunk-guerilla.css`

## Testing Resources

### Tools

- **axe DevTools**: Browser extension for accessibility testing
- **WAVE**: Web Accessibility Evaluation Tool
- **Contrast Ratio Checkers**: Ensure color compliance
- **Screen Readers**: NVDA (free), JAWS, VoiceOver

### Testing Checklist

- [ ] All text meets contrast requirements
- [ ] Keyboard navigation works throughout
- [ ] Screen reader announces content correctly
- [ ] No information conveyed by color alone
- [ ] Focus indicators visible
- [ ] Forms have proper labels
- [ ] Images have alt text
- [ ] Animations respect prefers-reduced-motion
- [ ] Page works at 200% zoom
- [ ] No horizontal scrolling at standard widths

## Contributing

When submitting a new theme:

1. Include full accessibility test results
2. Document any known limitations
3. Provide remediation for any AA failures
4. Include screenshots with different color filters
5. Test with at least one screen reader

## References

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Resources](https://webaim.org/)
- [Inclusive Design Principles](https://inclusivedesignprinciples.org/)
- [Disability Justice Collective](https://www.sinsinvalid.org/blog/disability-justice-a-working-draft-by-patty-berne)

---

> "Nothing About Us Without Us" - Disability rights movement
> 
> Every theme we create must embody this principle.