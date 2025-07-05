---
title: "Typography Specification"
description: "Complete typography system specification including font stacks, type scales, and usage guidelines across all DRUIDS themes."
created: 2025-07-01
updated: 2025-07-01
type: "docs/reference"
security: "L0"
version: "1.0.0"
document_id: "INT-REF-2025-100-L0"
tags: ["typography", "fonts", "design-system", "type-scale", "accessibility"]
draft: true
author: ["Comrade 192"]
exclusion: []
---

# Typography Specification

- [ ] TODO: Proof read this
- [ ] TODO: Format correctly


## Font Stack Definitions

### Primary Font Families

#### Heading Fonts

```css
/* Prairie Radical */
font-family: 'Playfair Display', 'Spectral', Georgia, 'Times New Roman', serif;

/* Neobrutalist */
font-family: 'EB Garamond', 'Spectral', Georgia, serif;

/* Mandalorian */
font-family: 'Bebas Neue', 'Oswald', Arial, sans-serif;
```

#### Body Fonts

```css
/* All Themes */
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif;
```

#### Monospace Fonts

```css
/* All Themes */
font-family: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', Consolas, 'Courier New', monospace;
```

## Type Scale

### Desktop Scale (base: 16px)

| Level | Size | Pixels | Line Height | Usage |
|-------|------|--------|-------------|-------|
| xs | 0.75rem | 12px | 1.5 | Captions, labels |
| sm | 0.875rem | 14px | 1.5 | Secondary text |
| base | 1rem | 16px | 1.625 | Body text |
| lg | 1.125rem | 18px | 1.625 | Lead paragraph |
| xl | 1.25rem | 20px | 1.5 | H6 |
| 2xl | 1.5rem | 24px | 1.375 | H5 |
| 3xl | 1.875rem | 30px | 1.375 | H4 |
| 4xl | 2.25rem | 36px | 1.25 | H3 |
| 5xl | 3rem | 48px | 1.25 | H2 |
| 6xl | 3.75rem | 60px | 1.125 | H1 |

### Mobile Scale (base: 14px)

| Level | Size | Pixels | Line Height |
|-------|------|--------|-------------|
| xs | 0.75rem | 10.5px | 1.5 |
| sm | 0.875rem | 12.25px | 1.5 |
| base | 1rem | 14px | 1.625 |
| lg | 1.125rem | 15.75px | 1.625 |
| xl | 1.25rem | 17.5px | 1.5 |
| 2xl | 1.5rem | 21px | 1.375 |
| 3xl | 1.875rem | 26.25px | 1.375 |
| 4xl | 2.25rem | 31.5px | 1.25 |
| 5xl | 2.5rem | 35px | 1.25 |
| 6xl | 3rem | 42px | 1.125 |

## Font Weights

### Weight Scale

```css
--font-weight-light: 300;
--font-weight-regular: 400;
--font-weight-medium: 500;
--font-weight-semibold: 600;
--font-weight-bold: 700;
--font-weight-extrabold: 800;
--font-weight-black: 900;
```

### Theme-Specific Weights

| Element | Prairie Radical | Neobrutalist | Mandalorian |
|---------|----------------|--------------|-------------|
| H1-H3 | 700 (bold) | 600 (semibold) | 400 (regular) |
| H4-H6 | 600 (semibold) | 600 (semibold) | 400 (regular) |
| Body | 400 (regular) | 400 (regular) | 400 (regular) |
| Strong | 600 (semibold) | 700 (bold) | 600 (semibold) |
| Code | 400 (regular) | 500 (medium) | 400 (regular) |

## Letter Spacing

```css
--letter-spacing-tighter: -0.05em;
--letter-spacing-tight: -0.025em;
--letter-spacing-normal: 0;
--letter-spacing-wide: 0.025em;
--letter-spacing-wider: 0.05em;
--letter-spacing-widest: 0.1em;
```

### Theme Applications

- **Prairie Radical**: Normal spacing for readability
- **Neobrutalist**: Wider spacing (0.05em) for headings
- **Mandalorian**: Wider spacing (0.1em) for Bebas Neue headings

## Text Transformations

### By Theme

