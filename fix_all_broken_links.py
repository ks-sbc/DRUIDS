#!/usr/bin/env python3
"""Comprehensive fix for all broken internal links in DRUIDS documentation."""

import os
import re
from pathlib import Path
from collections import defaultdict

# First, let's scan all files to understand link patterns
def scan_all_links(docs_dir):
    """Scan all markdown files to find all links."""
    all_links = defaultdict(list)
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    
    for filepath in Path(docs_dir).rglob('*.md'):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        for match in link_pattern.finditer(content):
            link_target = match.group(2)
            # Skip external links and anchors
            if not link_target.startswith(('http://', 'https://', '#', 'mailto:')):
                all_links[link_target].append(str(filepath))
    
    return all_links

# Mapping of broken links to their correct locations
LINK_MAPPINGS = {
    # Git-related files
    'git-isnt-programming.md': 'learn/git-basics/git-isnt-programming.md',
    'git-in-7-commands.md': 'learn/git-basics/git-in-7-commands.md',
    'your-first-revolutionary-commit.md': 'learn/tutorials/your-first-revolutionary-commit.md',
    'git-through-campaign.md': 'learn/git-basics/git-through-campaign.md',
    'git-through-campaign-template.md': 'teach/workshops/git-through-campaign-template.md',
    'visual-git-workflows.md': 'learn/git-basics/visual-git-workflows.md',
    'git-command-reference-card.md': 'implement/git/git-command-reference-card.md',
    'git-quick-reference.md': 'implement/git/git-quick-reference.md',
    'daily-git-workflows.md': 'learn/git-basics/daily-git-workflows.md',
    'git-workflows-by-role.md': 'implement/workflows/git-workflows-by-role.md',
    'git-learning-path.md': 'learn/git-learning-path.md',
    
    # Core concepts
    'democratic-centralism.md': 'learn/core-concepts/democratic-centralism.md',
    'druids-security-implementation.md': 'learn/core-concepts/druids-security-implementation.md',
    'institutional-memory.md': 'learn/core-concepts/institutional-memory.md',
    'three-tier-system.md': 'learn/core-concepts/three-tier-system.md',
    'tech-democratization-as-class-struggle.md': 'learn/core-concepts/tech-democratization-as-class-struggle.md',
    
    # DRUIDS fundamentals
    'druids-red-lines.md': 'learn/druids-fundamentals/druids-red-lines.md',
    'philosophy.md': 'learn/druids-fundamentals/philosophy.md',
    'revolutionary-style-guide.md': 'contributing/revolutionary-style-guide.md',
    
    # Start/Getting Started
    'quick-demo.md': 'start/quick-demo.md',
    'why-druids.md': 'start/why-druids.md',
    'getting-started.md': 'start/index.md',
    'druids-installation-guide.md': 'implement/getting-started/druids-installation-guide.md',
    'visual-roadmaps.md': 'learn/visual-roadmaps.md',
    
    # Migration
    'from-google-docs.md': 'implement/getting-started/migration-guides/from-google-docs.md',
    'from-discord.md': 'implement/getting-started/migration-guides/from-discord.md',
    'escaping-google-surveillance.md': 'learn/tutorials/escaping-google-surveillance.md',
    
    # Security
    'security-playbook.md': 'implement/security/security-playbook.md',
    'help-committed-sensitive-data.md': 'implement/security/help-committed-sensitive-data.md',
    
    # Templates
    'proposal-template.md': '_templates/proposal-template.md',
    'meeting-minutes-template.md': '_templates/meeting-minutes-template.md',
    'security-incident-template.md': '_templates/security-incident-template.md',
    
    # Teaching
    'teach-tech-without-priest-hood.md': 'teach/teach-tech-without-priest-hood.md',
    
    # Workflows
    'proposal-process.md': 'implement/workflows/proposal-process.md',
    'meeting-workflow-guide.md': 'implement/workflows/meeting-workflow-guide.md',
    'project-management-guide.md': 'implement/workflows/project-management-guide.md',
    
    # Other
    'glossary.md': 'reference/glossary.md',
    'complete-setup-guide.md': 'implement/obsidian-setup/complete-setup-guide.md',
    'why-discord-democracy-fails.md': 'learn/explanations/why-discord-democracy-fails.md',
    'qm-troubleshooting.md': 'implement/design/qm-troubleshooting.md',
    
    # MkDocs related
    'setup-giscus.md': 'implement/mkdocs/setup-giscus.md',
    'offline-usage-guide.md': 'implement/mkdocs/offline-usage-guide.md',
    'website-validations.md': 'implement/mkdocs/website-validations.md',
    
    # Files that were deleted - map to alternatives
    'obsidian.md': 'learn/druids-fundamentals/obsidian-integration.md',
    'test-features.md': 'test-features.md',  # In root
    'sensitive-data.md': 'implement/security/help-committed-sensitive-data.md',
    'first-commit.md': 'learn/tutorials/your-first-revolutionary-commit.md',
    'meetings.md': 'implement/workflows/meeting-workflow-guide.md',
    'pull-request-template.md': '_templates/proposal-template.md',
    'security-protocols.md': 'implement/security/security-playbook.md',
    
    # Files with no alternatives (will be removed)
    'why-rebase-warps-reality.md': None,
    'security-network.md': None,
    'infrastructure-as-politics.md': None,
    'git-democracy.md': None,
    'infrastructure-theory.md': None,
    'breaking-discord-chains.md': None,
    'obsidian-plugins-guide.md': None,
    'security-model.md': None,
    'campaign-planning.md': None,
    'organizational-failure-patterns.md': None,
    'first-pull-request.md': None,
    'git-as-democratic-centralism.md': None,
    'federation-setup.md': None,
    'pseudonym-discipline.md': None,
    'breaking-discord.md': None,
    'features-demo.md': None,
    'navigation-guide.md': None,
    'CSS_AESTHETIC_REFERENCE.md': None,
    
    # Special case - these exist but need path correction
    'links.md': None,  # This is a test file reference
    'does-not-exist.md': None,  # This is a test file reference
}

