#!/usr/bin/env python3
"""
Fix remaining broken links by updating paths to correct locations.
"""

import re
from pathlib import Path

# Mapping of incorrect paths to correct paths
LINK_FIXES = {
    # Files in wrong locations
    'learn/explanations/infrastructure-theory.md': '../../../infrastructure-theory.md',
    'learn/git-basics/why-rebase-warps-reality.md': '../../why-rebase-warps-reality.md',
    'implement/workflows/why-rebase-warps-reality.md': '../../why-rebase-warps-reality.md',
    
    # CSS file renamed
    'learn/mkdocs/CSS_AESTHETIC_REFERENCE.md': '../../implement/mkdocs/css.md',
    
    # Security files
    '_templates/security-audits-for-organizers.md': '../implement/security/security-audits-for-organizers.md',
    '_templates/when-they-come-knocking.md': '../implement/security/when-they-come-knocking.md',
    
    # Tutorial files
    '_templates/your-first-revolutionary-commit.md': '../learn/tutorials/your-first-revolutionary-commit.md',
    '_templates/tukhachevsky-bridge.md': '../learn/core-concepts/tukhachevsky-bridge.md',
    
    # Obsidian files
    'implement/obsidian-setup/obsidian.md': '../../learn/druids-fundamentals/obsidian-integration.md',
    
    # Federation
    'learn/druids-fundamentals/federation-setup.md': '../../implement/workflows/project-management-guide.md',
    
    # Git workflows
    'learn/druids-fundamentals/first-pull-request.md': '../../implement/obsidian-setup/pr-workflow.md',
    'learn/druids-fundamentals/pull-request-template.md': '../../implement/obsidian-setup/pr-workflow.md',
    
    # Security
    'learn/git-basics/security-model.md': '../core-concepts/druids-security-implementation.md',
    'learn/core-concepts/security-protocols.md': '../../implement/security/security-playbook.md',
    'learn/explanations/security-network.md': '../../implement/security/index.md',
    
    # Meetings and sensitive data
    'learn/tutorials/meetings.md': '../../implement/workflows/meeting-workflow-guide.md',
    'learn/tutorials/sensitive-data.md': '../../implement/security/help-committed-sensitive-data.md',
    'learn/tutorials/pseudonym-discipline.md': '../../implement/security/security-playbook.md',
    
    # Obsidian plugins
    'learn/git-basics/obsidian-plugins-guide.md': '../druids-fundamentals/obsidian-integration.md',
    
    # MkDocs
    'learn/mkdocs/features-demo.md': '../../test-features.md',
    'learn/mkdocs/navigation-guide.md': '../../implement/mkdocs/configuration-reference.md',
    
    # Files that need to be created
    'learn/branching-basics.md': 'branching-basics.md',
    'learn/git-errors.md': 'git-errors.md', 
    'learn/fixing-git-problems.md': 'fixing-git-problems.md',
    'learn/core-concepts/campaign-planning.md': 'campaign-planning.md',
    'learn/core-concepts/organizational-failure-patterns.md': 'organizational-failure-patterns.md',
    'learn/core-concepts/infrastructure-as-politics.md': 'infrastructure-as-politics.md',
    
    # Test files (these are intentionally broken for testing)
    'test-features.md': 'test-features.md',
    'links.md': 'links.md',
    'does-not-exist.md': 'does-not-exist.md',
}

def fix_markdown_links(content: str, file_path: Path) -> tuple[str, int]:
    """Fix markdown links with incorrect paths."""
    changes = 0
    
    # Pattern to match markdown links [text](path)
    pattern = r'\[([^\]]+)\]\(([^)]+\.md)\)'
    
    def replace_link(match):
        nonlocal changes
        text = match.group(1)
        path = match.group(2)
        
        # Check if this path needs fixing
        for wrong_path, correct_path in LINK_FIXES.items():
            if path.endswith(wrong_path.split('/')[-1]):
                # This might be the file we're looking for
                changes += 1
                return f'[{text}]({correct_path})'
        
        return match.group(0)
    
    new_content = re.sub(pattern, replace_link, content)
    return new_content, changes

