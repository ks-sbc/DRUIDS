#!/bin/bash

# MkDocs Material Versioning with Mike
# This script helps deploy versioned documentation

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if mike is installed
if ! command -v mike &> /dev/null; then
    print_error "Mike is not installed. Please install it with: pip install mike"
    exit 1
fi

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    print_error "This is not a git repository. Mike requires git for versioning."
    exit 1
fi

# Get version from command line argument or prompt
VERSION=${1:-}
if [ -z "$VERSION" ]; then
    echo -n "Enter version (e.g., 1.0, 2.1.0): "
    read VERSION
fi

if [ -z "$VERSION" ]; then
    print_error "Version is required"
    exit 1
fi

# Get title (optional)
TITLE=${2:-"v$VERSION"}

# Check if this is the first deployment
if ! mike list > /dev/null 2>&1; then
    print_status "First deployment detected. Setting up mike..."
    
    # Deploy the first version
    print_status "Deploying version $VERSION as latest..."
    mike deploy --push --update-aliases "$VERSION" latest
    
    # Set as default
    print_status "Setting $VERSION as default version..."
    mike set-default --push latest
    
    print_success "Initial version $VERSION deployed successfully!"
else
    # Check if version already exists
    if mike list | grep -q "^$VERSION"; then
        print_warning "Version $VERSION already exists. This will update it."
        echo -n "Continue? (y/N): "
        read CONFIRM
        if [[ ! $CONFIRM =~ ^[Yy]$ ]]; then
            print_status "Deployment cancelled."
            exit 0
        fi
    fi
    
    # Deploy new version
    print_status "Deploying version $VERSION..."
    mike deploy --push --update-aliases "$VERSION" "$TITLE"
    
    # Ask if this should be the new latest
    echo -n "Set this as the latest version? (y/N): "
    read SET_LATEST
    if [[ $SET_LATEST =~ ^[Yy]$ ]]; then
        print_status "Setting $VERSION as latest..."
        mike alias --push "$VERSION" latest
    fi
    
    # Ask if this should be the new default
    echo -n "Set this as the default version? (y/N): "
    read SET_DEFAULT
    if [[ $SET_DEFAULT =~ ^[Yy]$ ]]; then
        print_status "Setting $VERSION as default..."
        mike set-default --push "$VERSION"
    fi
    
    print_success "Version $VERSION deployed successfully!"
fi

# Show current versions
print_status "Current versions:"
mike list

# Show the site URL if available
if git remote get-url origin > /dev/null 2>&1; then
    REPO_URL=$(git remote get-url origin)
    if [[ $REPO_URL == *"github.com"* ]]; then
        # Extract GitHub Pages URL
        REPO_NAME=$(basename "$REPO_URL" .git)
        USER_NAME=$(basename "$(dirname "$REPO_URL")")
        SITE_URL="https://${USER_NAME}.github.io/${REPO_NAME}/"
        print_success "Site should be available at: $SITE_URL"
    fi
fi

print_success "Deployment complete!"