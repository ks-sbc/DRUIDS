---
title: "Custom DRUIDS-Tails Image Creation - Technical Deep Dive"
description: "Comprehensive technical guide for creating custom Tails images with DRUIDS branding and modifications"
created: 2025-07-04
updated: 2025-07-04
type: "docs/reference"
security: "L2"
version: "1.0.0"
document_id: "REF-TECH-2025-002-L2"
tags: ["tails", "customization", "technical", "image-building", "branding"]
draft: true
author: ["Comrade 47"]
---

# Custom DRUIDS-Tails Image Creation - Technical Deep Dive

*The complete technical guide to building custom Tails images with revolutionary aesthetics*

## Overview

This guide covers creating a fully customized Tails image with:
- Custom boot splash screens and GRUB themes
- Modified desktop environment (GNOME) aesthetics
- Pre-installed software and configurations
- Automated setup scripts
- Reproducible build process

## Prerequisites

### Build Environment

```bash
# Debian 12 build system with:
- 32GB+ RAM (for building in tmpfs)
- 100GB+ free disk space
- KVM virtualization support
- Fast internet (downloading packages)

# Required packages
sudo apt install -y \
    git vagrant virtualbox vagrant-libvirt \
    vmdebootstrap live-build rsync \
    syslinux syslinux-utils isolinux \
    xorriso mtools dosfstools squashfs-tools
```

## Understanding Tails Build System

### Architecture Overview

```
tails/
├── config/                 # Live-build configuration
│   ├── chroot_local-includes/    # Files to include in image
│   ├── chroot_local-hooks/       # Scripts run during build
│   ├── binary_local-includes/    # Files for ISO (not persistence)
│   └── binary_local-hooks/       # ISO customization scripts
├── features/              # Cucumber tests
├── vagrant/               # Build VM definitions
└── Rakefile              # Build orchestration
```

## Step 1: Clone and Prepare Tails Source

```bash
# Clone official Tails repository
git clone https://gitlab.tails.boum.org/tails/tails.git
cd tails

# Checkout stable version (adjust version as needed)
git checkout tails-6.15

# Create custom branch
git checkout -b druids-custom
```

## Step 2: Aesthetic Customizations

### 2.1 Boot Splash (Plymouth Theme)

Create custom Plymouth theme:

```bash
# Create theme directory
mkdir -p config/chroot_local-includes/usr/share/plymouth/themes/druids

# Create theme script
cat > config/chroot_local-includes/usr/share/plymouth/themes/druids/druids.script << 'EOF'
# DRUIDS Plymouth Theme
Window.SetBackgroundTopColor(0.1, 0.1, 0.1);
Window.SetBackgroundBottomColor(0.0, 0.0, 0.0);

# Load logo
logo.image = Image("druids-logo.png");
logo.sprite = Sprite(logo.image);

# Center logo
logo.sprite.SetX(Window.GetX() + (Window.GetWidth() - logo.image.GetWidth()) / 2);
logo.sprite.SetY(Window.GetY() + (Window.GetHeight() - logo.image.GetHeight()) / 2);

# Progress bar
progress_box.image = Image("progress_box.png");
progress_box.sprite = Sprite(progress_box.image);
progress_box.sprite.SetX(Window.GetX() + (Window.GetWidth() - progress_box.image.GetWidth()) / 2);
progress_box.sprite.SetY(logo.sprite.GetY() + logo.image.GetHeight() + 20);

progress_bar.image = Image("progress_bar.png");
progress_bar.sprite = Sprite();

fun progress_callback(progress) {
    progress_bar.image = progress_bar.image.Scale(progress_box.image.GetWidth() * progress, progress_bar.image.GetHeight());
    progress_bar.sprite.SetImage(progress_bar.image);
    progress_bar.sprite.SetX(progress_box.sprite.GetX());
    progress_bar.sprite.SetY(progress_box.sprite.GetY());
}

Plymouth.SetBootProgressFunction(progress_callback);
EOF

# Create theme configuration
cat > config/chroot_local-includes/usr/share/plymouth/themes/druids/druids.plymouth << 'EOF'
[Plymouth Theme]
Name=DRUIDS
Description=Democratic Resilient Unity-building Information Distribution System
ModuleName=script

[script]
ImageDir=/usr/share/plymouth/themes/druids
ScriptFile=/usr/share/plymouth/themes/druids/druids.script
EOF
```

Add your images:
```bash
# Copy your logo and progress bar images
cp /path/to/druids-logo.png config/chroot_local-includes/usr/share/plymouth/themes/druids/
cp /path/to/progress_*.png config/chroot_local-includes/usr/share/plymouth/themes/druids/
```

### 2.2 GRUB Theme Customization

