---
title: "Breaking Discord's Chains: Migrating Your Organization Off Discord"
description: "Step-by-step guide to liberating your organizing from Discord's corporate surveillance"
created: 2025-07-02
updated: 2025-07-02
type: "docs/how-to"
security: "L0"
version: "1.0.0"
document_id: "MIG-HOW-2025-002-L0"
tags: ["migration", "discord", "surveillance", "organizing", "liberation"]
draft: false
author: ["Comrade 47"]
---

# Breaking Discord's Chains: Migrating Your Organization Off Discord

## Why Discord Is Dangerous

Discord isn't your community - it's a surveillance platform:

- **All messages permanently logged**: Even "deleted" ones
- **Voice calls monitored**: AI transcription capabilities
- **Real identity leaks**: IP addresses, device IDs, payment info
- **Corporate collaboration**: Hands data to law enforcement
- **January 6th precedent**: Discord messages used as evidence

Your "secure server" is their evidence locker.

## Prerequisites

- Admin access to your Discord server
- 3-4 hours for initial migration
- Trusted comrades to help coordinate
- Alternative platform chosen (see our recommendations)
- Git repository set up (see "Your First Revolutionary Commit")

## Step 1: Map Your Discord Prison

Before escaping, document what you're leaving:

### Inventory Channels
```markdown
# Discord Structure Inventory

## Text Channels
- #general - Daily organizing chat
- #meeting-notes - Where we post minutes
- #campaigns - Active campaign planning
- #resources - Shared documents/links
- #memes - Community building

## Voice Channels
- General Voice - Weekly meetings
- Breakout Rooms - Committee work

## Roles/Permissions
- @organizers - Core planning group
- @members - Verified members
- @new - Onboarding

## Pinned Messages
- [List important pinned content]

## Active Integrations
- [Bots, webhooks, connected apps]
```

### Download Critical History

```bash
# Using DiscordChatExporter (command line)
# Install: https://github.com/Tyrrrz/DiscordChatExporter

# Export each channel
dotnet DiscordChatExporter.Cli.dll export \
  -t "YOUR_BOT_TOKEN" \
  -c CHANNEL_ID \
  -f HtmlDark \
  -o exports/

# Or use the GUI version for easier export
```

**Security Note**: Download on trusted computer only. These exports contain everything.

### Automated Export Script

```bash
#!/bin/bash
# discord-export.sh - Automate full server export

# Configuration
TOKEN="YOUR_BOT_TOKEN"
SERVER_ID="YOUR_SERVER_ID"
EXPORT_DIR="./discord-export-$(date +%Y%m%d)"

# Create export directory
mkdir -p "$EXPORT_DIR"

# Get all channels (requires discord.py)
python3 << EOF
import discord
import asyncio
import json

client = discord.Client()

@client.event
async def on_ready():
    guild = client.get_guild($SERVER_ID)
    channels = []
    
    for channel in guild.text_channels:
        channels.append({
            'id': channel.id,
            'name': channel.name,
            'category': channel.category.name if channel.category else 'None'
        })
    
    with open('$EXPORT_DIR/channels.json', 'w') as f:
        json.dump(channels, f, indent=2)
    
    await client.close()

client.run('$TOKEN')
EOF

# Export each channel
while IFS= read -r channel_id; do
    channel_name=$(jq -r ".[] | select(.id==$channel_id) | .name" "$EXPORT_DIR/channels.json")
    echo "Exporting #$channel_name..."
    
    dotnet DiscordChatExporter.Cli.dll export \
        -t "$TOKEN" \
        -c "$channel_id" \
        -f Json \
        -o "$EXPORT_DIR/channels/" \
        --dateformat "yyyy-MM-dd HH:mm"
done < <(jq -r '.[].id' "$EXPORT_DIR/channels.json")

# Export server info, roles, members
echo "Exporting server metadata..."
# Additional exports here
```

## Step 2: Prepare Your Liberation Infrastructure

### Set Up Git Repository Structure

```bash
# Create organized structure
mkdir -p liberation/{announcements,resources,archive,meeting-minutes}

# Create migration guide for comrades
cat > liberation/README.md << EOF
# [Organization Name] Liberation from Discord

We're moving off Discord to protect our organizing.

## Why We're Moving
- Discord logs everything permanently
- Corporate surveillance endangers comrades
- We need infrastructure we control

## Where We're Going
- Git: Permanent records, democratic process
- [Chosen chat platform]: Encrypted real-time communication
- Meeting minutes: Now in Git history

## Timeline
- Week 1: Core organizers train on new tools
- Week 2: Migrate active campaigns
- Week 3: General membership onboarding
- Week 4: Discord server archived and locked
EOF
```

