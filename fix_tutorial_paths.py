#!/usr/bin/env python3
"""
Fix paths to your-first-revolutionary-commit.md tutorial.
"""

import re
from pathlib import Path

def fix_tutorial_path(content: str, file_path: Path) -> tuple[str, int]:
    """Fix the path to the tutorial based on file location."""
    changes = 0
    
    # The tutorial is at docs/learn/tutorials/your-first-revolutionary-commit.md
    tutorial_path = Path("docs/learn/tutorials/your-first-revolutionary-commit.md")
    
    # Get the directory of the current file
    file_dir = file_path.parent
    
    # Calculate relative path from current file to tutorial
    try:
        # Calculate how to get from file_dir to tutorial_path
        rel_path = Path("docs").resolve()
        file_rel = file_dir.resolve()
        tutorial_rel = tutorial_path.resolve()
        
        # Get relative path
        common = Path(*[p for p in file_rel.parts if p in tutorial_rel.parts])
        
        # Simple approach: count directory levels
        if "learn/git-basics" in str(file_path):
            correct_path = "../tutorials/your-first-revolutionary-commit.md"
        elif "learn/core-concepts" in str(file_path):
            correct_path = "../tutorials/your-first-revolutionary-commit.md"
        elif "learn/druids-fundamentals" in str(file_path):
            correct_path = "../tutorials/your-first-revolutionary-commit.md"
        elif "learn/explanations" in str(file_path):
            correct_path = "../tutorials/your-first-revolutionary-commit.md"
        elif "learn/index.md" in str(file_path):
            correct_path = "tutorials/your-first-revolutionary-commit.md"
        elif "learn/git-learning-path.md" in str(file_path):
            correct_path = "tutorials/your-first-revolutionary-commit.md"
        elif "implement/getting-started" in str(file_path):
            correct_path = "../../../learn/tutorials/your-first-revolutionary-commit.md"
        elif "implement/git" in str(file_path):
            correct_path = "../../learn/tutorials/your-first-revolutionary-commit.md"
        elif "contributing" in str(file_path):
            correct_path = "../learn/tutorials/your-first-revolutionary-commit.md"
        else:
            return content, 0
            
        # Replace the incorrect path
        if "../learn/tutorials/your-first-revolutionary-commit.md" in content:
            content = content.replace("../learn/tutorials/your-first-revolutionary-commit.md", correct_path)
            changes += 1
            
    except Exception as e:
        print(f"Error calculating path for {file_path}: {e}")
        
    return content, changes

def process_file(file_path: Path) -> tuple[bool, int]:
    """Process a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, changes = fix_tutorial_path(content, file_path)
        
        if changes > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True, changes
        return False, 0
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, 0

def main():
    # Files that need fixing
    files_to_fix = [
        "docs/learn/git-basics/git-isnt-programming.md",
        "docs/learn/git-basics/visual-git-workflows.md",
        "docs/learn/core-concepts/power-steering-metaphor.md",
        "docs/learn/core-concepts/institutional-memory.md",
        "docs/learn/druids-fundamentals/philosophy.md",
        "docs/learn/index.md",
        "docs/learn/git-learning-path.md",
        "docs/learn/explanations/institutional-memory-and-onboarding.md",
        "docs/implement/getting-started/migration-guides/from-google-docs.md",
        "docs/implement/git/git-quick-reference.md",
        "docs/implement/git/git-command-reference-card.md",
        "docs/contributing/cross-reference-guide.md",
    ]
    
    total_changes = 0
    
    print("Fixing tutorial paths...\n")
    
    for file_str in files_to_fix:
        file_path = Path(file_str)
        if file_path.exists():
            modified, changes = process_file(file_path)
            if modified:
                total_changes += changes
                print(f"✓ Fixed {file_path}")
    
    print(f"\n=== TUTORIAL PATH FIXES COMPLETE ===")
    print(f"Total files fixed: {total_changes}")

if __name__ == "__main__":
    main()