```bash
# Create GRUB theme directory
mkdir -p config/chroot_local-includes/boot/grub/themes/druids

# Create theme.txt
cat > config/chroot_local-includes/boot/grub/themes/druids/theme.txt << 'EOF'
# DRUIDS GRUB Theme
title-text: "DRUIDS Secure Boot"
title-font: "DejaVu Sans Bold 16"
title-color: "#FF0000"
desktop-image: "background.png"
desktop-color: "#000000"

# Boot menu styling
+ boot_menu {
  left = 15%
  top = 20%
  width = 70%
  height = 60%
  
  item_font = "DejaVu Sans Regular 12"
  item_color = "#CCCCCC"
  selected_item_color = "#FFFFFF"
  selected_item_pixmap_style = "select_*.png"
  
  item_height = 32
  item_padding = 8
  item_spacing = 4
}

# Progress bar
+ progress_bar {
  id = "__timeout__"
  left = 15%
  top = 85%
  width = 70%
  height = 16
  
  fg_color = "#FF0000"
  bg_color = "#333333"
  border_color = "#FFFFFF"
}
EOF

# Copy theme assets
cp /path/to/background.png config/chroot_local-includes/boot/grub/themes/druids/
cp /path/to/select_*.png config/chroot_local-includes/boot/grub/themes/druids/
```

### 2.3 GNOME Desktop Customization

Create GNOME customization script:

```bash
cat > config/chroot_local-hooks/99-druids-gnome-customize << 'EOF'
#!/bin/sh
set -e

# DRUIDS GNOME Customizations

# Create custom GNOME Shell theme
mkdir -p /usr/share/themes/DRUIDS/gnome-shell
cat > /usr/share/themes/DRUIDS/gnome-shell/gnome-shell.css << 'THEME'
/* DRUIDS GNOME Shell Theme */
@import url("/usr/share/gnome-shell/theme/gnome-shell.css");

/* Top bar */
#panel {
    background-color: rgba(0, 0, 0, 0.9);
    font-weight: bold;
    height: 28px;
}

/* Activities button */
#panel .panel-button:hover {
    background-color: rgba(255, 0, 0, 0.3);
}

/* System menu */
.system-menu-action {
    color: #ffffff;
}

.system-menu-action:hover {
    background-color: rgba(255, 0, 0, 0.2);
}

/* Notifications */
.notification-banner {
    background-color: rgba(0, 0, 0, 0.9);
    border: 1px solid #ff0000;
}
THEME

# Set default wallpaper
mkdir -p /usr/share/backgrounds/druids
cp /usr/share/backgrounds/druids/druids-wallpaper.png /usr/share/gnome-background-properties/

# Create dconf defaults
mkdir -p /etc/dconf/db/local.d
cat > /etc/dconf/db/local.d/01-druids << 'DCONF'
[org/gnome/desktop/background]
picture-uri='file:///usr/share/backgrounds/druids/druids-wallpaper.png'
picture-options='zoom'
primary-color='#000000'
secondary-color='#000000'

[org/gnome/desktop/interface]
gtk-theme='Adwaita-dark'
icon-theme='Adwaita'
font-name='Liberation Sans 11'
document-font-name='Liberation Sans 11'
monospace-font-name='Liberation Mono 10'

[org/gnome/shell]
favorite-apps=['tor-browser.desktop', 'org.gnome.Nautilus.desktop', 'org.gnome.Terminal.desktop', 'obsidian.desktop']

[org/gnome/desktop/wm/preferences]
button-layout='close,minimize,maximize:'
theme='Adwaita-dark'
DCONF

# Update dconf
dconf update
EOF

chmod +x config/chroot_local-hooks/99-druids-gnome-customize
```

### 2.4 Custom Greeter Configuration

```bash
cat > config/chroot_local-includes/etc/gdm3/greeter.dconf-defaults << 'EOF'
[org/gnome/login-screen]
banner-message-enable=true
banner-message-text='DRUIDS - Secure Revolutionary Infrastructure\nRemember: No investigation, no right to speak'
disable-user-list=true
logo='/usr/share/pixmaps/druids-greeter-logo.png'
EOF
```

## Step 3: Pre-installed Software

### 3.1 Add Obsidian and Plugins

```bash
cat > config/chroot_local-hooks/98-install-obsidian << 'EOF'
#!/bin/sh
set -e

# Download and install Obsidian AppImage
OBSIDIAN_VERSION="1.4.16"
wget -O /tmp/obsidian.AppImage \
    "https://github.com/obsidianmd/obsidian-releases/releases/download/v${OBSIDIAN_VERSION}/Obsidian-${OBSIDIAN_VERSION}.AppImage"

# Install to system location
mkdir -p /opt/obsidian
mv /tmp/obsidian.AppImage /opt/obsidian/
chmod +x /opt/obsidian/obsidian.AppImage

# Create desktop file
cat > /usr/share/applications/obsidian.desktop << 'DESKTOP'
[Desktop Entry]
Name=Obsidian
Exec=/opt/obsidian/obsidian.AppImage %U
Terminal=false
Type=Application
Icon=obsidian
Categories=Office;
MimeType=x-scheme-handler/obsidian;
DESKTOP

# Download icon
wget -O /usr/share/pixmaps/obsidian.png \
    "https://obsidian.md/images/obsidian-logo-gradient.svg"
EOF

chmod +x config/chroot_local-hooks/98-install-obsidian
```

