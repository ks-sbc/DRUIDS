#!/usr/bin/env python3
"""
Tests specifically for wikilink rendering behavior with pub-obsidian plugin.
These tests ensure wikilinks are converted correctly to HTML links.
"""

import tempfile
import shutil
from pathlib import Path
import pytest
from bs4 import BeautifulSoup
from test_utils import run_command


class TestWikilinkRendering:
    """Test wikilink to HTML conversion"""
    
    @pytest.fixture
    def test_docs_dir(self):
        """Create a temporary docs directory with test content"""
        temp_dir = tempfile.mkdtemp()
        docs_dir = Path(temp_dir) / "docs"
        docs_dir.mkdir()
        
        # Create test pages with various wikilink patterns
        test_pages = {
            "index.md": """# Test Index

## Basic Wikilinks
- [[page1|Page One]]
- [[page2]]
- [[subdir/page3|Page in Subdirectory]]

## Relative Wikilinks
- [[../other|Parent Directory Link]]

## Mixed Syntax (SHOULD NOT WORK)
- [Mixed Link]([[page1]])
- [:icon: Text]([[page2|Display]])
""",
            "page1.md": "# Page One\nContent for page 1",
            "page2.md": "# Page Two\nContent for page 2",
            "subdir/page3.md": "# Page Three\nContent for page 3",
        }
        
        for path, content in test_pages.items():
            file_path = docs_dir / path
            file_path.parent.mkdir(exist_ok=True)
            file_path.write_text(content)
        
        yield temp_dir
        
        # Cleanup
        shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def test_mkdocs_config(self, test_docs_dir):
        """Create a test mkdocs.yml"""
        config_content = """site_name: Wikilink Test
theme:
  name: material

plugins:
  - search
  - pub-obsidian:
      obsidian_dir: .obsidian
      links:
        wikilinks_enabled: true
"""
        config_path = Path(test_docs_dir) / "mkdocs.yml"
        config_path.write_text(config_content)
        return config_path
    
    def build_and_parse(self, test_docs_dir, page="index.html"):
        """Build site and parse specific page"""
        site_dir = Path(test_docs_dir) / "site"
        
        success, stdout, stderr = run_command(
            f"mkdocs build --clean --site-dir {site_dir}",
            cwd=test_docs_dir
        )
        
        if not success:
            pytest.fail(f"Build failed: {stderr}")
        
        html_file = site_dir / page
        if not html_file.exists():
            pytest.fail(f"HTML file not found: {page}")
        
        with open(html_file, 'r') as f:
            return BeautifulSoup(f.read(), 'html.parser')
    
    @pytest.mark.integration
    def test_basic_wikilinks_convert_to_html(self, test_docs_dir, test_mkdocs_config):
        """Test that basic wikilinks convert to proper HTML links"""
        soup = self.build_and_parse(test_docs_dir)
        
        # Find all links in the content
        content = soup.find('div', class_='md-content') or soup.find('main')
        links = content.find_all('a', href=True) if content else []
        
        # Check conversions
        expected_conversions = {
            'Page One': 'page1/',
            'page2': 'page2/',
            'Page in Subdirectory': 'subdir/page3/'
        }
        
        found_links = {link.get_text(strip=True): link.get('href', '') for link in links}
        
        for text, expected_href in expected_conversions.items():
            assert text in found_links, f"Link text '{text}' not found"
            # Allow for index.html suffix
            actual_href = found_links[text]
            assert (actual_href == expected_href or 
                   actual_href == expected_href + 'index.html'), \
                f"Link '{text}' has href '{actual_href}', expected '{expected_href}'"
    
    @pytest.mark.integration
    def test_mixed_syntax_fails_gracefully(self, test_docs_dir, test_mkdocs_config):
        """Test that mixed Markdown/Wikilink syntax doesn't create broken output"""
        soup = self.build_and_parse(test_docs_dir)
        
        # Check that we don't have malformed hrefs
        all_links = soup.find_all('a', href=True)
        
        for link in all_links:
            href = link.get('href', '')
            # Should not contain wikilink syntax in href
            assert '[[' not in href and ']]' not in href, \
                f"Found wikilink syntax in href: {href}"
            # Should not have the broken pattern we saw
            assert not href.startswith('['), \
                f"Found bracket at start of href: {href}"
    
    @pytest.mark.integration
    def test_wikilinks_without_display_text(self, test_docs_dir, test_mkdocs_config):
        """Test that [[page]] uses page name as display text"""
        soup = self.build_and_parse(test_docs_dir)
        
        # Find link with text 'page2'
        page2_links = [
            link for link in soup.find_all('a', href=True)
            if link.get_text(strip=True) == 'page2'
        ]
        
        assert len(page2_links) > 0, "Link to page2 not found"
        assert page2_links[0].get('href', '') in ['page2/', 'page2/index.html'], \
            "page2 link has incorrect href"
    
    @pytest.mark.integration
    def test_relative_wikilinks(self, test_docs_dir, test_mkdocs_config):
        """Test that relative wikilinks work correctly"""
        # Create a page in a subdirectory that links to parent
        subdir = Path(test_docs_dir) / "docs" / "subdir"
        subdir.mkdir(exist_ok=True)
        
        (subdir / "child.md").write_text("""# Child Page
Link to parent: [[../index|Home]]
Link to sibling: [[page3|Page Three]]
""")
        
        soup = self.build_and_parse(test_docs_dir, "subdir/child.html")
        
        links = {
            link.get_text(strip=True): link.get('href', '')
            for link in soup.find_all('a', href=True)
        }
        
        # Check parent link
        assert 'Home' in links, "Parent link not found"
        assert links['Home'] in ['../index.html', '../'], \
            f"Parent link incorrect: {links.get('Home')}"
        
        # Check sibling link
        assert 'Page Three' in links, "Sibling link not found"
    
    @pytest.mark.integration
    def test_no_hash_anchors_in_wikilinks(self, test_docs_dir, test_mkdocs_config):
        """Test that wikilinks don't generate hash anchors"""
        soup = self.build_and_parse(test_docs_dir)
        
        # Check all links for hash patterns
        links_with_hashes = []
        for link in soup.find_all('a', href=True):
            href = link.get('href', '')
            # Look for MD5-like hashes
            if '#' in href and len(href.split('#')[1]) == 32:
                links_with_hashes.append({
                    'text': link.get_text(strip=True),
                    'href': href
                })
        
        assert len(links_with_hashes) == 0, \
            f"Found links with hash anchors: {links_with_hashes}"
    
    @pytest.mark.integration
    def test_wikilink_errors_reported(self, test_docs_dir, test_mkdocs_config):
        """Test that broken wikilinks are reported during build"""
        # Add a page with broken wikilink
        docs_dir = Path(test_docs_dir) / "docs"
        (docs_dir / "broken.md").write_text("""# Broken Links
- [[nonexistent|This Doesn't Exist]]
- [[../nowhere|Also Missing]]
""")
        
        site_dir = Path(test_docs_dir) / "site"
        success, stdout, stderr = run_command(
            f"mkdocs build --clean --site-dir {site_dir}",
            cwd=test_docs_dir
        )
        
        # Build should succeed but with warnings
        assert success, "Build should succeed even with broken links"
        
        # Check for warnings in output
        output = stdout + stderr
        assert 'nonexistent' in output or 'not found' in output.lower(), \
            "Build should warn about broken wikilinks"