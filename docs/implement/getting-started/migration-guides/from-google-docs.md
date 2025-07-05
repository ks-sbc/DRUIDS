---
title: "Escaping Google's Surveillance: Migrating Your Organization's Data"
description: "Step-by-step guide to liberating your organizing documents from Google's surveillance infrastructure"
created: 2025-07-02
updated: 2025-07-02
type: "docs/how-to"
security: "L0"
version: "1.0.0"
document_id: "MIG-HOW-2025-001-L0"
tags: ["migration", "google-docs", "surveillance", "organizing", "liberation"]
draft: false
author: ["Comrade 47"]
---

# Escaping Google's Surveillance: Migrating Your Organization's Data

**Why this matters**: See [our analysis of surveillance capitalism](../../../start/why-druids.md) in organizing.

**Already convinced?** Jump to [Step 1](#step-1-inventory-your-digital-prison) to begin liberation.

## The Material Reality

Google isn't your friend. They're a surveillance corporation that actively collaborates with the state:

- **Project Maven**: Google builds AI for military drone strikes
- **Keyword Warrants**: Police get data on everyone who searched specific terms
- **Geofence Warrants**: Everyone at a protest identified through location data
- **Real Example**: Inauguration protesters' entire Google accounts seized, years of organizing exposed

Every document in Google Drive is a future evidence exhibit. Every shared folder is a network map for investigators. Every comment thread is a recorded conversation.

**This isn't paranoia. It's pattern recognition.**

## Before You Start

### What You'll Need

- [ ] Computer with Git installed (see [installation guide](../../../implement/getting-started/druids-installation-guide.md))
- [ ] List of all Google Drives/folders your org uses
- [ ] 2-3 hours of focused time
- [ ] Trusted comrades to verify the migration
- [ ] Determination to break free from corporate surveillance

**New to Git?** Don't worry - [it's not programming](../../../learn/git-basics/git-isnt-programming.md) and you only need [7 commands](../../../learn/git-basics/git-in-7-commands.md).

### Security Considerations

**DO NOT** do this migration:
- On organization wifi
- From a personal Google account linked to your name
- Without VPN if possible
- While leaving browser logged into Google afterward

**DO** this migration:
- From a secure location
- Using dedicated browser profile
- With comrades aware it's happening
- After backing up critical documents elsewhere first

## Step 1: Inventory Your Digital Prison

Before escaping, map what you're liberating:

```markdown
# Organization Data Inventory

## Google Drive Folders
- [ ] Meeting Minutes (2020-2025)
- [ ] Campaign Planning Documents  
- [ ] Member Resources
- [ ] Financial Records (handle specially)
- [ ] Graphics and Flyers

## Google Docs Being Actively Edited
- [ ] Current Campaign Strategy
- [ ] Upcoming Event Planning
- [ ] Active Proposals

## Shared With External Organizations
- [ ] Coalition Documents
- [ ] Joint Statements
```

**Reality Check**: You probably have more than you think. Check:
- "Shared with me" section
- Trash (Google keeps deleted files)
- Version history of sensitive docs
- Comments that might contain real names

## Step 2: Download Your Data

### Method 1: Google Takeout (Complete Archive)

Best for comprehensive liberation:

