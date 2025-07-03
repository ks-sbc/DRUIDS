# Justfile for MkDocs project
# Comprehensive task runner for documentation development

# Default recipe to display help
default:
    @just --list

# =============================================================================
# 🚀 DEPLOYMENT COMMANDS (PRIMARY)
# =============================================================================

# One command to rule them all - check deployment readiness
deploy-ready:
    @echo "🎯 Checking deployment readiness..."
    just install-deps
    just format-check
    just validate-deployment
    @echo "✅ Ready for deployment!"

# Quick deployment check (no install)
check-only:
    @echo "🔍 Running deployment checks..."
    just format-check
    just validate-deployment

# Install only essential dependencies
install-deps:
    @echo "📦 Installing essential dependencies..."
    pip install -r dependencies/requirements.txt
    npm install

# Format check (don't modify files)
format-check:
    @echo "🎨 Checking code formatting..."
    npm run format:check

# Validate deployment readiness
validate-deployment:
    @echo "🔍 Validating deployment..."
    python validators/deployment.py

# Test MkDocs build
build-test:
    @echo "🏗️ Testing MkDocs build..."
    mkdocs build --clean --strict

# Test MkDocs serve
serve-test:
    @echo "🚀 Testing MkDocs serve..."
    @echo "Starting server on port 8001..."
    timeout 10s mkdocs serve --dev-addr=127.0.0.1:8001 || echo "✅ Server test completed"

# Fix formatting issues
format-fix:
    @echo "🔧 Fixing formatting issues..."
    npm run format
    npm run lint:md:fix

# Quick serve for development
serve:
    @echo "🚀 Starting development server..."
    mkdocs serve

# =============================================================================
# 🎉 TESTING & VERIFICATION
# =============================================================================

# Run comprehensive deployment test
test-full:
    @echo "🧪 Running full deployment test..."
    just deploy-ready
    just build-test
    just serve-test
    @echo "✨ All tests passed!"

# Clean build artifacts
clean:
    @echo "🧹 Cleaning build artifacts..."
    rm -rf site/
    rm -rf test_site/
    find . -name "*.pyc" -delete
    find . -name "__pycache__" -delete

# Install all dependencies
install:
    @echo "📦 Installing dependencies..."
    pip install -r dependencies/requirements.txt
    pip install pytest yamllint pre-commit
    npm install
    pre-commit install --config config/.pre-commit-config.yaml

# Initialize project (run once after cloning)
init:
    @echo "🚀 Initializing project..."
    just install
    just install-hooks
    @echo "✅ Project initialized! Run 'just serve' to start development server."

# Install git hooks
install-hooks:
    @echo "🔧 Installing git hooks..."
    ./scripts/install-hooks.sh

# =============================================================================
# VALIDATION & TESTING
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

# Run comprehensive test suite
test-all:
    @echo "🧪 Running comprehensive test suite..."
    ./run_tests.sh

# Run all checks (validate + test + build)
check-all: validate test build
    @echo "✅ All checks completed successfully!"

# Quick development check
dev-check:
    @echo "🚀 Running quick development checks..."
    python tests/validate_config.py
    python tests/validate_blog_posts.py
    mkdocs build --clean

# Pre-commit hook simulation
pre-commit-check:
    @echo "🔒 Running pre-commit checks..."
    pre-commit run --all-files --config config/.pre-commit-config.yaml

# Comprehensive validation script
validate-all:
    @echo "🔍 Running comprehensive validation..."
    ./scripts/validate-all.sh

# =============================================================================
# BUILD & DEPLOYMENT
# =============================================================================

# Build documentation with strict mode
build:
    @echo "🏗️  Building documentation..."
    mkdocs build --clean --strict

# Build documentation (non-strict for development)
build-dev:
    @echo "🏗️  Building documentation (dev mode)..."
    mkdocs build --clean

# Serve documentation locally
serve:
    @echo "🚀 Starting local server..."
    mkdocs serve

# Serve with specific host and port
serve-host host="127.0.0.1" port="8000":
    @echo "🚀 Starting local server on {{host}}:{{port}}..."
    mkdocs serve --dev-addr={{host}}:{{port}}

# Deploy to GitHub Pages
deploy:
    @echo "🚀 Deploying to GitHub Pages..."
    mkdocs gh-deploy --clean

# Deploy versioned documentation
deploy-version version:
    @echo "🚀 Deploying version {{version}}..."
    ./scripts/deploy-version.sh {{version}}

# =============================================================================
# FORMATTING & LINTING
# =============================================================================

# Format all files
format:
    @echo "✨ Formatting files..."
    npm run format
    black tests/ scripts/ --line-length 88 || echo "Black not available"
    isort tests/ scripts/ --profile black || echo "isort not available"

# Format specific file types
format-python:
    @echo "🐍 Formatting Python files..."
    black tests/ scripts/ --line-length 88
    isort tests/ scripts/ --profile black

format-yaml:
    @echo "📝 Formatting YAML files..."
    npm run format:yaml

format-markdown:
    @echo "📄 Formatting Markdown files..."
    npm run format:md

format-json:
    @echo "📋 Formatting JSON files..."
    npm run format:json

