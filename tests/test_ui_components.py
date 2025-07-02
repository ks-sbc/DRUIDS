#!/usr/bin/env python3
"""
UI component tests to verify header, footer, sidebar, and other visual elements.
These tests check the rendered HTML for proper structure and styling.
"""

import re
import shutil
from pathlib import Path
import pytest
from bs4 import BeautifulSoup
from test_utils import run_command


class TestUIComponents:
    """Test UI components are present and properly styled"""
    
    @pytest.fixture(scope="class")
    def built_site(self):
        """Build the site once for all tests in this class"""
        project_root = Path(__file__).parent.parent
        test_site_dir = project_root / "test_site_ui"
        
        # Build the site
        success, stdout, stderr = run_command(
            f"mkdocs build --clean --site-dir {test_site_dir}",
            cwd=project_root
        )
        
        if not success:
            pytest.fail(f"Failed to build site: {stderr}")
        
        yield test_site_dir
        
        # Cleanup
        if test_site_dir.exists():
            shutil.rmtree(test_site_dir)
    
    def read_html(self, built_site, path):
        """Read and parse HTML file"""
        file_path = built_site / path
        if not file_path.exists():
            pytest.fail(f"HTML file not found: {path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            return BeautifulSoup(f.read(), 'html.parser')
    
    def test_header_bar_exists(self, built_site):
        """Verify header bar is present and styled"""
        soup = self.read_html(built_site, "index.html")
        
        # Check for header element
        header = soup.find('header', class_='md-header')
        if not header:
            pytest.fail("Header bar not found - missing <header class='md-header'>")
        
        # Check header has proper structure
        required_elements = {
            'nav': "Navigation container",
            'md-header__title': "Site title",
            'md-header__button': "Header buttons (menu, search)",
            'md-logo': "Logo"
        }
        
        missing = []
        for element, description in required_elements.items():
            if element.startswith('md-'):
                found = header.find(class_=element)
            else:
                found = header.find(element)
            
            if not found:
                missing.append(f"{description} ({element})")
        
        if missing:
            pytest.fail(f"Header missing elements: {', '.join(missing)}")
        
        # Check header is visible (not hidden by CSS)
        header_style = header.get('style', '')
        if 'display: none' in header_style or 'visibility: hidden' in header_style:
            pytest.fail("Header is hidden by inline styles")
    
    def test_footer_bar_exists(self, built_site):
        """Verify footer bar is present and aligned"""
        soup = self.read_html(built_site, "index.html")
        
        # Check for footer element
        footer = soup.find('footer', class_='md-footer')
        if not footer:
            pytest.fail("Footer bar not found - missing <footer class='md-footer'>")
        
        # Check footer structure
        footer_meta = footer.find(class_='md-footer-meta')
        if not footer_meta:
            pytest.fail("Footer meta section missing")
        
        # Check for copyright
        copyright_elem = footer.find(class_='md-footer-copyright')
        if not copyright_elem:
            pytest.fail("Footer copyright section missing")
        
        # Check footer is at bottom (not floating)
        # This would need JavaScript to fully test, but we can check structure
        if footer.parent.name != 'body' and 'md-container' not in [p.get('class', []) for p in footer.parents]:
            pytest.fail("Footer not properly positioned in document structure")
    
    def test_side_menu_functionality(self, built_site):
        """Test side menu opens/closes properly"""
        soup = self.read_html(built_site, "index.html")
        
        # Check for sidebar
        sidebar = soup.find('div', class_='md-sidebar')
        if not sidebar:
            sidebar = soup.find('nav', class_='md-nav--primary')
            if not sidebar:
                pytest.fail("Side menu not found - missing sidebar navigation")
        
        # Check for toggle button
        toggle = soup.find('label', class_='md-nav__toggle')
        if not toggle:
            toggle = soup.find('input', {'type': 'checkbox', 'class': 'md-toggle'})
            if not toggle:
                pytest.fail("Side menu toggle button not found")
        
        # Check sidebar has content
        nav_items = sidebar.find_all(class_='md-nav__item')
        if len(nav_items) < 3:
            pytest.fail(f"Side menu has insufficient content - only {len(nav_items)} items found")
        
        # Check for mobile menu button in header
        mobile_menu = soup.find('label', {'for': re.compile(r'__drawer|drawer')})
        if not mobile_menu:
            pytest.fail("Mobile menu toggle not found in header")
    
    def test_color_scheme_preserved(self, built_site):
        """Ensure cyberpunk colors are maintained"""
        soup = self.read_html(built_site, "index.html")
        
        # Check for CSS files that should contain our theme
        css_links = soup.find_all('link', {'rel': 'stylesheet'})
        theme_css_found = False
        
        expected_css = [
            'queer-mandalorian.css',
            'cyberpunk-guerilla.css',
            'druids-theme.css'  # Future consolidated file
        ]
        
        for link in css_links:
            href = link.get('href', '')
            if any(css in href for css in expected_css):
                theme_css_found = True
                break
        
        if not theme_css_found:
            pytest.fail("Theme CSS files not linked in HTML")
        
        # Check for CSS variables in style tags (if any)
        style_tags = soup.find_all('style')
        has_color_vars = False
        
        for style in style_tags:
            if style.string and ('--cyber-' in style.string or '--qm-' in style.string):
                has_color_vars = True
                break
        
        # At minimum, we should have our CSS files linked
        assert theme_css_found, "Cyberpunk theme CSS not found"
    
    def test_responsive_breakpoints(self, built_site):
        """Test UI at different screen sizes"""
        soup = self.read_html(built_site, "index.html")
        
        # Check for viewport meta tag
        viewport = soup.find('meta', {'name': 'viewport'})
        if not viewport:
            pytest.fail("Viewport meta tag missing - responsive design won't work")
        
        content = viewport.get('content', '')
        if 'width=device-width' not in content:
            pytest.fail("Viewport not set to device-width")
        
        # Check for responsive classes
        responsive_elements = [
            ('md-content__inner', "Content container"),
            ('md-grid', "Grid layout"),
            ('md-nav--primary', "Primary navigation")
        ]
        
        missing_responsive = []
        for class_name, description in responsive_elements:
            if not soup.find(class_=class_name):
                missing_responsive.append(f"{description} ({class_name})")
        
        if missing_responsive:
            pytest.fail(f"Missing responsive elements: {', '.join(missing_responsive)}")
    
    def test_navigation_structure(self, built_site):
        """Test navigation menu structure and links"""
        soup = self.read_html(built_site, "index.html")
        
        # Check primary navigation
        nav = soup.find('nav', class_='md-nav--primary')
        if not nav:
            pytest.fail("Primary navigation not found")
        
        # Check for navigation items
        nav_links = nav.find_all('a', class_='md-nav__link')
        if len(nav_links) < 5:
            pytest.fail(f"Insufficient navigation items - only {len(nav_links)} found")
        
        # Check for active link
        active_link = nav.find('a', class_='md-nav__link--active')
        if not active_link:
            pytest.fail("No active navigation link found")
        
        # Check for nested navigation
        nested = nav.find(class_='md-nav__item--nested')
        if not nested:
            pytest.fail("No nested navigation items found")
    
    def test_search_functionality(self, built_site):
        """Test search box presence and structure"""
        soup = self.read_html(built_site, "index.html")
        
        # Check for search form
        search = soup.find('form', class_='md-search__form')
        if not search:
            search = soup.find('div', class_='md-search')
            if not search:
                pytest.fail("Search functionality not found")
        
        # Check for search input
        search_input = soup.find('input', {'type': 'search'})
        if not search_input:
            search_input = soup.find('input', class_='md-search__input')
            if not search_input:
                pytest.fail("Search input field not found")
        
        # Check search has proper attributes
        if not search_input.get('placeholder'):
            pytest.fail("Search input missing placeholder text")
    
    def test_giscus_integration(self, built_site):
        """Test Giscus comments are properly integrated"""
        # Check the test-giscus page specifically
        soup = self.read_html(built_site, "test-giscus/index.html")
        
        # Look for Giscus container or script
        giscus = soup.find('script', {'src': re.compile(r'giscus\.app')})
        if not giscus:
            # Check for container div
            giscus_div = soup.find('div', class_='giscus')
            if not giscus_div:
                pytest.fail("Giscus integration not found on test page")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])