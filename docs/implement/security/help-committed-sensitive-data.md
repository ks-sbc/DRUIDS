---
title: "Help, I Committed Sensitive Data! Emergency Recovery Guide"
description: "Emergency procedures for removing sensitive information from Git history while preserving democratic accountability"
created: 2025-07-03
updated: 2025-07-03
type: "docs/how-to"
security: "L1"
version: "1.0.0"
document_id: "INT-HT-2025-421-L1"
tags: ["security", "emergency", "git-rebase", "sensitive-data", "recovery"]
draft: false
author: ["Claude (AI)", "Comrade 47"]
---

# Help, I Committed Sensitive Data! Emergency Recovery Guide

## STOP! Don't Panic, Don't Push

If you just committed sensitive data, **DO NOT PUSH TO THE REMOTE REPOSITORY**. If you already pushed, skip to the "Already Pushed" section immediately.

## Quick Assessment

What got committed? This determines urgency:

### CRITICAL (Act within minutes):
- Government names
- Home addresses  
- Phone numbers
- Social Security Numbers
- Bank/financial info
- Unencrypted passwords

### HIGH (Act within hours):
- Workplace names
- License plates
- Email addresses
- Meeting locations
- Tactical plans

### MEDIUM (Act within day):
- Pseudonym connections
- Internal debates
- Resource amounts
- Partner organizations

## Quick Decision Flowchart

```
Did you push to remote?
├─ NO → Have you made other commits after?
│   ├─ NO → Use Option 1: Amend
│   └─ YES → Use Option 2: Interactive Rebase
│
└─ YES → Is the repo public?
    ├─ YES → EMERGENCY PROTOCOL
    │   ├─ Contact security team NOW
    │   ├─ Document in security incident
    │   └─ Coordinate democratic rewrite
    │
    └─ NO → How many people have access?
        ├─ < 10 → Coordinate quick rewrite
        └─ > 10 → Full democratic process
```

## If You Haven't Pushed Yet

### Option 1: Amend the Last Commit (Simplest)

If the sensitive data is ONLY in your last commit:

```bash
# 1. Remove or fix the sensitive file
nano sensitive-file.txt  # Delete the sensitive parts

# 2. Stage the fix
git add sensitive-file.txt

# 3. Amend the commit (keeps same message)
git commit --amend

# 4. Verify the sensitive data is gone
git show HEAD
```

### Option 2: Interactive Rebase (Multiple Commits)

If sensitive data is in recent commits:

```bash
# 1. Start interactive rebase for last 5 commits
git rebase -i HEAD~5

# 2. In the editor, change 'pick' to 'edit' 
# for commits with sensitive data

# 3. Git will stop at each 'edit' commit
# Fix the files, then:
git add fixed-file.txt
git commit --amend
git rebase --continue

# 4. Repeat for each problematic commit
```

### Option 3: Remove Entire File from History (filter-branch)

If a file should never have been committed:

```bash
# Remove file from all history
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/to/sensitive-file" \
  --prune-empty --tag-name-filter cat -- --all

# Clean up
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

### Option 4: BFG Repo Cleaner (Faster Alternative)

BFG is simpler and faster than filter-branch for removing sensitive data:

```bash
# 1. Install BFG (if not installed)
# macOS: brew install bfg
# Linux: Download from https://rtyley.github.io/bfg-repo-cleaner/

# 2. Clone a fresh copy (BFG works on bare repos)
git clone --mirror git@github.com:your-org/repo.git

# 3. Remove sensitive data patterns
# Remove files by name:
bfg --delete-files sensitive-file.txt repo.git

# Remove text from all files:
bfg --replace-text passwords.txt repo.git

# Where passwords.txt contains:
# PASSWORD1==>REMOVED
# secret-key==>REMOVED
# real-name==>REDACTED

# 4. Clean up the repo
cd repo.git
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# 5. Push the cleaned history
git push --force
```

### Option 5: Nuclear Option - Start Fresh

When history is too compromised or complex:

```bash
# 1. Export current state (no history)
git archive --format=tar HEAD > current-state.tar

