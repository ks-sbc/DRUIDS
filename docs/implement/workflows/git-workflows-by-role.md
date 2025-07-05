---
title: "Git Workflows by Role"
description: "Role-specific Git patterns for facilitators, coordinators, and secretaries. Learn the workflows that match your organizing responsibilities."
created: 2025-07-05
updated: 2025-07-05
type: "docs/how-to"
security: "L0"
version: "1.0.0"
document_id: "HTG-WFL-2025-188-L0"
tags: ["git", "workflows", "roles", "facilitator", "coordinator", "secretary", "patterns"]
draft: false
author: ["KSBC Tech Committee"]
navigation_order: 2
---

# Git Workflows by Role

## Your Role Shapes Your Workflow

Different organizing roles need different Git patterns. This guide maps your responsibilities to specific workflows, making Git serve your actual work rather than forcing you into generic patterns.

**Before diving in, understand** → [Why Git matters for organizers](../../learn/git-basics/why-revolutionaries-need-git.md)

## Quick Reference by Role

| Role | Primary Git Tasks | Key Commands | Complexity |
|------|------------------|--------------|------------|
| **Secretary** | Document meetings, track decisions | `git add`, `git commit`, `git push` | Basic → Intermediate |
| **Facilitator** | Manage proposals, merge decisions | `git branch`, `git merge`, `git tag` | Intermediate |
| **Coordinator** | Track tasks, integrate work | `git log`, `git merge`, `git branch` | Intermediate → Advanced |
| **Tech Support** | Maintain infrastructure, help others | All commands + recovery | Advanced |
| **New Member** | Read docs, suggest changes | `git pull`, `git add`, `git commit` | Basic |

## Visual Workflow Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    ROLE-BASED GIT WORKFLOWS                  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Secretary Flow:                                             │
│  [Meeting] → [Document] → [Commit] → [Push] → [Archive]     │
│      ↓                                          ↑            │
│  [Real-time notes] → [Clean up] → [Final version]           │
│                                                              │
│  Facilitator Flow:                                           │
│  [Proposals] → [Branches] → [Discussion] → [Merge] → [Tag]  │
│       ↓              ↓            ↓           ↑              │
│  [Review] → [Amendments] → [Vote] → [Decision]              │
│                                                              │
│  Coordinator Flow:                                           │
│  [Plan] → [Assign] → [Track] → [Integrate] → [Report]       │
│     ↓         ↓         ↓          ↓           ↑            │
│  [Branches] [Tasks] [Progress] [Merge] → [Evaluate]         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## New Member: Starting Your Git Journey

### Your Revolutionary Responsibility

As a new member, you're learning both organizing and Git. Start simple, build confidence, contribute early.

### Week 1: Read and Learn

```bash
# Your first commands (just 3!)
git clone https://github.com/your-org/organizing-docs.git
cd organizing-docs
git pull

# Read everything
ls
cat README.md
# Open files in your favorite editor
```

### Week 2: Your First Contribution

```bash
# Get latest updates
git pull

# Make your first edit (fix a typo, add your name)
nano members/roster.md
# Add your pseudonym to the list

# Save your change
git add members/roster.md
git commit -m "Add [YourPseudonym] to member roster"

# Share with collective
git push
```

### Week 3: Suggest Improvements

```bash
# Create your first branch
git checkout -b suggestion/improve-meeting-template

# Edit the template
nano templates/meeting-template.md
# Add something that would help new secretaries

# Save and push
git add templates/meeting-template.md
git commit -m "Add attendance tracking section to meeting template"
git push origin suggestion/improve-meeting-template

# Ask someone to review in next meeting
```

### Progressive Learning Path

```
Week 1-2: Clone → Pull → Read
Week 3-4: Edit → Add → Commit → Push  
Week 5-6: Branch → Merge request
Week 7-8: Review others' changes
Week 9+:  Choose specialized role
```

### Common New Member Concerns

**"What if I break something?"**
- Git saves everything - nothing is truly lost
- Work in branches until confident
- Ask for help early and often

