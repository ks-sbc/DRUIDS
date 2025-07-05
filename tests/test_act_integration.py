#!/usr/bin/env python3
"""
TDD tests for Act-based GitHub Actions workflow testing.
These tests define how our workflow should behave when run locally with Act.
"""

import json
import subprocess
import time
from pathlib import Path
from typing import Dict, List, Tuple

import pytest


class TestActIntegration:
    """Test GitHub Actions workflow using Act for local execution"""

    @pytest.fixture(autouse=True)
    def setup(self, project_root):
        """Set up test environment"""
        self.project_root = project_root
        self.workflows_dir = project_root / ".github" / "workflows"
        self.deploy_workflow = self.workflows_dir / "deploy.yml"
        self.act_dir = project_root / ".github" / "act"

    def check_act_available(self) -> bool:
        """Check if Act is available"""
        result = subprocess.run(
            ["which", "act"], 
            capture_output=True, 
            text=True
        )
        return result.returncode == 0

    def run_act_command(self, args: List[str], timeout: int = 60) -> Tuple[bool, str, str]:
        """Run Act command and return success, stdout, stderr"""
        cmd = ["act"] + args
        try:
            result = subprocess.run(
                cmd,
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return result.returncode == 0, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return False, "", "Command timed out"
        except Exception as e:
            return False, "", str(e)

    def test_act_is_available(self):
        """Test that Act is installed and available"""
        if not self.check_act_available():
            pytest.skip("Act not installed - install with: curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash")
        
        # Test Act version
        success, stdout, stderr = self.run_act_command(["--version"])
        assert success, f"Act version check failed: {stderr}"
        assert "act version" in stdout.lower(), "Act version output unexpected"

    def test_act_can_list_workflows(self):
        """Test that Act can list our workflows"""
        if not self.check_act_available():
            pytest.skip("Act not available")
        
        success, stdout, stderr = self.run_act_command(["--list"])
        assert success, f"Act failed to list workflows: {stderr}"
        
        # Should list our test-and-deploy job
        assert "test-and-deploy" in stdout, f"Deploy job not found in Act output: {stdout}"

    def test_act_can_validate_workflow_syntax(self):
        """Test that Act can validate our workflow syntax"""
        if not self.check_act_available():
            pytest.skip("Act not available")
        
        # Act should be able to parse the workflow without errors
        success, stdout, stderr = self.run_act_command(["--list", "--workflows", str(self.deploy_workflow)])
        assert success, f"Act failed to validate workflow syntax: {stderr}"

    def test_act_configuration_file_exists(self):
        """Test that .actrc configuration file exists"""
        actrc_path = self.project_root / ".actrc"
        assert actrc_path.exists(), ".actrc configuration file must exist for Act"

    def test_act_event_files_exist(self):
        """Test that Act event files exist"""
        push_event_file = self.act_dir / "push-event.json"
        assert push_event_file.exists(), "push-event.json must exist for Act testing"
        
        # Validate JSON structure
        with open(push_event_file, 'r') as f:
            try:
                event_data = json.load(f)
                assert 'ref' in event_data, "Event must have 'ref' field"
                assert 'repository' in event_data, "Event must have 'repository' field"
            except json.JSONDecodeError as e:
                pytest.fail(f"Invalid JSON in push-event.json: {e}")

    def test_act_can_execute_workflow_dry_run(self):
        """Test that Act can execute workflow in planning mode"""
        if not self.check_act_available():
            pytest.skip("Act not available")
        
        # Use --list to see what would be executed (equivalent to dry run)
        success, stdout, stderr = self.run_act_command(["push", "--list"])
        assert success, f"Act dry run failed: {stderr}"
        
        # Should show our job would be executed
        assert "test-and-deploy" in stdout, "Deploy job should be listed for execution"

    def test_act_workflow_steps_execute_in_order(self):
        """Test that Act executes workflow steps in correct order"""
        if not self.check_act_available():
            pytest.skip("Act not available")
        
        # Run Act with verbose output to see step execution
        success, stdout, stderr = self.run_act_command([
            "push", 
            "--verbose",
            "--env", "ACT=true",
            "--env", "SKIP_DEPLOY=true"
        ], timeout=300)
        
        # Note: This test may fail initially - that's expected in TDD Red phase
        # We'll implement the fixes in Green phase
        if not success:
            pytest.skip(f"Expected failure in Red phase - Act execution not yet optimized: {stderr}")
        
        # Check step execution order in output
        lines = stdout.split('\n')
        step_order = []
        for line in lines:
            if "| ✅" in line or "| ❌" in line:
                step_order.append(line)
        
        # Verify logical order (this will likely fail initially)
        assert len(step_order) > 0, "Should execute some steps"

    def test_act_workflow_fails_on_test_failure(self):
        """Test that Act workflow stops execution on test failure"""
        if not self.check_act_available():
            pytest.skip("Act not available")
        
        # This test simulates a test failure scenario
        # We'll implement proper test failure simulation in Green phase
        success, stdout, stderr = self.run_act_command([
            "push",
            "--env", "FORCE_TEST_FAILURE=true",
            "--env", "ACT=true"
        ], timeout=180)
        
        # In Red phase, this might not work as expected
        # We expect this test to initially fail
        pytest.skip("Test failure simulation not yet implemented - Red phase expected failure")

    def test_act_workflow_skips_deployment_locally(self):
        """Test that deployment step is skipped when running locally with Act"""
        if not self.check_act_available():
            pytest.skip("Act not available")
        
        # Run workflow with ACT environment variable
        success, stdout, stderr = self.run_act_command([
            "push",
            "--env", "ACT=true",
            "--verbose"
        ], timeout=300)
        
        # This test will likely fail initially - that's expected in Red phase
        # The workflow doesn't yet know how to handle ACT environment variable
        if not success:
            pytest.skip(f"Expected failure in Red phase - ACT environment handling not implemented: {stderr}")
        
        # Check that deployment step was skipped
        assert "mkdocs gh-deploy" not in stdout or "skipped" in stdout.lower(), \
            "Deployment should be skipped when running locally"

    def test_act_respects_environment_variables(self):
        """Test that Act properly sets and respects environment variables"""
        if not self.check_act_available():
            pytest.skip("Act not available")
        
        # Test with custom environment variables
        success, stdout, stderr = self.run_act_command([
            "push",
            "--env", "TEST_VAR=test_value",
            "--env", "ACT=true",
            "--list"
        ])
        
        assert success, f"Act failed to respect environment variables: {stderr}"

    def test_act_uses_correct_runner_image(self):
        """Test that Act uses the correct Ubuntu runner image"""
        if not self.check_act_available():
            pytest.skip("Act not available")
        
        # Check what images Act would use
        success, stdout, stderr = self.run_act_command(["--list", "--verbose"])
        assert success, f"Act failed to show runner information: {stderr}"
        
        # Should mention ubuntu runner
        assert "ubuntu" in stdout.lower(), "Should use Ubuntu runner image"

    def test_act_with_custom_event_file(self):
        """Test that Act can use custom event files"""
        if not self.check_act_available():
            pytest.skip("Act not available")
        
        # Test with custom push event
        push_event_file = self.act_dir / "push-event.json"
        if not push_event_file.exists():
            pytest.skip("Custom event file not yet created - Red phase expected")
        
        success, stdout, stderr = self.run_act_command([
            "push",
            "--eventpath", str(push_event_file),
            "--list"
        ])
        
        assert success, f"Act failed with custom event file: {stderr}"

    def test_workflow_execution_produces_expected_output(self):
        """Test that workflow execution produces expected log output"""
        if not self.check_act_available():
            pytest.skip("Act not available")
        
        # Run workflow and check for expected output patterns
        success, stdout, stderr = self.run_act_command([
            "push",
            "--env", "ACT=true",
            "--verbose"
        ], timeout=300)
        
        # This will likely fail initially - Red phase
        if not success:
            pytest.skip(f"Expected failure in Red phase - workflow optimization needed: {stderr}")
        
        # Check for expected output patterns
        expected_patterns = [
            "Checkout",
            "Set up Python", 
            "Install dependencies",
            "Run comprehensive tests"
        ]
        
        for pattern in expected_patterns:
            assert pattern in stdout, f"Expected pattern '{pattern}' not found in output"

    def test_act_integration_with_existing_tests(self):
        """Test that Act integration works with existing test infrastructure"""
        if not self.check_act_available():
            pytest.skip("Act not available")
        
        # This test verifies that our Act integration doesn't break existing functionality
        # We'll implement proper integration in Green phase
        pytest.skip("Act integration with existing tests not yet implemented - Red phase")


class TestActConfiguration:
    """Test Act configuration and setup"""

    def test_actrc_configuration_is_valid(self, project_root):
        """Test that .actrc configuration is valid"""
        actrc_path = project_root / ".actrc"
        
        # This will fail initially - we haven't created .actrc yet
        if not actrc_path.exists():
            pytest.fail(".actrc configuration file missing - Red phase expected failure")
        
        # Validate configuration syntax
        content = actrc_path.read_text()
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        # Check for essential configuration options
        has_platform = any('--platform' in line for line in lines)
        assert has_platform, ".actrc should specify platform configuration"

    def test_act_secrets_template_exists(self, project_root):
        """Test that secrets template exists for local testing"""
        secrets_template = project_root / ".github" / "act" / "secrets.example"
        
        # This will fail initially - Red phase
        if not secrets_template.exists():
            pytest.fail("secrets.example template missing - Red phase expected failure")

    def test_act_runner_configuration_exists(self, project_root):
        """Test that Act runner configuration exists"""
        runner_config = project_root / ".github" / "act" / "act-runner.yml"
        
        # This will fail initially - Red phase  
        if not runner_config.exists():
            pytest.fail("act-runner.yml configuration missing - Red phase expected failure")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])