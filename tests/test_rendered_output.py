#!/usr/bin/env python3
"""
Tests for rendered HTML output to catch issues that configuration tests miss.
These tests build the site and check the actual generated HTML.
"""

import re
import shutil
from pathlib import Path
import pytest
from bs4 import BeautifulSoup
from test_utils import run_command


def get_project_root():
    """Get the project root directory"""
    return Path(__file__).parent.parent


class TestRenderedOutput:
    """Test the actual rendered HTML output"""
    
    @pytest.fixture(scope="class")
    def built_site(self):
        """Build the site once for all tests in this class"""
        project_root = get_project_root()
        test_site_dir = project_root / "test_site_rendered"
        
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
    
    @pytest.mark.integration
    def test_no_broken_wikilink_syntax(self, built_site):
        """Test that wikilinks don't have mixed syntax in rendered output"""
        # Check tutorials page which had the issue
        soup = self.read_html(built_site, "tutorials/index.html")
        
        # Find all links
        links = soup.find_all('a', href=True)
        
        broken_patterns = []
        for link in links:
            href = link.get('href', '')
            # Check for the broken pattern: [../path](../path.md){#hash}
            if re.search(r'\[.*\]\(.*\)\{#[a-f0-9]+\}', href):
                broken_patterns.append({
                    'href': href,
                    'text': link.get_text(strip=True)
                })
        
        assert len(broken_patterns) == 0, \
            f"Found broken wikilink patterns: {broken_patterns}"
    
    @pytest.mark.integration
    def test_no_wikilink_hashes_in_urls(self, built_site):
        """Test that URLs don't contain Obsidian hash anchors"""
        pages_to_check = [
            "tutorials/index.html",
            "index.html",
            "blog/index.html"
        ]
        
        hash_pattern = re.compile(r'#[a-f0-9]{32}')
        problematic_links = []
        
        for page in pages_to_check:
            soup = self.read_html(built_site, page)
            links = soup.find_all('a', href=True)
            
            for link in links:
                href = link.get('href', '')
                if hash_pattern.search(href):
                    problematic_links.append({
                        'page': page,
                        'href': href,
                        'text': link.get_text(strip=True)
                    })
        
        assert len(problematic_links) == 0, \
            f"Found URLs with hash anchors: {problematic_links}"
    
    @pytest.mark.integration
    def test_code_blocks_have_syntax_highlighting(self, built_site):
        """Test that code blocks have proper syntax highlighting"""
        # Check customization guide which has code examples
        soup = self.read_html(built_site, "customization-guide/index.html")
        
        # Look for code blocks
        code_blocks = soup.find_all('pre')
        
        if len(code_blocks) > 0:
            # At least some code blocks should have highlighting
            highlighted_blocks = [
                block for block in code_blocks
                if 'highlight' in block.get('class', []) or
                   block.find('code', class_=re.compile(r'language-\w+')) or
                   block.find(class_=re.compile(r'highlight|codehilite'))
            ]
            
            assert len(highlighted_blocks) > 0, \
                f"No syntax highlighting found in {len(code_blocks)} code blocks"
    
    @pytest.mark.integration
    def test_all_internal_links_resolve(self, built_site):
        """Test that all internal links point to existing pages"""
        pages_to_check = [
            "index.html",
            "tutorials/index.html",
            "blog/index.html"
        ]
        
        broken_links = []
        
        for page in pages_to_check:
            soup = self.read_html(built_site, page)
            links = soup.find_all('a', href=True)
            
            for link in links:
                href = link.get('href', '')
                
                # Skip external links, anchors, and special links
                if (href.startswith('http') or 
                    href.startswith('#') or 
                    href.startswith('mailto:') or
                    href.startswith('javascript:') or
                    not href):
                    continue
                
                # Resolve relative links
                page_dir = Path(page).parent
                if href.startswith('../'):
                    # Handle parent directory references
                    resolved_path = (page_dir / href).resolve()
                    check_path = built_site / resolved_path.relative_to(built_site.parent)
                else:
                    check_path = built_site / page_dir / href
                
                # Remove anchors for file check
                if '#' in str(check_path):
                    check_path = Path(str(check_path).split('#')[0])
                
                # Check if file exists
                if not check_path.exists() and not (check_path.with_suffix('.html')).exists():
                    broken_links.append({
                        'page': page,
                        'href': href,
                        'text': link.get_text(strip=True),
                        'expected_path': str(check_path)
                    })
        
        assert len(broken_links) == 0, \
            f"Found broken internal links: {broken_links}"
    
    @pytest.mark.integration
    def test_blog_tags_link_resolves(self, built_site):
        """Test that blog tags link points to correct location"""
        soup = self.read_html(built_site, "blog/index.html")
        
        # Find the tags link
        tags_links = [
            link for link in soup.find_all('a', href=True)
            if 'tags' in link.get('href', '') and 'View all tags' in link.get_text()
        ]
        
        assert len(tags_links) > 0, "No 'View all tags' link found in blog index"
        
        # Check that it points to ../tags not just tags
        tags_href = tags_links[0].get('href', '')
        assert tags_href == '../tags/' or tags_href == '../tags/index.html', \
            f"Tags link should point to '../tags/' but points to '{tags_href}'"
    
    @pytest.mark.integration
    def test_no_mixed_link_syntax(self, built_site):
        """Test that no mixed Markdown/Wikilink syntax appears in output"""
        pages_to_check = [
            "tutorials/index.html",
            "blog/index.html",
            "index.html"
        ]
        
        mixed_syntax_pattern = re.compile(r'\[\[.*\]\]')
        problems = []
        
        for page in pages_to_check:
            soup = self.read_html(built_site, page)
            
            # Check link hrefs
            for link in soup.find_all('a', href=True):
                href = link.get('href', '')
                if mixed_syntax_pattern.search(href):
                    problems.append({
                        'page': page,
                        'element': 'href',
                        'value': href
                    })
            
            # Check visible text (shouldn't see raw wikilinks)
            page_text = soup.get_text()
            if mixed_syntax_pattern.search(page_text):
                # Find specific instances
                for match in mixed_syntax_pattern.finditer(page_text):
                    problems.append({
                        'page': page,
                        'element': 'text',
                        'value': match.group()
                    })
        
        assert len(problems) == 0, \
            f"Found mixed link syntax in rendered output: {problems}"
    
    @pytest.mark.integration 
    def test_footer_renders_correctly(self, built_site):
        """Test that custom footer renders without errors"""
        soup = self.read_html(built_site, "index.html")
        
        # Check for footer
        footer = soup.find('footer', class_='md-footer')
        assert footer is not None, "Footer not found"
        
        # Check for common footer elements
        footer_nav = footer.find(class_='md-footer__inner')
        assert footer_nav is not None, "Footer navigation not found"
    
    @pytest.mark.integration
    def test_navigation_links_valid(self, built_site):
        """Test that all navigation menu links are valid"""
        soup = self.read_html(built_site, "index.html")
        
        # Find navigation links
        nav = soup.find('nav', class_='md-tabs') or soup.find('nav', class_='md-nav--primary')
        assert nav is not None, "Navigation not found"
        
        nav_links = nav.find_all('a', href=True)
        broken_nav = []
        
        for link in nav_links:
            href = link.get('href', '')
            if href and not href.startswith('#') and not href.startswith('http'):
                # Check if target exists
                if href.endswith('/'):
                    check_path = built_site / href / 'index.html'
                else:
                    check_path = built_site / href
                
                if not check_path.exists():
                    broken_nav.append({
                        'href': href,
                        'text': link.get_text(strip=True)
                    })
        
        assert len(broken_nav) == 0, \
            f"Found broken navigation links: {broken_nav}"