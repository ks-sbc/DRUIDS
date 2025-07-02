#!/bin/bash
# Install git hooks for MkDocs validation

set -e

echo "🔧 Installing git hooks..."

# Create hooks directory if it doesn't exist
mkdir -p .git/hooks

# Pre-commit hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
# Pre-commit hook for MkDocs validation

echo "🔍 Running pre-commit validation..."

# Run the comprehensive validation script
if ./scripts/validate-all.sh; then
    echo "✅ Pre-commit validation passed"
    exit 0
else
    echo "❌ Pre-commit validation failed"
    echo "💡 Fix the issues above or use 'git commit --no-verify' to skip validation"
    exit 1
fi
EOF

# Make hooks executable
chmod +x .git/hooks/pre-commit

# Pre-push hook (optional, lighter validation)
cat > .git/hooks/pre-push << 'EOF'
#!/bin/bash
# Pre-push hook for MkDocs validation

echo "🚀 Running pre-push validation..."

# Quick validation before push
if python tests/validate_config.py && mkdocs build --clean --strict --site-dir temp_site; then
    rm -rf temp_site
    echo "✅ Pre-push validation passed"
    exit 0
else
    rm -rf temp_site
    echo "❌ Pre-push validation failed"
    exit 1
fi
EOF

chmod +x .git/hooks/pre-push

echo "✅ Git hooks installed successfully!"
echo ""
echo "Installed hooks:"
echo "  - pre-commit: Runs comprehensive validation before each commit"
echo "  - pre-push: Runs quick validation before pushing"
echo ""
echo "To skip validation for a specific commit, use: git commit --no-verify"