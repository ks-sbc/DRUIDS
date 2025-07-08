#!/usr/bin/env python3
"""
Convert wikilinks from full paths to filename-only format for pub-obsidian plugin.
The plugin will resolve these based on the filename across the entire docs directory.
"""

import re
from pathlib import Path

def convert_wikilinks_to_filename(content: str) -> str:
    """Convert [[path/to/file|text]] to [[file|text]] format."""
    
    # Pattern to match wikilinks with paths
    pattern = r'\[\[([^|\]]+)\|([^\]]+)\]\]'
    
    def replace_link(match):
        path = match.group(1)
        text = match.group(2)
        
        # Extract just the filename from the path
        filename = Path(path).name
        
        # Return wikilink with just filename
        return f'[[{filename}|{text}]]'
    
    return re.sub(pattern, replace_link, content)

def process_file(file_path: Path) -> tuple[bool, int]:
    """Process a single markdown file to fix wikilinks."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count wikilinks with paths before conversion
        link_count = len(re.findall(r'\[\[([^|\]]*\/[^|\]]+)\|([^\]]+)\]\]', content))
        
        # Convert wikilinks to filename-only format
        new_content = convert_wikilinks_to_filename(content)
        
        # Only write if changes were made
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True, link_count
        return False, 0
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, 0

def main():
    docs_dir = Path("docs")
    if not docs_dir.exists():
        print("docs/ directory not found")
        return
    
    total_files = 0
    converted_files = 0
    total_conversions = 0
    
    print("Converting wikilinks to filename-only format...\n")
    
    # Process all markdown files
    for md_file in docs_dir.rglob("*.md"):
        total_files += 1
        
        converted, link_count = process_file(md_file)
        
        if converted:
            converted_files += 1
            total_conversions += link_count
            print(f"✓ Fixed {link_count} wikilinks in {md_file}")
    
    print(f"\n=== CONVERSION COMPLETE ===")
    print(f"Total files processed: {total_files}")
    print(f"Files with conversions: {converted_files}")
    print(f"Total wikilinks fixed: {total_conversions}")
    
    print("\nNote: pub-obsidian plugin will now resolve links by filename across the entire docs directory.")

if __name__ == "__main__":
    main()