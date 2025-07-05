---
title: "DRUIDS Installation Guide"
description: "Step-by-step guide for installing and configuring DRUIDS infrastructure"
created: 2025-07-04
updated: 2025-07-04
type: "docs/how-to"
security: "L0"
version: "1.0.0"
document_id: "HOW-INSTALL-2025-001-L0"
tags: ["installation", "setup", "how-to", "deployment"]
draft: true
author: ["Comrade 47"]
---

# DRUIDS Installation Guide

*Get your revolutionary infrastructure running in under an hour*

**Prerequisites**: Review [why this matters](../../start/why-druids.md) and [see it in action](../../start/quick-demo.md) first.

**Different contexts?** Check [Visual Learning Paths](../../learn/visual-roadmaps.md) for installation paths by organizing type.

## Overview

This guide covers three installation paths:
1. **Quick Start** - Pre-built DRUIDS-Tails USB (15 minutes)
2. **Standard Install** - Existing system setup (45 minutes)
3. **Advanced Deploy** - Multi-org federation (2+ hours)

## Prerequisites

### Hardware Requirements

**Minimum**:
- 8GB RAM
- 32GB storage
- USB 3.0 port
- 64-bit processor

**Recommended**:
- 16GB RAM
- 128GB storage
- USB 3.1+ ports
- Hardware security key (Yubikey/Feitian)

### Knowledge Requirements

**Basic Path**: 
- Can follow instructions
- Comfortable with passwords
- Basic file management

**Advanced Path**:
- Command line basics
- Understanding of Git (see [Git essentials](../../learn/git-basics/git-in-7-commands.md))
- Network configuration

**Need to build skills first?** Start with [demystifying Git](../../learn/git-basics/git-isnt-programming.md) and [essential commands](../../learn/git-basics/git-in-7-commands.md).

## Path 1: Quick Start with DRUIDS-Tails

### Step 1: Obtain DRUIDS-Tails USB

**Option A: Request from Organization**
1. Contact your org's tech liaison
2. Verify distribution authenticity
3. Receive USB and hardware key

**Option B: Download and Create**
```bash
# Download verified image
wget https://druids.dev/releases/druids-tails-latest.iso
wget https://druids.dev/releases/druids-tails-latest.iso.sig

# Verify signature
gpg --verify druids-tails-latest.iso.sig

# Write to USB (replace sdX with your device)
sudo dd if=druids-tails-latest.iso of=/dev/sdX bs=16M status=progress
```

### Step 2: First Boot

1. **Insert USB and restart computer**
2. **Access boot menu** (Usually F12, F2, or Esc)
3. **Select USB device**
4. **At Tails Greeter**:
   - Enter temporary passphrase
   - Enable persistent storage
   - Start Tails

### Step 3: Initial Configuration

The welcome wizard launches automatically:

1. **Security Setup**
   ```
   - Create new GPG key
   - Configure hardware security key
   - Generate SSH keys
   - Change persistent storage passphrase
   ```

2. **Identity Configuration**
   ```
   - Set Git pseudonym
   - Configure email (use ProtonMail/Tutanota)
   - Set organizational identifier
   ```

3. **Vault Initialization**
   ```
   - Choose vault location
   - Set encryption preferences
   - Configure sync method
   ```

### Step 4: Verify Installation

```bash
# Check DRUIDS components
druids-status

# Expected output:
# ✓ Tails: 6.15
# ✓ DRUIDS: 0.1.0
# ✓ Obsidian: 1.4.16
# ✓ Git: 2.39.2
# ✓ GPG: 2.2.40
# ✓ Persistent Storage: Unlocked
# ✓ Network: Tor Connected
```

## Path 2: Standard Installation on Existing System

### Supported Systems

- Debian 12+
- Ubuntu 22.04+
- Fedora 38+
- Arch Linux (current)
- Tails 6.0+

### Step 1: Install Core Dependencies

**Debian/Ubuntu**:
```bash
sudo apt update
sudo apt install -y git gnupg2 curl wget age \
    syncthing obsidian tor torsocks
```

**Fedora**:
```bash
sudo dnf install -y git gnupg2 curl wget age \
    syncthing tor torsocks
# Install Obsidian separately
```

**Arch**:
```bash
sudo pacman -S git gnupg curl wget age \
    syncthing tor torsocks
yay -S obsidian-bin
```

### Step 2: Install DRUIDS Scripts

```bash
# Clone DRUIDS repository
git clone https://github.com/druids-dev/druids-core.git
cd druids-core

# Run installer
./install.sh --path=$HOME/.druids
```

### Step 3: Configure Security Tiers

```bash
# Initialize DRUIDS
druids init

# Configure security tiers
druids security setup

# Choose your model:
# 1. Single-user (personal organizing)
# 2. Small cell (2-10 members)
# 3. Organization (10+ members)
# 4. Federation (multiple orgs)
```

