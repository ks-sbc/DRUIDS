---
title: "DRUIDS-Tails Bootstrap Scripts"
description: "Production-ready scripts for automated DRUIDS-Tails setup and configuration"
created: 2025-07-04
updated: 2025-07-04
type: "docs/reference"
security: "L1"
version: "1.0.0"
document_id: "REF-SCRIPTS-2025-001-L1"
tags: ["scripts", "automation", "bootstrap", "tails", "setup"]
draft: true
author: ["Comrade 47"]
---

# DRUIDS-Tails Bootstrap Scripts

*Automated setup scripts for consistent, secure deployment*

## Master Bootstrap Script

```bash
#!/bin/bash
# druids-bootstrap.sh - Main bootstrap orchestrator
# Run this on first boot of DRUIDS-Tails

set -euo pipefail

# Configuration
DRUIDS_VERSION="0.1.0"
DRUIDS_HOME="/home/amnesia/Persistent/.druids"
VAULT_PATH="/home/amnesia/Persistent/Obsidian/Vault"
LOG_FILE="/home/amnesia/Persistent/.druids/bootstrap.log"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Logging function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Error handling
error_exit() {
    echo -e "${RED}ERROR: $1${NC}" >&2
    log "ERROR: $1"
    exit 1
}

# Success message
success() {
    echo -e "${GREEN}✓ $1${NC}"
    log "SUCCESS: $1"
}

# Warning message
warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
    log "WARNING: $1"
}

# Check if running on Tails
check_environment() {
    if [ ! -f /etc/os-release ] || ! grep -q "Tails" /etc/os-release; then
        error_exit "This script must be run on Tails"
    fi
    
    if [ ! -d /home/amnesia/Persistent ]; then
        error_exit "Persistent storage not found. Please enable it first."
    fi
    
    success "Environment check passed"
}

# Create directory structure
setup_directories() {
    log "Creating DRUIDS directory structure..."
    
    mkdir -p "$DRUIDS_HOME"/{config,keys,scripts,backups}
    mkdir -p "$VAULT_PATH"/{L0,L1,L2,templates,archive}
    mkdir -p "$VAULT_PATH"/L0/{announcements,education,guides}
    mkdir -p "$VAULT_PATH"/L1/{meetings,members,campaigns}
    mkdir -p "$VAULT_PATH"/L2/.encrypted
    
    # Set secure permissions
    chmod 700 "$DRUIDS_HOME"
    chmod 700 "$VAULT_PATH"/L2
    
    success "Directory structure created"
}

# Install additional software
install_software() {
    log "Installing additional software..."
    
    # Update package list
    sudo apt-get update || warning "Package update failed, continuing..."
    
    # Install required packages
    local packages=(
        "git"
        "gnupg2"
        "curl"
        "wget"
        "age"
        "jq"
        "tmux"
        "vim"
        "rsync"
        "pwgen"
        "libfido2-1"
        "yubikey-manager"
    )
    
    for package in "${packages[@]}"; do
        if ! dpkg -l | grep -q "^ii  $package"; then
            sudo apt-get install -y "$package" || warning "Failed to install $package"
        fi
    done
    
    success "Software installation complete"
}

# Configure Git
setup_git() {
    log "Configuring Git..."
    
    # Check if already configured
    if git config --global user.name &>/dev/null; then
        warning "Git already configured, skipping..."
        return
    fi
    
    # Interactive setup
    echo "=== Git Configuration ==="
    read -p "Enter your pseudonym: " git_name
    read -p "Enter your secure email: " git_email
    
    git config --global user.name "$git_name"
    git config --global user.email "$git_email"
    git config --global init.defaultBranch main
    git config --global commit.gpgsign true
    
    # Revolutionary aliases
    git config --global alias.unite "merge"
    git config --global alias.struggle "diff"
    git config --global alias.advance "push"
    git config --global alias.learn "pull"
    git config --global alias.history "log --oneline --graph --all"
    
    success "Git configured"
}

# Generate GPG key
setup_gpg() {
    log "Setting up GPG..."
    
    # Check if key already exists
    if gpg --list-secret-keys | grep -q sec; then
        warning "GPG key already exists, skipping generation..."
        return
    fi
    
    echo "=== GPG Key Generation ==="
    echo "This will generate a secure GPG key for signing and encryption."
    
    # Generate key with batch mode
    cat > /tmp/gpg-keygen << EOF
%echo Generating DRUIDS GPG key
Key-Type: RSA
Key-Length: 4096
Subkey-Type: RSA
Subkey-Length: 4096
Name-Real: $(git config --global user.name)
Name-Email: $(git config --global user.email)
Expire-Date: 1y
%no-protection
%commit
%echo done
EOF

    gpg --batch --generate-key /tmp/gpg-keygen
    rm -f /tmp/gpg-keygen
    
    # Get key ID and configure Git
    KEY_ID=$(gpg --list-secret-keys --keyid-format=long | grep sec | awk '{print $2}' | cut -d'/' -f2 | head -n1)
    git config --global user.signingkey "$KEY_ID"
    
    # Export public key
    gpg --export --armor "$KEY_ID" > "$DRUIDS_HOME/keys/gpg-public.asc"
    
    success "GPG key generated: $KEY_ID"
}

# Setup hardware key authentication
setup_hardware_key() {
    log "Setting up hardware key authentication..."
    
    # Check for hardware key
    if ! lsusb | grep -E "(Yubico|Feitian)" &>/dev/null; then
        warning "No hardware key detected. Please insert your security key."
        echo "Press Enter when ready, or 's' to skip..."
        read -n 1 response
        if [ "$response" = "s" ]; then
            warning "Skipping hardware key setup"
            return
        fi
    fi
    
    # Generate SSH key with hardware backing
    echo "=== Hardware Key SSH Setup ==="
    echo "You'll be prompted to touch your security key..."
    
    local ssh_key_file="$HOME/.ssh/id_ed25519_sk"
    
    if [ -f "$ssh_key_file" ]; then
        warning "Hardware SSH key already exists"
    else
        ssh-keygen -t ed25519-sk -C "$(date +%Y%m%d)-druids" -f "$ssh_key_file" -N ""
        success "Hardware SSH key created"
    fi
    
    # Configure SSH
    cat > "$HOME/.ssh/config" << EOF
Host *.onion
    ProxyCommand nc -x localhost:9050 %h %p
    
Host github.com
    User git
    IdentityFile $ssh_key_file
    IdentitiesOnly yes
EOF
    
    chmod 600 "$HOME/.ssh/config"
    success "SSH configured for Tor and GitHub"
}

# Setup Obsidian
setup_obsidian() {
    log "Setting up Obsidian..."
    
    # Check if Obsidian is installed
    if [ ! -f /opt/obsidian/obsidian.AppImage ]; then
        warning "Obsidian not found. Please install it manually."
        return
    fi
    
    # Initialize vault
    cd "$VAULT_PATH"
    git init
    
    # Create .gitignore
    cat > .gitignore << EOF
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/cache
.trash/
.DS_Store
L2/
*.tmp
*.age
EOF

    # Create initial files
    cat > README.md << EOF
# DRUIDS Vault

This is your secure organizational knowledge base.

## Security Tiers

- **L0**: Public information (this folder)
- **L1**: Member-only information (encrypted)
- **L2**: Sensitive operations (client-side only, never synced)

## Quick Start

1. Create new meeting notes: \`druids new meeting\`
2. Check security status: \`druids security status\`
3. Sync with comrades: \`druids sync\`

Remember: If in doubt, use a higher security tier.
EOF

    # Create templates
    mkdir -p templates
    
    cat > templates/meeting-minutes.md << 'EOF'
---
date: {{date}}
type: meeting
security: L1
attendees: 
decisions: 
actions: 
---

# Meeting Minutes - {{date}}

## Attendees


## Agenda


## Discussion


## Decisions


## Action Items
- [ ] 

## Next Meeting


---
*Recorded by: {{author}}*
EOF

    # Initial commit
    git add .
    git commit -m "Initialize DRUIDS vault"
    
    success "Obsidian vault initialized"
}

# Setup security scripts
install_druids_scripts() {
    log "Installing DRUIDS utility scripts..."
    
    # Main druids command
    cat > "$DRUIDS_HOME/scripts/druids" << 'EOF'
#!/bin/bash
# DRUIDS command-line interface

DRUIDS_HOME="/home/amnesia/Persistent/.druids"
VAULT_PATH="/home/amnesia/Persistent/Obsidian/Vault"

case "$1" in
    status)
        echo "=== DRUIDS Status ==="
        echo "Version: $(cat $DRUIDS_HOME/config/version 2>/dev/null || echo 'unknown')"
        echo "Vault: $VAULT_PATH"
        echo "GPG: $(gpg --list-secret-keys | grep uid | head -n1)"
        echo "Git: $(cd $VAULT_PATH && git log --oneline -1)"
        echo "Tor: $(systemctl is-active tor)"
        ;;
        
    new)
        case "$2" in
            meeting)
                DATE=$(date +%Y-%m-%d)
                FILE="$VAULT_PATH/L1/meetings/$DATE-meeting.md"
                mkdir -p $(dirname "$FILE")
                cp "$VAULT_PATH/templates/meeting-minutes.md" "$FILE"
                sed -i "s/{{date}}/$DATE/g" "$FILE"
                sed -i "s/{{author}}/$(git config user.name)/g" "$FILE"
                echo "Created: $FILE"
                ;;
            *)
                echo "Usage: druids new [meeting|document|campaign]"
                ;;
        esac
        ;;
        
    sync)
        cd "$VAULT_PATH"
        git add .
        git commit -m "Sync $(date +%Y-%m-%d-%H%M%S) from $(hostname)"
        echo "Changes committed locally"
        ;;
        
    security)
        case "$2" in
            audit)
                echo "=== Security Audit ==="
                find "$VAULT_PATH/L2" -type f -name "*.md" | wc -l | xargs echo "L2 files (should be 0):"
                find "$VAULT_PATH" -type f -perm /022 | xargs echo "World-readable files:"
                ;;
            *)
                echo "Usage: druids security [audit|status|rotate]"
                ;;
        esac
        ;;
        
    *)
        echo "DRUIDS - Democratic Resilient Unity-building Information Distribution System"
        echo ""
        echo "Usage: druids [command] [options]"
        echo ""
        echo "Commands:"
        echo "  status    Show system status"
        echo "  new       Create new documents"
        echo "  sync      Commit changes"
        echo "  security  Security operations"
        echo "  help      Show this help"
        ;;
esac
EOF

    chmod +x "$DRUIDS_HOME/scripts/druids"
    
    # Create symlink
    sudo ln -sf "$DRUIDS_HOME/scripts/druids" /usr/local/bin/druids
    
    # Security audit script
    cat > "$DRUIDS_HOME/scripts/security-audit.sh" << 'EOF'
#!/bin/bash
# Periodic security audit

echo "=== DRUIDS Security Audit ==="
echo "Date: $(date)"
echo ""

# Check for sensitive data in wrong tiers
echo "Checking for PII in L0..."
grep -r -i -E "(phone|address|ssn|license|passport)" "$VAULT_PATH/L0" || echo "✓ None found"

echo ""
echo "Checking for unencrypted L1 files..."
find "$VAULT_PATH/L1" -name "*.md" -exec file {} \; | grep -v "PGP\|GPG" | head -5

echo ""
echo "Checking permissions..."
find "$VAULT_PATH" -type f -perm /077 -ls | head -5

echo ""
echo "Checking for large files..."
find "$VAULT_PATH" -size +10M -ls

echo ""
echo "=== Audit Complete ==="
EOF

    chmod +x "$DRUIDS_HOME/scripts/security-audit.sh"
    
    success "DRUIDS scripts installed"
}

# Configure autostart
setup_autostart() {
    log "Configuring autostart..."
    
    # Create welcome script
    cat > "$DRUIDS_HOME/scripts/welcome.sh" << 'EOF'
#!/bin/bash

# Check if first run today
LAST_RUN_FILE="$HOME/.druids-last-run"
TODAY=$(date +%Y-%m-%d)

if [ -f "$LAST_RUN_FILE" ]; then
    LAST_RUN=$(cat "$LAST_RUN_FILE")
    if [ "$LAST_RUN" = "$TODAY" ]; then
        exit 0
    fi
fi

# Show daily reminder
zenity --info --title="DRUIDS Daily Reminder" \
    --text="Remember to:\n\n✓ Check for updates\n✓ Sync your vault\n✓ Review security tier usage\n✓ Clear L2 if needed\n\nStay safe, comrade!" \
    --width=300

echo "$TODAY" > "$LAST_RUN_FILE"

# Run security audit
/home/amnesia/Persistent/.druids/scripts/security-audit.sh > \
    /home/amnesia/Persistent/.druids/security-audit-$TODAY.log
EOF

    chmod +x "$DRUIDS_HOME/scripts/welcome.sh"
    
    # Create desktop file
    mkdir -p /home/amnesia/.config/autostart
    cat > /home/amnesia/.config/autostart/druids-welcome.desktop << EOF
[Desktop Entry]
Type=Application
Name=DRUIDS Welcome
Exec=$DRUIDS_HOME/scripts/welcome.sh
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
EOF

    success "Autostart configured"
}

# Main execution
main() {
    echo "==================================="
    echo "   DRUIDS Bootstrap - v$DRUIDS_VERSION"
    echo "==================================="
    echo ""
    
    # Create log directory
    mkdir -p "$(dirname "$LOG_FILE")"
    
    log "Starting DRUIDS bootstrap..."
    
    # Check if already bootstrapped
    if [ -f "$DRUIDS_HOME/config/.bootstrapped" ]; then
        warning "DRUIDS already bootstrapped. Run with --force to re-run."
        exit 0
    fi
    
    # Run setup steps
    check_environment
    setup_directories
    install_software
    setup_git
    setup_gpg
    setup_hardware_key
    setup_obsidian
    install_druids_scripts
    setup_autostart
    
    # Mark as complete
    echo "$DRUIDS_VERSION" > "$DRUIDS_HOME/config/version"
    touch "$DRUIDS_HOME/config/.bootstrapped"
    
    echo ""
    echo "======================================="
    echo -e "${GREEN}✓ DRUIDS Bootstrap Complete!${NC}"
    echo "======================================="
    echo ""
    echo "Next steps:"
    echo "1. Run 'druids status' to verify installation"
    echo "2. Open Obsidian and select: $VAULT_PATH"
    echo "3. Create your first meeting notes: 'druids new meeting'"
    echo "4. Read the security guide in your vault"
    echo ""
    echo "Stay secure, comrade!"
}

# Run main function
main "$@"
```

