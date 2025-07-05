#!/bin/bash
#
# Test GitHub Actions workflow locally using Act.
# This script provides a convenient interface for testing our deployment workflow.
#

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
WORKFLOW_FILE="$PROJECT_ROOT/.github/workflows/deploy.yml"
ACT_CONFIG="$PROJECT_ROOT/.actrc"

echo -e "${BLUE}🚀 Local GitHub Actions Workflow Testing${NC}"
echo -e "${BLUE}===========================================${NC}"

# Function to check if Act is installed
check_act_installed() {
    if ! command -v act &> /dev/null; then
        echo -e "${RED}❌ Act is not installed${NC}"
        echo -e "${YELLOW}💡 Install with: curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}✅ Act is installed${NC}"
    act --version
}

# Function to check if Docker is running
check_docker_running() {
    if ! docker info &> /dev/null; then
        echo -e "${RED}❌ Docker is not running${NC}"
        echo -e "${YELLOW}💡 Please start Docker and try again${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}✅ Docker is running${NC}"
}

# Function to list available workflows
list_workflows() {
    echo -e "${BLUE}📋 Available workflows:${NC}"
    cd "$PROJECT_ROOT"
    act --list
}

# Function to validate workflow syntax
validate_workflow() {
    echo -e "${BLUE}🔍 Validating workflow syntax...${NC}"
    cd "$PROJECT_ROOT"
    
    if act --list --workflows "$WORKFLOW_FILE" &> /dev/null; then
        echo -e "${GREEN}✅ Workflow syntax is valid${NC}"
    else
        echo -e "${RED}❌ Workflow syntax error${NC}"
        act --list --workflows "$WORKFLOW_FILE"
        exit 1
    fi
}

# Function to run workflow with Act
run_workflow() {
    local mode="$1"
    echo -e "${BLUE}🏃 Running workflow in $mode mode...${NC}"
    cd "$PROJECT_ROOT"
    
    case "$mode" in
        "list")
            act push --list
            ;;
        "dry-run")
            echo -e "${YELLOW}📋 Showing what would be executed:${NC}"
            act push --list --verbose
            ;;
        "test-only")
            echo -e "${YELLOW}🧪 Running tests only (no deployment):${NC}"
            act push \
                --env ACT=true \
                --env SKIP_DEPLOY=true \
                --verbose
            ;;
        "full")
            echo -e "${YELLOW}🚀 Running full workflow (deployment skipped in Act):${NC}"
            act push \
                --env ACT=true \
                --verbose
            ;;
        "debug")
            echo -e "${YELLOW}🐛 Running workflow with debug output:${NC}"
            act push \
                --env ACT=true \
                --env DEBUG=true \
                --verbose \
                --bind
            ;;
        *)
            echo -e "${RED}❌ Unknown mode: $mode${NC}"
            show_help
            exit 1
            ;;
    esac
}

# Function to show help
show_help() {
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Test GitHub Actions workflow locally using Act"
    echo ""
    echo "Commands:"
    echo "  check         Check prerequisites (Act, Docker)"
    echo "  list          List available workflows and jobs"
    echo "  validate      Validate workflow syntax"
    echo "  dry-run       Show what would be executed"
    echo "  test-only     Run tests only (skip deployment)"
    echo "  full          Run full workflow (deployment simulated)"
    echo "  debug         Run with debug output and bind mounts"
    echo "  help          Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 check                    # Check prerequisites"
    echo "  $0 test-only               # Run tests without deployment"
    echo "  $0 full                    # Run complete workflow"
    echo ""
    echo "Configuration:"
    echo "  Act config: $ACT_CONFIG"
    echo "  Workflow: $WORKFLOW_FILE"
}

# Function to check prerequisites
check_prerequisites() {
    echo -e "${BLUE}🔧 Checking prerequisites...${NC}"
    check_act_installed
    check_docker_running
    
    # Check if workflow file exists
    if [[ ! -f "$WORKFLOW_FILE" ]]; then
        echo -e "${RED}❌ Workflow file not found: $WORKFLOW_FILE${NC}"
        exit 1
    fi
    echo -e "${GREEN}✅ Workflow file exists${NC}"
    
    # Check if Act config exists
    if [[ ! -f "$ACT_CONFIG" ]]; then
        echo -e "${YELLOW}⚠️  Act config not found: $ACT_CONFIG${NC}"
        echo -e "${YELLOW}💡 Will use default Act configuration${NC}"
    else
        echo -e "${GREEN}✅ Act config exists${NC}"
    fi
    
    echo -e "${GREEN}🎉 All prerequisites met!${NC}"
}

# Main execution
main() {
    local command="${1:-help}"
    
    case "$command" in
        "check")
            check_prerequisites
            ;;
        "list")
            check_prerequisites
            list_workflows
            ;;
        "validate")
            check_prerequisites
            validate_workflow
            ;;
        "dry-run")
            check_prerequisites
            validate_workflow
            run_workflow "dry-run"
            ;;
        "test-only")
            check_prerequisites
            validate_workflow
            run_workflow "test-only"
            ;;
        "full")
            check_prerequisites
            validate_workflow
            run_workflow "full"
            ;;
        "debug")
            check_prerequisites
            validate_workflow
            run_workflow "debug"
            ;;
        "help"|"--help"|"-h")
            show_help
            ;;
        *)
            echo -e "${RED}❌ Unknown command: $command${NC}"
            echo ""
            show_help
            exit 1
            ;;
    esac
}

# Run main function with all arguments
main "$@"