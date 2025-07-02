---
title: "Pseudonym Discipline in Practice"
description: "How to implement and maintain revolutionary pseudonym discipline for security"
created: 2025-07-02
updated: 2025-07-02
type: "docs/how-to"
security: "L0"
version: "1.0.0"
document_id: "SEC-HOW-2025-001-L0"
tags: ["security", "pseudonyms", "discipline", "how-to", "protection"]
draft: false
author: ["Comrade 47"]
---

# Pseudonym Discipline in Practice

## Context

State surveillance is real. Every organizer arrested, every device seized, every network mapped starts with a name. Pseudonym discipline isn't paranoia - it's revolutionary practice based on material conditions.

## Prerequisites

- Organization committed to security culture
- Basic understanding of surveillance threats
- Git repository configured
- Secure communication channels established

## Step 1: Choose Your Revolutionary Name

### What Makes a Good Pseudonym

**DO**:
- Pick something memorable but not unique
- Use common revolutionary figures (Rosa, Karl, Vladimir)
- Create consistent persona across platforms
- Consider cultural background (don't appropriate)

**DON'T**:
- Use variations of your real name
- Pick something only you would choose
- Use identifying numbers (birth year, address)
- Create joke names that undermine seriousness

### Generate Your Identity

```bash
# Configure Git with pseudonym
git config user.name "Comrade Rosa"
git config user.email "rosa-collective@protonmail.com"

# For organization-wide consistency
git config --global user.name "Comrade Rosa"
```

### Create Secure Email

1. Use Protonmail/Tutanota over Tor
2. Generate random recovery codes
3. Never link to phone or backup email
4. Access only through VPN/Tor

## Step 2: Implement Compartmentalization

### The Three-Circle System

```
Circle 1: Public Organizing (L0)
- Pseudonym: "Rosa"
- Email: rosa-public@protonmail.com
- Known to: Everyone

Circle 2: Internal Work (L1)
- Pseudonym: "R-[City]"
- Email: r-city-secure@tutanota.com
- Known to: Verified members

Circle 3: Sensitive Operations (L2)
- Pseudonym: Rotates
- Email: Single-use addresses
- Known to: Need-to-know only
```

### Maintain Separation

```bash
# Different Git configs for different security levels
# L0 Public work
cd ~/organizing/public-campaigns
git config user.name "Rosa"

# L1 Internal organizing  
cd ~/organizing/internal
git config user.name "R-NYC"

# Never cross-contaminate identities
```

## Step 3: Operational Security Rules

### The Daily Practice

**Morning Check**:
- Which identity am I using today?
- What devices have which identity?
- Any crossover risks?

**Before Every Commit**:
```bash
# Verify identity
git config user.name
# Output should be pseudonym, never real name
```

**Before Every Meeting**:
- Remind comrades of pseudonym use
- Check recording devices
- Establish identity for minutes

### Communication Protocols

```markdown
# Bad - Mixed identities
"Hey, it's Sarah (Rosa), can we meet?"

# Good - Consistent identity
"Rosa here, proposing we meet Thursday"

# Bad - Identity leak
"My roommate (uses real name) can help"

# Good - Maintained separation  
"A trusted comrade can assist"
```

## Step 4: Handle Identity Challenges

### When Someone Slips

**Immediate Response**:
1. Don't panic or overreact
2. Quietly correct: "You mean Rosa?"
3. Edit/redact if in writing
4. Brief private education later

**In Git**:
```bash
# If real name committed accidentally
# DO NOT just amend - history exists

# Create security incident report
cp templates/security-incident-template.md \
   security/incidents/name-leak-2025-07-02.md

# Document and learn
```

### Social Situations

**Challenge**: "What's your real name?"
**Response**: "I go by Rosa in organizing spaces"

**Challenge**: "We're all friends here"
**Response**: "Security culture protects all of us"

**Challenge**: "This is silly paranoia"
**Response**: "Tell that to arrested forest defenders"

### Legal Preparedness

Know your rights:
- You don't have to provide ID in most situations
- "I don't consent to searches"
- "I am exercising my right to remain silent"
- "I want to speak to a lawyer"

Have lawyers who know you by pseudonym.

## Step 5: Digital Infrastructure

### Device Separation

```bash
# Organizing laptop - pseudonym only
# Personal laptop - real name only
# Never mix

# Check all configs
grep -r "YourRealName" ~/organizing/
# Should return nothing
```

### Browser Profiles

Create separate Firefox profiles:
```bash
firefox -ProfileManager

# Create profiles:
# - RosaOrganizing (VPN always)
# - PersonalBrowsing (normal use)
# - ResearchOnly (maximum security)
```

### Metadata Scrubbing

```bash
# Before sharing any files
exiftool -all= document.pdf

# Verify clean
exiftool document.pdf | grep -E "(Author|Creator|Producer)"
```

## Step 6: Build Collective Culture

### Normalize Pseudonyms

**Meeting Introductions**:
"I'm Rosa, she/her, been organizing for 2 years"
NOT: "I'm Sarah but I go by Rosa here"

**Documentation Standards**:
- Always use pseudonyms in minutes
- Create organization style guide
- Make it feel natural through practice

### Security Check-Ins

Weekly security roundup:
- Any close calls?
- Anyone need help with practices?
- New threats to discuss?
- Appreciation for good security

### Mutual Support

- Buddy system for learning
- Correct mistakes with compassion
- Share security wins
- Build culture, not fear

## Common Mistakes and Fixes

### "I forgot which email I used"

**Prevention**: Password manager with notes
```
Entry: Rosa Organizing
Email: rosa-collective@protonmail.com
Used for: Public campaigns, Git commits
Created: 2025-01-15
```

### "Autocomplete exposed my name"

**Fix**: 
1. Clear all browser data
2. Disable autocomplete
3. Use separate profiles
4. Consider browser compartmentalization

### "I used my credit card"

**Response**:
1. Document potential exposure
2. Assess threat level
3. Consider rotating pseudonym
4. Use cash/crypto going forward

## Verification Checklist

- [ ] Git configured with pseudonym only
- [ ] Secure email created and tested
- [ ] Browser profiles separated
- [ ] Devices compartmentalized
- [ ] Team trained on protocols
- [ ] Regular security check-ins scheduled
- [ ] Legal support briefed on pseudonyms
- [ ] Documentation standards updated

## The Political Importance

Pseudonym discipline isn't just personal protection - it's collective resistance:

1. **Breaks surveillance networks**: Can't map what you can't name
2. **Protects the vulnerable**: Some face more risk than others
3. **Practices future operations**: Building habits for escalation
4. **Prefigures new world**: Identity on our terms

## Advanced Considerations

### When to Rotate

- After security incident
- Change in threat level
- Every 6-12 months for L2
- When compromised

### Building Legend

For deeper work:
- Consistent backstory
- Social media presence
- Document trail
- Behavioral patterns

This requires dedicated training.

## Remember

Every slip is a learning opportunity. Every success builds collective security. Every pseudonym is a small act of resistance.

The state names us to control us. We name ourselves for liberation.

---

*"The revolutionary hides their identity not from shame but from wisdom."*

Next steps:
- [Metadata Stripping Pipeline](/how-to/metadata-stripping.md)
- [Security Audits for Organizers](/how-to/security-audits.md)
- [When They Come Knocking](/how-to/raid-response.md)