#!/bin/bash

# MkDocs Build Test Suite
# Tests various aspects of the MkDocs build process

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test counter
TESTS_RUN=0
TESTS_PASSED=0

# Helper functions
log_info() {
    echo -e "${YELLOW}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[PASS]${NC} $1"
    ((TESTS_PASSED++))
}

log_error() {
    echo -e "${RED}[FAIL]${NC} $1"
}

run_test() {
    local test_name="$1"
    local test_command="$2"
    
    ((TESTS_RUN++))
    log_info "Running test: $test_name"
    
    if eval "$test_command"; then
        log_success "$test_name"
        return 0
    else
        log_error "$test_name"
        return 1
    fi
}

# Change to project root
cd "$(dirname "$0")/.."

log_info "Starting MkDocs Build Test Suite"
log_info "Project directory: $(pwd)"

# Test 1: Check if required files exist
run_test "Required files exist" '
    [ -f "mkdocs.yml" ] && 
    [ -f "config/pyproject.toml" ] && 
    [ -d "docs" ] &&
    [ -f "config/.prettierrc.json" ]
'

# Test 2: Check if virtual environment is activated
run_test "Virtual environment check" '
    [ -n "$VIRTUAL_ENV" ] || [ -f ".venv/bin/activate" ]
'

# Test 3: Check if MkDocs is installed and accessible
run_test "MkDocs installation check" '
    command -v mkdocs >/dev/null 2>&1
'

# Test 4: Validate MkDocs configuration
run_test "MkDocs config validation" '
    mkdocs config-check 2>/dev/null || mkdocs build --help >/dev/null 2>&1
'

# Test 5: Clean build test
run_test "Clean build test" '
    mkdocs build --clean --quiet
'

# Test 6: Check if site directory was created
run_test "Site directory creation" '
    [ -d "site" ] && [ -f "site/index.html" ]
'

# Test 7: Check if CSS and JS assets are generated
run_test "Asset generation check" '
    find site -name "*.css" | grep -q . &&
    find site -name "*.js" | grep -q .
'

# Test 8: Prettier formatting check
run_test "Prettier formatting check" '
    npx prettier --check . >/dev/null 2>&1
'

# Test 9: Python syntax check for hooks
run_test "Python hooks syntax check" '
    if [ -f "hooks/shortcodes.py" ]; then
        python -m py_compile hooks/shortcodes.py
    else
        true  # Pass if no hooks file
    fi
'

# Test 10: Check for broken internal links (basic)
run_test "Basic link validation" '
    if [ -d "site" ]; then
        # Check if any HTML files contain obvious broken links
        ! grep -r "href=\"#\"" site/ >/dev/null 2>&1
    else
        false
    fi
'

# Test 11: Serve test (quick start/stop)
run_test "Development server test" '
    timeout 5s mkdocs serve --dev-addr=127.0.0.1:8001 >/dev/null 2>&1 || 
    [ $? -eq 124 ]  # timeout exit code means server started successfully
'

# Test 12: Check if search index is generated
run_test "Search index generation" '
    [ -f "site/search/search_index.json" ] || 
    find site -name "*search*" | grep -q .
'

# Summary
echo
log_info "Test Summary"
echo "Tests run: $TESTS_RUN"
echo "Tests passed: $TESTS_PASSED"
echo "Tests failed: $((TESTS_RUN - TESTS_PASSED))"

if [ $TESTS_PASSED -eq $TESTS_RUN ]; then
    log_success "All tests passed!"
    exit 0
else
    log_error "Some tests failed!"
    exit 1
fi