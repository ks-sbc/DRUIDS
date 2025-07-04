---
title: "CSS Variables Reference"
description: "Complete reference for CSS custom properties used throughout the DRUIDS design system."
created: 2025-07-01
updated: 2025-07-01
type: "docs/reference"
security: "L0"
version: "1.0.0"
document_id: "INT-REF-2025-100-L0"
tags: ["css", "variables", "design-system", "theming", "styling"]
draft: true
author: ["Comrade 192", "Comrade 190"]
exclusion: []
---

# CSS Variables Reference

- [ ] TODO: Proof read this
- [ ] TODO: Format correctly


## Core Variables Structure

### Root Variables

```css
:root {
  /* ===== BRAND COLORS ===== */
  --druids-revolutionary-red: #CC3C3A;
  --druids-revolutionary-red-900: #661E1D;
  --druids-revolutionary-red-700: #992D2C;
  --druids-revolutionary-red-500: #CC3C3A;
  --druids-revolutionary-red-300: #E56B69;
  --druids-revolutionary-red-100: #F5A5A4;
  --druids-revolutionary-red-50: #FAD2D2;
  
  --druids-theory-black: #121212;
  --druids-theory-black-900: #000000;
  --druids-theory-black-700: #0A0A0A;
  --druids-theory-black-500: #121212;
  --druids-theory-black-300: #3A3A3A;
  --druids-theory-black-100: #6B6B6B;
  --druids-theory-black-50: #9A9A9A;
  
  --druids-paper-white: #F8F7F6;
  --druids-comrade-gold: #D6AA00;
  
  /* ===== SPACING SYSTEM ===== */
  --druids-space-xs: 0.25rem;   /* 4px */
  --druids-space-sm: 0.5rem;    /* 8px */
  --druids-space-md: 1rem;      /* 16px */
  --druids-space-lg: 1.5rem;    /* 24px */
  --druids-space-xl: 2rem;      /* 32px */
  --druids-space-2xl: 3rem;     /* 48px */
  --druids-space-3xl: 4rem;     /* 64px */
  
  /* ===== TYPOGRAPHY SCALE ===== */
  --druids-font-size-xs: 0.75rem;    /* 12px */
  --druids-font-size-sm: 0.875rem;   /* 14px */
  --druids-font-size-base: 1rem;     /* 16px */
  --druids-font-size-lg: 1.125rem;   /* 18px */
  --druids-font-size-xl: 1.25rem;    /* 20px */
  --druids-font-size-2xl: 1.5rem;    /* 24px */
  --druids-font-size-3xl: 1.875rem;  /* 30px */
  --druids-font-size-4xl: 2.25rem;   /* 36px */
  --druids-font-size-5xl: 3rem;      /* 48px */
  
  /* ===== FONT FAMILIES ===== */
  --druids-font-heading: 'Spectral', 'Playfair Display', Georgia, serif;
  --druids-font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --druids-font-mono: 'JetBrains Mono', 'Courier New', monospace;
  
  /* ===== LINE HEIGHTS ===== */
  --druids-line-height-tight: 1.25;
  --druids-line-height-normal: 1.5;
  --druids-line-height-relaxed: 1.625;
  --druids-line-height-loose: 2;
  
  /* ===== BORDERS ===== */
  --druids-border-width-thin: 1px;
  --druids-border-width-medium: 2px;
  --druids-border-width-thick: 3px;
  --druids-border-width-heavy: 4px;
  --druids-border-radius-sm: 0.25rem;
  --druids-border-radius-md: 0.5rem;
  --druids-border-radius-lg: 0.75rem;
  --druids-border-radius-full: 9999px;
  
  /* ===== SHADOWS ===== */
  --druids-shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --druids-shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --druids-shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  --druids-shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
  --druids-shadow-neo: 8px 8px 0 0 #000000;
  
  /* ===== TRANSITIONS ===== */
  --druids-transition-fast: 150ms ease-in-out;
  --druids-transition-normal: 250ms ease-in-out;
  --druids-transition-slow: 350ms ease-in-out;
  
  /* ===== Z-INDEX SCALE ===== */
  --druids-z-base: 0;
  --druids-z-dropdown: 1000;
  --druids-z-sticky: 1100;
  --druids-z-fixed: 1200;
  --druids-z-modal-backdrop: 1300;
  --druids-z-modal: 1400;
  --druids-z-popover: 1500;
  --druids-z-tooltip: 1600;
}
```

### Theme-Specific Variables

#### Prairie Radical Theme

```css
.theme-prairie-radical {
  /* Colors */
  --druids-background-primary: #f8f1e5;
  --druids-background-secondary: #ebe3d3;
  --druids-background-tertiary: #dfd6c5;
  --druids-text-primary: #3a3226;
  --druids-text-secondary: #5c5142;
  --druids-text-muted: #7a6e5e;
  --druids-accent-primary: #8b2e2e;
  --druids-accent-secondary: #d4a574;
  --druids-border-color: #c8b8a1;
  
  /* Component Specific */
  --druids-button-bg: var(--druids-accent-primary);
  --druids-button-text: var(--druids-paper-white);
  --druids-button-hover-bg: #6b2424;
  --druids-card-bg: var(--druids-background-secondary);
  --druids-card-border: var(--druids-border-color);
  
  /* Typography */
  --druids-heading-font: 'Playfair Display', Georgia, serif;
  --druids-heading-weight: 700;
  --druids-body-weight: 400;
}
```

#### Neobrutalist Theme

