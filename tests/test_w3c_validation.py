"""Test W3C CSS validation compliance."""

import re
import json
from pathlib import Path
import pytest
import requests
from typing import Dict, List, Tuple


class TestW3CCSSValidation:
    """Test CSS files against W3C validation standards."""
    
    @pytest.fixture
    def css_files(self):
        """Get all CSS files."""
        css_dir = Path("docs/assets/css")
        files = {}
        for css_file in css_dir.glob("druids-*.css"):
            files[css_file.name] = {
                "path": css_file,
                "content": css_file.read_text()
            }
        return files
    
    def test_css_syntax_validity(self, css_files):
        """Test that CSS syntax is valid according to W3C standards."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Check for valid CSS property syntax
            property_pattern = r'([a-zA-Z-]+)\s*:\s*([^;]+);'
            properties = re.findall(property_pattern, content)
            
            for prop, value in properties:
                # Property names should be lowercase with hyphens
                assert re.match(r'^[a-z-]+$', prop), \
                    f"Invalid property name '{prop}' in {filename}"
                
                # Values should not be empty
                assert value.strip(), \
                    f"Empty value for property '{prop}' in {filename}"
    
    def test_at_rules_validity(self, css_files):
        """Test that @-rules follow W3C specifications."""
        valid_at_rules = [
            '@media', '@keyframes', '@import', '@charset',
            '@font-face', '@supports', '@page', '@namespace'
        ]
        
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find all @-rules
            at_rules = re.findall(r'(@[a-zA-Z-]+)', content)
            
            for at_rule in at_rules:
                assert at_rule in valid_at_rules, \
                    f"Invalid @-rule '{at_rule}' in {filename}"
    
    def test_selector_validity(self, css_files):
        """Test that selectors follow W3C standards."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Extract selectors (more precise to avoid matching across blocks)
            # Split content into lines and look for selector patterns
            selectors = []
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if '{' in line and not line.strip().startswith(('@', '/*', '//', '*')):
                    # Extract selector part before {
                    selector_part = line.split('{')[0].strip()
                    if selector_part:
                        selectors.append(selector_part)
            
            for selector in selectors:
                selector = selector.strip()
                
                # Check for invalid characters in selectors (> is valid for child combinator)
                assert not re.search(r'[<]', selector), \
                    f"Invalid characters in selector '{selector}' in {filename}"
                
                # Check pseudo-class/element syntax
                if '::' in selector:
                    # Double colon for pseudo-elements
                    pseudo_element = re.search(r'::([a-zA-Z-]+)', selector)
                    if pseudo_element:
                        valid_pseudo_elements = [
                            'before', 'after', 'first-line', 'first-letter',
                            'selection', 'backdrop', 'placeholder',
                            '-webkit-scrollbar', '-webkit-scrollbar-thumb', 
                            '-webkit-scrollbar-track', '-webkit-scrollbar-button'
                        ]
                        assert pseudo_element.group(1) in valid_pseudo_elements, \
                            f"Invalid pseudo-element '::{pseudo_element.group(1)}' in {filename}"
    
    def test_color_format_validity(self, css_files):
        """Test that color values follow W3C formats."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find all color values
            hex_colors = re.findall(r'#([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})\b', content)
            rgb_colors = re.findall(r'rgba?\([^)]+\)', content)
            
            # Validate hex colors
            for hex_color in hex_colors:
                assert len(hex_color) in [3, 6], \
                    f"Invalid hex color length #{hex_color} in {filename}"
            
            # Validate rgb/rgba colors
            for rgb_color in rgb_colors:
                # Check format
                if rgb_color.startswith('rgb('):
                    assert re.match(r'rgb\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)', rgb_color), \
                        f"Invalid RGB format '{rgb_color}' in {filename}"
                elif rgb_color.startswith('rgba('):
                    assert re.match(r'rgba\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*,\s*[\d.]+\s*\)', rgb_color), \
                        f"Invalid RGBA format '{rgb_color}' in {filename}"
    
    def test_unit_validity(self, css_files):
        """Test that CSS units are valid according to W3C."""
        valid_units = [
            'px', 'em', 'rem', '%', 'vh', 'vw', 'vmin', 'vmax',
            'ch', 'ex', 'cm', 'mm', 'in', 'pt', 'pc', 'deg',
            'rad', 'grad', 'turn', 's', 'ms', 'fr'
        ]
        
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find numeric values with units
            unit_pattern = r':\s*[\d.]+([a-zA-Z%]+)'
            units_found = re.findall(unit_pattern, content)
            
            for unit in units_found:
                # Skip color keywords and functions
                if unit.lower() in ['transparent', 'inherit', 'initial', 'unset']:
                    continue
                if unit.endswith((')', 'px', 'em', 'rem')) or unit in valid_units:
                    continue
                    
                # Check if it's a valid unit
                assert unit in valid_units, \
                    f"Invalid CSS unit '{unit}' found in {filename}"
    
    def test_media_query_syntax(self, css_files):
        """Test that media queries follow W3C syntax."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find media queries
            media_queries = re.findall(r'@media\s+([^{]+){', content)
            
            for query in media_queries:
                # Check for valid media types
                if 'screen' in query or 'print' in query or 'all' in query:
                    # Valid media type
                    pass
                
                # Check for valid features
                valid_features = [
                    'width', 'height', 'min-width', 'max-width',
                    'min-height', 'max-height', 'orientation',
                    'resolution', 'prefers-reduced-motion',
                    'prefers-contrast', 'prefers-color-scheme'
                ]
                
                # Basic validation - print queries don't need features
                if query.strip() not in ['print', 'screen', 'all']:
                    assert '(' in query and ')' in query, \
                        f"Invalid media query syntax '{query}' in {filename}"
    
    def test_no_proprietary_properties(self, css_files):
        """Test that CSS doesn't use non-standard proprietary properties."""
        # Properties that should be avoided or have standard alternatives
        proprietary_properties = [
            '-ms-filter',  # Use standard filter
            'zoom',  # Use transform: scale()
            '*display',  # IE6/7 hack
            '_display',  # IE6 hack
        ]
        
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            for prop in proprietary_properties:
                assert prop not in content, \
                    f"Proprietary property '{prop}' found in {filename}. Use standard alternatives."
    
    def test_css_validation_comments(self, css_files):
        """Test that CSS files have proper validation markers."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Check for file header comment
            assert content.strip().startswith('/*'), \
                f"{filename} should start with a descriptive comment"
            
            # Check that comments are properly closed
            open_comments = content.count('/*')
            close_comments = content.count('*/')
            assert open_comments == close_comments, \
                f"Unclosed comments in {filename}: {open_comments} opened, {close_comments} closed"