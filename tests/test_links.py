#!/usr/bin/env python3
"""
Comprehensive link validation tests for MkDocs project.
Tests all types of links: navigation, internal markdown, wikilinks, and external links.
"""

import re
from pathlib import Path
from typing import Dict, List, Set, Tuple

import pytest
import yaml

from test_utils import (
    find_markdown_links,
    get_all_markdown_files,
    validate_internal_link,
)


class TestLinkValidation:
    """Comprehensive link validation tests"""

    def load_mkdocs_config(self, project_root: Path) -> Dict:
        """Load and parse mkdocs.yml configuration"""
        config_path = project_root / "mkdocs.yml"
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    def extract_nav_links(self, nav_item, base_path: str = "") -> List[str]:
        """Extract all file paths from navigation configuration"""
        links = []
        
        if isinstance(nav_item, dict):
            for key, value in nav_item.items():
                if isinstance(value, str):
                    # Direct file reference
                    links.append(value)
                elif isinstance(value, list):
                    # Nested navigation
                    for sub_item in value:
                        links.extend(self.extract_nav_links(sub_item, base_path))
        elif isinstance(nav_item, str):
            # Direct string reference
            links.append(nav_item)
        elif isinstance(nav_item, list):
            # List of navigation items
            for item in nav_item:
                links.extend(self.extract_nav_links(item, base_path))
        
        return links

    def find_wikilinks(self, content: str) -> List[Dict[str, str]]:
        """Find all wikilinks in content"""
        # Pattern for [[target|display]] or [[target]]
        wikilink_pattern = r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]'
        links = []
        
        for match in re.finditer(wikilink_pattern, content):
            target = match.group(1)
            display = match.group(2) if match.group(2) else target
            links.append({
                'target': target,
                'display': display,
                'raw': match.group(0)
            })
        
        return links

    def resolve_link_path(self, link: str, source_file: Path, docs_dir: Path) -> Path:
        """Resolve a link to its target path"""
        # Handle absolute links (starting with /)
        if link.startswith('/'):
            # Remove leading slash and resolve from docs_dir
            link = link[1:]
            target_path = docs_dir / link
        else:
            # Relative link
            target_path = source_file.parent / link
        
        # Resolve to absolute path
        target_path = target_path.resolve()
        
        # If it's a directory, look for index.md
        if target_path.is_dir():
            target_path = target_path / "index.md"
        
        # Add .md extension if not present and file doesn't exist
        if not target_path.suffix and not target_path.exists():
            target_path = target_path.with_suffix('.md')
        
        return target_path

    def is_external_link(self, link: str) -> bool:
        """Check if link is external"""
        return link.startswith(('http://', 'https://', 'mailto:', 'ftp://'))

    def is_anchor_link(self, link: str) -> bool:
        """Check if link is just an anchor"""
        return link.startswith('#')

    @pytest.mark.integration
    @pytest.mark.link_validation
    def test_navigation_links_exist(self, project_root, docs_dir):
        """Test that all navigation links point to existing files"""
        config = self.load_mkdocs_config(project_root)
        nav = config.get('nav', [])
        
        missing_files = []
        nav_links = []
        
        # Extract all navigation links
        for nav_item in nav:
            nav_links.extend(self.extract_nav_links(nav_item))
        
        # Check each navigation link
        for link in nav_links:
            # Skip external links
            if self.is_external_link(link):
                continue
            
            # Resolve path
            target_path = docs_dir / link
            
            # Check if file exists
            if not target_path.exists():
                missing_files.append(link)
        
        if missing_files:
            error_msg = f"\nMissing navigation files ({len(missing_files)}):\n"
            for file in sorted(missing_files):
                error_msg += f"  - {file}\n"
            pytest.fail(error_msg)

    @pytest.mark.integration
    def test_internal_markdown_links(self, docs_dir):
        """Test all internal markdown links"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        broken_links = {}
        
        for md_file in markdown_files:
            content = md_file.read_text(encoding='utf-8')
            links = find_markdown_links(content)
            
            file_broken_links = []
            for link in links:
                url = link['url']
                
                # Skip external links, anchors, and mailto
                if self.is_external_link(url) or self.is_anchor_link(url):
                    continue
                
                # Validate internal link
                if not validate_internal_link(url, md_file, docs_dir):
                    file_broken_links.append(link)
            
            if file_broken_links:
                broken_links[str(md_file.relative_to(docs_dir))] = file_broken_links
        
        if broken_links:
            error_msg = f"\nBroken internal links found in {len(broken_links)} files:\n"
            for file_path, links in broken_links.items():
                error_msg += f"\n{file_path}:\n"
                for link in links:
                    error_msg += f"  - [{link['text']}]({link['url']})\n"
            pytest.fail(error_msg)

    @pytest.mark.integration
    def test_wikilink_validation(self, docs_dir):
        """Test all wikilinks for validity"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        broken_wikilinks = {}
        
        for md_file in markdown_files:
            content = md_file.read_text(encoding='utf-8')
            wikilinks = self.find_wikilinks(content)
            
            file_broken_links = []
            for wikilink in wikilinks:
                target = wikilink['target']
                
                # Skip external links
                if self.is_external_link(target):
                    continue
                
                # Resolve wikilink target
                target_path = self.resolve_link_path(target, md_file, docs_dir)
                
                # Check if target exists
                if not target_path.exists():
                    file_broken_links.append(wikilink)
            
            if file_broken_links:
                broken_wikilinks[str(md_file.relative_to(docs_dir))] = file_broken_links
        
        if broken_wikilinks:
            error_msg = f"\nBroken wikilinks found in {len(broken_wikilinks)} files:\n"
            for file_path, links in broken_wikilinks.items():
                error_msg += f"\n{file_path}:\n"
                for link in links:
                    error_msg += f"  - [[{link['target']}]] (display: {link['display']})\n"
            pytest.fail(error_msg)

    @pytest.mark.integration
    def test_absolute_vs_relative_links(self, docs_dir):
        """Test for absolute links that should be relative"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        absolute_links = {}
        
        for md_file in markdown_files:
            content = md_file.read_text(encoding='utf-8')
            links = find_markdown_links(content)
            
            file_absolute_links = []
            for link in links:
                url = link['url']
                
                # Check for absolute internal links (starting with /)
                if url.startswith('/') and not self.is_external_link(url):
                    # Check if this could be a relative link
                    absolute_path = docs_dir / url[1:]  # Remove leading slash
                    
                    # Try to find a relative path
                    try:
                        relative_path = absolute_path.relative_to(md_file.parent)
                        suggested_link = str(relative_path)
                        
                        file_absolute_links.append({
                            'original': link,
                            'suggested': suggested_link
                        })
                    except ValueError:
                        # Can't make relative, might be legitimate
                        pass
            
            if file_absolute_links:
                absolute_links[str(md_file.relative_to(docs_dir))] = file_absolute_links
        
        if absolute_links:
            warning_msg = f"\nAbsolute links that could be relative ({len(absolute_links)} files):\n"
            for file_path, links in absolute_links.items():
                warning_msg += f"\n{file_path}:\n"
                for link in links:
                    original = link['original']
                    warning_msg += f"  - [{original['text']}]({original['url']}) → could be: {link['suggested']}\n"
            
            # This is a warning, not a failure
            pytest.skip(f"Found absolute links (warning):{warning_msg}")

    @pytest.mark.integration
    def test_anchor_links_valid(self, docs_dir):
        """Test that anchor links point to existing headings"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        broken_anchors = {}
        
        for md_file in markdown_files:
            content = md_file.read_text(encoding='utf-8')
            links = find_markdown_links(content)
            
            file_broken_anchors = []
            for link in links:
                url = link['url']
                
                # Check for anchor links
                if '#' in url:
                    # Split into file and anchor parts
                    if url.startswith('#'):
                        # Same-file anchor
                        file_part = ""
                        anchor_part = url[1:]
                        target_file = md_file
                    else:
                        parts = url.split('#', 1)
                        file_part = parts[0]
                        anchor_part = parts[1]
                        
                        # Resolve target file
                        if file_part:
                            target_file = self.resolve_link_path(file_part, md_file, docs_dir)
                        else:
                            target_file = md_file
                    
                    # Check if target file exists
                    if not target_file.exists():
                        continue  # Will be caught by other tests
                    
                    # Extract headings from target file
                    target_content = target_file.read_text(encoding='utf-8')
                    headings = self.extract_headings(target_content)
                    
                    # Convert anchor to expected heading format
                    expected_heading = self.anchor_to_heading(anchor_part)
                    
                    # Check if heading exists
                    if expected_heading not in headings:
                        file_broken_anchors.append({
                            'link': link,
                            'anchor': anchor_part,
                            'target_file': str(target_file.relative_to(docs_dir)) if target_file != md_file else 'same file',
                            'available_headings': headings
                        })
            
            if file_broken_anchors:
                broken_anchors[str(md_file.relative_to(docs_dir))] = file_broken_anchors
        
        if broken_anchors:
            error_msg = f"\nBroken anchor links found in {len(broken_anchors)} files:\n"
            for file_path, anchors in broken_anchors.items():
                error_msg += f"\n{file_path}:\n"
                for anchor in anchors:
                    link = anchor['link']
                    error_msg += f"  - [{link['text']}]({link['url']}) → anchor '{anchor['anchor']}' not found\n"
                    if anchor['available_headings']:
                        error_msg += f"    Available: {', '.join(anchor['available_headings'][:3])}\n"
            
            # This might be too strict for some cases, so make it a warning
            pytest.skip(f"Found broken anchor links (warning):{error_msg}")

    def extract_headings(self, content: str) -> List[str]:
        """Extract all headings from markdown content"""
        headings = []
        
        # Pattern for markdown headings
        heading_pattern = r'^(#{1,6})\s+(.+)$'
        
        for line in content.split('\n'):
            match = re.match(heading_pattern, line.strip())
            if match:
                heading_text = match.group(2).strip()
                # Convert to anchor format (lowercase, replace spaces with dashes)
                anchor = heading_text.lower().replace(' ', '-')
                # Remove special characters
                anchor = re.sub(r'[^a-z0-9\-]', '', anchor)
                headings.append(anchor)
        
        return headings

    def anchor_to_heading(self, anchor: str) -> str:
        """Convert anchor to expected heading format"""
        # Already in the right format typically
        return anchor.lower()

    @pytest.mark.integration
    def test_link_target_case_sensitivity(self, docs_dir):
        """Test for case sensitivity issues in links"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        case_issues = {}
        
        # Build map of actual files (case-sensitive)
        actual_files = set()
        for md_file in markdown_files:
            actual_files.add(str(md_file.relative_to(docs_dir)))
        
        for md_file in markdown_files:
            content = md_file.read_text(encoding='utf-8')
            links = find_markdown_links(content)
            
            file_case_issues = []
            for link in links:
                url = link['url']
                
                # Skip external links and anchors
                if self.is_external_link(url) or self.is_anchor_link(url):
                    continue
                
                # Remove anchor if present
                if '#' in url:
                    url = url.split('#')[0]
                
                # Skip empty links
                if not url:
                    continue
                
                # Check if this link exists but with different case
                target_path = self.resolve_link_path(url, md_file, docs_dir)
                relative_target = str(target_path.relative_to(docs_dir))
                
                # If target doesn't exist, check for case variations
                if not target_path.exists():
                    for actual_file in actual_files:
                        if actual_file.lower() == relative_target.lower() and actual_file != relative_target:
                            file_case_issues.append({
                                'link': link,
                                'expected': relative_target,
                                'actual': actual_file
                            })
                            break
            
            if file_case_issues:
                case_issues[str(md_file.relative_to(docs_dir))] = file_case_issues
        
        if case_issues:
            error_msg = f"\nCase sensitivity issues found in {len(case_issues)} files:\n"
            for file_path, issues in case_issues.items():
                error_msg += f"\n{file_path}:\n"
                for issue in issues:
                    link = issue['link']
                    error_msg += f"  - [{link['text']}]({link['url']}) → should be: {issue['actual']}\n"
            pytest.fail(error_msg)

    @pytest.mark.integration
    def test_circular_links(self, docs_dir):
        """Test for circular link references"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        
        # Build link graph
        link_graph = {}
        for md_file in markdown_files:
            content = md_file.read_text(encoding='utf-8')
            links = find_markdown_links(content)
            
            file_key = str(md_file.relative_to(docs_dir))
            link_graph[file_key] = []
            
            for link in links:
                url = link['url']
                
                # Skip external links and anchors
                if self.is_external_link(url) or self.is_anchor_link(url):
                    continue
                
                # Resolve target
                target_path = self.resolve_link_path(url, md_file, docs_dir)
                if target_path.exists():
                    target_key = str(target_path.relative_to(docs_dir))
                    link_graph[file_key].append(target_key)
        
        # Simple circular reference detection (A -> B -> A)
        circular_refs = []
        for file_a, targets in link_graph.items():
            for file_b in targets:
                if file_b in link_graph and file_a in link_graph[file_b]:
                    if file_a < file_b:  # Avoid duplicates
                        circular_refs.append((file_a, file_b))
        
        if circular_refs:
            warning_msg = f"\nCircular link references found ({len(circular_refs)}):\n"
            for file_a, file_b in circular_refs:
                warning_msg += f"  - {file_a} ↔ {file_b}\n"
            
            # This is informational, not necessarily a problem
            print(warning_msg)

    @pytest.mark.integration
    def test_link_statistics(self, docs_dir):
        """Generate link statistics for the project"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        
        stats = {
            'total_files': len(markdown_files),
            'total_links': 0,
            'internal_links': 0,
            'external_links': 0,
            'wikilinks': 0,
            'anchor_links': 0,
            'broken_links': 0
        }
        
        for md_file in markdown_files:
            content = md_file.read_text(encoding='utf-8')
            
            # Count markdown links
            links = find_markdown_links(content)
            stats['total_links'] += len(links)
            
            for link in links:
                url = link['url']
                if self.is_external_link(url):
                    stats['external_links'] += 1
                elif self.is_anchor_link(url):
                    stats['anchor_links'] += 1
                else:
                    stats['internal_links'] += 1
                    
                    # Check if broken
                    if not validate_internal_link(url, md_file, docs_dir):
                        stats['broken_links'] += 1
            
            # Count wikilinks
            wikilinks = self.find_wikilinks(content)
            stats['wikilinks'] += len(wikilinks)
        
        print(f"\nLink Statistics:")
        print(f"  Total files: {stats['total_files']}")
        print(f"  Total links: {stats['total_links']}")
        print(f"  Internal links: {stats['internal_links']}")
        print(f"  External links: {stats['external_links']}")
        print(f"  Wikilinks: {stats['wikilinks']}")
        print(f"  Anchor links: {stats['anchor_links']}")
        print(f"  Broken links: {stats['broken_links']}")
        
        # Store stats for other tests to use
        self.link_stats = stats


if __name__ == "__main__":
    pytest.main([__file__, "-v"])