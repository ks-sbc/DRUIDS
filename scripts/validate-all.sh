#!/bin/bash
# Comprehensive validation script for MkDocs project

set -e  # Exit on any error

echo "🔍 Running comprehensive MkDocs validation..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Track overall success
OVERALL_SUCCESS=true

# 1. Check if required files exist
print_status $BLUE "📁 Checking required files..."
required_files=("mkdocs.yml" "docs/index.md")
for file in "${required_files[@]}"; do
    if [[ ! -f "$file" ]]; then
        print_status $RED "❌ Required file missing: $file"
        OVERALL_SUCCESS=false
    else
        print_status $GREEN "✅ Found: $file"
    fi
done

# 2. Validate YAML syntax
print_status $BLUE "📝 Validating YAML syntax..."
if command_exists yamllint; then
    if yamllint -c .yamllint.yml mkdocs.yml; then
        print_status $GREEN "✅ YAML syntax valid"
    else
        print_status $RED "❌ YAML syntax errors found"
        OVERALL_SUCCESS=false
    fi
else
    print_status $YELLOW "⚠️  yamllint not available, skipping YAML validation"
fi

# 3. Validate MkDocs configuration
print_status $BLUE "⚙️  Validating MkDocs configuration..."
if python tests/validate_config.py; then
    print_status $GREEN "✅ MkDocs configuration valid"
else
    print_status $RED "❌ MkDocs configuration errors found"
    OVERALL_SUCCESS=false
fi

# 4. Validate blog posts
print_status $BLUE "📝 Validating blog posts..."
if python tests/validate_blog_posts.py; then
    print_status $GREEN "✅ Blog posts valid"
else
    print_status $RED "❌ Blog post validation errors found"
    OVERALL_SUCCESS=false
fi

# 5. Test MkDocs build
print_status $BLUE "🏗️  Testing MkDocs build..."
if mkdocs build --clean --site-dir test_site; then
    print_status $GREEN "✅ MkDocs build successful"
    # Clean up test build
    rm -rf test_site
else
    print_status $RED "❌ MkDocs build failed"
    OVERALL_SUCCESS=false
fi

# 6. Run pytest if available
if [[ -d "tests" ]] && command_exists pytest; then
    print_status $BLUE "🧪 Running pytest..."
    if pytest tests/ -v; then
        print_status $GREEN "✅ All tests passed"
    else
        print_status $RED "❌ Some tests failed"
        OVERALL_SUCCESS=false
    fi
else
    print_status $YELLOW "⚠️  pytest not available or no tests directory, skipping tests"
fi

# 7. Check for common issues
print_status $BLUE "🔍 Checking for common issues..."

# Check for authors configuration mismatch
if grep -q "authors: true" mkdocs.yml; then
    if [[ ! -f "docs/blog/.authors.yml" ]]; then
        print_status $RED "❌ Authors enabled but .authors.yml file missing"
        OVERALL_SUCCESS=false
    fi
fi

# Check for broken internal links in blog posts
if [[ -d "docs/blog/posts" ]]; then
    broken_links=0
    for post in docs/blog/posts/*.md; do
        if [[ -f "$post" ]]; then
            # Check for common broken link patterns
            if grep -q "author/" "$post" && ! grep -q "authors: true" mkdocs.yml; then
                print_status $YELLOW "⚠️  Found author links in $post but authors are disabled"
            fi
        fi
    done
fi

# 8. Security check (if safety is available)
if command_exists safety; then
    print_status $BLUE "🔒 Running security check..."
    if safety check; then
        print_status $GREEN "✅ No known security vulnerabilities"
    else
        print_status $YELLOW "⚠️  Security vulnerabilities found (check output above)"
        # Don't fail overall validation for security issues, just warn
    fi
fi

# Final result
echo ""
if [[ "$OVERALL_SUCCESS" == true ]]; then
    print_status $GREEN "🎉 All validations passed successfully!"
    exit 0
else
    print_status $RED "❌ Some validations failed. Please fix the issues above."
    exit 1
fi