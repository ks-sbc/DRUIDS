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

```python
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

## Step 4: Coordinate the Migration

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

## Step 5: Establish New Workflows

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

## Verification Checklist

- [ ] All active campaigns migrated
- [ ] Meeting minutes in Git
- [ ] Resources documented
- [ ] Members trained on new tools
- [ ] Discord data exported and secured
- [ ] Server deleted (not just "archived")
- [ ] New workflows documented
- [ ] Security protocols updated

## What You've Accomplished

By completing this migration:
- Removed corporate surveillance from organizing
- Built infrastructure you control
- Practiced collective discipline
- Protected comrades from state repression
- Joined the revolutionary infrastructure movement

## Next Steps

1. **Deepen Security**: [Pseudonym Discipline in Practice](/how-to/pseudonym-discipline.md)
2. **Expand Liberation**: [Signal Isn't Enough](/explanation/signal-limits.md)
3. **Build Power**: [Git as Democratic Centralism](/explanation/git-democracy.md)

---

*"The revolutionary doesn't choose comfortable tools - they choose tools for revolution."*

Discord was built for gamers and sold to surveillance.
We're building infrastructure for liberation.