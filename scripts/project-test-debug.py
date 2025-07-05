#!/usr/bin/env python3
"""
/project:test-debug - Intelligent debugging for failing tests with context-aware troubleshooting

This command analyzes test failures, categorizes issues, runs diagnostic commands,
and provides specific remediation steps based on the type of failure detected.
"""

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

# Colors for output
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'  # No Color

class TestDebugger:
    """Intelligent test failure analysis and debugging"""
    
    def __init__(self, project_root: Optional[Path] = None):
        self.project_root = project_root or Path.cwd()
        self.results = {
            'timestamp': time.time(),
            'test_results': {},
            'failure_analysis': {},
            'environment_info': {},
            'recommendations': [],
            'diagnostic_commands': [],
            'resolved_issues': []
        }
        
        # Common failure patterns and their solutions
        self.failure_patterns = {
            'import_error': {
                'patterns': [r'ImportError', r'ModuleNotFoundError', r'No module named'],
                'category': 'dependency',
                'severity': 'high',
                'solutions': [
                    "Install missing dependencies: pip install -r dependencies/requirements.txt",
                    "Check if package is in requirements.txt",
                    "Verify Python path and virtual environment",
                    "Check for typos in import statements"
                ]
            },
            'file_not_found': {
                'patterns': [r'FileNotFoundError', r'No such file or directory', r'\[Errno 2\]'],
                'category': 'configuration',
                'severity': 'high',
                'solutions': [
                    "Check if required files exist in expected locations",
                    "Verify file paths in configuration",
                    "Ensure working directory is correct",
                    "Check for case sensitivity issues"
                ]
            },
            'permission_denied': {
                'patterns': [r'PermissionError', r'Permission denied', r'\[Errno 13\]'],
                'category': 'environment',
                'severity': 'medium',
                'solutions': [
                    "Check file permissions: ls -la",
                    "Add user to docker group if Docker-related",
                    "Run with appropriate privileges",
                    "Check directory ownership"
                ]
            },
            'network_error': {
                'patterns': [r'ConnectionError', r'TimeoutError', r'Network is unreachable'],
                'category': 'network',
                'severity': 'medium',
                'solutions': [
                    "Check network connectivity",
                    "Verify firewall settings",
                    "Test with longer timeout values",
                    "Check proxy configuration"
                ]
            },
            'assertion_error': {
                'patterns': [r'AssertionError', r'assert .+ == .+', r'Expected .+ but got'],
                'category': 'logic',
                'severity': 'medium',
                'solutions': [
                    "Review test expectations vs actual behavior",
                    "Check if test data has changed",
                    "Verify business logic implementation",
                    "Update test assertions if requirements changed"
                ]
            },
            'timeout_error': {
                'patterns': [r'TimeoutExpired', r'timeout', r'Command timed out'],
                'category': 'performance',
                'severity': 'medium',
                'solutions': [
                    "Increase timeout values in test configuration",
                    "Optimize slow operations",
                    "Check for deadlocks or infinite loops",
                    "Use mocking for external dependencies"
                ]
            },
            'docker_error': {
                'patterns': [r'docker', r'container', r'Cannot connect to the Docker daemon'],
                'category': 'environment',
                'severity': 'high',
                'solutions': [
                    "Start Docker daemon: sudo systemctl start docker",
                    "Add user to docker group: sudo usermod -aG docker $USER",
                    "Check Docker installation",
                    "Verify Docker socket permissions"
                ]
            },
            'act_error': {
                'patterns': [r'act:', r'GitHub Actions', r'workflow'],
                'category': 'tooling',
                'severity': 'medium',
                'solutions': [
                    "Check Act installation: act --version",
                    "Verify workflow YAML syntax",
                    "Update Act to latest version",
                    "Check Act configuration files"
                ]
            },
            'yaml_error': {
                'patterns': [r'YAMLError', r'yaml.scanner', r'mapping values are not allowed'],
                'category': 'configuration',
                'severity': 'high',
                'solutions': [
                    "Validate YAML syntax with yamllint",
                    "Check indentation and spacing",
                    "Verify quote usage in YAML",
                    "Use YAML validator tools"
                ]
            },
            'pytest_collection': {
                'patterns': [r'ERROR collecting', r'import errors', r'collection errors'],
                'category': 'test_setup',
                'severity': 'high',
                'solutions': [
                    "Fix import errors in test files",
                    "Check test file naming conventions",
                    "Verify pytest configuration",
                    "Review conftest.py for issues"
                ]
            }
        }
    
    def print_header(self, title: str):
        """Print formatted section header"""
        print(f"\n{Colors.BLUE}{'=' * 60}{Colors.NC}")
        print(f"{Colors.BLUE}🔧 {title}{Colors.NC}")
        print(f"{Colors.BLUE}{'=' * 60}{Colors.NC}")
    
    def print_status(self, status: str, message: str, details: str = ""):
        """Print formatted status message"""
        status_colors = {
            'SUCCESS': Colors.GREEN,
            'WARNING': Colors.YELLOW,
            'ERROR': Colors.RED,
            'INFO': Colors.CYAN,
            'DEBUG': Colors.PURPLE
        }
        color = status_colors.get(status, Colors.NC)
        icon = {
            'SUCCESS': '✅',
            'WARNING': '⚠️',
            'ERROR': '❌',
            'INFO': 'ℹ️',
            'DEBUG': '🔍'
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
    
    def collect_environment_info(self) -> Dict[str, Any]:
        """Collect comprehensive environment information"""
        self.print_header("Environment Information")
        
        env_info = {}
        
        # Python information
        env_info['python_version'] = sys.version
        env_info['python_executable'] = sys.executable
        
        # Operating system
        import platform
        env_info['os'] = platform.system()
        env_info['os_version'] = platform.release()
        env_info['architecture'] = platform.machine()
        
        # Working directory
        env_info['working_directory'] = str(self.project_root)
        
        # Git information
        success, stdout, stderr = self.run_command(["git", "branch", "--show-current"])
        if success:
            env_info['git_branch'] = stdout.strip()
        
        success, stdout, stderr = self.run_command(["git", "rev-parse", "HEAD"])
        if success:
            env_info['git_commit'] = stdout.strip()[:8]
        
        # Docker information
        success, stdout, stderr = self.run_command(["docker", "--version"])
        if success:
            env_info['docker_version'] = stdout.strip()
        
        # Act information
        success, stdout, stderr = self.run_command(["act", "--version"])
        if success:
            env_info['act_version'] = stdout.strip()
        
        # Display environment info
        for key, value in env_info.items():
            if value:
                self.print_status('INFO', f"{key.replace('_', ' ').title()}: {value}")
        
        return env_info
    
    def run_test_and_capture_output(self, test_pattern: str, verbose: bool = False) -> Dict[str, Any]:
        """Run tests and capture detailed output"""
        self.print_header(f"Running Tests: {test_pattern}")
        
        # Build pytest command
        cmd = ["python", "-m", "pytest", test_pattern, "--tb=long"]
        if verbose:
            cmd.extend(["-v", "-s"])
        
        # Add common pytest options for better debugging
        cmd.extend([
            "--capture=no",  # Don't capture stdout/stderr
            "--show-capture=all",  # Show captured output
            "--tb=long",  # Long traceback format
        ])
        
        self.print_status('INFO', f"Executing: {' '.join(cmd)}")
        
        start_time = time.time()
        success, stdout, stderr = self.run_command(cmd, timeout=300)
        duration = time.time() - start_time
        
        results = {
            'success': success,
            'duration': duration,
            'stdout': stdout,
            'stderr': stderr,
            'command': ' '.join(cmd)
        }
        
        if success:
            self.print_status('SUCCESS', f"Tests completed successfully", f"Duration: {duration:.1f}s")
        else:
            self.print_status('ERROR', f"Tests failed", f"Duration: {duration:.1f}s")
        
        return results
    
    def analyze_failure_patterns(self, test_output: str) -> List[Dict[str, Any]]:
        """Analyze test output for known failure patterns"""
        self.print_header("Failure Pattern Analysis")
        
        found_patterns = []
        
        for pattern_name, pattern_info in self.failure_patterns.items():
            for regex_pattern in pattern_info['patterns']:
                matches = re.findall(regex_pattern, test_output, re.IGNORECASE | re.MULTILINE)
                if matches:
                    found_patterns.append({
                        'name': pattern_name,
                        'category': pattern_info['category'],
                        'severity': pattern_info['severity'],
                        'matches': matches,
                        'solutions': pattern_info['solutions']
                    })
                    
                    severity_color = {
                        'high': Colors.RED,
                        'medium': Colors.YELLOW,
                        'low': Colors.GREEN
                    }.get(pattern_info['severity'], Colors.NC)
                    
                    self.print_status('ERROR', 
                        f"Detected: {pattern_name.replace('_', ' ').title()}", 
                        f"Category: {pattern_info['category']}, Severity: {pattern_info['severity']}")
        
        if not found_patterns:
            self.print_status('INFO', "No known failure patterns detected", 
                             "Manual analysis may be required")
        
        return found_patterns
    
    def extract_specific_errors(self, test_output: str) -> List[Dict[str, str]]:
        """Extract specific error messages and locations"""
        self.print_header("Specific Error Analysis")
        
        errors = []
        
        # Extract Python tracebacks
        traceback_pattern = r'(File "([^"]+)", line (\d+).*\n.*)'
        traceback_matches = re.findall(traceback_pattern, test_output, re.MULTILINE)
        
        for match in traceback_matches:
            error_line, file_path, line_number = match
            errors.append({
                'type': 'traceback',
                'file': file_path,
                'line': line_number,
                'message': error_line.strip()
            })
            
            self.print_status('ERROR', f"Error in {file_path}:{line_number}", error_line.strip())
        
        # Extract assertion errors
        assertion_pattern = r'(assert.*\n.*Expected.*\n.*Actual.*)'
        assertion_matches = re.findall(assertion_pattern, test_output, re.MULTILINE | re.DOTALL)
        
        for match in assertion_matches:
            errors.append({
                'type': 'assertion',
                'message': match.strip()
            })
            
            self.print_status('ERROR', "Assertion Error", match.strip())
        
        # Extract pytest collection errors
        collection_pattern = r'ERROR collecting (.*): (.*)'
        collection_matches = re.findall(collection_pattern, test_output)
        
        for file_path, error_msg in collection_matches:
            errors.append({
                'type': 'collection',
                'file': file_path,
                'message': error_msg.strip()
            })
            
            self.print_status('ERROR', f"Collection error in {file_path}", error_msg.strip())
        
        return errors
    
    def run_diagnostic_commands(self, failure_patterns: List[Dict]) -> Dict[str, Any]:
        """Run diagnostic commands based on detected failure patterns"""
        self.print_header("Running Diagnostic Commands")
        
        diagnostics = {}
        
        # Determine which diagnostics to run based on failure patterns
        categories = set(pattern['category'] for pattern in failure_patterns)
        
        diagnostic_commands = {
            'dependency': [
                (["pip", "list"], "List installed packages"),
                (["pip", "check"], "Check package dependencies"),
                (["python", "-c", "import sys; print('\\n'.join(sys.path))"], "Python path")
            ],
            'environment': [
                (["ls", "-la"], "Directory permissions"),
                (["whoami"], "Current user"),
                (["groups"], "User groups"),
                (["env"], "Environment variables")
            ],
            'configuration': [
                (["find", ".", "-name", "*.yml", "-o", "-name", "*.yaml"], "YAML files"),
                (["yamllint", "--version"], "YAML linter availability"),
                (["cat", "mkdocs.yml"], "MkDocs configuration")
            ],
            'tooling': [
                (["act", "--version"], "Act version"),
                (["docker", "--version"], "Docker version"),
                (["docker", "info"], "Docker info")
            ],
            'network': [
                (["ping", "-c", "1", "8.8.8.8"], "Network connectivity"),
                (["curl", "-I", "https://github.com"], "GitHub connectivity")
            ]
        }
        
        for category in categories:
            if category in diagnostic_commands:
                self.print_status('INFO', f"Running {category} diagnostics")
                diagnostics[category] = {}
                
                for cmd, description in diagnostic_commands[category]:
                    success, stdout, stderr = self.run_command(cmd, timeout=30)
                    diagnostics[category][description] = {
                        'command': ' '.join(cmd),
                        'success': success,
                        'output': stdout if success else stderr
                    }
                    
                    if success:
                        self.print_status('SUCCESS', description)
                    else:
                        self.print_status('WARNING', f"{description} failed", stderr[:100])
        
        return diagnostics
    
    def generate_recommendations(self, failure_patterns: List[Dict], specific_errors: List[Dict]) -> List[str]:
        """Generate specific recommendations based on analysis"""
        self.print_header("Recommendations")
        
        recommendations = []
        
        # Add solutions from detected patterns
        for pattern in failure_patterns:
            recommendations.extend(pattern['solutions'])
        
        # Add specific recommendations based on error types
        error_types = set(error['type'] for error in specific_errors)
        
        if 'traceback' in error_types:
            recommendations.extend([
                "Review Python tracebacks for exact error locations",
                "Check imports and function calls in failing files",
                "Verify file paths and working directory"
            ])
        
        if 'assertion' in error_types:
            recommendations.extend([
                "Review test assertions for correctness",
                "Check if test data or expectations have changed",
                "Consider updating tests if requirements changed"
            ])
        
        if 'collection' in error_types:
            recommendations.extend([
                "Fix import errors in test files",
                "Check test file naming conventions",
                "Review conftest.py configuration"
            ])
        
        # Add general debugging recommendations
        recommendations.extend([
            "Run tests with -v flag for verbose output",
            "Use --pdb flag to drop into debugger on failure",
            "Check recent changes that might have introduced issues",
            "Verify environment consistency across team members"
        ])
        
        # Remove duplicates and display
        unique_recommendations = list(dict.fromkeys(recommendations))
        
        for i, rec in enumerate(unique_recommendations, 1):
            self.print_status('INFO', f"{i}. {rec}")
        
        return unique_recommendations
    
    def suggest_fixes(self, failure_patterns: List[Dict]) -> List[str]:
        """Suggest specific fixes that can be applied"""
        self.print_header("Suggested Fixes")
        
        fixes = []
        
        # Check for common fixable issues
        categories = [pattern['category'] for pattern in failure_patterns]
        
        if 'dependency' in categories:
            # Check if requirements.txt exists
            requirements_file = self.project_root / "dependencies" / "requirements.txt"
            if requirements_file.exists():
                fixes.append("pip install -r dependencies/requirements.txt")
                self.print_status('INFO', "Suggested fix: Install missing dependencies")
        
        if 'configuration' in categories:
            # Check for common configuration files
            config_files = ["mkdocs.yml", ".actrc", "pytest.ini"]
            missing_configs = [f for f in config_files if not (self.project_root / f).exists()]
            
            if missing_configs:
                for config in missing_configs:
                    fixes.append(f"Create missing configuration file: {config}")
                    self.print_status('INFO', f"Suggested fix: Create {config}")
        
        if 'environment' in categories:
            # Docker-related fixes
            success, stdout, stderr = self.run_command(["docker", "info"])
            if not success:
                fixes.append("sudo systemctl start docker")
                fixes.append("sudo usermod -aG docker $USER")
                self.print_status('INFO', "Suggested fix: Start Docker and add user to docker group")
        
        return fixes
    
    def run_debug_session(self, test_pattern: str, verbose: bool = False, auto_fix: bool = False) -> Dict[str, Any]:
        """Run complete debug session"""
        print(f"{Colors.CYAN}🔧 Test Debugging Session{Colors.NC}")
        print(f"{Colors.CYAN}Target: {test_pattern}{Colors.NC}")
        print(f"{Colors.CYAN}Project: {self.project_root}{Colors.NC}")
        
        # Collect environment information
        self.results['environment_info'] = self.collect_environment_info()
        
        # Run tests and capture output
        self.results['test_results'] = self.run_test_and_capture_output(test_pattern, verbose)
        
        if self.results['test_results']['success']:
            self.print_status('SUCCESS', "All tests passed - no debugging needed!")
            return self.results
        
        # Analyze failures
        combined_output = (
            self.results['test_results']['stdout'] + 
            self.results['test_results']['stderr']
        )
        
        failure_patterns = self.analyze_failure_patterns(combined_output)
        specific_errors = self.extract_specific_errors(combined_output)
        
        self.results['failure_analysis'] = {
            'patterns': failure_patterns,
            'specific_errors': specific_errors
        }
        
        # Run diagnostics
        if failure_patterns:
            self.results['diagnostic_commands'] = self.run_diagnostic_commands(failure_patterns)
        
        # Generate recommendations
        self.results['recommendations'] = self.generate_recommendations(failure_patterns, specific_errors)
        
        # Suggest fixes
        suggested_fixes = self.suggest_fixes(failure_patterns)
        
        if auto_fix and suggested_fixes:
            self.print_header("Applying Auto-Fixes")
            for fix in suggested_fixes:
                if fix.startswith("pip install"):
                    cmd = fix.split()
                    success, stdout, stderr = self.run_command(cmd, timeout=120)
                    if success:
                        self.print_status('SUCCESS', f"Applied: {fix}")
                        self.results['resolved_issues'].append(fix)
                    else:
                        self.print_status('ERROR', f"Failed to apply: {fix}", stderr)
        
        # Final summary
        self.print_header("Debug Session Summary")
        
        if failure_patterns:
            self.print_status('INFO', f"Found {len(failure_patterns)} failure patterns")
        if specific_errors:
            self.print_status('INFO', f"Found {len(specific_errors)} specific errors")
        if self.results['recommendations']:
            self.print_status('INFO', f"Generated {len(self.results['recommendations'])} recommendations")
        
        return self.results


def main():
    parser = argparse.ArgumentParser(
        description="Intelligent debugging for failing tests with context-aware troubleshooting",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python project-test-debug.py test_act_integration.py          # Debug specific test file
  python project-test-debug.py test_*deployment* --verbose     # Debug with verbose output
  python project-test-debug.py tests/ --auto-fix               # Debug and attempt fixes
  python project-test-debug.py . -k "test_workflow"            # Debug specific test pattern
        """
    )
    
    parser.add_argument(
        "test_pattern",
        help="Test file, directory, or pattern to debug"
    )
    
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Run tests with verbose output"
    )
    
    parser.add_argument(
        "--auto-fix",
        action="store_true",
        help="Attempt to automatically fix detected issues"
    )
    
    parser.add_argument(
        "--save-report",
        type=Path,
        help="Save debug report to specified file"
    )
    
    parser.add_argument(
        "--project-root",
        type=Path,
        help="Project root directory (default: current directory)"
    )
    
    args = parser.parse_args()
    
    # Initialize debugger
    debugger = TestDebugger(args.project_root)
    
    try:
        # Run debug session
        results = debugger.run_debug_session(
            args.test_pattern, 
            verbose=args.verbose,
            auto_fix=args.auto_fix
        )
        
        # Save report if requested
        if args.save_report:
            with open(args.save_report, 'w') as f:
                json.dump(results, f, indent=2, default=str)
            print(f"\n{Colors.GREEN}📄 Debug report saved to: {args.save_report}{Colors.NC}")
        
        # Exit with appropriate code
        test_success = results['test_results'].get('success', False)
        sys.exit(0 if test_success else 1)
        
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}⚠️ Debug session interrupted by user{Colors.NC}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}❌ Unexpected error: {e}{Colors.NC}")
        sys.exit(1)


if __name__ == "__main__":
    main()