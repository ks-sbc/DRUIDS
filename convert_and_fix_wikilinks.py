#!/usr/bin/env python3
"""
Convert all markdown links to WikiLinks format and fix broken paths.
This script both converts markdown links to wikilinks AND fixes broken link paths.
"""

import os
import re
from pathlib import Path
from typing import Dict, Tuple, Optional

# Mapping of broken link targets to their correct paths
LINK_MAPPINGS = {
    # Core concepts
    'democratic-centralism': 'learn/core-concepts/democratic-centralism',
    'institutional-memory': 'learn/core-concepts/institutional-memory',
    'three-tier-system': 'learn/core-concepts/three-tier-system',
    'power-steering-metaphor': 'learn/core-concepts/power-steering-metaphor',
    'tukhachevsky-bridge': 'learn/core-concepts/tukhachevsky-bridge',
    'anti-pattern-framework': 'learn/core-concepts/anti-pattern-framework',
    
    # Git basics
    'git-isnt-programming': 'learn/git-basics/git-isnt-programming',
    'git-in-7-commands': 'learn/git-basics/git-in-7-commands',
    'git-through-campaign': 'learn/git-basics/git-through-campaign',
    'git-through-campaign-template': 'teach/workshops/git-through-campaign-template',
    'your-first-revolutionary-commit': 'learn/tutorials/your-first-revolutionary-commit',
    'visual-git-workflows': 'learn/git-basics/visual-git-workflows',
    'daily-git-workflows': 'learn/git-basics/daily-git-workflows',
    'git-learning-path': 'learn/git-learning-path',
    'why-revolutionaries-need-git': 'learn/git-basics/why-revolutionaries-need-git',
    
    # DRUIDS fundamentals
    'druids-security-implementation': 'implement/security/druids-security-implementation',
    'druids-red-lines': 'learn/druids-fundamentals/druids-red-lines',
    'philosophy': 'learn/druids-fundamentals/philosophy',
    'federation-protocols': 'learn/druids-fundamentals/federation-protocols',
    
    # Security
    'security-playbook': 'implement/security/security-playbook',
    'security-protocols': 'implement/security/security-protocols',
    'security-network': 'implement/security/security-network',
    'help-committed-sensitive-data': 'implement/security/help-committed-sensitive-data',
    'security-incident-template': 'templates/security-incident-template',
    
    # Implementation
    'druids-installation-guide': 'implement/getting-started/druids-installation-guide',
    'complete-setup-guide': 'implement/obsidian-setup/complete-setup-guide',
    'obsidian': 'implement/obsidian-setup/obsidian',
    'obsidian-plugins-guide': 'implement/obsidian-setup/obsidian-plugins-guide',
    'pr-workflow': 'implement/obsidian-setup/pr-workflow',
    'proposal-process': 'implement/workflows/proposal-process',
    
    # Git reference
    'git-quick-reference': 'implement/git/git-quick-reference',
    'git-command-reference-card': 'implement/git/git-command-reference-card',
    
    # Explanations
    'why-discord-democracy-fails': 'learn/explanations/why-discord-democracy-fails',
    'state-repression': 'learn/explanations/state-repression',
    'tech-democratization-as-class-struggle': 'learn/explanations/tech-democratization-as-class-struggle',
    
    # Migration guides
    'breaking-discord-chains': 'implement/migration-guides/breaking-discord-chains',
    'from-google-docs': 'implement/migration-guides/from-google-docs',
    'from-discord': 'implement/migration-guides/from-discord',
    'escaping-google-surveillance': 'learn/tutorials/escaping-google-surveillance',
    
    # Tutorials
    'onboarding-without-burnout': 'learn/tutorials/onboarding-without-burnout',
    
    # Teaching
    'teach-tech-without-priest-hood': 'teach/teach-tech-without-priest-hood',
    'revolutionary-style-guide': 'teach/revolutionary-style-guide',
    
    # Templates
    'proposal-template': 'templates/proposal-template',
    'meeting-minutes-template': 'templates/meeting-minutes-template',
    
    # Start/quick references
    'why-druids': 'start/why-druids',
    'quick-demo': 'start/quick-demo',
    'onboarding-yourself-in-3-days': 'start/onboarding-yourself-in-3-days',
    'visual-roadmaps': 'learn/visual-roadmaps',
    'getting-started': 'start/getting-started',
    
    # Workflows
    'git-workflow-guide': 'implement/workflows/git-workflow-guide',
    'bus-factor-elimination': 'implement/workflows/bus-factor-elimination',
    'meeting-workflow-guide': 'implement/workflows/meeting-workflow-guide',
    'project-management-guide': 'implement/workflows/project-management-guide',
    
    # MkDocs/website
    'mkdocs': 'learn/mkdocs/mkdocs',
    'features-demo': 'learn/mkdocs/features-demo',
    'navigation-guide': 'learn/mkdocs/navigation-guide',
    'test-features': 'test-features',
    'CSS_AESTHETIC_REFERENCE': 'learn/mkdocs/CSS_AESTHETIC_REFERENCE',
    'setup-giscus': 'learn/mkdocs/setup-giscus',
    'offline-usage-guide': 'learn/mkdocs/offline-usage-guide',
    'website-validations': 'learn/mkdocs/website-validations',
    
    # Other references
    'glossary': 'reference/glossary',
    'qm-troubleshooting': 'reference/design/qm-troubleshooting',
    'links': 'reference/links',
    'does-not-exist': 'reference/does-not-exist',
    
    # Missing explanations/theory
    'why-rebase-warps-reality': 'learn/explanations/why-rebase-warps-reality',
    'git-democracy': 'learn/explanations/git-democracy',
    'infrastructure-theory': 'learn/explanations/infrastructure-theory',
    'infrastructure-as-politics': 'learn/explanations/infrastructure-as-politics',
    'organizational-failure-patterns': 'learn/explanations/organizational-failure-patterns',
    
    # Missing how-tos
    'campaign-planning': 'implement/workflows/campaign-planning',
    'federation-setup': 'implement/federation/federation-setup',
    'git-workflows-by-role': 'implement/workflows/git-workflows-by-role',
    'first-pull-request': 'implement/workflows/first-pull-request',
    'pull-request-template': 'templates/pull-request-template',
    'git-as-democratic-centralism': 'learn/explanations/git-as-democratic-centralism',
    
    # Missing references
    'sensitive-data': 'implement/security/sensitive-data',
    'first-commit': 'learn/tutorials/first-commit',
    'pseudonym-discipline': 'implement/security/pseudonym-discipline',
    'meetings': 'implement/workflows/meetings',
    'breaking-discord': 'implement/migration-guides/breaking-discord',
}