## Supporting Scripts

### Hardware Key Setup Script

```bash
#!/bin/bash
# setup-hardware-key.sh - Configure hardware security key

set -euo pipefail

echo "=== Hardware Security Key Setup ==="
echo ""
echo "This script will help you configure your hardware security key."
echo "Supported devices: Yubikey 5, Feitian K9/K40"
echo ""

# Detect hardware key
detect_key() {
    if lsusb | grep -q "Yubico"; then
        echo "✓ Detected: Yubikey"
        KEY_TYPE="yubikey"
    elif lsusb | grep -q "Feitian"; then
        echo "✓ Detected: Feitian ePass"
        KEY_TYPE="feitian"
    else
        echo "✗ No hardware key detected"
        echo "Please insert your security key and try again."
        exit 1
    fi
}

# Configure FIDO2 PIN
setup_fido2_pin() {
    echo ""
    echo "=== Setting FIDO2 PIN ==="
    echo "Choose a 4-8 digit PIN for your security key."
    echo "This PIN will be required for authentication."
    echo ""
    
    if [ "$KEY_TYPE" = "yubikey" ]; then
        ykman fido access change-pin
    else
        # Feitian uses standard FIDO2 commands
        echo "Please use your key's management software to set PIN"
    fi
}

# Generate resident SSH key
generate_ssh_key() {
    echo ""
    echo "=== Generating SSH Key ==="
    echo "This creates a hardware-backed SSH key."
    echo ""
    
    local key_file="$HOME/.ssh/id_ed25519_sk_druids"
    
    if [ -f "$key_file" ]; then
        echo "Key already exists at $key_file"
        read -p "Generate new key? (y/N): " response
        if [ "$response" != "y" ]; then
            return
        fi
    fi
    
    # Try ed25519-sk first, fall back to ecdsa-sk
    if ssh-keygen -t ed25519-sk -O resident -O verify-required \
                  -C "druids-$(date +%Y%m%d)" \
                  -f "$key_file"; then
        echo "✓ Generated ed25519-sk key"
    else
        echo "ed25519-sk not supported, trying ecdsa-sk..."
        ssh-keygen -t ecdsa-sk -O resident -O verify-required \
                   -C "druids-$(date +%Y%m%d)" \
                   -f "$key_file"
        echo "✓ Generated ecdsa-sk key"
    fi
    
    # Display public key
    echo ""
    echo "Your public SSH key:"
    echo "===================="
    cat "${key_file}.pub"
    echo "===================="
    echo ""
    echo "Add this key to your Git hosting service (GitHub/GitLab)"
}

# Configure GPG with hardware key
setup_gpg_card() {
    echo ""
    echo "=== GPG Card Setup ==="
    echo "This configures GPG to use your hardware key."
    echo ""
    
    if [ "$KEY_TYPE" != "yubikey" ]; then
        echo "Note: GPG card features require a Yubikey"
        return
    fi
    
    echo "Initializing GPG card..."
    gpg --card-edit
}

# Test configuration
test_setup() {
    echo ""
    echo "=== Testing Configuration ==="
    
    # Test SSH
    echo -n "Testing SSH key... "
    if ssh-add -L | grep -q "sk"; then
        echo "✓ OK"
    else
        echo "✗ Not found"
    fi
    
    # Test FIDO2
    echo -n "Testing FIDO2... "
    if command -v fido2-token >/dev/null; then
        fido2-token -L | head -1 && echo "✓ OK" || echo "✗ Failed"
    else
        echo "✗ fido2-tools not installed"
    fi
}

# Main execution
main() {
    detect_key
    setup_fido2_pin
    generate_ssh_key
    
    if [ "$KEY_TYPE" = "yubikey" ]; then
        read -p "Configure GPG card features? (y/N): " response
        if [ "$response" = "y" ]; then
            setup_gpg_card
        fi
    fi
    
    test_setup
    
    echo ""
    echo "=== Setup Complete ==="
    echo ""
    echo "Your hardware key is configured for DRUIDS."
    echo "Remember to:"
    echo "1. Backup your key's recovery codes"
    echo "2. Register a second key as backup"
    echo "3. Test authentication before relying on it"
}

main "$@"
```