1. Go to [takeout.google.com](https://takeout.google.com)
2. Click "Deselect all"
3. Select ONLY "Drive"
4. Click "Next step"
5. Choose:
   - **Export once**
   - **File type**: .zip
   - **Size**: 2GB chunks (easier to handle)
6. Create export
7. Wait for email (can take hours for large archives)

**Warning**: This downloads EVERYTHING, including:
- Files others shared with you
- Revision history
- Comments with potential real names
- Deleted items in trash

### Method 2: Selective Download (Recommended)

More secure, gives you control:

1. Open Google Drive
2. Navigate to each folder
3. Right-click → Download
4. Creates .zip with folder structure preserved
5. Repeat for each organizational folder

**Pro tip**: Download in chunks to avoid overwhelming your system or triggering Google's suspicion.

### What About Google Docs?

Google's proprietary formats need conversion:

- **Google Docs** → Downloads as .docx (Microsoft Word)
- **Google Sheets** → Downloads as .xlsx (Excel)  
- **Google Slides** → Downloads as .pptx (PowerPoint)

You'll convert these to Markdown later for Git compatibility.

## Step 3: Cleanse the Data

Before importing to Git, remove surveillance traces:

### Remove Metadata

Every file contains hidden data about you:

```bash
# Install metadata removal tool
sudo apt install mat2  # Debian/Ubuntu
brew install mat2     # Mac

# Clean all files in directory
mat2 --inplace downloaded-files/*

# Verify metadata removed
mat2 --show cleaned-file.docx
```

### Check for Exposed Names

Search for accidental identity leaks:

```bash
# Search for common name patterns
grep -r "First Last" downloaded-files/
grep -r "@gmail.com" downloaded-files/
grep -r "phone:" downloaded-files/
```

Replace any found with pseudonyms before proceeding.

### Convert to Markdown

For Git compatibility and future-proofing:

```bash
# Install pandoc for conversion
sudo apt install pandoc

# Convert all .docx files
for file in *.docx; do
    pandoc "$file" -t markdown -o "${file%.docx}.md"
done
```

## Step 4: Initialize Your Liberation Repository

Time to create your organization's new home:

```bash
# Create repository directory
mkdir ~/organizing/our-org-docs
cd ~/organizing/our-org-docs

# Initialize Git repository
git init

# Create basic structure
mkdir -p {meetings,campaigns,resources,graphics}

# Create README
echo "# [Organization Name] Liberation Archive" > README.md
echo "Escaped from Google's surveillance: $(date)" >> README.md
```

## Step 5: Import Your Liberated Data

Move your cleaned files into the new structure:

```bash
# Move meeting minutes
mv ~/Downloads/cleaned-export/meetings/* ./meetings/

# Move campaign docs
mv ~/Downloads/cleaned-export/campaigns/* ./campaigns/

# Move resources
mv ~/Downloads/cleaned-export/resources/* ./resources/
```

Organize thoughtfully - this is your chance to improve on Google's chaos.

## Step 6: Your First Revolutionary Commit

This moment matters. You're not just saving files - you're practicing digital self-determination:

```bash
# Configure Git with pseudonym
git config user.name "Comrade 102"
git config user.email "comrade102@protonmail.com"

# Stage all liberated documents
git add .

# Make your liberation commit
git commit -m "Liberation from Google surveillance complete

- Migrated 5 years of meeting minutes
- Preserved campaign documentation  
- Removed all metadata and real names
- Began practice of revolutionary infrastructure

No more corporate surveillance. No more data harvesting.
Our organizing, our control.

Death to digital landlords! 🚩"

# View your revolutionary history
git log
```

## Step 7: Verification and Cleanup

### Verify Migration Success

With trusted comrades, confirm:

- [ ] All critical documents transferred
- [ ] No real names in committed files
- [ ] Folder structure makes sense
- [ ] Git history shows your liberation commit

### Destroy the Colonial Records

After verification:

1. Download your Google Takeout archive (keep encrypted backup)
2. Delete files from Google Drive
3. Empty Google Drive trash
4. Remove Google permissions from browser
5. Consider account deletion timeline

**Warning**: Google keeps deleted data for up to 60 days. Plan accordingly.

## Common Problems and Solutions

### "The download is huge!"

Google bloats exports. Focus on essential organizing documents first. Graphics and videos can migrate separately.

### "Conversion broke formatting!"

Markdown is simpler than Google Docs. This is good - fancy formatting was corporate distraction. Content matters, not fonts.

### "Found real names after committing!"

See our guide: [Help, I Committed Sensitive Data!](../../security/help-committed-sensitive-data.md)

### "Comrades resist leaving Google!"

Normal. Share this guide. Show them RICO charges. Demonstrate the alternative. Change takes time.

## What You've Accomplished

You've just:
- Removed organizational data from corporate surveillance
- Taken first step toward infrastructural autonomy
- Practiced security culture concretely
- Created foundation for democratic centralism

Your documents are no longer evidence. They're revolutionary resources under collective control.

## Next Steps

1. **Learn Git Basics**: [Your First Revolutionary Commit](../../../learn/tutorials/your-first-revolutionary-commit.md)
2. **Set Up Security**: [Why Discord Democracy Fails](../../../learn/explanations/why-discord-democracy-fails.md)
3. **Organize Workflows**: [Meeting Workflows That Work](../../../implement/workflows/meeting-workflow-guide.md)
4. **Break Other Chains**: [Breaking Discord's Chains](../../../implement/getting-started/migration-guides/from-discord.md)

## Remember

Google made it easy because surveillance is profitable. DRUIDS requires discipline because liberation takes work.

Every commit is a blow against digital feudalism. Every push spreads revolutionary infrastructure.

---

*"The master's tools will never dismantle the master's house."* - Audre Lorde

But we can steal the tools, learn their craft, and build our own damn house.

*Welcome to revolutionary infrastructure, comrade.*