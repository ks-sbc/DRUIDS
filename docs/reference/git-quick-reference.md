---
title: "Git Quick Reference for Organizers"
description: "Essential Git commands for revolutionary organizing - print and keep handy"
created: 2025-07-02
updated: 2025-07-02
type: "docs/reference"
security: "L0"
version: "1.0.0"
document_id: "REF-GIT-2025-001-L0"
tags: ["reference", "git", "commands", "printable"]
draft: false
author: ["Comrade 47"]
---

# Git Quick Reference for Organizers

*Print this page and keep it near your computer*

## Essential Daily Commands

### Starting Work
```bash
# See current state
git status

# Update from collective
git pull

# Create new branch for proposal
git checkout -b proposals/rent-strike-2025
```

### Saving Work
```bash
# Stage all changes
git add .

# Stage specific file
git add meetings/2025-07-02-minutes.md

# Commit with message
git commit -m "Add July 2 meeting minutes

- Decided on rent strike strategy
- Assigned organizing tasks
- Next meeting July 9"

# Push to share with comrades
git push origin branch-name
```

### Viewing History
```bash
# See commit history
git log --oneline

# See detailed history
git log

# See what changed
git diff

# See who wrote what line
git blame file.md
```

## Democratic Centralism Commands

### Freedom of Discussion (Branches)
```bash
# Create proposal branch
git checkout -b proposals/campaign-idea

# Switch between branches
git checkout main
git checkout proposals/campaign-idea

# List all branches
git branch -a
```

### Unity of Action (Merging)
```bash
# Update branch with main
git checkout your-branch
git merge main

# After approval, merge to main
git checkout main
git merge proposals/approved-campaign
```

## Common Scenarios

### "I made a mistake!"
```bash
# Undo last commit but keep changes
git reset HEAD~1

# Completely undo last commit
git reset --hard HEAD~1

# Fix commit message
git commit --amend -m "Better message"
```

### "I need to save work temporarily"
```bash
# Stash current changes
git stash

# Do other work, then restore
git stash pop
```

### "What's different from main?"
```bash
# See changed files
git diff main --name-only

# See actual changes
git diff main
```

### "I want to find something"
```bash
# Search all files
git grep "search term"

# Search history
git log --grep="keyword"

# Find when line was added
git log -S "code snippet"
```

## Security Commands

### Identity Management
```bash
# Check current identity
git config user.name
git config user.email

# Set identity for repo
git config user.name "Comrade Rosa"
git config user.email "rosa@protonmail.com"
```

### Cleaning Sensitive Data
```bash
# Remove file from history (DANGEROUS)
git filter-branch --tree-filter \
  'rm -f passwords.txt' HEAD

# Better: Use BFG Repo Cleaner
bfg --delete-files passwords.txt
```

## Collaborative Workflows

### Before Meeting
```bash
# Create meeting branch
git checkout -b meetings/2025-07-02

# Create minutes file
touch meetings/2025-07-02-general.md
```

### After Meeting
```bash
# Add and commit minutes
git add meetings/
git commit -m "Add July 2 general meeting minutes"

# Push for review
git push origin meetings/2025-07-02
```

### Reviewing Proposals
```bash
# Fetch all remote branches
git fetch --all

# Checkout someone's proposal
git checkout origin/proposals/their-idea

# Return to your work
git checkout -
```

## Troubleshooting

### "Permission denied"
```bash
# Check SSH keys
ssh -T git@github.com

# Generate new SSH key if needed
ssh-keygen -t ed25519 -C "rosa@protonmail.com"
```

### "Merge conflict!"
```bash
# See conflicted files
git status

# After editing conflicts
git add resolved-file.md
git commit -m "Resolve merge conflict"
```

### "I committed to wrong branch"
```bash
# Move commit to correct branch
git checkout correct-branch
git cherry-pick commit-hash
git checkout wrong-branch
git reset --hard HEAD~1
```

## Aliases for Efficiency

Add to `~/.gitconfig`:
```ini
[alias]
    # Shortcuts
    st = status
    co = checkout
    br = branch
    cm = commit -m
    
    # Useful compounds
    last = log -1 HEAD
    unstage = reset HEAD --
    visual = log --graph --oneline --all
    
    # Revolutionary aliases
    propose = checkout -b
    decide = merge
    remember = log --grep
```

## Git Philosophy for Organizers

| Git Concept | Organizing Parallel |
|-------------|-------------------|
| Repository | Collective memory |
| Commit | Decision point |
| Branch | Proposal/Discussion |
| Merge | Democratic decision |
| History | Accountability |
| Blame | Not punishment - understanding |

## Emergency Contacts

```bash
# If everything breaks
git reflog  # Shows all actions
git reset --hard HEAD@{1}  # Go back one step

# Nuclear option - fresh start
cd ..
mv repo repo-backup
git clone [repository-url]
```

## Remember

- Commit early, commit often
- Write meaningful commit messages
- Pull before starting work
- Push after completing work
- Branches are free - use them
- History is permanent - be thoughtful
- When confused, ask comrades

---

*"In Git, as in revolution, many branches lead to strong roots."*

**Print double-sided and laminate for durability**

See also: [Your First Revolutionary Commit](/tutorials/your-first-revolutionary-commit.md)