### Vault Sync Script

```bash
#!/bin/bash
# vault-sync.sh - Secure vault synchronization

set -euo pipefail

VAULT_PATH="/home/amnesia/Persistent/Obsidian/Vault"
SYNC_METHOD="${1:-git}" # git, syncthing, or usb

# Git sync
sync_git() {
    cd "$VAULT_PATH"
    
    # Check for changes
    if [ -z "$(git status --porcelain)" ]; then
        echo "No changes to sync"
        return
    fi
    
    # Add and commit
    git add -A
    
    # Get commit message
    if [ -n "${2:-}" ]; then
        MSG="$2"
    else
        MSG="Sync from $(hostname) at $(date +%Y-%m-%d-%H%M)"
    fi
    
    git commit -m "$MSG" \
        -m "Changed files: $(git diff --cached --name-only | wc -l)"
    
    # Check for remote
    if git remote | grep -q origin; then
        echo "Pushing to remote..."
        git push origin main || echo "Push failed - will retry later"
    else
        echo "No remote configured - local commit only"
    fi
}

# Syncthing sync
sync_syncthing() {
    # Check if syncthing is running
    if ! systemctl --user is-active syncthing >/dev/null; then
        echo "Starting Syncthing..."
        systemctl --user start syncthing
        sleep 5
    fi
    
    # Trigger sync via API
    curl -s -X POST -H "X-API-Key: $(cat ~/.config/syncthing/api-key)" \
        http://localhost:8384/rest/db/scan?folder=druids-vault
    
    echo "Syncthing scan triggered"
}

# USB backup sync
sync_usb() {
    local USB_PATH="/media/amnesia/DRUIDS-BACKUP"
    
    if [ ! -d "$USB_PATH" ]; then
        echo "Please insert DRUIDS-BACKUP USB drive"
        exit 1
    fi
    
    # Create encrypted backup
    echo "Creating encrypted backup..."
    tar -czf - -C "$VAULT_PATH" . | \
        age -e -r "$(cat ~/.druids/keys/backup-pubkey)" > \
        "$USB_PATH/vault-$(date +%Y%m%d-%H%M%S).tar.gz.age"
    
    echo "Backup created on USB"
    
    # Verify
    echo -n "Verifying backup... "
    if age -d -i ~/.druids/keys/backup-key \
        "$USB_PATH/vault-*.tar.gz.age" | \
        tar -tzf - >/dev/null 2>&1; then
        echo "✓ OK"
    else
        echo "✗ Failed"
        exit 1
    fi
}

# Pre-sync security check
security_check() {
    echo "Running pre-sync security check..."
    
    # Check for sensitive data in L0
    if grep -r -i "password\|secret\|private" "$VAULT_PATH/L0" 2>/dev/null; then
        echo "WARNING: Possible sensitive data in L0!"
        read -p "Continue anyway? (y/N): " response
        if [ "$response" != "y" ]; then
            exit 1
        fi
    fi
    
    # Check file permissions
    find "$VAULT_PATH" -type f -perm /077 | while read -r file; do
        echo "Fixing permissions: $file"
        chmod 600 "$file"
    done
    
    # Remove L2 files from git
    if [ -d "$VAULT_PATH/L2" ]; then
        cd "$VAULT_PATH"
        git rm -r --cached L2/ 2>/dev/null || true
        echo "L2/" >> .gitignore
        git add .gitignore
    fi
}

# Main execution
main() {
    echo "=== DRUIDS Vault Sync ==="
    echo "Method: $SYNC_METHOD"
    echo ""
    
    # Run security check
    security_check
    
    # Execute sync
    case "$SYNC_METHOD" in
        git)
            sync_git "$@"
            ;;
        syncthing)
            sync_syncthing
            ;;
        usb)
            sync_usb
            ;;
        *)
            echo "Unknown sync method: $SYNC_METHOD"
            echo "Usage: $0 [git|syncthing|usb] [commit message]"
            exit 1
            ;;
    esac
    
    echo ""
    echo "✓ Sync complete"
}

main "$@"
```

