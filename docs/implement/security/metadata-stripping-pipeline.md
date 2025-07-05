---
title: "Metadata Stripping Pipeline: Automating Security for Revolutionary Organizations"
description: "Step-by-step guide to automatically remove dangerous metadata from all files before they enter your repository"
created: 2025-07-03
updated: 2025-07-03
type: "docs/how-to"
security: "L1"
version: "1.0.0"
document_id: "INT-HT-2025-423-L1"
tags: ["security", "metadata", "automation", "privacy", "technical"]
draft: false
author: ["Claude (AI)", "Comrade 47"]
---

# Metadata Stripping Pipeline: Automating Security

## Overview

Every photo, document, and file contains hidden metadata that can destroy operational security. This guide sets up automated systems to strip dangerous metadata before it ever enters your repository.

## Prerequisites

- Basic command line knowledge
- Git repository set up
- Admin access to install tools
- 30 minutes for initial setup

## What Is Metadata and Why It Kills

### The Hidden Danger in Every File

```bash
# What you see: cute_cat.jpg
# What metadata reveals:
exiftool cute_cat.jpg

GPS Position         : 40.7128° N, 74.0060° W  # Your exact location
Date/Time Original   : 2024:03:21 18:45:23     # When you were there
Camera Model Name    : iPhone 12 Pro           # Your device
Owner Name           : Sarah's iPhone          # Your identity
Software             : Instagram               # Your apps
```

### Real World Consequences

**Case 1**: FBI tracked January 6 participants through photo EXIF data
**Case 2**: Vice journalist exposed confidential source through PDF metadata  
**Case 3**: Activist's home raided after photo contained GPS coordinates

## Installing the Tools

### Core Tools Installation

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y \
    exiftool \      # Swiss army knife of metadata
    mat2 \          # Metadata removal tool
    imagemagick \   # Image processing
    poppler-utils \ # PDF handling
    git-filter-repo # Git history cleaning

# macOS (with Homebrew)
brew install exiftool mat2 imagemagick poppler git-filter-repo

# Verify installation
exiftool -ver
mat2 --version
```

### Python Dependencies

```bash
# For advanced automation
pip3 install --user \
    python-magic \  # File type detection
    pillow \        # Image processing
    pypdf2          # PDF manipulation
```

## Basic Manual Stripping

### Quick Commands for Immediate Use

```bash
# Strip ALL metadata from image
exiftool -all= dangerous-photo.jpg

# Strip metadata from PDF
exiftool -all= meeting-notes.pdf

# Strip entire directory
exiftool -all= -r sensitive-folder/

# Using mat2 (more thorough)
mat2 protest-photo.jpg
mat2 --inplace *.pdf  # Strip in place
```

### What Gets Stripped

```bash
# Before stripping
exiftool IMG_1234.jpg | wc -l
# Output: 246 lines of metadata

# After stripping  
exiftool -all= IMG_1234.jpg
exiftool IMG_1234_original.jpg | wc -l
# Output: 8 lines (only essential image data)
```

## Automated Git Pipeline

### Setting Up Pre-Commit Hooks

Never accidentally commit metadata again:

```bash
#!/bin/bash
# .git/hooks/pre-commit
# Make executable: chmod +x .git/hooks/pre-commit

echo "🔍 Checking for metadata in staged files..."

# Get list of staged files
files=$(git diff --cached --name-only --diff-filter=ACM)

# Check each file
for file in $files; do
    # Skip if file doesn't exist (deleted)
    [ -f "$file" ] || continue
    
    # Get file extension
    ext="${file##*.}"
    
    case "$ext" in
        jpg|jpeg|png|gif|bmp|tiff)
            echo "Stripping metadata from image: $file"
            exiftool -all= "$file" -overwrite_original
            git add "$file"
            ;;
        pdf)
            echo "Stripping metadata from PDF: $file"
            exiftool -all= "$file" -overwrite_original
            git add "$file"
            ;;
        mp4|mov|avi)
            echo "WARNING: Video $file may contain metadata"
            echo "Run: exiftool -all= '$file'"
            ;;
    esac
done

echo "✅ Metadata stripping complete"
```

### Advanced Pipeline Script

Create comprehensive automation:

```bash
#!/bin/bash
# scripts/security/metadata-strip.sh

set -e  # Exit on error

# Configuration
LOGFILE="logs/metadata-strip.log"
QUARANTINE="quarantine/"
PROCESSED="processed/"

