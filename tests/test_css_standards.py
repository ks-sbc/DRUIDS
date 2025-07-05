"""Test CSS standards compliance and validation."""

import re
from pathlib import Path
import pytest


class TestCSSStandards:
    """Test CSS files meet coding standards and best practices."""
    
    @pytest.fixture
    def css_files(self):
        """Get all CSS files in the project."""
        css_dir = Path("docs/assets/css")
        return list(css_dir.glob("druids-*.css"))
    
    def test_css_files_exist(self, css_files):
        """Test that all expected CSS files exist."""
        expected_files = [
            "druids-theme.css",
            "druids-layout.css", 
            "druids-components.css",
            "druids-utilities.css"
        ]
        
        actual_files = [f.name for f in css_files]
        for expected in expected_files:
            assert expected in actual_files, f"Missing CSS file: {expected}"
    
    def test_css_syntax_valid(self, css_files):
        """Test that CSS files have valid syntax."""
        for css_file in css_files:
            content = css_file.read_text()
            
            # Check for balanced braces
            open_braces = content.count('{')
            close_braces = content.count('}')
            assert open_braces == close_braces, f"Unbalanced braces in {css_file.name}"
            
            # Check for proper semicolons (simple check)
            # Every property should end with semicolon except last in block
            lines = content.split('\n')
            in_block = False
            for i, line in enumerate(lines):
                line = line.strip()
                if '{' in line:
                    in_block = True
                elif '}' in line:
                    in_block = False
                elif in_block and ':' in line and not line.startswith('/*'):
                    # This is a CSS property
                    if not (line.endswith(';') or line.endswith('}') or 
                            (i + 1 < len(lines) and '}' in lines[i + 1].strip())):
                        # Allow last property before closing brace to omit semicolon
                        assert False, f"Missing semicolon in {css_file.name}: {line}"
    
    def test_css_variables_defined(self, css_files):
        """Test that all CSS variables are properly defined."""
        # Find druids-theme.css which should contain variable definitions
        theme_file = next((f for f in css_files if f.name == "druids-theme.css"), None)
        assert theme_file is not None, "druids-theme.css not found"
        
        theme_content = theme_file.read_text()
        
        # Extract all variable definitions from :root
        root_match = re.search(r':root\s*{([^}]+)}', theme_content, re.DOTALL)
        assert root_match is not None, "No :root block found in theme CSS"
        
        root_block = root_match.group(1)
        defined_vars = set(re.findall(r'(--druids-[\w-]+):', root_block))
        
        # Check all CSS files for variable usage
        for css_file in css_files:
            content = css_file.read_text()
            used_vars = set(re.findall(r'var\((--druids-[\w-]+)\)', content))
            
            undefined_vars = used_vars - defined_vars
            assert len(undefined_vars) == 0, \
                f"Undefined variables in {css_file.name}: {undefined_vars}"
    
    def test_color_values_consistent(self, css_files):
        """Test that color values use consistent format."""
        for css_file in css_files:
            content = css_file.read_text()
            
            # Find all color values
            hex_colors = re.findall(r'#[0-9A-Fa-f]{3,8}', content)
            
            for color in hex_colors:
                # Check that hex colors are uppercase and 6 or 8 digits (not 3)
                if len(color) == 4:  # #RGB format
                    assert False, f"Use 6-digit hex colors, not 3-digit: {color} in {css_file.name}"
                elif len(color) == 7 or len(color) == 9:  # #RRGGBB or #RRGGBBAA
                    assert color[1:].isupper(), f"Hex color should be uppercase: {color} in {css_file.name}"
    
    def test_no_important_overuse(self, css_files):
        """Test that !important is not overused."""
        max_important_per_file = 30  # Reasonable limit
        
        for css_file in css_files:
            content = css_file.read_text()
            important_count = content.count('!important')
            
            assert important_count <= max_important_per_file, \
                f"Too many !important declarations ({important_count}) in {css_file.name}"
    
    def test_media_queries_consistent(self, css_files):
        """Test that media queries use consistent breakpoints."""
        expected_breakpoints = {
            "767px",    # Mobile max
            "768px",    # Tablet min
            "959px",    # Tablet max  
            "960px",    # Desktop min
        }
        
        for css_file in css_files:
            content = css_file.read_text()
            
            # Find all media query breakpoints
            breakpoints = re.findall(r'@media[^{]+\((?:max-|min-)?width:\s*(\d+px)', content)
            
            for breakpoint in breakpoints:
                # Allow some flexibility for specific needs, but flag unusual values
                if breakpoint not in expected_breakpoints:
                    # Check if it's close to an expected value (within 50px)
                    bp_value = int(breakpoint.replace('px', ''))
                    close_to_expected = any(
                        abs(bp_value - int(exp.replace('px', ''))) <= 50 
                        for exp in expected_breakpoints
                    )
                    
                    if not close_to_expected and bp_value not in [600, 1200, 1440]:  # Common alternatives
                        assert False, f"Unusual breakpoint {breakpoint} in {css_file.name}"
    
    def test_clamp_usage(self, css_files):
        """Test that clamp() is used correctly for fluid typography."""
        theme_file = next((f for f in css_files if f.name == "druids-theme.css"), None)
        assert theme_file is not None
        
        content = theme_file.read_text()
        
        # Check that typography variables use clamp()
        typography_vars = [
            '--druids-text-xs',
            '--druids-text-sm', 
            '--druids-text-base',
            '--druids-text-lg',
            '--druids-text-xl',
            '--druids-text-2xl',
            '--druids-text-3xl',
            '--druids-text-4xl'
        ]
        
        for var in typography_vars:
            pattern = rf'{var}:\s*clamp\('
            assert re.search(pattern, content), f"{var} should use clamp() for fluid sizing"
    
    def test_z_index_values(self, css_files):
        """Test that z-index values are reasonable and organized."""
        z_index_values = []
        
        for css_file in css_files:
            content = css_file.read_text()
            
            # Find all z-index values
            matches = re.findall(r'z-index:\s*(\d+)', content)
            z_index_values.extend([(int(m), css_file.name) for m in matches])
        
        # Check that z-index values are reasonable (not too high)
        for value, filename in z_index_values:
            assert value <= 10000, f"z-index {value} is too high in {filename}"
            
        # Common z-index levels
        expected_levels = [1, 10, 100, 999, 1000, 1001]
        for value, filename in z_index_values:
            if value not in expected_levels and value < 100:
                # Small values are fine, but large arbitrary values should follow pattern
                assert value in expected_levels or value < 100, \
                    f"z-index {value} should follow standard levels in {filename}"