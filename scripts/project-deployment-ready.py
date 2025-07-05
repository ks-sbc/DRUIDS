#!/usr/bin/env python3
"""
/project:deployment-ready - Validate complete deployment readiness with automated checks

This command performs comprehensive validation of deployment prerequisites,
runs Act-based workflow simulation, and generates actionable deployment checklist.
"""

import argparse
import json
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

class DeploymentReadinessChecker:
    """Comprehensive deployment readiness validation"""
    
    def __init__(self, project_root: Optional[Path] = None, environment: str = "production"):
        self.project_root = project_root or Path.cwd()
        self.environment = environment
        self.results = {
            'environment': environment,
            'timestamp': time.time(),
            'checks': {},
            'blocking_issues': [],
            'warnings': [],
            'recommendations': [],
            'deployment_ready': False,
            'confidence_score': 0
        }
    
    def print_header(self, title: str):
        """Print formatted section header"""
        print(f"\n{Colors.BLUE}{'=' * 60}{Colors.NC}")
        print(f"{Colors.BLUE}🚀 {title}{Colors.NC}")
        print(f"{Colors.BLUE}{'=' * 60}{Colors.NC}")
    
    def print_status(self, status: str, message: str, details: str = ""):
        """Print formatted status message"""
        status_colors = {
            'PASS': Colors.GREEN,
            'WARN': Colors.YELLOW,
            'FAIL': Colors.RED,
            'INFO': Colors.CYAN,
            'SKIP': Colors.PURPLE
        }
        color = status_colors.get(status, Colors.NC)
        icon = {
            'PASS': '✅',
            'WARN': '⚠️',
            'FAIL': '❌',
            'INFO': 'ℹ️',
            'SKIP': '⏭️'
        }.get(status, '•')
        
        print(f"{color}{icon} {message}{Colors.NC}")
        if details:
            print(f"   {details}")
    
    def run_command(self, cmd: List[str], timeout: int = 60, cwd: Optional[Path] = None) -> Tuple[bool, str, str]:
        """Run command and return success, stdout, stderr"""
        try:
            result = subprocess.run(
                cmd,
                cwd=cwd or self.project_root,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return result.returncode == 0, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return False, "", f"Command timed out after {timeout} seconds"
        except Exception as e:
            return False, "", str(e)
    
    def check_configuration_files(self) -> Dict[str, Any]:
        """Check for required configuration files"""
        self.print_header("Configuration Files Check")
        
        required_files = {
            'mkdocs.yml': 'MkDocs configuration',
            'dependencies/requirements.txt': 'Python dependencies',
            '.github/workflows/deploy.yml': 'Deployment workflow',
            'docs/index.md': 'Documentation entry point'
        }
        
        optional_files = {
            '.actrc': 'Act configuration for local testing',
            '.gitignore': 'Git ignore rules',
            'README.md': 'Project documentation'
        }
        
        results = {'required': {}, 'optional': {}, 'all_required_present': True}
        
        # Check required files
        for file_path, description in required_files.items():
            full_path = self.project_root / file_path
            if full_path.exists():
                self.print_status('PASS', f"{description}", f"Found: {file_path}")
                results['required'][file_path] = True
            else:
                self.print_status('FAIL', f"{description}", f"Missing: {file_path}")
                results['required'][file_path] = False
                results['all_required_present'] = False
                self.results['blocking_issues'].append(f"Missing required file: {file_path}")
        
        # Check optional files
        for file_path, description in optional_files.items():
            full_path = self.project_root / file_path
            if full_path.exists():
                self.print_status('PASS', f"{description}", f"Found: {file_path}")
                results['optional'][file_path] = True
            else:
                self.print_status('WARN', f"{description}", f"Recommended: {file_path}")
                results['optional'][file_path] = False
                self.results['warnings'].append(f"Missing recommended file: {file_path}")
        
        return results
    
    def check_dependencies(self) -> Dict[str, Any]:
        """Check Python dependencies and installation"""
        self.print_header("Dependencies Check")
        
        results = {'python_version': None, 'dependencies_installed': False, 'missing_packages': []}
        
        # Check Python version
        success, stdout, stderr = self.run_command([sys.executable, "--version"])
        if success:
            python_version = stdout.strip()
            results['python_version'] = python_version
            self.print_status('PASS', f"Python available", python_version)
        else:
            self.print_status('FAIL', "Python not available", stderr)
            self.results['blocking_issues'].append("Python interpreter not available")
            return results
        
        # Check if requirements.txt exists and install dependencies
        requirements_file = self.project_root / "dependencies" / "requirements.txt"
        if requirements_file.exists():
            # Try to install dependencies
            self.print_status('INFO', "Installing dependencies", "Running pip install...")
            success, stdout, stderr = self.run_command([
                sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
            ], timeout=120)
            
            if success:
                self.print_status('PASS', "Dependencies installed successfully")
                results['dependencies_installed'] = True
            else:
                self.print_status('WARN', "Dependency installation issues", stderr)
                self.results['warnings'].append("Some dependencies may not be properly installed")
        
        # Check critical packages
        critical_packages = ['mkdocs', 'mkdocs-material', 'pytest']
        for package in critical_packages:
            success, stdout, stderr = self.run_command([
                sys.executable, "-m", "pip", "show", package
            ])
            
            if success:
                # Extract version from pip show output
                version_line = [line for line in stdout.split('\n') if line.startswith('Version:')]
                version = version_line[0].split(':')[1].strip() if version_line else 'unknown'
                self.print_status('PASS', f"{package} installed", f"Version: {version}")
            else:
                self.print_status('FAIL', f"{package} not installed", "Required for deployment")
                results['missing_packages'].append(package)
                self.results['blocking_issues'].append(f"Missing critical package: {package}")
        
        return results
    
    def check_mkdocs_configuration(self) -> Dict[str, Any]:
        """Validate MkDocs configuration"""
        self.print_header("MkDocs Configuration Check")
        
        results = {'config_valid': False, 'required_sections': {}, 'warnings': []}
        
        config_file = self.project_root / "mkdocs.yml"
        if not config_file.exists():
            self.print_status('FAIL', "MkDocs config missing", "mkdocs.yml not found")
            self.results['blocking_issues'].append("MkDocs configuration file missing")
            return results
        
        # Check if config can be loaded
        success, stdout, stderr = self.run_command(["mkdocs", "config"], timeout=30)
        
        if success:
            self.print_status('PASS', "MkDocs config is valid")
            results['config_valid'] = True
        else:
            self.print_status('FAIL', "MkDocs config has errors", stderr)
            self.results['blocking_issues'].append("MkDocs configuration is invalid")
            return results
        
        # Check required sections by parsing YAML
        try:
            import yaml
            with open(config_file, 'r') as f:
                config_data = yaml.safe_load(f)
            
            required_sections = ['site_name', 'theme', 'nav']
            for section in required_sections:
                if section in config_data:
                    self.print_status('PASS', f"Required section: {section}")
                    results['required_sections'][section] = True
                else:
                    self.print_status('WARN', f"Missing section: {section}", "May cause build issues")
                    results['required_sections'][section] = False
                    results['warnings'].append(f"Missing recommended section: {section}")
            
            # Check for GitHub Pages specific configuration
            if 'site_url' in config_data:
                site_url = config_data['site_url']
                if 'github.io' in site_url:
                    self.print_status('PASS', "GitHub Pages URL configured", site_url)
                else:
                    self.print_status('WARN', "Site URL may not be GitHub Pages", site_url)
            else:
                self.print_status('WARN', "No site_url configured", "Recommended for GitHub Pages")
                results['warnings'].append("site_url not configured")
        
        except ImportError:
            self.print_status('WARN', "PyYAML not available", "Cannot validate YAML structure")
        except Exception as e:
            self.print_status('WARN', "Config validation error", str(e))
        
        return results
    
    def check_build_process(self) -> Dict[str, Any]:
        """Test MkDocs build process"""
        self.print_header("Build Process Check")
        
        results = {'build_success': False, 'build_time': 0, 'warnings': [], 'site_created': False}
        
        # Clean any existing build
        site_dir = self.project_root / "site"
        if site_dir.exists():
            import shutil
            shutil.rmtree(site_dir)
        
        # Run build
        start_time = time.time()
        success, stdout, stderr = self.run_command(["mkdocs", "build", "--clean"], timeout=120)
        build_time = time.time() - start_time
        
        results['build_time'] = build_time
        
        if success:
            self.print_status('PASS', f"Build completed successfully", f"Duration: {build_time:.1f}s")
            results['build_success'] = True
        else:
            self.print_status('FAIL', "Build failed", stderr)
            self.results['blocking_issues'].append("MkDocs build process fails")
            return results
        
        # Check if site directory was created
        if site_dir.exists():
            self.print_status('PASS', "Site directory created")
            results['site_created'] = True
            
            # Check essential files
            essential_files = ['index.html', 'sitemap.xml']
            for file_name in essential_files:
                file_path = site_dir / file_name
                if file_path.exists():
                    self.print_status('PASS', f"Essential file: {file_name}")
                else:
                    self.print_status('WARN', f"Missing file: {file_name}", "May affect functionality")
                    results['warnings'].append(f"Missing essential file: {file_name}")
        else:
            self.print_status('FAIL', "Site directory not created", "Build may have failed silently")
            self.results['blocking_issues'].append("Site directory not created during build")
        
        # Performance check
        if build_time > 60:
            self.print_status('WARN', "Build time is slow", f"{build_time:.1f}s > 60s")
            self.results['warnings'].append("Build process is slower than recommended")
        
        return results
    
    def check_deployment_workflow(self) -> Dict[str, Any]:
        """Validate deployment workflow with Act"""
        self.print_header("Deployment Workflow Check")
        
        results = {'workflow_valid': False, 'act_available': False, 'simulation_success': False}
        
        # Check if Act is available
        success, stdout, stderr = self.run_command(["act", "--version"])
        if success:
            self.print_status('PASS', "Act is available", stdout.strip())
            results['act_available'] = True
        else:
            self.print_status('WARN', "Act not available", "Cannot simulate workflow locally")
            self.results['warnings'].append("Act not available for workflow simulation")
            return results
        
        # Check workflow file
        workflow_file = self.project_root / ".github" / "workflows" / "deploy.yml"
        if not workflow_file.exists():
            self.print_status('FAIL', "Deployment workflow missing", "No deploy.yml found")
            self.results['blocking_issues'].append("Deployment workflow file missing")
            return results
        
        # Validate workflow syntax with Act
        success, stdout, stderr = self.run_command([
            "act", "--list", "--workflows", str(workflow_file)
        ])
        
        if success:
            self.print_status('PASS', "Workflow syntax is valid")
            results['workflow_valid'] = True
        else:
            self.print_status('FAIL', "Workflow syntax error", stderr)
            self.results['blocking_issues'].append("Deployment workflow has syntax errors")
            return results
        
        # Simulate workflow execution
        self.print_status('INFO', "Simulating workflow execution", "This may take a moment...")
        success, stdout, stderr = self.run_command([
            "act", "push",
            "--workflows", str(workflow_file),
            "--env", "ACT=true",
            "--env", "SKIP_DEPLOY=true"
        ], timeout=300)
        
        if success:
            self.print_status('PASS', "Workflow simulation successful")
            results['simulation_success'] = True
        else:
            self.print_status('WARN', "Workflow simulation issues", "Check configuration")
            self.results['warnings'].append("Workflow simulation encountered issues")
        
        return results
    
    def check_git_repository(self) -> Dict[str, Any]:
        """Check Git repository status"""
        self.print_header("Git Repository Check")
        
        results = {'is_git_repo': False, 'clean_working_tree': False, 'on_main_branch': False}
        
        # Check if it's a Git repository
        success, stdout, stderr = self.run_command(["git", "status"])
        if not success:
            self.print_status('FAIL', "Not a Git repository", "Initialize Git repository first")
            self.results['blocking_issues'].append("Project is not a Git repository")
            return results
        
        results['is_git_repo'] = True
        self.print_status('PASS', "Git repository detected")
        
        # Check working tree status
        if "nothing to commit, working tree clean" in stdout:
            self.print_status('PASS', "Working tree is clean")
            results['clean_working_tree'] = True
        else:
            self.print_status('WARN', "Working tree has changes", "Consider committing changes before deployment")
            self.results['warnings'].append("Uncommitted changes in working tree")
        
        # Check current branch
        success, stdout, stderr = self.run_command(["git", "branch", "--show-current"])
        if success:
            current_branch = stdout.strip()
            if current_branch == "main":
                self.print_status('PASS', f"On main branch", current_branch)
                results['on_main_branch'] = True
            else:
                self.print_status('WARN', f"Not on main branch", f"Current: {current_branch}")
                if self.environment == "production":
                    self.results['warnings'].append(f"Not on main branch for production deployment")
        
        return results
    
    def run_comprehensive_tests(self) -> Dict[str, Any]:
        """Run comprehensive test suite"""
        self.print_header("Comprehensive Tests")
        
        results = {'tests_passed': False, 'test_results': {}}
        
        # Check if test runner exists
        test_runner = self.project_root / "run_tests.py"
        if not test_runner.exists():
            self.print_status('WARN', "Test runner not found", "Cannot run comprehensive tests")
            self.results['warnings'].append("No comprehensive test runner available")
            return results
        
        # Run comprehensive tests
        self.print_status('INFO', "Running comprehensive tests", "This may take several minutes...")
        success, stdout, stderr = self.run_command([
            sys.executable, "run_tests.py", "comprehensive"
        ], timeout=600)
        
        if success:
            self.print_status('PASS', "All comprehensive tests passed")
            results['tests_passed'] = True
        else:
            self.print_status('FAIL', "Some tests failed", "Review test output for details")
            self.results['blocking_issues'].append("Comprehensive tests are failing")
        
        # Parse test results if possible
        if "passed" in stdout or "failed" in stdout:
            # Extract basic test statistics
            lines = stdout.split('\n')
            for line in lines:
                if "passed" in line and "failed" in line:
                    results['test_results']['summary'] = line.strip()
                    break
        
        return results
    
    def calculate_confidence_score(self) -> int:
        """Calculate deployment confidence score (0-100)"""
        score = 100
        
        # Deduct points for blocking issues
        score -= len(self.results['blocking_issues']) * 25
        
        # Deduct points for warnings
        score -= len(self.results['warnings']) * 5
        
        # Ensure score doesn't go below 0
        score = max(0, score)
        
        return score
    
    def generate_deployment_checklist(self) -> List[str]:
        """Generate actionable deployment checklist"""
        checklist = []
        
        if self.results['blocking_issues']:
            checklist.append("🚨 BLOCKING ISSUES - Must fix before deployment:")
            for issue in self.results['blocking_issues']:
                checklist.append(f"   • {issue}")
            checklist.append("")
        
        if self.results['warnings']:
            checklist.append("⚠️ WARNINGS - Recommended to fix:")
            for warning in self.results['warnings']:
                checklist.append(f"   • {warning}")
            checklist.append("")
        
        if self.results['recommendations']:
            checklist.append("💡 RECOMMENDATIONS:")
            for rec in self.results['recommendations']:
                checklist.append(f"   • {rec}")
            checklist.append("")
        
        # Add deployment-specific recommendations
        if self.environment == "production":
            checklist.extend([
                "📋 PRE-DEPLOYMENT CHECKLIST:",
                "   • Ensure all team members are notified",
                "   • Backup current site if applicable",
                "   • Monitor deployment process",
                "   • Verify site functionality after deployment",
                ""
            ])
        
        return checklist
    
    def auto_fix_issues(self, auto_fix: bool = False) -> Dict[str, Any]:
        """Attempt to automatically fix common issues"""
        if not auto_fix:
            return {'fixes_attempted': 0, 'fixes_successful': 0}
        
        self.print_header("Auto-Fix Attempts")
        
        fixes = {'fixes_attempted': 0, 'fixes_successful': 0, 'fixes': []}
        
        # Auto-fix: Install missing dependencies
        if any("Missing critical package" in issue for issue in self.results['blocking_issues']):
            self.print_status('INFO', "Attempting to install missing packages")
            fixes['fixes_attempted'] += 1
            
            success, stdout, stderr = self.run_command([
                sys.executable, "-m", "pip", "install", "-r", 
                str(self.project_root / "dependencies" / "requirements.txt")
            ], timeout=120)
            
            if success:
                self.print_status('PASS', "Dependencies installed successfully")
                fixes['fixes_successful'] += 1
                fixes['fixes'].append("Installed missing Python dependencies")
            else:
                self.print_status('FAIL', "Failed to install dependencies", stderr)
        
        # Auto-fix: Create missing directories
        missing_dirs = ['.github/workflows', '.github/act', 'docs']
        for dir_path in missing_dirs:
            full_path = self.project_root / dir_path
            if not full_path.exists():
                fixes['fixes_attempted'] += 1
                try:
                    full_path.mkdir(parents=True, exist_ok=True)
                    self.print_status('PASS', f"Created directory: {dir_path}")
                    fixes['fixes_successful'] += 1
                    fixes['fixes'].append(f"Created missing directory: {dir_path}")
                except Exception as e:
                    self.print_status('FAIL', f"Failed to create directory: {dir_path}", str(e))
        
        return fixes
    
    def run_full_check(self, auto_fix: bool = False) -> Dict[str, Any]:
        """Run complete deployment readiness check"""
        print(f"{Colors.CYAN}🔍 Deployment Readiness Check for {self.environment.upper()} environment{Colors.NC}")
        print(f"{Colors.CYAN}Project: {self.project_root}{Colors.NC}")
        
        # Run all checks
        checks = [
            ("Configuration Files", self.check_configuration_files),
            ("Dependencies", self.check_dependencies),
            ("MkDocs Configuration", self.check_mkdocs_configuration),
            ("Build Process", self.check_build_process),
            ("Git Repository", self.check_git_repository),
            ("Deployment Workflow", self.check_deployment_workflow),
            ("Comprehensive Tests", self.run_comprehensive_tests),
        ]
        
        for check_name, check_func in checks:
            try:
                result = check_func()
                self.results['checks'][check_name] = result
            except Exception as e:
                self.print_status('FAIL', f"{check_name} check failed", str(e))
                self.results['blocking_issues'].append(f"{check_name} check encountered an error: {str(e)}")
        
        # Auto-fix if requested
        if auto_fix:
            fix_results = self.auto_fix_issues(auto_fix=True)
            self.results['auto_fix'] = fix_results
        
        # Calculate final status
        self.results['deployment_ready'] = len(self.results['blocking_issues']) == 0
        self.results['confidence_score'] = self.calculate_confidence_score()
        
        # Generate final report
        self.print_header("Deployment Readiness Summary")
        
        if self.results['deployment_ready']:
            self.print_status('PASS', f"🎉 DEPLOYMENT READY for {self.environment.upper()}")
            self.print_status('INFO', f"Confidence Score: {self.results['confidence_score']}/100")
        else:
            self.print_status('FAIL', f"❌ NOT READY for {self.environment.upper()} deployment")
            self.print_status('INFO', f"Confidence Score: {self.results['confidence_score']}/100")
            self.print_status('INFO', f"Blocking Issues: {len(self.results['blocking_issues'])}")
        
        if self.results['warnings']:
            self.print_status('WARN', f"Warnings: {len(self.results['warnings'])}")
        
        # Show checklist
        checklist = self.generate_deployment_checklist()
        if checklist:
            print(f"\n{Colors.YELLOW}📋 DEPLOYMENT CHECKLIST:{Colors.NC}")
            for item in checklist:
                print(item)
        
        return self.results


def main():
    parser = argparse.ArgumentParser(
        description="Validate complete deployment readiness with automated checks",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python project-deployment-ready.py                    # Check production readiness
  python project-deployment-ready.py --env staging     # Check staging readiness
  python project-deployment-ready.py --auto-fix        # Check and attempt auto-fixes
  python project-deployment-ready.py --save-report     # Save detailed report
        """
    )
    
    parser.add_argument(
        "--env", "--environment",
        choices=["staging", "production"],
        default="production",
        help="Target deployment environment (default: production)"
    )
    
    parser.add_argument(
        "--auto-fix",
        action="store_true",
        help="Attempt to automatically fix common issues"
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
    
    # Initialize checker
    checker = DeploymentReadinessChecker(args.project_root, args.env)
    
    try:
        # Run full check
        results = checker.run_full_check(auto_fix=args.auto_fix)
        
        # Save report if requested
        if args.save_report:
            with open(args.save_report, 'w') as f:
                json.dump(results, f, indent=2, default=str)
            print(f"\n{Colors.GREEN}📄 Report saved to: {args.save_report}{Colors.NC}")
        
        # Exit with appropriate code
        sys.exit(0 if results['deployment_ready'] else 1)
        
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}⚠️ Check interrupted by user{Colors.NC}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}❌ Unexpected error: {e}{Colors.NC}")
        sys.exit(1)


if __name__ == "__main__":
    main()