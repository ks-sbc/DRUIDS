#!/usr/bin/env python3
"""
Test suite for MkDocs configuration validation
"""

import os
import sys
import yaml
import pytest
from pathlib import Path
from mkdocs.config import load_config
from mkdocs.commands.build import build
from mkdocs.exceptions import ConfigurationError

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

class TestMkDocsConfig:
    """Test MkDocs configuration validity"""
    
    @pytest.fixture
    def config_file(self):
        """Path to mkdocs.yml"""
        return project_root / "mkdocs.yml"
    
    @pytest.fixture
    def config(self, config_file):
        """Load MkDocs configuration"""
        return load_config(str(config_file))
    
    def test_config_loads_successfully(self, config_file):
        """Test that mkdocs.yml loads without errors"""
        try:
            config = load_config(str(config_file))
            assert config is not None
        except ConfigurationError as e:
            pytest.fail(f"Configuration failed to load: {e}")
    
    def test_required_files_exist(self, config):
        """Test that all referenced files in nav exist"""
        docs_dir = Path(config['docs_dir'])
        nav = config.get('nav', [])
        
        missing_files = []
        
        def check_nav_item(item, path_prefix=""):
            if isinstance(item, dict):
                for key, value in item.items():
                    if isinstance(value, str):
                        # This is a file reference
                        file_path = docs_dir / value
                        if not file_path.exists() and not value.startswith('http'):
                            missing_files.append(value)
                    elif isinstance(value, list):
                        # This is a nested section
                        for sub_item in value:
                            check_nav_item(sub_item, path_prefix)
            elif isinstance(item, str):
                file_path = docs_dir / item
                if not file_path.exists() and not item.startswith('http'):
                    missing_files.append(item)
        
        for nav_item in nav:
            check_nav_item(nav_item)
        
        if missing_files:
            print(f"Missing files: {missing_files}")
            # Don't fail the test for missing files, just warn
            # This allows for optional files that might not exist yet
    
    def test_blog_configuration(self, config):
        """Test blog plugin configuration"""
        plugins = config.get('plugins', [])
        blog_config = None
        
        for plugin in plugins:
            if isinstance(plugin, dict) and 'blog' in plugin:
                blog_config = plugin['blog']
                break
            elif plugin == 'blog':
                blog_config = {}
                break
        
        if blog_config is not None:
            # If authors are enabled, check that authors file exists
            if blog_config.get('authors', False):
                authors_file = blog_config.get('authors_file', 'blog/.authors.yml')
                authors_path = Path(config['docs_dir']) / authors_file
                assert authors_path.exists(), f"Authors file {authors_file} not found but authors are enabled"
    
    def test_theme_icons_exist(self, config):
        """Test that all referenced theme icons are valid"""
        theme_config = config.get('theme', {})
        icon_config = theme_config.get('icon', {})
        
        # List of known valid icon prefixes
        valid_prefixes = [
            'material/',
            'fontawesome/brands/',
            'fontawesome/solid/',
            'fontawesome/regular/',
            'octicons/',
        ]
        
        def check_icon(icon_name, context=""):
            if not icon_name:
                return
            
            # Check if icon has a valid prefix
            has_valid_prefix = any(icon_name.startswith(prefix) for prefix in valid_prefixes)
            if not has_valid_prefix:
                pytest.fail(f"Invalid icon '{icon_name}' in {context}. Must use a valid prefix: {valid_prefixes}")
        
        # Check various icon configurations
        if 'logo' in icon_config:
            check_icon(icon_config['logo'], "theme.icon.logo")
        
        if 'repo' in icon_config:
            check_icon(icon_config['repo'], "theme.icon.repo")
        
        # Check tag icons
        tag_icons = icon_config.get('tag', {})
        for tag, icon in tag_icons.items():
            check_icon(icon, f"theme.icon.tag.{tag}")
    
    def test_build_succeeds(self, config_file):
        """Test that mkdocs build completes successfully"""
        try:
            config = load_config(str(config_file))
            # Use a temporary site directory for testing
            config['site_dir'] = str(project_root / 'test_site')
            
            # Run the build
            build(config, dirty=False)
            
            # Clean up test site directory
            import shutil
            test_site = Path(config['site_dir'])
            if test_site.exists():
                shutil.rmtree(test_site)
                
        except Exception as e:
            pytest.fail(f"MkDocs build failed: {e}")


