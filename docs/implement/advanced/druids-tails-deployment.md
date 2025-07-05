---
title: "DRUIDS-Tails Deployment Reference"
description: "Technical reference for deploying DRUIDS on Tails with hardware security keys"
created: 2025-07-04
updated: 2025-07-04
type: "docs/reference"
security: "L2"
version: "1.0.0"
document_id: "REF-SEC-2025-001-L2"
tags: ["tails", "deployment", "security", "hardware-keys", "reference"]
draft: true
author: ["Comrade 47"]
---

# DRUIDS-Tails Deployment Reference

*Secure, anonymous, hardware-authenticated infrastructure for revolutionary organizations*

## Overview

This reference documents the complete deployment process for DRUIDS on Tails OS with:
- Pre-configured Obsidian environment
- Hardware security key authentication (Yubikey/Feitian)
- Clone-once, deploy-many distribution model
- Three-tier trust architecture

## System Requirements

### Hardware
- **Master Build System**: Debian 12+ with 16GB RAM
- **USB Drives**: 32GB minimum, USB 3.0 recommended
- **Security Keys**: FIDO2-compatible (Yubikey 5, Feitian K9)

### Software Versions
- Tails: 6.15+
- Obsidian: Latest AppImage
- Git: 2.39+
- GnuPG: 2.2.40+

## Architecture Overview

```
┌─────────────────────────────────────────┐
│         MASTER TAILS BUILD              │
│  - Base Tails + Persistence             │
│  - Obsidian + Required Plugins          │
│  - Security Scripts & Documentation     │
└────────────┬────────────────────────────┘
             │ Clone Process
    ┌────────┴────────┬────────────────┐
    ▼                 ▼                ▼
┌─────────┐    ┌─────────┐     ┌─────────┐
│ USER 1  │    │ USER 2  │     │ USER N  │
│ USB+KEY │    │ USB+KEY │     │ USB+KEY │
└─────────┘    └─────────┘     └─────────┘
```

## Security Model

### Three Trust Paths

1. **Physical Distribution** (Convenient)
   - Pre-cloned USB with temporary passphrase
   - Hardware key shipped separately
   - User generates own keys on first boot
   - Risk: Supply chain trust

2. **Image Download** (Balanced)
   - Verified image with checksums
   - User writes own USB
   - Hardware key acquired independently
   - Risk: Download integrity

3. **DIY Bootstrap** (Secure)
   - Build from source
   - Full audit capability
   - Complete control
   - Risk: Technical complexity

### Key Security Properties

- **Forward Secrecy**: Compromised USB doesn't reveal past work
- **Key Isolation**: Hardware keys never touch persistent storage
- **Pseudonymous**: No real names in Git history
- **Amnesic Base**: Tails forgets everything not explicitly persisted

## Master Build Process

### 1. Create Base Tails USB

```bash
# Verify Tails image
gpg --keyid-format 0xlong --verify tails-amd64-*.img.sig

# Write to USB (replace sdX with actual device)
sudo dd if=tails-amd64-*.img of=/dev/sdX bs=16M oflag=direct status=progress
```

### 2. Configure Persistence

Boot Tails and enable:
- Persistent Folder
- GnuPG
- SSH Client
- Dotfiles
- Additional Software
- Network Connections

### 3. Install Core Software

```bash
# Core dependencies
sudo apt update
sudo apt install -y libfuse2 git curl libfido2-1 opensc \
                    pcscd scdaemon yubikey-manager pcsc-tools

# Obsidian (download via Tor Browser first)
mkdir -p ~/Persistent/Obsidian
mv ~/Tor\ Browser/Obsidian-*.AppImage ~/Persistent/Obsidian/
chmod +x ~/Persistent/Obsidian/*.AppImage
```

### 4. Configure Obsidian Plugins

Required plugins:
- Git (for version control)
- GPG Encrypt (for sensitive notes)
- Kanban (for task tracking)
- Dataview (for organizational queries)

### 5. Create Security Scripts

