#!/usr/bin/env python3
"""
Convert all markdown links to WikiLinks format in DRUIDS documentation.
"""

import os
import re
from pathlib import Path

def convert_markdown_to_wikilinks(content: str) -> str:
    """Convert markdown links [text](file.md) to WikiLinks [[file|text]] format."""
    
    # Pattern to match markdown links with .md files
    # Matches: [text](path/file.md) or [text](file.md#anchor)
    pattern = r'\[([^\]]+)\]\(([^)]*\.md[^)]*)\)'
    
    def replace_link(match):
        text = match.group(1)
        path = match.group(2)
        
        # Extract just the filename without extension and path
        # Handle anchors if present
        if '#' in path:
            file_part, anchor = path.split('#', 1)
            filename = Path(file_part).stem
            # For now, ignore anchors in WikiLinks (can be added back if needed)
            return f'[[{filename}|{text}]]'
        else:
            filename = Path(path).stem
            return f'[[{filename}|{text}]]'
    
    return re.sub(pattern, replace_link, content)

def process_file(file_path: Path) -> bool:
    """Process a single markdown file to convert links."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert markdown links to wikilinks
        new_content = convert_markdown_to_wikilinks(content)
        
        # Only write if changes were made
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    docs_dir = Path("docs")
    if not docs_dir.exists():
        print("docs/ directory not found")
        return
    
    total_files = 0
    converted_files = 0
    total_conversions = 0
    
    # Process all markdown files
    for md_file in docs_dir.rglob("*.md"):
        total_files += 1
        
        # Count links before conversion
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        before_count = len(re.findall(r'\[([^\]]+)\]\(([^)]*\.md[^)]*)\)', content))
        
        if process_file(md_file):
            converted_files += 1
            total_conversions += before_count
            print(f"Converted {before_count} links in {md_file}")
    
    print(f"\n=== CONVERSION COMPLETE ===")
    print(f"Total files processed: {total_files}")
    print(f"Files with conversions: {converted_files}")
    print(f"Total links converted: {total_conversions}")

if __name__ == "__main__":
    main()