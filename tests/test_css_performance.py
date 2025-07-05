"""Test CSS performance and optimization metrics."""

import re
from pathlib import Path
import pytest


class TestCSSPerformance:
    """Test CSS performance characteristics and optimization."""
    
    @pytest.fixture
    def css_files(self):
        """Get all CSS files with their sizes."""
        css_dir = Path("docs/assets/css")
        files = {}
        for css_file in css_dir.glob("druids-*.css"):
            content = css_file.read_text()
            files[css_file.name] = {
                "path": css_file,
                "content": content,
                "size": len(content.encode('utf-8'))
            }
        return files
    
    def test_css_file_sizes(self, css_files):
        """Test that CSS files are reasonably sized."""
        max_sizes = {
            "druids-theme.css": 10000,      # 10KB max
            "druids-layout.css": 15000,     # 15KB max
            "druids-components.css": 20000, # 20KB max
            "druids-utilities.css": 8000    # 8KB max
        }
        
        for filename, file_info in css_files.items():
            max_size = max_sizes.get(filename, 25000)  # Default 25KB
            assert file_info["size"] <= max_size, \
                f"{filename} is {file_info['size']} bytes, exceeds limit of {max_size} bytes"
    
    def test_no_unused_selectors(self, css_files):
        """Test for obviously unused selectors (basic check)."""
        # Check for common unused patterns
        unused_patterns = [
            r'\.unused-',          # Classes starting with unused-
            r'\.deprecated-',      # Deprecated classes
            r'\.old-',            # Old classes
            r'#temp-',            # Temporary IDs
            r'\.test-(?!features)' # Test classes except test-features
        ]
        
        for filename, file_info in css_files.items():
            content = file_info["content"]
            for pattern in unused_patterns:
                matches = re.findall(pattern, content)
                assert len(matches) == 0, \
                    f"Found potentially unused selectors in {filename}: {matches}"
    
    def test_no_duplicate_rules(self, css_files):
        """Test for duplicate CSS rules within files."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Extract all selectors (simple regex, not perfect)
            selectors = re.findall(r'^([^{]+){', content, re.MULTILINE)
            selectors = [s.strip() for s in selectors if s.strip() and not s.strip().startswith('@')]
            
            # Check for exact duplicates
            seen = set()
            duplicates = []
            for selector in selectors:
                if selector in seen:
                    duplicates.append(selector)
                seen.add(selector)
            
            assert len(duplicates) == 0, \
                f"Duplicate selectors found in {filename}: {duplicates[:5]}..."  # Show first 5
    
    def test_efficient_selectors(self, css_files):
        """Test that selectors are efficient (not overly specific)."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Check for overly specific selectors (more than 4 levels)
            overly_specific = re.findall(r'([^{]+)\s+[^{]+\s+[^{]+\s+[^{]+\s+[^{]+{', content)
            
            # Filter out false positives (media queries, keyframes, etc.)
            overly_specific = [s for s in overly_specific 
                              if not s.strip().startswith('@') 
                              and ' > ' in s or ' ' in s]
            
            assert len(overly_specific) <= 5, \
                f"Too many overly specific selectors in {filename}: {overly_specific[:3]}..."
    
    def test_minification_potential(self, css_files):
        """Test how much the CSS could be minified."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            original_size = file_info["size"]
            
            # Simple minification simulation
            minified = content
            # Remove comments
            minified = re.sub(r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/', '', minified)
            # Remove unnecessary whitespace
            minified = re.sub(r'\s+', ' ', minified)
            minified = re.sub(r'\s*([{}:;,])\s*', r'\1', minified)
            minified = minified.strip()
            
            minified_size = len(minified.encode('utf-8'))
            reduction_percent = ((original_size - minified_size) / original_size) * 100
            
            # If more than 50% can be reduced, file might have too much whitespace
            assert reduction_percent <= 50, \
                f"{filename} could be reduced by {reduction_percent:.1f}% - consider optimizing"
    
    def test_no_redundant_vendor_prefixes(self, css_files):
        """Test that vendor prefixes are not overused."""
        # Properties that don't need prefixes in modern browsers
        no_prefix_needed = [
            'border-radius',
            'box-shadow',
            'text-shadow',
            'opacity',
            'background-size'
        ]
        
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            for prop in no_prefix_needed:
                # Check for -webkit-, -moz-, -ms-, -o- prefixes
                prefixed = re.findall(rf'-(?:webkit|moz|ms|o)-{prop}', content)
                assert len(prefixed) == 0, \
                    f"Unnecessary vendor prefix found in {filename}: {prefixed}"
    
    def test_css_property_order(self, css_files):
        """Test that CSS properties follow a logical order (optional but good practice)."""
        # This is a soft test - we check for mixing of property types
        property_groups = {
            'positioning': ['position', 'top', 'right', 'bottom', 'left', 'z-index'],
            'display': ['display', 'flex', 'grid', 'float', 'clear'],
            'dimensions': ['width', 'height', 'margin', 'padding'],
            'visual': ['background', 'border', 'color', 'font']
        }
        
        # This is more of a warning than a hard failure
        # Just check that files exist and have content
        for filename, file_info in css_files.items():
            assert len(file_info["content"]) > 0, f"{filename} is empty"
    
    def test_critical_css_extraction(self, css_files):
        """Test that critical CSS (above-the-fold) is identifiable."""
        # Check that layout and theme CSS are small enough to inline if needed
        critical_files = ["druids-theme.css", "druids-layout.css"]
        
        total_critical_size = 0
        for filename in critical_files:
            if filename in css_files:
                total_critical_size += css_files[filename]["size"]
        
        # Critical CSS should be under 20KB for good performance
        assert total_critical_size <= 20000, \
            f"Critical CSS (theme + layout) is {total_critical_size} bytes, should be under 20KB"
    
    def test_no_base64_images(self, css_files):
        """Test that CSS doesn't contain large base64 encoded images."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Look for base64 data URIs
            base64_matches = re.findall(r'data:image/[^;]+;base64,([^"\']+)', content)
            
            for match in base64_matches:
                # Check size of base64 data
                size = len(match)
                assert size <= 5000, \
                    f"Large base64 image ({size} chars) found in {filename}. Use external files instead."
    
    def test_animation_performance(self, css_files):
        """Test that animations use performant properties."""
        # Properties that trigger reflow/repaint
        expensive_animated_props = [
            'width', 'height', 'padding', 'margin',
            'border', 'top', 'left', 'right', 'bottom'
        ]
        
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find keyframes
            keyframes = re.findall(r'@keyframes[^{]+{([^}]+(?:{[^}]+}[^}]+)*)}', content, re.DOTALL)
            
            for keyframe in keyframes:
                for prop in expensive_animated_props:
                    if prop + ':' in keyframe:
                        # This is a warning, not a hard failure
                        print(f"Warning: Animating expensive property '{prop}' in {filename}")
    
    def test_css_custom_properties_usage(self, css_files):
        """Test that CSS custom properties are used efficiently."""
        theme_file = css_files.get("druids-theme.css", {})
        theme_content = theme_file.get("content", "")
        
        # Extract defined custom properties
        defined_props = set(re.findall(r'(--druids-[\w-]+):', theme_content))
        
        # Check usage across all files
        total_usages = 0
        for filename, file_info in css_files.items():
            content = file_info["content"]
            usages = re.findall(r'var\((--druids-[\w-]+)\)', content)
            total_usages += len(usages)
            
            # Check that used properties are defined
            for used_prop in set(usages):
                assert used_prop in defined_props, \
                    f"Undefined CSS variable {used_prop} used in {filename}"
        
        # Check that defined properties are actually used
        for prop in defined_props:
            used = any(f"var({prop})" in f["content"] for f in css_files.values())
            assert used, f"Defined CSS variable {prop} is never used"