# 2. Create new repo
cd ..
mkdir repo-clean
cd repo-clean
git init

# 3. Import clean state
tar -xf ../current-state.tar
git add .
git commit -m "Initial commit - clean history after security incident"

# 4. Push to new remote (after democratic decision)
git remote add origin git@github.com:your-org/repo-clean.git
git push -u origin main
```

## If You Already Pushed

### 1. Immediate Damage Control

```bash
# Contact your security point person IMMEDIATELY
# They need to know:
# - What was exposed
# - When it was pushed  
# - Who has repo access
# - Whether it's public/private
```

### 2. Document the Decision

This requires collective decision because rewriting public history affects everyone:

```bash
# Create security incident record
mkdir -p security/incidents/$(date +%Y)
cat > security/incidents/$(date +%Y)/$(date +%Y%m%d)-data-exposure.md << EOF
# Security Incident: Sensitive Data Exposure

**Date**: $(date)
**Severity**: CRITICAL/HIGH/MEDIUM
**Discovered by**: [Your pseudonym]

## What Was Exposed
- [Specific data types]
- [Affected comrades]
- [Commits involved]

## Immediate Actions Taken
- [ ] Notified security committee
- [ ] Contacted affected comrades
- [ ] Assessed downstream exposure

## Collective Decision Required
Rewriting public history requires democratic decision.
Calling emergency security meeting.
EOF
```

### 3. Coordinate the Rewrite

After democratic approval:

```bash
# 1. Everyone must pull before you rewrite
# Send urgent message: "FREEZE ALL PUSHES - SECURITY INCIDENT"

# 2. Perform the rewrite (same as local methods above)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/to/sensitive-file" \
  --prune-empty --tag-name-filter cat -- --all

# 3. Force push (requires consensus!)
git push origin --force --all
git push origin --force --tags

# 4. Everyone must re-clone or reset
# Send instructions to all members
```

## Emergency Communication Protocol

### Secure Notification Template

```
SECURITY ALERT - ACTION REQUIRED

Severity: [CRITICAL/HIGH/MEDIUM]
Action needed by: [time]

A security incident requires us to rewrite Git history.

DO NOT PUSH until further notice.

Instructions:
1. Note any uncommitted work
2. Wait for all-clear signal
3. Follow reset instructions when sent

Details in Signal group.
```

### Reset Instructions for Other Members

After rewrite is complete:

```bash
# For other members to sync after rewrite
# Option 1: Fresh clone (safest)
cd ..
mv repo-name repo-name-backup
git clone [repo-url]

# Option 2: Hard reset (if they have no local changes)
git fetch origin
git reset --hard origin/main
git clean -fd
```

## Verification Steps

### After Local Cleanup

```bash
# 1. Verify file is gone from all commits
git log --all --full-history -- path/to/sensitive-file
# Should return nothing

# 2. Search for sensitive strings in history
git grep "sensitive-string" $(git rev-list --all)
# Should return nothing

# 3. Check file isn't in any branch
git branch -a --contains $(git hash-object path/to/sensitive-file)
# Should return nothing

# 4. Verify object is truly gone
git fsck --full --unreachable
# Run garbage collection
git gc --prune=now --aggressive
```

### After Remote Cleanup

```bash
# 1. Fresh clone to verify
cd /tmp
git clone git@github.com:your-org/repo.git verify-clean
cd verify-clean

# 2. Search entire history
git log --all --full-history -p | grep -i "sensitive-pattern"
# Should return nothing

# 3. Check all branches
for branch in $(git branch -r | grep -v HEAD); do
  echo "Checking $branch"
  git checkout $branch
  grep -r "sensitive-pattern" .
