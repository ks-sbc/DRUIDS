---
title: "Git Through Campaign: Workshop Template"
description: "Teaching Git through real organizing scenarios, not abstract tech concepts"
created: 2025-07-05
updated: 2025-07-05
type: "docs/tutorial"
security: "L0"
version: "1.0.0"
document_id: "TUTORIAL-GITWORKSHOP-2025-187-L0"
tags: ["workshop", "git", "teaching", "campaign", "collective-learning", "praxis"]
draft: false
author: ["KSBC Tech Committee"]
navigation_order: 1
---

# Git Through Campaign: Workshop Template

## Material Problem This Solves

Traditional Git tutorials teach commands in a vacuum. Organizers learn to type `git add` without understanding WHY it matters for their work. This leads to:
- **Mechanical usage** without political understanding
- **Fear of Git** as mysterious "programmer tool"
- **Abandoned adoption** when complexity increases
- **Individual heroes** instead of collective capacity

This workshop teaches Git as what it is: **infrastructure for democratic organizing**.

## Political Framing

Git accidentally implements democratic centralism:
- **Branches** = Autonomous working groups
- **Commits** = Meeting minutes and decisions
- **Pull Requests** = Proposals for collective approval
- **Merge** = Unity after democratic debate

By teaching through campaign scenarios, we transform Git from tech tool to organizing weapon.

## Workshop Structure (3 Hours)

### Opening (30 minutes)

#### Set the Scene
"Your tenant union is planning a city-wide rent strike. 50 buildings, 200 organizers, multiple committees. Last time, you lost months of work when Maria's laptop was stolen. This time will be different."

**[EXPAND HERE: Use a campaign relevant to your participants]**

#### Material Conditions Check
Go around the room:
- Who's lost organizing work to tech failure?
- Who's repeated work because they couldn't find the latest version?
- Who's been excluded because they "aren't tech people"?

**[EXPAND HERE: Add questions specific to your organizing context]**

#### Political Line
"We're not learning Git to become programmers. We're learning it to build power. Every command we learn is a brick in our revolutionary infrastructure."

### Part 1: Foundation Through Crisis (45 minutes)

#### Scenario: The Raid
"Police raided the union office. They took computers but not the struggle. How do we recover?"

##### Exercise 1: Clone the Struggle
```bash
# Each organizer clones the repository
git clone https://gitserver.local/tenant-union/rent-strike-2025.git

# Explain: This is why we distribute power
# Every comrade now has complete history
```

**Teaching Points:**
- Decentralization as security practice
- Each clone is complete, not dependent
- Connection to guerrilla cell structure

**[EXPAND HERE: Add local examples of resilience through distribution]**

##### Exercise 2: Check Our Losses
```bash
# See what we have
git log --oneline -20

# Find specific work
git log --grep="eastside buildings"

# Explain: Our memory is collective, not individual
```

**Teaching Points:**
- History as institutional memory
- Searchable record of decisions
- No single point of failure

#### Scenario: Emergency Response
"Landlords just announced mass evictions. We need rapid coordinated response."

##### Exercise 3: Branch the Resistance
```bash
# Legal team starts research
git checkout -b legal-team/eviction-defense

# Outreach prepares flyers
git checkout -b outreach/emergency-flyers

# Direct action plans response
git checkout -b action/building-blockades
```

**Teaching Points:**
- Parallel work without interference
- Autonomy with coordination
- Branch names as political clarity

**[EXPAND HERE: Create branches for your organizing structure]**

### Part 2: Democratic Development (60 minutes)

#### Scenario: Building the Campaign
"Each committee works autonomously but transparently."

##### Exercise 4: Document the Work
```bash
# In legal-team branch
echo "## Eviction Defense Rights" > know-your-rights.md
echo "- You have 30 days to respond" >> know-your-rights.md
git add know-your-rights.md
git commit -m "legal: Add basic tenant rights for eviction defense

Based on city ordinance 24.5.B. Reviewed by volunteer lawyers.
Next: Translate to Spanish, Vietnamese, Somali"
```

**Teaching Points:**
- Commits as meeting minutes
- Clear messages for accountability
- Documentation AS organizing

**[EXPAND HERE: Add commit examples from your campaigns]**

##### Exercise 5: Share the Work
```bash
# Push branch for collective review
git push origin legal-team/eviction-defense

# Create pull request (use UI or CLI)
# Title: "Legal: Eviction defense rights - ready for review"
# Body: 
# - What changed and why
# - Who needs to review
# - Timeline for merge
```

