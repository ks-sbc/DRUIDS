---
title: "Complete Obsidian-Git Integration Setup Guide"
description: "Comprehensive guide for setting up Obsidian with Git integration for DRUIDS, including mobile setup and troubleshooting"
type: "how-to"
security: "L0"
document_id: "HTG-2025-889-L0"
version: "1.0.0"
tags: ["obsidian", "git", "setup", "installation", "mobile", "troubleshooting"]
---

# Complete Obsidian-Git Integration Setup Guide

## Overview

This guide provides comprehensive instructions for setting up Obsidian with Git integration, covering everything from initial installation to advanced troubleshooting. It's designed for organizers who want to use Obsidian as their primary interface for DRUIDS while maintaining full Git functionality.

## Prerequisites

- Basic computer literacy
- Obsidian installed (free from [[obsidian|obsidian.md]])
- Git installed on your system
- A Git repository (GitHub, GitLab, or self-hosted)

## Desktop Setup (Windows/Mac/Linux)

### Step 1: Install Required Software

#### Install Git

**Windows**:
```bash
# Download from https://git-scm.com/download/win
# Run installer with default options
# Verify installation:
git --version
```

**macOS**:
```bash
# Using Homebrew
brew install git

# Or download from https://git-scm.com/download/mac
# Verify:
git --version
```

**Linux**:
```bash
# Debian/Ubuntu
sudo apt update
sudo apt install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git

# Verify:
git --version
```

#### Install Obsidian

1. Download from [[obsidian|obsidian.md]]
2. Run installer for your platform
3. Launch Obsidian

### Step 2: Set Up Your Vault

#### Option A: Clone Existing Repository

```bash
# Navigate to where you want your vault
cd ~/Documents

# Clone your repository
git clone https://github.com/your-org/your-vault.git my-obsidian-vault

# Or using SSH (recommended for security)
git clone git@github.com:your-org/your-vault.git my-obsidian-vault
```

#### Option B: Create New Vault with Git

```bash
# Create vault directory
mkdir ~/Documents/my-obsidian-vault
cd ~/Documents/my-obsidian-vault

# Initialize Git
git init

# Create initial structure
mkdir -p .obsidian attachments templates
echo "# My DRUIDS Vault" > README.md

# Create .gitignore
cat > .gitignore << 'EOF'
# Obsidian cache and workspace
.obsidian/workspace*
.obsidian/cache
.obsidian/plugins/*/data.json
.trash/

# OS files
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.bak
~*

# Sensitive data (customize as needed)
secrets/
private/
EOF

# Initial commit
git add .
git commit -m "Initial vault setup"

# Add remote (replace with your repository URL)
git remote add origin https://github.com/your-org/your-vault.git
git push -u origin main
```

### Step 3: Install and Configure Obsidian-Git Plugin

#### Install the Plugin

1. Open Obsidian
2. Open Settings (gear icon)
3. Navigate to Community plugins
4. Click "Turn on community plugins"
5. Click "Browse" and search for "Obsidian Git"
6. Click "Install" then "Enable"

#### Configure Plugin Settings

1. Go to Settings → Community plugins → Obsidian Git
2. Configure these essential settings:

```yaml
# Auto backup
Vault backup interval (minutes): 15
Auto pull interval (minutes): 15
Commit message: "vault backup: {{date}}"
Auto backup after file change: true
Auto pull on startup: true

# Performance
Disable push: false
Pull before push: true

# Advanced
Show status bar: true
Disable BranchBar: false
```

### Step 4: Authentication Setup

#### SSH Keys (Recommended)

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your-email@example.com"

# Start SSH agent
eval "$(ssh-agent -s)"

# Add key to agent
ssh-add ~/.ssh/id_ed25519

# Copy public key
cat ~/.ssh/id_ed25519.pub
# Add this to your GitHub/GitLab SSH keys