done
```

## Preventing Future Incidents

### Pre-Commit Hooks

Install this comprehensive hook to catch sensitive data:

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Color codes for output
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# More comprehensive patterns
declare -A patterns=(
  ["SSN"]="[0-9]{3}-[0-9]{2}-[0-9]{4}"
  ["Phone"]="(\+?1[-.\s]?)?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}"
  ["Email"]="[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"
  ["Credit Card"]="[0-9]{4}[-\s]?[0-9]{4}[-\s]?[0-9]{4}[-\s]?[0-9]{4}"
  ["API Key"]="(api[_-]?key|apikey|api_secret)[\s]*[:=][\s]*['\"]?[A-Za-z0-9]{20,}['\"]?"
  ["Password"]="(password|passwd|pwd)[\s]*[:=][\s]*['\"]?[^\s'\"]{8,}['\"]?"
  ["Private Key"]="-----BEGIN (RSA |DSA |EC |OPENSSH )?PRIVATE KEY-----"
  ["AWS Key"]="AKIA[0-9A-Z]{16}"
  ["Street Address"]="[0-9]{1,5}\s+[A-Za-z\s]{4,50}\s+(Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|Circle|Cir|Plaza|Pl)"
)

# Files to check
files=$(git diff --cached --name-only --diff-filter=AM)

if [ -z "$files" ]; then
  exit 0
fi

found_issues=0

for file in $files; do
  # Skip binary files
  if file "$file" | grep -q "binary"; then
    continue
  fi
  
  for pattern_name in "${!patterns[@]}"; do
    pattern="${patterns[$pattern_name]}"
    if git diff --cached "$file" | grep -E "$pattern" > /dev/null; then
      echo -e "${RED}[BLOCKED]${NC} Possible $pattern_name found in $file"
      echo -e "${YELLOW}Pattern:${NC} $pattern"
      echo "Review your changes and remove sensitive data before committing."
      ((found_issues++))
    fi
  done
done

# Check for files that shouldn't be committed
dangerous_files=(
  ".env"
  ".env.local"
  ".env.production"
  "secrets.yml"
  "secrets.yaml"
  "credentials"
  "id_rsa"
  "id_dsa"
  "id_ecdsa"
  "*.pem"
  "*.key"
  "*.p12"
  "*.pfx"
)

for file in $files; do
  for dangerous in "${dangerous_files[@]}"; do
    if ["$file" == $dangerous]("$file" == $dangerous.md); then
      echo -e "${RED}[BLOCKED]${NC} Attempting to commit dangerous file: $file"
      echo "Add this file to .gitignore instead."
      ((found_issues++))
    fi
  done
done

if [ $found_issues -gt 0 ]; then
  echo -e "\n${RED}Commit blocked:${NC} $found_issues security issues found."
  echo "Fix these issues and try again."
  exit 1
fi

# Make hook executable
chmod +x .git/hooks/pre-commit
```

### Security Checklist

Before every commit:

- [ ] No government names
- [ ] No personal addresses
- [ ] No phone numbers  
- [ ] No workplace details
- [ ] No unmasked locations
- [ ] No financial information
- [ ] Only organizing pseudonyms

## Lessons from Real Incidents

### Case 1: Meeting Minutes Disaster
**What happened**: Secretary committed raw meeting notes with everyone's full names
**Impact**: 30 comrades exposed
**Response**: Emergency rewrite within 2 hours
**Lesson**: Always use pseudonyms, even in notes

### Case 2: Screenshot With Address
**What happened**: Strategy map screenshot included organizer's home address
**Impact**: One comrade had to relocate  
**Response**: Immediate rewrite, security assessment
**Lesson**: Always review images for metadata/content

### Case 3: Debug Log With Database
**What happened**: Developer committed debug log with database passwords
**Impact**: Had to rotate all credentials
**Response**: Rewrite plus full security audit
**Lesson**: Never commit logs, use .gitignore

## Democratic Rewrite Protocol

Rewriting history is serious. It requires:

