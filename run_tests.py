#!/usr/bin/env python3
"""
Comprehensive test runner for DRUIDS MkDocs project.
This replaces justfile-based testing with pure Python pytest workflow.
"""

import sys
import subprocess
from pathlib import Path
from typing import List, Optional


class TestRunner:
    """Pytest-based test runner with comprehensive options"""
    
    def __init__(self, project_root: Optional[Path] = None):
        self.project_root = project_root or Path(__file__).parent
        self.test_dir = self.project_root / "tests"
        
    def run_command(self, cmd: List[str], description: str) -> bool:
        """Run a command and return success status"""
        print(f"🔄 {description}")
        print(f"   Command: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(cmd, cwd=self.project_root, check=True)
            print(f"✅ {description} - PASSED")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ {description} - FAILED (exit code: {e.returncode})")
            return False
    
    def test_links(self) -> bool:
        """Run link validation tests"""
        return self.run_command([
            "python", "-m", "pytest", 
            "tests/test_build_quality.py", 
            "tests/test_links.py",
            "-v", "-m", "link_validation or build_quality"
        ], "Link Validation Tests")
    
    def test_static_analysis(self) -> bool:
        """Run static analysis tests"""
        return self.run_command([
            "python", "-m", "pytest",
            "tests/test_static_analysis.py",
            "-v", "-m", "static_analysis"
        ], "Static Analysis Tests")
    
    def test_content_structure(self) -> bool:
        """Run content structure tests"""
        return self.run_command([
            "python", "-m", "pytest",
            "tests/test_content_structure.py", 
            "-v", "-m", "content_structure"
        ], "Content Structure Tests")
    
    def test_build_quality(self) -> bool:
        """Run build quality tests"""
        return self.run_command([
            "python", "-m", "pytest",
            "tests/test_build_quality.py",
            "-v", "-m", "build_quality"
        ], "Build Quality Tests")
    
    def test_deployment_readiness(self) -> bool:
        """Run deployment readiness tests"""
        return self.run_command([
            "python", "-m", "pytest",
            "tests/test_deployment_readiness.py",
            "-v"
        ], "Deployment Readiness Tests")
    
    def test_workflow_with_act(self) -> bool:
        """Run workflow tests using Act"""
        return self.run_command([
            "python", "-m", "pytest",
            "tests/test_act_integration.py",
            "-v", "-k", "not test_act_workflow_steps_execute_in_order"
        ], "Act Workflow Tests")
    
    def test_unit_only(self) -> bool:
        """Run only fast unit tests"""
        return self.run_command([
            "python", "-m", "pytest",
            "tests/",
            "-v", "-m", "unit and not slow"
        ], "Unit Tests Only")
    
    def test_integration_only(self) -> bool:
        """Run only integration tests"""
        return self.run_command([
            "python", "-m", "pytest",
            "tests/",
            "-v", "-m", "integration"
        ], "Integration Tests Only")
    
    def test_comprehensive(self) -> bool:
        """Run all comprehensive tests"""
        tests = [
            ("Link Validation", self.test_links),
            ("Static Analysis", self.test_static_analysis), 
            ("Content Structure", self.test_content_structure),
            ("Build Quality", self.test_build_quality),
            ("Deployment Readiness", self.test_deployment_readiness),
            ("Workflow (Act)", self.test_workflow_with_act)
        ]
        
        print("🚀 Running Comprehensive Test Suite")
        print("=" * 50)
        
        results = []
        for name, test_func in tests:
            success = test_func()
            results.append((name, success))
            print()  # Add spacing between test suites
        
        # Summary
        print("📊 Test Results Summary")
        print("=" * 50)
        
        passed = 0
        for name, success in results:
            status = "✅ PASSED" if success else "❌ FAILED"
            print(f"  {name}: {status}")
            if success:
                passed += 1
        
        total = len(results)
        print(f"\nOverall: {passed}/{total} test suites passed")
        
        return passed == total
    
    def test_all(self) -> bool:
        """Run all tests including existing ones"""
        return self.run_command([
            "python", "-m", "pytest",
            "tests/",
            "-v"
        ], "All Tests")
    
    def test_with_coverage(self) -> bool:
        """Run tests with coverage report"""
        return self.run_command([
            "python", "-m", "pytest",
            "tests/",
            "--cov=tests",
            "--cov-report=html",
            "--cov-report=term-missing",
            "-v"
        ], "Tests with Coverage")
    
    def test_parallel(self) -> bool:
        """Run tests in parallel"""
        return self.run_command([
            "python", "-m", "pytest",
            "tests/",
            "-n", "auto",  # Requires pytest-xdist
            "-v"
        ], "Parallel Tests")
    
    def test_failed_only(self) -> bool:
        """Run only previously failed tests"""
        return self.run_command([
            "python", "-m", "pytest",
            "tests/",
            "--lf",  # last failed
            "-v"
        ], "Failed Tests Only")


def main():
    """Main CLI interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="DRUIDS MkDocs Test Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_tests.py links              # Test link validation
  python run_tests.py comprehensive      # Run all comprehensive tests  
  python run_tests.py all                # Run all tests
  python run_tests.py unit               # Run only unit tests
  python run_tests.py --coverage         # Run with coverage report
  python run_tests.py --parallel         # Run tests in parallel
        """
    )
    
    parser.add_argument(
        "test_type",
        choices=[
            "links", "static", "structure", "build-quality", "deployment", "workflow",
            "comprehensive", "all", "unit", "integration", "failed"
        ],
        help="Type of tests to run"
    )
    
    parser.add_argument(
        "--coverage", 
        action="store_true",
        help="Run with coverage report"
    )
    
    parser.add_argument(
        "--parallel",
        action="store_true", 
        help="Run tests in parallel (requires pytest-xdist)"
    )
    
    args = parser.parse_args()
    
    runner = TestRunner()
    
    # Handle special flags
    if args.coverage:
        success = runner.test_with_coverage()
    elif args.parallel:
        success = runner.test_parallel()
    else:
        # Handle test types
        test_methods = {
            "links": runner.test_links,
            "static": runner.test_static_analysis,
            "structure": runner.test_content_structure,
            "build-quality": runner.test_build_quality,
            "deployment": runner.test_deployment_readiness,
            "workflow": runner.test_workflow_with_act,
            "comprehensive": runner.test_comprehensive,
            "all": runner.test_all,
            "unit": runner.test_unit_only,
            "integration": runner.test_integration_only,
            "failed": runner.test_failed_only
        }
        
        success = test_methods[args.test_type]()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()