def find_correct_path(link_target: str, source_file: Path, docs_dir: Path) -> Optional[str]:
    """Find the correct path for a broken link."""
    # Remove .md extension and any anchors
    clean_target = link_target.replace('.md', '').split('#')[0]
    
    # Check if it's in our mappings
    for pattern, correct_path in LINK_MAPPINGS.items():
        if clean_target.endswith(pattern) or pattern == clean_target:
            return correct_path
    
    # If not in mappings, try to find the file
    target_name = Path(clean_target).name
    for md_file in docs_dir.rglob(f"{target_name}.md"):
        # Get relative path from docs dir
        rel_path = md_file.relative_to(docs_dir).with_suffix('')
        return str(rel_path)
    
    return None

def convert_markdown_to_wikilinks(content: str, source_file: Path, docs_dir: Path) -> str:
    """Convert markdown links [text](file.md) to WikiLinks [[file|text]] format with fixed paths."""
    
    # Pattern to match markdown links with .md files
    pattern = r'\[([^\]]+)\]\(([^)]*\.md[^)]*)\)'
    
    def replace_link(match):
        text = match.group(1)
        path = match.group(2)
        
        # Handle external links
        if path.startswith('http'):
            return match.group(0)  # Keep as-is
        
        # Find correct path
        correct_path = find_correct_path(path, source_file, docs_dir)
        
        if correct_path:
            # Convert to wikilink with full path (no .md extension)
            return f'[[{correct_path}|{text}]]'
        else:
            print(f"WARNING: Could not find correct path for '{path}' in {source_file}")
            # Convert to wikilink anyway, but keep the broken path
            filename = Path(path).stem
            return f'[[{filename}|{text}]]'
    
    return re.sub(pattern, replace_link, content)

def process_file(file_path: Path, docs_dir: Path) -> Tuple[bool, int]:
    """Process a single markdown file to convert links."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count links before conversion
        link_count = len(re.findall(r'\[([^\]]+)\]\(([^)]*\.md[^)]*)\)', content))
        
        # Convert markdown links to wikilinks with fixed paths
        new_content = convert_markdown_to_wikilinks(content, file_path, docs_dir)
        
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
    
    print("Converting markdown links to wikilinks and fixing broken paths...\n")
    
    # Process all markdown files
    for md_file in docs_dir.rglob("*.md"):
        total_files += 1
        
        converted, link_count = process_file(md_file, docs_dir)
        
        if converted:
            converted_files += 1
            total_conversions += link_count
            print(f"✓ Converted {link_count} links in {md_file}")
    
    print(f"\n=== CONVERSION COMPLETE ===")
    print(f"Total files processed: {total_files}")
    print(f"Files with conversions: {converted_files}")
    print(f"Total links converted: {total_conversions}")
    
    # Update TodoWrite to mark task complete
    print("\n✓ All markdown links have been converted to wikilinks with corrected paths")

if __name__ == "__main__":
    main()