**Teaching Points:**
- Transparency in all work
- Collective ownership
- Review as political education

#### Scenario: Resolving Contradictions
"Outreach and legal have different phone numbers on flyers."

##### Exercise 6: Merge Conflicts as Democracy
```bash
# Try to merge outreach work
git checkout main
git merge outreach/emergency-flyers

# Conflict! This is good - it means we're catching contradictions
# Git shows:
<<<<<<< HEAD
Call hotline: 555-LEGAL-AID
=======
Call hotline: 555-TENANTS-WIN
>>>>>>> outreach/emergency-flyers
```

**Resolution Process:**
1. Stop and discuss (not just pick one)
2. Why different numbers?
3. What serves the campaign?
4. Document decision in commit

**Teaching Points:**
- Conflicts surface contradictions
- Technical process serves political process
- Unity through struggle, not avoidance

**[EXPAND HERE: Add examples of productive conflicts from organizing]**

### Part 3: Campaign in Action (45 minutes)

#### Scenario: Strike Day Coordination
"It's strike day. 50 buildings need real-time coordination."

##### Exercise 7: Rapid Response Cycle
```bash
# Morning: Building captains report
git checkout -b reports/eastside-status
echo "Building 1: 90% participation" > eastside-report.md
git add . && git commit -m "report: Eastside strong, need support at Building 5"
git push origin reports/eastside-status

# Merge quickly for visibility
git checkout main
git merge reports/eastside-status
git push origin main
```

**Real-world practice:**
- Short cycles for rapid response
- Clear commit messages under pressure
- Push early, push often

**[EXPAND HERE: Create rapid scenarios from your actions]**

##### Exercise 8: Victory Documentation
```bash
# Document wins immediately
git checkout -b victory/rent-freeze-won
echo "## WE WON: 6-month rent freeze!" > victory-announcement.md
# Add details, quotes, next steps
git add . && git commit -m "VICTORY: Document rent freeze win for history"
```

**Teaching Points:**
- History written by victors (us)
- Institutional memory of tactics
- Morale through documentation

### Closing Circle (30 minutes)

#### Reflection Questions
1. How does Git change how we organize?
2. What scared you? What excited you?
3. How will you use this in your committee?

#### Commitments
Each participant commits to:
- Teaching one other organizer
- Using Git for one real project
- Joining weekly Git practice sessions

#### Political Synthesis
"Git is not neutral - it embodies collective power. We've learned not just commands but new ways of working together. This is prefigurative politics through technology."

**[EXPAND HERE: Connect to your organization's political principles]**

## Workshop Variations

### For Labor Organizers
- Branches for different shops
- Commits as grievance documentation
- Merges as contract negotiations

### For Community Defense
- Branches for rapid response teams
- Commits as incident reports
- History as evidence collection

### For Revolutionary Study
- Branches for reading groups
- Commits as study notes
- Pull requests as theoretical development

**[EXPAND HERE: Create variations for your movement sectors]**

## Facilitator Notes

### Common Challenges

**"This is too technical!"**
- Return to material problems
- Use physical metaphors (folders, papers)
- Pair technical with political

**"Why not just use Google Docs?"**
- Reference [Why Discord Democracy Fails](../../learn/explanations/why-discord-democracy-fails.md)
- Discuss surveillance capitalism
- Show concrete surveillance risks

**"Our members won't adopt this"**
- Start with willing early adopters
- Show immediate benefits
- Build slowly but surely

**[EXPAND HERE: Add challenges you've encountered]**

### Materials Needed
- Laptops (organize loaner system)
- Git pre-installed (provide installer guide)
- Practice repository set up
- Printed cheat sheets
- Snacks (always snacks)

### Follow-Up Plan
- Weekly practice sessions
- Buddy system for new users
- Real campaign to practice on
- Documentation of learnings

## Remember

We're not teaching Git. We're building revolutionary capacity through Git. Every command is politics. Every commit is praxis. Every merge is democracy.

The revolution will be version controlled.

---

**Ready to run this workshop?** Check [Teaching Without Hierarchy](../../teach/teach-tech-without-priest-hood.md) for facilitation principles.

**Need the technical foundation?** Review [Git in 7 Commands](../../learn/git-basics/git-in-7-commands.md) for yourself first.