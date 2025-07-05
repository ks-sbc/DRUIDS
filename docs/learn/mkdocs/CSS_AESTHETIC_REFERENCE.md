# CSS Aesthetic Reference - DRUIDS MkDocs Theme

This document extracts and documents all aesthetic properties from the CSS files in `docs/assets/css/`.

## 1. Color Schemes

### Primary Color Palettes

#### DRUIDS Theme Colors (`druids-theme.css`, `druids-components.css`, `druids-layout.css`)

```css
/* Primary Colors */
--druids-orange: #FF6B35;        /* Neon orange - primary accent */
--druids-rust: #B84A14;          /* Darker orange for headers */
--druids-cyan: #00D9FF;          /* Bright cyan - links, highlights */
--druids-dark-blue: #0A1628;     /* Deep blue for code blocks */

/* Accent Colors */
--druids-purple: #BD10E0;        /* Bright purple accent */
--druids-pink: #FF006E;          /* Hot pink for warnings */
--druids-teal: #00CFC1;          /* Teal accent */
--druids-magenta: #FF00FF;       /* Magenta for glows */
--druids-green: #00FF41;         /* Cyber green */
--druids-yellow: #FFD23F;        /* Highlight yellow */

/* Background Colors */
--druids-bg-primary: #0A0E27;    /* Deep space black */
--druids-bg-secondary: #0D1117;  /* Slightly lighter */
--druids-bg-tertiary: #141933;   /* Code backgrounds */
--druids-bg-code: rgba(10, 22, 40, 0.6);
--druids-bg-hover: rgba(0, 217, 255, 0.1);

/* Text Colors */
--druids-text-primary: #E0E0E0;
--druids-text-bright: #FFFFFF;
--druids-text-muted: #B0B0B0;
--druids-text-code: #00D9FF;
```

#### Cyberpunk Guerrilla Colors (`cyberpunk-guerrilla.css`)

```css
/* Extended color variations */
--druids-cyber-dark: #0a0e27;
--druids-cyber-darker: #050714;
--druids-cyber-darkest: #020309;
--druids-cyber-blue: #1a237e;
--druids-cyber-blue-light: #283593;

/* Neon variations with alpha */
--druids-neon-orange-bright: #ff8c42;
--druids-neon-orange-glow: #ff451f;
--druids-cyber-green-dark: #00cc33;
--druids-cyber-green-glow: #00ff4180;
--druids-trans-pink-soft: #ff69b4;
--druids-trans-pink-glow: #ff149380;
--druids-cyber-cyan-dark: #00cccc;
--druids-cyber-cyan-glow: #00ffff80;
```

#### Queer Mandalorian Colors (`queer-mandalorian.css`)

```css
/* Trans pride inspired inverted colors */
--qm-primary-orange: #FF6B35;    /* Inverted light blue */
--qm-rust: #B84A14;              /* H1 headers */
--qm-cyan: #00D9FF;              /* Bright accent */
--qm-purple: #BD10E0;            /* Bright accent */
--qm-pink: #FF006E;              /* Hot pink accent */
--qm-teal: #00CFC1;              /* Inverted pink */
--qm-magenta-glow: #FF00FF;      /* Glitch effects */
```

#### Giscus Dark Theme (`giscus-druids.css`)

```css
--color-canvas-default: #0f172a;
--color-canvas-subtle: #1e293b;
--color-fg-default: #e2e8f0;
--color-accent-fg: #34d399;
--color-accent-emphasis: #10b981;
```

### Gradient Definitions

```css
/* Primary gradients */
--druids-gradient-primary: linear-gradient(135deg, var(--druids-bg-primary) 0%, var(--druids-bg-secondary) 100%);
--druids-gradient-accent: linear-gradient(135deg, var(--druids-orange) 0%, var(--druids-pink) 100%);
--druids-gradient-cyber: linear-gradient(90deg, var(--druids-cyan) 0%, var(--druids-purple) 100%);
--druids-gradient-subtle: linear-gradient(180deg, rgba(255, 255, 255, 0.05) 0%, transparent 100%);

/* Complex mesh gradients */
--druids-bg-mesh: 
  radial-gradient(at 40% 20%, #1a237e33 0px, transparent 50%),
  radial-gradient(at 80% 0%, #ff149333 0px, transparent 50%),
  radial-gradient(at 0% 50%, #00ff4133 0px, transparent 50%),
  radial-gradient(at 80% 50%, #ff6b3533 0px, transparent 50%),
  radial-gradient(at 0% 100%, #00ffff33 0px, transparent 50%);

/* Text gradients */
h1: linear-gradient(90deg, var(--druids-cyber-cyan) 0%, var(--druids-trans-pink) 50%, var(--druids-neon-orange) 100%);
```

