#!/usr/bin/env python3
"""Fix wiki-style links to markdown links in DRUIDS documentation."""

import os
import re
from pathlib import Path

# Same mapping as before
LINK_MAPPINGS = {
    # Git-related files
    'git-isnt-programming': 'learn/git-basics/git-isnt-programming.md',
    'git-in-7-commands': 'learn/git-basics/git-in-7-commands.md',
    'your-first-revolutionary-commit': 'learn/tutorials/your-first-revolutionary-commit.md',
    'git-through-campaign': 'learn/git-basics/git-through-campaign.md',
    'git-through-campaign-template': 'teach/workshops/git-through-campaign-template.md',
    'visual-git-workflows': 'learn/git-basics/visual-git-workflows.md',
    'git-command-reference-card': 'implement/git/git-command-reference-card.md',
    'git-quick-reference': 'implement/git/git-quick-reference.md',
    'daily-git-workflows': 'learn/git-basics/daily-git-workflows.md',
    'git-workflows-by-role': 'implement/workflows/git-workflows-by-role.md',
    'git-learning-path': 'learn/git-learning-path.md',
    
    # Core concepts
    'democratic-centralism': 'learn/core-concepts/democratic-centralism.md',
    'druids-security-implementation': 'learn/core-concepts/druids-security-implementation.md',
    'institutional-memory': 'learn/core-concepts/institutional-memory.md',
    'three-tier-system': 'learn/core-concepts/three-tier-system.md',
    'tech-democratization-as-class-struggle': 'learn/core-concepts/tech-democratization-as-class-struggle.md',
    
    # DRUIDS fundamentals
    'druids-red-lines': 'learn/druids-fundamentals/druids-red-lines.md',
    'philosophy': 'learn/druids-fundamentals/philosophy.md',
    'revolutionary-style-guide': 'contributing/revolutionary-style-guide.md',
    
    # Start/Getting Started
    'quick-demo': 'start/quick-demo.md',
    'why-druids': 'start/why-druids.md',
    'getting-started': 'start/index.md',
    'druids-installation-guide': 'implement/getting-started/druids-installation-guide.md',
    'visual-roadmaps': 'learn/visual-roadmaps.md',
    
    # Migration
    'from-google-docs': 'implement/getting-started/migration-guides/from-google-docs.md',
    'from-discord': 'implement/getting-started/migration-guides/from-discord.md',
    'escaping-google-surveillance': 'learn/tutorials/escaping-google-surveillance.md',
    
    # Security
    'security-playbook': 'implement/security/security-playbook.md',
    'help-committed-sensitive-data': 'implement/security/help-committed-sensitive-data.md',
    
    # Templates
    'proposal-template': '_templates/proposal-template.md',
    'meeting-minutes-template': '_templates/meeting-minutes-template.md',
    'security-incident-template': '_templates/security-incident-template.md',
    
    # Teaching
    'teach-tech-without-priest-hood': 'teach/teach-tech-without-priest-hood.md',
    
    # Workflows
    'proposal-process': 'implement/workflows/proposal-process.md',
    'meeting-workflow-guide': 'implement/workflows/meeting-workflow-guide.md',
    'project-management-guide': 'implement/workflows/project-management-guide.md',
    
    # Other
    'glossary': 'reference/glossary.md',
    'complete-setup-guide': 'implement/obsidian-setup/complete-setup-guide.md',
    'why-discord-democracy-fails': 'learn/explanations/why-discord-democracy-fails.md',
    'qm-troubleshooting': 'implement/design/qm-troubleshooting.md',
    
    # MkDocs related
    'setup-giscus': 'implement/mkdocs/setup-giscus.md',
    'offline-usage-guide': 'implement/mkdocs/offline-usage-guide.md',
    'website-validations': 'implement/mkdocs/website-validations.md',
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

def fix_wiki_links_in_file(filepath):
    """Fix wiki-style links in a single markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes_made = []
    
    # Find all wiki-style links [[link|text]] or [[link]]
    wiki_pattern = re.compile(r'\[\[([^\|\]]+)(?:\|([^\]]+))?\]\]')
    
    def replace_wiki_link(match):
        link_target = match.group(1).strip()
        link_text = match.group(2) or link_target
        
        # Remove .md extension if present
        if link_target.endswith('.md'):
            link_target = link_target[:-3]
        
        # Check if this is a link we know how to fix
        if link_target in LINK_MAPPINGS:
            correct_path = LINK_MAPPINGS[link_target]
            
            # Calculate relative path from current file to correct location
            relative_path = get_relative_path(filepath, f"docs/{correct_path}")
            
            new_link = f'[{link_text}]({relative_path})'
            changes_made.append(f"  - '[[{match.group(1)}{'|' + match.group(2) if match.group(2) else ''}]]' → '{new_link}'")
            return new_link
        
        # If we don't know this link, convert to markdown format anyway
        new_link = f'[{link_text}]({link_target}.md)'
        changes_made.append(f"  - '[[{match.group(0)[2:-2]}]]' → '{new_link}' (unknown link)")
        return new_link
    
    content = wiki_pattern.sub(replace_wiki_link, content)
    
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
    """Fix all wiki-style links in the docs directory."""
    docs_dir = Path('docs')
    total_fixes = 0
    files_fixed = 0
    
    # Process all markdown files
    print("Fixing wiki-style links...")
    for filepath in docs_dir.rglob('*.md'):
        fixes = fix_wiki_links_in_file(filepath)
        if fixes > 0:
            total_fixes += fixes
            files_fixed += 1
    
    print(f"\n✅ Fixed {total_fixes} wiki-style links across {files_fixed} files")

if __name__ == '__main__':
    main()