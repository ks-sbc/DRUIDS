---
title: "Institutional Memory and Onboarding - Key DRUIDS Value Props"
description: "Understanding how DRUIDS solves the two critical pain points organizations face"
created: 2025-07-03
updated: 2025-07-03
type: "docs/reference"
security: "L0"
version: "1.0.0"
document_id: "INT-REF-2025-411-L0"
tags: ["institutional-memory", "onboarding", "pain-points", "value-proposition"]
draft: false
author: ["Comrade 47"]
---

# Institutional Memory and Onboarding - Key DRUIDS Value Props

*These are the two things comrades care deeply about. This document explains how DRUIDS addresses them.*

## The Two Critical Pain Points

### 1. Institutional Memory Loss

**The Problem**:
- Sarah leaves → passwords gone
- Mike burns out → campaign history lost  
- Rosa moves cities → years of context vanishes
- New members ask "why don't we do X?" → "We tried in 2019 but I forget why it failed"

**The Material Cost**:
- Repeated failures from forgotten lessons
- Endless re-litigation of settled questions
- Tribal knowledge in few heads
- Organizational alzheimer's

**How DRUIDS Solves It**:

```bash
# Traditional organizing memory:
"Ask Sarah about the phone tree campaign"
"Sarah left 6 months ago"
"..."

# DRUIDS organizing memory:
git log --grep="phone tree"
# commit 3a4f2d1 2019-03-15
# Stop phone tree campaign - analysis
# - Only reached 30% of members
# - Required dedicated coordinator
# - Signal groups more effective
# See campaigns/2019/phone-tree-retrospective.md
```

Every decision preserved. Every lesson searchable. Every failure educational.

### 2. Onboarding Nightmare

**The Problem**:
- New member joins excited → 3 months later still confused
- "How do things work here?" → 20 different answers
- Information scattered across Discord/Signal/Google/brains
- Old-timers exhausted from explaining basics

**The Material Cost**:
- Months from joining to contributing
- Burnout from constant explanation
- Inconsistent organizational culture
- High dropout rate from confusion

**How DRUIDS Solves It**:

```bash
# Day 1 for new member:
git clone org-repo
cd org-repo
cat README.md  # Orientation in 5 minutes

# Day 2:
ls meetings/  # See all meeting history
git log --oneline -20  # Recent organizational activity

# Day 3:
cp templates/proposal-template.md my-first-proposal.md
# Already contributing!
```

## Concrete Examples

### Institutional Memory in Action

**Scenario**: Rent strike proposal in 2025

**Without DRUIDS**:
- "Didn't we try this before?"
- "I think so but not sure when"
- "Ask Jamie... oh they moved"
- Proceed to repeat 2021's failures

**With DRUIDS**:
```bash
git log --grep="rent strike"
# Shows:
# - 2021 attempt (failed: no legal support)
# - 2022 attempt (partial success: 3 buildings)
# - Lessons learned documents
# - Contact info for lawyers who helped

# New proposal builds on history:
"Based on 2022's partial success (see commit a4f3d21), 
this proposal addresses the legal support gap that 
caused 2021's failure..."
```

### Onboarding in Action

**Scenario**: Alex joins the organization

**Without DRUIDS**:
- Week 1: "Welcome! Talk to Sarah about passwords"
- Week 2: "Check Discord for last month's discussion"
- Week 3: "I think the bylaws are in someone's Google Drive"
- Month 2: Still asking basic questions
- Month 3: Finally somewhat productive

**With DRUIDS**:
- Day 1: Clone repo, read README
- Day 2: Read last 3 meeting minutes
- Day 3: Understand current campaigns from proposals/
- Day 4: First commit fixing typo
- Week 1: Submit first proposal using template
- Week 2: Facilitate first meeting using template

## The Key Differentiators

### For Institutional Memory

**Not Just Storage** - Active, Searchable Wisdom:
- Git grep finds any decision ever made
- Blame shows who made each choice and when
- Log connects decisions to context
- Branches preserve minority positions

**Not Just History** - Living Documentation:
- Templates encode organizational culture
- Commit messages explain reasoning
- Failed branches show what didn't work
- Success patterns emerge from repetition

### For Onboarding

**Not Just Documentation** - Self-Service Learning:
- New members explore at their pace
- Questions become specific, not general
- Templates teach by example
- Git workflow teaches democratic process

**Not Just Information** - Cultural Transmission:
- Commit style shows communication norms
- Meeting minutes demonstrate process
- Proposals reveal strategic thinking
- Security practices embedded in structure

## How to Convey This Message

### For Institutional Memory

**The Amnesia Metaphor**:
> "Your organization has alzheimer's. Every time someone leaves, you forget years of lessons. DRUIDS is organizational memory that can't walk out the door."

**The Wikipedia Comparison**:
> "Wikipedia never forgets an edit. Why does your organization forget every decision? DRUIDS makes your organizing history searchable and learnable."

**The Concrete Example**:
> "In 2019, you tried a phone tree. Failed. In 2021, new members proposed a phone tree. In 2023, newer members proposed a phone tree. With DRUIDS, they'd search 'phone tree' and find three retrospectives explaining exactly why it doesn't work for your organization."

### For Onboarding

**The First Day Comparison**:
> "Traditional: 'Welcome! Ask around if you need anything.' 
> DRUIDS: 'Welcome! Clone this repo. Everything you need is there.'"

**The Productivity Timeline**:
> "Most organizations: 3 months to productivity.
> DRUIDS organizations: 3 days to first contribution."

**The Self-Service Liberation**:
> "Stop making old-timers explain everything. New members can answer their own questions by exploring organizational history. When they do ask questions, they're specific and advanced."

## The Power Steering Connection

Remember: DRUIDS doesn't tell you WHERE to go (that's ideology). It just ensures you don't forget HOW you got here or lose passengers along the way.

- **Institutional Memory** = GPS tracking where you've been
- **Onboarding** = Passenger seats that adjust automatically
- **Both Together** = Arriving at revolution with everyone aboard and knowing the route

## Summary for Comrades

When explaining DRUIDS, lead with these two pain points:

1. **"Tired of losing everything when someone leaves?"** → Institutional Memory
2. **"Tired of explaining everything to new people?"** → Onboarding

These are universal organizing pains. DRUIDS solves both through Git's inherent properties, not through complex features. Simple infrastructure, revolutionary results.

## Learn More

- **See the theory:** [Institutional Memory and Revolutionary Capacity](../core-concepts/institutional-memory.md)
- **Get hands-on:** [Your First Revolutionary Commit](../tutorials/your-first-revolutionary-commit.md)
- **Find your path:** [Git Learning Path](../git-learning-path.md)
- **Implement in your org:** [Implementation Guide](../../implement/index.md)
- **See it in action:** [Quick Demo](../../start/quick-demo.md)