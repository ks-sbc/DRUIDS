"""Test CSS-specific accessibility standards and WCAG compliance."""

import re
from pathlib import Path
import pytest


class TestCSSAccessibility:
    """Test that CSS meets WCAG accessibility standards."""
    
    @pytest.fixture
    def theme_css(self):
        """Load theme CSS containing color definitions."""
        css_file = Path("docs/assets/css/druids-theme.css")
        return css_file.read_text()
    
    def _hex_to_rgb(self, hex_color):
        """Convert hex color to RGB values."""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def _relative_luminance(self, rgb):
        """Calculate relative luminance of RGB color."""
        r, g, b = [x / 255.0 for x in rgb]
        
        # Apply gamma correction
        r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
        g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
        b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4
        
        return 0.2126 * r + 0.7152 * g + 0.0722 * b
    
    def _contrast_ratio(self, color1_hex, color2_hex):
        """Calculate contrast ratio between two colors."""
        rgb1 = self._hex_to_rgb(color1_hex)
        rgb2 = self._hex_to_rgb(color2_hex)
        
        lum1 = self._relative_luminance(rgb1)
        lum2 = self._relative_luminance(rgb2)
        
        lighter = max(lum1, lum2)
        darker = min(lum1, lum2)
        
        return (lighter + 0.05) / (darker + 0.05)
    
    def test_text_color_contrast(self, theme_css):
        """Test that primary text color meets WCAG AA standards."""
        # Extract color values
        text_primary_match = re.search(r'--druids-text-primary:\s*([^;]+);', theme_css)
        bg_primary_match = re.search(r'--druids-bg-primary:\s*([^;]+);', theme_css)
        
        assert text_primary_match and bg_primary_match, "Could not find color definitions"
        
        text_color = text_primary_match.group(1).strip()
        bg_color = bg_primary_match.group(1).strip()
        
        # Colors from our CSS
        assert text_color == "#F0F0F0", f"Expected text color #F0F0F0, got {text_color}"
        assert bg_color == "#0A0E27", f"Expected bg color #0A0E27, got {bg_color}"
        
        # Calculate contrast ratio
        ratio = self._contrast_ratio(text_color, bg_color)
        
        # WCAG AA requires 4.5:1 for normal text
        assert ratio >= 4.5, f"Text contrast ratio {ratio:.2f} is below WCAG AA standard of 4.5:1"
    
    def test_link_color_contrast(self, theme_css):
        """Test that link colors meet WCAG AA standards."""
        # Extract color values
        cyan_match = re.search(r'--druids-cyan:\s*([^;]+);', theme_css)
        bg_primary_match = re.search(r'--druids-bg-primary:\s*([^;]+);', theme_css)
        
        assert cyan_match and bg_primary_match, "Could not find color definitions"
        
        link_color = cyan_match.group(1).strip()
        bg_color = bg_primary_match.group(1).strip()
        
        # Calculate contrast ratio
        ratio = self._contrast_ratio(link_color, bg_color)
        
        # WCAG AA requires 4.5:1 for normal text (links are normal text)
        assert ratio >= 4.5, f"Link contrast ratio {ratio:.2f} is below WCAG AA standard of 4.5:1"
    
    def test_large_text_contrast(self, theme_css):
        """Test that large text (headings) meet WCAG AA standards."""
        # Extract color values for headings
        orange_match = re.search(r'--druids-orange:\s*([^;]+);', theme_css)
        rust_match = re.search(r'--druids-rust:\s*([^;]+);', theme_css)
        bg_primary_match = re.search(r'--druids-bg-primary:\s*([^;]+);', theme_css)
        
        assert orange_match and rust_match and bg_primary_match, "Could not find color definitions"
        
        # Test orange (h2) on dark background
        orange_color = orange_match.group(1).strip()
        bg_color = bg_primary_match.group(1).strip()
        
        ratio = self._contrast_ratio(orange_color, bg_color)
        
        # WCAG AA requires 3:1 for large text (18pt+ or 14pt+ bold)
        assert ratio >= 3.0, f"Orange heading contrast ratio {ratio:.2f} is below WCAG AA standard of 3:1 for large text"
        
        # Test rust (h1) on dark background
        rust_color = rust_match.group(1).strip()
        ratio = self._contrast_ratio(rust_color, bg_color)
        
        assert ratio >= 3.0, f"Rust heading contrast ratio {ratio:.2f} is below WCAG AA standard of 3:1 for large text"
    
    def test_focus_indicators(self):
        """Test that focus indicators are properly defined."""
        css_files = ["druids-theme.css", "druids-utilities.css"]
        focus_defined = False
        
        for filename in css_files:
            css_file = Path(f"docs/assets/css/{filename}")
            if css_file.exists():
                content = css_file.read_text()
                if ":focus" in content:
                    # Check for outline or other focus indicator
                    pattern = r':focus\s*{[^}]*(?:outline|border|box-shadow)[^}]*}'
                    if re.search(pattern, content, re.DOTALL):
                        focus_defined = True
                        break
        
        assert focus_defined, "No focus indicators found in CSS"
    
    def test_touch_target_sizes(self):
        """Test that interactive elements have adequate touch target sizes."""
        layout_css = Path("docs/assets/css/druids-layout.css").read_text()
        
        # Check button/link padding for header buttons
        pattern = r'\.md-header__button\s*{[^}]*padding:\s*([^;]+);'
        match = re.search(pattern, layout_css, re.DOTALL)
        
        if match:
            padding = match.group(1).strip()
            # 0.5rem = 8px, so total size with content should be adequate
            assert "0.5rem" in padding or "0.75rem" in padding or "1rem" in padding, \
                f"Header button padding {padding} may be too small for touch targets"
    
    def test_reduced_motion_support(self):
        """Test that reduced motion preferences are respected."""
        utilities_css = Path("docs/assets/css/druids-utilities.css").read_text()
        
        # Check for prefers-reduced-motion media query
        assert "@media (prefers-reduced-motion: reduce)" in utilities_css, \
            "No reduced motion support found"
        
        # Check that animations are disabled in reduced motion
        pattern = r'@media\s*\(prefers-reduced-motion:\s*reduce\)[^{]*{[^}]*(?:animation|transition)[^}]*}'
        match = re.search(pattern, utilities_css, re.DOTALL)
        
        assert match is not None, "Reduced motion media query should disable animations"
    
    def test_high_contrast_support(self):
        """Test that high contrast mode is supported."""
        utilities_css = Path("docs/assets/css/druids-utilities.css").read_text()
        
        # Check for prefers-contrast media query
        assert "@media (prefers-contrast: high)" in utilities_css, \
            "No high contrast mode support found"
    
    def test_semantic_color_usage(self):
        """Test that colors are used semantically."""
        theme_css = Path("docs/assets/css/druids-theme.css").read_text()
        
        # Check that CSS variables have semantic names
        semantic_vars = [
            "--druids-text-primary",
            "--druids-text-bright", 
            "--druids-text-muted",
            "--druids-bg-primary",
            "--druids-bg-secondary"
        ]
        
        for var in semantic_vars:
            assert var in theme_css, f"Missing semantic color variable: {var}"
    
    def test_font_size_minimums(self):
        """Test that font sizes meet minimum recommendations."""
        theme_css = Path("docs/assets/css/druids-theme.css").read_text()
        
        # Check base font size
        pattern = r'--druids-text-base:\s*([^;]+);'
        match = re.search(pattern, theme_css)
        
        if match:
            base_size = match.group(1).strip()
            # Should use clamp with minimum 1rem (16px)
            assert "clamp(" in base_size, "Base font should use clamp() for responsive sizing"
            assert "1rem" in base_size, "Base font minimum should be at least 1rem (16px)"
    
    def test_line_height_readability(self):
        """Test that line heights support readability."""
        theme_css = Path("docs/assets/css/druids-theme.css").read_text()
        
        # Check line height values
        pattern = r'--druids-line-height:\s*([^;]+);'
        match = re.search(pattern, theme_css)
        
        if match:
            line_height = float(match.group(1).strip())
            # WCAG recommends 1.5 for body text
            assert line_height >= 1.5, f"Line height {line_height} is below recommended 1.5"
    
    def test_color_blind_considerations(self):
        """Test that color is not the only means of conveying information."""
        # This is more of a reminder test - actual implementation would need manual review
        components_css = Path("docs/assets/css/druids-components.css").read_text()
        
        # Check that links have underlines or other indicators besides color
        assert "text-decoration" in components_css or "border-bottom" in components_css, \
            "Links should have non-color indicators for color-blind users"
        
        # Check that error/warning states use more than just color
        # Look for icons or borders in addition to color changes
        assert "border" in components_css, \
            "Components should use borders or other non-color indicators"