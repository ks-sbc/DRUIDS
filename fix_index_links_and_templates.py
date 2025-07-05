#!/usr/bin/env python3
"""
Fix index.md wikilinks and remove template directory references.
"""

import re
from pathlib import Path

def fix_index_links(content: str, file_path: Path) -> str:
    """Convert index.md wikilinks back to relative markdown links."""
    
    # Pattern to match wikilinks
    pattern = r'\[\[([^|]+)\|([^\]]+)\]\]'
    
    def replace_link(match):
        target = match.group(1)
        text = match.group(2)
        
        # If the target is "index" or ends with "-index", convert to relative path
        if target == "index" or target.endswith("-index"):
            # Determine the relative path based on context
            if "learn/index" in str(file_path):
                if "core-concepts" in text:
                    return f"[{text}](core-concepts/index.md)"
                elif "git-basics" in text:
                    return f"[{text}](git-basics/index.md)"
                elif "druids-fundamentals" in text:
                    return f"[{text}](druids-fundamentals/index.md)"
            elif "implement/index" in str(file_path):
                if "workflows" in text:
                    return f"[{text}](workflows/index.md)"
                elif "security" in text:
                    return f"[{text}](security/index.md)"
            # For root index.md
            elif str(file_path) == "docs/index.md":
                if "Start" in text:
                    return f"[{text}](start/index.md)"
                elif "Learn" in text:
                    return f"[{text}](learn/index.md)"
                elif "Implement" in text:
                    return f"[{text}](implement/index.md)"
                elif "Teach" in text:
                    return f"[{text}](teach/index.md)"
        
        # For non-index files, keep as wikilink
        return match.group(0)
    
    return re.sub(pattern, replace_link, content)

def remove_template_references(content: str) -> str:
    """Remove or fix references to template directory."""
    
    # Remove wikilinks to template files
    content = re.sub(r'\[\[(?:proposal-template|meeting-minutes-template|security-incident-template)\|([^\]]+)\]\]', r'`\1`', content)
    
    # Remove links to _templates directory
    content = re.sub(r'\[([^\]]+)\]\(_templates/[^)]+\)', r'`\1`', content)
    
    return content

def process_file(file_path: Path) -> tuple[bool, int, int]:
    """Process a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Fix index links
        content = fix_index_links(content, file_path)
        
        # Remove template references (but not in _templates directory itself)
        if "_templates" not in str(file_path):
            content = remove_template_references(content)
        
        # Count changes
        index_changes = original.count('[[index|') - content.count('[[index|')
        template_changes = original.count('template|') - content.count('template|')
        
        # Only write if changes were made
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, index_changes, template_changes
        return False, 0, 0
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, 0, 0

def main():
    docs_dir = Path("docs")
    if not docs_dir.exists():
        print("docs/ directory not found")
        return
    
    total_files = 0
    modified_files = 0
    total_index_fixes = 0
    total_template_fixes = 0
    
    print("Fixing index links and removing template references...\n")
    
    # Process all markdown files
    for md_file in docs_dir.rglob("*.md"):
        total_files += 1
        
        modified, index_fixes, template_fixes = process_file(md_file)
        
        if modified:
            modified_files += 1
            total_index_fixes += index_fixes
            total_template_fixes += template_fixes
            if index_fixes > 0 or template_fixes > 0:
                print(f"✓ Fixed {index_fixes} index links, {template_fixes} template refs in {md_file}")
    
    print(f"\n=== FIXES COMPLETE ===")
    print(f"Total files processed: {total_files}")
    print(f"Files modified: {modified_files}")
    print(f"Index links fixed: {total_index_fixes}")
    print(f"Template references removed: {total_template_fixes}")

if __name__ == "__main__":
    main()