# Test connection
ssh -T git@github.com
```

#### HTTPS with Credential Manager

**Windows**:
```bash
# Git Credential Manager is included with Git for Windows
git config --global credential.helper manager-core
```

**macOS**:
```bash
# Use keychain
git config --global credential.helper osxkeychain
```

**Linux**:
```bash
# Use libsecret
sudo apt install libsecret-1-0 libsecret-1-dev
git config --global credential.helper /usr/share/doc/git/contrib/credential/libsecret/git-credential-libsecret
```

### Step 5: Test Your Setup

1. Make a test change in Obsidian
2. Wait for auto-backup or use Ctrl/Cmd+P → "Obsidian Git: Commit all changes"
3. Check status bar for sync status
4. Verify on remote repository

## Mobile Setup (iOS/Android)

### iOS Setup with Working Copy

1. **Install Apps**:
   - Obsidian from App Store
   - Working Copy from App Store (Git client)

2. **Clone Repository in Working Copy**:
   - Open Working Copy
   - Tap "+" → "Clone repository"
   - Enter repository URL
   - Configure authentication

3. **Link to Obsidian**:
   - In Working Copy, tap repository
   - Tap "Share" → "Link Repository"
   - Choose "Obsidian"
   - Select folder location

4. **Setup Sync Workflow**:
   - Create iOS Shortcuts for:
     - Pull latest changes
     - Commit and push
   - Add to home screen for quick access

### Android Setup with Termux

1. **Install Apps**:
   - Obsidian from Play Store
   - Termux from F-Droid
   - Termux:API addon

2. **Setup Termux**:
```bash
# Update packages
pkg update && pkg upgrade

# Install Git
pkg install git openssh

# Setup storage access
termux-setup-storage

# Navigate to shared storage
cd /storage/emulated/0/Documents

# Clone repository
git clone https://github.com/your-org/your-vault.git
```

3. **Configure Obsidian**:
   - Open vault from Documents folder
   - Install Obsidian Git plugin
   - Note: Plugin has limited functionality on mobile

4. **Create Sync Scripts**:
```bash
# Create sync script
cat > ~/sync-vault.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
cd /storage/emulated/0/Documents/your-vault
git pull
git add .
git commit -m "Mobile sync: $(date)"
git push
EOF

chmod +x ~/sync-vault.sh

# Add to Termux:Widget for easy access
mkdir -p ~/.shortcuts
cp ~/sync-vault.sh ~/.shortcuts/
```

## Common Setup Issues and Solutions

### Issue: "Permission denied (publickey)"

**Solution**:
```bash
# Check SSH key is loaded
ssh-add -l

# If not, add it
ssh-add ~/.ssh/id_ed25519

# Ensure correct permissions
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

### Issue: "Failed to connect to repository"

**Solution**:
1. Check internet connection
2. Verify repository URL
3. Test Git outside Obsidian:
```bash
cd /path/to/vault
git remote -v
git fetch origin
```

### Issue: "Merge conflicts detected"

**Solution**:
1. Don't panic - your data is safe
2. Open conflicted files in Obsidian
3. Look for conflict markers:
```
<<<<<<< HEAD
Your version
=======
Remote version
>>>>>>> origin/main
```
4. Edit to keep desired content
5. Remove conflict markers
6. Commit resolution

### Issue: Plugin not working after Obsidian update

**Solution**:
1. Check for plugin updates
2. Disable and re-enable plugin
3. Clear Obsidian cache:
   - Settings → About → Clear cache
4. Reinstall plugin if needed

### Issue: Auto-backup not working

**Checklist**:
```bash
# 1. Check Git configuration
git config --list

# 2. Verify authentication works
git fetch

# 3. Check for uncommitted changes
git status

# 4. Review plugin console
# Ctrl+Shift+I → Console tab

# 5. Test manual commit
# Ctrl/Cmd+P → "Obsidian Git: Commit all changes"
```

## Advanced Configuration

### Multiple Vaults with Different Security Levels

```bash
# Create separate vaults
~/Documents/
├── druids-public/      # L0 - Public information
├── druids-internal/    # L1 - Internal only
└── druids-secure/      # L2 - Highly sensitive

# Each with own Git repository and branch strategy
```

