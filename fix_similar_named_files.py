#!/usr/bin/env python3
"""
Fix wikilinks that point to similar but differently named files.
"""

import re
from pathlib import Path

# Mapping of wikilink targets to actual existing files
SIMILAR_FILE_MAPPINGS = {
    # Files that exist with different names
    'signal-isnt-enough': 'signal-isnt-enough',  # Already exists
    'role-of-ai': 'role-of-ai',  # Already exists
    'google-drive-trap': 'google-drive-trap',  # Already exists
    'git-command-reference-card': 'git-command-reference-card',  # Already exists
    'git-commands': 'git-command-reference-card',  # Map to existing reference card
    'visual-git-reference': 'visual-git-workflows',  # Map to visual workflows
    'first-commit': 'your-first-revolutionary-commit',  # Map to revolutionary commit
    'git-as-democratic-centralism': 'democratic-centralism-code-review',  # Map to code review doc
    'git-democracy': 'democratic-centralism-code-review',  # Also map to code review doc
    'breaking-discord-chains': 'from-discord',  # Map to migration guide
    'breaking-discord': 'from-discord',  # Also map to migration guide
    
    # Other common mappings
    'druids-security-implementation': 'druids-security-implementation',
    'revolutionary-commit-conventions': 'revolutionary-commit-conventions', 
    'complete-setup-guide': 'complete-setup-guide',
    'druids-red-lines': 'druids-red-lines',
    'federation-protocols': 'federation-protocols',
    
    # Files we'll need to create later
    'why-rebase-warps-reality': 'why-rebase-warps-reality',  # Needs creation
    'infrastructure-theory': 'infrastructure-theory',  # Needs creation
    'infrastructure-as-politics': 'infrastructure-as-politics',  # Needs creation
    'organizational-failure-patterns': 'organizational-failure-patterns',  # Needs creation
    'branching-basics': 'branching-basics',  # Needs creation
    'git-errors': 'git-errors',  # Needs creation
    'fixing-git-problems': 'fixing-git-problems',  # Needs creation
    'first-pull-request': 'first-pull-request',  # Needs creation
    'federation-setup': 'federation-setup',  # Needs creation
    'campaign-planning': 'campaign-planning',  # Needs creation
}

def fix_wikilinks(content: str) -> tuple[str, int]:
    """Fix wikilinks to use correct file names."""
    changes = 0
    
    # Pattern to match wikilinks
    pattern = r'\[\[([^|]+)\|([^\]]+)\]\]'
    
    def replace_link(match):
        nonlocal changes
        target = match.group(1)
        text = match.group(2)
        
        # Check if this target needs to be mapped
        if target in SIMILAR_FILE_MAPPINGS:
            new_target = SIMILAR_FILE_MAPPINGS[target]
            if new_target != target:
                changes += 1
                return f'[[{new_target}|{text}]]'
        
        return match.group(0)
    
    new_content = re.sub(pattern, replace_link, content)
    return new_content, changes

def process_file(file_path: Path) -> tuple[bool, int]:
    """Process a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, changes = fix_wikilinks(content)
        
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
    
    # First, let's verify which files exist
    print("Verifying existing files...\n")
    existing_files = set()
    for md_file in docs_dir.rglob("*.md"):
        filename = md_file.stem
        existing_files.add(filename)
    
    # Check our mappings
    print("Files that exist:")
    for old, new in SIMILAR_FILE_MAPPINGS.items():
        if old != new and new in existing_files:
            print(f"  ✓ {old} → {new}")
    
    print("\nFiles that need to be created:")
    missing = set()
    for old, new in SIMILAR_FILE_MAPPINGS.items():
        if new not in existing_files and new not in missing:
            missing.add(new)
            print(f"  ✗ {new}")
    
    print("\n" + "="*50 + "\n")
    
    total_files = 0
    modified_files = 0
    total_changes = 0
    
    print("Fixing wikilinks to similar named files...\n")
    
    # Process all markdown files
    for md_file in docs_dir.rglob("*.md"):
        total_files += 1
        
        modified, changes = process_file(md_file)
        
        if modified:
            modified_files += 1
            total_changes += changes
            print(f"✓ Fixed {changes} wikilinks in {md_file}")
    
    print(f"\n=== FIXES COMPLETE ===")
    print(f"Total files processed: {total_files}")
    print(f"Files modified: {modified_files}")
    print(f"Wikilinks fixed: {total_changes}")

if __name__ == "__main__":
    main()