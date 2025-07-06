---
title: Offline Usage Setup Guide
description: Complete guide to building Progressive Web App functionality
tags:
  - offline
  - pwa
  - service-worker
  - performance
  - mobile
comments: true
---

# Offline Usage Setup Guide

Transform your MkDocs Material site into a Progressive Web App (PWA) that works seamlessly offline.

## Overview

The offline plugin enables:

- 📱 **Progressive Web App** functionality
- 🔄 **Service Worker** for caching
- 📶 **Offline browsing** of visited pages
- 🚀 **Faster loading** through intelligent caching
- 📲 **App-like experience** on mobile devices

## Basic Offline Configuration

### 1. Enable Offline Plugin

```yaml
# mkdocs.yml
plugins:
  - material/offline:
      enabled: !ENV [CI, false]
      offline: true
      offline_on_serve: false
```

### 2. Configuration Options

```yaml
plugins:
  - material/offline:
      enabled: !ENV [CI, false]        # Enable in production
      offline: true                    # Enable offline functionality
      offline_on_serve: false          # Disable during development
```

**Why `offline_on_serve: false`?**

- Development servers change frequently
- Service workers cache aggressively
- Can interfere with live reloading
- Better to test offline functionality in production builds

## Progressive Web App Features

### 1. Web App Manifest

The offline plugin automatically generates a `manifest.json`:

```json
{
  "name": "Your Documentation Site",
  "short_name": "Docs",
  "description": "Comprehensive documentation site",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#2563eb",
  "icons": [
    {
      "src": "assets/images/icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "assets/images/icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```

### 2. Custom PWA Configuration

Enhance the PWA experience with custom configuration:

```yaml
# mkdocs.yml
extra:
  pwa:
    name: "Documentation Hub"
    short_name: "Docs"
    description: "Your comprehensive documentation resource"
    theme_color: "#2563eb"
    background_color: "#ffffff"
    display: "standalone"
    orientation: "portrait"
    scope: "/"
    start_url: "/"
```

### 3. PWA Icons

Create PWA icons in multiple sizes:

```bash
# Create icon directory
mkdir -p docs/assets/images/icons

# Required icon sizes for PWA
# 192x192 - Android home screen
# 512x512 - Android splash screen
# 180x180 - iOS home screen (apple-touch-icon)
# 32x32   - Browser favicon
# 16x16   - Browser favicon
```

## Service Worker Functionality

### 1. Automatic Caching Strategy

The offline plugin implements intelligent caching:

```javascript
// Automatic service worker features:
// - Cache-first strategy for static assets
// - Network-first strategy for HTML pages
// - Stale-while-revalidate for API calls
// - Background sync for form submissions
```

### 2. Cache Management

```yaml
# Configure caching behavior
extra:
  offline:
    cache_strategy: "cache-first"     # or "network-first"
    cache_max_age: 86400             # 24 hours in seconds
    cache_max_entries: 100           # Maximum cached pages
    precache_assets: true            # Precache critical assets
```

### 3. Custom Service Worker

For advanced use cases, extend the service worker:

```javascript
// docs/assets/js/sw-custom.js
self.addEventListener('install', function(event) {
  console.log('Custom service worker installing...');

  // Custom installation logic
  event.waitUntil(
    caches.open('custom-cache-v1').then(function(cache) {
      return cache.addAll([
        '/offline.html',
        '/assets/css/offline.css'
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
  // Custom fetch handling
  if (event.request.url.includes('/api/')) {
    event.respondWith(
      fetch(event.request).catch(function() {
        return new Response('Offline - API unavailable');
      })
    );
  }
});
```

## Offline User Experience

### 1. Offline Indicator

Add visual feedback for offline status:

```css
/* Offline indicator styling */
.offline-indicator {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background: #ef4444;
  color: white;
  text-align: center;
  padding: 0.5rem;
  z-index: 1000;
  transform: translateY(-100%);
  transition: transform 0.3s ease;
}

.offline-indicator.show {
  transform: translateY(0);
}
```

```javascript
// Offline detection
window.addEventListener('online', function() {
  document.querySelector('.offline-indicator').classList.remove('show');
});

window.addEventListener('offline', function() {
  document.querySelector('.offline-indicator').classList.add('show');
});
```

### 2. Offline Page

Create a custom offline fallback page:

```html
<!-- docs/offline.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Offline - Documentation</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, sans-serif;
      text-align: center;
      padding: 2rem;
      background: #f8fafc;
    }
    .offline-message {
      max-width: 400px;
      margin: 0 auto;
      background: white;
      padding: 2rem;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
<body>
  <div class="offline-message">
    <h1>📶 You're Offline</h1>
    <p>This page isn't available offline yet. Try visiting it while online first, then it will be cached for offline viewing.</p>
    <button onclick="window.history.back()">Go Back</button>
  </div>
</body>
</html>
```

### 3. Cache Status Display

Show users which pages are available offline:

```javascript
// Display cached pages
async function showCachedPages() {
  if ('caches' in window) {
    const cacheNames = await caches.keys();
    const cache = await caches.open(cacheNames[0]);
    const cachedRequests = await cache.keys();

    const cachedPages = cachedRequests
      .map(req => req.url)
      .filter(url => url.endsWith('.html'))
      .map(url => new URL(url).pathname);

    console.log('Pages available offline:', cachedPages);
  }
}
```

## Mobile App Experience

### 1. Install Prompt

Encourage users to install your PWA:

