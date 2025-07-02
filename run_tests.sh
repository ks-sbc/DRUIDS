#!/bin/bash

# Comprehensive Test Runner for MkDocs Project
# Runs both Python and Bash tests

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Change to project root
cd "$(dirname "$0")"

log_info "Starting comprehensive test suite for MkDocs project"
log_info "Project directory: $(pwd)"

# Initialize test results
PYTHON_TESTS_PASSED=false
BASH_TESTS_PASSED=false

echo
log_info "=== Running Python Tests with pytest ==="
if python -m pytest tests/ -v; then
    log_success "Python tests passed"
    PYTHON_TESTS_PASSED=true
else
    log_error "Python tests failed"
fi

echo
log_info "=== Running Bash Tests ==="
if ./tests/test_build.sh; then
    log_success "Bash tests passed"
    BASH_TESTS_PASSED=true
else
    log_error "Bash tests failed"
fi

echo
log_info "=== Test Summary ==="
if $PYTHON_TESTS_PASSED; then
    log_success "✓ Python tests: PASSED"
else
    log_error "✗ Python tests: FAILED"
fi

if $BASH_TESTS_PASSED; then
    log_success "✓ Bash tests: PASSED"
else
    log_error "✗ Bash tests: FAILED"
fi

echo
if $PYTHON_TESTS_PASSED && $BASH_TESTS_PASSED; then
    log_success "🎉 All tests passed!"
    echo
    log_info "Test reports available at:"
    log_info "  - Python: tests/reports/report.html"
    log_info "  - Site build: site/ directory"
    exit 0
else
    log_error "❌ Some tests failed!"
    exit 1
fi