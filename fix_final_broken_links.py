#!/usr/bin/env python3
"""
Fix final broken links based on user guidance.
"""

import re
from pathlib import Path

def fix_links(content: str, file_path: Path) -> tuple[str, int]:
    """Fix broken links in content."""
    changes = 0
    
    # Remove infrastructure theory references (user said to erase these)
    if "infrastructure-theory.md" in content or "infrastructure-as-politics.md" in content:
        content = re.sub(r'- \[.*?\]\(.*?infrastructure-theory\.md\)\s*-[^\n]*\n', '', content)
        content = re.sub(r'- \[.*?\]\(.*?infrastructure-as-politics\.md\)\s*-[^\n]*\n', '', content)
        changes += content.count('infrastructure') - content.count('infrastructure')
    
    # Map campaign-planning to project-management-guide
    if "campaign-planning.md" in content:
        content = content.replace("campaign-planning.md", "../../implement/workflows/project-management-guide.md")
        changes += 1
    
    # Map git-errors and fixing-git-problems to a single reference
    if "git-errors.md" in content or "fixing-git-problems.md" in content:
        # Point both to git-command-reference-card which has troubleshooting
        content = content.replace("git-errors.md", "../implement/git/git-command-reference-card.md")
        content = content.replace("fixing-git-problems.md", "../implement/git/git-command-reference-card.md")
        changes += 2
    
    # Map organizational-failure-patterns to anti-pattern-framework
    if "organizational-failure-patterns.md" in content:
        content = content.replace("organizational-failure-patterns.md", "anti-pattern-framework.md")
        changes += 1
    
    # Map first-pull-request and pull-request-template to pr-workflow
    if "first-pull-request.md" in content:
        content = content.replace("first-pull-request.md", "../../implement/obsidian-setup/pr-workflow.md")
        changes += 1
    if "pull-request-template.md" in content:
        content = content.replace("pull-request-template.md", "../../implement/obsidian-setup/pr-workflow.md")
        changes += 1
    
    # Map federation-setup to federation-protocols
    if "federation-setup.md" in content:
        content = content.replace("federation-setup.md", "federation-protocols.md")
        changes += 1
    
    # Map branching-basics to git-in-7-commands (which covers branching)
    if "branching-basics.md" in content:
        content = content.replace("branching-basics.md", "../learn/git-basics/git-in-7-commands.md")
        changes += 1
    
    # Fix remaining specific paths
    if "obsidian-plugins-guide.md" in content:
        content = content.replace("obsidian-plugins-guide.md", "obsidian-integration.md")
        changes += 1
    
    if "pseudonym-discipline.md" in content:
        content = content.replace("pseudonym-discipline.md", "../../implement/security/security-playbook.md")
        changes += 1
    
    if "sensitive-data.md" in content:
        content = content.replace("sensitive-data.md", "../../implement/security/help-committed-sensitive-data.md")
        changes += 1
    
    if "meetings.md" in content:
        content = content.replace("meetings.md", "../../implement/workflows/meeting-workflow-guide.md")
        changes += 1
    
    if "security-model.md" in content:
        content = content.replace("security-model.md", "../core-concepts/druids-security-implementation.md")
        changes += 1
    
    if "security-network.md" in content:
        content = content.replace("security-network.md", "../../implement/security/index.md")
        changes += 1
    
    if "security-protocols.md" in content:
        content = content.replace("security-protocols.md", "../../implement/security/security-playbook.md")
        changes += 1
    
    return content, changes

def process_file(file_path: Path) -> tuple[bool, int]:
    """Process a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, changes = fix_links(content, file_path)
        
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
    
    print("Applying final link fixes...\n")
    
    # Process all markdown files
    for md_file in docs_dir.rglob("*.md"):
        total_files += 1
        
        modified, changes = process_file(md_file)
        
        if modified:
            modified_files += 1
            total_changes += changes
            print(f"✓ Fixed {changes} links in {md_file}")
    
    print(f"\n=== FINAL FIXES COMPLETE ===")
    print(f"Total files processed: {total_files}")
    print(f"Files modified: {modified_files}")
    print(f"Links fixed: {total_changes}")
    
    print("\n=== SUMMARY OF MAPPINGS ===")
    print("- infrastructure-theory/politics → REMOVED (per user request)")
    print("- campaign-planning → project-management-guide")
    print("- git-errors/fixing-git-problems → git-command-reference-card")
    print("- organizational-failure-patterns → anti-pattern-framework")
    print("- first-pull-request/pull-request-template → pr-workflow")
    print("- federation-setup → federation-protocols")
    print("- branching-basics → git-in-7-commands")

if __name__ == "__main__":
    main()