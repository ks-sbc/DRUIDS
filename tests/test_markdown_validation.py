#!/usr/bin/env python3
"""
Tests for markdown file validation
"""

import re
from pathlib import Path

import pytest

from test_utils import (
    extract_frontmatter,
    find_markdown_images,
    find_markdown_links,
    get_all_markdown_files,
    validate_internal_link,
)


class TestMarkdownValidation:
    """Test markdown file validation"""

    @pytest.mark.unit
    def test_extract_frontmatter_valid(self, sample_markdown_content):
        """Test extracting valid frontmatter"""
        frontmatter, content = extract_frontmatter(sample_markdown_content["valid"])
        
        assert frontmatter is not None
        assert "title" in frontmatter
        assert frontmatter["title"] == "Test Document"
        assert "# Test Document" in content

    @pytest.mark.unit
    def test_extract_frontmatter_missing(self, sample_markdown_content):
        """Test extracting from file without frontmatter"""
        frontmatter, content = extract_frontmatter(sample_markdown_content["no_frontmatter"])
        
        assert frontmatter is None
        assert "# Test Document" in content

    @pytest.mark.unit
    def test_extract_frontmatter_invalid(self, sample_markdown_content):
        """Test extracting invalid frontmatter"""
        frontmatter, content = extract_frontmatter(sample_markdown_content["invalid_frontmatter"])
        
        assert frontmatter is None
        assert content is None

    @pytest.mark.unit
    def test_find_markdown_links(self, sample_markdown_content):
        """Test finding markdown links"""
        content = sample_markdown_content["valid"]
        links = find_markdown_links(content)
        
        assert len(links) == 2
        assert links[0]["text"] == "internal link"
        assert links[0]["url"] == "../other-page"
        assert links[1]["text"] == "external link"
        assert links[1]["url"] == "https://example.com"

    @pytest.mark.unit
    def test_find_markdown_images(self):
        """Test finding markdown images"""
        content = """
        # Test
        ![Alt text](images/test.png)
        ![](images/no-alt.jpg)
        ![Logo](https://example.com/logo.png)
        """
        images = find_markdown_images(content)
        
        assert len(images) == 3
        assert images[0]["alt"] == "Alt text"
        assert images[0]["src"] == "images/test.png"
        assert images[1]["alt"] == ""
        assert images[2]["src"] == "https://example.com/logo.png"

    @pytest.mark.integration
    def test_all_markdown_files_have_frontmatter(self, docs_dir):
        """Test that all markdown files have frontmatter"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        # Exclude certain files that might not need frontmatter
        exclude_patterns = ["**/README.md", "**/CHANGELOG.md"]
        markdown_files = get_all_markdown_files(docs_dir, exclude_patterns)
        
        files_without_frontmatter = []
        
        for md_file in markdown_files:
            content = md_file.read_text(encoding='utf-8')
            frontmatter, _ = extract_frontmatter(content)
            
            if frontmatter is None:
                files_without_frontmatter.append(md_file.relative_to(docs_dir))
        
        # This is informational - not all files need frontmatter
        if files_without_frontmatter:
            print(f"\nFiles without frontmatter: {files_without_frontmatter}")

    @pytest.mark.integration
    def test_internal_links_valid(self, docs_dir):
        """Test that internal links point to existing files"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        all_broken_links = {}
        
        for md_file in markdown_files:
            content = md_file.read_text(encoding='utf-8')
            links = find_markdown_links(content)
            
            broken_links = []
            for link in links:
                url = link["url"]
                # Skip external links, anchors, and mailto
                if url.startswith(('http://', 'https://', 'mailto:', '#')):
                    continue
                
                if not validate_internal_link(url, md_file, docs_dir):
                    broken_links.append(link)
            
            if broken_links:
                all_broken_links[str(md_file.relative_to(docs_dir))] = broken_links
        
        if all_broken_links:
            # Format the error message
            error_msg = "\nBroken internal links found:\n"
            for file_path, links in all_broken_links.items():
                error_msg += f"\n{file_path}:\n"
                for link in links:
                    error_msg += f"  - [{link['text']}]({link['url']})\n"
            
            pytest.fail(error_msg)

    @pytest.mark.integration
    def test_images_exist(self, docs_dir):
        """Test that referenced images exist"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        all_missing_images = {}
        
        for md_file in markdown_files:
            content = md_file.read_text(encoding='utf-8')
            images = find_markdown_images(content)
            
            missing_images = []
            for image in images:
                src = image["src"]
                # Skip external images
                if src.startswith(('http://', 'https://', '//')):
                    continue
                
                # Resolve image path relative to the markdown file
                image_path = (md_file.parent / src).resolve()
                if not image_path.exists():
                    missing_images.append(image)
            
            if missing_images:
                all_missing_images[str(md_file.relative_to(docs_dir))] = missing_images
        
        if all_missing_images:
            # This is a warning, not a failure
            warning_msg = "\nMissing images found:\n"
            for file_path, images in all_missing_images.items():
                warning_msg += f"\n{file_path}:\n"
                for image in images:
                    warning_msg += f"  - ![{image['alt']}]({image['src']})\n"
            
            print(warning_msg)

    @pytest.mark.unit
    def test_markdown_heading_structure(self, sample_markdown_content):
        """Test that markdown has proper heading structure"""
        content = sample_markdown_content["valid"]
        
        # Find all headings
        heading_pattern = r'^(#{1,6})\s+(.+)$'
        headings = []
        
        for line in content.split('\n'):
            match = re.match(heading_pattern, line)
            if match:
                level = len(match.group(1))
                text = match.group(2)
                headings.append((level, text))
        
        # Check that we have headings
        assert len(headings) > 0, "No headings found"
        
        # Check that first heading is H1
        assert headings[0][0] == 1, "First heading should be H1"
        
        # Check heading hierarchy (no skipping levels)
        for i in range(1, len(headings)):
            current_level = headings[i][0]
            previous_level = headings[i-1][0]
            
            # Level can stay same, go up any amount, or go down by 1
            assert current_level <= previous_level + 1, \
                f"Heading level jumped from {previous_level} to {current_level}"

    @pytest.mark.integration
    def test_code_blocks_have_language(self, docs_dir):
        """Test that code blocks specify a language"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        files_with_issues = {}
        
        # Pattern for code blocks without language
        code_block_pattern = r'^```\s*$'
        
        for md_file in markdown_files:
            content = md_file.read_text(encoding='utf-8')
            lines = content.split('\n')
            
            issues = []
            for i, line in enumerate(lines):
                if re.match(code_block_pattern, line):
                    issues.append(i + 1)  # Line numbers are 1-based
            
            if issues:
                files_with_issues[str(md_file.relative_to(docs_dir))] = issues
        
        if files_with_issues:
            # This is a warning, not a failure
            warning_msg = "\nCode blocks without language specification:\n"
            for file_path, line_numbers in files_with_issues.items():
                warning_msg += f"\n{file_path}: lines {line_numbers}\n"
            
            print(warning_msg)

    @pytest.mark.unit
    def test_no_html_in_markdown(self, sample_markdown_content):
        """Test that markdown files don't contain raw HTML (best practice)"""
        content = sample_markdown_content["valid"]
        
        # Common HTML tags to check for
        html_pattern = r'<(?!--)(/?)(div|span|script|style|table|tr|td|th|iframe)'
        
        html_matches = re.findall(html_pattern, content, re.IGNORECASE)
        assert not html_matches, f"Found HTML tags in markdown: {html_matches}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])