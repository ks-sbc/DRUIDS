---
title: "When They Come Knocking: DRUIDS Raid Response Procedures"
description: "Practical procedures for protecting organizational infrastructure and comrades during state raids"
created: 2025-07-03
updated: 2025-07-03
type: "docs/how-to"
security: "L1"
version: "1.0.0"
document_id: "INT-HT-2025-422-L1"
tags: ["security", "raid-response", "emergency", "state-repression", "protocols"]
draft: false
author: ["Claude (AI)", "Comrade 47"]
---

# When They Come Knocking: DRUIDS Raid Response Procedures

## Overview

State raids on revolutionary organizations are not paranoia - they're pattern recognition. This guide provides concrete procedures for protecting your DRUIDS infrastructure and comrades when state repression materializes at your door.

## Threat Models by Context

### Labor Organizing
**Threats**: Corporate security, private investigators, police collaboration
**Typical Tactics**: Workplace raids, home visits, device seizure during strikes
**Response Priority**: Protect member lists, wage data, workplace maps

### Tenant Organizing  
**Threats**: Landlord attorneys, eviction squads, local police
**Typical Tactics**: "Welfare checks," code enforcement raids, targeted evictions
**Response Priority**: Protect tenant data, rent strike funds, building plans

### Environmental/Climate
**Threats**: FBI, corporate security, fusion centers
**Typical Tactics**: Terrorism charges, conspiracy claims, infiltration
**Response Priority**: Protect action plans, security culture, affinity groups

### Immigrant Rights
**Threats**: ICE, CBP, local police partnerships
**Typical Tactics**: Workplace raids, home raids, family separation
**Response Priority**: Protect member identities, safe house locations, legal status

### Political Organizations
**Threats**: FBI, NSA, local red squads, grand juries
**Typical Tactics**: Pre-dawn raids, RICO charges, conspiracy theories
**Response Priority**: Protect communications, membership, international connections

## Prerequisites

- Completed security setup (see security guides)
- Emergency contact system established
- Legal support infrastructure
- Practice drills completed

## Before They Come: Preparation

### 1. Distributed Infrastructure

Never have single points of failure:

```bash
# Every organizer should have:
git clone org-repo ~/safe-location/org-backup

# Multiple remotes for resilience
git remote add backup1 git@backup-server1.org:repo.git
git remote add backup2 git@backup-server2.org:repo.git
git remote add emergency comrade@trusted-host:backup.git

# Regular push to all remotes
git push --all backup1
git push --all backup2
git push --all emergency
```

### 2. Emergency Protocols File

Create and memorize:

```bash
# security/emergency/raid-response.md
## If Raided - IMMEDIATE ACTIONS

1. **STAY CALM** - They want you panicked
2. **"I am exercising my right to remain silent"**
3. **"I do not consent to searches"**
4. **"I am requesting a lawyer"**
5. **DO NOT** unlock devices
6. **DO NOT** provide passwords
7. **DO NOT** answer questions

## Legal Support
Emergency Lawyer: [MEMORIZE AND DELETE]
Legal Hotline: [MEMORIZE AND DELETE]
```

### 3. Automated Dead Switch

Set up automatic alerts if you don't check in:

```bash
#!/bin/bash
# scripts/dead-switch.sh
# Run via cron every 24 hours

LAST_CHECKIN=$(cat ~/.druids/last-checkin)
NOW=$(date +%s)
DIFF=$((NOW - LAST_CHECKIN))

# If no check-in for 48 hours
if [ $DIFF -gt 172800 ]; then
    # Send encrypted alert to security committee
    gpg --encrypt --recipient security@org.net < emergency-alert.txt | 
        mail -s "URGENT: Possible Raid" security@org.net
    
    # Trigger infrastructure protection
    ssh backup-server "bash /home/org/lockdown.sh"
fi
```

### 4. Evidence Handling Protocols

Prepare for evidence seizure:

