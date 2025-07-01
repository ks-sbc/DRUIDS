# Justfile for MkDocs project

# Default recipe to display help
default:
    @just --list

# Install dependencies
install:
    @echo "📦 Installing dependencies..."
    pip install -r requirements.txt
    pip install pytest yamllint pre-commit
    pre-commit install

# Run all validation checks
validate:
    @echo "🔍 Running validation checks..."
    @echo "  Validating YAML files..."
    yamllint -c .yamllint.yml mkdocs.yml
    @echo "  Validating MkDocs configuration..."
    python tests/validate_config.py
    @echo "  Validating blog posts..."
    python tests/validate_blog_posts.py

# Run pytest tests
test:
    @echo "🧪 Running pytest..."
    pytest tests/ -v

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

# Clean build artifacts
clean:
    @echo "🧹 Cleaning build artifacts..."
    rm -rf site/
    rm -rf test_site/
    find . -name "*.pyc" -delete
    find . -name "__pycache__" -delete

# Run linting checks
lint:
    @echo "🔍 Running linting checks..."
    yamllint -c .yamllint.yml mkdocs.yml
    find . -name "*.py" -exec python -m py_compile {} \;

# Format files
format:
    @echo "✨ Formatting files..."
    #!/usr/bin/env bash
    if command -v black >/dev/null 2>&1; then \
        black tests/ --line-length 88; \
    else \
        echo "Black not installed, skipping Python formatting"; \
    fi

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
    pre-commit run --all-files

# Check for broken links (requires linkchecker)
check-links:
    @echo "🔗 Checking for broken links..."
    #!/usr/bin/env bash
    if ! command -v linkchecker &> /dev/null; then
        echo "❌ linkchecker not installed. Install with: pip install linkchecker"
        exit 1
    fi
    
    echo "Starting MkDocs server..."
    mkdocs serve --dev-addr=127.0.0.1:8000 &
    SERVER_PID=$!
    
    # Wait for server to start
    sleep 5
    
    echo "Running linkchecker..."
    linkchecker http://127.0.0.1:8000 --check-extern || true
    
    echo "Stopping server..."
    kill $SERVER_PID

# Watch for changes and rebuild automatically
watch:
    @echo "👀 Watching for changes..."
    #!/usr/bin/env bash
    if command -v watchexec >/dev/null 2>&1; then
        watchexec -e md,yml,yaml,html,css,js -- just dev-check
    else
        echo "❌ watchexec not installed. Install with: cargo install watchexec-cli"
        echo "Falling back to mkdocs serve..."
        mkdocs serve
    fi

# Create a new blog post
new-post title:
    @echo "📝 Creating new blog post: {{title}}"
    #!/usr/bin/env bash
    DATE=$(date +%Y-%m-%d)
    SLUG=$(echo "{{title}}" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-\|-$//g')
    FILENAME="docs/blog/posts/${SLUG}.md"
    
    if [ -f "$FILENAME" ]; then
        echo "❌ File $FILENAME already exists"
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
    pip freeze > requirements.txt
    @echo "✅ requirements.txt updated"

# Update dependencies
update:
    @echo "⬆️  Updating dependencies..."
    pip install --upgrade -r requirements.txt

# Run security check on dependencies
security-check:
    @echo "🔒 Running security check..."
    #!/usr/bin/env bash
    if command -v safety >/dev/null 2>&1; then
        safety check
    else
        echo "❌ safety not installed. Install with: pip install safety"
        exit 1
    fi

# Profile build performance
profile:
    @echo "📊 Profiling build performance..."
    time mkdocs build --clean --strict

# Deploy to GitHub Pages (if configured)
deploy:
    @echo "🚀 Deploying to GitHub Pages..."
    mkdocs gh-deploy --clean

# Show project statistics
stats:
    @echo "📊 Project Statistics:"
    @echo "  Total files: $(find docs -name '*.md' | wc -l)"
    @echo "  Blog posts: $(find docs/blog/posts -name '*.md' 2>/dev/null | wc -l || echo 0)"
    @echo "  Pages: $(find docs -name '*.md' -not -path 'docs/blog/*' | wc -l)"
    @echo "  Templates: $(find overrides -name '*.html' 2>/dev/null | wc -l || echo 0)"
    @echo "  Assets: $(find docs -name '*.css' -o -name '*.js' -o -name '*.png' -o -name '*.jpg' -o -name '*.svg' | wc -l)"

# Initialize project (run once after cloning)
init:
    @echo "🚀 Initializing project..."
    just install
    @echo "✅ Project initialized! Run 'just serve' to start development server."