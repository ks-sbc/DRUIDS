#!/bin/bash
# Essential validation script for MkDocs project

set -e  # Exit on any error

echo "🔍 Running essential MkDocs validation..."

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

# Track overall success
OVERALL_SUCCESS=true

# 1. Check if required files exist
print_status $BLUE "📁 Checking required files..."
if [[ -f "mkdocs.yml" ]] && [[ -f "docs/index.md" ]]; then
    print_status $GREEN "✅ Required files found"
else
    print_status $RED "❌ Missing required files"
    OVERALL_SUCCESS=false
fi

# 2. Quick YAML check
print_status $BLUE "📝 Checking YAML syntax..."
if python -c "import yaml; yaml.safe_load(open('mkdocs.yml'))" 2>/dev/null; then
    print_status $GREEN "✅ YAML syntax valid"
else
    print_status $RED "❌ YAML syntax error in mkdocs.yml"
    OVERALL_SUCCESS=false
fi

# 3. Test MkDocs build (the most important check)
print_status $BLUE "🏗️  Testing MkDocs build..."
if mkdocs build --clean --site-dir test_site >/dev/null 2>&1; then
    print_status $GREEN "✅ MkDocs build successful"
    rm -rf test_site
else
    print_status $RED "❌ MkDocs build failed"
    print_status $YELLOW "Run 'mkdocs build' to see detailed errors"
    OVERALL_SUCCESS=false
fi

# Final result
echo ""
if [[ "$OVERALL_SUCCESS" == true ]]; then
    print_status $GREEN "✅ Essential validation passed!"
    exit 0
else
    print_status $RED "❌ Validation failed. Fix the issues above."
    exit 1
fi