```bash
# What they typically seize
- All electronic devices (phones, laptops, USB drives)
- Paper documents (notebooks, calendars, sticky notes)
- External storage (hard drives, SD cards)
- Routers and network equipment
- SIM cards and burner phones

# Pre-raid preparation
1. Minimize local storage
   - Work from encrypted repos only
   - No local meeting minutes
   - No unencrypted member lists

2. Use deniable encryption
   - Hidden volumes in VeraCrypt
   - Plausible cover data
   - Separate "clean" user accounts

3. Regular data purges
   # Weekly cleanup script
   shred -vfz ~/Documents/temp/*
   rm -rf ~/.cache/*
   history -c
```

### 5. Communication Security Layers

```bash
# Everyday communications
Signal/Element -> Good for daily organizing

# Sensitive planning  
In-person only -> No digital trail

# Post-raid emergency
Briar/Session -> Metadata resistant
Tor + SecureDrop -> Anonymous reporting
```

## During the Raid: Immediate Response

### 1. Personal Protection

**YOUR RIGHTS** (US context - adapt for your jurisdiction):
```
- Remain silent (5th Amendment)
- Refuse searches without warrant (4th Amendment)
- Request lawyer immediately (6th Amendment)
- Do not unlock devices (5th Amendment)
```

**NEVER**:
- Try to destroy evidence during raid (obstruction charge)
- Physically resist (assault charges)
- Lie to federal agents (separate felony)
- Talk to "friendly" agents (there are none)

### 2. Technical Protection

If you have ANY warning:

```bash
# 30 seconds or less procedure
# Practice until muscle memory

# 1. Lock all devices (don't shut down - encryption keys in memory)
Windows+L / Cmd+Control+Q

# 2. If time, trigger panic button
bash ~/.druids/panic.sh

# 3. Close all applications
# Modern full-disk encryption protects locked devices
```

**Panic Script Example**:
```bash
#!/bin/bash
# ~/.druids/panic.sh

# Unmount encrypted volumes
umount /secure/*

# Clear sensitive environment variables
unset DRUIDS_KEY
unset GPG_PASSPHRASE

# Lock password manager
keepassxc --lock

# Send alert to comrades
echo "RAID IN PROGRESS" | 
    gpg --encrypt -r security@org.net | 
    mail -s "URGENT"

# Clear bash history
history -c
```

### 3. Network Alert System

If one comrade is raided, all must know:

```bash
# Designated person outside raid sends:
echo "CODE RED: [Location] compromised. 
Execute security protocol 3." | 
    signal-cli -g EMERGENCY_GROUP send
```

## After the Raid: Damage Assessment

### 1. Immediate Security Audit

Within 24 hours of raid:

```bash
# 1. Assume all local systems compromised
# DO NOT log into anything from raided devices

# 2. From secure device, rotate all credentials
# Start with most critical
- Repository access tokens
- Server SSH keys  
- Email passwords
- Encryption keys

# 3. Check for unauthorized access
git log --all --since="2 days ago"
grep "Failed password" /var/log/auth.log
```

### 2. Infrastructure Recovery

```bash
# From clean device
# 1. Create new repository
git init recovery-repo
git remote add origin new-secure-server:repo.git

# 2. Pull from distributed backups
git remote add backup comrade@trusted:backup.git
git fetch backup
git merge backup/main

# 3. Audit for planted files
git diff HEAD backup/main

# 4. Re-establish secure communications
# Generate new GPG keys
# Distribute through secure channels
```

### 3. Legal Documentation

Document everything for legal defense:

```markdown
## Raid Documentation

**Date/Time**: 2024-03-21 06:30 AM
**Location**: [Organizing space address]
**Agencies Present**: FBI, Local PD
**Warrant**: [Yes/No, scope if known]
**Items Seized**: 
- 3 laptops
- 2 phones
- Paper documents
**Witnesses**: [Pseudonyms]
**Injuries**: [Any violence]
**Statements Made**: [Hopefully none]
```

