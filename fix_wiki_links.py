#!/usr/bin/env python3
"""
Convert Obsidian-style wiki links [[path|text]] to standard markdown links [text](path)
"""
import re
import os
import sys
from pathlib import Path

def convert_wiki_link(match):
    """Convert a single wiki link to markdown format"""
    full_match = match.group(0)
    link_content = match.group(1)
    
    # Split on pipe to get path and text
    if '|' in link_content:
        path, text = link_content.split('|', 1)
    else:
        path = link_content
        text = path.split('/')[-1]  # Use filename as text
    
    # Clean up the path
    path = path.strip()
    text = text.strip()
    
    # Convert absolute paths to relative
    if path.startswith('/'):
        path = path[1:]
    
    # Add .md extension if missing
    if not path.endswith('.md') and not path.endswith('/'):
        path += '.md'
    
    # Calculate relative path based on current file location
    # This is a simplified version - in reality we'd need to know the current file's location
    # For now, we'll use simple heuristics
    if not path.startswith('../') and not path.startswith('./'):
        # If it starts with a known top-level dir, make it relative
        if path.startswith(('learn/', 'teach/', 'implement/', 'start/')):
            # We'll fix these manually per file
            path = path
        else:
            # Assume it's in the same directory
            path = path
    
    return f'[{text}]({path})'

def fix_file(filepath):
    """Fix all wiki links in a single file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match [[path]] or [[path|text]]
    pattern = r'\[\[([^\[\]]+)\]\]'
    
    # Count matches
    matches = re.findall(pattern, content)
    if not matches:
        return 0
    
    # Convert all wiki links
    new_content = re.sub(pattern, convert_wiki_link, content)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return len(matches)

def main():
    docs_dir = Path('/home/percy/Documents/mkdocs/mkdocs/docs')
    
    total_fixed = 0
    files_fixed = 0
    
    # Find all markdown files
    for md_file in docs_dir.rglob('*.md'):
        fixed = fix_file(md_file)
        if fixed > 0:
            print(f"Fixed {fixed} links in {md_file.relative_to(docs_dir)}")
            total_fixed += fixed
            files_fixed += 1
    
    print(f"\nTotal: Fixed {total_fixed} links in {files_fixed} files")

if __name__ == '__main__':
    main()