### Choose Replacement Tools

For different Discord functions:

**Real-time chat**:
- Matrix/Element: Federated, encrypted, self-hostable
- Signal: Good for small groups (<1000)
- Mattermost: Self-hosted Slack alternative

**Voice meetings**:
- Jitsi Meet: No account needed, encrypted
- Mumble: Low bandwidth, high security
- BigBlueButton: Full meeting features

**Document storage**:
- Git: For permanent records
- NextCloud: For active collaboration
- Cryptpad: For sensitive drafts

## Step 3: Export and Transform Content

### Meeting Notes Migration

```bash
# Convert Discord meeting notes to Git
# For each meeting in Discord:

# 1. Copy content from Discord
# 2. Create proper markdown file
cat > meetings/2025-06-15-general-meeting.md << 'EOF'
# General Meeting Minutes
Date: 2025-06-15
Ported from Discord by: Comrade 47

[Original Discord content here]

---
*Migrated from Discord on 2025-07-02*
*Original message ID: [ID for reference]*
EOF

# 3. Commit to Git
git add meetings/
git commit -m "Migrate June 15 meeting minutes from Discord

- Preserved original formatting
- Removed member handles for security
- Part of Discord liberation project"
```

### Resource Channel Migration

```bash
# Extract all links and documents
# Create organized resource list

cat > resources/migrated-from-discord.md << 'EOF'
# Resources Migrated from Discord

## Organizing Guides
- [Title]: [URL]
- Security Culture 101: https://crimethinc.com/2004/11/01/
- [Continue with all resources]

## Templates
[Migrate all shared templates]

## Important Links
[Preserve institutional knowledge]
EOF
```

## Step 4: User Migration Process

### Map Discord Roles to New Permissions

```bash
# Create role mapping document
cat > migration/role-mapping.md << 'EOF'
# Discord → New Platform Role Mapping

## Discord Roles → Git + Matrix Permissions

### @admin (Discord) → Repository Owners (Git) + Space Admin (Matrix)
- Can manage all settings
- Merge permissions on protected branches
- Can add/remove other admins

### @organizer (Discord) → Repository Maintainers (Git) + Moderator (Matrix)
- Can merge pull requests
- Can manage issues/discussions
- Can moderate chat rooms

### @member (Discord) → Repository Contributors (Git) + Member (Matrix)
- Can create branches
- Can open pull requests
- Full chat participation

### @new (Discord) → Repository Readers (Git) + Guest (Matrix)
- Read-only Git access
- Limited chat rooms
- Onboarding pathway

## Permission Translation Table

| Discord Permission | Git Equivalent | Matrix Equivalent |
|-------------------|----------------|-------------------|
| Manage Server | Org Owner | Space Admin |
| Manage Channels | Repo Admin | Room Admin |
| Manage Messages | PR Reviewer | Moderator |
| Send Messages | Contributor | Member |
| View Channels | Read Access | Room Access |
| Voice Chat | - | Voice Room Access |
EOF
```

### Batch User Migration Script

```python
#!/usr/bin/env python3
# migrate-users.py - Migrate Discord users to new platforms

import csv
import json
import subprocess

def export_discord_users(guild_id, token):
    """Export Discord user list with roles"""
    # Use discord.py to get member list
    members = []
    # ... discord API calls ...
    
    with open('discord-users.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['username', 'discriminator', 'roles', 'joined_date'])
        for member in members:
            writer.writerow([
                member['username'],
                member['discriminator'],
                ','.join(member['roles']),
                member['joined_at']
            ])
    return 'discord-users.csv'

def create_git_users(csv_file):
    """Create Git access for migrated users"""
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            username = row['username']
            roles = row['roles'].split(',')
            
            # Map Discord roles to Git permissions
            if 'admin' in roles:
                git_role = 'maintainer'
            elif 'organizer' in roles:
                git_role = 'developer'
            else:
                git_role = 'reporter'
            
            # Add to Git platform (GitLab example)
            cmd = f"gitlab user create --username {username} --role {git_role}"
            print(f"Creating Git user: {username} with role: {git_role}")
            # subprocess.run(cmd, shell=True)

def create_matrix_accounts(csv_file, homeserver):
    """Batch create Matrix accounts"""
    accounts_created = []
    
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            username = row['username'].lower()
            # Generate secure random password
            password = generate_secure_password()
            
            # Create Matrix account
            matrix_user = f"@{username}:{homeserver}"
            accounts_created.append({
                'discord_name': row['username'],
                'matrix_id': matrix_user,
                'temp_password': password
            })
    
    # Save credentials securely for distribution
    with open('matrix-accounts.json', 'w') as f:
        json.dump(accounts_created, f, indent=2)
    
    return accounts_created

# Main migration flow
if __name__ == "__main__":
    # 1. Export from Discord
    user_file = export_discord_users(GUILD_ID, TOKEN)
    
    # 2. Create Git accounts
    create_git_users(user_file)
    
    # 3. Create Matrix accounts  
    matrix_accounts = create_matrix_accounts(user_file, "our-homeserver.org")
    
    # 4. Generate migration packets for users
    create_migration_packets(matrix_accounts)
```