### 3.2 Pre-configure Git Aliases

```bash
cat > config/chroot_local-includes/etc/skel/.gitconfig << 'EOF'
[alias]
    # Revolutionary aliases
    unite = merge
    struggle = diff
    advance = push
    learn = pull
    history = log --oneline --graph --all
    
    # Practical aliases
    st = status
    co = checkout
    br = branch
    cm = commit -m
    unstage = reset HEAD --
    
[init]
    defaultBranch = main
    
[user]
    # Will be configured on first use
    name = 
    email = 
EOF
```

## Step 4: Build Automation Scripts

### 4.1 First-Boot Setup Script

```bash
cat > config/chroot_local-includes/usr/local/bin/druids-first-boot << 'EOF'
#!/bin/bash
# DRUIDS First Boot Configuration

set -e

FIRST_BOOT_MARKER="/var/lib/druids/.first-boot-complete"

if [ -f "$FIRST_BOOT_MARKER" ]; then
    exit 0
fi

# Show welcome
zenity --info --width=600 --title="Welcome to DRUIDS-Tails" \
    --text="Welcome to your secure revolutionary infrastructure!\n\nThis setup wizard will:\n• Configure your security keys\n• Set up Git identity\n• Initialize Obsidian vault\n• Create secure communication channels\n\nThis process takes about 10 minutes."

# Run setup modules
/usr/local/bin/druids-setup-keys
/usr/local/bin/druids-setup-git
/usr/local/bin/druids-setup-obsidian

# Mark complete
mkdir -p /var/lib/druids
touch "$FIRST_BOOT_MARKER"

zenity --info --title="Setup Complete" \
    --text="DRUIDS setup is complete!\n\nYour system is ready for secure organizing."
EOF

chmod +x config/chroot_local-includes/usr/local/bin/druids-first-boot
```

### 4.2 Create Systemd Service for First Boot

```bash
cat > config/chroot_local-includes/etc/systemd/system/druids-first-boot.service << 'EOF'
[Unit]
Description=DRUIDS First Boot Setup
After=gdm.service
Wants=gdm.service

[Service]
Type=oneshot
ExecStart=/usr/local/bin/druids-first-boot
RemainAfterExit=yes
User=amnesia
Environment="DISPLAY=:0"
Environment="XAUTHORITY=/run/user/1000/gdm/Xauthority"

[Install]
WantedBy=default.target
EOF

# Enable service
cat > config/chroot_local-hooks/97-enable-druids-services << 'EOF'
#!/bin/sh
systemctl enable druids-first-boot.service
EOF

chmod +x config/chroot_local-hooks/97-enable-druids-services
```

## Step 5: Building the Image

### 5.1 Configure Build Variables

```bash
# Set custom version
export DRUIDS_VERSION="0.1.0"
export TAILS_VERSION="6.15"
export BUILD_DATE=$(date +%Y%m%d)

# Update version files
echo "DRUIDS-Tails ${DRUIDS_VERSION} (based on Tails ${TAILS_VERSION})" > \
    config/chroot_local-includes/etc/druids-version
```

### 5.2 Build Process

```bash
# Clean previous builds
lb clean --purge

# Configure live-build
lb config \
    --architecture amd64 \
    --binary-images iso-hybrid \
    --distribution bookworm \
    --iso-application "DRUIDS-Tails" \
    --iso-volume "DRUIDS-Tails-${DRUIDS_VERSION}" \
    --memtest none

# Add custom packages
echo "git
curl
wget
gnupg2
obsidian
vim
tmux
htop
rsync
jq" >> config/package-lists/druids.list.chroot

# Build the image
sudo lb build
```

### 5.3 Post-Build Customization

```bash
# Extract ISO for modification
mkdir iso_extracted
xorriso -osirrox on -indev tails-amd64-*.iso -extract / iso_extracted

# Modify isolinux splash
cp /path/to/druids-isolinux-splash.png iso_extracted/isolinux/splash.png

# Update bootloader text
sed -i 's/Tails/DRUIDS-Tails/g' iso_extracted/isolinux/live64.cfg
sed -i 's/The Amnesic Incognito Live System/Democratic Resilient Unity-building Information Distribution System/g' \
    iso_extracted/isolinux/*.cfg

# Rebuild ISO
xorriso -as mkisofs \
    -r -V "DRUIDS-Tails-${DRUIDS_VERSION}" \
    -J -joliet-long \
    -isohybrid-mbr /usr/lib/ISOLINUX/isohdpfx.bin \
    -c isolinux/boot.cat \
    -b isolinux/isolinux.bin \
    -no-emul-boot -boot-load-size 4 -boot-info-table \
    -eltorito-alt-boot \
    -e boot/grub/efi.img \
    -no-emul-boot -isohybrid-gpt-basdat \
    -o druids-tails-${DRUIDS_VERSION}-${BUILD_DATE}.iso \
    iso_extracted
```