**"The commands seem complicated"**
- You only need 7 commands to start
- Copy-paste is fine while learning
- Repetition builds muscle memory

**"I don't understand the messages"**
- Error messages are learning opportunities
- Screenshot and ask in tech support channel
- Most errors have simple fixes

## Secretary: Documenting Collective Memory

### Your Revolutionary Responsibility

As secretary, you're the guardian of institutional memory. Every meeting, every decision, every lesson learned flows through your documentation.

### Progressive Complexity for Secretaries

#### Level 1: Basic Meeting Documentation (Weeks 1-4)

Just focus on capturing and saving:

```bash
# Before meeting
git pull
cp templates/meeting-template.md meetings/today-meeting.md

# After meeting  
git add meetings/today-meeting.md
git commit -m "Add notes from today's general meeting"
git push
```

#### Level 2: Structured Documentation (Weeks 5-8)

Add organization and tracking:

```bash
# Use meaningful filenames
cp templates/meeting-template.md meetings/2024-11-20-general.md

# Commit with descriptive messages
git add meetings/2024-11-20-general.md
git commit -m "General meeting: Decided on rent strike, assigned coordinators"
git push
```

#### Level 3: Real-time Documentation (Weeks 9-12)

Commit during meetings for transparency:

```bash
# After each major decision
git add meetings/2024-11-20-general.md
git commit -m "DECIDED: Rent strike begins Dec 1 (vote: 18-3-2)"

# After action items
git commit -m "Assigned: Maria leads legal committee, Chen does outreach"
```

#### Level 4: Advanced Secretary Patterns (Months 3+)

Full workflow mastery:

```bash
# Create meeting branch
git checkout -b meeting/2024-11-20-general

# Multiple commits during meeting
git add -p  # Stage specific sections
git commit -m "Document pre-meeting announcements"
git commit -m "Capture proposal discussion points"
git commit -m "Record vote results and dissenting opinions"

# Clean up and merge
git checkout main
git merge meeting/2024-11-20-general
```

### Daily Workflow

#### Before the Meeting

```bash
# Start fresh with latest information
git pull origin main

# Create a branch for today's meeting
git checkout -b meeting-2024-11-20-general

# Set up the meeting document
cp templates/meeting-template.md meetings/2024-11-20-general.md
nano meetings/2024-11-20-general.md
```

#### During the Meeting

**Live Documentation Pattern**:

```markdown
# Eastside Tenant Union - General Meeting
**Date**: 2024-11-20
**Facilitator**: Maria
**Secretary**: Chen
**Attendees**: 23 members present

## Agenda
1. Report back: Building C organizing
2. Vote: Rent strike demands
3. Planning: Next week's actions

## Decisions
DECIDED[general-meeting](18-3-2): Approve rent strike demands as amended
- Majority felt demands were strategic
- Minority wanted more militant approach
- See proposals/rent-strike-demands-v3.md for full text

## Action Items
- [ ] Maria: Schedule legal consultation by Nov 22
- [ ] James: Coordinate Building C tenant meeting
- [ ] Chen: Distribute demands to all buildings
```

**Commit After Each Major Decision**:

```bash
# After vote on demands
git add meetings/2024-11-20-general.md
git commit -m "Document rent strike demands vote: 18-3-2 approval"

# After action items assigned
git add meetings/2024-11-20-general.md
git commit -m "Assign action items for strike preparation"
```

#### After the Meeting

```bash
# Final review and cleanup
git add meetings/2024-11-20-general.md
git commit -m "Finalize meeting notes with attendance and follow-ups"

# Push for collective review
git push origin meeting-2024-11-20-general

# Create pull request for transparency
# Use GitHub/GitLab interface or CLI
```

### Advanced Secretary Patterns

#### Meeting Series Tracking

```bash
# Find all general meetings this year
git log --grep="general-meeting" --since="2024-01-01" --oneline

# Track decision history
git log --grep="DECIDED" --format="%ad - %s" --date=short

# Find when something was discussed
git log -S "rent control" -- meetings/
```

