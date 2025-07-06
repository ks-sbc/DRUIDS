---
title: "Git Command Reference Card for Revolutionary Organizers"
description: "Essential Git commands for daily organizing work - print and keep handy!"
created: 2025-07-03
updated: 2025-07-03
type: "docs/reference"
security: "L0"
version: "1.0.0"
document_id: "INT-REF-2025-426-L0"
tags: ["git", "reference", "commands", "cheatsheet", "printable"]
draft: false
author: ["Claude (AI)", "Comrade 47"]
---

# Git Command Reference Card for Revolutionary Organizers

*Print this card and keep it handy. 90% of organizing work uses these commands.*

**Learning Git?** See [[git-isnt-programming|Git Isn't Programming]] and [[git-in-7-commands|Git in 7 Commands]]

**Want visual guides?** Check [[visual-git-workflows|Visual Git Workflows]]

---

## THE ESSENTIAL SEVEN

### 1. `git status`
**See what's happening**
```bash
git status
# Shows: changed files, staged files, branch info
```

### 2. `git add`
**Stage changes for commit**
```bash
git add meeting-notes.md          # Add specific file
git add .                        # Add all changes
git add -p                       # Review changes interactively
```

### 3. `git commit`
**Save changes with message**
```bash
git commit -m "DECIDED[meeting](12-3-0): Launch rent strike"
git commit -am "Update meeting notes"  # Add + commit if files already tracked
```

### 4. `git push`
**Share changes with comrades**
```bash
git push                         # Push to default remote
git push origin main            # Push specific branch
git push --all                  # Push all branches
```

### 5. `git pull`
**Get latest changes**
```bash
git pull                         # Fetch and merge changes
git pull --rebase               # Cleaner history (advanced)
```

### 6. `git log`
**View history**
```bash
git log --oneline               # Compact view
git log --grep="DECIDED"        # Search decisions
git log --since="1 week ago"    # Recent changes
git log --author="ComradeAlex"  # Specific person's commits
```

### 7. `git clone`
**Copy repository**
```bash
git clone https://git.server.org/repo.git
git clone git@server.org:repo.git  # SSH version
```

---

## DAILY WORKFLOWS

### Starting Your Day
```bash
git pull                        # Get latest changes
git status                      # Check your workspace
```

### After A Meeting
```bash
git add meetings/2024-03-21-minutes.md
git commit -m "DOCUMENTED[secretary]: General meeting 2024-03-21"
git push
```

### Creating A Proposal
```bash
git checkout -b proposal/new-campaign
# Work on your proposal
git add proposal.md
git commit -m "PROPOSED[yourname]: New tenant organizing campaign"
git push origin proposal/new-campaign
```

### Reviewing Changes
```bash
git diff                        # See unstaged changes
git diff --staged              # See what will be committed
git show                       # See last commit
git show HEAD~3                # See 3 commits ago
```

---

## ORGANIZING-SPECIFIC COMMANDS

### Find Decisions
```bash
git log --grep="DECIDED" --oneline
git log --grep="EMERGENCY" --since="1 month ago"
```

### Track Campaign Work
```bash
git log -- campaigns/rent-strike/
git blame campaigns/strategy.md  # Who wrote each line
```

### Meeting History
```bash
git log -- meetings/ --oneline
git show meetings/2024-03-15-minutes.md
```

### Find Information
```bash
git grep "phone banking"        # Search all files
git log -S "union drive"        # Find when text was added
```

---

## BRANCHES FOR PROPOSALS

### Create New Proposal
```bash
git checkout -b proposal/description
git push -u origin proposal/description
```

### Switch Between Work
```bash
git branch                      # List branches
git checkout main              # Switch to main
git checkout proposal/name     # Switch to proposal
```

### Merge Approved Proposal
```bash
git checkout main
git merge proposal/description
git push
```

---

## EMERGENCY COMMANDS

### Undo Last Commit (NOT pushed)
```bash
git reset HEAD~1               # Undo commit, keep changes
git reset --hard HEAD~1        # Undo commit, discard changes
```

### Discard Local Changes
```bash
git checkout -- file.md        # Discard changes to file
git checkout -- .              # Discard all changes
```

### Emergency Backup
```bash
git push backup --all --force  # Push everything to backup remote
```

### See Deleted Content
```bash
git log --diff-filter=D --summary  # Find deleted files
git show <commit>:path/to/file     # View deleted file
```

---

## COMMIT MESSAGE FORMATS

### Standard Organizing Commits
```
DECIDED[body](vote): Description
ORGANIZED[who]: What was organized
DOCUMENTED[role]: What was documented
PROPOSED[author]: Proposal title
EMERGENCY[authority]: Urgent action
```

### Examples
```
DECIDED[general-meeting](15-2-1): Endorse transit strike
ORGANIZED[action-comm]: March route and permits secured
DOCUMENTED[secretary]: February financial report
PROPOSED[alice]: Switch to weekly meetings
EMERGENCY[security]: Rotate all passwords after breach
```

---

## SECURITY REMINDERS

### Before Every Commit
- [ ] No real names
- [ ] No addresses
- [ ] No phone numbers
- [ ] No workplace names
- [ ] Only pseudonyms

### Check What You're Committing
```bash
git diff --staged              # Review before commit
git status                     # See all changes
```

---

## COMMON PROBLEMS

### "Rejected push"
```bash
git pull                       # Get latest changes first
git push                       # Try again
```

### "Merge conflict"
```bash
# Edit conflicted files, then:
git add fixed-file.md
git commit -m "Resolved conflict in meeting notes"
```

### "Wrong branch"
```bash
git checkout correct-branch    # Switch to right branch
git cherry-pick <commit-id>   # Bring commit over
```

---

## LEARNING MORE

### Built-in Help
```bash
git help <command>             # Detailed help
git <command> -h              # Quick help
```

### Practice Commands
```bash
git log --graph --oneline     # Visualize history
git reflog                    # See everything you did
git stash                     # Temporarily save work
```

---

## QUICK WINS

**Your First Week**: Focus on status, add, commit, push, pull

**Week Two**: Add log and branches

**Week Three**: Learn diff and grep

**Month Two**: Everything else as needed

---

*Remember: Git is a tool for collective liberation. Every commit strengthens our organizational memory. Every push shares power with comrades.*

**Print double-sided and laminate for durability!**

**Ready to practice?** Start with [[your-first-revolutionary-commit|Your First Revolutionary Commit]]

**Teaching Git?** Use our [[git-through-campaign-template|Git Workshop Template]]