### Color Combinations

- **Primary/Secondary**: Cyan (#00D9FF) + Orange (#FF6B35)
- **Warning/Danger**: Orange (#FF6B35) + Pink (#FF006E)
- **Success/Info**: Green (#00FF41) + Cyan (#00D9FF)
- **Code blocks**: Cyan borders with dark blue backgrounds
- **Tables**: Orange gradient backgrounds with cyan headers

## 2. Visual Effects

### Box Shadows

```css
/* Standard shadows */
box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);  /* Small */
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);  /* Medium */
box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4); /* Large */

/* Colored glow shadows */
box-shadow: 0 0 20px var(--druids-cyber-cyan-glow);      /* Cyan glow */
box-shadow: 0 0 15px var(--druids-neon-orange-glow);     /* Orange glow */
box-shadow: 0 0 15px var(--druids-trans-pink-glow);      /* Pink glow */
box-shadow: 0 4px 12px rgba(0, 217, 255, 0.3);          /* Cyan shadow */
box-shadow: 0 4px 12px rgba(255, 107, 53, 0.3);         /* Orange shadow */

/* Complex shadows */
.druids-hero-banner:
  inset 0 0 100px rgba(255, 107, 53, 0.2),
  0 0 50px rgba(255, 0, 255, 0.3);

/* Button hover shadows */
box-shadow: 0 6px 20px rgba(0, 217, 255, 0.5);
transform: translateY(-2px);
```

### Text Shadows

```css
/* Standard text shadows */
text-shadow: 0 0 5px currentColor, 0 0 10px currentColor;
text-shadow: 0 0 10px var(--druids-cyber-cyan-glow);
text-shadow: 0 0 8px rgba(255, 107, 53, 0.5);
text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);

/* Glitch effect shadows */
text-shadow: 2px 2px 0 var(--qm-cyan), -2px -2px 0 var(--qm-magenta-glow);

/* Hero banner complex shadow */
text-shadow: 
  0 0 20px rgba(255, 107, 53, 0.8),
  0 0 40px rgba(255, 107, 53, 0.5),
  2px 2px 4px rgba(0, 0, 0, 0.9);
```

### Glow Effects

```css
/* Filter-based glows */
filter: drop-shadow(0 0 10px var(--druids-cyan));

/* Sunflower multi-layer glow */
filter: 
  drop-shadow(0 0 30px #FFD700)
  drop-shadow(0 0 50px #FF6B35)
  drop-shadow(0 0 70px #FF00FF)
  drop-shadow(0 0 90px rgba(255, 215, 0, 0.5))
  saturate(2) brightness(1.3) contrast(1.2);

/* Utility glow classes */
.glow-cyan: box-shadow: 0 0 20px rgba(0, 217, 255, 0.5);
.glow-orange: box-shadow: 0 0 20px rgba(255, 107, 53, 0.5);
```

### Blur Effects

```css
backdrop-filter: blur(10px);  /* Header blur */
backdrop-filter: blur(5px);   /* Card blur */
```

### Transitions and Animations

#### Transitions

```css
transition: all 0.2s ease;
transition: all 0.3s ease;
transition: color 0.2s ease;
transition: width 0.3s ease;
transition: transform 0.3s ease;
```

#### Animations

```css
/* Pulse animation */
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

/* Glow animation */
@keyframes glow {
  0%, 100% { text-shadow: 0 0 5px currentColor, 0 0 10px currentColor; }
  50% { text-shadow: 0 0 10px currentColor, 0 0 20px currentColor, 0 0 30px currentColor; }
}

/* Glitch animation */
@keyframes glitch {
  0%, 100% { text-shadow: 2px 2px 0 var(--qm-cyan), -2px -2px 0 var(--qm-magenta-glow); }
  25% { text-shadow: -2px 2px 0 var(--qm-cyan), 2px -2px 0 var(--qm-magenta-glow); }
  50% { text-shadow: 2px -2px 0 var(--qm-cyan), -2px 2px 0 var(--qm-magenta-glow); }
  75% { text-shadow: -2px -2px 0 var(--qm-cyan), 2px 2px 0 var(--qm-magenta-glow); }
}

/* Scan line animation */
@keyframes scan {
  0%, 100% { transform: translateY(0); opacity: 1; }
  50% { transform: translateY(100px); opacity: 0; }
}

/* Grid movement */
@keyframes grid-move {
  0% { background-position: -1px -1px; }
  100% { background-position: 49px 49px; }
}

/* Stripe slide */
@keyframes stripe-slide {
  0% { transform: translateX(0); }
  100% { transform: translateX(40px); }
}

/* Hero pulse */
@keyframes hero-pulse {
  0%, 100% { transform: scale(1) rotate(0deg); }
  25% { transform: scale(1.05) rotate(5deg); }
  50% { transform: scale(1.1) rotate(-5deg); }
  75% { transform: scale(1.05) rotate(3deg); }
}

/* Text glow animation */
@keyframes text-glow {
  from { text-shadow: 0 0 20px rgba(255, 107, 53, 0.8), 0 0 40px rgba(255, 107, 53, 0.5); }
  to { text-shadow: 0 0 30px rgba(255, 107, 53, 1), 0 0 60px rgba(255, 107, 53, 0.7), 0 0 80px rgba(255, 0, 255, 0.4); }
}

/* Subtle glitch */
@keyframes subtle-glitch {
  0%, 100% { transform: translateX(0); }
  20% { transform: translateX(-1px); }
  40% { transform: translateX(1px); }
  60% { transform: translateX(-1px); }
  80% { transform: translateX(1px); }
}

/* Gradient shift */
@keyframes gradient-shift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Fade pulse */
@keyframes fade-pulse {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.6; }
}

/* Subtle glow */
@keyframes subtle-glow {
  0%, 100% { opacity: 0.8; }
  50% { opacity: 1; }
}
```

### Transform Effects

```css
transform: translateY(-2px);         /* Button hover lift */
transform: translateY(-4px);         /* Card hover lift */
transform: translateX(-50%);         /* Center horizontally */
transform: scale(1.15) rotate(10deg); /* Sunflower hover */
transform: translateX(40px);         /* Stripe animation */
```

## 3. Typography Aesthetics

### Font Families

```css
/* Headers */
--druids-font-headers: 'Impact', 'Arial Black', -apple-system, sans-serif;
--qm-font-headers: 'Impact', 'Arial Black', -apple-system, sans-serif;

/* Body text */
--druids-font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
--qm-font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
--md-text-font: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;

/* Monospace/Code */
--druids-font-mono: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace;
--qm-font-mono: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace;
--md-code-font: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
```

### Font Sizes and Scales

```css
/* DRUIDS scale */
--druids-text-xs: 0.875rem;    /* 14px */
--druids-text-sm: 1rem;        /* 16px */
--druids-text-base: 1.125rem;  /* 18px */
--druids-text-lg: 1.25rem;     /* 20px */
--druids-text-xl: 1.5rem;      /* 24px */
--druids-text-2xl: 1.875rem;   /* 30px */
--druids-text-3xl: 2.25rem;    /* 36px */
--druids-text-4xl: 3rem;       /* 48px */

/* Hero title massive size */
.hero-title: 5rem !important;

/* Smoothed typography scale */
--qm-text-xs: 0.75rem;      /* 12px */
--qm-text-sm: 0.875rem;     /* 14px */
--qm-text-base: 1rem;       /* 16px */
--qm-text-lg: 1.125rem;     /* 18px */
--qm-text-xl: 1.25rem;      /* 20px */
--qm-text-2xl: 1.5rem;      /* 24px */
--qm-text-3xl: 1.875rem;    /* 30px */
--qm-text-4xl: 2.25rem;     /* 36px */
--qm-text-5xl: 3rem;        /* 48px */
```

### Letter Spacing

```css
/* Tracking values */
--qm-tracking-tight: -0.025em;
--qm-tracking-normal: 0;
--qm-tracking-wide: 0.05em;
--qm-tracking-wider: 0.1em;
--qm-tracking-widest: 0.15em;

/* Applied values */
letter-spacing: 5px;    /* Hero title */
letter-spacing: 4px;    /* H1 */
letter-spacing: 2px;    /* H2, navigation titles */
letter-spacing: 1.5px;  /* H3 */
letter-spacing: 1px;    /* Tables, buttons */
```

### Line Height Ratios

```css
/* Line height scale */
--druids-line-height: 1.6;
--qm-leading-tight: 1.25;
--qm-leading-normal: 1.5;
--qm-leading-relaxed: 1.75;

/* Applied line heights */
line-height: 1.2;  /* Tight headers */
line-height: 1.4;  /* Code blocks */
line-height: 1.6;  /* General text */
line-height: 1.7;  /* Paragraphs */
```

### Text Decorations and Effects

```css
/* Text transforms */
text-transform: uppercase;  /* Headers, buttons, navigation */
text-transform: capitalize; /* Some elements */

/* Font weights */
font-weight: 500;   /* Medium */
font-weight: 600;   /* Semi-bold */
font-weight: 700;   /* Bold */
font-weight: 800;   /* Extra bold */
font-weight: 900;   /* Black */

/* Text decorations */
text-decoration: none;
text-decoration: underline;
text-decoration-style: dotted;
text-decoration-thickness: 2px;
text-underline-offset: 0.2em;
text-underline-offset: 4px;
text-decoration-skip-ink: auto;

/* Special effects */
-webkit-background-clip: text;
background-clip: text;
-webkit-text-fill-color: transparent;
-webkit-font-smoothing: antialiased;
-moz-osx-font-smoothing: grayscale;
text-rendering: optimizeLegibility;
```

## 4. Border and Shape Aesthetics

### Border Styles and Widths

```css
/* Border widths */
border: 1px solid;
border: 2px solid;
border: 3px solid;
border: 4px solid;  /* Left borders for sections */
border-left: 4px solid;
border-bottom: 2px solid;

/* Border colors commonly used */
border-color: var(--druids-cyan);
border-color: var(--druids-orange);
border-color: var(--druids-purple);
border-color: rgba(0, 217, 255, 0.3);
border-color: rgba(255, 107, 53, 0.3);
```

### Border Radius Values

```css
/* DRUIDS theme (subtle rounding) */
--druids-radius-sm: 4px;
--druids-radius-md: 8px;
--druids-radius-lg: 12px;

/* Queer Mandalorian (sharp edges) */
border-radius: 0 !important;  /* Global reset */
border-radius: 4px !important;  /* Pills and badges only */

/* Specific rounded elements */
border-radius: 20px;  /* Search input */
border-radius: 12px;  /* Tags */
border-radius: 6px;   /* Buttons in extra.css */
border-radius: 0 var(--druids-radius-md) 0 var(--druids-radius-sm);  /* Code header */
```

### Custom Shapes

```css
/* Cyber grid background pattern */
background-image: 
  linear-gradient(rgba(0, 255, 255, 0.1) 1px, transparent 1px),
  linear-gradient(90deg, rgba(0, 255, 255, 0.1) 1px, transparent 1px);
background-size: 50px 50px;

/* Tiger stripe pattern */
background: repeating-linear-gradient(
  45deg,
  transparent,
  transparent 20px,
  rgba(255, 0, 255, 0.1) 20px,
  rgba(255, 0, 255, 0.1) 40px
);

/* Decorative elements */
content: "◣◥◣◥◣◥◣◥◣◥◣◥";  /* Hero banner decoration */
content: "◆";              /* HR decoration */
content: "//";             /* Blockquote prefix */
content: "$ ";             /* Terminal prompt */
```

## 5. Spacing and Layout Patterns

### Padding Patterns

```css
/* Common padding values */
padding: 0.125rem 0.25rem;   /* Inline code */
padding: 0.125rem 0.375rem;  /* Small elements */
padding: 0.25rem 0.5rem;     /* Tags */
padding: 0.25rem 0.75rem;    /* Code headers */
padding: 0.375rem 0.75rem;   /* TOC links */
padding: 0.5rem 0.75rem;     /* Nav links */
padding: 0.5rem 1rem;        /* Search, buttons */
padding: 0.75rem 1.25rem;    /* Table cells, admonition titles */
padding: 0.75rem 1.5rem;     /* Buttons */
padding: 1rem 1.5rem;        /* Blockquotes, cards */
padding: 1rem 2rem;          /* Content areas */
padding: 2rem;               /* Main content */
padding: 4rem 2rem;          /* Hero banner */
```

### Margin Patterns

```css
/* Common margin values */
margin: 0.125rem 0;    /* Small spacing */
margin: 0.25rem 0;     /* List items */
margin: 0.375rem 0;    /* Navigation items */
margin: 0.5rem 0;      /* Task lists */
margin: 1rem 0;        /* Paragraphs, general elements */
margin: 1.5rem 0;      /* Cards, admonitions */
margin: 2rem 0 1rem;   /* Headers */
margin: 3rem 0;        /* HR separators */
margin-bottom: 3rem;   /* H1 */
```

### Layout Patterns

```css
/* Flexbox layouts */
display: flex;
flex-direction: row/column;
justify-content: center/space-between/flex-start/flex-end;
align-items: center/flex-start/flex-end;
flex-grow: 1;
flex-wrap: wrap;
gap: 1rem;

/* Grid layouts */
display: grid;
grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
gap: 1rem;

/* Positioning */
position: relative/absolute/fixed/sticky;
z-index: 1/2/999/1000/1001;
```

## 6. Special Effects

### Hover States

```css
/* Color changes */
:hover { color: var(--druids-orange); }
:hover { color: var(--druids-trans-pink); }
:hover { background: var(--druids-bg-hover); }
:hover { background: rgba(0, 217, 255, 0.1); }

/* Transform effects */
:hover { transform: translateY(-2px); }
:hover { transform: translateY(-4px); }
:hover { transform: scale(1.15) rotate(10deg); }
:hover { padding-left: 1.25rem; }  /* Navigation indent */

/* Shadow intensification */
:hover { box-shadow: 0 6px 20px rgba(0, 217, 255, 0.5); }
:hover { box-shadow: 0 8px 24px rgba(0, 217, 255, 0.3); }

/* Complex hover effects */
:hover {
  filter: 
    drop-shadow(0 0 40px #FFD700)
    drop-shadow(0 0 70px #FF6B35)
    drop-shadow(0 0 90px #FF00FF)
    drop-shadow(0 0 110px rgba(255, 215, 0, 0.7))
    saturate(3) brightness(1.5) contrast(1.4);
}
```

### Focus States

```css
/* Standard focus */
:focus {
  outline: 2px solid var(--druids-cyan);
  outline-offset: 2px;
}

/* Enhanced focus */
:focus-visible {
  outline: 3px solid var(--cyber-blue, #00D9FF);
  outline-offset: 2px;
}

/* Input focus */
:focus {
  border-color: var(--druids-orange);
  box-shadow: 0 0 0 2px rgba(255, 107, 53, 0.2);
  box-shadow: 0 0 10px var(--druids-cyber-cyan-glow);
}

/* Giscus focus */
*:focus-visible {
  outline: 2px solid #34d399;
  outline-offset: 2px;
}
```

### Active States

```css
/* Navigation active */
.md-nav__link--active {
  background: linear-gradient(90deg, rgba(0, 217, 255, 0.2), transparent);
  color: var(--druids-cyan);
  font-weight: 600;
  border-left: 3px solid var(--druids-cyan);
}

/* Tab active */
.md-tabs__link--active {
  color: var(--druids-cyber-cyan);
  text-shadow: 0 0 10px var(--druids-cyber-cyan-glow);
}
```

### Disabled States

```css
:disabled {
  opacity: 0.5;
  opacity: 0.6;
  cursor: not-allowed;
}
```

### Selection Colors

```css
::selection {
  background: var(--druids-magenta);
  color: var(--druids-bg-primary);
}

::selection {
  background: var(--druids-trans-pink-glow);
  color: var(--druids-text-primary);
}

::selection {
  background-color: rgba(52, 211, 153, 0.3);
  color: #ffffff;
}
```

### Custom Scrollbars

```css
/* Width and height */
::-webkit-scrollbar {
  width: 8px/10px/12px;
  height: 8px/10px/12px;
}

/* Track styling */
::-webkit-scrollbar-track {
  background: var(--druids-bg-secondary);
  border: 1px solid var(--druids-cyber-blue-light);
  border-radius: var(--druids-radius-sm);
}

/* Thumb styling */
::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg, var(--druids-cyan), var(--druids-purple));
  border-radius: 6px;
  border: 1px solid var(--druids-bg-secondary);
}

::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(180deg, var(--druids-orange), var(--druids-pink));
}

/* Firefox scrollbar */
scrollbar-width: thin;
scrollbar-color: var(--druids-cyan) var(--druids-bg-secondary);
```

## 7. Unique Design Elements

### Security Indicators

```css
/* L0 - Public (Green) */
.security-l0 {
  border-left: 4px solid #00FF41;
  background: linear-gradient(90deg, rgba(0, 255, 65, 0.1) 0%, transparent 100%);
}
.security-l0::before { content: "🟢 L0 - PUBLIC"; }

/* L1 - Member (Orange) */
.security-l1 {
  border-left: 4px solid var(--qm-primary-orange);
  background: linear-gradient(90deg, rgba(255, 107, 53, 0.1) 0%, transparent 100%);
}
.security-l1::before { content: "🟠 L1 - MEMBER"; }

/* L2 - Cadre (Red/Pink) */
.security-l2 {
  border-left: 4px solid var(--qm-pink);
  background: linear-gradient(90deg, rgba(255, 0, 110, 0.1) 0%, transparent 100%);
}
.security-l2::before { content: "🔴 L2 - CADRE ⚠"; animation: pulse 2s ease-in-out infinite; }
```

### Terminal Aesthetics

```css
/* Code block terminal prompt */
pre code::before {
  content: "$ ";
  color: var(--qm-cyan);
  font-weight: bold;
}

/* Scan line effect */
.md-typeset pre::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--druids-cyber-cyan) 0%, var(--druids-trans-pink) 50%, var(--druids-neon-orange) 100%);
  animation: scan 3s ease-in-out infinite;
}
```

### Hero Banner Elements

```css
/* Glowing sunflower with multiple filters */
.glowing-sunflower {
  filter: 
    drop-shadow(0 0 30px #FFD700)
    drop-shadow(0 0 50px #FF6B35)
    drop-shadow(0 0 70px #FF00FF)
    drop-shadow(0 0 90px rgba(255, 215, 0, 0.5))
    saturate(2) brightness(1.3) contrast(1.2);
}

/* Decorative pattern overlays */
.druids-hero-banner::before {
  background: repeating-linear-gradient(
    45deg,
    transparent,
    transparent 20px,
    rgba(255, 0, 255, 0.1) 20px,
    rgba(255, 0, 255, 0.1) 40px
  );
}
```

### Mix Blend Modes

While not extensively used in these files, the CSS supports:

```css
mix-blend-mode: multiply/screen/overlay;  /* For future enhancements */
```

### Backdrop Filters

```css
backdrop-filter: blur(10px);  /* Header glass effect */
backdrop-filter: blur(5px);   /* Card glass effect */
```

## Files and Their Primary Aesthetic Contributions

1. **`druids-theme.css`**: Core color palette, typography sizes, gradients, base animations
2. **`druids-components.css`**: Code blocks, tables, admonitions, buttons, task lists, grids
3. **`druids-layout.css`**: Header/footer styling, navigation, search, spacing
4. **`druids-utilities.css`**: Utility classes, accessibility, print styles, responsive helpers
5. **`cyberpunk-guerrilla.css`**: Extended color variations, complex gradients, glow effects, cyber grid
6. **`queer-mandalorian.css`**: Sharp edges, glitch effects, security indicators, terminal aesthetics
7. **`hero-banner.css`**: Sunflower glow effects, animated stripes, complex text shadows
8. **`typography-smoothing.css`**: Font size refinements, line height adjustments, reading width optimization
9. **`accessibility-enhancements.css`**: High contrast modes, focus states, motion preferences
10. **`giscus-druids.css`**: Dark theme for comments, matching main theme
11. **`giscus.css`**: Basic Giscus integration styling
12. **`final-typography-fix.css`**: Typography overrides, shadow removal
13. **`extra.css`**: Material theme base with blue/green color scheme (appears to be older/different theme)

## Common Aesthetic Patterns

1. **Cyberpunk Aesthetic**: Neon colors (cyan, orange, pink), glow effects, sharp contrasts
2. **Trans Pride Colors**: Inverted color scheme drawing from trans flag colors
3. **Terminal/Hacker Theme**: Monospace fonts, terminal prompts, scan lines
4. **Glassmorphism**: Blur effects, transparency, layered backgrounds
5. **Brutalist Elements**: Sharp edges (border-radius: 0), bold typography, high contrast
6. **Accessibility First**: Clear focus states, motion preferences, high contrast support
7. **Revolutionary Aesthetic**: Security levels, warning indicators, uppercase text
8. **Gradient Heavy**: Linear and radial gradients used extensively for backgrounds and text
