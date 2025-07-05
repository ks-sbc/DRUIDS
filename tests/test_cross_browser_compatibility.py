"""Test CSS cross-browser compatibility."""

import re
from pathlib import Path
import pytest
from typing import Dict, List, Set


class TestCrossBrowserCompatibility:
    """Test that CSS works across different browsers."""
    
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
    
    def test_vendor_prefixes(self, css_files):
        """Test that vendor prefixes are used appropriately."""
        # Properties that might need prefixes for older browsers
        prefix_properties = {
            'transform': ['-webkit-transform', '-ms-transform'],
            'transition': ['-webkit-transition'],
            'animation': ['-webkit-animation'],
            'flex': ['-webkit-flex', '-ms-flex'],
            'user-select': ['-webkit-user-select', '-moz-user-select', '-ms-user-select'],
            'backdrop-filter': ['-webkit-backdrop-filter'],
            'mask': ['-webkit-mask'],
            'clip-path': ['-webkit-clip-path']
        }
        
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            for property_name, prefixes in prefix_properties.items():
                # Check if property is used
                if f'{property_name}:' in content:
                    # For modern browsers, we might not need all prefixes
                    # But check critical ones
                    if property_name in ['backdrop-filter', 'mask', 'clip-path']:
                        webkit_prefix = f'-webkit-{property_name}'
                        if webkit_prefix not in content and property_name in content:
                            print(f"Info: Consider adding {webkit_prefix} in {filename} for Safari support")
    
    def test_flexbox_compatibility(self, css_files):
        """Test flexbox syntax for cross-browser support."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Check for flexbox usage
            if 'display: flex' in content or 'display: inline-flex' in content:
                # Modern flexbox is well supported, but check for old syntax
                old_flexbox = ['display: box', 'display: -webkit-box', 'box-orient', 'box-flex']
                
                for old_syntax in old_flexbox:
                    assert old_syntax not in content, \
                        f"Old flexbox syntax '{old_syntax}' found in {filename}. Use modern syntax."
                
                # Check for flex shorthand vs longhand
                if 'flex:' in content:
                    # Flex shorthand can have issues in IE11
                    flex_values = re.findall(r'flex:\s*([^;]+);', content)
                    for value in flex_values:
                        if value.count(' ') == 0 and value not in ['none', 'auto', 'initial']:
                            print(f"Info: flex: {value} in {filename} - consider using flex: {value} 1 0% for IE11")
    
    def test_grid_compatibility(self, css_files):
        """Test CSS Grid syntax and fallbacks."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Check for grid usage
            if 'display: grid' in content:
                # Check for IE-specific grid syntax
                if '-ms-grid' in content:
                    print(f"Warning: IE grid syntax found in {filename}. IE is deprecated.")
                
                # Check for feature queries
                if '@supports (display: grid)' not in content:
                    print(f"Info: Consider using @supports for grid in {filename} if you need fallbacks")
    
    def test_calc_compatibility(self, css_files):
        """Test calc() syntax for compatibility."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find calc expressions
            calc_expressions = re.findall(r'calc\([^)]+\)', content)
            
            for calc_expr in calc_expressions:
                # Check for spaces around operators (required for compatibility)
                if not re.search(r'\s[+\-*/]\s', calc_expr):
                    print(f"Warning: calc() without spaces around operators in {filename}: {calc_expr}")
                    print("  Some browsers require spaces around operators")
    
    def test_custom_properties_fallbacks(self, css_files):
        """Test that CSS custom properties have fallbacks where needed."""
        for filename, file_info in css_files.items():
            if filename == "druids-theme.css":
                continue  # Skip theme file that defines properties
                
            content = file_info["content"]
            
            # Find var() usage
            var_usage = re.findall(r'var\(([^)]+)\)', content)
            
            for var_expr in var_usage:
                # Check if it has a fallback
                if ',' not in var_expr:
                    # No fallback provided
                    # This is often OK for internal properties, but check critical ones
                    if any(critical in var_expr for critical in ['color', 'background', 'font']):
                        print(f"Info: var({var_expr}) without fallback in {filename}")
    
    def test_modern_css_features(self, css_files):
        """Test usage of modern CSS features that might need fallbacks."""
        modern_features = {
            'clamp(': 'CSS clamp() - not supported in IE',
            'min(': 'CSS min() - not supported in older browsers',
            'max(': 'CSS max() - not supported in older browsers',
            ':is(': 'CSS :is() selector - limited support',
            ':where(': 'CSS :where() selector - limited support',
            ':has(': 'CSS :has() selector - very limited support',
            'aspect-ratio:': 'CSS aspect-ratio - not in older browsers',
            'gap:': 'gap property in flexbox - limited support',
            'inset:': 'CSS logical property - modern browsers only'
        }
        
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            for feature, description in modern_features.items():
                if feature in content:
                    # Check if there's a fallback or feature query
                    if feature == 'clamp(':
                        # Clamp is OK as it's used in our design system
                        continue
                    elif feature == 'gap:' and 'display: flex' in content:
                        print(f"Info: {description} used in {filename}")
                        print("  Consider margin fallbacks for older browsers")
                    elif feature in [':has(', ':is(', ':where(']:
                        print(f"Warning: {description} used in {filename}")
                        print("  Provide fallbacks for critical functionality")
    
    def test_position_sticky_support(self, css_files):
        """Test position: sticky usage and fallbacks."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            if 'position: sticky' in content:
                # Check for -webkit prefix (needed for some Safari versions)
                if 'position: -webkit-sticky' not in content:
                    print(f"Info: Add 'position: -webkit-sticky' before 'position: sticky' in {filename}")
                
                # Check for fallback
                sticky_selectors = re.findall(r'([^{]+)\s*{[^}]*position:\s*sticky', content)
                for selector in sticky_selectors:
                    if 'position: fixed' not in content:
                        print(f"Consider position: fixed fallback for sticky element '{selector.strip()}' in {filename}")
    
    def test_filter_compatibility(self, css_files):
        """Test CSS filter usage and compatibility."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Check for filter usage
            if 'filter:' in content:
                # Check for webkit prefix
                if '-webkit-filter:' not in content:
                    print(f"Info: Consider adding -webkit-filter for older Safari in {filename}")
                
                # Check for backdrop-filter
                if 'backdrop-filter:' in content and '-webkit-backdrop-filter:' not in content:
                    print(f"Warning: backdrop-filter needs -webkit prefix for Safari in {filename}")
    
    def test_scroll_behavior(self, css_files):
        """Test scroll-behavior and scrollbar styling."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Check scroll-behavior
            if 'scroll-behavior:' in content:
                print(f"Info: scroll-behavior in {filename} not supported in Safari")
                print("  Consider JavaScript fallback for smooth scrolling")
            
            # Check custom scrollbars
            if '::-webkit-scrollbar' in content:
                # Check if there are standard alternatives
                if 'scrollbar-width:' not in content or 'scrollbar-color:' not in content:
                    print(f"Info: Webkit scrollbars in {filename} - add standard properties too:")
                    print("  scrollbar-width and scrollbar-color for Firefox")
    
    def test_logical_properties(self, css_files):
        """Test usage of CSS logical properties."""
        logical_properties = {
            'margin-inline-start': 'margin-left',
            'margin-inline-end': 'margin-right',
            'padding-block-start': 'padding-top',
            'padding-block-end': 'padding-bottom',
            'inset-inline-start': 'left',
            'inset-inline-end': 'right'
        }
        
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            for logical_prop, physical_prop in logical_properties.items():
                if logical_prop in content:
                    print(f"Info: Logical property '{logical_prop}' in {filename}")
                    print(f"  Not supported in older browsers. Consider {physical_prop} fallback")
    
    def test_font_format_compatibility(self, css_files):
        """Test font format declarations for compatibility."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Check @font-face declarations
            font_faces = re.findall(r'@font-face\s*{([^}]+)}', content, re.DOTALL)
            
            for font_face in font_faces:
                # Check font formats
                if 'src:' in font_face:
                    # Modern format
                    if 'format("woff2")' in font_face:
                        # Check for woff fallback
                        if 'format("woff")' not in font_face:
                            print(f"Info: Consider adding WOFF fallback for older browsers in {filename}")
                    
                    # Check for variable fonts
                    if 'font-variation-settings' in font_face:
                        print(f"Info: Variable fonts in {filename} not supported in older browsers")
    
    def test_media_query_syntax(self, css_files):
        """Test media query syntax for compatibility."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find media queries
            media_queries = re.findall(r'@media([^{]+){', content)
            
            for query in media_queries:
                # Check for modern syntax
                if 'not all and' in query:
                    # This is a hack for IE
                    pass
                
                # Check for range syntax (very modern)
                if '<=' in query or '>=' in query:
                    print(f"Warning: Range media queries in {filename} not widely supported")
                    print(f"  Query: @media{query}")
                    print("  Use min-width/max-width instead")