# Ensure directories exist
mkdir -p "$(dirname "$LOGFILE")" "$QUARANTINE" "$PROCESSED"

# Logging function
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOGFILE"
}

# Process single file
process_file() {
    local file="$1"
    local basename=$(basename "$file")
    
    log "Processing: $file"
    
    # Backup original to quarantine
    cp "$file" "$QUARANTINE/$basename.original"
    
    # Detect file type
    filetype=$(file -b --mime-type "$file")
    
    case "$filetype" in
        image/*)
            # Strip EXIF, keep copyright if needed
            exiftool -all= -TagsFromFile @ -ColorSpaceTags \
                    -overwrite_original "$file"
            ;;
        application/pdf)
            # Strip all PDF metadata
            exiftool -all= -overwrite_original "$file"
            # Additional PDF cleaning
            qpdf --linearize --replace-input "$file"
            ;;
        video/*)
            # Videos need special handling
            ffmpeg -i "$file" -map_metadata -1 -c:v copy -c:a copy \
                   "$PROCESSED/$basename" 2>/dev/null
            mv "$PROCESSED/$basename" "$file"
            ;;
        *)
            log "Unknown type: $filetype for $file"
            ;;
    esac
    
    log "✓ Stripped: $file"
}

# Main processing
if [ $# -eq 0 ]; then
    # Process all files in current directory
    find . -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \
                      -o -iname "*.pdf" -o -iname "*.mp4" -o -iname "*.mov" \) \
          -exec "$0" {} \;
else
    # Process specific file
    process_file "$1"
fi
```

## Git Integration

### Global Git Filters

Apply metadata stripping to ALL repositories:

```bash
# Configure global filters
git config --global filter.stripmetadata.clean \
    'mat2 --inplace %f && cat %f'

# Create global attributes
echo "*.jpg filter=stripmetadata" >> ~/.gitattributes_global
echo "*.jpeg filter=stripmetadata" >> ~/.gitattributes_global
echo "*.png filter=stripmetadata" >> ~/.gitattributes_global
echo "*.pdf filter=stripmetadata" >> ~/.gitattributes_global

# Enable global attributes
git config --global core.attributesfile ~/.gitattributes_global
```

### Repository-Specific Configuration

For maximum control per repository:

```bash
# In your repository root
cat > .gitattributes << 'EOF'
# Strip metadata from images
*.jpg filter=stripmetadata
*.jpeg filter=stripmetadata
*.png filter=stripmetadata
*.gif filter=stripmetadata

# Strip metadata from documents
*.pdf filter=stripmetadata
*.doc filter=stripmetadata
*.docx filter=stripmetadata

# Videos (warn only due to size)
*.mp4 filter=warn-metadata
*.mov filter=warn-metadata
EOF

# Configure filters
git config filter.stripmetadata.clean 'exiftool -all= %f -overwrite_original && cat %f'
git config filter.warn-metadata.clean 'echo "WARNING: Video may contain metadata" && cat'
```

## Handling Specific File Types

### Images: The Biggest Risk

```bash
# Complete image sanitization
sanitize_image() {
    local input="$1"
    local output="${input%.*}_safe.${input##*.}"
    
    # Remove ALL metadata
    exiftool -all= "$input" -o "$output"
    
    # Extra paranoid: Re-encode image
    convert "$output" -strip -resize 100% -quality 95 "$output"
    
    # Verify no metadata remains
    if exiftool "$output" | grep -E "(GPS|Date|Serial|Owner)"; then
        echo "ERROR: Metadata still present!"
        return 1
    fi
    
    mv "$output" "$input"
}
```

### PDFs: Hidden Danger

```bash
# PDF deep cleaning
clean_pdf() {
    local input="$1"
    
    # Method 1: exiftool
    exiftool -all= "$input" -overwrite_original
    
    # Method 2: qpdf (more thorough)
    qpdf --linearize --remove-unreferenced-resources=yes \
         --empty --replace-input "$input"
    
    # Method 3: Ghostscript (nuclear option)
    gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 \
       -dPDFSETTINGS=/prepress -sOutputFile="${input}.clean" "$input"
    
    mv "${input}.clean" "$input"
}
```

### Office Documents: Metadata Nightmare

```bash
# LibreOffice conversion method (most thorough)
clean_office_doc() {
    local input="$1"
    local temp="${input%.*}_temp.pdf"
    local output="${input%.*}_clean.${input##*.}"
    
    # Convert to PDF (strips most metadata)
    libreoffice --headless --convert-to pdf "$input"
    
    # Strip PDF metadata
    exiftool -all= "${input%.*}.pdf" -overwrite_original
    
    # Convert back if needed
    # Or keep as PDF for distribution
}
```

## Verification Pipeline

### Trust But Verify

```bash
#!/bin/bash
# scripts/verify-metadata.sh

verify_file() {
    local file="$1"
    echo "Checking: $file"
    
    # Extract remaining metadata
    metadata=$(exiftool "$file" 2>/dev/null)
    
    # Check for dangerous fields
    dangerous_fields="GPS|Latitude|Longitude|Owner|Serial|Author|Creator|Producer|Company"
    
    if echo "$metadata" | grep -E "$dangerous_fields"; then
        echo "❌ DANGER: Sensitive metadata found in $file"
        return 1
    else
        echo "✅ SAFE: $file contains no sensitive metadata"
        return 0
    fi
}

# Verify entire repository
find . -type f \( -iname "*.jpg" -o -iname "*.pdf" \) | while read file; do
    verify_file "$file" || exit 1
done
```

## Continuous Integration

### GitHub Actions Workflow

```yaml
# .github/workflows/metadata-check.yml
name: Metadata Security Check

on: [push, pull_request]

jobs:
  metadata-scan:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Install tools
      run: |
        sudo apt-get update
        sudo apt-get install -y exiftool mat2
    
    - name: Check for metadata
      run: |
        # Find all images and documents
        files=$(find . -type f \( -iname "*.jpg" -o -iname "*.jpeg" \
                                  -o -iname "*.png" -o -iname "*.pdf" \))
        
        # Check each file
        for file in $files; do
          echo "Checking $file..."
          
          # Look for GPS data
          if exiftool "$file" | grep -i "GPS"; then
            echo "::error::GPS data found in $file"
            exit 1
          fi
          
          # Look for personal info
          if exiftool "$file" | grep -E "(Owner|Author|Creator)"; then
            echo "::warning::Personal metadata in $file"
          fi
        done
```

## Emergency Response

### When Metadata Leaks Happen

```bash
# If metadata was already committed
# 1. Remove from history
git filter-repo --path sensitive-photo.jpg --invert-paths

# 2. Clean all historical versions
git filter-branch --index-filter \
    'git ls-files -s | grep ".jpg" | while read mode object stage file; do
        cleaned=$(exiftool -all= "$file" -o -)
        new_object=$(echo "$cleaned" | git hash-object -w --stdin)
        git update-index --cacheinfo "$mode,$new_object,$file"
    done' -- --all

# 3. Force push (requires team coordination)
git push --force-with-lease
```

## Best Practices

### DO:
- ✓ Strip metadata BEFORE committing
- ✓ Verify stripping worked
- ✓ Automate everything possible
- ✓ Keep original files offline only
- ✓ Train all members on risks
- ✓ Regular audits of repository

### DON'T:
- ✗ Trust any device's "privacy" settings
- ✗ Assume cloud services strip metadata
- ✗ Share photos directly from phones
- ✗ Forget about video metadata
- ✗ Skip verification steps
- ✗ Process files on compromised devices

## Common Mistakes

### "But I turned off location services!"
Device settings aren't reliable. Always strip manually.

### "The platform said it removes metadata"
- Twitter: Removes some, not all
- Facebook: Keeps everything internally
- Signal: Good but verify
- Discord: Keeps everything

### "It's just a screenshot"
Screenshots can contain:
- Device information
- App data
- Timestamp
- Sometimes even location

## Building a Security Culture

Make metadata stripping part of daily practice:

```bash
# Add to .bashrc/.zshrc
alias strip='exiftool -all= -overwrite_original'
alias stripdir='exiftool -all= -r -overwrite_original'
alias checkdata='exiftool'

# Quick strip function
stripfile() {
    exiftool -all= "$1" -overwrite_original
    echo "✅ Stripped: $1"
}
```

## Next Steps

1. Install the tools TODAY
2. Set up pre-commit hooks
3. Audit existing repository
4. Train all members
5. Create organization-specific pipeline
6. Regular security audits

Remember: Metadata has put comrades in prison. Every photo you share, every document you commit, every file you upload could contain the evidence that destroys lives.

Strip first. Verify second. Share third.

*"In intelligence work, there are no small mistakes."* - Markus Wolf

Make metadata stripping as automatic as breathing. Your freedom depends on it.