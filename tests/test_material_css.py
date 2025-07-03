"""Test CSS support for Material for MkDocs components.

This tests that our consolidated CSS files properly support:
- Annotations
- Buttons  
- Grids
- Tooltips
"""

import pytest
from pathlib import Path
import re


class TestMaterialCSS:
    """Test that our CSS files include Material component styles."""
    
    @pytest.fixture(scope="class")
    def css_files(self):
        """Load all CSS files."""
        css_dir = Path("docs/assets/css")
        css_content = {}
        for css_file in css_dir.glob("*.css"):
            with open(css_file, 'r') as f:
                css_content[css_file.name] = f.read()
        return css_content
    
    def test_annotation_styles_exist(self, css_files):
        """Test that annotation CSS is present."""
        required_selectors = [
            r"\.md-annotation",  # Annotation container
            r"\.md-annotation__index",  # Annotation number/marker
            r"\.md-annotation__content",  # Annotation popup content
            r"\.md-annotation--active",  # Active state
        ]
        
        all_css = "\n".join(css_files.values())
        
        missing = []
        for selector in required_selectors:
            if not re.search(selector, all_css):
                missing.append(selector.replace("\\", ""))
        
        assert not missing, f"Missing annotation CSS selectors: {', '.join(missing)}"
    
    def test_button_styles_exist(self, css_files):
        """Test that button CSS is present."""
        required_selectors = [
            r"\.md-button",  # Base button
            r"\.md-button--primary",  # Primary variant
            r"\.md-button:hover",  # Hover state
            r"\.md-button:active",  # Active state
        ]
        
        all_css = "\n".join(css_files.values())
        
        missing = []
        for selector in required_selectors:
            if not re.search(selector, all_css):
                missing.append(selector.replace("\\", ""))
        
        assert not missing, f"Missing button CSS selectors: {', '.join(missing)}"
        
        # Check button has proper styling
        button_styles = re.findall(r"\.md-button\s*{([^}]+)}", all_css)
        if button_styles:
            styles = button_styles[0]
            assert "padding" in styles, "Buttons should have padding"
            assert "background" in styles or "background-color" in styles, \
                "Buttons should have background"
            assert "border-radius" in styles, "Buttons should have rounded corners"
    
    def test_grid_styles_exist(self, css_files):
        """Test that grid CSS is present."""
        required_selectors = [
            r"\.grid",  # Base grid
            r"\.grid\.cards",  # Card grid variant
            r"\.grid\s*{[^}]*display:\s*(grid|flex)",  # Uses CSS Grid or Flexbox
        ]
        
        all_css = "\n".join(css_files.values())
        
        # Check base grid class exists
        assert re.search(r"\.grid", all_css), "Missing .grid class"
        
        # Check card variant
        assert re.search(r"\.grid\.cards", all_css) or \
               re.search(r"\.grid.cards", all_css), \
               "Missing .grid.cards class"
        
        # Check uses modern layout
        grid_css = re.findall(r"\.grid[^{]*{([^}]+)}", all_css)
        if grid_css:
            styles = " ".join(grid_css)
            assert "display: grid" in styles or "display: flex" in styles, \
                "Grid should use CSS Grid or Flexbox"
            assert "gap" in styles or "grid-gap" in styles or "margin" in styles, \
                "Grid should have spacing between items"
    
    def test_tooltip_styles_exist(self, css_files):
        """Test that tooltip CSS is present."""
        # Tooltips can be implemented in different ways
        tooltip_patterns = [
            r"\.md-tooltip",  # Material tooltip class
            r"abbr\[title\]",  # Abbr tooltip styling
            r"\[data-md-tooltip\]",  # Data attribute styling
            r"::after.*content.*attr\(title\)",  # CSS tooltip using ::after
        ]
        
        all_css = "\n".join(css_files.values())
        
        found_any = False
        for pattern in tooltip_patterns:
            if re.search(pattern, all_css):
                found_any = True
                break
        
        assert found_any, "No tooltip styling found (checked multiple patterns)"
    
    def test_material_component_colors(self, css_files):
        """Test that Material components use our color scheme."""
        all_css = "\n".join(css_files.values())
        
        # Extract button styles
        button_matches = re.findall(r"\.md-button[^{]*{([^}]+)}", all_css, re.DOTALL)
        if button_matches:
            button_css = " ".join(button_matches)
            # Should use our color variables
            assert "var(--druids-" in button_css or \
                   "#00D9FF" in button_css or \
                   "#FF6B35" in button_css, \
                   "Buttons should use DRUIDS color scheme"
        
        # Check grid cards use our styling
        grid_matches = re.findall(r"\.grid\.cards[^{]*{([^}]+)}", all_css, re.DOTALL)
        if grid_matches:
            grid_css = " ".join(grid_matches)
            assert "var(--druids-" in grid_css or "border" in grid_css, \
                "Grid cards should use DRUIDS styling"
    
    def test_interactive_states(self, css_files):
        """Test that interactive elements have proper states."""
        all_css = "\n".join(css_files.values())
        
        # Check hover states
        assert re.search(r"\.md-button:hover", all_css), \
            "Buttons should have hover state"
        
        # Check focus states  
        assert re.search(r"\.md-button:focus|\.md-annotation.*:focus", all_css), \
            "Interactive elements should have focus states"
        
        # Check active/clicked states
        assert re.search(r":active|--active", all_css), \
            "Interactive elements should have active states"
    
    def test_responsive_styles(self, css_files):
        """Test that components have responsive styles."""
        all_css = "\n".join(css_files.values())
        
        # Check for media queries
        media_queries = re.findall(r"@media[^{]+", all_css)
        assert len(media_queries) > 0, "Should have media queries for responsive design"
        
        # Check grid is responsive
        if re.search(r"\.grid", all_css):
            # Should have responsive grid columns
            assert re.search(r"repeat\s*\(\s*auto-fit|grid-template-columns.*minmax", all_css), \
                "Grid should be responsive"
    
    def test_css_organization(self, css_files):
        """Test that Material styles are in appropriate files."""
        # Components should be in druids-components.css
        components_css = css_files.get("druids-components.css", "")
        
        # At least some Material components should be defined
        material_selectors = [".md-button", ".grid", ".md-annotation", ".md-tooltip"]
        found_count = sum(1 for sel in material_selectors if sel in components_css)
        
        assert found_count >= 2, \
            f"druids-components.css should contain Material component styles, found {found_count}/4"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])