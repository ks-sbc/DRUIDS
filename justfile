# DRUIDS MkDocs Project Justfile
# Democratic Revolutionary Unified Information & Documentation System

# =============================================================================
# HELP & INFO
# =============================================================================

# Show available commands with descriptions
default:
    @just --list

# Show detailed help with examples
help:
    @echo "📚 DRUIDS MkDocs Project Commands"
    @echo ""
    @echo "🚀 Quick Start:"
    @echo "  just init          # Initialize project after cloning"
    @echo "  just serve         # Start development server"
    @echo "  just watch         # Watch for changes and auto-rebuild"
    @echo ""
    @echo "🔍 Testing & Validation:"
    @echo "  just test                # Run all pytest tests"
    @echo "  just test-comprehensive  # Run complete test suite"
    @echo "  just test-links         # Test link validation"
    @echo "  just test-build-quality # Test build warnings"
    @echo "  just test-static        # Test static analysis"
    @echo "  just test-structure     # Test content structure"
    @echo ""
    @echo "🏗️  Building:"
    @echo "  just build         # Build documentation with strict mode"
    @echo "  just build-dev     # Build without strict mode"
    @echo "  just dev-check     # Quick development validation"
    @echo ""
    @echo "✨ Formatting:"
    @echo "  just format        # Format all files"
    @echo "  just lint          # Check formatting"
    @echo ""
    @echo "🚀 Deployment:"
    @echo "  just deploy        # Deploy to GitHub Pages"
    @echo ""
    @echo "🔧 Maintenance:"
    @echo "  just clean         # Clean build artifacts"
    @echo "  just stats         # Show project statistics"

# =============================================================================
# PROJECT SETUP
# =============================================================================

# Install all dependencies
install:
    @echo "📦 Installing dependencies..."
    pip install -r dependencies/requirements.txt
    pip install pytest yamllint pre-commit
    npm install
    pre-commit install --config config/.pre-commit-config.yaml

# Initialize project (run once after cloning)
init:
    @echo "🚀 Initializing DRUIDS project..."
    just install
    @echo "✅ Project initialized! Run 'just serve' to start development server."

# =============================================================================
# DEVELOPMENT
# =============================================================================

# Start development server (default: localhost:8000)
serve:
    @echo "🌐 Starting development server..."
    mkdocs serve

# Watch for changes and auto-rebuild
watch:
    @echo "👀 Watching for changes..."
    watchexec -e md,yml,yaml,html,css,js -- just dev-check

# Quick development check (validates and builds)
dev-check:
    @echo "🚀 Running quick development checks..."
    python tests/validate_config.py
    python tests/validate_blog_posts.py
    mkdocs build --clean

# =============================================================================
# TESTING & VALIDATION
# =============================================================================

# Run all validation checks
validate:
    @echo "🔍 Running validation checks..."
    @echo "  Validating YAML files..."
    yamllint -c config/.yamllint.yml mkdocs.yml
    @echo "  Validating MkDocs configuration..."
    python tests/validate_config.py
    @echo "  Validating blog posts..."
    python tests/validate_blog_posts.py

# Run pytest tests
test:
    @echo "🧪 Running pytest..."
    pytest tests/ -v

# Test build quality and link validation
test-links:
    @echo "🔗 Testing link validation..."
    pytest tests/test_build_quality.py tests/test_links.py -v

# Test static analysis of markdown
test-static:
    @echo "📝 Running static analysis tests..."
    pytest tests/test_static_analysis.py -v

# Test content structure (Diátaxis compliance)
test-structure:
    @echo "📚 Testing content structure..."
    pytest tests/test_content_structure.py -v

# Test build warnings and quality
test-build-quality:
    @echo "⚠️  Testing build quality..."
    pytest tests/test_build_quality.py -v

# Run all new comprehensive tests
test-comprehensive: test-links test-static test-structure test-build-quality
    @echo "✅ All comprehensive tests completed!"

# Run comprehensive test suite (Python + Bash)
test-all:
    @echo "🧪 Running comprehensive test suite..."
    ./run_tests.sh

# Run all checks (validate + test + build)
check-all: validate test build
    @echo "✅ All checks completed successfully!"