```javascript
// PWA install prompt
let deferredPrompt;

window.addEventListener('beforeinstallprompt', function(e) {
  // Prevent Chrome 67 and earlier from automatically showing the prompt
  e.preventDefault();

  // Stash the event so it can be triggered later
  deferredPrompt = e;

  // Show custom install button
  showInstallButton();
});

function showInstallButton() {
  const installButton = document.createElement('button');
  installButton.textContent = '📱 Install App';
  installButton.className = 'install-button';
  installButton.onclick = function() {
    // Show the prompt
    deferredPrompt.prompt();

    // Wait for the user to respond to the prompt
    deferredPrompt.userChoice.then(function(choiceResult) {
      if (choiceResult.outcome === 'accepted') {
        console.log('User accepted the install prompt');
      }
      deferredPrompt = null;
    });
  };

  document.body.appendChild(installButton);
}
```

### 2. App-like Navigation

Enhance mobile navigation for app-like feel:

```css
/* App-like mobile navigation */
@media (display-mode: standalone) {
  /* Styles when running as PWA */
  .md-header {
    padding-top: env(safe-area-inset-top);
  }

  .md-container {
    padding-bottom: env(safe-area-inset-bottom);
  }

  /* Hide browser UI elements */
  .md-header__source {
    display: none;
  }
}

/* iOS Safari specific */
@supports (-webkit-touch-callout: none) {
  .md-header {
    padding-top: max(env(safe-area-inset-top), 20px);
  }
}
```

### 3. Splash Screen

Configure splash screen for better app experience:

```html
<!-- In head section -->
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Docs">

<!-- iOS splash screens -->
<link rel="apple-touch-startup-image" href="/assets/images/splash-2048x2732.png" media="(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2)">
<link rel="apple-touch-startup-image" href="/assets/images/splash-1668x2224.png" media="(device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2)">
```

## Performance Optimization

### 1. Critical Resource Preloading

```html
<!-- Preload critical resources -->
<link rel="preload" href="/assets/css/main.css" as="style">
<link rel="preload" href="/assets/js/main.js" as="script">
<link rel="preload" href="/assets/fonts/roboto.woff2" as="font" type="font/woff2" crossorigin>
```

### 2. Lazy Loading Implementation

```javascript
// Lazy load non-critical content
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      img.classList.remove('lazy');
      observer.unobserve(img);
    }
  });
});

document.querySelectorAll('img[data-src]').forEach(img => {
  observer.observe(img);
});
```

### 3. Cache Optimization

```yaml
# Optimize caching strategy
extra:
  offline:
    # Cache static assets aggressively
    static_cache_max_age: 31536000  # 1 year

    # Cache HTML pages for shorter periods
    page_cache_max_age: 86400       # 1 day

    # Limit cache size to prevent storage issues
    cache_max_size: 50              # 50MB
    cache_max_entries: 200          # 200 pages
```

## Testing Offline Functionality

### 1. Development Testing

```bash
# Build for production
mkdocs build

# Serve built site
cd site && python -m http.server 8000

# Test offline functionality:
# 1. Visit pages while online
# 2. Disconnect network
# 3. Navigate to cached pages
# 4. Verify offline experience
```

### 2. Browser DevTools Testing

```javascript
// Test service worker in DevTools
// 1. Open DevTools → Application → Service Workers
// 2. Check "Offline" checkbox
// 3. Navigate through site
// 4. Verify cached resources in Cache Storage
```

### 3. Lighthouse PWA Audit

```bash
# Install Lighthouse CLI
npm install -g lighthouse

# Run PWA audit
lighthouse http://localhost:8000 --view --preset=pwa

# Check for:
# - Service worker registration
# - Web app manifest
# - Offline functionality
# - Install prompts
```

## Deployment Considerations

### 1. HTTPS Requirement

PWAs require HTTPS in production:

```yaml
# Ensure HTTPS in production
site_url: https://yourdomain.com  # Must be HTTPS
```

### 2. Service Worker Scope

Configure service worker scope properly:

```javascript
// Service worker registration
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js', {
    scope: '/'  // Ensure correct scope
  });
}
```

### 3. Cache Invalidation

Handle cache updates properly:

```javascript
// Handle service worker updates
navigator.serviceWorker.addEventListener('controllerchange', function() {
  // Reload page when new service worker takes control
  window.location.reload();
});
```

## Troubleshooting

### Common Issues

**Service worker not registering:**

```javascript
// Check for HTTPS requirement
if (location.protocol !== 'https:' && location.hostname !== 'localhost') {
  console.warn('Service workers require HTTPS');
}
```

**Pages not caching:**

```javascript
// Check cache storage in DevTools
caches.keys().then(console.log);
```

**Install prompt not showing:**

```javascript
// Check PWA criteria
// - HTTPS
// - Web app manifest
// - Service worker
// - User engagement signals
```

### Debug Service Worker

```javascript
// Service worker debugging
navigator.serviceWorker.getRegistrations().then(function(registrations) {
  console.log('Active service workers:', registrations);
});

// Check cache contents
caches.open('mkdocs-offline').then(function(cache) {
  cache.keys().then(function(keys) {
    console.log('Cached resources:', keys.map(k => k.url));
  });
});
```

## Best Practices

### 1. Progressive Enhancement

- **Start with basic functionality** that works without JavaScript
- **Layer on PWA features** for enhanced experience
- **Graceful degradation** for unsupported browsers

### 2. Cache Strategy

- **Cache critical pages** immediately after first visit
- **Lazy cache** less important content
- **Regular cleanup** of old cache entries
- **Respect storage quotas** to avoid eviction

### 3. User Communication

- **Clear offline indicators** when network is unavailable
- **Cache status feedback** showing what's available offline
- **Install prompts** at appropriate moments
- **Update notifications** when new content is available

---

_Offline functionality transforms your documentation into a reliable resource that works anywhere, anytime._
