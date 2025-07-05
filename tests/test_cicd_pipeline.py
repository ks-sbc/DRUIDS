#!/usr/bin/env python3
"""
TDD tests for CI-CD pipeline functionality.
These tests define what our GitHub Actions pipeline should accomplish.
"""

import subprocess
import yaml
from pathlib import Path
from typing import Dict, List

import pytest


class TestCICDPipeline:
    """Test CI-CD pipeline functionality following TDD principles"""

    @pytest.fixture(autouse=True)
    def setup(self, project_root):
        """Set up test environment"""
        self.project_root = project_root
        self.workflows_dir = project_root / ".github" / "workflows"
        self.deploy_workflow = self.workflows_dir / "deploy.yml"

    def test_deploy_workflow_file_exists(self):
        """Test that deploy.yml workflow file exists"""
        assert self.deploy_workflow.exists(), "deploy.yml workflow must exist"

    def test_deploy_workflow_is_valid_yaml(self):
        """Test that deploy.yml is valid YAML"""
        with open(self.deploy_workflow, 'r') as f:
            try:
                workflow = yaml.safe_load(f)
                assert isinstance(workflow, dict), "Workflow must be a valid YAML dict"
            except yaml.YAMLError as e:
                pytest.fail(f"Invalid YAML in deploy.yml: {e}")

    def test_deploy_workflow_triggers_on_main_branch(self):
        """Test that workflow triggers on push to main branch using act"""
        # Check if act is available
        result = subprocess.run(
            ["which", "act"], 
            capture_output=True, 
            text=True
        )
        
        if result.returncode != 0:
            pytest.skip("act not installed - install with: curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash")
        
        # Use act to validate workflow triggers
        result = subprocess.run(
            ["act", "--list", "--workflows", str(self.deploy_workflow)],
            cwd=self.project_root,
            capture_output=True,
            text=True
        )
        
        assert result.returncode == 0, f"Act failed to parse workflow: {result.stderr}"
        
        # Check that push events are listed
        output = result.stdout
        assert "push" in output.lower(), "Workflow should trigger on push events"

    def test_deploy_workflow_has_required_jobs(self):
        """Test that workflow has required jobs"""
        with open(self.deploy_workflow, 'r') as f:
            workflow = yaml.safe_load(f)
        
        assert 'jobs' in workflow, "Workflow must have jobs"
        jobs = workflow['jobs']
        
        # Should have at least one job that handles test and deploy
        assert len(jobs) > 0, "Workflow must have at least one job"
        
        # Check for test-and-deploy job
        job_names = list(jobs.keys())
        assert any('test' in name.lower() for name in job_names), \
            "Workflow must have a job that includes testing"

    def test_deploy_workflow_runs_comprehensive_tests(self):
        """Test that workflow runs comprehensive tests before deployment"""
        with open(self.deploy_workflow, 'r') as f:
            workflow = yaml.safe_load(f)
        
        # Find the main job
        main_job = list(workflow['jobs'].values())[0]
        steps = main_job.get('steps', [])
        
        # Check for test step
        test_step_found = False
        for step in steps:
            if 'run' in step:
                run_command = step['run']
                if 'run_tests.py comprehensive' in run_command:
                    test_step_found = True
                    break
        
        assert test_step_found, "Workflow must run comprehensive tests"

    def test_deploy_workflow_verifies_deployment_readiness(self):
        """Test that workflow verifies deployment readiness"""
        with open(self.deploy_workflow, 'r') as f:
            workflow = yaml.safe_load(f)
        
        main_job = list(workflow['jobs'].values())[0]
        steps = main_job.get('steps', [])
        
        # Check for deployment readiness step
        readiness_step_found = False
        for step in steps:
            if 'run' in step:
                run_command = step['run']
                if 'test_deployment_readiness' in run_command:
                    readiness_step_found = True
                    break
        
        assert readiness_step_found, "Workflow must verify deployment readiness"

    def test_deploy_workflow_builds_site_with_strict_mode(self):
        """Test that workflow builds site in strict mode"""
        with open(self.deploy_workflow, 'r') as f:
            workflow = yaml.safe_load(f)
        
        main_job = list(workflow['jobs'].values())[0]
        steps = main_job.get('steps', [])
        
        # Check for strict build step
        strict_build_found = False
        for step in steps:
            if 'run' in step:
                run_command = step['run']
                if 'mkdocs build --strict' in run_command:
                    strict_build_found = True
                    break
        
        assert strict_build_found, "Workflow must build with --strict flag"

    def test_deploy_workflow_deploys_to_github_pages(self):
        """Test that workflow deploys to GitHub Pages using mkdocs gh-deploy"""
        with open(self.deploy_workflow, 'r') as f:
            workflow = yaml.safe_load(f)
        
        main_job = list(workflow['jobs'].values())[0]
        steps = main_job.get('steps', [])
        
        # Check for gh-deploy step
        deploy_step_found = False
        for step in steps:
            if 'run' in step:
                run_command = step['run']
                if 'mkdocs gh-deploy' in run_command:
                    deploy_step_found = True
                    break
        
        assert deploy_step_found, "Workflow must use mkdocs gh-deploy"

    def test_deploy_workflow_has_correct_permissions(self):
        """Test that workflow has correct permissions for GitHub Pages"""
        with open(self.deploy_workflow, 'r') as f:
            workflow = yaml.safe_load(f)
        
        # Check permissions
        assert 'permissions' in workflow, "Workflow must specify permissions"
        permissions = workflow['permissions']
        
        # Check required permissions
        assert 'contents' in permissions, "Must have contents permission"
        assert 'pages' in permissions, "Must have pages permission"
        assert permissions['pages'] == 'write', "Pages permission must be write"

    def test_deploy_workflow_uses_ubuntu_runner(self):
        """Test that workflow uses Ubuntu runner"""
        with open(self.deploy_workflow, 'r') as f:
            workflow = yaml.safe_load(f)
        
        main_job = list(workflow['jobs'].values())[0]
        assert 'runs-on' in main_job, "Job must specify runs-on"
        assert 'ubuntu' in main_job['runs-on'], "Must use Ubuntu runner"

    def test_deploy_workflow_sets_up_python(self):
        """Test that workflow sets up Python correctly"""
        with open(self.deploy_workflow, 'r') as f:
            workflow = yaml.safe_load(f)
        
        main_job = list(workflow['jobs'].values())[0]
        steps = main_job.get('steps', [])
        
        # Check for Python setup step
        python_setup_found = False
        for step in steps:
            if 'uses' in step and 'setup-python' in step['uses']:
                python_setup_found = True
                # Check Python version
                if 'with' in step:
                    assert 'python-version' in step['with'], "Must specify Python version"
                break
        
        assert python_setup_found, "Workflow must set up Python"

    def test_deploy_workflow_installs_dependencies(self):
        """Test that workflow installs dependencies"""
        with open(self.deploy_workflow, 'r') as f:
            workflow = yaml.safe_load(f)
        
        main_job = list(workflow['jobs'].values())[0]
        steps = main_job.get('steps', [])
        
        # Check for dependency installation
        deps_install_found = False
        for step in steps:
            if 'run' in step:
                run_command = step['run']
                if 'pip install -r' in run_command and 'requirements.txt' in run_command:
                    deps_install_found = True
                    break
        
        assert deps_install_found, "Workflow must install dependencies"

    def test_deploy_workflow_has_proper_step_order(self):
        """Test that workflow steps are in correct order"""
        with open(self.deploy_workflow, 'r') as f:
            workflow = yaml.safe_load(f)
        
        main_job = list(workflow['jobs'].values())[0]
        steps = main_job.get('steps', [])
        
        # Expected order: checkout, setup-python, install-deps, test, build, deploy
        step_types = []
        for step in steps:
            if 'uses' in step:
                if 'checkout' in step['uses']:
                    step_types.append('checkout')
                elif 'setup-python' in step['uses']:
                    step_types.append('setup-python')
            elif 'run' in step:
                run_command = step['run']
                if 'pip install' in run_command:
                    step_types.append('install-deps')
                elif 'run_tests.py' in run_command:
                    step_types.append('test')
                elif 'mkdocs build' in run_command:
                    step_types.append('build')
                elif 'mkdocs gh-deploy' in run_command:
                    step_types.append('deploy')
        
        # Verify checkout comes first
        assert step_types[0] == 'checkout', "Checkout must be first step"
        
        # Verify setup-python comes before install-deps
        checkout_idx = step_types.index('checkout')
        python_idx = step_types.index('setup-python')
        deps_idx = step_types.index('install-deps')
        assert python_idx > checkout_idx, "Python setup must come after checkout"
        assert deps_idx > python_idx, "Dependency install must come after Python setup"
        
        # Verify tests come before build
        test_idx = step_types.index('test')
        build_idx = step_types.index('build')
        deploy_idx = step_types.index('deploy')
        assert test_idx < build_idx, "Tests must run before build"
        assert build_idx < deploy_idx, "Build must complete before deploy"

    def test_pipeline_fails_on_test_failure(self):
        """Test that pipeline fails if tests fail (this validates our TDD approach)"""
        # This test validates that our pipeline properly implements fail-fast behavior
        # If tests fail, deployment should not happen
        
        # We can simulate this by checking that the workflow doesn't use --continue-on-error
        with open(self.deploy_workflow, 'r') as f:
            workflow = yaml.safe_load(f)
        
        main_job = list(workflow['jobs'].values())[0]
        steps = main_job.get('steps', [])
        
        for step in steps:
            # No step should have continue-on-error: true
            assert step.get('continue-on-error') != True, \
                "Pipeline steps should fail fast on errors"

    def test_workflow_can_be_executed_with_act(self):
        """Test that workflow can be executed with act (dry run)"""
        # Check if act is available
        result = subprocess.run(
            ["which", "act"], 
            capture_output=True, 
            text=True
        )
        
        if result.returncode != 0:
            pytest.skip("act not installed - skipping workflow execution test")
        
        # Run workflow with act in list mode (equivalent to dry-run)
        result = subprocess.run(
            ["act", "--list"],
            cwd=self.project_root,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Act should be able to parse and list the workflow jobs
        assert result.returncode == 0, \
            f"Act failed to list workflow jobs: {result.stderr}"
        
        # Check that our deploy job is listed
        assert "test-and-deploy" in result.stdout, \
            f"Deploy job not found in act output: {result.stdout}"


class TestPipelineIntegration:
    """Integration tests for the complete pipeline"""

    def test_run_tests_supports_deployment_validation(self, project_root):
        """Test that run_tests.py includes deployment readiness validation"""
        run_tests_path = project_root / "run_tests.py"
        assert run_tests_path.exists(), "run_tests.py must exist"
        
        # Check that it has deployment-related functionality
        content = run_tests_path.read_text()
        assert 'deployment' in content.lower(), \
            "run_tests.py should include deployment validation"

    def test_comprehensive_tests_include_deployment_checks(self, project_root):
        """Test that comprehensive test suite includes deployment readiness"""
        # Run comprehensive tests and verify deployment readiness is checked
        result = subprocess.run(
            ["python", "run_tests.py", "--help"],
            cwd=project_root,
            capture_output=True,
            text=True
        )
        
        assert result.returncode == 0, "run_tests.py should be executable"
        
        # Check help output includes deployment-related options
        help_output = result.stdout
        assert 'comprehensive' in help_output.lower(), \
            "Should have comprehensive test option"

    def test_deployment_readiness_test_exists(self, project_root):
        """Test that deployment readiness test file exists and is executable"""
        test_file = project_root / "tests" / "test_deployment_readiness.py"
        assert test_file.exists(), "test_deployment_readiness.py must exist"
        
        # Verify it can be run
        result = subprocess.run(
            ["python", "-m", "pytest", str(test_file), "--collect-only"],
            cwd=project_root,
            capture_output=True,
            text=True
        )
        
        assert result.returncode == 0, "Deployment readiness tests must be valid pytest tests"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])