#### Templates and Efficiency

```bash
# Create secretary toolkit branch
git checkout -b secretary-toolkit

# Add useful aliases
git config alias.meeting-notes "!f() { cp templates/meeting-template.md meetings/$(date +%Y-%m-%d)-$1.md && git add meetings/*.md; }; f"

# Use: git meeting-notes general
```

### Common Secretary Challenges

**"I forgot to commit during the meeting"**
- Commit major decisions immediately
- Use git add -p to stage specific sections
- Multiple small commits > one huge commit

**"Meeting was chaotic, notes are messy"**
- Commit the raw notes first
- Create a cleanup branch
- Edit for clarity, then merge

**"Sensitive information was discussed"**
- See [Security practices](../security/help-committed-sensitive-data.md)
- Use .gitignore for off-record discussions
- Consider L1/L2 repository tiers

## Facilitator: Managing Democratic Process

### Your Revolutionary Responsibility

As facilitator, you guide collective decision-making. Git helps you manage proposals, track discussions, and ensure democratic participation.

### Visual: Facilitator's Proposal Flow

```
┌─────────────────────────────────────────────────────────┐
│                 PROPOSAL LIFECYCLE                       │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  1. SUBMISSION     2. REVIEW        3. DISCUSSION       │
│  ┌──────────┐     ┌──────────┐     ┌──────────┐        │
│  │ Member   │     │ Working  │     │ General  │        │
│  │ creates  │ --> │ Group    │ --> │ Meeting  │        │
│  │ branch   │     │ reviews  │     │ debates  │        │
│  └──────────┘     └──────────┘     └──────────┘        │
│       |                 |                 |              │
│       v                 v                 v              │
│  proposal/idea    Add comments      Amendments          │
│                   Tag concerns      Vote recorded       │
│                                                          │
│  4. DECISION       5. MERGE         6. IMPLEMENT        │
│  ┌──────────┐     ┌──────────┐     ┌──────────┐        │
│  │ Vote     │     │ Approved │     │ Action   │        │
│  │ recorded │ --> │ proposals│ --> │ items    │        │
│  │ in Git   │     │ merged   │     │ tracked  │        │
│  └──────────┘     └──────────┘     └──────────┘        │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### Progressive Complexity for Facilitators

#### Level 1: Basic Proposal Tracking (First Month)

Start with simple proposal management:

```bash
# View proposals
git branch -a | grep proposal/

# Read a proposal
git checkout proposal/community-garden
cat proposals/community-garden.md

# Return to main
git checkout main
```

#### Level 2: Facilitate Amendments (Months 2-3)

Guide democratic improvements:

```bash
# During meeting discussion
git checkout proposal/community-garden

# Add amendment suggested by member
echo "## Amendment: Include tool library" >> proposals/community-garden.md
git add proposals/community-garden.md
git commit -m "Add tool library amendment from Rosa"

# Show changes to meeting
git diff main...proposal/community-garden
```

#### Level 3: Manage Multiple Proposals (Months 4-6)

Handle complex democratic processes:

```bash
# Prepare proposals for meeting
git checkout -b facilitation/meeting-prep

# Merge all proposals for review (without committing)
git merge --no-commit proposal/garden proposal/kitchen proposal/childcare
git reset  # Unstage but keep changes for review

