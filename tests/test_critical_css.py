"""Test critical CSS extraction and optimization."""

import re
from pathlib import Path
import pytest
from typing import Set, List, Dict


class TestCriticalCSS:
    """Test that critical CSS is properly structured for performance."""
    
    @pytest.fixture
    def css_files(self):
        """Get all CSS files with content."""
        css_dir = Path("docs/assets/css")
        files = {}
        for css_file in css_dir.glob("druids-*.css"):
            files[css_file.name] = {
                "path": css_file,
                "content": css_file.read_text(),
                "size": len(css_file.read_text().encode('utf-8'))
            }
        return files
    
    def test_critical_css_identification(self, css_files):
        """Test that critical CSS files are properly identified."""
        # Theme and layout CSS should be considered critical
        critical_files = ["druids-theme.css", "druids-layout.css"]
        
        for filename in critical_files:
            assert filename in css_files, \
                f"Critical CSS file '{filename}' not found"
            
            # Critical CSS should be reasonably sized
            file_size = css_files[filename]["size"]
            assert file_size < 15000, \
                f"Critical CSS file '{filename}' is too large ({file_size} bytes). Should be < 15KB"
    
    def test_above_the_fold_styles(self, css_files):
        """Test that above-the-fold styles are in critical CSS."""
        critical_selectors = [
            '.md-header',
            '.md-nav',
            '.md-content',
            'body',
            'html',
            'h1', 'h2', 'h3',
            ':root'  # Custom properties
        ]
        
        # These should be in theme or layout CSS
        critical_content = css_files.get("druids-theme.css", {}).get("content", "")
        critical_content += css_files.get("druids-layout.css", {}).get("content", "")
        
        for selector in critical_selectors:
            assert selector in critical_content, \
                f"Critical selector '{selector}' not found in critical CSS files"
    
    def test_font_loading_strategy(self, css_files):
        """Test that font loading is optimized."""
        theme_css = css_files.get("druids-theme.css", {}).get("content", "")
        
        # Check for @font-face rules
        font_faces = re.findall(r'@font-face\s*{[^}]+}', theme_css, re.DOTALL)
        
        if font_faces:
            for font_face in font_faces:
                # Should use font-display
                assert 'font-display' in font_face, \
                    "Font faces should use font-display for better loading performance"
                
                # Recommend swap or optional
                if 'font-display' in font_face:
                    assert any(value in font_face for value in ['swap', 'optional', 'fallback']), \
                        "Use font-display: swap or optional for better UX"
    
    def test_critical_path_css(self, css_files):
        """Test that critical path CSS is minimal and efficient."""
        critical_files = ["druids-theme.css", "druids-layout.css"]
        
        for filename in critical_files:
            if filename not in css_files:
                continue
                
            content = css_files[filename]["content"]
            
            # Check for non-critical elements
            non_critical_selectors = [
                '.print-only',
                '@media print',
                ':hover',  # Interactions not critical
                '::before',  # Decorative elements
                '::after',
                '.modal',  # Hidden by default
                '.tooltip',
                '.dropdown'
            ]
            
            # Count non-critical rules
            non_critical_count = sum(
                1 for selector in non_critical_selectors
                if selector in content
            )
            
            # Critical CSS should minimize non-critical rules
            total_rules = len(re.findall(r'{[^}]+}', content))
            critical_ratio = 1 - (non_critical_count / max(total_rules, 1))
            
            assert critical_ratio > 0.8, \
                f"Critical CSS file '{filename}' contains too many non-critical rules"
    
    def test_render_blocking_resources(self, css_files):
        """Test for patterns that might block rendering."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Check for @import (render-blocking)
            imports = re.findall(r'@import\s+[^;]+;', content)
            assert len(imports) == 0, \
                f"Avoid @import in {filename} as it blocks rendering. Use <link> instead"
            
            # Check for heavy selectors in critical CSS
            if filename in ["druids-theme.css", "druids-layout.css"]:
                # Avoid attribute selectors in critical path
                complex_selectors = re.findall(r'\[[^\]]+\]', content)
                assert len(complex_selectors) < 5, \
                    f"Too many attribute selectors in critical CSS '{filename}'"
    
    def test_css_loading_order(self, css_files):
        """Test that CSS files are structured for optimal loading."""
        # Expected loading order
        expected_order = [
            "druids-theme.css",    # Variables and base styles
            "druids-layout.css",   # Layout and structure
            "druids-components.css",  # Component styles
            "druids-utilities.css"    # Utility classes
        ]
        
        # Verify all files exist
        for expected_file in expected_order:
            assert expected_file in css_files, \
                f"Expected CSS file '{expected_file}' not found"
        
        # Check dependencies
        theme_css = css_files["druids-theme.css"]["content"]
        
        # Theme should define all custom properties
        custom_props = re.findall(r'--druids-[a-zA-Z0-9-]+:', theme_css)
        assert len(custom_props) > 20, \
            "Theme CSS should define design system custom properties"
    
    def test_inline_critical_css_size(self, css_files):
        """Test that critical CSS is small enough to inline."""
        critical_files = ["druids-theme.css", "druids-layout.css"]
        
        total_critical_size = sum(
            css_files[f]["size"] for f in critical_files
            if f in css_files
        )
        
        # Critical CSS should be under 14KB for inlining
        assert total_critical_size < 14336, \
            f"Combined critical CSS is {total_critical_size} bytes. Should be < 14KB for inlining"
        
        # Individual file recommendations
        recommendations = {
            "druids-theme.css": 8192,   # 8KB
            "druids-layout.css": 6144    # 6KB
        }
        
        for filename, recommended_size in recommendations.items():
            if filename in css_files:
                actual_size = css_files[filename]["size"]
                if actual_size > recommended_size:
                    print(f"Warning: {filename} is {actual_size} bytes, recommended < {recommended_size}")
    
    def test_unused_css_detection(self, css_files):
        """Test for potentially unused CSS patterns."""
        # Common patterns that might indicate unused CSS
        unused_patterns = [
            r'\.unused-',
            r'\.deprecated-',
            r'\.legacy-',
            r'\.old-',
            r'\.temp-',
            r'\.TODO-'
        ]
        
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            for pattern in unused_patterns:
                matches = re.findall(pattern, content)
                assert len(matches) == 0, \
                    f"Potentially unused CSS pattern '{pattern}' found in {filename}"
    
    def test_css_splitting_strategy(self, css_files):
        """Test that CSS is properly split by concern."""
        expected_content = {
            "druids-theme.css": [
                "--druids-",  # Custom properties
                ":root",      # Root variables
                "body",       # Base styles
                "h1", "h2",   # Typography
            ],
            "druids-layout.css": [
                ".md-header",    # Header layout
                ".md-nav",       # Navigation
                ".md-content",   # Content area
                "@media",        # Responsive layout
            ],
            "druids-components.css": [
                ".admonition",   # Components
                "table",         # Tables
                "code",          # Code blocks
                ".md-typeset",   # Typography components
            ],
            "druids-utilities.css": [
                "!important",    # Utility classes need !important
                ".text-",        # Text utilities
                ".bg-",          # Background utilities
            ]
        }
        
        for filename, expected_patterns in expected_content.items():
            if filename not in css_files:
                continue
                
            content = css_files[filename]["content"]
            
            # Check that expected content is present
            for pattern in expected_patterns:
                assert pattern in content, \
                    f"Expected pattern '{pattern}' not found in {filename}"
    
    def test_performance_best_practices(self, css_files):
        """Test for CSS performance best practices."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Avoid universal selector in critical CSS
            if filename in ["druids-theme.css", "druids-layout.css"]:
                universal_selectors = re.findall(r'^\s*\*\s*{', content, re.MULTILINE)
                assert len(universal_selectors) == 0, \
                    f"Avoid universal selector (*) in critical CSS '{filename}'"
            
            # Check for CSS containment
            if ".md-content" in content:
                # Content area could benefit from containment
                if "contain:" not in content:
                    print(f"Consider using CSS containment in {filename} for better performance")
            
            # Check for will-change overuse
            will_change_count = content.count('will-change:')
            assert will_change_count < 5, \
                f"Overuse of will-change in {filename} ({will_change_count} instances). Use sparingly."