```css
/* Prairie Radical */
.theme-prairie-radical h1,
.theme-prairie-radical h2 {
  text-transform: none;
}

/* Neobrutalist */
.theme-neobrutalist h1,
.theme-neobrutalist h2,
.theme-neobrutalist h3 {
  text-transform: uppercase;
}

/* Mandalorian */
.theme-mandalorian h1,
.theme-mandalorian h2 {
  text-transform: uppercase;
}
```

## Responsive Typography

### Fluid Type Scale

```css
/* Fluid typography using clamp() */
h1 {
  font-size: clamp(2.5rem, 5vw + 1rem, 3.75rem);
}

h2 {
  font-size: clamp(2rem, 4vw + 0.5rem, 3rem);
}

h3 {
  font-size: clamp(1.5rem, 3vw + 0.5rem, 2.25rem);
}

body {
  font-size: clamp(0.875rem, 1vw + 0.5rem, 1rem);
}
```

## Text Styles

### Paragraph Styles

```css
/* Default paragraph */
p {
  font-size: var(--druids-font-size-base);
  line-height: var(--druids-line-height-relaxed);
  margin-bottom: var(--druids-space-md);
}

/* Lead paragraph */
.lead {
  font-size: var(--druids-font-size-lg);
  line-height: var(--druids-line-height-relaxed);
  font-weight: var(--font-weight-light);
}

/* Small text */
.small {
  font-size: var(--druids-font-size-sm);
  line-height: var(--druids-line-height-normal);
}
```

### List Styles

```css
/* Unordered lists */
ul {
  list-style-type: disc;
  padding-left: var(--druids-space-lg);
}

/* Ordered lists */
ol {
  list-style-type: decimal;
  padding-left: var(--druids-space-lg);
}

/* Nested lists */
ul ul, ol ul {
  list-style-type: circle;
}

ul ul ul, ol ul ul {
  list-style-type: square;
}
```

### Code Styles

```css
/* Inline code */
code {
  font-family: var(--druids-font-mono);
  font-size: 0.875em;
  background-color: var(--druids-background-secondary);
  padding: 0.125rem 0.25rem;
  border-radius: var(--druids-border-radius-sm);
}

/* Code blocks */
pre {
  font-family: var(--druids-font-mono);
  font-size: var(--druids-font-size-sm);
  line-height: var(--druids-line-height-normal);
  overflow-x: auto;
  padding: var(--druids-space-md);
}
```

## Accessibility Considerations

### Minimum Sizes

- Body text: Never smaller than 14px (0.875rem)
- UI text: Never smaller than 12px (0.75rem)
- Touch targets with text: Minimum 44px height

### Line Height Guidelines

- Body text: 1.5-1.625 for optimal readability
- Headings: 1.125-1.375 depending on size
- Code: 1.5 for clarity

### Contrast Requirements

- Normal text: 4.5:1 minimum
- Large text (18px+ or 14px+ bold): 3:1 minimum
- All theme combinations tested for WCAG AA compliance

## Font Loading Strategy

```css
/* Font Face Declarations with font-display */
@font-face {
  font-family: 'Playfair Display';
  src: url('/fonts/playfair-display.woff2') format('woff2');
  font-weight: 400 700;
  font-display: swap; /* Ensures text remains visible during load */
}

/* System Font Fallback */
.system-font-fallback {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
```

### Performance Optimization

1. Use `font-display: swap` for all custom fonts
2. Preload critical fonts: `<link rel="preload" as="font">`
3. Subset fonts to only needed characters
4. Use variable fonts where possible

## Special Typography Features

### Drop Caps (Prairie Radical)

```css
.theme-prairie-radical article > p:first-of-type::first-letter {
  font-family: 'Playfair Display', serif;
  font-size: 4em;
  float: left;
  line-height: 0.8;
  margin: 0.1em 0.1em 0 0;
  color: var(--druids-accent-primary);
}
```

### Outlined Text (Neobrutalist)

```css
.theme-neobrutalist .text-outline {
  color: transparent;
  -webkit-text-stroke: 2px var(--druids-text-primary);
  text-stroke: 2px var(--druids-text-primary);
}
```

### Glitch Effect (Mandalorian)

```css
.theme-mandalorian .glitch {
  position: relative;
  text-shadow: 
    0.05em 0 0 var(--druids-accent-secondary),
    -0.05em 0 0 var(--druids-accent-primary);
  animation: glitch 500ms infinite;
}
```