# Create summary for agenda
ls proposals/*.md | while read prop; do
  echo "=== $prop ===" >> agenda.md
  head -20 $prop >> agenda.md
done
```

#### Level 4: Advanced Facilitation Patterns (6+ Months)

Master democratic Git workflows:

```bash
# Handle competing proposals
git checkout -b reconciliation/space-use

# Cherry-pick best parts from each
git cherry-pick proposal/garden~3  # Good research section
git cherry-pick proposal/playground~2  # Community input

# Create synthesis
cat > proposals/synthesis-community-space.md << EOF
# Synthesis: Combined Community Space
Integrating garden education with children's play area
[merged best elements from both proposals]
EOF

# Facilitate ranked choice voting
git tag -a vote-1st-choice-garden -m "8 members first choice"
git tag -a vote-1st-choice-playground -m "6 members first choice"
git tag -a vote-2nd-choice-synthesis -m "12 members second choice"
```

### Proposal Management Workflow

#### Before the Meeting

```bash
# Review all open proposals
git branch -r | grep proposal/
git checkout -b review-proposals

# Summarize for agenda
for branch in $(git branch -r | grep proposal/); do
  echo "=== $branch ==="
  git log origin/main..$branch --oneline
done > meeting-prep/open-proposals.md
```

#### Managing Proposal Branches

```bash
# Someone submits a proposal
git checkout -b proposal/community-garden

# Help them structure it
cp templates/proposal-template.md proposals/community-garden.md
# Edit with proposer

git add proposals/community-garden.md
git commit -m "Draft community garden proposal from Working Group 2"
git push origin proposal/community-garden
```

#### Facilitating Amendments

During discussion, amendments arise:

```bash
# Switch to proposal branch
git checkout proposal/community-garden

# Document amendment
echo "## Amendment 1: Include composting program" >> proposals/community-garden.md
echo "Proposed by: Lisa" >> proposals/community-garden.md
echo "Rationale: Reduces waste, builds soil" >> proposals/community-garden.md

git add proposals/community-garden.md
git commit -m "Add Lisa's composting amendment to garden proposal"
```

#### Recording Votes

```bash
# After the vote
git checkout proposal/community-garden

# Document the decision
cat >> proposals/community-garden.md << EOF

## VOTE RESULT
DECIDED[general-meeting](12-4-3): Approved with amendments
- Majority: Strong community building opportunity
- Minority: Concerns about maintenance capacity
- Abstentions: Need more information about costs

Implementation begins: 2024-12-01
EOF

git add proposals/community-garden.md
git commit -m "DECIDED: Community garden approved 12-4-3 with composting amendment"

# Merge to main
git checkout main
git merge proposal/community-garden
git push origin main
```

### Conflict Resolution Patterns

When proposals conflict:

```bash
# Two proposals for same resource
git checkout -b reconcile-conflicts

# Create comparison document
echo "# Conflicting Proposals Analysis" > reconciliation/space-usage.md
echo "## Proposal 1: Community Garden" >> reconciliation/space-usage.md
git show proposal/community-garden:proposals/community-garden.md >> reconciliation/space-usage.md
echo "## Proposal 2: Children's Playground" >> reconciliation/space-usage.md
git show proposal/playground:proposals/playground.md >> reconciliation/space-usage.md

# Facilitate synthesis
echo "## Synthesis Option" >> reconciliation/space-usage.md
echo "Combined space with garden education area for children" >> reconciliation/space-usage.md
```

### Facilitator Best Practices

1. **Pre-meeting Preparation**
   ```bash
   git fetch --all
   git log --since="last week" --oneline
   git diff main...proposal/active-proposal
   ```

2. **Meeting Branch Management**
   ```bash
   # Archive old proposals
   git tag archive/2024-11-approved proposal/community-garden
   git push origin --tags
   git branch -d proposal/community-garden
   ```

3. **Democratic Transparency**
   ```bash
   # Show all positions on an issue
   git log --grep="garden" --format="%an: %s" | sort | uniq
   ```

## Coordinator: Orchestrating Collective Action

### Your Revolutionary Responsibility

As coordinator, you synchronize parallel work streams, ensure tasks complete, and maintain momentum across campaigns.

### Visual: Coordinator's Task Flow

```
┌────────────────────────────────────────────────────────────┐
│                  COORDINATION WORKFLOW                      │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  PLANNING          DISTRIBUTION        TRACKING             │
│  ┌─────────┐      ┌─────────────┐    ┌──────────┐         │
│  │ Campaign │      │   Branch    │    │ Progress │         │
│  │ Strategy │ ---> │ per Working │--> │ Tracking │         │
│  │ in Git   │      │   Group     │    │ & Logs   │         │
│  └─────────┘      └─────────────┘    └──────────┘         │
│       |                  |                  |               │
│       v                  v                  v               │
│  main branch      feature branches    git log/status       │
│                                                             │
│  INTEGRATION       REPORTING          EVALUATION            │
│  ┌─────────┐      ┌────────────┐    ┌───────────┐         │
│  │  Merge   │      │  Generate  │    │  Lessons  │         │
│  │ Results  │ ---> │  Reports   │--> │  Learned  │         │
│  │ to Main  │      │  from Git  │    │ Document  │         │
│  └─────────┘      └────────────┘    └───────────┘         │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

### Progressive Complexity for Coordinators

#### Level 1: Basic Task Tracking (First Month)

Simple task assignment and tracking:

```bash
# Create a task
echo "Fix broken door at community center" > tasks/fix-door.md
git add tasks/fix-door.md
git commit -m "Create task: Fix broken door"

# Check task status
ls tasks/
cat tasks/fix-door.md

# Mark complete
echo "COMPLETED: 2024-11-20 by Jamie" >> tasks/fix-door.md
git add tasks/fix-door.md
git commit -m "DONE: Fixed door task completed"
```

#### Level 2: Campaign Coordination (Months 2-3)

Manage multiple working groups:

```bash
# Set up campaign structure
mkdir -p campaigns/winter-prep/{outreach,supplies,volunteers}

# Create branches for teams
git checkout -b outreach/winter-prep
git checkout -b supplies/winter-prep
git checkout -b volunteers/winter-prep

# Track progress
git log --oneline --graph --all --since="1 week ago"
```

#### Level 3: Advanced Coordination (Months 4-6)

Complex campaign management:

```bash
# Morning coordination routine
git fetch --all
for branch in $(git branch -r | grep "winter-prep"); do
  echo "=== $branch ==="
  git log main..$branch --oneline
done

# Generate status report
cat > reports/weekly-status.md << EOF
# Winter Prep Campaign Status - Week 3

## Completed This Week
$(git log --grep="DONE" --since="1 week ago" --format="- %s")

## In Progress
$(git branch -r | grep -E "task|action" | wc -l) active tasks

## Blockers
$(git log --grep="BLOCKED" --since="1 week ago" --format="- %s")
EOF

git add reports/weekly-status.md
git commit -m "Weekly coordination report: Winter prep week 3"
```

#### Level 4: Strategic Coordination (6+ Months)

Full strategic oversight:

```bash
# Multi-campaign dashboard
git checkout -b coordination/q4-overview

# Aggregate all campaigns
for campaign in winter-prep tenant-rights mutual-aid; do
  echo "# $campaign Status" >> coordination/q4-status.md
  git log --grep=$campaign --since="3 months ago" --format="- %s" >> coordination/q4-status.md
done

# Resource allocation tracking
git log --format="%an" --since="1 month ago" | sort | uniq -c | sort -rn > coordination/contributor-stats.txt

# Identify bottlenecks
for branch in $(git branch -r); do
  last_update=$(git log -1 --format="%ar" $branch)
  if [$last_update == *"week"*]($last_update == *"week"*.md); then
    echo "STALLED: $branch - $last_update"
  fi
done
```

### Campaign Coordination Workflow

#### Setting Up Campaign Structure

```bash
# Initialize campaign
git checkout -b campaign/winter-heating

# Create campaign structure
mkdir -p campaigns/winter-heating/{plans,outreach,research,actions}

cat > campaigns/winter-heating/README.md << EOF
# Winter Heating Campaign

## Objective
Ensure all tenants have adequate heating by December 1

## Working Groups
- Research: Document violations
- Outreach: Build tenant participation  
- Direct Action: Pressure tactics

## Timeline
- Week 1-2: Research and documentation
- Week 3-4: Outreach and education
- Week 5-6: Escalation if needed
EOF

git add campaigns/winter-heating/
git commit -m "Initialize winter heating campaign structure"
```

#### Coordinating Parallel Work

```bash
# Create branches for each working group
git branch research/heating-violations campaign/winter-heating
git branch outreach/tenant-education campaign/winter-heating
git branch action/pressure-tactics campaign/winter-heating

# Assign to teams
git push origin research/heating-violations
git push origin outreach/tenant-education
git push origin action/pressure-tactics
```

#### Daily Coordination Check-ins

```bash
# Morning sync script
#!/bin/bash
echo "=== Campaign Status Check ==="
for branch in $(git branch -r | grep winter-heating); do
  echo "\n## $branch"
  git log main..$branch --oneline --since="yesterday"
done

# Check task completion
git log --grep="DONE:" --since="yesterday" --format="%s"
```

#### Merging Parallel Work

```bash
# Research team reports violations
git checkout campaign/winter-heating
git merge research/heating-violations

# Outreach achieves critical mass
git merge outreach/tenant-education

# Review combined status
git log --graph --oneline --all --since="last week"
```

### Task Management Patterns

#### Creating Task Branches

```bash
# Urgent task assignment
git checkout -b task/emergency-heat-301

cat > tasks/emergency-heat-301.md << EOF
# URGENT: No heat in Unit 301

**Assigned**: Marcus
**Deadline**: Today 5PM
**Priority**: Critical

## Task
1. Contact tenant to verify situation
2. Document with photos/thermometer
3. Call city inspector
4. Prepare emergency grievance

## Updates
- 2:15 PM: Contacted tenant, confirmed no heat for 3 days
- 3:30 PM: Photos taken, temperature 52°F
EOF

git add tasks/emergency-heat-301.md
git commit -m "URGENT: Assign Marcus to handle no heat in 301"
```

#### Tracking Task Progress

```bash
# Task dashboard view
git log --grep="task/" --format="%s %an %ar" | column -t

# Overdue tasks
git log --grep="Deadline:" --format="%B" | grep -B1 "$(date -d 'yesterday' +%Y-%m-%d)"

# Completion rate
echo "Completed: $(git log --grep="DONE:" --since="this week" | wc -l)"
echo "Assigned: $(git log --grep="Assigned:" --since="this week" | wc -l)"
```

### Integration Patterns

#### Daily Stand-up Automation

```bash
# Create daily coordination report
git checkout -b coordination/daily-$(date +%Y-%m-%d)

# Generate report
cat > coordination/standup-$(date +%Y-%m-%d).md << EOF
# Daily Coordination Report - $(date +%Y-%m-%d)

## Completed Yesterday
$(git log --since="yesterday" --until="today" --grep="DONE:" --format="- %s")

## In Progress Today  
$(git branch -r | grep -E "(task|action)/" | while read branch; do
  echo "- $branch: $(git log -1 --format=%s $branch)"
done)

## Blockers
$(git log --grep="BLOCKED:" --since="last week" --format="- %s")

## Needs Review
$(git branch -r | grep "ready-for-review")
EOF

git add coordination/
git commit -m "Daily coordination report for $(date +%Y-%m-%d)"
```

### Coordinator Best Practices

1. **Maintain Campaign Momentum**
   ```bash
   # Weekly momentum check
   git shortlog -sn --since="last week"
   git log --since="last week" | grep -c "DONE:"
   ```

2. **Prevent Bottlenecks**
   ```bash
   # Find stalled branches
   for branch in $(git branch -r); do
     last_commit=$(git log -1 --format=%ar $branch)
     echo "$branch: $last_commit"
   done | grep -E "(days|weeks) ago"
   ```

3. **Celebrate Victories**
   ```bash
   # Tag campaign milestones
   git tag -a "50-tenants-committed" -m "Reached critical mass for heating campaign"
   git tag -a "heat-restored-building-c" -m "First victory: Building C heat restored"
   ```

## Cross-Role Collaboration

### Secretary ↔ Facilitator

```bash
# Secretary prepares agenda from proposals
git checkout meeting-prep
git merge --no-commit $(git branch -r | grep proposal/ | tr '\n' ' ')
git reset # Don't actually merge, just view

# Facilitator reviews meeting outcomes
git log --author="Secretary" --grep="DECIDED" --since="last meeting"
```

### Facilitator ↔ Coordinator

```bash
# Facilitator assigns approved proposals
git checkout coordination/assignments
git merge proposal/approved-action

# Coordinator reports back on implementation
git checkout proposal/approved-action
echo "## Implementation Report" >> proposals/original-proposal.md
echo "Status: 75% complete, on track for deadline" >> proposals/original-proposal.md
```

### Secretary ↔ Coordinator

```bash
# Secretary documents task outcomes
git log --grep="task/" --format="%s" > meetings/task-report.md

# Coordinator uses meeting decisions for planning
git log --grep="DECIDED.*action" --format="%s" | \
  while read decision; do
    echo "git checkout -b task/$decision"
  done
```

## Advanced Patterns for All Roles

### Building Institutional Memory

```bash
# Create knowledge base from patterns
git log --grep="worked:" --format="%B" > knowledge/what-worked.md
git log --grep="failed:" --format="%B" > knowledge/lessons-learned.md

# Tag important patterns
git tag -a "pattern/successful-rent-strike" \
  -m "This commit series shows effective rent strike organization"
```

### Automation for Efficiency

```bash
# ~/.gitconfig aliases for common role tasks
[alias]
  # Secretary shortcuts
  meeting = "!f() { cp templates/meeting.md meetings/$(date +%Y-%m-%d)-$1.md; }; f"
  decided = "commit -m \"DECIDED[$1]($2): $3\""
  
  # Facilitator shortcuts  
  proposals = "branch -r | grep proposal/"
  conflicts = "diff --name-only --diff-filter=U"
  
  # Coordinator shortcuts
  tasks = "log --grep='task/' --oneline"
  blockers = "log --grep='BLOCKED:' --oneline"
  progress = "shortlog -sn --since='last week'"
```

## Tech Support: Maintaining Revolutionary Infrastructure

### Your Revolutionary Responsibility

As tech support, you keep the infrastructure running, help comrades overcome technical barriers, and ensure no one gets left behind.

### Progressive Complexity for Tech Support

#### Level 1: Basic Help Desk (First Month)

Help others with common issues:

```bash
# Common fixes you'll use daily
git status  # Diagnose current state
git diff    # Show what changed
git log --oneline -10  # Recent history

# Help someone who's stuck
git reset --hard HEAD  # Nuclear option - discard all changes
git clean -fd         # Remove untracked files
```

#### Level 2: Troubleshooting (Months 2-3)

Solve common Git problems:

```bash
# Fix merge conflicts
git status  # See conflicted files
nano conflicted-file.md  # Edit to resolve
git add conflicted-file.md
git commit -m "Resolved merge conflict in meeting notes"

# Recover lost work
git reflog  # Show all recent actions
git checkout HEAD@{2}  # Go back 2 actions
```

#### Level 3: Infrastructure Maintenance (Months 4-6)

Keep systems running smoothly:

```bash
# Repository health check
git fsck --full
git gc --aggressive
git count-objects -vH

# Set up automated backups
cat > scripts/backup-repos.sh << 'EOF'
#!/bin/bash
for repo in /home/*/repos/*; do
  cd $repo
  git bundle create /backups/$(basename $repo)-$(date +%Y%m%d).bundle --all
done
EOF

chmod +x scripts/backup-repos.sh
```

#### Level 4: Advanced Recovery (6+ Months)

Handle complex disasters:

```bash
# Recover from force push disaster
git reflog show origin/main
git push --force-with-lease origin origin/main@{1}:main

# Extract file from specific commit
git show COMMIT:path/to/file > recovered-file.md

# Bisect to find when something broke
git bisect start
git bisect bad HEAD
git bisect good v1.0
# Test each commit git suggests
git bisect good/bad
# Eventually finds the breaking commit
```

### Common Support Requests

#### "I accidentally committed passwords!"
```bash
# If not pushed yet
git reset --soft HEAD~1
# Edit file to remove password
git add .
git commit -m "Previous commit without passwords"

# If already pushed, see security guide
```

#### "Git says I have conflicts"
```bash
# Show them the conflict
cat conflicted-file.md | grep -A5 -B5 "<<<<<<"

# Walk through resolution
nano conflicted-file.md
# Remove <<<, ===, >>> markers
# Keep the version they want

git add conflicted-file.md
git commit
```

#### "I can't push my changes"
```bash
# Usually means they need to pull first
git pull --rebase origin main
# Fix any conflicts
git push
```

### Tech Support Best Practices

1. **Document Everything**
   ```bash
   # Create knowledge base from support requests
   echo "## Issue: $1" >> support/kb/$(date +%Y%m%d)-$1.md
   echo "## Solution:" >> support/kb/$(date +%Y%m%d)-$1.md
   # Document what fixed it
   ```

2. **Automate Common Tasks**
   ```bash
   # Create helper scripts
   cat > bin/git-meeting << 'EOF'
   #!/bin/bash
   cp templates/meeting.md meetings/$(date +%Y%m%d)-meeting.md
   git add meetings/
   echo "Created meeting notes for $(date)"
   EOF
   chmod +x bin/git-meeting
   ```

3. **Teach While Fixing**
   - Don't just fix - explain
   - Create cheat sheets
   - Run mini-workshops

## Quick Command Reference by Role

### Universal Commands (Everyone Needs)
```bash
git clone [url]          # Get repository
git pull                 # Get updates
git add [file]           # Stage changes
git commit -m "message"  # Save changes
git push                 # Share changes
git status              # Check state
git log --oneline       # View history
```

### Secretary Commands
```bash
git add -p              # Stage specific parts
git commit --amend      # Fix last commit
git log --grep="DECIDED" # Find decisions
git blame [file]        # Who wrote what
```

### Facilitator Commands
```bash
git branch              # List branches
git checkout -b [name]  # Create branch
git merge [branch]      # Combine work
git tag -a [name]       # Mark milestones
git cherry-pick [commit] # Take specific changes
```

### Coordinator Commands
```bash
git fetch --all         # Update all remotes
git log --graph --all   # Visualize work
git shortlog -sn        # Contribution stats
git branch -r           # Remote branches
git log --since="1 week" # Recent activity
```

### Tech Support Commands
```bash
git reflog              # Recovery history
git fsck                # Check integrity
git gc                  # Clean up
git reset --hard        # Nuclear option
git clean -fd           # Remove untracked
```

## Troubleshooting Flowchart

```
Problem?
├─ "I don't know what to do"
│  └─ git status → Read the suggestions
├─ "I messed up my last commit"
│  └─ git commit --amend (if not pushed)
├─ "I need to undo changes"
│  ├─ Not committed → git checkout -- [file]
│  ├─ Committed → git reset --soft HEAD~1
│  └─ Pushed → git revert [commit]
├─ "Git says conflict"
│  └─ Edit file → Remove markers → git add → commit
└─ "I'm totally lost"
   └─ git status → Ask for help → Learn together
```

## Remember Your Power

Each role builds revolutionary capacity:

- **New Member**: You bring fresh perspectives
- **Secretary**: You prevent knowledge hemorrhaging
- **Facilitator**: You ensure democratic participation
- **Coordinator**: You transform decisions into reality
- **Tech Support**: You eliminate technical barriers

Git isn't neutral technology - in your hands, it becomes infrastructure for liberation.

## Role Transition Paths

```
New Member (Learn basics)
    ├→ Secretary (Document everything)
    ├→ Facilitator (Guide democracy)
    ├→ Coordinator (Drive action)
    └→ Tech Support (Help everyone)
        └→ Teach others → Build capacity
```

Start where you are. Grow at your pace. Every commit builds the revolution.

---

*Need the basics first? → [Git in 7 Commands](../../learn/git-basics/git-in-7-commands.md)*  
*Ready for security? → [Security Workflows](../security/security-audits-for-organizers.md)*  
*Want to teach others? → [Running a Git Workshop](../../teach/workshops/git-through-campaign-template.md)*