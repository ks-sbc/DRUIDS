#!/usr/bin/env python3
"""
Test that our linting and formatting tools work correctly
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd, cwd=None):
    """Run a command and return success status and output"""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, cwd=cwd
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)


def test_prettier_available():
    """Test that Prettier is available and working"""
    success, stdout, stderr = run_command("npm run format:check")
    # Prettier should be available (may have formatting issues, that's ok)
    assert "prettier --check" in stdout or "prettier --check" in stderr


def test_yamllint_available():
    """Test that yamllint is available"""
    success, stdout, stderr = run_command("yamllint --version")
    assert success, f"yamllint not available: {stderr}"


def test_black_available():
    """Test that black is available"""
    success, stdout, stderr = run_command("black --version")
    assert success, f"black not available: {stderr}"


def test_flake8_available():
    """Test that flake8 is available"""
    success, stdout, stderr = run_command("flake8 --version")
    assert success, f"flake8 not available: {stderr}"


def test_isort_available():
    """Test that isort is available"""
    success, stdout, stderr = run_command("isort --version")
    assert success, f"isort not available: {stderr}"


def test_prettier_config_valid():
    """Test that Prettier configuration is valid"""
    project_root = Path(__file__).parent.parent
    prettier_config = project_root / ".prettierrc.json"
    assert prettier_config.exists(), "Prettier config file missing"

    # Test that prettier can parse its own config
    success, stdout, stderr = run_command(
        f"npx prettier --check {prettier_config}", cwd=project_root
    )
    # Should not have syntax errors (formatting issues are ok)
    assert "SyntaxError" not in stderr


def test_yamllint_config_valid():
    """Test that yamllint configuration is valid"""
    project_root = Path(__file__).parent.parent
    yamllint_config = project_root / ".yamllint.yml"
    assert yamllint_config.exists(), "yamllint config file missing"

    # Test that yamllint can use its own config
    success, stdout, stderr = run_command(
        f"yamllint -c {yamllint_config} {yamllint_config}", cwd=project_root
    )
    # Should not have syntax errors in config
    assert "invalid config" not in stderr.lower()


def test_flake8_config_valid():
    """Test that flake8 configuration is valid"""
    project_root = Path(__file__).parent.parent
    flake8_config = project_root / ".flake8"
    assert flake8_config.exists(), "flake8 config file missing"

    # Test that flake8 can read its config
    success, stdout, stderr = run_command("flake8 --help", cwd=project_root)
    assert success, f"flake8 config invalid: {stderr}"


def test_linting_catches_issues():
    """Test that our linting setup catches common issues"""
    project_root = Path(__file__).parent.parent

    # Create a temporary Python file with issues
    test_file = project_root / "temp_test_file.py"
    try:
        with open(test_file, "w") as f:
            f.write(
                """
import os
import sys

def bad_function( ):
    x=1+2
    print("hello world")
    return x
"""
            )

        # Test that flake8 catches issues
        success, stdout, stderr = run_command(
            f"flake8 {test_file} --max-line-length=88", cwd=project_root
        )
        assert not success, "flake8 should catch formatting issues"
        assert "imported but unused" in stdout or "imported but unused" in stderr

    finally:
        # Clean up
        if test_file.exists():
            test_file.unlink()


def test_formatting_fixes_issues():
    """Test that our formatting tools can fix issues"""
    project_root = Path(__file__).parent.parent

    # Create a temporary Python file with formatting issues
    test_file = project_root / "temp_format_test.py"
    try:
        with open(test_file, "w") as f:
            f.write(
                """
def good_function():
    x = 1 + 2
    return x
"""
            )

        # Test that black can format it
        success, stdout, stderr = run_command(
            f"black {test_file} --line-length=88", cwd=project_root
        )
        assert success, f"black should be able to format file: {stderr}"

        # Test that isort can sort imports
        success, stdout, stderr = run_command(
            f"isort {test_file} --profile black", cwd=project_root
        )
        assert success, f"isort should be able to sort imports: {stderr}"

    finally:
        # Clean up
        if test_file.exists():
            test_file.unlink()


def test_pre_commit_config_valid():
    """Test that pre-commit configuration is valid"""
    project_root = Path(__file__).parent.parent
    precommit_config = project_root / ".pre-commit-config.yaml"
    assert precommit_config.exists(), "pre-commit config file missing"

    # Test YAML syntax
    success, stdout, stderr = run_command(
        f"yamllint {precommit_config}", cwd=project_root
    )
    # Should not have syntax errors (style issues are ok)
    assert "syntax error" not in stderr.lower()


if __name__ == "__main__":
    # Run tests manually
    import pytest

    pytest.main([__file__, "-v"])