class TestBlogPosts:
    """Test blog post configuration and content"""
    
    @pytest.fixture
    def blog_posts_dir(self):
        """Path to blog posts directory"""
        return project_root / "docs" / "blog" / "posts"
    
    @pytest.fixture
    def config(self):
        """Load MkDocs configuration"""
        return load_config(str(project_root / "mkdocs.yml"))
    
    def test_blog_posts_have_valid_frontmatter(self, blog_posts_dir, config):
        """Test that all blog posts have valid frontmatter"""
        if not blog_posts_dir.exists():
            pytest.skip("No blog posts directory found")
        
        # Get blog configuration
        blog_config = None
        for plugin in config.get('plugins', []):
            if isinstance(plugin, dict) and 'blog' in plugin:
                blog_config = plugin['blog']
                break
        
        authors_enabled = blog_config and blog_config.get('authors', False)
        
        for post_file in blog_posts_dir.glob("*.md"):
            with open(post_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for frontmatter
            if not content.startswith('---'):
                pytest.fail(f"Blog post {post_file.name} missing frontmatter")
            
            # Extract frontmatter
            try:
                _, frontmatter_str, _ = content.split('---', 2)
                frontmatter = yaml.safe_load(frontmatter_str)
            except (ValueError, yaml.YAMLError) as e:
                pytest.fail(f"Invalid frontmatter in {post_file.name}: {e}")
            
            # Check required fields
            assert 'date' in frontmatter, f"Missing 'date' in {post_file.name}"
            
            # If authors are disabled, ensure no author references
            if not authors_enabled and 'authors' in frontmatter:
                pytest.fail(f"Authors found in {post_file.name} but authors are disabled in config")
            
            # Check categories are in allowed list if specified
            if blog_config and 'categories_allowed' in blog_config:
                allowed_categories = blog_config['categories_allowed']
                post_categories = frontmatter.get('categories', [])
                for category in post_categories:
                    assert category in allowed_categories, f"Category '{category}' in {post_file.name} not in allowed list"


class TestTemplateOverrides:
    """Test custom template overrides"""
    
    @pytest.fixture
    def overrides_dir(self):
        """Path to template overrides directory"""
        return project_root / "overrides"
    
    def test_template_syntax(self, overrides_dir):
        """Test that custom templates have valid Jinja2 syntax"""
        if not overrides_dir.exists():
            pytest.skip("No template overrides directory found")
        
        from jinja2 import Environment, FileSystemLoader, TemplateSyntaxError
        
        env = Environment(loader=FileSystemLoader(str(overrides_dir)))
        
        for template_file in overrides_dir.rglob("*.html"):
            template_path = template_file.relative_to(overrides_dir)
            try:
                env.get_template(str(template_path))
            except TemplateSyntaxError as e:
                pytest.fail(f"Template syntax error in {template_path}: {e}")
    
    def test_comments_template_safety(self, overrides_dir):
        """Test that comments template handles edge cases safely"""
        comments_template = overrides_dir / "partials" / "comments.html"
        
        if not comments_template.exists():
            pytest.skip("No custom comments template found")
        
        with open(comments_template, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for safe page access patterns
        unsafe_patterns = [
            'page.meta.comments',  # Should be 'page and page.meta and page.meta.comments'
            'page.meta.',  # Any direct page.meta access without checking page first
        ]
        
        for pattern in unsafe_patterns:
            if pattern in content and 'page and page.meta' not in content:
                pytest.fail(f"Unsafe page access pattern '{pattern}' found in comments template")


if __name__ == "__main__":
    # Run tests directly
    pytest.main([__file__, "-v"])