1. **Immediate notification** of security committee
2. **Assessment** of exposure and impact
3. **Democratic decision** on response
4. **Coordinated action** to minimize disruption
5. **Post-incident review** to prevent recurrence

Template motion for emergency meeting:

```markdown
## Emergency Motion: Security Rewrite

**Situation**: Sensitive data committed to repository
**Exposed**: [Specific data]
**Risk Assessment**: [Immediate dangers]

**Proposed Action**: 
1. Freeze all repository activity
2. Rewrite history to remove exposure
3. Force push clean history
4. All members re-sync repositories

**Vote Required**: Emergency security protocol allows 
security committee to act with 3 member approval.

[ ] Approve emergency rewrite
[ ] Deny - seek alternatives
[ ] Abstain
```

## Technical Details

### Understanding Git's Object Model

When you commit sensitive data:

```
Working Directory → Staging Area → Local Repo → Remote Repo
     (edit)           (add)         (commit)      (push)
```

Each stage requires different recovery methods:
- **Working Directory**: Just edit the file
- **Staging Area**: Use `git reset`
- **Local Repo**: Use `git commit --amend` or rebase
- **Remote Repo**: Requires force push after local cleanup

### Why Rebase Is Necessary

Git's content-addressed storage means:
- Every commit has a unique SHA based on content
- Child commits reference parent SHAs
- Changing any commit changes all subsequent SHAs
- This is why everyone must re-sync after rewrite

## Remember

1. **Speed matters** - Government names exposed for hours can destroy lives
2. **Democracy matters** - Rewriting shared history requires consent
3. **Prevention matters** - Every incident is a learning opportunity
4. **Solidarity matters** - We protect each other from our mistakes

The revolutionary movement has a long history of security breaches from simple mistakes. DRUIDS gives us tools to recover. Use them wisely, democratically, and quickly when needed.

*"In the sphere of security, as in every other sphere, we can only learn by our mistakes."* - Lenin

Learn, recover, and strengthen security culture for next time.

## Common Gotchas and Edge Cases

### Pull Requests and Forks

**Problem**: Sensitive data in a PR from a fork
**Solution**: 
```bash
# 1. Close the PR immediately
# 2. Contact the fork owner to clean their repo
# 3. Even after cleaning, GitHub may cache PR diffs
# 4. Contact GitHub support if critical data exposed
```

### Git Submodules

**Problem**: Sensitive data in a submodule
**Solution**:
```bash
# Clean both the submodule AND parent repo
# 1. Clean submodule repository first
cd path/to/submodule
# Run cleanup procedures

# 2. Update submodule reference in parent
cd ../..
git submodule update --remote
git add path/to/submodule
git commit -m "Update submodule after security cleanup"
```

### Large Files and Git LFS

**Problem**: Sensitive data in LFS-tracked files
**Solution**:
```bash
# BFG handles LFS, but filter-branch doesn't
# Use BFG or manually clean:
git lfs untrack sensitive-file
git rm --cached sensitive-file
git add .gitattributes
git commit -m "Remove sensitive LFS file"
# Then run history cleanup
```

### CI/CD and Automated Systems

**Problem**: CI systems may have cached the sensitive data
**Actions Required**:
- Clear CI build caches
- Rotate any credentials that CI had access to
- Check if CI logs contain sensitive data
- Update CI to pull fresh after rewrite

### Archived/Tagged Releases

**Problem**: Sensitive data in tagged releases
**Solution**:
```bash
# Delete and recreate tags after cleanup
git tag -d v1.0.0
git push origin :refs/tags/v1.0.0
# After cleanup:
git tag v1.0.0
git push origin v1.0.0
```

### Remember These Edge Cases

1. **GitHub/GitLab cache PR diffs** even after force push
2. **Webhooks may have sent** the sensitive commit data
3. **Git reflog keeps references** for 90 days by default
4. **Mirrors and backups** may have the old history
5. **IDE local history** might retain sensitive files
6. **Shell history** might contain sensitive commands

Always assume data is compromised if it touched any external system.