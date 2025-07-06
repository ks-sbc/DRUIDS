---
title: "Git History Scrubbing Guide"
description: "Comprehensive guide for removing sensitive information from Git history"
type: "how-to"
security: "L1"
document_id: "SEC-HTG-2025-001-L1"
version: "1.0.0"
tags: ["security", "git", "privacy", "remediation", "critical"]
---

# Git History Scrubbing Guide

> **⚠️ WARNING**: These procedures rewrite Git history. This is a destructive operation that requires coordination with all team members. Always backup before proceeding.

## When to Use This Guide

You need Git history scrubbing when:

- Real names appear in commit authors
- Personal email addresses are exposed
- Sensitive information was committed (passwords, keys, personal data)
- Accidental commits to wrong security tier
- Privacy audit reveals historical exposure

## Prerequisites

### 1. Full Backup

```bash
# Create complete backup
cd /path/to/repo
tar -czf repo-backup-$(date +%Y%m%d).tar.gz .

# Or clone to backup location
git clone --mirror . ../repo-backup-$(date +%Y%m%d)
```

### 2. Team Coordination

- **Notify all contributors** - They'll need to re-clone
- **Set maintenance window** - No commits during cleanup
- **Document what's being removed** - For verification

### 3. Install BFG Repo-Cleaner

```bash
# Download BFG (faster than git-filter-branch)
wget https://repo1.maven.org/maven2/com/madgag/bfg/1.14.0/bfg-1.14.0.jar

# Verify Java is installed
java --version
```

## Method 1: BFG Repo-Cleaner (Recommended)

BFG is faster and simpler than git-filter-branch for most cases.

### Remove Names from Commit Authors

1. **Create mailmap file** mapping old names to pseudonyms:

```bash
cat > mailmap.txt << EOF
YourPseudonym <member@ksbc.org> Real Name <personal@email.com>
ComradeTwo <member@ksbc.org> Another Name <their@email.com>
EOF
```

2. **Run BFG to update authors**:

```bash
java -jar bfg-1.14.0.jar \
  --convert-to-git-lfs '*.{pdf,doc,docx}' \
  --replace-text mailmap.txt \
  --no-blob-protection \
  repo.git
```

### Remove Sensitive Files

```bash
# Remove specific file from all history
java -jar bfg-1.14.0.jar --delete-files secret-file.txt repo.git

# Remove files by pattern
java -jar bfg-1.14.0.jar --delete-files '*.key' repo.git

# Remove folders
java -jar bfg-1.14.0.jar --delete-folders .credentials repo.git
```

### Replace Text in Files

1. **Create replacements file**:

```bash
cat > replacements.txt << EOF
personal.email@example.com==>member@ksbc.org
"John Smith"==>[REDACTED]
555-123-4567==>[PHONE-REDACTED]
Password123!==>***REMOVED***
EOF
```

2. **Run replacement**:

```bash
java -jar bfg-1.14.0.jar --replace-text replacements.txt repo.git
```

### Clean Repository

After BFG operations:

```bash
cd repo.git
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

## Method 2: git-filter-branch (Complex Cases)

For cases BFG can't handle, use git-filter-branch.

### Change All Author Emails/Names

```bash
git filter-branch --env-filter '
OLD_EMAIL="personal@email.com"
NEW_NAME="YourPseudonym"
NEW_EMAIL="member@ksbc.org"

if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]; then
    export GIT_COMMITTER_NAME="$NEW_NAME"
    export GIT_COMMITTER_EMAIL="$NEW_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]; then
    export GIT_AUTHOR_NAME="$NEW_NAME"
    export GIT_AUTHOR_EMAIL="$NEW_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags
```

### Remove Specific Commits

```bash
# Find commit with sensitive data
git log --oneline --all -- sensitive-file.txt

# Remove specific commit
git filter-branch --commit-filter '
    if [ "$GIT_COMMIT" = "abc123def456" ]; then
        skip_commit "$@";
    else
        git commit-tree "$@";
    fi' HEAD
```

### Remove File from All History

```bash
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch path/to/sensitive-file' \
  --prune-empty --tag-name-filter cat -- --all
```

## Method 3: git-filter-repo (Modern Alternative)

Newer and faster than git-filter-branch.

### Install

```bash
pip install git-filter-repo
```

### Use Cases

```bash
# Change email/name
git filter-repo --mailmap mailmap.txt

