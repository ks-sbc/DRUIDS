---
title: "Git Through a Campaign"
description: "Learn Git by following a tenant union's rent strike campaign from start to victory"
created: 2025-07-04
updated: 2025-07-04
type: "docs/tutorial"
security: "L0"
version: "1.0.0"
document_id: "TUT-GIT-2025-003-L0"
tags: ["tutorial", "git", "campaign", "story-based", "rent-strike"]
draft: true
author: ["Comrade 47"]
---

# Git Through a Campaign

*Learn Git by following the Riverside Tenant Union through their victorious rent strike campaign*

## You're Not Just Learning Git

You're learning how to preserve struggle, build on victories, and never lose hard-won knowledge again. This tutorial follows a real campaign structure, teaching Git through the actual work of organizing.

## Meet Your Comrades

**Maria** - Lead organizer, been fighting slumlords for 5 years  
**Jamal** - New member, great at talking to neighbors  
**Li** - Takes amazing notes, never misses a detail  
**You** - Ready to learn Git while organizing  

## Chapter 1: The Campaign Begins

### Day 1: First Meeting

Maria calls an emergency meeting. SafeHaven Corp just announced a 40% rent increase. Tenants are furious but disorganized.

Li takes notes in a Google Doc. By Day 3, they can't find the doc. Someone "cleaned up" the shared drive. Again.

**Maria**: "We can't keep losing our history. We need Git."

### Your First Git Steps

```bash
# Create a folder for the campaign
mkdir riverside-rent-strike
cd riverside-rent-strike

# Initialize Git repository
git init
```

**What just happened?** You created a filing cabinet (repository) that never forgets.

```bash
# Check what's happening
git status
```

Output:
```
On branch main
No commits yet
nothing to commit
```

**Translation**: "New filing cabinet ready. Nothing filed yet."

### Document the First Meeting

Create your first file:

```bash
# Create meetings folder
mkdir meetings

# Create first meeting notes
echo "# Riverside Rent Strike - Emergency Meeting" > meetings/2024-11-15-emergency.md
echo "" >> meetings/2024-11-15-emergency.md
echo "## Attendees" >> meetings/2024-11-15-emergency.md
echo "- Maria (facilitator)" >> meetings/2024-11-15-emergency.md
echo "- Jamal" >> meetings/2024-11-15-emergency.md
echo "- Li (notes)" >> meetings/2024-11-15-emergency.md
echo "- 47 other tenants" >> meetings/2024-11-15-emergency.md
echo "" >> meetings/2024-11-15-emergency.md
echo "## Decisions" >> meetings/2024-11-15-emergency.md
echo "1. Form Riverside Tenant Union" >> meetings/2024-11-15-emergency.md
echo "2. Demand: Freeze rent at current levels" >> meetings/2024-11-15-emergency.md
echo "3. Next meeting: Tuesday Nov 19" >> meetings/2024-11-15-emergency.md
```

### Save History Forever

```bash
# See what Git notices
git status
```

Output shows:
```
Untracked files:
  meetings/2024-11-15-emergency.md
```

**Translation**: "I see new files. Want to save them?"

```bash
# Add to staging area
git add meetings/

# Commit to history
git commit -m "Add emergency meeting notes - union formed, 40% increase opposed"
```

🎉 **First Victory!** You've preserved your first piece of organizing history.

## Chapter 2: Building Momentum

### Day 5: Outreach Begins

Jamal has been talking to neighbors. He has notes on napkins, phone notes, scattered everywhere.

**You**: "Let's track our outreach in Git."

```bash
# Create outreach directory
mkdir outreach

# Create contact tracking
cat > outreach/building-contacts.md << 'EOF'
# Building Contacts

## Building A
- Apt 101: Interested, needs Spanish materials
- Apt 102: Very engaged, wants to help organize  
- Apt 103: Scared of retaliation
- Apt 104: No answer

## Building B
- Apt 201: Already can't afford rent
- Apt 202: Supportive but traveling
- Apt 203: Wants to know more
- Apt 204: Landlord's friend - skip
EOF

# Track it
git add outreach/
git commit -m "Track outreach progress - Building A and B initial contacts"
```

