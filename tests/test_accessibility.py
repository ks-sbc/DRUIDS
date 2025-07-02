#!/usr/bin/env python3
"""
Accessibility tests using pa11y to ensure WCAG compliance and usability.
These tests check for color contrast, keyboard navigation, and screen reader compatibility.
"""

import json
import subprocess
import time
from pathlib import Path
import pytest
from test_utils import run_command


class TestAccessibility:
    """Test accessibility compliance using pa11y"""
    
    @pytest.fixture(scope="class")
    def mkdocs_server(self):
        """Start MkDocs server for accessibility testing"""
        project_root = Path(__file__).parent.parent
        
        # Start server in background
        process = subprocess.Popen(
            ["mkdocs", "serve", "--dev-addr", "0.0.0.0:8000"],
            cwd=project_root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Wait for server to start
        time.sleep(5)
        
        yield process
        
        # Clean up
        process.terminate()
        process.wait()
    
    def test_pa11y_installed(self):
        """Verify pa11y-ci is installed and available"""
        success, stdout, stderr = run_command("npx pa11y-ci --version")
        assert success, f"pa11y-ci not installed: {stderr}"
        assert "pa11y-ci" in stdout or stderr
    
    def test_wcag_compliance(self, mkdocs_server):
        """Test WCAG 2.1 AA compliance across all pages"""
        project_root = Path(__file__).parent.parent
        
        # Run pa11y-ci
        success, stdout, stderr = run_command(
            "npx pa11y-ci",
            cwd=project_root
        )
        
        # Check for specific accessibility issues we expect to find
        if not success:
            # Parse the output to understand failures
            issues = []
            if "color contrast" in stderr.lower():
                issues.append("Color contrast issues found")
            if "missing alt" in stderr.lower():
                issues.append("Missing alt text on images")
            if "heading" in stderr.lower():
                issues.append("Heading structure issues")
            if "landmark" in stderr.lower():
                issues.append("Missing ARIA landmarks")
            
            # We expect these to fail initially (TDD red phase)
            pytest.fail(f"Accessibility issues found: {', '.join(issues) if issues else stderr}")
    
    def test_keyboard_navigation(self, mkdocs_server):
        """Test keyboard navigation functionality"""
        # This test checks for proper focus indicators and tab order
        # We'll use pa11y with specific actions
        project_root = Path(__file__).parent.parent
        
        config = {
            "defaults": {
                "standard": "WCAG2AA",
                "timeout": 30000
            },
            "urls": [{
                "url": "http://localhost:8000/",
                "actions": [
                    "wait for element body to be visible",
                    "press Tab",
                    "wait for 200"
                ]
            }]
        }
        
        # Write temporary config
        temp_config = project_root / "temp_pa11y.json"
        with open(temp_config, 'w') as f:
            json.dump(config, f)
        
        try:
            success, stdout, stderr = run_command(
                f"npx pa11y-ci -c {temp_config}",
                cwd=project_root
            )
            
            if not success and "focus" in stderr.lower():
                pytest.fail("Keyboard navigation issues: Missing or improper focus indicators")
        finally:
            temp_config.unlink(missing_ok=True)
    
    def test_color_contrast(self, mkdocs_server):
        """Test color contrast ratios for the cyberpunk theme"""
        # Specifically test our theme colors
        project_root = Path(__file__).parent.parent
        
        # Test with specific color contrast rules
        config = {
            "defaults": {
                "standard": "WCAG2AA",
                "rules": ["color-contrast"],
                "timeout": 30000
            },
            "urls": [
                "http://localhost:8000/",
                "http://localhost:8000/test-features/"
            ]
        }
        
        temp_config = project_root / "temp_contrast.json"
        with open(temp_config, 'w') as f:
            json.dump(config, f)
        
        try:
            success, stdout, stderr = run_command(
                f"npx pa11y-ci -c {temp_config}",
                cwd=project_root
            )
            
            if not success:
                # We expect contrast issues with the current theme
                pytest.fail("Color contrast issues found - cyberpunk theme needs adjustment")
        finally:
            temp_config.unlink(missing_ok=True)
    
    def test_responsive_accessibility(self, mkdocs_server):
        """Test accessibility at different viewport sizes"""
        # Mobile, tablet, and desktop viewports
        viewports = [
            {"width": 320, "height": 568},   # iPhone SE
            {"width": 768, "height": 1024},  # iPad
            {"width": 1920, "height": 1080}  # Desktop
        ]
        
        project_root = Path(__file__).parent.parent
        
        for viewport in viewports:
            config = {
                "defaults": {
                    "standard": "WCAG2AA",
                    "viewport": viewport,
                    "timeout": 30000
                },
                "urls": ["http://localhost:8000/"]
            }
            
            temp_config = project_root / f"temp_viewport_{viewport['width']}.json"
            with open(temp_config, 'w') as f:
                json.dump(config, f)
            
            try:
                success, stdout, stderr = run_command(
                    f"npx pa11y-ci -c {temp_config}",
                    cwd=project_root
                )
                
                if not success:
                    pytest.fail(f"Accessibility issues at {viewport['width']}x{viewport['height']}: {stderr}")
            finally:
                temp_config.unlink(missing_ok=True)
    
    def test_aria_landmarks(self, mkdocs_server):
        """Test for proper ARIA landmarks"""
        # Check for header, nav, main, footer landmarks
        project_root = Path(__file__).parent.parent
        
        config = {
            "defaults": {
                "standard": "WCAG2AA",
                "rules": ["landmark-*", "region"],
                "timeout": 30000
            },
            "urls": ["http://localhost:8000/"]
        }
        
        temp_config = project_root / "temp_landmarks.json"
        with open(temp_config, 'w') as f:
            json.dump(config, f)
        
        try:
            success, stdout, stderr = run_command(
                f"npx pa11y-ci -c {temp_config}",
                cwd=project_root
            )
            
            if not success and ("landmark" in stderr.lower() or "region" in stderr.lower()):
                pytest.fail("Missing ARIA landmarks for navigation")
        finally:
            temp_config.unlink(missing_ok=True)
    
    def test_heading_structure(self, mkdocs_server):
        """Test for proper heading hierarchy"""
        project_root = Path(__file__).parent.parent
        
        config = {
            "defaults": {
                "standard": "WCAG2AA",
                "rules": ["heading-order", "empty-heading"],
                "timeout": 30000
            },
            "urls": [
                "http://localhost:8000/",
                "http://localhost:8000/test-features/"
            ]
        }
        
        temp_config = project_root / "temp_headings.json"
        with open(temp_config, 'w') as f:
            json.dump(config, f)
        
        try:
            success, stdout, stderr = run_command(
                f"npx pa11y-ci -c {temp_config}",
                cwd=project_root
            )
            
            if not success and "heading" in stderr.lower():
                pytest.fail("Heading structure issues - check h1-h6 hierarchy")
        finally:
            temp_config.unlink(missing_ok=True)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])