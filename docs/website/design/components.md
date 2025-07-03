---
title: "Component Library Reference"
description: "Complete CSS component library for DRUIDS interface elements across all themes and platforms."
created: 2025-07-01
updated: 2025-07-01
type: "docs/reference"
security: "L0"
version: "1.0.0"
document_id: "INT-REF-2025-100-L0"
tags: ["components", "css", "design-system", "ui-library", "theming"]
draft: true
author: ["Comrade 193"]
exclusion: []
---

# Component Library Reference

- [ ] TODO: Proof read this
- [ ] TODO: Format correctly


## Button Components

### Base Button Styles

```css
.druids-btn {
  /* Base styles */
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--druids-space-sm) var(--druids-space-md);
  font-family: var(--druids-font-body);
  font-size: var(--druids-font-size-base);
  font-weight: var(--font-weight-medium);
  line-height: 1;
  text-decoration: none;
  border-radius: var(--druids-border-radius-md);
  transition: all var(--druids-transition-normal);
  cursor: pointer;
  
  /* Prevent text selection */
  user-select: none;
  -webkit-user-select: none;
}

/* Focus styles for accessibility */
.druids-btn:focus-visible {
  outline: 2px solid var(--druids-focus-color);
  outline-offset: 2px;
}
```

### Theme Variants

#### Prairie Radical Buttons

```css
.theme-prairie-radical .druids-btn-primary {
  background-color: var(--druids-accent-primary);
  color: var(--druids-paper-white);
  border: 1px solid var(--druids-accent-primary);
}

.theme-prairie-radical .druids-btn-primary:hover {
  background-color: #6b2424;
  transform: translateY(-1px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.theme-prairie-radical .druids-btn-secondary {
  background-color: transparent;
  color: var(--druids-accent-primary);
  border: 1px solid var(--druids-accent-primary);
}
```

#### Neobrutalist Buttons

```css
.theme-neobrutalist .druids-btn-primary {
  background-color: var(--druids-accent-primary);
  color: var(--druids-paper-white);
  border: 3px solid #000000;
  box-shadow: 5px 5px 0 0 #000000;
  text-transform: uppercase;
}

.theme-neobrutalist .druids-btn-primary:hover {
  transform: translate(2px, 2px);
  box-shadow: 3px 3px 0 0 #000000;
}

.theme-neobrutalist .druids-btn-primary:active {
  transform: translate(5px, 5px);
  box-shadow: 0 0 0 0 #000000;
}
```

#### Mandalorian Buttons

```css
.theme-mandalorian .druids-btn-primary {
  background-color: var(--druids-accent-primary);
  color: var(--druids-paper-white);
  border: 1px solid var(--druids-accent-primary);
  position: relative;
  overflow: hidden;
}

.theme-mandalorian .druids-btn-primary::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
  transition: left 0.5s;
}

.theme-mandalorian .druids-btn-primary:hover::before {
  left: 100%;
}
```

### Button Sizes

```css
.druids-btn-sm {
  padding: var(--druids-space-xs) var(--druids-space-sm);
  font-size: var(--druids-font-size-sm);
}

.druids-btn-lg {
  padding: var(--druids-space-md) var(--druids-space-lg);
  font-size: var(--druids-font-size-lg);
}

.druids-btn-full {
  width: 100%;
}
```

## Card Components

### Base Card

```css
.druids-card {
  background-color: var(--druids-card-bg);
  border: var(--druids-card-border);
  border-radius: var(--druids-border-radius-md);
  padding: var(--druids-space-md);
  margin-bottom: var(--druids-space-md);
}

.druids-card-header {
  margin-bottom: var(--druids-space-sm);
  padding-bottom: var(--druids-space-sm);
  border-bottom: 1px solid var(--druids-border-color);
}

.druids-card-body {
  /* Card content */
}

.druids-card-footer {
  margin-top: var(--druids-space-sm);
  padding-top: var(--druids-space-sm);
  border-top: 1px solid var(--druids-border-color);
}
```

### Theme Card Variants

#### Prairie Radical Cards

```css
.theme-prairie-radical .druids-card {
  background-color: var(--druids-background-secondary);
  border: 1px solid var(--druids-border-color);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.theme-prairie-radical .druids-card-featured {
  border-left: 4px solid var(--druids-accent-primary);
  background: linear-gradient(135deg, 
    var(--druids-background-secondary) 0%, 
    var(--druids-background-primary) 100%);
}
```

#### Neobrutalist Cards