### Individual User Migration Packet

```bash
# Generate personalized migration instructions
cat > migration-packets/username-migration.md << 'EOF'
# Your Personal Migration Guide

Welcome to freedom from corporate surveillance!

## Your New Accounts

### Git Repository Access
- URL: https://git.our-org.net
- Username: [your-username]
- Temporary Password: [generated]
- First Login: You'll be prompted to change password

### Encrypted Chat (Matrix/Element)
- Server: https://matrix.our-org.net  
- Username: @[your-username]:our-org.net
- Temporary Password: [generated]
- Download Element: https://element.io

## Quick Start Checklist

- [ ] Log into Git repository
- [ ] Change temporary password
- [ ] Set up 2FA (required within 48 hours)
- [ ] Join Matrix/Element
- [ ] Join #general-migration room
- [ ] Complete tool training (Saturday 2pm)

## Your Discord Data

Your Discord history export: [secure download link - expires in 7 days]

## Support

Need help? Contact:
- Tech support: #migration-help on Matrix
- Or email: tech-support@our-org.net (encrypted)
EOF
```

## Step 5: Coordinate the Migration

### Phase 1: Core Organizers (Week 1)

1. Train security committee on new tools
2. Test workflows with small group
3. Document pain points
4. Create guides for broader membership

### Phase 2: Active Campaigns (Week 2)

Move active work first:
- Current campaign channels
- Upcoming event planning
- Task assignments

### Phase 3: Full Membership (Week 3)

```markdown
# Announcement for #general

@everyone 

**DISCORD LIBERATION BEGINS NOW**

Comrades, we're moving off Discord to protect our organizing from corporate surveillance.

**What's Happening:**
- Discord permanently logs everything (even "deleted" messages)
- Law enforcement regularly subpoenas Discord data
- We're building infrastructure we control

**Action Required:**
1. Join our Matrix space: [link]
2. Attend migration training: [Saturday 2pm]
3. Download channel history if you need it: [deadline]

**Timeline:**
- Now-Sunday: Join new platforms
- Monday: Begin using new tools
- Next Sunday: Discord goes read-only
- Two weeks: Discord deleted

Questions? Ask in #migration-help

Solidarity forever! ✊
```

### Phase 4: Archive and Exit (Week 4)

1. Set all channels to read-only
2. Post final message with new platform info
3. Export full server data (admin only)
4. Delete server entirely

## Step 5: Automation Scripts

### Channel Migration Script

```bash
#!/bin/bash
# migrate-channels.sh - Convert Discord channels to Git structure

EXPORT_DIR="./discord-export"
GIT_REPO="./liberation"

# Create directory structure matching Discord
while IFS= read -r line; do
    category=$(echo "$line" | jq -r '.category')
    channel=$(echo "$line" | jq -r '.name')
    
    # Sanitize names for filesystem
    safe_category=$(echo "$category" | tr ' ' '-' | tr '[:upper:]' '[:lower:]')
    safe_channel=$(echo "$channel" | tr ' ' '-' | tr '[:upper:]' '[:lower:]')
    
    # Create Git directory structure
    if [ "$category" != "None" ]; then
        mkdir -p "$GIT_REPO/$safe_category/$safe_channel"
    else
        mkdir -p "$GIT_REPO/$safe_channel"
    fi
    
    # Process channel exports
    if [ -f "$EXPORT_DIR/channels/$channel.json" ]; then
        python3 process-discord-export.py \
            --input "$EXPORT_DIR/channels/$channel.json" \
            --output "$GIT_REPO/$safe_category/$safe_channel" \
            --format markdown
    fi
done < <(jq -c '.[]' "$EXPORT_DIR/channels.json")

# Commit the migration
cd "$GIT_REPO"
git add .
git commit -m "Migrate Discord channels to Git structure

- Preserved channel organization
- Converted messages to markdown
- Removed personal data for privacy
- Part of liberation from Discord surveillance"
```