## Organizational Continuity

### 1. Activate Succession Plan

```bash
# If key organizers arrested
# Pre-designated backups activate

# Transfer repository ownership
git remote set-url origin https://backup-admin@server:repo.git

# Restore from distributed backups
for remote in $(cat ~/.druids/backup-remotes.txt); do
    git fetch $remote
    git merge $remote/main --strategy-option theirs
done
```

### 2. Maintain Operations

Don't let raids stop organizing:

```markdown
## Continuity Checklist

- [ ] Legal support coordinated
- [ ] Bail fund activated
- [ ] Public statement drafted
- [ ] Alternative meeting location secured
- [ ] Members safety-checked
- [ ] Operations resumed within 48 hours
```

### 3. Security Culture Reinforcement

Post-raid meetings should cover:

```markdown
## Security Review Agenda

1. What worked in our response?
2. What failed? 
3. How did they know to raid?
4. What can we improve?
5. Updated protocols needed?

Remember: State wants us paranoid and inactive.
We respond with discipline and continued organizing.
```

## Lessons from History

### COINTELPRO Raids (1960s-70s)
- **Targeted**: Black Panthers, AIM, Puerto Rican independence
- **Tactics**: Pre-dawn raids, planted evidence, assassination
- **Response**: Breakfast programs continued during raids

### Green Scare Raids (2000s)
- **Targeted**: Environmental/animal liberation
- **Tactics**: Grand juries, conspiracy charges, informants
- **Response**: Security culture, support networks

### Recent Raids (2020s)
- **Targeted**: Atlanta forest defenders, Palestinian solidarity
- **Tactics**: RICO charges, social media evidence, drone surveillance
- **Response**: Distributed infrastructure, legal support

## Technical Considerations

### Full Disk Encryption Is Not Enough

If device is on during raid:
- Cold boot attacks can extract keys
- Coercion to unlock ("contempt of court")
- Biometrics can be compelled (use passwords)

### Network Security During Raids

Assume all traffic monitored:
```bash
# Use Tor for any post-raid communications
torify git push backup-repo

# Avoid regular patterns
# Vary times, locations, methods
```

### Distributed Git Protects History

Unlike centralized services:
- Every clone has full history
- Can't be deleted by single raid
- Cryptographic integrity preserved
- Recovery possible from any copy

## Drill Procedures

Practice monthly until automatic:

### 10-Minute Raid Drill

1. **Alert sounds**
2. **Lock all devices** (time it!)
3. **Execute panic script**
4. **Practice rights assertion**
5. **Designate who calls lawyer**
6. **Review and improve**

### Infrastructure Recovery Drill

1. **Simulate seized devices**
2. **Recovery from backups**
3. **Credential rotation**
4. **Communication re-establishment**
5. **Operations resumption**

## Digital Forensics Awareness

### What They Can Recover

Even after deletion:
```bash
# They can recover:
- Deleted files (up to years later)
- Browser history (even "private" mode)
- WiFi connection history
- USB device history
- Clipboard history
- Thumbnail caches
- Swap file contents
- Hibernation files

# They cannot recover (if done right):
- Properly shredded files (shred -vfz)
- Full-disk encrypted data (if powered off)
- Data overwritten multiple times
- RAM contents after power off
```

### Counter-Forensics

```bash
# Before any sensitive work
# 1. Boot from USB/Tails
# 2. Work in RAM only
# 3. No persistent storage
# 4. Shutdown (not sleep) when done

# Regular maintenance
# Clear all forensic traces
sudo swapoff -a
sudo swapon -a  # Clear swap
rm -rf ~/.local/share/recently-used.xbel
rm -rf ~/.thumbnails/*
bleachbit --clean system.* firefox.*
```

## Grand Jury Resistance

### Understanding Grand Juries

