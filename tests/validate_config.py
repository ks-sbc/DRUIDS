#!/usr/bin/env python3
"""
Standalone MkDocs configuration validator
"""

import sys
import os
from pathlib import Path
from mkdocs.config import load_config
from mkdocs.exceptions import ConfigurationError

def validate_mkdocs_config():
    """Validate MkDocs configuration"""
    project_root = Path(__file__).parent.parent
    config_file = project_root / "mkdocs.yml"
    
    if not config_file.exists():
        print("❌ mkdocs.yml not found")
        return False
    
    try:
        print("🔍 Loading MkDocs configuration...")
        config = load_config(str(config_file))
        print("✅ Configuration loaded successfully")
        
        # Validate blog configuration
        print("🔍 Validating blog configuration...")
        plugins = config.get('plugins', [])
        blog_config = None
        
        for plugin in plugins:
            if isinstance(plugin, dict) and 'blog' in plugin:
                blog_config = plugin['blog']
                break
        
        if blog_config:
            authors_enabled = blog_config.get('authors', False)
            authors_file = blog_config.get('authors_file', 'blog/.authors.yml')
            
            if authors_enabled:
                authors_path = Path(config['docs_dir']) / authors_file
                if not authors_path.exists():
                    print(f"❌ Authors enabled but authors file {authors_file} not found")
                    return False
                else:
                    print("✅ Authors configuration valid")
            else:
                print("ℹ️  Authors disabled (free tier)")
        
        # Validate theme icons
        print("🔍 Validating theme icons...")
        theme_config = config.get('theme', {})
        icon_config = theme_config.get('icon', {})
        
        valid_prefixes = [
            'material/',
            'fontawesome/brands/',
            'fontawesome/solid/',
            'fontawesome/regular/',
            'octicons/',
        ]
        
        def check_icon(icon_name, context=""):
            if not icon_name:
                return True
            
            has_valid_prefix = any(icon_name.startswith(prefix) for prefix in valid_prefixes)
            if not has_valid_prefix:
                print(f"❌ Invalid icon '{icon_name}' in {context}")
                return False
            return True
        
        icon_valid = True
        for icon_type, icon_name in icon_config.items():
            if isinstance(icon_name, str):
                if not check_icon(icon_name, f"theme.icon.{icon_type}"):
                    icon_valid = False
            elif isinstance(icon_name, dict):
                for sub_type, sub_icon in icon_name.items():
                    if not check_icon(sub_icon, f"theme.icon.{icon_type}.{sub_type}"):
                        icon_valid = False
        
        if icon_valid:
            print("✅ Theme icons valid")
        else:
            return False
        
        print("✅ All configuration checks passed")
        return True
        
    except ConfigurationError as e:
        print(f"❌ Configuration error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = validate_mkdocs_config()
    sys.exit(0 if success else 1)