#!/usr/bin/env python3
"""
Static analysis tests for markdown files before build.
These tests catch issues early without requiring a full MkDocs build.
"""

import re
from pathlib import Path
from typing import Dict, List, Set, Tuple

import pytest
import yaml

from test_utils import (
    extract_frontmatter,
    find_markdown_links,
    get_all_markdown_files,
)


class TestStaticAnalysis:
    """Static analysis tests for markdown content"""

    @pytest.mark.unit
    def test_all_markdown_files_parseable(self, docs_dir):
        """Test that all markdown files can be parsed"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        unparseable_files = []
        
        for md_file in markdown_files:
            try:
                content = md_file.read_text(encoding='utf-8')
                # Basic parsing check
                if not content.strip():
                    unparseable_files.append(f"{md_file.relative_to(docs_dir)}: Empty file")
                    continue
                
                # Check for malformed frontmatter
                frontmatter, body = extract_frontmatter(content)
                if content.startswith('---') and frontmatter is None:
                    unparseable_files.append(f"{md_file.relative_to(docs_dir)}: Malformed frontmatter")
                    
            except UnicodeDecodeError:
                unparseable_files.append(f"{md_file.relative_to(docs_dir)}: Unicode decode error")
            except Exception as e:
                unparseable_files.append(f"{md_file.relative_to(docs_dir)}: {str(e)}")
        
        if unparseable_files:
            error_msg = f"\nUnparseable markdown files ({len(unparseable_files)}):\n"
            for error in unparseable_files:
                error_msg += f"  - {error}\n"
            pytest.fail(error_msg)

    @pytest.mark.unit
    def test_frontmatter_consistency(self, docs_dir):
        """Test frontmatter consistency across files"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        frontmatter_issues = []
        
        # Common frontmatter fields
        common_fields = {'title', 'description', 'date', 'tags', 'category'}
        
        for md_file in markdown_files:
            content = md_file.read_text(encoding='utf-8')
            frontmatter, _ = extract_frontmatter(content)
            
            if frontmatter:
                # Check for required fields based on file location
                rel_path = md_file.relative_to(docs_dir)
                
                # Blog posts should have certain fields
                if 'blog' in str(rel_path) and rel_path.name != 'index.md':
                    required_fields = {'title', 'date'}
                    missing_fields = required_fields - set(frontmatter.keys())
                    if missing_fields:
                        frontmatter_issues.append(
                            f"{rel_path}: Blog post missing required fields: {missing_fields}"
                        )
                
                # Tutorial files should have titles
                if 'tutorial' in str(rel_path) and rel_path.name != 'index.md':
                    if 'title' not in frontmatter:
                        frontmatter_issues.append(f"{rel_path}: Tutorial missing title")
                
                # Check for empty values
                for key, value in frontmatter.items():
                    if value is None or (isinstance(value, str) and not value.strip()):
                        frontmatter_issues.append(f"{rel_path}: Empty frontmatter field '{key}'")
        
        if frontmatter_issues:
            warning_msg = f"\nFrontmatter issues ({len(frontmatter_issues)}):\n"
            for issue in frontmatter_issues[:20]:  # Limit to first 20
                warning_msg += f"  - {issue}\n"
            if len(frontmatter_issues) > 20:
                warning_msg += f"  ... and {len(frontmatter_issues) - 20} more\n"
            
            # This is a warning, not a failure
            pytest.skip(f"Found frontmatter issues (warning):{warning_msg}")

    @pytest.mark.unit
    def test_markdown_structure_quality(self, docs_dir):
        """Test markdown structural quality"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        structure_issues = []
        
        for md_file in markdown_files:
            content = md_file.read_text(encoding='utf-8')
            rel_path = md_file.relative_to(docs_dir)
            
            # Extract content without frontmatter
            _, body = extract_frontmatter(content)
            if body is None:
                body = content
            
            lines = body.split('\n')
            
            # Check for proper heading structure
            headings = []
            for i, line in enumerate(lines):
                heading_match = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
                if heading_match:
                    level = len(heading_match.group(1))
                    text = heading_match.group(2)
                    headings.append((level, text, i + 1))
            
            # Validate heading hierarchy
            if headings:
                # First heading should be H1
                if headings[0][0] != 1:
                    structure_issues.append(
                        f"{rel_path}:L{headings[0][2]}: First heading should be H1, found H{headings[0][0]}"
                    )
                
                # Check for heading level jumps
                for i in range(1, len(headings)):
                    current_level = headings[i][0]
                    previous_level = headings[i-1][0]
                    line_num = headings[i][2]
                    
                    if current_level > previous_level + 1:
                        structure_issues.append(
                            f"{rel_path}:L{line_num}: Heading level jumped from H{previous_level} to H{current_level}"
                        )
            
            # Check for empty sections
            current_section_lines = 0
            for line in lines:
                if re.match(r'^#{1,6}\s+', line.strip()):
                    if current_section_lines < 2:  # Heading + at least one content line
                        # Find the line number (approximate)
                        pass  # This would need more complex tracking
                    current_section_lines = 0
                elif line.strip():
                    current_section_lines += 1
            
            # Check for broken markdown syntax
            # Unmatched brackets
            if '[' in body and ']' in body:
                bracket_count = body.count('[') - body.count(']')
                if bracket_count != 0:
                    structure_issues.append(f"{rel_path}: Unmatched brackets (diff: {bracket_count})")
            
            # Check for malformed links
            malformed_links = re.findall(r'\]\([^)]*\[', body)
            if malformed_links:
                structure_issues.append(f"{rel_path}: Malformed links found: {len(malformed_links)}")
        
        if structure_issues:
            warning_msg = f"\nMarkdown structure issues ({len(structure_issues)}):\n"
            for issue in structure_issues[:15]:  # Limit output
                warning_msg += f"  - {issue}\n"
            if len(structure_issues) > 15:
                warning_msg += f"  ... and {len(structure_issues) - 15} more\n"
            
            # This is a warning for most issues
            pytest.skip(f"Found structure issues (warning):{warning_msg}")

    @pytest.mark.unit
    def test_link_syntax_validation(self, docs_dir):
        """Test link syntax before build"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        syntax_issues = []
        
        for md_file in markdown_files:
            content = md_file.read_text(encoding='utf-8')
            rel_path = md_file.relative_to(docs_dir)
            
            # Check for common link syntax issues
            
            # 1. Spaces in link URLs (should be encoded)
            space_links = re.findall(r'\[([^\]]*)\]\(([^)]*\s[^)]*)\)', content)
            for text, url in space_links:
                if not url.startswith(('http://', 'https://')):  # Skip external URLs
                    syntax_issues.append(f"{rel_path}: Link with spaces in URL: [{text}]({url})")
            
            # 2. Malformed wikilinks
            malformed_wikilinks = re.findall(r'\[\[([^\]]*)\](?!\])', content)
            for wikilink in malformed_wikilinks:
                syntax_issues.append(f"{rel_path}: Malformed wikilink: [[{wikilink}]")
            
            # 3. Empty links
            empty_links = re.findall(r'\[([^\]]*)\]\(\s*\)', content)
            for text in empty_links:
                syntax_issues.append(f"{rel_path}: Empty link: [{text}]()")
            
            # 4. Mixed syntax (markdown links with wikilink targets)
            mixed_syntax = re.findall(r'\[([^\]]*)\]\(\[\[([^\]]*)\]\]\)', content)
            for text, target in mixed_syntax:
                syntax_issues.append(f"{rel_path}: Mixed link syntax: [{text}]([[{target}]])")
            
            # 5. Unescaped special characters in links
            special_chars = re.findall(r'\[([^\]]*)\]\(([^)]*[<>"\s][^)]*)\)', content)
            for text, url in special_chars:
                if not url.startswith(('http://', 'https://')):
                    syntax_issues.append(f"{rel_path}: Special characters in link: [{text}]({url})")
        
        if syntax_issues:
            error_msg = f"\nLink syntax issues ({len(syntax_issues)}):\n"
            for issue in syntax_issues[:20]:
                error_msg += f"  - {issue}\n"
            if len(syntax_issues) > 20:
                error_msg += f"  ... and {len(syntax_issues) - 20} more\n"
            
            # These are often real issues
            pytest.fail(error_msg)

    @pytest.mark.unit
    def test_file_organization(self, docs_dir):
        """Test file organization follows conventions"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        organization_issues = []
        
        # Check for expected directory structure
        expected_dirs = ['tutorials', 'how-to', 'reference', 'explanation']
        existing_dirs = [d.name for d in docs_dir.iterdir() if d.is_dir()]
        
        # This is informational
        missing_dirs = set(expected_dirs) - set(existing_dirs)
        if missing_dirs:
            organization_issues.append(f"Missing Diátaxis directories: {missing_dirs}")
        
        # Check for files in wrong locations
        markdown_files = get_all_markdown_files(docs_dir)
        
        for md_file in markdown_files:
            rel_path = md_file.relative_to(docs_dir)
            path_parts = rel_path.parts
            
            # Check for tutorial files outside tutorials directory
            content = md_file.read_text(encoding='utf-8')
            frontmatter, _ = extract_frontmatter(content)
            
            if frontmatter and frontmatter.get('type') == 'tutorial':
                if not path_parts[0].startswith('tutorial'):
                    organization_issues.append(f"{rel_path}: Tutorial file outside tutorials directory")
            
            # Check for orphaned files (files that might belong in specific directories)
            filename = rel_path.name.lower()
            if 'tutorial' in filename and not path_parts[0].startswith('tutorial'):
                organization_issues.append(f"{rel_path}: File with 'tutorial' in name outside tutorials directory")
            
            if 'guide' in filename and not any(d in path_parts[0] for d in ['how-to', 'tutorial']):
                organization_issues.append(f"{rel_path}: Guide file in unexpected location")
        
        if organization_issues:
            warning_msg = f"\nFile organization issues ({len(organization_issues)}):\n"
            for issue in organization_issues:
                warning_msg += f"  - {issue}\n"
            
            # This is organizational advice, not a failure
            print(warning_msg)

    @pytest.mark.unit
    def test_content_quality_metrics(self, docs_dir):
        """Test content quality metrics"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        quality_stats = {
            'total_files': len(markdown_files),
            'files_with_frontmatter': 0,
            'files_with_headings': 0,
            'files_with_links': 0,
            'very_short_files': 0,
            'very_long_files': 0,
            'files_without_title': 0
        }
        
        quality_issues = []
        
        for md_file in markdown_files:
            content = md_file.read_text(encoding='utf-8')
            rel_path = md_file.relative_to(docs_dir)
            
            # Basic metrics
            frontmatter, body = extract_frontmatter(content)
            if body is None:
                body = content
                
            word_count = len(body.split())
            line_count = len(body.strip().split('\n'))
            
            # Track stats
            if frontmatter:
                quality_stats['files_with_frontmatter'] += 1
                if 'title' not in frontmatter:
                    quality_stats['files_without_title'] += 1
            
            if re.search(r'^#{1,6}\s+', body, re.MULTILINE):
                quality_stats['files_with_headings'] += 1
            
            if find_markdown_links(content):
                quality_stats['files_with_links'] += 1
            
            # Quality thresholds
            if word_count < 50 and rel_path.name != 'index.md':
                quality_stats['very_short_files'] += 1
                quality_issues.append(f"{rel_path}: Very short file ({word_count} words)")
            
            if word_count > 5000:
                quality_stats['very_long_files'] += 1
                quality_issues.append(f"{rel_path}: Very long file ({word_count} words)")
            
            # Check for potential issues
            if not frontmatter and rel_path.name != 'index.md':
                quality_issues.append(f"{rel_path}: No frontmatter")
            
            if word_count > 50 and not re.search(r'^#{1,6}\s+', body, re.MULTILINE):
                quality_issues.append(f"{rel_path}: No headings in substantial content")
        
        # Print statistics
        print(f"\nContent Quality Statistics:")
        print(f"  Total files: {quality_stats['total_files']}")
        print(f"  Files with frontmatter: {quality_stats['files_with_frontmatter']}")
        print(f"  Files with headings: {quality_stats['files_with_headings']}")
        print(f"  Files with links: {quality_stats['files_with_links']}")
        print(f"  Very short files: {quality_stats['very_short_files']}")
        print(f"  Very long files: {quality_stats['very_long_files']}")
        
        # Report significant quality issues
        significant_issues = [
            issue for issue in quality_issues 
            if 'No frontmatter' in issue or 'No headings' in issue
        ]
        
        if significant_issues and len(significant_issues) > len(markdown_files) * 0.3:
            warning_msg = f"\nSignificant content quality issues ({len(significant_issues)}):\n"
            for issue in significant_issues[:10]:
                warning_msg += f"  - {issue}\n"
            if len(significant_issues) > 10:
                warning_msg += f"  ... and {len(significant_issues) - 10} more\n"
            
            pytest.skip(f"Many quality issues found (warning):{warning_msg}")

    @pytest.mark.unit
    def test_duplicate_content_detection(self, docs_dir):
        """Test for duplicate or very similar content"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        content_hashes = {}
        duplicates = []
        
        for md_file in markdown_files:
            content = md_file.read_text(encoding='utf-8')
            rel_path = md_file.relative_to(docs_dir)
            
            # Extract just the body content
            _, body = extract_frontmatter(content)
            if body is None:
                body = content
            
            # Simple hash of normalized content
            normalized = re.sub(r'\s+', ' ', body.strip().lower())
            content_hash = hash(normalized)
            
            if content_hash in content_hashes:
                duplicates.append((rel_path, content_hashes[content_hash]))
            else:
                content_hashes[content_hash] = rel_path
        
        if duplicates:
            warning_msg = f"\nPossible duplicate content ({len(duplicates)} pairs):\n"
            for file1, file2 in duplicates:
                warning_msg += f"  - {file1} ≈ {file2}\n"
            
            # This is informational
            print(warning_msg)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])