#!/bin/bash
"""
Simple deployment verification script for MkDocs GitHub Pages deployment.
This script verifies that the deployed site is accessible and functional.
"""

set -e  # Exit on any error

# Configuration
SITE_URL="${1:-https://USERNAME.github.io/REPOSITORY}"  # Override with actual URL
MAX_RETRIES=10
RETRY_DELAY=30

echo "🔍 Verifying deployment to: $SITE_URL"

# Function to check if site is accessible
check_site_accessibility() {
    local url=$1
    local max_retries=$2
    local delay=$3
    
    for i in $(seq 1 $max_retries); do
        echo "📡 Attempt $i/$max_retries: Checking site accessibility..."
        
        if curl -f -s --max-time 10 "$url" > /dev/null; then
            echo "✅ Site is accessible!"
            return 0
        else
            echo "❌ Site not accessible yet. Waiting ${delay}s before retry..."
            sleep $delay
        fi
    done
    
    echo "🚨 Site not accessible after $max_retries attempts"
    return 1
}

# Function to verify essential pages
verify_essential_pages() {
    local base_url=$1
    local pages=("index.html" "sitemap.xml")
    
    echo "📄 Verifying essential pages..."
    
    for page in "${pages[@]}"; do
        local url="${base_url}/${page}"
        echo "   Checking: $url"
        
        if curl -f -s --max-time 10 "$url" > /dev/null; then
            echo "   ✅ $page is accessible"
        else
            echo "   ❌ $page is not accessible"
            return 1
        fi
    done
    
    return 0
}

# Function to check for common issues
check_common_issues() {
    local url=$1
    echo "🔧 Checking for common deployment issues..."
    
    # Check if site returns proper content type
    local content_type=$(curl -s -I "$url" | grep -i "content-type" | head -1)
    if [[ $content_type == *"text/html"* ]]; then
        echo "   ✅ Content-Type is HTML"
    else
        echo "   ⚠️  Content-Type: $content_type"
    fi
    
    # Check if site has proper title
    local title=$(curl -s "$url" | grep -o '<title>[^<]*</title>' | head -1)
    if [[ -n "$title" ]]; then
        echo "   ✅ Page has title: $title"
    else
        echo "   ⚠️  No title found"
    fi
    
    # Check for 404 errors on homepage
    local status=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    if [[ "$status" == "200" ]]; then
        echo "   ✅ HTTP Status: $status"
    else
        echo "   ❌ HTTP Status: $status"
        return 1
    fi
    
    return 0
}

# Main verification process
main() {
    echo "🚀 Starting deployment verification..."
    echo "📍 Target URL: $SITE_URL"
    echo ""
    
    # Step 1: Check basic accessibility
    if ! check_site_accessibility "$SITE_URL" "$MAX_RETRIES" "$RETRY_DELAY"; then
        echo "💥 Deployment verification failed: Site not accessible"
        exit 1
    fi
    
    echo ""
    
    # Step 2: Verify essential pages
    if ! verify_essential_pages "$SITE_URL"; then
        echo "💥 Deployment verification failed: Essential pages missing"
        exit 1
    fi
    
    echo ""
    
    # Step 3: Check for common issues
    if ! check_common_issues "$SITE_URL"; then
        echo "💥 Deployment verification failed: Common issues detected"
        exit 1
    fi
    
    echo ""
    echo "🎉 Deployment verification successful!"
    echo "✅ Site is live and functional at: $SITE_URL"
}

# Show usage if no URL provided
if [[ "$1" == "--help" || "$1" == "-h" ]]; then
    echo "Usage: $0 [SITE_URL]"
    echo ""
    echo "Verify that a deployed MkDocs site is accessible and functional."
    echo ""
    echo "Arguments:"
    echo "  SITE_URL    The URL of the deployed site (optional)"
    echo ""
    echo "Example:"
    echo "  $0 https://username.github.io/repository"
    echo ""
    echo "Environment variables:"
    echo "  MAX_RETRIES     Maximum number of retry attempts (default: 10)"
    echo "  RETRY_DELAY     Delay between retries in seconds (default: 30)"
    exit 0
fi

# Run main function
main