### Message Conversion Script

```python
#!/usr/bin/env python3
# process-discord-export.py - Convert Discord JSON to markdown

import json
import argparse
from datetime import datetime
import re
import os

def sanitize_username(author):
    """Remove discriminators and personal info"""
    # Remove #1234 discriminators
    username = re.sub(r'#\d{4}$', '', author.get('name', 'Unknown'))
    # Use nickname if available
    if author.get('nickname'):
        return author['nickname']
    return username

def convert_message(msg):
    """Convert Discord message to markdown format"""
    timestamp = datetime.fromisoformat(msg['timestamp'].replace('Z', '+00:00'))
    author = sanitize_username(msg['author'])
    content = msg['content']
    
    # Convert Discord mentions to generic
    content = re.sub(r'<@!?\d+>', '@member', content)
    content = re.sub(r'<#\d+>', '#channel', content)
    
    # Format as markdown
    formatted = f"**{author}** - {timestamp.strftime('%Y-%m-%d %H:%M')}  \n{content}\n"
    
    # Handle attachments
    if msg.get('attachments'):
        formatted += "\n📎 Attachments:\n"
        for att in msg['attachments']:
            formatted += f"- {att['fileName']} (not migrated for security)\n"
    
    return formatted

def process_channel_export(input_file, output_dir):
    """Process entire channel export"""
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Group messages by date
    messages_by_date = {}
    
    for msg in data['messages']:
        date = msg['timestamp'][:10]  # YYYY-MM-DD
        if date not in messages_by_date:
            messages_by_date[date] = []
        messages_by_date[date].append(msg)
    
    # Create markdown files per day
    for date, messages in messages_by_date.items():
        output_file = os.path.join(output_dir, f"{date}-archive.md")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# Discord Archive - {date}\n\n")
            f.write("*Migrated from Discord - personal data removed for security*\n\n")
            
            # Sort messages by timestamp
            messages.sort(key=lambda x: x['timestamp'])
            
            for msg in messages:
                f.write(convert_message(msg))
                f.write("\n---\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--format', default='markdown')
    
    args = parser.parse_args()
    
    os.makedirs(args.output, exist_ok=True)
    process_channel_export(args.input, args.output)
```

### Verification Script

```bash
#!/bin/bash
# verify-migration.sh - Ensure complete migration

echo "=== Discord Liberation Verification ==="
echo

# Check 1: All channels migrated
echo "Checking channel migration..."
DISCORD_CHANNELS=$(jq -r '.[].name' discord-export/channels.json | wc -l)
GIT_DIRS=$(find liberation -type d -name "*-archive.md" | wc -l)
echo "Discord channels: $DISCORD_CHANNELS"
echo "Git directories: $GIT_DIRS"

# Check 2: User accounts created
echo -e "\nChecking user migration..."
DISCORD_USERS=$(wc -l < discord-users.csv)
MATRIX_ACCOUNTS=$(jq '. | length' matrix-accounts.json)
echo "Discord users: $DISCORD_USERS"
echo "Matrix accounts created: $MATRIX_ACCOUNTS"

# Check 3: Permissions mapped
echo -e "\nChecking permission mapping..."
grep -c "admin" discord-users.csv
grep -c "maintainer" git-permissions.log

# Check 4: No sensitive data in Git
echo -e "\nScanning for sensitive data..."
git grep -E "[0-9]{3}-[0-9]{2}-[0-9]{4}" || echo "✓ No SSNs found"
git grep -E "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b" || echo "✓ No emails found"
git grep -E "#[0-9]{4}" || echo "✓ No Discord discriminators found"

# Generate report
cat > migration-report.md << EOF
# Discord Liberation Report
Generated: $(date)

## Migration Statistics
- Channels migrated: $DISCORD_CHANNELS
- Users migrated: $DISCORD_USERS  
- Messages archived: $(find liberation -name "*.md" -exec wc -l {} + | tail -1)
- Total data size: $(du -sh liberation | cut -f1)

## Verification Results
$([ $DISCORD_CHANNELS -eq $GIT_DIRS ] && echo "✓ All channels migrated" || echo "⚠ Channel count mismatch")
$([ $DISCORD_USERS -eq $MATRIX_ACCOUNTS ] && echo "✓ All users migrated" || echo "⚠ User count mismatch")

## Next Steps
1. Review this report with security committee
2. Conduct user acceptance testing
3. Schedule Discord deletion date
4. Celebrate liberation!
EOF

echo -e "\n✓ Verification complete. See migration-report.md"
```