### Custom Commit Messages

```javascript
// In .obsidian/plugins/obsidian-git/data.json
{
  "commitMessage": "{{date}} - {{hostname}} - {{numFiles}} files",
  "commitDateFormat": "YYYY-MM-DD HH:mm:ss",
  // ... other settings
}
```

### Pre-commit Hooks

```bash
# .git/hooks/pre-commit
#!/bin/bash

# Check for sensitive data
if git diff --cached | grep -E "(password|secret|private_key)" ; then
    echo "Error: Possible sensitive data detected"
    exit 1
fi

# Ensure no large files
find . -size +10M | grep -v .git | while read file; do
    if git diff --cached --name-only | grep -q "$file"; then
        echo "Error: Large file detected: $file"
        exit 1
    fi
done
```

### Sync Across Multiple Devices

```yaml
# Device-specific branches strategy
main                 # Protected, requires PR
devices/laptop       # Auto-push from laptop
devices/phone        # Auto-push from phone
devices/tablet       # Auto-push from tablet

# Merge via PR when ready
```

## Performance Optimization

### Large Vault Optimization

```bash
# Add to .gitignore
# Large files
*.pdf
*.mp4
*.zip

# Cache directories
.obsidian/cache/
.obsidian/workspace/

# Use Git LFS for large files
git lfs track "*.pdf"
git lfs track "*.png"
git lfs track "*.jpg"
```

### Reduce Sync Frequency for Battery

```yaml
# Mobile settings
Vault backup interval: 60  # Once per hour
Auto pull interval: 60     # Once per hour
Auto backup after file change: false
```

## Security Best Practices

### 1. Never Commit Sensitive Data

```bash
# Add to .gitignore
secrets/
passwords.md
*.key
*.pem
.env
```

### 2. Use Separate Vaults for Different Security Levels

```bash
# Public vault
git remote add origin https://github.com/org/public-notes.git

# Private vault (different repository)
git remote add origin git@private-server:org/secure-notes.git
```

### 3. Enable 2FA on Git Hosting

- GitHub: Settings → Security → Two-factor authentication
- GitLab: Settings → Account → Two-Factor Authentication
- Use hardware key when possible

### 4. Regular Security Audits

```bash
# Check for sensitive data in history
git log -p | grep -i "password\|secret\|key\|token"

# List large files
find .git/objects -size +5M

# Check commit authors
git log --format='%aN <%aE>' | sort -u
```

## Troubleshooting Flowchart

```
Problem with Obsidian-Git?
├─ Sync not working?
│  ├─ Check internet connection
│  ├─ Verify Git credentials
│  ├─ Test manual Git commands
│  └─ Review plugin settings
├─ Merge conflicts?
│  ├─ Pull latest changes
│  ├─ Resolve conflicts manually
│  └─ Commit resolution
├─ Performance issues?
│  ├─ Check vault size
│  ├─ Review .gitignore
│  ├─ Optimize sync frequency
│  └─ Consider Git LFS
└─ Security concerns?
   ├─ Audit commit history
   ├─ Check .gitignore
   ├─ Review access permissions
   └─ Enable 2FA
```

## Quick Reference Commands

```bash
# Daily operations
git status                    # Check current state
git pull                      # Get latest changes
git add .                     # Stage all changes
git commit -m "message"       # Commit changes
git push                      # Push to remote

# Troubleshooting
git log --oneline -10         # Recent commits
git diff                      # Unstaged changes
git diff --staged             # Staged changes
git remote -v                 # Check remotes
git config --list             # Check configuration

# Recovery
git reset --hard HEAD         # Discard all changes
git checkout -- file.md       # Discard file changes
git clean -fd                 # Remove untracked files
```

## Getting Help

- Plugin issues: [github.com/denolehov/obsidian-git/issues](https://github.com/denolehov/obsidian-git/issues)
- DRUIDS support: Check your organization's tech support channel
- Git help: `git help <command>`
- Community: Obsidian Discord server

Remember: Git is your safety net. Even if something goes wrong, your history is preserved and recoverable.