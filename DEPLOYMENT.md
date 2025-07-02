# GitHub Pages Deployment

This repository is configured for automated deployment to GitHub Pages using the DRUIDS branch.

## Setup Instructions

1. **Enable GitHub Pages** in your repository settings:
   - Go to Settings > Pages
   - Source: Deploy from a branch
   - Branch: `DRUIDS` / `root`

2. **Create DRUIDS branch** (if not exists):
   ```bash
   git checkout -b DRUIDS
   git push origin DRUIDS
   ```

## Deployment Process

### Automatic Deployment
The site automatically deploys when you push to the DRUIDS branch:
```bash
git checkout DRUIDS
git merge main
git push origin DRUIDS
```

### Manual Deployment
Run the deployment script:
```bash
python scripts/deploy_to_github_pages.py
```

## Testing

Run deployment tests:
```bash
python -m pytest tests/test_github_pages_deployment.py -v
```

## Workflow Details

The GitHub Actions workflow (`.github/workflows/deploy-to-github-pages.yml`) handles:
- Building the MkDocs site
- Creating required GitHub Pages files (.nojekyll)
- Deploying to GitHub Pages environment

## URLs

Once deployed, your site will be available at:
- `https://<username>.github.io/<repository-name>/`
- Or your custom domain if configured