def fix_specific_links(content: str, file_path: Path) -> tuple[str, int]:
    """Fix specific problematic links based on file location."""
    changes = 0
    
    # Get relative path from docs root
    try:
        rel_path = file_path.relative_to(Path("docs"))
    except ValueError:
        return content, 0
    
    # Specific fixes based on file location
    if str(rel_path) == "learn/explanations/why-discord-democracy-fails.md":
        if "(infrastructure-theory.md)" in content:
            content = content.replace("(infrastructure-theory.md)", "(../../infrastructure-theory.md)")
            changes += 1
    
    elif str(rel_path) == "learn/git-basics/daily-git-workflows.md":
        if "(why-rebase-warps-reality.md)" in content:
            content = content.replace("(why-rebase-warps-reality.md)", "(../../why-rebase-warps-reality.md)")
            changes += 1
    
    elif str(rel_path) == "implement/workflows/git-workflow-guide.md":
        if "(why-rebase-warps-reality.md)" in content:
            content = content.replace("(why-rebase-warps-reality.md)", "(../../why-rebase-warps-reality.md)")
            changes += 1
    
    elif str(rel_path) == "learn/mkdocs/mkdocs.md":
        if "(CSS_AESTHETIC_REFERENCE.md)" in content:
            content = content.replace("(CSS_AESTHETIC_REFERENCE.md)", "(../../implement/mkdocs/css.md)")
            changes += 1
        if "(features-demo.md)" in content:
            content = content.replace("(features-demo.md)", "(../../test-features.md)")
            changes += 1
        if "(navigation-guide.md)" in content:
            content = content.replace("(navigation-guide.md)", "(../../implement/mkdocs/configuration-reference.md)")
            changes += 1
    
    elif str(rel_path).startswith("_templates/"):
        # Fix template file links
        replacements = {
            "(security-audits-for-organizers.md)": "(../implement/security/security-audits-for-organizers.md)",
            "(when-they-come-knocking.md)": "(../implement/security/when-they-come-knocking.md)",
            "(your-first-revolutionary-commit.md)": "(../learn/tutorials/your-first-revolutionary-commit.md)",
            "(tukhachevsky-bridge.md)": "(../learn/core-concepts/tukhachevsky-bridge.md)",
        }
        for old, new in replacements.items():
            if old in content:
                content = content.replace(old, new)
                changes += 1
    
    return content, changes

def process_file(file_path: Path) -> tuple[bool, int]:
    """Process a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply specific fixes first
        new_content, changes1 = fix_specific_links(content, file_path)
        
        # Then apply general fixes
        new_content, changes2 = fix_markdown_links(new_content, file_path)
        
        total_changes = changes1 + changes2
        
        if total_changes > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True, total_changes
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
    
    print("Fixing remaining broken links...\n")
    
    # Process all markdown files
    for md_file in docs_dir.rglob("*.md"):
        total_files += 1
        
        modified, changes = process_file(md_file)
        
        if modified:
            modified_files += 1
            total_changes += changes
            print(f"✓ Fixed {changes} links in {md_file}")
    
    print(f"\n=== FIXES COMPLETE ===")
    print(f"Total files processed: {total_files}")
    print(f"Files modified: {modified_files}")
    print(f"Links fixed: {total_changes}")
    
    # List files that still need to be created
    print("\n=== FILES THAT NEED TO BE CREATED ===")
    missing_files = [
        "branching-basics.md",
        "git-errors.md",
        "fixing-git-problems.md",
        "campaign-planning.md",
        "organizational-failure-patterns.md",
        "infrastructure-as-politics.md",
        "infrastructure-theory.md",
        "first-pull-request.md",
        "federation-setup.md",
    ]
    for f in missing_files:
        print(f"  - {f}")

if __name__ == "__main__":
    main()