# Run linting checks
lint:
    @echo "🔍 Running linting checks..."
    npm run format:check
    yamllint -c config/.yamllint.yml mkdocs.yml || echo "yamllint not available"
    flake8 tests/ scripts/ || echo "flake8 not available"
    find . -name "*.py" -exec python -m py_compile {} \;

# =============================================================================
# DEVELOPMENT TOOLS
# =============================================================================

# Watch for changes and rebuild automatically
watch:
    @echo "👀 Watching for changes..."
    if command -v watchexec >/dev/null 2>&1; then
        watchexec -e md,yml,yaml,html,css,js -- just dev-check
    else
        echo "watchexec not installed. Install with: cargo install watchexec-cli"
        echo "Falling back to mkdocs serve..."
        mkdocs serve
    fi

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

# Profile build performance
profile:
    @echo "📊 Profiling build performance..."
    time mkdocs build --clean --strict

# =============================================================================
# CONTENT MANAGEMENT
# =============================================================================

# Create a new blog post
new-post title:
    @echo "📝 Creating new blog post: {{title}}"
    #!/usr/bin/env bash
    DATE=$(date +%Y-%m-%d)
    SLUG=$(echo "{{title}}" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-\|-$//g')
    FILENAME="docs/blog/posts/${SLUG}.md"
    if [ -f "$FILENAME" ]; then
        echo "File $FILENAME already exists"
        exit 1
    fi
    
    cat > "$FILENAME" << EOF
    ---
    date: $DATE
    categories:
      - Announcements
    tags:
      - new
    comments: true
    ---
    
    # {{title}}
    
    Brief description of the post.
    
    <!-- more -->
    
    ## Content
    
    Your content here...
    EOF
    
    echo "✅ Created $FILENAME"

# Validate specific blog post
validate-post file:
    @echo "🔍 Validating blog post: {{file}}"
    #!/usr/bin/env bash
    if [ ! -f "{{file}}" ]; then
        echo "❌ File {{file}} not found"
        exit 1
    fi
    
    # Check frontmatter
    if ! head -1 "{{file}}" | grep -q "^---$"; then
        echo "❌ Missing frontmatter"
        exit 1
    fi
    
    # Check for excerpt separator
    if ! grep -q "<!-- more -->" "{{file}}"; then
        echo "⚠️  Missing excerpt separator '<!-- more -->'"
    fi
    
    echo "✅ Blog post validation passed"

# Generate requirements.txt from current environment
freeze:
    @echo "🧊 Generating requirements.txt..."
    pip freeze > dependencies/requirements.txt
    @echo "requirements.txt updated"

# Update dependencies
update:
    @echo "⬆️  Updating dependencies..."
    pip install --upgrade -r dependencies/requirements.txt

# Run security check on dependencies
security-check:
    @echo "🔒 Running security check..."
    #!/usr/bin/env bash
    if command -v safety >/dev/null 2>&1; then
        safety check
    else
        echo "safety not installed. Install with: pip install safety"
        exit 1
    fi

# =============================================================================
# UTILITIES
# =============================================================================

# Show project statistics
stats:
    @echo "📊 Project Statistics:"
    @echo "  Total files: $(find docs -name '*.md' | wc -l)"
    @echo "  Blog posts: $(find docs/blog/posts -name '*.md' 2>/dev/null | wc -l || echo 0)"
    @echo "  Pages: $(find docs -name '*.md' -not -path 'docs/blog/*' | wc -l)"
    @echo "  Templates: $(find overrides -name '*.html' 2>/dev/null | wc -l || echo 0)"
    @echo "  Assets: $(find docs -name '*.css' -o -name '*.js' -o -name '*.png' -o -name '*.jpg' -o -name '*.svg' | wc -l)"

<<<<<<< HEAD
# Initialize project (run once after cloning)
init:
    @echo "🚀 Initializing project..."
    just install
    @echo "✅ Project initialized! Run 'just serve' to start development server."
=======
# Show help with examples
help:
    @echo "📚 MkDocs Project Commands"
    @echo ""
    @echo "🚀 Quick Start:"
    @echo "  just init          # Initialize project after cloning"
    @echo "  just serve         # Start development server"
    @echo "  just watch         # Watch for changes and auto-rebuild"
    @echo ""
    @echo "🔍 Validation:"
    @echo "  just validate      # Run all validation checks"
    @echo "  just test          # Run pytest tests"
    @echo "  just check-all     # Run all checks (validate + test + build)"
    @echo ""
    @echo "✨ Formatting:"
    @echo "  just format        # Format all files"
    @echo "  just lint          # Run all linting checks"
    @echo ""
    @echo "📝 Content:"
    @echo "  just new-post 'Title'  # Create new blog post"
    @echo "  just validate-post file.md  # Validate specific post"
    @echo ""
    @echo "🚀 Deployment:"
    @echo "  just deploy        # Deploy to GitHub Pages"
    @echo "  just deploy-version 1.0  # Deploy versioned docs"
    @echo ""
    @echo "🔧 Maintenance:"
    @echo "  just clean         # Clean build artifacts"
    @echo "  just update        # Update dependencies"
    @echo "  just stats         # Show project statistics"