```css
.theme-neobrutalist .druids-card {
  background-color: var(--druids-paper-white);
  border: 3px solid #000000;
  box-shadow: 8px 8px 0 0 #000000;
}

.theme-neobrutalist .druids-card:hover {
  transform: translate(-2px, -2px);
  box-shadow: 10px 10px 0 0 #000000;
}
```

#### Mandalorian Cards

```css
.theme-mandalorian .druids-card {
  background-color: var(--druids-background-secondary);
  border: 1px solid var(--druids-border-color);
  position: relative;
}

.theme-mandalorian .druids-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url('/img/scratched-metal.svg');
  opacity: 0.05;
  pointer-events: none;
}
```

## Form Components

### Input Fields

```css
.druids-input {
  width: 100%;
  padding: var(--druids-space-sm);
  font-family: var(--druids-font-body);
  font-size: var(--druids-font-size-base);
  background-color: var(--druids-background-primary);
  border: 1px solid var(--druids-border-color);
  border-radius: var(--druids-border-radius-sm);
  transition: border-color var(--druids-transition-fast);
}

.druids-input:focus {
  outline: none;
  border-color: var(--druids-focus-color);
  box-shadow: 0 0 0 3px var(--druids-focus-shadow);
}

/* Theme variants */
.theme-neobrutalist .druids-input {
  border: 3px solid #000000;
  box-shadow: 3px 3px 0 0 #000000;
}

.theme-neobrutalist .druids-input:focus {
  transform: translate(1px, 1px);
  box-shadow: 2px 2px 0 0 #000000;
}
```

### Labels

```css
.druids-label {
  display: block;
  margin-bottom: var(--druids-space-xs);
  font-weight: var(--font-weight-medium);
  font-size: var(--druids-font-size-sm);
  color: var(--druids-text-secondary);
}

.druids-label-required::after {
  content: ' *';
  color: var(--druids-error-color);
}
```

### Form Groups

```css
.druids-form-group {
  margin-bottom: var(--druids-space-md);
}

.druids-form-help {
  margin-top: var(--druids-space-xs);
  font-size: var(--druids-font-size-sm);
  color: var(--druids-text-muted);
}

.druids-form-error {
  margin-top: var(--druids-space-xs);
  font-size: var(--druids-font-size-sm);
  color: var(--druids-error-color);
}
```

## Navigation Components

### Nav Bar

```css
.druids-nav {
  display: flex;
  align-items: center;
  padding: var(--druids-space-sm) var(--druids-space-md);
  background-color: var(--druids-background-secondary);
  border-bottom: 1px solid var(--druids-border-color);
}

.druids-nav-brand {
  font-size: var(--druids-font-size-xl);
  font-weight: var(--font-weight-bold);
  color: var(--druids-text-primary);
  text-decoration: none;
}

.druids-nav-menu {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  margin-left: auto;
}

.druids-nav-item {
  margin-left: var(--druids-space-md);
}

.druids-nav-link {
  color: var(--druids-text-secondary);
  text-decoration: none;
  transition: color var(--druids-transition-fast);
}

.druids-nav-link:hover,
.druids-nav-link.active {
  color: var(--druids-accent-primary);
}
```

### Breadcrumbs

```css
.druids-breadcrumb {
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  margin: 0;
  padding: 0;
}

.druids-breadcrumb-item {
  display: flex;
  align-items: center;
}

.druids-breadcrumb-item:not(:last-child)::after {
  content: '/';
  margin: 0 var(--druids-space-sm);
  color: var(--druids-text-muted);
}

.theme-neobrutalist .druids-breadcrumb-item:not(:last-child)::after {
  content: '>';
  font-weight: bold;
}
```

## Alert Components

### Base Alert

```css
.druids-alert {
  padding: var(--druids-space-md);
  margin-bottom: var(--druids-space-md);
  border-radius: var(--druids-border-radius-md);
  border: 1px solid;
}

.druids-alert-title {
  font-weight: var(--font-weight-semibold);
  margin-bottom: var(--druids-space-xs);
}
```

### Alert Variants

```css
.druids-alert-info {
  background-color: var(--druids-info-bg);
  border-color: var(--druids-info-border);
  color: var(--druids-info-text);
}

.druids-alert-success {
  background-color: var(--druids-success-bg);
  border-color: var(--druids-success-border);
  color: var(--druids-success-text);
}

.druids-alert-warning {
  background-color: var(--druids-warning-bg);
  border-color: var(--druids-warning-border);
  color: var(--druids-warning-text);
}

.druids-alert-error {
  background-color: var(--druids-error-bg);
  border-color: var(--druids-error-border);
  color: var(--druids-error-text);
}
```

