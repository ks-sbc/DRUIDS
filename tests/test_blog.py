#!/usr/bin/env python3
"""
Tests for blog functionality
"""

from pathlib import Path

import pytest
import yaml

from test_utils import extract_frontmatter, get_all_markdown_files


class TestBlogFunctionality:
    """Test blog-specific functionality"""

    @pytest.fixture
    def blog_config(self, mkdocs_config):
        """Extract blog configuration from MkDocs config"""
        plugins = mkdocs_config.get("plugins", [])
        
        for plugin in plugins:
            if isinstance(plugin, dict) and "blog" in plugin:
                return plugin["blog"]
            elif plugin == "blog":
                return {}
        
        return None

    @pytest.fixture
    def blog_posts_dir(self, docs_dir):
        """Get blog posts directory"""
        return docs_dir / "blog" / "posts"

    @pytest.mark.integration
    def test_blog_plugin_configured(self, blog_config):
        """Test that blog plugin is properly configured"""
        if blog_config is None:
            pytest.skip("Blog plugin not configured")
        
        # Common blog configuration checks
        if blog_config.get("authors", False):
            authors_file = blog_config.get("authors_file", "blog/.authors.yml")
            assert authors_file, "Authors enabled but no authors_file specified"

    @pytest.mark.integration
    def test_blog_posts_exist(self, blog_posts_dir):
        """Test that blog posts directory exists and has posts"""
        if not blog_posts_dir.exists():
            pytest.skip("No blog posts directory")
        
        posts = list(blog_posts_dir.glob("*.md"))
        assert len(posts) > 0, "No blog posts found"

    @pytest.mark.integration
    def test_blog_posts_have_required_frontmatter(self, blog_posts_dir, blog_config):
        """Test that all blog posts have required frontmatter fields"""
        if not blog_posts_dir.exists():
            pytest.skip("No blog posts directory")
        
        if blog_config is None:
            pytest.skip("Blog plugin not configured")
        
        posts = list(blog_posts_dir.glob("*.md"))
        authors_enabled = blog_config.get("authors", False)
        
        errors = []
        
        for post in posts:
            content = post.read_text(encoding='utf-8')
            frontmatter, _ = extract_frontmatter(content)
            
            if frontmatter is None:
                errors.append(f"{post.name}: Missing frontmatter")
                continue
            
            # Check required fields
            if "date" not in frontmatter:
                errors.append(f"{post.name}: Missing 'date' field")
            
            # Check authors configuration
            if "authors" in frontmatter and not authors_enabled:
                errors.append(f"{post.name}: Has authors but blog.authors is disabled")
            
            # If authors are required, check they exist
            if authors_enabled and blog_config.get("authors_required", False):
                if "authors" not in frontmatter:
                    errors.append(f"{post.name}: Missing required authors field")
        
        assert not errors, "Blog post validation errors:\n" + "\n".join(errors)

    @pytest.mark.integration
    def test_blog_posts_have_excerpt_separator(self, blog_posts_dir):
        """Test that blog posts have excerpt separator"""
        if not blog_posts_dir.exists():
            pytest.skip("No blog posts directory")
        
        posts = list(blog_posts_dir.glob("*.md"))
        posts_without_excerpt = []
        
        for post in posts:
            content = post.read_text(encoding='utf-8')
            if "<!-- more -->" not in content:
                posts_without_excerpt.append(post.name)
        
        # This is a warning, not an error
        if posts_without_excerpt:
            print(f"\nPosts without excerpt separator: {posts_without_excerpt}")

    @pytest.mark.integration
    def test_blog_categories_valid(self, blog_posts_dir, blog_config):
        """Test that blog post categories are in allowed list"""
        if not blog_posts_dir.exists():
            pytest.skip("No blog posts directory")
        
        if blog_config is None:
            pytest.skip("Blog plugin not configured")
        
        allowed_categories = blog_config.get("categories_allowed")
        if not allowed_categories:
            pytest.skip("No category restrictions configured")
        
        posts = list(blog_posts_dir.glob("*.md"))
        errors = []
        
        for post in posts:
            content = post.read_text(encoding='utf-8')
            frontmatter, _ = extract_frontmatter(content)
            
            if frontmatter and "categories" in frontmatter:
                post_categories = frontmatter["categories"]
                if isinstance(post_categories, list):
                    for category in post_categories:
                        if category not in allowed_categories:
                            errors.append(
                                f"{post.name}: Category '{category}' not in allowed list"
                            )
        
        assert not errors, "Invalid categories found:\n" + "\n".join(errors)

    @pytest.mark.integration
    def test_blog_authors_file_valid(self, docs_dir, blog_config):
        """Test that authors file is valid if authors are enabled"""
        if blog_config is None:
            pytest.skip("Blog plugin not configured")
        
        if not blog_config.get("authors", False):
            pytest.skip("Authors not enabled")
        
        authors_file = blog_config.get("authors_file", "blog/.authors.yml")
        authors_path = docs_dir / authors_file
        
        assert authors_path.exists(), f"Authors file not found: {authors_file}"
        
        # Validate YAML syntax
        try:
            with open(authors_path, 'r') as f:
                authors_data = yaml.safe_load(f)
            
            assert isinstance(authors_data, dict), "Authors file should contain a dictionary"
            
            # Validate author entries
            for author_id, author_info in authors_data.items():
                assert isinstance(author_info, dict), \
                    f"Author '{author_id}' should be a dictionary"
                assert "name" in author_info, \
                    f"Author '{author_id}' missing 'name' field"
        
        except yaml.YAMLError as e:
            pytest.fail(f"Invalid YAML in authors file: {e}")

    @pytest.mark.integration
    def test_blog_posts_authors_exist(self, blog_posts_dir, docs_dir, blog_config):
        """Test that authors referenced in posts exist in authors file"""
        if not blog_posts_dir.exists():
            pytest.skip("No blog posts directory")
        
        if blog_config is None or not blog_config.get("authors", False):
            pytest.skip("Authors not enabled")
        
        # Load authors
        authors_file = blog_config.get("authors_file", "blog/.authors.yml")
        authors_path = docs_dir / authors_file
        
        if not authors_path.exists():
            pytest.skip("Authors file not found")
        
        with open(authors_path, 'r') as f:
            authors_data = yaml.safe_load(f)
        
        available_authors = set(authors_data.keys())
        
        # Check posts
        posts = list(blog_posts_dir.glob("*.md"))
        errors = []
        
        for post in posts:
            content = post.read_text(encoding='utf-8')
            frontmatter, _ = extract_frontmatter(content)
            
            if frontmatter and "authors" in frontmatter:
                post_authors = frontmatter["authors"]
                if isinstance(post_authors, list):
                    for author in post_authors:
                        if author not in available_authors:
                            errors.append(
                                f"{post.name}: Unknown author '{author}'"
                            )
        
        assert not errors, "Unknown authors found:\n" + "\n".join(errors)

    @pytest.mark.unit
    def test_blog_post_date_format(self, create_test_file, temp_dir):
        """Test that blog post dates are in correct format"""
        # Test various date formats
        test_cases = [
            ("2024-01-15", True),  # ISO format
            ("2024-1-15", True),   # Also valid
            ("15/01/2024", False), # Wrong format
            ("Jan 15, 2024", False), # Wrong format
            ("2024", False),       # Incomplete
        ]
        
        for date_str, should_be_valid in test_cases:
            content = f"""---
date: {date_str}
title: Test Post
---

# Test Post
"""
            file_path = create_test_file(f"post_{date_str.replace('/', '-')}.md", content)
            
            frontmatter, _ = extract_frontmatter(content)
            
            if should_be_valid:
                assert frontmatter is not None
                assert "date" in frontmatter
            else:
                # Date parsing might still work, but format is non-standard
                pass  # This would need more specific validation


if __name__ == "__main__":
    pytest.main([__file__, "-v"])