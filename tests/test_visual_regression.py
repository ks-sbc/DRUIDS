"""Test visual dimensions and layout specifications."""

import re
import subprocess
from pathlib import Path
import pytest
import tempfile
import shutil


class TestVisualRegression:
    """Test that CSS produces correct visual output."""
    
    @pytest.fixture
    def css_content(self):
        """Load all CSS files content."""
        css_files = {}
        css_dir = Path("docs/assets/css")
        for css_file in css_dir.glob("druids-*.css"):
            css_files[css_file.name] = css_file.read_text()
        return css_files
    
    def test_header_height_specification(self, css_content):
        """Test that header height is correctly set to 2.5rem."""
        layout_css = css_content.get("druids-layout.css", "")
        
        # Check .md-header__inner height
        pattern = r'\.md-header__inner\s*{[^}]*height:\s*([^;]+);'
        match = re.search(pattern, layout_css, re.DOTALL)
        
        assert match is not None, "No height specification found for .md-header__inner"
        height_value = match.group(1).strip()
        assert height_value == "2.5rem", f"Header height should be 2.5rem, got {height_value}"
    
    def test_header_padding_removed(self, css_content):
        """Test that header padding has been removed."""
        layout_css = css_content.get("druids-layout.css", "")
        
        # Check .md-header padding
        pattern = r'\.md-header\s*{[^}]*padding:\s*([^;]+);'
        match = re.search(pattern, layout_css, re.DOTALL)
        
        assert match is not None, "No padding specification found for .md-header"
        padding_value = match.group(1).strip()
        assert padding_value == "0", f"Header padding should be 0, got {padding_value}"
    
    def test_logo_size_reduced(self, css_content):
        """Test that logo size is reduced to 2rem."""
        layout_css = css_content.get("druids-layout.css", "")
        
        # Check .md-logo img height
        pattern = r'\.md-logo\s+img\s*{[^}]*height:\s*([^;]+);'
        match = re.search(pattern, layout_css, re.DOTALL)
        
        assert match is not None, "No height specification found for .md-logo img"
        height_value = match.group(1).strip()
        assert height_value == "2rem", f"Logo height should be 2rem, got {height_value}"
    
    def test_duplicate_title_hidden(self, css_content):
        """Test that duplicate site title is hidden."""
        layout_css = css_content.get("druids-layout.css", "")
        
        # Check that first topic is hidden
        pattern = r'\.md-header__topic:first-child\s*{[^}]*display:\s*([^;]+);'
        match = re.search(pattern, layout_css, re.DOTALL)
        
        assert match is not None, "No display rule found for hiding duplicate title"
        display_value = match.group(1).strip()
        assert display_value == "none", f"First topic should be hidden, got display: {display_value}"
    
    def test_search_box_responsive(self, css_content):
        """Test that search box uses max-width for responsiveness."""
        layout_css = css_content.get("druids-layout.css", "")
        
        # Check .md-search__input has max-width
        pattern = r'\.md-search__input\s*{[^}]*max-width:\s*([^;]+);'
        match = re.search(pattern, layout_css, re.DOTALL)
        
        assert match is not None, "No max-width found for search input"
        max_width_value = match.group(1).strip()
        assert max_width_value == "15rem", f"Search box max-width should be 15rem, got {max_width_value}"
        
        # Also check it has width: 100%
        pattern = r'\.md-search__input\s*{[^}]*width:\s*([^;]+);'
        match = re.search(pattern, layout_css, re.DOTALL)
        
        assert match is not None, "No width found for search input"
        width_value = match.group(1).strip()
        assert width_value == "100%", f"Search box width should be 100%, got {width_value}"
    
    def test_content_padding_reduced(self, css_content):
        """Test that content padding is reduced."""
        layout_css = css_content.get("druids-layout.css", "")
        
        # Check .md-content padding
        pattern = r'\.md-content\s*{[^}]*padding:\s*([^;]+);'
        match = re.search(pattern, layout_css, re.DOTALL)
        
        assert match is not None, "No padding found for content"
        padding_value = match.group(1).strip()
        assert padding_value == "1rem 1.5rem", f"Content padding should be '1rem 1.5rem', got {padding_value}"
    
    def test_container_padding_matches_header(self, css_content):
        """Test that container padding-top matches header height."""
        layout_css = css_content.get("druids-layout.css", "")
        
        # Check .md-container padding-top
        pattern = r'\.md-container\s*{[^}]*padding-top:\s*([^;]+);'
        match = re.search(pattern, layout_css, re.DOTALL)
        
        assert match is not None, "No padding-top found for container"
        padding_value = match.group(1).strip()
        assert padding_value == "2.5rem", f"Container padding-top should match header (2.5rem), got {padding_value}"
    
    def test_heading_sizes_reduced(self, css_content):
        """Test that heading sizes use fluid typography variables."""
        theme_css = css_content.get("druids-theme.css", "")
        
        # Check h1 uses variable
        pattern = r'h1\s*{[^}]*font-size:\s*([^;]+);'
        match = re.search(pattern, theme_css, re.DOTALL)
        
        assert match is not None, "No font-size found for h1"
        size_value = match.group(1).strip()
        assert "var(--druids-text-3xl)" in size_value, f"h1 should use var(--druids-text-3xl), got {size_value}"
        
        # Check h2 uses variable
        pattern = r'h2\s*{[^}]*font-size:\s*([^;]+);'
        match = re.search(pattern, theme_css, re.DOTALL)
        
        assert match is not None, "No font-size found for h2"
        size_value = match.group(1).strip()
        assert "var(--druids-text-2xl)" in size_value, f"h2 should use var(--druids-text-2xl), got {size_value}"
    
    def test_mobile_breakpoints(self, css_content):
        """Test that mobile breakpoints are properly defined."""
        layout_css = css_content.get("druids-layout.css", "")
        
        # Check for mobile breakpoint at 767px
        assert "@media screen and (max-width: 767px)" in layout_css, \
            "Missing mobile breakpoint at 767px"
        
        # Check for tablet breakpoint range
        assert "@media screen and (min-width: 768px) and (max-width: 959px)" in layout_css, \
            "Missing tablet breakpoint range"
        
        # Check mobile header height adjustment
        pattern = r'@media[^{]+767px[^{]+{[^}]*\.md-header__inner\s*{[^}]*height:\s*([^;]+);'
        match = re.search(pattern, layout_css, re.DOTALL)
        
        if match:
            height_value = match.group(1).strip()
            assert height_value == "2.25rem", f"Mobile header height should be 2.25rem, got {height_value}"
    
    def test_component_spacing_reduced(self, css_content):
        """Test that component margins are reduced."""
        components_css = css_content.get("druids-components.css", "")
        
        # Check code block margins
        pattern = r'\.md-typeset\s+pre\s*{[^}]*margin:\s*([^;]+);'
        match = re.search(pattern, components_css, re.DOTALL)
        
        assert match is not None, "No margin found for code blocks"
        margin_value = match.group(1).strip()
        assert margin_value == "0.75rem 0", f"Code block margin should be 0.75rem 0, got {margin_value}"
        
        # Check admonition margins
        pattern = r'\.md-typeset\s+\.admonition\s*{[^}]*margin:\s*([^;]+);'
        match = re.search(pattern, components_css, re.DOTALL)
        
        assert match is not None, "No margin found for admonitions"
        margin_value = match.group(1).strip()
        assert margin_value == "1rem 0", f"Admonition margin should be 1rem 0, got {margin_value}"
    
    def test_build_succeeds(self):
        """Test that site builds successfully with CSS changes."""
        # Create temporary directory for build
        with tempfile.TemporaryDirectory() as temp_dir:
            # Run mkdocs build
            result = subprocess.run(
                ["mkdocs", "build", "--site-dir", temp_dir, "--clean"],
                capture_output=True,
                text=True
            )
            
            assert result.returncode == 0, f"MkDocs build failed: {result.stderr}"
            
            # Check that CSS files are copied to build
            css_dir = Path(temp_dir) / "assets" / "css"
            assert css_dir.exists(), "CSS directory not found in build"
            
            expected_files = [
                "druids-theme.css",
                "druids-layout.css",
                "druids-components.css",
                "druids-utilities.css"
            ]
            
            for css_file in expected_files:
                assert (css_dir / css_file).exists(), f"{css_file} not found in build output"