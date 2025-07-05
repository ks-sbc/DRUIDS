#!/usr/bin/env python3
"""
Convert all wikilinks to standard markdown links.
"""

import re
from pathlib import Path

def find_target_file(filename: str, current_file: Path, docs_dir: Path) -> str:
    """Find the correct relative path to the target file."""
    # Remove .md extension if present
    if filename.endswith('.md'):
        filename = filename[:-3]
    
    # Search for the file
    for md_file in docs_dir.rglob("*.md"):
        if md_file.stem == filename:
            # Calculate relative path from current file to target
            try:
                rel_path = md_file.relative_to(docs_dir)
                current_rel = current_file.parent.relative_to(docs_dir)
                
                # Calculate how many levels up we need to go
                levels_up = len(current_rel.parts)
                
                if levels_up == 0:
                    # We're in the docs root
                    return str(rel_path)
                else:
                    # Go up the required levels
                    prefix = "../" * levels_up
                    return prefix + str(rel_path)
            except ValueError:
                # If relative_to fails, use absolute path from docs
                return "/" + str(md_file.relative_to(docs_dir))
    
    # If not found, return the original with .md
    return filename + ".md"

def convert_wikilinks(content: str, current_file: Path, docs_dir: Path) -> tuple[str, int]:
    """Convert wikilinks to markdown links."""
    changes = 0
    
    # Pattern to match wikilinks [[target|text]] or [[target]]
    pattern = r'\[\[([^|\]]+)(?:\|([^\]]+))?\]\]'
    
    def replace_link(match):
        nonlocal changes
        target = match.group(1).strip()
        text = match.group(2)
        
        if text is None:
            # No custom text, use the target as text
            text = target
        
        # Find the correct path
        correct_path = find_target_file(target, current_file, docs_dir)
        
        changes += 1
        return f'[{text}]({correct_path})'
    
    new_content = re.sub(pattern, replace_link, content)
    return new_content, changes

def process_file(file_path: Path, docs_dir: Path) -> tuple[bool, int]:
    """Process a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, changes = convert_wikilinks(content, file_path, docs_dir)
        
        if changes > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True, changes
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
    modified_files = 0
    total_changes = 0
    
    print("Converting all wikilinks to markdown links...\n")
    
    # Process all markdown files
    for md_file in docs_dir.rglob("*.md"):
        # Skip template files
        if '_templates' in str(md_file):
            continue
            
        total_files += 1
        
        modified, changes = process_file(md_file, docs_dir)
        
        if modified:
            modified_files += 1
            total_changes += changes
            print(f"✓ Converted {changes} wikilinks in {md_file}")
    
    print(f"\n=== CONVERSION COMPLETE ===")
    print(f"Total files processed: {total_files}")
    print(f"Files modified: {modified_files}")
    print(f"Wikilinks converted: {total_changes}")

if __name__ == "__main__":
    main()