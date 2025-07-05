# CLAUDE.md - Web Design Worktree

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the DRUIDS (Democratic Revolutionary Unified Information & Documentation System) MkDocs project - a secure, privacy-respecting documentation system built with MkDocs Material featuring a Mandalorian tactical aesthetic and GitHub Discussions-based commenting.

## IMPORTANT: Web Design Worktree Instructions

**This is the WEB DESIGN worktree** - Focus on CSS and visual improvements

### Critical Instructions for Visual Testing

**ALWAYS inspect the actual HTML output:**
1. Build the site: `mkdocs build --clean`
2. **Check the `site/` directory for the generated HTML**
3. Open HTML files directly in browser: `firefox site/index.html`
4. Use browser DevTools to inspect actual rendered CSS

**DO NOT rely only on `mkdocs serve`** - The built HTML in `site/` shows the final output.

### Visual Testing Workflow

```bash
# Build site to generate HTML
mkdocs build --clean

# Open the built site
firefox site/index.html

# Or use Python's simple server for the built site
cd site && python -m http.server 8001

# For live CSS testing with actual HTML
mkdocs build --clean && cd site && python -m http.server 8001
```

### CSS Development Focus

**Primary Goals**:
1. Fix header layout issues (reduce height, remove redundancy)
2. Optimize typography (responsive font sizes, better readability)
3. Improve mobile responsiveness
4. Enhance color contrast for accessibility
5. Clean up spacing and alignment

**Key CSS Files**:
- `docs/assets/css/druids-layout.css` - Header, footer, main layout
- `docs/assets/css/druids-theme.css` - Colors, typography, base styles
- `docs/assets/css/druids-components.css` - Specific components
- `docs/assets/css/druids-utilities.css` - Helper classes

### Browser DevTools Tips

1. **Inspect actual computed styles** in the built HTML
2. **Test responsive breakpoints** using device emulation
3. **Check color contrast** using accessibility tools
4. **Measure actual sizes** with ruler/measurement tools
5. **Test with different zoom levels** (100%, 150%, 200%)

### Visual Issues to Fix

Based on the screenshot:
- Header bar too tall with excess padding
- Redundant "DRUIDS Wiki" text in multiple places
- Search box positioning/sizing issues
- Excessive spacing between sections
- Font sizes need fluid responsive scaling
- Color contrast improvements needed

## Key Commands

### Development

```bash
# Install dependencies and initialize project
just init

# Start development server (default: localhost:8000)
just serve
mkdocs serve

# Watch for changes and auto-rebuild
just watch

# Quick development check (validates and builds)
just dev-check
```

### Building

```bash
# Build documentation with strict mode
just build
mkdocs build --clean --strict

# Build without strict mode (for development)
just build-dev
mkdocs build --clean
```

### Testing and Validation

```bash
# Run all tests (Python + Bash)
just test-all
./run_tests.sh

# Run Python tests only
just test
pytest tests/ -v

# Run specific test
pytest tests/test_mkdocs_config.py -v

# Validate YAML and configuration
just validate
yamllint -c .yamllint.yml mkdocs.yml
python tests/validate_config.py
python tests/validate_blog_posts.py

# Run all checks (validate + test + build)
just check-all

# Pre-commit checks
just pre-commit-check
pre-commit run --all-files
```

### Formatting and Linting

```bash
# Format all files
just format
npm run format

# Format specific types
just format-python    # Black + isort
just format-yaml      # Prettier
just format-markdown  # Prettier
just format-json      # Prettier

# Check formatting
just lint
npm run format:check
```

### Content Management

```bash
# Create new blog post
just new-post "Title of Post"

# Check for broken links
just check-links

# Show project statistics
just stats
```

### Deployment

```bash
# Deploy to GitHub Pages
just deploy
mkdocs gh-deploy --clean

# Deploy versioned documentation
just deploy-version 1.0
```

## Project Architecture

### Core Structure

- **MkDocs Material Theme**: Modern responsive documentation framework
- **Justfile**: Primary task runner for all development workflows
- **pytest**: Python testing framework for configuration and validation
- **npm/prettier**: Code formatting for YAML, Markdown, JSON files
- **Black/isort**: Python code formatting

### Key Directories

- `docs/`: All documentation content
  - `blog/posts/`: Blog posts in Markdown
  - `tutorials/`, `reference/`, `how-to/`: Diátaxis-structured documentation
- `overrides/`: Custom MkDocs Material theme overrides
- `assets/`: Static assets (CSS, JS, images, fonts)
- `tests/`: Python test suite
- `scripts/`: Bash automation scripts
- `hooks/`: MkDocs hooks for advanced functionality

### Configuration Files

- `mkdocs.yml`: Main MkDocs configuration
- `config/pyproject.toml`: Python tooling configuration (Black, isort, pytest)
- `dependencies/package.json`: Node.js dependencies and scripts
- `dependencies/requirements.txt`: Python dependencies
- `justfile`: Task automation

### Testing Infrastructure

The project uses a two-tier testing approach:

1. **Python tests** (`pytest`): Validate MkDocs configuration, blog posts, and content structure
2. **Bash tests** (`test_build.sh`): Test actual site building and deployment

Test files:

- `tests/test_mkdocs_config.py`: Configuration validation
- `tests/validate_config.py`: YAML and structure validation
- `tests/validate_blog_posts.py`: Blog post frontmatter validation
- `tests/test_build.sh`: Build process testing

### Key Features Implementation

1. **Giscus Comments**: Configured in `mkdocs.yml` under `extra.comments`
2. **Mandalorian Theme**: Custom CSS in `assets/stylesheets/`
3. **Security Indicators**: Visual L0/L1/L2 content markers
4. **Blog System**: MkDocs Material blog plugin with categories and archive
5. **Git Integration**: Revision dates, edit links, GitHub integration

### Development Workflow

1. Make changes to documentation or code
2. Run `just dev-check` for quick validation
3. Use `just serve` to preview changes locally
4. Run `just check-all` before committing
5. Use `just deploy` to publish to GitHub Pages

### Important Notes

- The project uses environment variables for sensitive data (GISCUS_REPO_ID, GOOGLE_ANALYTICS_KEY)
- Blog posts require specific frontmatter structure (see `tests/validate_blog_posts.py`)
- All Markdown files should follow the project's formatting standards (enforced by Prettier)
- The project follows Diátaxis documentation framework for content organization

## Development Best Practices

- **Commit Guidelines**:
  - ALWAYS commit your work regularly
  - ALWAYS use the KS-SBC version of conventional commit
  - NEVER EVER mention an AI in the commit message