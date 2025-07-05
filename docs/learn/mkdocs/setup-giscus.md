# Setting up Giscus Comments

This guide explains how to set up and configure Giscus comments for your MkDocs Material site.

## Overview

Giscus is a comments system powered by GitHub Discussions. It's privacy-friendly, free, and integrates seamlessly with MkDocs Material.

## Current Configuration Status

✅ **Giscus is fully configured** in this repository with:

- **Repository**: ks-sbc/DRUIDS
- **Category**: General Discussions
- **Theme**: Auto-syncs with Material theme
- **Position**: Comments at top
- **Reactions**: Enabled

## How It Works

1. Pages with `comments: true` in frontmatter show comments
2. Comments are stored as GitHub Discussions
3. Users need a GitHub account to comment
4. Theme automatically syncs with site theme (light/dark)

## Setup Instructions

### Step 1: Enable GitHub Discussions

1. Go to your GitHub repository
2. Click **Settings** → **Features**
3. Check **Discussions**

### Step 2: Configure Giscus

1. Visit [giscus.app](https://giscus.app)
2. Enter your repository: `username/repository-name`
3. Configure settings:
   - **Mapping**: `pathname` (recommended)
   - **Category**: Create or select (e.g., "General")
   - **Theme**: `preferred_color_scheme`
   - **Features**: Enable reactions

### Step 3: Get Configuration Values

From giscus.app, copy:
- Repository ID
- Category ID

### Step 4: Update MkDocs Configuration

In `mkdocs.yml`:

```yaml
extra:
  comments:
    enabled: true
    provider: giscus
    giscus:
      repo: username/repository
      repo-id: "YOUR_REPO_ID"
      category: General
      category-id: "YOUR_CATEGORY_ID"
      mapping: pathname
      strict: 0
      reactions: 1
      emit-metadata: 0
      input-position: top
      theme: preferred_color_scheme
      lang: en
      loading: lazy
```

### Step 5: Enable Comments on Pages

Add to page frontmatter:

```yaml
---
comments: true
---
```

## File Structure

The integration requires these files:

```
overrides/
└── partials/
    └── comments.html    # Giscus integration

docs/
├── assets/
│   ├── css/
│   │   └── giscus.css  # Comment styling
│   └── js/
│       └── giscus.js   # Theme sync
└── giscus.json         # Security config
```

## Features

✅ **Automatic theme switching** - Syncs with Material theme  
✅ **Responsive design** - Works on all devices  
✅ **Privacy-friendly** - No tracking  
✅ **Moderation tools** - Via GitHub  
✅ **Reactions** - Users can react  
✅ **Notifications** - Via GitHub

## Customization

### Styling

Edit `docs/assets/css/giscus.css`:

```css
.giscus {
  max-width: 100%;
  margin: 2rem 0;
}

.giscus-frame {
  border: none;
  width: 100%;
}
```

### Theme Synchronization

The theme automatically syncs via JavaScript in `comments.html`:

```javascript
function updateGiscusTheme() {
  const theme = document.body.getAttribute('data-md-color-scheme');
  // Theme update logic
}
```

## Security Configuration

Create `giscus.json` in your docs root:

```json
{
  "origins": [
    "https://yourdomain.com",
    "http://localhost:8000"
  ]
}
```

## Troubleshooting

### Comments Not Appearing

1. Verify GitHub Discussions is enabled
2. Check repository is public
3. Confirm configuration values are correct
4. Look for console errors

### Theme Not Syncing

- Ensure Material theme palette is configured
- Check JavaScript is loading correctly
- Clear browser cache

### Testing Locally

```bash
# Start dev server
mkdocs serve

# Visit a page with comments: true
# Try commenting (requires GitHub login)
```

## Best Practices

1. **Moderate regularly** - Check GitHub Discussions
2. **Set guidelines** - Create discussion guidelines
3. **Enable reactions** - Encourage engagement
4. **Test thoroughly** - Before deploying

## Next Steps

- Test comments on a page with `comments: true`
- Customize styling if needed
- Set up moderation guidelines
- Monitor GitHub Discussions
