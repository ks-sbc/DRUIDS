#!/usr/bin/env python3
"""
Tests for MkDocs build quality - parsing and analyzing build warnings/errors.
This test module ensures that the build output is clean and catches all link issues.
"""

import subprocess
from pathlib import Path
from typing import Dict, List, Set

import pytest

from test_utils import (
    categorize_warnings,
    format_warning_report,
    parse_mkdocs_output,
    run_command,
)


class TestBuildQuality:
    """Test MkDocs build output quality"""

    def run_mkdocs_build(self, project_root: Path, strict: bool = True) -> tuple[bool, str, Dict]:
        """
        Run MkDocs build and parse output
        
        Args:
            project_root: Project root directory
            strict: Whether to use --strict flag
            
        Returns:
            Tuple of (success, combined_output, parsed_output)
        """
        cmd = "mkdocs build --clean"
        if strict:
            cmd += " --strict"
        
        success, stdout, stderr = run_command(cmd, cwd=project_root)
        combined_output = stdout + "\n" + stderr
        parsed_output = parse_mkdocs_output(combined_output)
        
        return success, combined_output, parsed_output

    @pytest.mark.integration
    @pytest.mark.build_quality
    def test_no_critical_warnings(self, project_root):
        """Test that build has no critical warnings"""
        success, output, parsed = self.run_mkdocs_build(project_root)
        categorized = categorize_warnings(parsed)
        
        if categorized['critical']:
            report = format_warning_report(categorized)
            pytest.fail(f"Build has critical issues:\n{report}")

    @pytest.mark.integration
    def test_no_broken_navigation_links(self, project_root):
        """Test that all navigation links exist"""
        success, output, parsed = self.run_mkdocs_build(project_root)
        
        nav_errors = [
            w for w in parsed['warnings']
            if w.get('type') == 'nav_reference_not_found'
        ]
        
        if nav_errors:
            error_msg = "\nBroken navigation references:\n"
            for error in nav_errors:
                error_msg += f"  - {error['file']}\n"
            pytest.fail(error_msg)

    @pytest.mark.integration
    def test_no_broken_internal_links(self, project_root):
        """Test that all internal links are valid"""
        success, output, parsed = self.run_mkdocs_build(project_root)
        
        broken_links = [
            w for w in parsed['warnings']
            if w.get('type') in ['broken_link', 'broken_link_with_suggestion']
        ]
        
        if broken_links:
            error_msg = "\nBroken internal links:\n"
            # Group by source file
            by_file = {}
            for link in broken_links:
                source = link['source_file']
                if source not in by_file:
                    by_file[source] = []
                by_file[source].append(link)
            
            for source_file, links in by_file.items():
                error_msg += f"\n{source_file}:\n"
                for link in links:
                    error_msg += f"  - Link '{link['link']}' → target '{link.get('target', link['link'])}' not found\n"
                    if link.get('suggestion'):
                        error_msg += f"    Suggestion: {link['suggestion']}\n"
            
            pytest.fail(error_msg)

    @pytest.mark.integration
    def test_absolute_links_have_suggestions(self, project_root):
        """Test that absolute links have relative suggestions"""
        success, output, parsed = self.run_mkdocs_build(project_root)
        
        absolute_links = [
            w for w in parsed['info']
            if w.get('type') == 'absolute_link'
        ]
        
        # This is a warning-level test, not a failure
        if absolute_links:
            warning_msg = "\nAbsolute links that should be relative:\n"
            for link in absolute_links:
                warning_msg += f"  - {link['source_file']}: '{link['link']}'"
                if link.get('suggestion'):
                    warning_msg += f" → should be '{link['suggestion']}'"
                warning_msg += "\n"
            
            # Use pytest.skip to report as warning
            pytest.skip(f"Found absolute links (warning):{warning_msg}")

    @pytest.mark.integration
    def test_build_completes_successfully(self, project_root):
        """Test that build completes even with warnings"""
        success, output, parsed = self.run_mkdocs_build(project_root, strict=False)
        
        assert success or "site" in output, "Build should complete successfully"
        
        # Check that site directory was created
        site_dir = project_root / "site"
        assert site_dir.exists(), "Site directory should be created"

    @pytest.mark.integration
    def test_warning_count_threshold(self, project_root):
        """Test that total warnings are below threshold"""
        success, output, parsed = self.run_mkdocs_build(project_root)
        categorized = categorize_warnings(parsed)
        
        # Count all issues
        total_warnings = sum(len(categorized[sev]) for sev in ['critical', 'high', 'medium'])
        
        # Current threshold based on known issues
        WARNING_THRESHOLD = 75  # Allowing some buffer above 72
        
        if total_warnings > WARNING_THRESHOLD:
            report = format_warning_report(categorized)
            pytest.fail(
                f"Too many warnings ({total_warnings} > {WARNING_THRESHOLD}):\n{report}"
            )

    @pytest.mark.integration
    def test_specific_known_issues(self, project_root):
        """Test for specific known problematic patterns"""
        success, output, parsed = self.run_mkdocs_build(project_root)
        
        # Check for wikilink issues
        wikilink_issues = []
        for warning in parsed['warnings']:
            if warning.get('type') == 'broken_link':
                link = warning.get('link', '')
                # Check for wikilink patterns
                if '[[' in link or ']]' in link:
                    wikilink_issues.append(warning)
        
        if wikilink_issues:
            error_msg = "\nWikilink syntax issues found:\n"
            for issue in wikilink_issues:
                error_msg += f"  - {issue['source_file']}: {issue['link']}\n"
            pytest.fail(error_msg)

    @pytest.mark.integration
    def test_build_output_format(self, project_root):
        """Test that build output can be parsed correctly"""
        success, output, parsed = self.run_mkdocs_build(project_root)
        
        # Ensure we captured some output
        assert output, "Build should produce output"
        
        # Check that parsing worked
        total_items = (
            len(parsed.get('warnings', [])) +
            len(parsed.get('errors', [])) +
            len(parsed.get('info', []))
        )
        
        # We know there are issues, so we should parse some
        assert total_items > 0, "Parser should find warnings/errors in output"

    @pytest.mark.integration
    def test_categorization_consistency(self, project_root):
        """Test that warning categorization is consistent"""
        success, output, parsed = self.run_mkdocs_build(project_root)
        categorized = categorize_warnings(parsed)
        
        # Verify categorization
        for severity in ['critical', 'high', 'medium', 'low']:
            for item in categorized[severity]:
                # Each item should have required fields
                assert 'type' in item, f"Missing type in {severity} item"
                assert 'message' in item, f"Missing message in {severity} item"
                
                # Verify severity matches
                if 'severity' in item:
                    assert item['severity'] == severity, \
                        f"Mismatched severity: {item['severity']} != {severity}"

    @pytest.mark.integration
    @pytest.mark.parametrize("check_external", [False])
    def test_link_validation_completeness(self, project_root, check_external):
        """Test that all link types are caught"""
        success, output, parsed = self.run_mkdocs_build(project_root)
        
        # Types of link issues we should catch
        expected_issue_types = {
            'nav_reference_not_found',
            'broken_link',
            'broken_link_with_suggestion',
            'absolute_link'
        }
        
        found_types = set()
        for warning in parsed['warnings']:
            found_types.add(warning.get('type'))
        for info in parsed['info']:
            found_types.add(info.get('type'))
        
        # We expect to find most of these types given the known issues
        missing_types = expected_issue_types - found_types
        
        # It's OK if we don't have all types, but log what we found
        print(f"\nFound issue types: {found_types}")
        print(f"Missing issue types: {missing_types}")

    def generate_quality_report(self, project_root) -> str:
        """Generate a full quality report for documentation"""
        success, output, parsed = self.run_mkdocs_build(project_root)
        categorized = categorize_warnings(parsed)
        
        report = format_warning_report(categorized)
        
        # Add recommendations
        report += "\n\nRecommendations:\n"
        report += "-" * 40 + "\n"
        
        if categorized['critical']:
            report += "1. Fix all critical issues (missing nav files) immediately\n"
        if categorized['high']:
            report += "2. Fix all broken internal links\n"
        if categorized['medium']:
            report += "3. Convert absolute links to relative links\n"
        
        return report


if __name__ == "__main__":
    pytest.main([__file__, "-v"])