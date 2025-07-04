#!/bin/bash
set -e

# MkDocs Management Script
# Usage: ./mkdocs.sh [command]

show_help() {
    echo "MkDocs Management Script"
    echo
    echo "Usage: ./mkdocs.sh [command]"
    echo
    echo "Commands:"
    echo "  deploy-ready    Check deployment readiness (install + format + validate)"
    echo "  serve          Start development server"
    echo "  build          Test MkDocs build"
    echo "  format         Fix formatting issues"
    echo "  clean          Clean build artifacts"
    echo "  install        Install dependencies only"
    echo "  help           Show this help message"
    echo
    echo "Examples:"
    echo "  ./mkdocs.sh deploy-ready"
    echo "  ./mkdocs.sh serve"
}

install_deps() {
    echo "📦 Installing dependencies..."
    pip install -r dependencies/requirements.txt
    npm install
}

format_fix() {
    echo "🔧 Fixing formatting issues..."
    npm run format
    npm run lint:md:fix
}

build_test() {
    echo "🏗️ Testing MkDocs build..."
    mkdocs build --clean --strict
}

serve_dev() {
    echo "🚀 Starting development server..."
    mkdocs serve -a localhost:8001
}

clean_artifacts() {
    echo "🧹 Cleaning build artifacts..."
    rm -rf site/
    rm -rf test_site/
    find . -name "*.pyc" -delete
    find . -name "__pycache__" -delete
}

deploy_ready() {
    echo "🎯 Checking deployment readiness..."
    install_deps
    echo "🎨 Checking formatting..."
    npm run format:check
    echo "✅ Ready for deployment!"
}

# Main script logic
case "${1:-help}" in
    deploy-ready)
        deploy_ready
        ;;
    serve)
        serve_dev
        ;;
    build)
        build_test
        ;;
    format)
        format_fix
        ;;
    clean)
        clean_artifacts
        ;;
    install)
        install_deps
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        echo "❌ Unknown command: $1"
        echo
        show_help
        exit 1
        ;;
esac