# Remove file
git filter-repo --path sensitive-file.txt --invert-paths

# Replace text
git filter-repo --replace-text replacements.txt
```

## Verification Steps

### 1. Check Authors

```bash
# List all historical authors
git log --format="%an <%ae>" | sort | uniq

# Verify no real names remain
git log --format="%an <%ae>" | grep -i "john\|smith\|real"
```

### 2. Search Content

```bash
# Search all history for sensitive strings
git grep "personal@email.com" $(git rev-list --all)

# Check for phone numbers
git grep -E "[0-9]{3}-[0-9]{3}-[0-9]{4}" $(git rev-list --all)
```

### 3. Verify File Removal

```bash
# Ensure file is gone from all commits
git log --all --oneline -- removed-file.txt
```

## Force Push & Team Coordination

### 1. Force Push to Remote

```bash
# This rewrites remote history!
git push origin --force --all
git push origin --force --tags
```

### 2. Team Instructions

Send this to all team members:

```
URGENT: Git History Rewritten

We've cleaned sensitive data from our repository history.
You MUST re-clone the repository:

1. Backup any uncommitted work
2. Delete your local repository
3. Re-clone fresh:
   git clone [repository-url]
4. Re-apply any local changes

DO NOT pull/merge from your old local copy - it will 
reintroduce the removed data!
```

## Common Pitfalls & Solutions

### Pitfall 1: Incomplete Removal

**Problem**: Sensitive data still visible in some commits
**Solution**: Run verification steps thoroughly, check all branches

### Pitfall 2: Team Member Pushes Old History

**Problem**: Someone pulls/pushes from old clone
**Solution**:

- Lock repository during cleanup
- Use branch protection rules
- Monitor for reintroduction

### Pitfall 3: Forks and Mirrors

**Problem**: Forks still contain sensitive data
**Solution**:

- Contact fork owners
- Request DMCA takedown if necessary
- Monitor for re-exposure

### Pitfall 4: Cached Views

**Problem**: GitHub/GitLab still shows old data
**Solution**:

- Contact support for cache clearing
- May take 24-48 hours to fully propagate

## Emergency Response Procedure

If sensitive data is currently exposed:

### 1. Immediate Actions (First 15 minutes)

```bash
# Make repository private (if possible)
# GitHub: Settings → Danger Zone → Change visibility

# Remove sensitive file immediately
git rm sensitive-file
git commit -m "Emergency removal"
git push

# This doesn't remove history but stops bleeding
```

### 2. Communication (First hour)

- Notify security team
- Alert affected members
- Document exposure timeline

### 3. Cleanup (First 24 hours)

- Follow full scrubbing procedure
- Verify complete removal
- Re-enable repository access

## Recovery Procedures

### If Something Goes Wrong

1. **Restore from backup**:

```bash
# If you have mirror backup
cd /path/to/new/location
git clone --mirror ../repo-backup-20250630

# If you have tarball
tar -xzf repo-backup-20250630.tar.gz
```

2. **Restore specific commits**:

```bash
# Find lost commits in reflog
git reflog

# Cherry-pick needed commits
git cherry-pick abc123
```

3. **Contact Git hosting support**:

- GitHub: <support@github.com>
- GitLab: Open support ticket
- Request restoration from their backups

## Prevention Best Practices

1. **Pre-commit hooks**: Install check-no-names.sh
2. **Regular audits**: Run privacy-audit.sh weekly
3. **Education**: Ensure all members read pseudonym guide
4. **Git configuration**: Template for new contributors
5. **Review process**: Check new contributor's first commits

## Quick Command Reference

```bash
# Backup
git clone --mirror . ../backup

# BFG - Remove file
java -jar bfg.jar --delete-files secret.txt repo.git

# BFG - Replace text
java -jar bfg.jar --replace-text replacements.txt repo.git

# Filter-branch - Change author
git filter-branch --env-filter 'export GIT_AUTHOR_NAME="NewName"'

# Verify authors
git log --format="%an <%ae>" | sort | uniq

# Force push
git push --force --all

# Clean repository
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

---

*Remember: Git history rewriting is serious. When in doubt, make another backup.*