## Step 6: Reproducible Builds

### 6.1 Create Build Container

```dockerfile
# Dockerfile for reproducible DRUIDS-Tails builds
FROM debian:bookworm

RUN apt-get update && apt-get install -y \
    live-build git wget xorriso syslinux \
    syslinux-utils isolinux mtools dosfstools \
    squashfs-tools genisoimage

WORKDIR /build
COPY . /build/

ENV SOURCE_DATE_EPOCH=1704067200
ENV DRUIDS_VERSION=0.1.0

CMD ["/build/scripts/build-druids-tails.sh"]
```

### 6.2 Build Script

```bash
cat > scripts/build-druids-tails.sh << 'EOF'
#!/bin/bash
set -e

# Set reproducible build environment
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export TZ=UTC

# Build with consistent timestamp
find config/chroot_local-includes -type f -exec touch -d @${SOURCE_DATE_EPOCH} {} \;

# Run build
lb clean --purge
lb config
lb build

# Generate checksums
sha256sum *.iso > SHA256SUMS
gpg --clearsign SHA256SUMS
EOF

chmod +x scripts/build-druids-tails.sh
```

## Step 7: Verification and Testing

### 7.1 Automated Testing

```bash
# Create test script
cat > test/verify-build.sh << 'EOF'
#!/bin/bash

ISO_PATH=$1

# Verify ISO integrity
echo "Verifying ISO integrity..."
xorriso -indev "$ISO_PATH" -check_media --

# Check for required files
echo "Checking for DRUIDS customizations..."
xorriso -osirrox on -indev "$ISO_PATH" -find / -name "*druids*" -exec echo {} \;

# Verify packages
echo "Extracting filesystem.squashfs..."
xorriso -osirrox on -indev "$ISO_PATH" -extract /live/filesystem.squashfs /tmp/fs.squashfs
unsquashfs -l /tmp/fs.squashfs | grep -E "(obsidian|druids)" | head -20
EOF
```

### 7.2 QEMU Testing

```bash
# Quick boot test
qemu-system-x86_64 \
    -m 4096 \
    -cdrom druids-tails-*.iso \
    -boot d \
    -enable-kvm \
    -display gtk
```

## Advanced Customizations

### Custom Package Repository

```bash
# Add custom APT repository for DRUIDS packages
cat > config/chroot_local-includes/etc/apt/sources.list.d/druids.list << 'EOF'
deb [signed-by=/usr/share/keyrings/druids-keyring.gpg] https://apt.druids.dev bookworm main
EOF

# Add repository key
wget -O config/chroot_local-includes/usr/share/keyrings/druids-keyring.gpg \
    https://apt.druids.dev/druids-keyring.gpg
```

### Hardware-Specific Optimizations

```bash
# Add firmware for specific hardware
echo "firmware-iwlwifi
firmware-realtek
firmware-atheros" >> config/package-lists/firmware.list.chroot

# Kernel parameters for specific hardware
echo "amdgpu.dc=1 nvme_core.default_ps_max_latency_us=0" >> \
    config/bootloaders/isolinux/live.cfg.in
```

## Security Considerations

1. **Build Environment**: Always build in isolated VMs
2. **Supply Chain**: Verify all downloaded components
3. **Reproducibility**: Use consistent timestamps and environments
4. **Testing**: Verify each build before distribution
5. **Signing**: GPG sign all images and checksums

## Distribution

```bash
# Create distribution package
mkdir -p dist/druids-tails-${DRUIDS_VERSION}
cp druids-tails-*.iso dist/druids-tails-${DRUIDS_VERSION}/
cp SHA256SUMS* dist/druids-tails-${DRUIDS_VERSION}/
cp docs/verification-guide.md dist/druids-tails-${DRUIDS_VERSION}/

# Create torrent for distribution
mktorrent \
    -a "udp://tracker.opentrackr.org:1337/announce" \
    -n "DRUIDS-Tails-${DRUIDS_VERSION}" \
    -o druids-tails-${DRUIDS_VERSION}.torrent \
    dist/druids-tails-${DRUIDS_VERSION}/
```

---

*This is the deep technical dive. With this guide, you can create fully customized Tails images with revolutionary aesthetics while maintaining security.*