```css
.theme-neobrutalist {
  /* Colors */
  --druids-background-primary: #FFE200;
  --druids-background-secondary: #FFD700;
  --druids-text-primary: #000000;
  --druids-text-secondary: #333333;
  --druids-accent-primary: #FF0000;
  --druids-accent-secondary: #0000FF;
  --druids-border-color: #000000;
  
  /* Brutalist Specific */
  --druids-border-width: 3px;
  --druids-shadow-offset: 8px;
  --druids-rotation: -1deg;
  
  /* Component Specific */
  --druids-button-bg: var(--druids-accent-primary);
  --druids-button-text: var(--druids-paper-white);
  --druids-button-border: var(--druids-border-width) solid #000000;
  --druids-button-shadow: var(--druids-shadow-offset) var(--druids-shadow-offset) 0 0 #000000;
  
  /* Typography */
  --druids-heading-font: 'EB Garamond', Georgia, serif;
  --druids-heading-transform: uppercase;
  --druids-heading-letter-spacing: 0.05em;
}
```

#### Mandalorian Theme

```css
.theme-mandalorian {
  /* Colors */
  --druids-background-primary: #1a1d23;
  --druids-background-secondary: #22252c;
  --druids-background-tertiary: #2a2d35;
  --druids-text-primary: #e0e0e0;
  --druids-text-secondary: #b0b0b0;
  --druids-text-muted: #808080;
  --druids-accent-primary: #4a8b4a;
  --druids-accent-secondary: #c76e2e;
  --druids-border-color: #2d3137;
  
  /* Technical Specific */
  --druids-code-bg: #0d1117;
  --druids-code-border: #30363d;
  --druids-texture-opacity: 0.05;
  
  /* Component Specific */
  --druids-button-bg: var(--druids-accent-primary);
  --druids-button-text: var(--druids-paper-white);
  --druids-button-hover-bg: #3a6b3a;
  --druids-card-bg: var(--druids-background-secondary);
  --druids-card-border: 1px solid var(--druids-border-color);
  
  /* Typography */
  --druids-heading-font: 'Bebas Neue', Arial, sans-serif;
  --druids-heading-weight: 400;
  --druids-code-font-size: 0.9em;
}
```

### Security Level Variables

```css
:root {
  /* L0 - Public */
  --druids-security-l0-color: #3B82F6;
  --druids-security-l0-bg: rgba(59, 130, 246, 0.05);
  --druids-security-l0-border: #3B82F6;
  --druids-security-l0-text: #1E40AF;
  --druids-security-l0-icon: "🟢";
  
  /* L1 - Member */
  --druids-security-l1-color: #D6AA00;
  --druids-security-l1-bg: rgba(214, 170, 0, 0.05);
  --druids-security-l1-border: #D6AA00;
  --druids-security-l1-text: #92400E;
  --druids-security-l1-icon: "🟡";
  
  /* L2 - Cadre */
  --druids-security-l2-color: #CC3C3A;
  --druids-security-l2-bg: rgba(204, 60, 58, 0.05);
  --druids-security-l2-border: #CC3C3A;
  --druids-security-l2-text: #991B1B;
  --druids-security-l2-icon: "🔴";
}
```

## Responsive Variables

```css
/* Mobile First Breakpoints */
@custom-media --druids-sm (min-width: 640px);
@custom-media --druids-md (min-width: 768px);
@custom-media --druids-lg (min-width: 1024px);
@custom-media --druids-xl (min-width: 1280px);
@custom-media --druids-2xl (min-width: 1536px);

/* Responsive Spacing */
@media (--druids-sm) {
  :root {
    --druids-space-responsive: var(--druids-space-md);
  }
}

@media (--druids-lg) {
  :root {
    --druids-space-responsive: var(--druids-space-lg);
  }
}
```

## Dark Mode Support

```css
@media (prefers-color-scheme: dark) {
  .theme-prairie-radical {
    --druids-background-primary: #2a2520;
    --druids-text-primary: #f8f1e5;
    /* ... additional dark mode overrides */
  }
}

/* Manual dark mode toggle */
[data-theme="dark"] {
  /* Dark mode variable overrides */
}
```

## Animation Variables

```css
:root {
  /* Keyframes */
  --druids-pulse: druids-pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
  --druids-bounce: druids-bounce 1s infinite;
  --druids-shake: druids-shake 0.5s;
  
  /* Easing Functions */
  --druids-ease-in: cubic-bezier(0.4, 0, 1, 1);
  --druids-ease-out: cubic-bezier(0, 0, 0.2, 1);
  --druids-ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
}

@keyframes druids-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

@keyframes druids-bounce {
  0%, 100% { transform: translateY(-25%); }
  50% { transform: translateY(0); }
}

@keyframes druids-shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-5px); }
  75% { transform: translateX(5px); }
}
```

## Usage Examples

### Basic Component

```css
.druids-button {
  background-color: var(--druids-button-bg);
  color: var(--druids-button-text);
  padding: var(--druids-space-sm) var(--druids-space-md);
  border-radius: var(--druids-border-radius-md);
  font-family: var(--druids-font-body);
  font-size: var(--druids-font-size-base);
  transition: all var(--druids-transition-normal);
}
```

### Security Badge

```css
.security-badge[data-level="l0"] {
  color: var(--druids-security-l0-text);
  background-color: var(--druids-security-l0-bg);
  border-left: var(--druids-border-width-heavy) solid var(--druids-security-l0-border);
}
```

### Responsive Container

```css
.druids-container {
  padding: var(--druids-space-responsive);
  max-width: calc(100% - (var(--druids-space-responsive) * 2));
}
```