def get_relative_path(from_file, to_file):
    """Calculate relative path from one file to another."""
    from_path = Path(from_file).parent
    to_path = Path(to_file)
    
    try:
        return os.path.relpath(to_path, from_path)
    except ValueError:
        # If paths are on different drives on Windows
        return to_file

def fix_links_in_file(filepath):
    """Fix broken links in a single markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes_made = []
    
    # Find all markdown links
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    
    def replace_link(match):
        link_text = match.group(1)
        link_target = match.group(2)
        
        # Skip external links and anchors
        if link_target.startswith(('http://', 'https://', '#', 'mailto:')):
            return match.group(0)
        
        # Extract just the filename from the path
        filename = os.path.basename(link_target)
        
        # Check if this is a broken link we know how to fix
        if filename in LINK_MAPPINGS:
            correct_path = LINK_MAPPINGS[filename]
            
            # Handle deleted files
            if correct_path is None:
                # Comment out the link
                changes_made.append(f"  - '{link_target}' → REMOVED (file deleted)")
                return f'{link_text} *(link removed - file deleted)*'
            
            # Calculate relative path from current file to correct location
            relative_path = get_relative_path(filepath, f"docs/{correct_path}")
            
            new_link = f'[{link_text}]({relative_path})'
            changes_made.append(f"  - '{link_target}' → '{relative_path}'")
            return new_link
        
        return match.group(0)
    
    content = link_pattern.sub(replace_link, content)
    
    # Only write if changes were made
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\nFixed {filepath}:")
        for change in changes_made:
            print(change)
        return len(changes_made)
    
    return 0

def main():
    """Fix all broken links in the docs directory."""
    docs_dir = Path('docs')
    total_fixes = 0
    files_fixed = 0
    
    # First, scan to understand what links exist
    print("Scanning for all internal links...")
    all_links = scan_all_links(docs_dir)
    
    # Process all markdown files
    print("\nFixing broken links...")
    for filepath in docs_dir.rglob('*.md'):
        fixes = fix_links_in_file(filepath)
        if fixes > 0:
            total_fixes += fixes
            files_fixed += 1
    
    print(f"\n✅ Fixed {total_fixes} broken links across {files_fixed} files")

if __name__ == '__main__':
    main()