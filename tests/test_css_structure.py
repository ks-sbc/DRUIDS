#!/usr/bin/env python3
"""
CSS structure and validation tests to ensure clean, maintainable stylesheets.
These tests check for duplicates, file sizes, and proper organization.
"""

import re
from pathlib import Path
import pytest
import cssutils
from collections import defaultdict
from test_utils import run_command


class TestCSSStructure:
    """Test CSS file structure and organization"""
    
    def get_css_files(self):
        """Get all CSS files in the assets directory"""
        css_dir = Path(__file__).parent.parent / "docs" / "assets" / "css"
        return list(css_dir.glob("*.css"))
    
    def parse_css(self, file_path):
        """Parse CSS file and return cssutils stylesheet object"""
        cssutils.log.setLevel(100)  # Suppress warnings
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return cssutils.parseString(content)
    
    def test_no_duplicate_selectors(self):
        """Ensure no CSS selectors are duplicated across files"""
        selectors_by_file = defaultdict(list)
        duplicates = []
        
        for css_file in self.get_css_files():
            sheet = self.parse_css(css_file)
            
            for rule in sheet:
                if hasattr(rule, 'selectorText'):
                    selector = rule.selectorText
                    # Check if this selector exists in other files
                    for other_file, other_selectors in selectors_by_file.items():
                        if selector in other_selectors and other_file != css_file.name:
                            duplicates.append({
                                'selector': selector,
                                'files': [css_file.name, other_file]
                            })
                    
                    selectors_by_file[css_file.name].append(selector)
        
        if duplicates:
            msg = "Duplicate selectors found:\n"
            for dup in duplicates[:5]:  # Show first 5
                msg += f"  - '{dup['selector']}' in {', '.join(dup['files'])}\n"
            pytest.fail(msg)
    
    def test_css_file_sizes(self):
        """Ensure consolidated CSS files are under size limits"""
        total_size = 0
        large_files = []
        
        # Target: individual files < 20KB, total < 50KB
        max_individual_size = 20 * 1024  # 20KB
        max_total_size = 50 * 1024  # 50KB
        
        for css_file in self.get_css_files():
            size = css_file.stat().st_size
            total_size += size
            
            if size > max_individual_size:
                large_files.append({
                    'file': css_file.name,
                    'size': size / 1024  # Convert to KB
                })
        
        issues = []
        if large_files:
            files_str = ', '.join(f"{f['file']} ({f['size']:.1f}KB)" for f in large_files)
            issues.append(f"Large CSS files found: {files_str}")
        
        if total_size > max_total_size:
            issues.append(f"Total CSS size {total_size/1024:.1f}KB exceeds target of 50KB")
        
        if issues:
            pytest.fail("\n".join(issues))
    
    def test_css_variables_defined(self):
        """Ensure all CSS variables are properly defined in :root"""
        undefined_vars = []
        defined_vars = set()
        
        for css_file in self.get_css_files():
            content = css_file.read_text()
            
            # Find all :root definitions
            root_matches = re.findall(r':root\s*{([^}]+)}', content, re.DOTALL)
            for match in root_matches:
                var_definitions = re.findall(r'(--[a-zA-Z0-9-]+):', match)
                defined_vars.update(var_definitions)
            
            # Find all var() usage
            var_usage = re.findall(r'var\((--[a-zA-Z0-9-]+)', content)
            
            # Check if used variables are defined
            for var in var_usage:
                if var not in defined_vars:
                    undefined_vars.append({
                        'variable': var,
                        'file': css_file.name
                    })
        
        if undefined_vars:
            msg = "Undefined CSS variables:\n"
            for var in undefined_vars[:10]:  # Show first 10
                msg += f"  - {var['variable']} used in {var['file']}\n"
            pytest.fail(msg)
    
    def test_no_conflicting_styles(self):
        """Check for conflicting style definitions"""
        # Look for !important overuse and conflicting properties
        important_count = defaultdict(int)
        conflicts = []
        
        for css_file in self.get_css_files():
            content = css_file.read_text()
            
            # Count !important usage
            important_matches = re.findall(r'([^{]+){[^}]*!important', content)
            important_count[css_file.name] = len(important_matches)
            
            # Check for multiple definitions of the same property in a rule
            sheet = self.parse_css(css_file)
            for rule in sheet:
                if hasattr(rule, 'style'):
                    props = defaultdict(list)
                    for prop in rule.style:
                        props[prop.name].append(prop.value)
                    
                    for prop_name, values in props.items():
                        if len(values) > 1:
                            conflicts.append({
                                'file': css_file.name,
                                'selector': getattr(rule, 'selectorText', 'unknown'),
                                'property': prop_name,
                                'values': values
                            })
        
        issues = []
        
        # Check for excessive !important usage
        for file, count in important_count.items():
            if count > 50:  # Threshold for !important usage
                issues.append(f"{file} has {count} !important declarations")
        
        if conflicts:
            issues.append("Conflicting property definitions found")
        
        if issues:
            pytest.fail("\n".join(issues))
    
    def test_proper_css_organization(self):
        """Verify CSS is organized by component/purpose"""
        expected_files = {
            'druids-layout.css': ['header', 'footer', 'sidebar', 'nav', 'grid'],
            'druids-theme.css': ['color', 'cyber', 'pride', 'dark', 'light'],
            'druids-components.css': ['button', 'table', 'code', 'admonition', 'giscus'],
            'druids-utilities.css': ['typography', 'spacing', 'accessibility', 'print']
        }
        
        # For now, check that we at least have some organization
        css_files = [f.name for f in self.get_css_files()]
        
        # We expect to see multiple files, not just one huge file
        if len(css_files) < 4:
            pytest.fail(f"CSS not properly organized. Only {len(css_files)} files found, expected at least 4")
        
        # Check for the massive extra.css file
        if 'extra.css' in css_files:
            extra_size = (Path(__file__).parent.parent / "docs" / "assets" / "css" / "extra.css").stat().st_size
            if extra_size > 50 * 1024:  # 50KB
                pytest.fail(f"extra.css is {extra_size/1024:.1f}KB - should be split into organized files")
    
    def test_stylelint_passes(self):
        """Run stylelint and ensure no errors"""
        project_root = Path(__file__).parent.parent
        
        success, stdout, stderr = run_command(
            "npx stylelint 'docs/assets/css/*.css'",
            cwd=project_root
        )
        
        if not success:
            # Parse stylelint output for specific issues
            issues = []
            if "duplicate" in stderr.lower():
                issues.append("Duplicate selectors or properties")
            if "order" in stderr.lower():
                issues.append("Properties not in alphabetical order")
            if "specificity" in stderr.lower():
                issues.append("Selector specificity too high")
            
            pytest.fail(f"Stylelint errors: {', '.join(issues) if issues else stderr}")
    
    def test_color_consistency(self):
        """Ensure consistent use of color variables"""
        hardcoded_colors = []
        
        for css_file in self.get_css_files():
            content = css_file.read_text()
            
            # Find hardcoded colors (hex, rgb, rgba) not in variables
            # Skip :root blocks
            non_root_content = re.sub(r':root\s*{[^}]+}', '', content, flags=re.DOTALL)
            
            # Look for hardcoded colors
            hex_colors = re.findall(r'(?<![-])#[0-9a-fA-F]{3,6}(?![0-9a-fA-F])', non_root_content)
            rgb_colors = re.findall(r'rgba?\([^)]+\)', non_root_content)
            
            if hex_colors or rgb_colors:
                hardcoded_colors.append({
                    'file': css_file.name,
                    'hex': hex_colors[:5],  # First 5
                    'rgb': rgb_colors[:5]
                })
        
        if hardcoded_colors:
            msg = "Hardcoded colors found (should use variables):\n"
            for item in hardcoded_colors:
                if item['hex']:
                    msg += f"  - {item['file']}: {', '.join(item['hex'])}\n"
                if item['rgb']:
                    msg += f"  - {item['file']}: {', '.join(item['rgb'][:3])}\n"
            pytest.fail(msg)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])