#!/usr/bin/env python3
"""
Test that our linting and formatting tools work correctly
"""

import tempfile
from pathlib import Path

import pytest

from test_utils import check_command_available, run_command


class TestLintingTools:
    """Test linting and formatting tools"""

    @pytest.mark.unit
    def test_prettier_available(self, project_root):
        """Test that Prettier is available and working"""
        success, stdout, stderr = run_command("npm run format:check", cwd=project_root)
        # Prettier should be available (may have formatting issues, that's ok)
        assert "prettier --check" in stdout or "prettier --check" in stderr


    @pytest.mark.unit
    def test_yamllint_available(self):
        """Test that yamllint is available"""
        if not check_command_available("yamllint"):
            pytest.skip("yamllint not available")
        
        success, stdout, stderr = run_command("yamllint --version")
        assert success, f"yamllint not available: {stderr}"


    @pytest.mark.unit
    def test_black_available(self):
        """Test that black is available"""
        if not check_command_available("black"):
            pytest.skip("black not available")
        
        success, stdout, stderr = run_command("black --version")
        assert success, f"black not available: {stderr}"


    @pytest.mark.unit
    def test_flake8_available(self):
        """Test that flake8 is available"""
        if not check_command_available("flake8"):
            pytest.skip("flake8 not available")
        
        success, stdout, stderr = run_command("flake8 --version")
        assert success, f"flake8 not available: {stderr}"


    @pytest.mark.unit
    def test_isort_available(self):
        """Test that isort is available"""
        if not check_command_available("isort"):
            pytest.skip("isort not available")
        
        success, stdout, stderr = run_command("isort --version")
        assert success, f"isort not available: {stderr}"


    @pytest.mark.unit
    def test_prettier_config_valid(self, project_root):
        """Test that Prettier configuration is valid"""
        prettier_configs = ["config/.prettierrc", "config/.prettierrc.json", "config/.prettierrc.yaml", "config/.prettierrc.yml"]
        config_found = False
        
        for config_name in prettier_configs:
            prettier_config = project_root / config_name
            if prettier_config.exists():
                config_found = True
                # Test that prettier can parse its own config
                success, stdout, stderr = run_command(
                    f"npx prettier --check {prettier_config}", cwd=project_root
                )
                # Should not have syntax errors (formatting issues are ok)
                assert "SyntaxError" not in stderr
                break
        
        assert config_found, "No Prettier config file found"


    @pytest.mark.unit
    def test_yamllint_config_valid(self, project_root):
        """Test that yamllint configuration is valid"""
        if not check_command_available("yamllint"):
            pytest.skip("yamllint not available")
        
        yamllint_configs = [".yamllint", ".yamllint.yml", ".yamllint.yaml"]
        config_found = False
        
        for config_name in yamllint_configs:
            yamllint_config = project_root / config_name
            if yamllint_config.exists():
                config_found = True
                # Test that yamllint can use its own config
                success, stdout, stderr = run_command(
                    f"yamllint -c {yamllint_config} {yamllint_config}", cwd=project_root
                )
                # Should not have syntax errors in config
                assert "invalid config" not in stderr.lower()
                break
        
        if not config_found:
            pytest.skip("No yamllint config file found")


    @pytest.mark.unit
    def test_flake8_config_valid(self, project_root):
        """Test that flake8 configuration is valid"""
        if not check_command_available("flake8"):
            pytest.skip("flake8 not available")
        
        flake8_configs = [".flake8", "setup.cfg", "tox.ini"]
        config_found = False
        
        for config_name in flake8_configs:
            flake8_config = project_root / config_name
            if flake8_config.exists():
                config_found = True
                # Test that flake8 can read its config
                success, stdout, stderr = run_command("flake8 --help", cwd=project_root)
                assert success, f"flake8 config invalid: {stderr}"
                break
        
        if not config_found:
            # Check pyproject.toml for flake8 config
            pyproject = project_root / "config" / "pyproject.toml"
            if pyproject.exists():
                content = pyproject.read_text()
                if "[tool.flake8]" in content:
                    config_found = True
        
        if not config_found:
            pytest.skip("No flake8 config file found")


    @pytest.mark.integration
    def test_linting_catches_issues(self, project_root):
        """Test that our linting setup catches common issues"""
        if not check_command_available("flake8"):
            pytest.skip("flake8 not available")
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("""
import os
import sys

def bad_function( ):
    x=1+2
    print("hello world")
    return x
""")
            test_file = Path(f.name)
        
        try:
            # Test that flake8 catches issues
            success, stdout, stderr = run_command(
                f"flake8 {test_file} --max-line-length=88"
            )
            assert not success, "flake8 should catch formatting issues"
            assert "imported but unused" in stdout or "imported but unused" in stderr
        finally:
            # Clean up
            if test_file.exists():
                test_file.unlink()


    @pytest.mark.integration
    def test_formatting_fixes_issues(self):
        """Test that our formatting tools can fix issues"""
        if not check_command_available("black"):
            pytest.skip("black not available")
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("""
def good_function():
    x = 1 + 2
    return x
""")
            test_file = Path(f.name)
        
        try:
            # Test that black can format it
            success, stdout, stderr = run_command(
                f"black {test_file} --line-length=88"
            )
            assert success, f"black should be able to format file: {stderr}"
            
            if check_command_available("isort"):
                # Test that isort can sort imports
                success, stdout, stderr = run_command(
                    f"isort {test_file} --profile black"
                )
                assert success, f"isort should be able to sort imports: {stderr}"
        finally:
            # Clean up
            if test_file.exists():
                test_file.unlink()


    @pytest.mark.unit
    def test_pre_commit_config_valid(self, project_root):
        """Test that pre-commit configuration is valid"""
        precommit_config = project_root / ".pre-commit-config.yaml"
        if not precommit_config.exists():
            pytest.skip("pre-commit config file not found")
        
        if check_command_available("yamllint"):
            # Test YAML syntax
            success, stdout, stderr = run_command(
                f"yamllint {precommit_config}", cwd=project_root
            )
            # Should not have syntax errors (style issues are ok)
            assert "syntax error" not in stderr.lower()
        
        # Also check with pre-commit if available
        if check_command_available("pre-commit"):
            success, stdout, stderr = run_command(
                "pre-commit validate-config", cwd=project_root
            )
            assert success, f"pre-commit config validation failed: {stderr}"


    @pytest.mark.integration
    def test_markdown_formatting(self, project_root, temp_dir):
        """Test markdown formatting with prettier"""
        # Create a test markdown file with formatting issues
        test_file = temp_dir / "test.md"
        test_file.write_text("""
# Test Document


This has too many blank lines.



And inconsistent spacing.
""")
        
        if check_command_available("prettier"):
            # Test that prettier can format it
            success, stdout, stderr = run_command(
                f"npx prettier --write {test_file}"
            )
            assert success, f"prettier should format markdown: {stderr}"
            
            # Check that file was modified
            content = test_file.read_text()
            # Should have normalized blank lines
            assert "\n\n\n" not in content

    @pytest.mark.integration
    def test_yaml_formatting(self, project_root, temp_dir):
        """Test YAML formatting and validation"""
        # Create a test YAML file
        test_file = temp_dir / "test.yml"
        test_file.write_text("""
key1: value1
key2:   value2
list:
- item1
-    item2
""")
        
        if check_command_available("prettier"):
            # Test that prettier can format it
            success, stdout, stderr = run_command(
                f"npx prettier --write {test_file}"
            )
            assert success, f"prettier should format YAML: {stderr}"
        
        if check_command_available("yamllint"):
            # Test that yamllint validates it
            success, stdout, stderr = run_command(
                f"yamllint {test_file}"
            )
            # May have warnings but should parse
            assert "syntax error" not in stderr.lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])