# Setting up Giscus Comments

This guide will help you set up Giscus comments for your MkDocs Material site.

## Prerequisites

1. A public GitHub repository
2. GitHub Discussions enabled on your repository
3. The Giscus app installed on your repository

## Step 1: Enable GitHub Discussions

1. Go to your GitHub repository
2. Click on **Settings**
3. Scroll down to **Features**
4. Check **Discussions**

## Step 2: Install Giscus App

1. Visit [giscus.app](https://giscus.app)
2. Enter your repository in the format `username/repository-name`
3. Choose your preferred settings:
   - **Page ↔️ Discussions Mapping**: `pathname` (recommended)
   - **Discussion Category**: Choose or create a category (e.g., "General")
   - **Features**: Enable reactions and metadata as desired
   - **Theme**: `preferred_color_scheme` (automatically matches your site theme)

## Step 3: Get Your Configuration

After configuring on giscus.app, you'll get:
- Repository ID (`data-repo-id`)
- Category ID (`data-category-id`)

## Step 4: Set Environment Variables

Add these to your `.envrc` file or environment:

```bash
export GISCUS_REPO_ID="your-repo-id-here"
export GISCUS_CATEGORY_ID="your-category-id-here"
```

## Step 5: Update Repository Information

In `mkdocs.yml`, update the repository information:

```yaml
repo_name: yourusername/your-actual-repo
repo_url: https://github.com/yourusername/your-actual-repo

extra:
  comments:
    enabled: true
    provider: giscus
    giscus:
      repo: yourusername/your-actual-repo  # Update this
      repo-id: !ENV [GISCUS_REPO_ID, '']
      category: General  # Update if different
      category-id: !ENV [GISCUS_CATEGORY_ID, '']
      # ... other settings are already configured
```

## Step 6: Enable Comments on Pages

Add this to the front matter of pages where you want comments:

```yaml
---
comments: true
---
```

Or enable globally by adding to your page templates.

## Features Included

✅ **Automatic theme switching** - Comments theme matches your site theme  
✅ **Responsive design** - Works on all device sizes  
✅ **Privacy-friendly** - No tracking, uses GitHub authentication  
✅ **Moderation** - Use GitHub's moderation tools  
✅ **Reactions** - Readers can react to discussions  
✅ **Notifications** - Get notified of new comments via GitHub  

## Troubleshooting

### Comments not showing up?
1. Check that GitHub Discussions is enabled
2. Verify your repository is public
3. Ensure environment variables are set correctly
4. Check browser console for errors

### Theme not switching?
The JavaScript automatically handles theme switching. If it's not working, check that the Material theme palette is properly configured.

### Want to customize the appearance?
Edit `docs/assets/css/giscus.css` to customize the styling.

## Security Notes

- Comments are hosted by GitHub and subject to their terms of service
- Users must have a GitHub account to comment
- Repository owners can moderate comments through GitHub Discussions
- No personal data is stored on your site