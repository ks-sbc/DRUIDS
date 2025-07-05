#!/usr/bin/env python3
"""
/project:act-test - Execute comprehensive local GitHub Actions workflow testing using Act

This command automates the complete Act testing workflow with intelligent error handling,
performance monitoring, and detailed reporting.
"""

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Colors for output
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'  # No Color

class ActTestRunner:
    """Comprehensive Act testing automation"""
    
    def __init__(self, project_root: Optional[Path] = None):
        self.project_root = project_root or Path.cwd()
        self.workflows_dir = self.project_root / ".github" / "workflows"
        self.act_dir = self.project_root / ".github" / "act"
        self.results = {
            'start_time': None,
            'end_time': None,
            'duration': 0,
            'checks': {},
            'execution': {},
            'recommendations': []
        }
    
    def print_header(self, title: str):
        """Print formatted section header"""
        print(f"\n{Colors.BLUE}{'=' * 60}{Colors.NC}")
        print(f"{Colors.BLUE}🚀 {title}{Colors.NC}")
        print(f"{Colors.BLUE}{'=' * 60}{Colors.NC}")
    
    def print_status(self, status: str, message: str, details: str = ""):
        """Print formatted status message"""
        status_colors = {
            'SUCCESS': Colors.GREEN,
            'WARNING': Colors.YELLOW,
            'ERROR': Colors.RED,
            'INFO': Colors.CYAN
        }
        color = status_colors.get(status, Colors.NC)
        icon = {
            'SUCCESS': '✅',
            'WARNING': '⚠️',
            'ERROR': '❌',
            'INFO': 'ℹ️'
        }.get(status, '•')
        
        print(f"{color}{icon} {message}{Colors.NC}")
        if details:
            print(f"   {details}")
    
    def run_command(self, cmd: List[str], timeout: int = 60, capture_output: bool = True) -> Tuple[bool, str, str]:
        """Run command and return success, stdout, stderr"""
        try:
            result = subprocess.run(
                cmd,
                cwd=self.project_root,
                capture_output=capture_output,
                text=True,
                timeout=timeout
            )
            return result.returncode == 0, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return False, "", f"Command timed out after {timeout} seconds"
        except Exception as e:
            return False, "", str(e)
    
    def check_prerequisites(self) -> bool:
        """Check all prerequisites for Act testing"""
        self.print_header("Prerequisites Check")
        all_good = True
        
        checks = [
            ("Act Installation", self.check_act_installed),
            ("Docker Running", self.check_docker_running),
            ("Workflow Files", self.check_workflow_files),
            ("Act Configuration", self.check_act_configuration),
            ("Project Structure", self.check_project_structure)
        ]
        
        for check_name, check_func in checks:
            try:
                success, message, details = check_func()
                self.results['checks'][check_name] = {'success': success, 'message': message}
                
                if success:
                    self.print_status('SUCCESS', message, details)
                else:
                    self.print_status('ERROR', message, details)
                    all_good = False
            except Exception as e:
                self.print_status('ERROR', f"{check_name} check failed", str(e))
                all_good = False
        
        return all_good
    
    def check_act_installed(self) -> Tuple[bool, str, str]:
        """Check if Act is installed and get version"""
        success, stdout, stderr = self.run_command(["act", "--version"])
        if success and "act version" in stdout:
            version = stdout.strip()
            return True, "Act is installed", f"Version: {version}"
        else:
            return False, "Act is not installed", "Install with: curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash"
    
    def check_docker_running(self) -> Tuple[bool, str, str]:
        """Check if Docker is running"""
        success, stdout, stderr = self.run_command(["docker", "info"], timeout=10)
        if success:
            return True, "Docker is running", "Docker daemon is accessible"
        else:
            return False, "Docker is not running", "Please start Docker service"
    
    def check_workflow_files(self) -> Tuple[bool, str, str]:
        """Check for workflow files"""
        if not self.workflows_dir.exists():
            return False, "No .github/workflows directory", "Create workflow directory first"
        
        workflows = list(self.workflows_dir.glob("*.yml")) + list(self.workflows_dir.glob("*.yaml"))
        if workflows:
            workflow_list = ", ".join([w.name for w in workflows])
            return True, f"Found {len(workflows)} workflow(s)", f"Workflows: {workflow_list}"
        else:
            return False, "No workflow files found", "Create at least one .yml workflow file"
    
    def check_act_configuration(self) -> Tuple[bool, str, str]:
        """Check Act configuration files"""
        actrc = self.project_root / ".actrc"
        if actrc.exists():
            return True, "Act configuration exists", f"Config file: {actrc}"
        else:
            return False, "No .actrc configuration", "Consider creating .actrc for consistent behavior"
    
    def check_project_structure(self) -> Tuple[bool, str, str]:
        """Check project structure for testing"""
        required_files = ["mkdocs.yml", "dependencies/requirements.txt"]
        missing = []
        
        for file_path in required_files:
            if not (self.project_root / file_path).exists():
                missing.append(file_path)
        
        if missing:
            return False, "Missing required files", f"Missing: {', '.join(missing)}"
        else:
            return True, "Project structure is valid", "All required files present"
    
    def list_workflows(self, workflow_filter: Optional[str] = None) -> List[Dict]:
        """List available workflows with Act"""
        self.print_header("Available Workflows")
        
        cmd = ["act", "--list"]
        if workflow_filter:
            workflow_path = self.workflows_dir / workflow_filter
            if workflow_path.exists():
                cmd.extend(["--workflows", str(workflow_path)])
        
        success, stdout, stderr = self.run_command(cmd)
        
        workflows = []
        if success:
            lines = stdout.strip().split('\n')
            # Skip header line and parse workflow information
            for line in lines[1:]:
                if line.strip() and not line.startswith('Detected'):
                    parts = line.split()
                    if len(parts) >= 3:
                        workflows.append({
                            'job_id': parts[1],
                            'job_name': parts[2],
                            'workflow_name': ' '.join(parts[3:-2]) if len(parts) > 5 else parts[3],
                            'events': parts[-1] if len(parts) > 4 else 'unknown'
                        })
            
            for workflow in workflows:
                self.print_status('INFO', 
                    f"Job: {workflow['job_name']}", 
                    f"ID: {workflow['job_id']}, Events: {workflow['events']}")
        else:
            self.print_status('ERROR', "Failed to list workflows", stderr)
        
        return workflows
    
    def execute_workflow(self, workflow: str, mode: str = "test-only") -> bool:
        """Execute workflow with specified mode"""
        self.print_header(f"Executing Workflow: {workflow} ({mode})")
        
        # Build Act command based on mode
        cmd = ["act", "push"]
        
        # Add workflow specification if provided
        if workflow and workflow != "all":
            workflow_path = self.workflows_dir / workflow
            if workflow_path.exists():
                cmd.extend(["--workflows", str(workflow_path)])
        
        # Configure execution mode
        env_vars = ["ACT=true"]
        
        if mode == "dry-run":
            cmd.append("--list")
            self.print_status('INFO', "Running in dry-run mode", "Showing execution plan")
        elif mode == "test-only":
            env_vars.append("SKIP_DEPLOY=true")
            self.print_status('INFO', "Running tests only", "Deployment steps will be skipped")
        elif mode == "debug":
            cmd.append("--verbose")
            env_vars.append("DEBUG=true")
            self.print_status('INFO', "Running in debug mode", "Verbose output enabled")
        elif mode == "full":
            self.print_status('INFO', "Running full workflow", "All steps will execute (deployment simulated)")
        
        # Add environment variables
        for env_var in env_vars:
            cmd.extend(["--env", env_var])
        
        # Execute command
        start_time = time.time()
        self.results['execution']['start_time'] = start_time
        
        success, stdout, stderr = self.run_command(cmd, timeout=300)
        
        end_time = time.time()
        duration = end_time - start_time
        self.results['execution']['end_time'] = end_time
        self.results['execution']['duration'] = duration
        self.results['execution']['success'] = success
        
        # Report results
        if success:
            self.print_status('SUCCESS', f"Workflow completed successfully", 
                            f"Duration: {duration:.1f} seconds")
            self.analyze_execution_output(stdout, stderr)
        else:
            self.print_status('ERROR', "Workflow execution failed", stderr)
            self.diagnose_failure(stdout, stderr)
        
        return success
    
    def analyze_execution_output(self, stdout: str, stderr: str):
        """Analyze execution output for insights"""
        self.print_header("Execution Analysis")
        
        # Count steps executed
        step_lines = [line for line in stdout.split('\n') if '|' in line and ('✅' in line or '❌' in line)]
        successful_steps = len([line for line in step_lines if '✅' in line])
        failed_steps = len([line for line in step_lines if '❌' in line])
        
        self.print_status('INFO', f"Steps executed: {len(step_lines)}", 
                         f"Successful: {successful_steps}, Failed: {failed_steps}")
        
        # Check for warnings
        warning_lines = [line for line in stderr.split('\n') if 'warning' in line.lower()]
        if warning_lines:
            self.print_status('WARNING', f"Found {len(warning_lines)} warnings", 
                             "Review output for details")
        
        # Performance analysis
        if self.results['execution']['duration'] > 120:
            self.results['recommendations'].append(
                "Consider optimizing workflow for faster execution (> 2 minutes)"
            )
        
        # Success recommendations
        if successful_steps == len(step_lines):
            self.results['recommendations'].append(
                "All steps completed successfully - workflow is ready for production"
            )
    
    def diagnose_failure(self, stdout: str, stderr: str):
        """Diagnose common failure patterns"""
        self.print_header("Failure Diagnosis")
        
        common_issues = [
            ("Docker permission", "permission denied", "Add user to docker group or use sudo"),
            ("Missing dependencies", "command not found", "Install missing dependencies in workflow"),
            ("Network issues", "connection refused", "Check network connectivity and firewall"),
            ("Resource limits", "no space left", "Clean up disk space or increase limits"),
            ("Timeout", "timeout", "Increase timeout values or optimize slow steps"),
            ("Configuration error", "error loading", "Check workflow YAML syntax and configuration")
        ]
        
        found_issues = []
        for issue_type, pattern, solution in common_issues:
            if pattern in stderr.lower() or pattern in stdout.lower():
                found_issues.append((issue_type, solution))
                self.print_status('WARNING', f"Detected: {issue_type}", solution)
        
        if not found_issues:
            self.print_status('INFO', "No common issues detected", 
                             "Check full output for specific error details")
        
        # Add diagnostic recommendations
        self.results['recommendations'].extend([
            "Review full error output for specific failure details",
            "Try running with --verbose flag for more information",
            "Check Docker logs if container-related issues persist"
        ])
    
    def generate_report(self) -> Dict:
        """Generate comprehensive test report"""
        self.print_header("Test Report Summary")
        
        # Overall status
        prerequisites_passed = all(check['success'] for check in self.results['checks'].values())
        execution_success = self.results['execution'].get('success', False)
        overall_success = prerequisites_passed and execution_success
        
        status = 'SUCCESS' if overall_success else 'ERROR'
        self.print_status(status, f"Overall Status: {'PASSED' if overall_success else 'FAILED'}")
        
        # Duration
        if 'duration' in self.results['execution']:
            duration = self.results['execution']['duration']
            self.print_status('INFO', f"Total Duration: {duration:.1f} seconds")
        
        # Recommendations
        if self.results['recommendations']:
            self.print_status('INFO', "Recommendations:")
            for i, rec in enumerate(self.results['recommendations'], 1):
                print(f"   {i}. {rec}")
        
        return self.results
    
    def save_report(self, output_file: Optional[Path] = None):
        """Save detailed report to file"""
        if not output_file:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            output_file = self.project_root / f"act_test_report_{timestamp}.json"
        
        with open(output_file, 'w') as f:
            json.dump(self.results, f, indent=2, default=str)
        
        self.print_status('SUCCESS', f"Report saved to: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Execute comprehensive local GitHub Actions workflow testing using Act",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python project-act-test.py                          # Test all workflows in test-only mode
  python project-act-test.py deploy.yml               # Test specific workflow
  python project-act-test.py deploy.yml --mode debug  # Test with verbose debugging
  python project-act-test.py --mode dry-run           # Show execution plan only
  python project-act-test.py --check-only             # Run prerequisite checks only
        """
    )
    
    parser.add_argument(
        "workflow",
        nargs="?",
        default="all",
        help="Workflow file to test (default: all workflows)"
    )
    
    parser.add_argument(
        "--mode",
        choices=["dry-run", "test-only", "full", "debug"],
        default="test-only",
        help="Execution mode (default: test-only)"
    )
    
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Run prerequisite checks only"
    )
    
    parser.add_argument(
        "--save-report",
        type=Path,
        help="Save detailed report to specified file"
    )
    
    parser.add_argument(
        "--project-root",
        type=Path,
        help="Project root directory (default: current directory)"
    )
    
    args = parser.parse_args()
    
    # Initialize runner
    runner = ActTestRunner(args.project_root)
    runner.results['start_time'] = time.time()
    
    try:
        # Check prerequisites
        prerequisites_ok = runner.check_prerequisites()
        
        if not prerequisites_ok:
            print(f"\n{Colors.RED}❌ Prerequisites check failed. Please fix issues before proceeding.{Colors.NC}")
            sys.exit(1)
        
        if args.check_only:
            print(f"\n{Colors.GREEN}✅ All prerequisites passed!{Colors.NC}")
            sys.exit(0)
        
        # List workflows
        workflows = runner.list_workflows(args.workflow if args.workflow != "all" else None)
        
        if not workflows:
            print(f"\n{Colors.RED}❌ No workflows found to execute.{Colors.NC}")
            sys.exit(1)
        
        # Execute workflow
        success = runner.execute_workflow(args.workflow, args.mode)
        
        # Generate report
        runner.results['end_time'] = time.time()
        runner.results['duration'] = runner.results['end_time'] - runner.results['start_time']
        
        report = runner.generate_report()
        
        # Save report if requested
        if args.save_report:
            runner.save_report(args.save_report)
        
        # Exit with appropriate code
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}⚠️ Test execution interrupted by user{Colors.NC}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}❌ Unexpected error: {e}{Colors.NC}")
        sys.exit(1)


if __name__ == "__main__":
    main()