### See Your History

```bash
git log --oneline
```

Output:
```
a3f42d1 Track outreach progress - Building A and B initial contacts
b2e1c93 Add emergency meeting notes - union formed, 40% increase opposed
```

**You're building institutional memory!** Every door knocked, every conversation, preserved.

## Chapter 3: Parallel Organizing

### Day 8: Teams Form

The union splits into working groups:
- **Outreach Team** (Jamal leads)
- **Research Team** (Li leads)  
- **Direct Action Team** (Maria leads)

Each team needs to work independently but stay coordinated.

### Enter: Branches

```bash
# Create branch for outreach team
git checkout -b outreach-team

# Jamal's team adds more contacts
cat >> outreach/building-contacts.md << 'EOF'

## Building C
- Apt 301: Enthusiastic! Wants to organize their floor
- Apt 302: Undocumented, worried but supportive
- Apt 303: Offered living room for meetings
- Apt 304: Will join if others do
EOF

git add outreach/building-contacts.md
git commit -m "Add Building C contacts - found meeting space in 303!"
```

Meanwhile, Li's team works on research:

```bash
# Switch to new branch
git checkout main
git checkout -b research-team

# Create research directory
mkdir research

# Document findings
cat > research/safehaven-violations.md << 'EOF'
# SafeHaven Corp Code Violations

## Building A
- 15 health code violations unaddressed
- Heating system failed inspection 2019, 2021, 2023
- Mold in 6 units reported, no remediation

## Building B  
- Fire exits blocked (illegal)
- No hot water for 3 months in 2023
- Rat infestation reports ignored

## Sources
- City inspection records (public database)
- Tenant photos and documentation
- Health department complaints
EOF

git add research/
git commit -m "Document SafeHaven violations - major health and safety issues"
```

### See Your Branches

```bash
git branch
```

Output:
```
  main
  outreach-team
* research-team
```

**What's happening?** Three parallel workstreams, no stepping on toes!

## Chapter 4: Coming Together

### Day 12: Merge the Work

Teams reconvene. Everyone's work needs to combine for the big tenant meeting.

```bash
# Go back to main
git checkout main

# Merge outreach work
git merge outreach-team
# Merging happens automatically!

# Merge research work  
git merge research-team
# Also automatic!

# See combined work
ls
```

Now you have:
```
meetings/  outreach/  research/
```

All work preserved, all teams credited, no information lost!

## Chapter 5: The Conflict

### Day 15: Disagreement on Demands

Two groups emerge with different demands documents:

