#!/bin/bash

# Setup script for Giscus integration

echo "🔧 Giscus Setup Script"
echo "====================="
echo ""
echo "This script will help you configure Giscus for your MkDocs site."
echo ""
echo "Prerequisites:"
echo "1. Your GitHub repository must be public"
echo "2. GitHub Discussions must be enabled"
echo "3. You need to visit https://giscus.app to get your repo and category IDs"
echo ""
echo "Press Enter to continue..."
read

# Get repository information
echo "Enter your GitHub repository (format: username/repo-name):"
read REPO

echo "Enter your Giscus repository ID (from giscus.app):"
read REPO_ID

echo "Enter your Giscus category ID (from giscus.app):"
read CATEGORY_ID

# Update mkdocs.yml
echo ""
echo "Updating mkdocs.yml..."

# Create a backup
cp mkdocs.yml mkdocs.yml.backup

# Update the configuration
sed -i "s|repo: yourusername/your-repo|repo: $REPO|g" mkdocs.yml
sed -i "s|repo_id: R_placeholder|repo_id: $REPO_ID|g" mkdocs.yml
sed -i "s|category_id: DIC_placeholder|category_id: $CATEGORY_ID|g" mkdocs.yml

# Update giscus.json with the repository URL
DOMAIN=$(echo $REPO | sed 's/\//\./g')
sed -i "s|yourdomain.com|$DOMAIN.github.io|g" docs/giscus.json

echo "✅ Configuration updated!"
echo ""
echo "Next steps:"
echo "1. Build your site: mkdocs build"
echo "2. Test locally: mkdocs serve"
echo "3. Visit a page with 'comments: true' in the front matter"
echo "4. Deploy to GitHub Pages"
echo ""
echo "To enable comments on a page, add this to the front matter:"
echo "---"
echo "comments: true"
echo "---"