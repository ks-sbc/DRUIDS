---
title: "DRUIDS Quick Demo"
description: "See DRUIDS in action in 5 minutes"
created: 2025-07-04
updated: 2025-07-04
type: "docs/tutorial"
security: "L0"
version: "1.0.0"
document_id: "TUT-DEMO-2025-001-L0"
tags: ["demo", "quick-start", "example", "tutorial"]
draft: false
author: ["KSBC Tech Committee"]
navigation_order: 2
---

# DRUIDS in 5 Minutes

This demo shows how DRUIDS solves real organizing problems. Follow along to see the power of revolutionary infrastructure.

## Scenario: Planning a Rent Strike

Your tenant union is planning a rent strike. Let's see how DRUIDS transforms this work.

**Want to learn Git through a complete campaign?** Check out [[git-through-campaign|Git Through Campaign]] for an in-depth tutorial.

### Without DRUIDS (The Old Way)

**Monday** - Emergency meeting about 40% rent increase  
*Maria takes notes in Google Doc #47*

**Wednesday** - Someone "cleans up" the drive  
*Meeting notes are... somewhere?*

**Friday** - "What did we decide?"  
*45 minutes searching emails and docs*

**Next Week** - New member joins  
*"Talk to Maria, Sarah, and check Discord from last month"*

**Month Later** - Maria burns out and leaves  
*Years of knowledge walks out the door*

### With DRUIDS (The Revolutionary Way)

#### Step 1: Document the Meeting (30 seconds)

```bash
# Create meeting notes
druids new meeting --type=emergency

# DRUIDS creates: meetings/2024-11-15-emergency-meeting.md
```

The template appears:
```markdown
# Emergency Meeting - 2024-11-15

## Attendees
- Maria (facilitator)
- Jamal  
- Li (notes)
- 47 other tenants

## Agenda
1. SafeHaven 40% rent increase
2. Formation of tenant union
3. Next steps

## Decisions
- [DECIDED] Form Riverside Tenant Union (unanimous)
- [DECIDED] Demand rent freeze (48-2-0)
- [DECIDED] Next meeting Tuesday Nov 19

## Action Items
- [ ] Maria: Draft demand letter
- [ ] Jamal: Flyer building
- [ ] Li: Create contact sheet
```

#### Step 2: Save Forever (10 seconds)

```bash
# Save to permanent history
druids save "Form tenant union to fight 40% increase"

# Created commit: a3f42d1
```

#### Step 3: Everyone Stays Synchronized

**Jamal's computer:**
```bash
druids pull
# Receives: Emergency meeting notes
```

**New member next week:**
```bash
druids clone riverside-union
# Gets: Complete history, all decisions, context
```

#### Step 4: Find Anything Instantly

**"What did we decide about rent freeze?"**
```bash
druids search "rent freeze"

# Found in commits:
# a3f42d1 - DECIDED: Demand rent freeze (48-2-0)
# b2e1c93 - Research: Average rent increases 2019-2024
# c5d8f22 - Template: Rent freeze demand letter
```

**"Why did previous phone banking fail?"**
```bash
druids search "phone banking lessons"

# Found in: campaigns/2019-phone-banking-retrospective.md
# Key lesson: Started too late, needed 3 week lead time
```

### The Power Revealed

In 5 minutes you've seen:

✅ **Institutional Memory** - Decisions preserved forever  
✅ **Instant Onboarding** - New members productive immediately  
✅ **No Single Point of Failure** - Maria can leave, work continues  
✅ **Searchable History** - Find anything in seconds  
✅ **Democratic Transparency** - See who decided what and when  

## Try It Yourself

### Option 1: Browser Demo (No Installation)
Visit [try.druids.dev](https://try.druids.dev) for an interactive demo
*(Note: Demo environment coming soon)*

### Option 2: Local Quick Start (15 minutes)

```bash
# Install DRUIDS
curl -sSL https://druids.dev/install.sh | bash

# Create your first repository
druids init my-organization

# Create a meeting note
druids new meeting

# Make your first commit
druids save "Our first DRUIDS commit!"
```

## What Makes This Revolutionary?

### 1. You Own Your Infrastructure
- No Google reading your plans
- No Discord forgetting your history  
- No corporate surveillance
- Your data, your control

### 2. Knowledge Compounds Over Time
- Every lesson learned is preserved
- Mistakes aren't repeated
- New campaigns build on old ones
- Experience accumulates

### 3. Democracy in Practice
- Every decision tracked
- Minority positions preserved
- Transparent process
- Accountable leadership

### 4. Sustainable Organizing
- No more burnout from repetition
- Knowledge outlasts individuals
- Onboarding becomes self-service
- Focus energy on new struggles

## Common Questions

**"Is this just Git with templates?"**  
Git is the foundation, but DRUIDS adds:
- Security tiers for sensitive info
- Templates for organizing work
- Integration with friendly tools
- Workflows designed for movements

**"How is this different from Google Docs?"**  
- You control it (not Google)
- History is permanent (not editable)
- Works offline (not cloud-dependent)
- Encrypted options (not surveilled)

**"Do I need to be technical?"**  
If you can:
- Send an email
- Use a word processor
- Follow a recipe

You can use DRUIDS.

## Next Steps

**Ready to implement?**  
→ [[druids-installation-guide|Installation Guide]]

**Want to understand more?**  
→ [[index|Core Concepts]]

**Need to convince others?**  
→ [[why-druids|Why DRUIDS?]]

**Escaping corporate surveillance?**  
→ [[from-google-docs|Migration from Google]]  
→ [[from-discord|Migration from Discord]]

**Ready to teach others?**  
→ [[teach-tech-without-priest-hood|Teaching Without Priesthood]]

---

*In 5 minutes, you've seen how DRUIDS transforms organizing. Imagine what it can do for your movement.*