See [Scripts Section](#security-scripts) for complete scripts.

## Cloning & Distribution

### Cloning Process

```bash
# Using Tails Cloner
# 1. Boot master USB
# 2. Applications → Tails → Tails Cloner
# 3. Select "Clone current Tails"
# 4. Enable "Clone Persistent Storage"
# 5. Set unique passphrase per user
```

### Distribution Checklist

- [ ] USB in tamper-evident bag
- [ ] Hardware key in separate package
- [ ] Printed quick-start guide
- [ ] Temporary passphrase card (destroy after use)
- [ ] Emergency contact info

## First Boot Workflow

### User Setup Sequence

1. **Boot & Unlock**
   ```
   Enter temporary passphrase → Start Tails
   ```

2. **Generate Keys**
   ```bash
   ~/Persistent/scripts/create-gpg-key.sh
   ~/Persistent/scripts/create-ssh-keys-hardware.sh
   ```

3. **Configure Git**
   ```bash
   git config --global user.name "Comrade Pseudonym"
   git config --global user.email "pseudo@protonmail.com"
   git config --global user.signingkey $GPG_KEY_ID
   ```

4. **Change Passphrase**
   ```
   Applications → Tails → Persistent Storage → Change Passphrase
   ```

5. **Verify Setup**
   ```bash
   ssh -T git@github.com
   git clone git@github.com:org/test-repo.git
   ```

## Security Scripts

### Hardware Key SSH Generation

```bash
#!/bin/bash
# create-ssh-keys-hardware.sh
set -e

echo "=== Hardware Security Key SSH Setup ==="
echo "Insert your security key now."

# Try ed25519-sk first, fall back to ecdsa-sk
if ssh-keygen -t ed25519-sk -O resident -O verify-required \
              -C "$(date +%Y%m%d)" -f ~/.ssh/id_ed25519_sk; then
    echo "Created ed25519-sk key"
else
    ssh-keygen -t ecdsa-sk -O resident -O verify-required \
               -C "$(date +%Y%m%d)" -f ~/.ssh/id_ecdsa_sk
    echo "Created ecdsa-sk key"
fi

# Configure for GitHub
cat >> ~/.ssh/config << EOF
Host github.com
  IdentityFile ~/.ssh/id_*_sk
  IdentitiesOnly yes
EOF
```

### GPG Key Generation

```bash
#!/bin/bash
# create-gpg-key.sh
gpg --batch --gen-key <<EOF
Key-Type: RSA
Key-Length: 4096
Name-Real: $1
Name-Email: $2
Expire-Date: 2y
%commit
EOF
```

## Troubleshooting

### Common Issues

| Problem | Solution |
|---------|----------|
| Hardware key not detected | `sudo service pcscd restart` |
| Obsidian config lost | Check symlinks in `~/.obsidian` |
| Git auth fails | Verify `~/.ssh/config` |
| Persistence not mounting | Check `/live/persistence/TailsData_unlocked/` |

### Emergency Procedures

1. **Lost Hardware Key**
   - Revoke old SSH keys from all services
   - Generate new keys with replacement
   - Update all repo access

2. **Compromised USB**
   - Don't boot the USB
   - Report immediately
   - Prepare for key rotation

3. **Forgotten Passphrase**
   - No recovery possible
   - Request new USB
   - Regenerate all keys

## Maintenance

### Regular Tasks

- **Monthly**: Security updates via Additional Software
- **Quarterly**: Verify all plugins still work
- **Yearly**: Fresh rebuild of master image

### Update Distribution

```bash
# Create update package
tar -czf druids-update-$(date +%Y%m).tar.gz \
    ~/Persistent/scripts/ \
    ~/Persistent/Obsidian/plugins/

# Sign update
gpg --sign --armor druids-update-*.tar.gz
```

## Operational Security Notes

### DO
- Keep USB and hardware key separated when not in use
- Use different pseudonyms across organizations
- Regular security check-ins with your cell
- Backup critical data (encrypted) off-device

### DON'T
- Use real names in any configuration
- Connect to personal accounts from Tails
- Skip the passphrase change on first boot
- Share hardware keys between people

## Appendix: Plugin Configuration

### Git Plugin Settings
```json
{
  "commitMessage": "{{date}} {{hostname}}",
  "autoCommitInterval": 5,
  "autoPush": false,
  "disablePush": false
}
```

### GPG Encrypt Settings
```json
{
  "recipientKeyId": "AUTO_DETECT",
  "encryptByDefault": false,
  "fileExtension": ".gpg"
}
```

---

*This document is L2 security tier. Distribute only through secure channels.*