### Step 4: Obsidian Configuration

1. **Launch Obsidian**
2. **Open vault**: Choose `$HOME/.druids/vault`
3. **Install community plugins**:
   - Git
   - Obsidian GPG
   - Kanban
   - Dataview
   - Tasks

4. **Configure Git plugin**:
   ```
   - Repository path: .
   - Commit message: {{date}} {{hostname}}
   - Auto-commit: 5 minutes
   - Push on commit: No (security)
   ```

### Step 5: Syncing Setup

**Option A: Syncthing (Recommended)**
```bash
# Start Syncthing
systemctl --user enable syncthing
systemctl --user start syncthing

# Access web UI
firefox http://localhost:8384

# Add devices using their IDs
# Share .druids/vault folder
```

**Option B: Git Remote (Advanced)**
```bash
# Add encrypted remote
git remote add origin tor://your-onion-address.onion/vault.git

# Configure push through Tor
git config --global http.proxy socks5h://127.0.0.1:9050
```

## Path 3: Advanced Multi-Org Deployment

### Architecture Overview

```
┌─────────────────┐     ┌─────────────────┐
│   Org Node A    │────│   Org Node B    │
│  (10 members)   │    │  (15 members)   │
└────────┬────────┘    └────────┬────────┘
         │                      │
         └──────────┬───────────┘
                    │
            ┌───────┴────────┐
            │ Federation Hub │
            │  (Shared L1)   │
            └────────────────┘
```

### Step 1: Deploy Infrastructure Node

```bash
# On dedicated server (VPS or local)
wget https://druids.dev/releases/druids-server-latest.tar.gz
tar -xzf druids-server-latest.tar.gz
cd druids-server

# Configure as federation hub
./deploy.sh --mode=federation \
            --name="Regional Hub" \
            --security=L1 \
            --port=7744
```

### Step 2: Organization Setup

For each organization:

```bash
# Initialize org node
druids org init --name="Tenant Union Local 47" \
                --hub=tor://federation-address.onion:7744 \
                --members=15

# Generate org keys
druids org keygen --type=master
druids org keygen --type=member --count=15

# Create member USBs
druids org create-media --template=druids-tails \
                       --count=15 \
                       --output=/media/batch/
```

### Step 3: Network Configuration

```bash
# Configure Tor hidden service
sudo nano /etc/tor/torrc

# Add:
HiddenServiceDir /var/lib/tor/druids/
HiddenServicePort 7744 127.0.0.1:7744

# Restart Tor
sudo systemctl restart tor

# Get onion address
sudo cat /var/lib/tor/druids/hostname
```

### Step 4: Security Hardening

```bash
# Enable firewall
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 7744/tcp comment "DRUIDS Federation"
sudo ufw enable

# Configure fail2ban
sudo cp druids-server/config/fail2ban/druids.conf /etc/fail2ban/filter.d/
sudo systemctl restart fail2ban

# Set up monitoring
druids monitor enable --alerts=email \
                     --threshold=3 \
                     --contact=security@org.dev
```

## Post-Installation

### Essential First Steps

1. **Create First Documents**
   ```bash
   # Meeting template
   druids new meeting --date=today
   
   # Security policy
   druids new document --template=security-policy
   
   # Member roster (encrypted)
   druids new roster --encrypt=L2
   ```

2. **Test Sync**
   ```bash
   # Create test file
   echo "Test sync $(date)" > vault/test-sync.md
   
   # Commit and sync
   druids sync
   
   # Verify on other device
   druids pull
   ```

3. **Security Verification**
   ```bash
   # Run security audit
   druids security audit
   
   # Check encryption
   druids security verify-encryption
   
   # Test recovery
   druids security test-recovery
   ```

### Training Resources

After installation, work through:
1. [Onboarding Without Burnout](../../learn/tutorials/onboarding-without-burnout.md)
2. [Daily Workflows](../../learn/git-basics/daily-git-workflows.md)
3. [Security Playbook](../../implement/security/security-playbook.md)

### Common Issues

| Problem | Solution |
|---------|----------|
| "Cannot find vault" | Run `druids vault init` |
| "Sync failed" | Check `druids sync status` |
| "Permission denied" | Verify GPG key: `druids security check` |
| "Tor not connected" | `sudo systemctl restart tor` |

## Maintenance

### Daily
```bash
# Quick status check
druids status
```

### Weekly
```bash
# Sync verification
druids sync verify

# Backup check
druids backup status
```

### Monthly
```bash
# Security audit
druids security audit --full

# Update components
druids update --check
```

## Getting Help

1. **Documentation**: `/docs` in your vault
2. **Logs**: `druids logs --tail=50`
3. **Debug mode**: `druids --debug [command]`
4. **Community**: Via secure channels only

---

*Installation is just the beginning. The revolution requires practice.*