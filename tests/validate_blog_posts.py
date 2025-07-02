#!/usr/bin/env python3
"""
Blog post validation script
"""

import sys
import yaml
from pathlib import Path
from mkdocs.config import load_config

def validate_blog_posts():
    """Validate blog post frontmatter and content"""
    project_root = Path(__file__).parent.parent
    blog_posts_dir = project_root / "docs" / "blog" / "posts"
    
    if not blog_posts_dir.exists():
        print("ℹ️  No blog posts directory found, skipping validation")
        return True
    
    # Load MkDocs config to check blog settings
    try:
        config = load_config(str(project_root / "mkdocs.yml"))
    except Exception as e:
        print(f"❌ Failed to load MkDocs config: {e}")
        return False
    
    # Get blog configuration
    blog_config = None
    for plugin in config.get('plugins', []):
        if isinstance(plugin, dict) and 'blog' in plugin:
            blog_config = plugin['blog']
            break
    
    authors_enabled = blog_config and blog_config.get('authors', False)
    allowed_categories = blog_config and blog_config.get('categories_allowed', [])
    
    print(f"🔍 Validating blog posts (authors: {'enabled' if authors_enabled else 'disabled'})...")
    
    all_valid = True
    post_files = list(blog_posts_dir.glob("*.md"))
    
    if not post_files:
        print("ℹ️  No blog posts found")
        return True
    
    for post_file in post_files:
        print(f"  📄 Checking {post_file.name}...")
        
        try:
            with open(post_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"    ❌ Failed to read file: {e}")
            all_valid = False
            continue
        
        # Check for frontmatter
        if not content.startswith('---'):
            print(f"    ❌ Missing frontmatter")
            all_valid = False
            continue
        
        # Extract and parse frontmatter
        try:
            parts = content.split('---', 2)
            if len(parts) < 3:
                print(f"    ❌ Invalid frontmatter format")
                all_valid = False
                continue
            
            frontmatter_str = parts[1]
            frontmatter = yaml.safe_load(frontmatter_str)
            
            if not isinstance(frontmatter, dict):
                print(f"    ❌ Frontmatter is not a dictionary")
                all_valid = False
                continue
                
        except yaml.YAMLError as e:
            print(f"    ❌ Invalid YAML in frontmatter: {e}")
            all_valid = False
            continue
        
        # Check required fields
        if 'date' not in frontmatter:
            print(f"    ❌ Missing required 'date' field")
            all_valid = False
        
        # Check authors configuration
        if 'authors' in frontmatter:
            if not authors_enabled:
                print(f"    ❌ Authors found but authors are disabled in config")
                all_valid = False
            else:
                # Validate author format
                authors = frontmatter['authors']
                if not isinstance(authors, list):
                    print(f"    ❌ Authors must be a list")
                    all_valid = False
        
        # Check categories
        if 'categories' in frontmatter and allowed_categories:
            post_categories = frontmatter['categories']
            if isinstance(post_categories, list):
                for category in post_categories:
                    if category not in allowed_categories:
                        print(f"    ❌ Category '{category}' not in allowed list: {allowed_categories}")
                        all_valid = False
        
        # Check for excerpt separator
        if '<!-- more -->' not in content:
            print(f"    ⚠️  Missing excerpt separator '<!-- more -->' (recommended)")
        
        if all_valid:
            print(f"    ✅ Valid")
    
    if all_valid:
        print("✅ All blog posts are valid")
    else:
        print("❌ Some blog posts have validation errors")
    
    return all_valid

if __name__ == "__main__":
    success = validate_blog_posts()
    sys.exit(0 if success else 1)