# Pre-commit hook simulation
pre-commit-check:
    @echo "🔒 Running pre-commit checks..."
    pre-commit run --all-files --config config/.pre-commit-config.yaml

# =============================================================================
# BUILDING & DEPLOYMENT
# =============================================================================

# Build documentation with strict mode
build:
    @echo "🏗️  Building documentation..."
    mkdocs build --clean --strict

# Build without strict mode (for development)
build-dev:
    @echo "🏗️  Building documentation (dev mode)..."
    mkdocs build --clean

# Deploy to GitHub Pages
deploy:
    @echo "🚀 Deploying to GitHub Pages..."
    mkdocs gh-deploy --clean

# Deploy versioned documentation
deploy-version VERSION:
    @echo "🚀 Deploying version {{VERSION}}..."
    mike deploy --push --update-aliases {{VERSION}} latest

# =============================================================================
# FORMATTING & LINTING
# =============================================================================

# Format all files
format:
    @echo "✨ Formatting all files..."
    npm run format

# Format Python files
format-python:
    @echo "🐍 Formatting Python files..."
    black tests/
    isort tests/

# Format YAML files
format-yaml:
    @echo "📄 Formatting YAML files..."
    npx prettier --write "**/*.{yml,yaml}"

# Format Markdown files
format-markdown:
    @echo "📝 Formatting Markdown files..."
    npx prettier --write "docs/**/*.md"

# Format JSON files
format-json:
    @echo "📋 Formatting JSON files..."
    npx prettier --write "**/*.json"

# Check formatting
lint:
    @echo "🔍 Checking formatting..."
    npm run format:check

# =============================================================================
# CONTENT MANAGEMENT
# =============================================================================

# Create new blog post
new-post TITLE:
    @echo "📝 Creating new blog post: {{TITLE}}"
    #!/bin/bash
    set -euo pipefail
    DATE=$(date +%Y-%m-%d)
    SLUG=$(echo "{{TITLE}}" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd '[:alnum:]-')
    FILENAME="docs/blog/posts/${DATE}-${SLUG}.md"
    
    cat > "${FILENAME}" << EOF
    ---
    title: "{{TITLE}}"
    description: ""
    date: ${DATE}
    categories:
      - General
    tags:
      - 
    draft: true
    ---
    
    # {{TITLE}}
    
    Content goes here...
    EOF
    
    echo "Created: ${FILENAME}"

# Validate specific blog post
validate-post FILE:
    @echo "🔍 Validating blog post: {{FILE}}"
    python tests/validate_blog_posts.py {{FILE}}

# Check for broken links (requires linkchecker)
check-links:
    @echo "🔗 Checking for broken links..."
    echo "Starting MkDocs server..."
    mkdocs serve --dev-addr=127.0.0.1:8000 &
    SERVER_PID=$!
    sleep 5
    echo "Running linkchecker..."
    linkchecker http://127.0.0.1:8000 --check-extern || true
    echo "Stopping server..."
    kill $SERVER_PID

# =============================================================================
# MAINTENANCE & UTILITIES
# =============================================================================

# Clean build artifacts and caches
clean:
    @echo "🧹 Cleaning build artifacts..."
    rm -rf site/
    rm -rf test_site/
    find . -name "*.pyc" -delete
    find . -name "__pycache__" -delete

# Update dependencies
update:
    @echo "⬆️  Updating dependencies..."
    pip install --upgrade -r dependencies/requirements.txt
    npm update

# Show project statistics
stats:
    @echo "📊 Project Statistics:"
    @echo "  Lines of documentation: $(find docs -name '*.md' -exec wc -l {} + | tail -1 | awk '{print $1}')"
    @echo "  Blog posts: $(find docs/blog/posts -name '*.md' | wc -l)"
    @echo "  Pages: $(find docs -name '*.md' -not -path 'docs/blog/*' | wc -l)"
    @echo "  Templates: $(find overrides -name '*.html' 2>/dev/null | wc -l || echo 0)"
    @echo "  Assets: $(find docs -name '*.css' -o -name '*.js' -o -name '*.png' -o -name '*.jpg' -o -name '*.svg' | wc -l)"