Federal prosecutors use grand juries to:
- Force testimony (no 5th Amendment)
- Gather intelligence on movements
- Create informants through pressure
- Map organizational structures

### Resistance Strategies

```markdown
## If Subpoenaed to Grand Jury

1. **Get a lawyer immediately**
   - Specialized in grand jury resistance
   - Experience with political cases

2. **Solidarity approach**
   - Refuse to testify about others
   - "I will not participate in this fishing expedition"
   - Accept contempt charges if necessary

3. **Know the consequences**
   - Up to 18 months jail for contempt
   - No conviction, just coercion
   - Released when grand jury expires

4. **Community support needed**
   - Legal fund
   - Jail support
   - Public pressure campaign
```

## Special Considerations

### For Undocumented Comrades
- Higher stakes (deportation)
- Separate legal support needed
- Consider remote participation
- Extra identity protection
- Know your ICE raid rights

### For Public Organizers
- Expect targeting
- Maintain nothing locally
- All work in encrypted repos
- Regular device swaps
- Public vs private persona separation

### For Technical Maintainers
- You're high-value targets
- Maximum security practices
- Dead switches mandatory
- Succession planning critical
- Consider pseudonymous maintenance

### For Parents/Caregivers
- Child protective services threats
- Emergency childcare plans needed
- Legal custody documentation ready
- Support network activated

### For People with Disabilities
- Medication access during detention
- Accessibility needs documentation
- Medical advocate designated
- Adaptive equipment protection

## Building Resilient Infrastructure

The goal isn't paranoia but preparedness:

```bash
# Daily: Push to multiple remotes
# Weekly: Security check-in
# Monthly: Raid drills  
# Quarterly: Full security audit
# Annually: Infrastructure evolution
```

## Remember

1. **They raid to intimidate** - Don't let them
2. **Silence is golden** - Seriously, shut up
3. **Infrastructure survives** - If properly distributed
4. **We continue organizing** - That's the victory
5. **Solidarity is strength** - Support raided comrades

The state has resources, but we have resilience. Every raid they conduct teaches us to build better infrastructure. Every comrade they arrest inspires two more to join.

*"You can jail a revolutionary, but you can't jail the revolution."* - Fred Hampton

Build infrastructure that survives when they come knocking. Because they will come knocking. And we'll keep building.

## Emergency Contacts Template

```bash
# Memorize and destroy
# security/contacts/emergency.asc (encrypted)

Legal:
- Lawyer Name: [Memorize]
- Emergency #: [Memorize]
- Backup Legal: [Memorize]

Security Committee:
- Primary: [Signal Username]
- Secondary: [Signal Username]  
- Emergency: [Encrypted Email]

Safe Houses:
- Location A: [Memorize]
- Location B: [Memorize]
```

Stay ready. Stay vigilant. Keep organizing.

## Quick Reference Card

Print, laminate, and keep accessible:

```
═══════════════════════════════════════════
        RAID RESPONSE QUICK REFERENCE
═══════════════════════════════════════════

IF THEY'RE AT THE DOOR:
1. Stay calm, breathe deeply
2. Lock all devices (Win+L / Cmd+Ctrl+Q)
3. "I need to see a warrant"

MAGIC WORDS (REPEAT ONLY THESE):
• "I am exercising my right to remain silent"
• "I do not consent to searches"  
• "I want to speak to a lawyer"

DO NOT:
• Answer ANY questions
• Unlock ANY devices
• Sign ANYTHING
• Lie or resist physically

DEVICES:
• Powered off = Good (encrypted)
• Locked = Okay  
• Unlocked = Bad
• Biometrics = Disable NOW

EMERGENCY CONTACTS:
Lawyer: [Memorize number]
Security: [Signal username]
Bail fund: [Memorize number]

AFTER THEY LEAVE:
1. Document everything
2. Contact lawyer
3. Alert security committee
4. DO NOT log into accounts

═══════════════════════════════════════════
```