## Modal Components

### Modal Structure

```css
.druids-modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: var(--druids-z-modal-backdrop);
}

.druids-modal {
  background-color: var(--druids-background-primary);
  border-radius: var(--druids-border-radius-lg);
  box-shadow: var(--druids-shadow-xl);
  max-width: 500px;
  width: 90%;
  max-height: 90vh;
  overflow: hidden;
  z-index: var(--druids-z-modal);
}

.druids-modal-header {
  padding: var(--druids-space-md);
  border-bottom: 1px solid var(--druids-border-color);
}

.druids-modal-body {
  padding: var(--druids-space-md);
  overflow-y: auto;
  max-height: calc(90vh - 120px);
}

.druids-modal-footer {
  padding: var(--druids-space-md);
  border-top: 1px solid var(--druids-border-color);
  display: flex;
  justify-content: flex-end;
  gap: var(--druids-space-sm);
}
```

## Badge Components

```css
.druids-badge {
  display: inline-flex;
  align-items: center;
  padding: var(--druids-space-xs) var(--druids-space-sm);
  font-size: var(--druids-font-size-xs);
  font-weight: var(--font-weight-medium);
  line-height: 1;
  border-radius: var(--druids-border-radius-full);
  white-space: nowrap;
}

.druids-badge-primary {
  background-color: var(--druids-accent-primary);
  color: var(--druids-paper-white);
}

.druids-badge-secondary {
  background-color: var(--druids-background-tertiary);
  color: var(--druids-text-secondary);
}

/* Dot indicator */
.druids-badge-dot {
  width: 0.5rem;
  height: 0.5rem;
  border-radius: 50%;
  margin-right: var(--druids-space-xs);
}
```

## Loading Components

### Spinner

```css
.druids-spinner {
  display: inline-block;
  width: 1em;
  height: 1em;
  border: 2px solid var(--druids-border-color);
  border-top-color: var(--druids-accent-primary);
  border-radius: 50%;
  animation: druids-spin 0.8s linear infinite;
}

@keyframes druids-spin {
  to { transform: rotate(360deg); }
}
```

### Progress Bar

```css
.druids-progress {
  height: 0.5rem;
  background-color: var(--druids-background-secondary);
  border-radius: var(--druids-border-radius-full);
  overflow: hidden;
}

.druids-progress-bar {
  height: 100%;
  background-color: var(--druids-accent-primary);
  transition: width var(--druids-transition-normal);
}

/* Animated variant */
.druids-progress-bar.animated {
  background-image: linear-gradient(
    45deg,
    rgba(255, 255, 255, 0.15) 25%,
    transparent 25%,
    transparent 50%,
    rgba(255, 255, 255, 0.15) 50%,
    rgba(255, 255, 255, 0.15) 75%,
    transparent 75%,
    transparent
  );
  background-size: 1rem 1rem;
  animation: druids-progress-animation 1s linear infinite;
}

@keyframes druids-progress-animation {
  0% { background-position: 0 0; }
  100% { background-position: 1rem 0; }
}
```

## Utility Classes

### Spacing

```css
/* Margin */
.m-0 { margin: 0; }
.m-1 { margin: var(--druids-space-xs); }
.m-2 { margin: var(--druids-space-sm); }
.m-3 { margin: var(--druids-space-md); }
.m-4 { margin: var(--druids-space-lg); }
.m-5 { margin: var(--druids-space-xl); }

/* Padding */
.p-0 { padding: 0; }
.p-1 { padding: var(--druids-space-xs); }
.p-2 { padding: var(--druids-space-sm); }
.p-3 { padding: var(--druids-space-md); }
.p-4 { padding: var(--druids-space-lg); }
.p-5 { padding: var(--druids-space-xl); }
```

### Display

```css
.d-none { display: none; }
.d-block { display: block; }
.d-inline { display: inline; }
.d-inline-block { display: inline-block; }
.d-flex { display: flex; }
.d-grid { display: grid; }
```

### Text

```css
.text-left { text-align: left; }
.text-center { text-align: center; }
.text-right { text-align: right; }
.text-justify { text-align: justify; }

.text-uppercase { text-transform: uppercase; }
.text-lowercase { text-transform: lowercase; }
.text-capitalize { text-transform: capitalize; }

.font-weight-normal { font-weight: var(--font-weight-regular); }
.font-weight-bold { font-weight: var(--font-weight-bold); }
```