## Step 6: Establish New Workflows

### Meeting Flow Without Discord

```bash
# Before Meeting
- Agenda in Git repository
- Reminder via Signal/Matrix

# During Meeting
- Jitsi/Mumble for voice
- Collaborative notes in CryptPad
- Screen sharing for documents

# After Meeting
- Minutes committed to Git
- Action items in project management
- No ephemeral Discord chaos
```

### Daily Communication

Replace Discord habits:
- Morning check-ins → Matrix/Signal
- Quick questions → Designated support hours
- Memes → Revolutionary culture channel
- Announcements → Git + secure broadcast

## Common Challenges and Solutions

### "But Discord is convenient!"

**Response**: Convenience for us is convenience for surveillance. Every "easy" feature is a data collection point.

### "Members resist change!"

**Solutions**:
- Lead by example - organizers first
- Buddy system for learning
- Celebrate early adopters
- Make it about collective security, not individual preference

### "We'll lose our history!"

**Actually**: You'll GAIN history. Discord can delete everything tomorrow. Git is forever.

### "Alternative tools are harder!"

**Reality**: They're different, not harder. We learned Discord; we can learn freedom.

## Security Considerations

### During Migration

- Use VPN when downloading Discord data
- Store exports encrypted
- Delete Discord exports after Git migration
- Never put Discord export links in Git

### After Migration

- Audit who has Discord export copies
- Establish retention policy
- Train on new platform security
- Regular security check-ins

## Post-Migration Monitoring

### Week 1 Health Check

```bash
#!/bin/bash
# post-migration-check.sh - Monitor adoption success

echo "=== Post-Migration Health Check ==="

# Active user check
echo "Checking platform adoption..."
ACTIVE_GIT=$(git shortlog -sn --since="1 week ago" | wc -l)
ACTIVE_MATRIX=$(curl -s https://matrix.our-org.net/api/stats | jq '.active_users')

echo "Active Git contributors: $ACTIVE_GIT"
echo "Active Matrix users: $ACTIVE_MATRIX"

# Migration issues tracker
echo -e "\nCommon issues reported:"
grep -c "help" migration-support.log
grep -c "error" migration-support.log
grep -c "confused" migration-support.log

# Success metrics
cat > week-1-report.md << EOF
# Migration Week 1 Report

## Adoption Metrics
- Git users active: $ACTIVE_GIT / $TOTAL_MEMBERS
- Matrix daily active: $ACTIVE_MATRIX / $TOTAL_MEMBERS
- Support tickets: $(wc -l < migration-support.log)

## Wins
- [Document successes]

## Challenges  
- [Document issues]

## Adjustments Needed
- [Action items]
EOF
```

## Verification Checklist

- [ ] All active campaigns migrated
- [ ] Meeting minutes in Git
- [ ] Resources documented
- [ ] Members trained on new tools
- [ ] Discord data exported and secured
- [ ] Server deleted (not just "archived")
- [ ] New workflows documented
- [ ] Security protocols updated
- [ ] Post-migration monitoring active
- [ ] Success metrics tracked

## What You've Accomplished

By completing this migration:
- Removed corporate surveillance from organizing
- Built infrastructure you control
- Practiced collective discipline
- Protected comrades from state repression
- Joined the revolutionary infrastructure movement

## Next Steps

1. **Deepen Security**: [[../../../learn/explanations/why-discord-democracy-fails|Why Discord Democracy Fails]]
2. **Expand Liberation**: [[../../../learn/explanations/signal-isnt-enough|Signal Isn't Enough]]
3. **Build Power**: [[../../../learn/core-concepts/democratic-centralism|Democratic Centralism]]

---

*"The revolutionary doesn't choose comfortable tools - they choose tools for revolution."*

Discord was built for gamers and sold to surveillance.
We're building infrastructure for liberation.