**Group 1** (Maria's draft):
```bash
git checkout -b demands-militant

cat > demands.md << 'EOF'
# Riverside Tenant Union Demands

1. Immediate rent freeze
2. 50% rent reduction for code violations
3. Tenant committee approval for any increases
4. Right to organize without retaliation
EOF

git add demands.md
git commit -m "Draft militant demands - 50% reduction"
```

**Group 2** (Moderate draft):
```bash
git checkout main
git checkout -b demands-moderate

cat > demands.md << 'EOF'
# Riverside Tenant Union Demands

1. Rent increase capped at 5%
2. 30-day notice for any changes
3. Monthly building inspections
4. Good faith negotiations
EOF

git add demands.md
git commit -m "Draft moderate demands - 5% cap"
```

### The Merge Conflict

At the meeting, both proposals are discussed. Through democratic debate, a unified position emerges:

```bash
git checkout main
git merge demands-militant
```

Git responds:
```
Auto-merging demands.md
CONFLICT (add/add): Merge conflict in demands.md
```

**Don't panic!** This is democracy in action.

Look at the file:
```bash
cat demands.md
```

You see:
```
<<<<<<< HEAD
=======
# Riverside Tenant Union Demands

1. Immediate rent freeze
2. 50% rent reduction for code violations
3. Tenant committee approval for any increases
4. Right to organize without retaliation
>>>>>>> demands-militant
```

### Resolve Through Democracy

After debate, the union votes. Edit the file to reflect collective decision:

```bash
cat > demands.md << 'EOF'
# Riverside Tenant Union Demands

1. Immediate rent freeze for all tenants
2. 50% rent reduction until code violations fixed
3. Tenant committee approval for future increases
4. Right to organize without retaliation
5. All negotiations public with tenant observers
EOF

# Mark conflict resolved
git add demands.md
git commit -m "Merge demands after democratic vote - unified position"
```

## Chapter 6: Campaign Intensifies

### Day 20: Shifting Tactics

SafeHaven ignores demands. Time for escalation. Maria creates action plans:

```bash
git checkout -b direct-action

mkdir actions
cat > actions/phase-1-pressure.md << 'EOF'
# Phase 1: Building Pressure

## Week 1: Visibility
- Banner drop from Building C
- Flyers in neighborhood
- Social media campaign

## Week 2: Disruption  
- Picket at SafeHaven offices
- Calls to board members
- Media outreach

## Week 3: Escalation
- Rent strike begins
- Letter to city officials
- Know Your Rights trainings
EOF

git add actions/
git commit -m "Plan Phase 1 pressure campaign"
```

### Sharing the Plan

```bash
# Push to shared repository
git push origin direct-action
```

Now organizers in other buildings can:
```bash
git pull
git checkout direct-action
```

Everyone stays coordinated. No "Did you get my email?" No "Which version is latest?"

## Chapter 7: Victory Through History

### Day 45: Leverage from the Past

City council meeting tomorrow. Li remembers something:

```bash
git log --grep="violations"
```

Finds:
```
d4f3a21 Document SafeHaven violations - major health and safety issues
```

```bash
git show d4f3a21
```

The detailed violations list from Day 8! Li presents it to council with photos. City inspectors launch investigation.

### Day 50: We Win!

SafeHaven caves:
- Rent frozen for 2 years
- Violations must be fixed
- Tenant committee recognized

Document the victory:

```bash
cat > victory-announcement.md << 'EOF'
# WE WON!

After 50 days of organizing:
- ✊ Rent frozen for 2 years
- ✊ All violations must be fixed in 90 days
- ✊ Tenant committee officially recognized
- ✊ No retaliation pledge signed

## Key to Victory
- 95% tenant participation
- Documented history of violations  
- United demands
- Strategic escalation

The struggle continues, but today we celebrate!
EOF

git add victory-announcement.md
git commit -m "VICTORY! Document win - 2 year freeze achieved"
```

## Chapter 8: The Knowledge Lives On

### Six Months Later

New organizer joins. Instead of spending weeks catching up:

```bash
# Clone the repository
git clone https://github.com/riverside-union/rent-strike.git

# See the entire campaign
git log --oneline

# Find specific information
git log --grep="contact" # All outreach
git log --grep="violation" # All research
git log --grep="action" # All tactics
```

In one day, they understand:
- How the campaign developed
- What tactics worked
- Who did what
- Why decisions were made

**The institution remembers, even when individuals move on.**

## Your Git Journey

Through this campaign, you learned:

✅ `git init` - Start tracking history  
✅ `git add` - Stage changes  
✅ `git commit` - Save forever  
✅ `git branch` - Parallel organizing  
✅ `git merge` - Unite work  
✅ `git log` - Search history  
✅ `git push/pull` - Share with comrades  

But more importantly, you learned:
- **History is power**
- **Parallel work multiplies capacity**  
- **Conflicts resolve through democracy**
- **Knowledge compounds over time**

## Practice Your Skills

Try these exercises using the campaign structure:

1. **Create a branch** for planning next campaign
2. **Document** lessons learned
3. **Merge** different strategic proposals  
4. **Search** for specific decisions
5. **Share** with other tenant unions

## The Real Victory

Git isn't about commands. It's about ensuring that every hour spent organizing, every lesson learned, every victory won becomes part of permanent revolutionary infrastructure.

SafeHaven thought tenant memory was short. They were wrong. The repository remembers.

## Next Steps

1. Start using Git for your real organizing
2. Read [Daily Git for Meeting Notes](/how-to/git-for-meeting-notes.md)
3. Learn [Git Workflows by Role](/how-to/git-workflows-by-role.md)
4. Teach another organizer

---

*"The people, united, will never be defeated - especially when they use version control"*

Ready to preserve your own struggles? The revolution will be committed.