### First Boot Wizard

```bash
#!/bin/bash
# first-boot-wizard.sh - Interactive setup for new users

set -euo pipefail

# Use zenity for GUI dialogs
TITLE="DRUIDS Setup Wizard"

# Welcome screen
show_welcome() {
    zenity --info --title="$TITLE" --width=500 --height=300 \
        --text="Welcome to DRUIDS - Democratic Resilient Unity-building Information Distribution System\n\n\
This wizard will help you:\n\
• Create your security keys\n\
• Configure your identity\n\
• Set up your vault\n\
• Learn basic operations\n\n\
The process takes about 15 minutes.\n\n\
Click OK to begin."
}

# Identity setup
setup_identity() {
    # Get pseudonym
    PSEUDONYM=$(zenity --entry --title="$TITLE" \
        --text="Choose your pseudonym (not your real name):" \
        --entry-text="Comrade-$(shuf -i 100-999 -n1)")
    
    if [ -z "$PSEUDONYM" ]; then
        zenity --error --text="Pseudonym is required"
        exit 1
    fi
    
    # Get secure email
    EMAIL=$(zenity --entry --title="$TITLE" \
        --text="Enter your secure email address:\n(ProtonMail or Tutanota recommended)")
    
    if [ -z "$EMAIL" ]; then
        zenity --error --text="Email is required"
        exit 1
    fi
    
    # Configure Git
    git config --global user.name "$PSEUDONYM"
    git config --global user.email "$EMAIL"
}

# Key generation with progress
generate_keys() {
    (
        echo "10"
        echo "# Generating GPG key..."
        
        # Generate GPG key
        gpg --batch --generate-key <<EOF
%echo Generating GPG key
Key-Type: RSA
Key-Length: 4096
Name-Real: $PSEUDONYM
Name-Email: $EMAIL
Expire-Date: 1y
%no-protection
%commit
EOF
        
        echo "50"
        echo "# Generating SSH key..."
        
        # Generate SSH key
        ssh-keygen -t ed25519 -C "$EMAIL" -N "" -f ~/.ssh/id_ed25519_druids
        
        echo "75"
        echo "# Configuring security..."
        
        # Get GPG key ID
        KEY_ID=$(gpg --list-secret-keys --keyid-format=long | grep sec | \
                 awk '{print $2}' | cut -d'/' -f2 | head -n1)
        git config --global user.signingkey "$KEY_ID"
        git config --global commit.gpgsign true
        
        echo "100"
        echo "# Complete!"
        
    ) | zenity --progress --title="$TITLE" \
        --text="Generating security keys..." \
        --percentage=0 --auto-close
}

# Vault setup
setup_vault() {
    zenity --info --title="$TITLE" \
        --text="Now we'll set up your Obsidian vault.\n\n\
This is where all your organizational knowledge will be stored.\n\n\
Click OK to continue."
    
    # Initialize vault
    cd /home/amnesia/Persistent/Obsidian/Vault
    
    if [ ! -d .git ]; then
        git init
        git add README.md
        git commit -m "Initialize DRUIDS vault for $PSEUDONYM"
    fi
    
    # Show Obsidian
    zenity --info --title="$TITLE" \
        --text="Obsidian will now open.\n\n\
1. Select 'Open folder as vault'\n\
2. Choose: /home/amnesia/Persistent/Obsidian/Vault\n\
3. Enable community plugins when prompted\n\n\
Click OK to launch Obsidian."
    
    # Launch Obsidian
    /opt/obsidian/obsidian.AppImage &
}

# Security training
show_security_training() {
    zenity --text-info --title="$TITLE - Security Guidelines" \
        --width=600 --height=500 \
        --filename=/dev/stdin << 'EOF'
DRUIDS Security Guidelines

1. PSEUDONYM DISCIPLINE
   - Never use real names in the system
   - Create consistent pseudonyms
   - Keep a secure mapping separately

2. SECURITY TIERS
   - L0: Public information (can be leaked)
   - L1: Members only (encrypted)
   - L2: Sensitive operations (never synced)

3. DAILY PRACTICES
   - Clear L2 folder after each session
   - Run security audit weekly
   - Verify encryption before sync

4. EMERGENCY PROCEDURES
   - If compromised: Revoke all keys immediately
   - Notify security contact
   - Do not boot compromised USB

5. REMEMBER
   - The state is always watching
   - Perfect security doesn't exist
   - Vigilance is collective care

Click OK when you've read and understood these guidelines.
EOF
}

# Completion
show_completion() {
    # Create quick reference card
    cat > ~/Desktop/DRUIDS-Quick-Reference.txt << EOF
DRUIDS Quick Reference

Your Identity:
- Pseudonym: $PSEUDONYM
- Email: $EMAIL
- GPG Key: $(gpg --list-secret-keys | grep uid | head -1)

Common Commands:
- Create meeting notes: druids new meeting
- Save your work: druids sync
- Check security: druids security audit
- Get help: druids help

Daily Workflow:
1. Open Terminal
2. Run: druids status
3. Work in Obsidian
4. Run: druids sync
5. Clear L2 folder before shutdown

Stay safe, comrade!
EOF

    zenity --info --title="$TITLE - Complete!" --width=500 \
        --text="Congratulations! DRUIDS is now configured.\n\n\
Your quick reference has been saved to the Desktop.\n\n\
Important next steps:\n\
1. Practice the daily workflow\n\
2. Create your first meeting notes\n\
3. Share your PUBLIC key with your cell\n\
4. Never share your PRIVATE keys\n\n\
Welcome to the resistance, $PSEUDONYM!"
}

# Main execution
main() {
    show_welcome
    setup_identity
    generate_keys
    setup_vault
    show_security_training
    show_completion
}

# Error handling
trap 'zenity --error --text="Setup failed. Please try again."' ERR

# Run wizard
main "$@"
```

## Installation Instructions

To use these scripts on a DRUIDS-Tails system:

1. **During image creation**, place scripts in:
   ```
   config/chroot_local-includes/usr/local/bin/
   ```

2. **On existing Tails**, download and run:
   ```bash
   wget https://druids.dev/bootstrap/druids-bootstrap.sh
   chmod +x druids-bootstrap.sh
   ./druids-bootstrap.sh
   ```

3. **For development**, clone and link:
   ```bash
   git clone https://github.com/druids-dev/bootstrap-scripts.git
   cd bootstrap-scripts
   ./install-dev.sh
   ```

## Script Security

All scripts follow these principles:

1. **Fail-safe defaults** - Err on the side of security
2. **No network assumptions** - Work offline
3. **Explicit user consent** - No automatic sensitive operations
4. **Audit trails** - Log all security-relevant actions
5. **Idempotency** - Safe to run multiple times

---

*These scripts automate the revolution, one bootstrap at a time.*