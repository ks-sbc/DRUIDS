---
title: "Revolutionary Commit Conventions"
description: "Git commit format that encodes democratic decision-making and enables organizational automation"
created: 2025-07-04
updated: 2025-07-04
type: "docs/reference"
security: "L0"
version: "1.0.0"
document_id: "REF-GIT-2025-001-L0"
tags: ["git", "commits", "conventions", "democracy", "automation"]
draft: true
author: ["Comrade 47"]
---

# Revolutionary Commit Conventions

## Overview

Transform Git commits from individual changes to collective decisions. Revolutionary Commit Conventions encode democratic decision-making directly into version control. Every commit records:

- **WHO** made the decision (which democratic body)
- **HOW** it was decided (vote counts/consensus)
- **WHAT** was decided (in organizing language)
- **WHY** it matters (political context)

## Basic Format

```git
TYPE[decision-body](vote-result): Action description
```

### Examples

```bash
DECIDED[general-meeting](15-2-1): Implement 3-tier security model
ORGANIZED[tenant-union](consensus): Launch rent strike campaign
EDUCATED[study-group](12-present): Document Capital Vol.1 Ch.3 key concepts
EMERGENCY[security-comm](immediate): Rotate compromised credentials
```

## Commit Types

| Type | Purpose | Example |
|------|---------|---------|
| `DECIDED` | Formal organizational decisions | `DECIDED[committee](unanimous): Adopt new bylaws` |
| `ORGANIZED` | Campaign/action planning | `ORGANIZED[working-group](8-1-0): Plan march route` |
| `EDUCATED` | Political education materials | `EDUCATED[study-group](15-present): Create Lenin reading guide` |
| `DOCUMENTED` | Meeting minutes/records | `DOCUMENTED[secretary](routine): Record June meeting` |
| `SECURED` | Security-related changes | `SECURED[security-team](emergency): Update access controls` |
| `EMERGENCY` | Urgent response actions | `EMERGENCY[coords](quorum): Remove compromised data` |
| `REFLECTED` | Self-criticism/evaluation | `REFLECTED[plenary](collective): Assess campaign effectiveness` |

## Decision Bodies

| Body | Description | Authority |
|------|-------------|-----------|
| `[general-meeting]` | Full membership assembly | Highest authority |
| `[committee-name]` | Standing committees | Delegated authority |
| `[working-group]` | Temporary formations | Task-specific |
| `[security-team]` | Security committee | Emergency powers |
| `[coords]` | Coordination committee | Daily operations |
| `[plenary]` | Evaluation sessions | Assessment only |

## Vote Results

| Format | Meaning | Example |
|--------|---------|---------|
| `(unanimous)` | No opposition | Full agreement |
| `(consensus)` | No blocks, possible concerns | General agreement |
| `(15-2-1)` | For-Against-Abstain count | Democratic vote |
| `(12-present)` | Attendance for education | No vote needed |
| `(quorum)` | Minimum attendance met | Emergency decision |
| `(postponed)` | Tabled for future | Needs more discussion |
| `(amended)` | Modified during meeting | See details in commit |

## Extended Format

For complex decisions, use multi-line format:

```bash
git commit -m "DECIDED[general-meeting](18-3-0): Adopt 3-month campaign timeline

Meeting: 2024-07-03 General Assembly
Proposer: Housing Committee  
Discussion: 45 minutes
Key Points:
- Timeline balances urgency with capacity
- Includes 2-week education phase
- Built-in evaluation checkpoints

Implementation assigns:
- Week 1-2: Education (Ed Committee)
- Week 3-8: Escalation (Direct Action)  
- Week 9-12: Negotiation (Liaison)

References: proposal-2024-15.md
Security: L0"
```

## Git Configuration

### Commit Template

Create `.gitmessage` in your repository:

```git
# TYPE[body](result): Subject (50 chars max)
#
# Meeting: Date and type
# Proposer: Who brought forward
# Discussion: Duration and key points
# Decision: Specific outcome
# Assigns: Who does what
# Timeline: When complete
# References: Related documents
# Security: L0/L1/L2
```

Configure Git to use template:

```bash
git config commit.template .gitmessage
```

### Validation Hook

Create `.git/hooks/commit-msg`:

```bash
#!/bin/bash
# Validate revolutionary commit format

commit_regex='^(DECIDED|ORGANIZED|EDUCATED|DOCUMENTED|SECURED|EMERGENCY|REFLECTED)\[[a-z-]+\]\([a-z0-9-]+\): .{1,50}'

if ! grep -qE "$commit_regex" "$1"; then
    echo "ERROR: Commit message must follow revolutionary format:"
    echo "TYPE[decision-body](vote-result): Description"
    echo ""
    echo "Example:"
    echo "DECIDED[general-meeting](unanimous): Implement new security protocols"
    exit 1
fi
```

## Automation Integration

### Parse Commits for Automation

```python
import re
from typing import Dict, Optional

class RevolutionaryCommit:
    def __init__(self, message: str):
        self.pattern = r'^(\w+)\[([^\]]+)\]\(([^)]+)\): (.+)'
        self.parse(message)
    
    def parse(self, message: str) -> None:
        match = re.match(self.pattern, message)
        if match:
            self.type = match.group(1)
            self.body = match.group(2)
            self.result = match.group(3)
            self.action = match.group(4)
        else:
            raise ValueError("Invalid revolutionary commit format")
    
    def needs_implementation(self) -> bool:
        return self.type == "DECIDED"
    
    def is_urgent(self) -> bool:
        return self.type == "EMERGENCY"
    
    def was_unanimous(self) -> bool:
        return self.result == "unanimous"
```

### Automation Rules

```yaml
# .druids/automation.yml
commit_triggers:
  - pattern: "DECIDED.*general-meeting.*"
    actions:
      - notify: all_members
      - create_task: implementation_tracking
      - deadline: 72_hours
      
  - pattern: "EMERGENCY.*"
    actions:
      - notify: security_team
      - notify: coordination_committee
      - escalate: immediate
      
  - pattern: "EDUCATED.*"
    actions:
      - update: education_tracker
      - schedule: follow_up_discussion
      
  - pattern: ".*unanimous.*"
    actions:
      - priority: high
      - flag: full_consensus
```

## Security Integration

### Linking to Security Tiers

```bash
# Public decision (L0)
DECIDED[general-meeting](public): Update public organizing guide

# Internal decision (L1) 
DECIDED[members](15-2-0): Approve new member applications

# Sensitive decision (L2) - minimal public detail
SECURED[security-team](approved): Implement protocols per L2-2024-07-03
```

### Audit Trail

Revolutionary commits create an immutable audit trail:

```bash
# Show all democratic decisions
git log --grep="DECIDED"

# Show emergency actions
git log --grep="EMERGENCY" --since="1 month ago"

# Show education work
git log --grep="EDUCATED" --format="%ai %s" | sort
```

## Benefits

1. **Democratic Transparency**: Every decision is recorded with vote counts
2. **Automated Accountability**: Parse commits to track implementation  
3. **Organizational Memory**: New members can understand history
4. **Political Education**: Commit messages teach democratic process
5. **Integration Ready**: Enables powerful automation workflows

## Examples in Practice

### Campaign Launch

```git
ORGANIZED[tenant-union](consensus): Launch "Fair Rent Now" campaign
DECIDED[general-meeting](22-3-2): Approve $500 campaign budget  
EDUCATED[outreach](30-present): Train canvassers on tenant rights
DOCUMENTED[secretary](routine): Record campaign kickoff meeting
```

### Security Response  

```git
EMERGENCY[security](immediate): Disable compromised account
SECURED[security-team](unanimous): Implement 2FA requirement
REFLECTED[coords](emergency): Assess security breach impact
DECIDED[general-meeting](18-0-1): Adopt new security protocols
```

### Regular Operations

```git
DOCUMENTED[facilitator](routine): Record weekly check-in notes
EDUCATED[study-group](8-present): Discuss Chapter 4 of State and Revolution  
ORGANIZED[food-comm](5-0-0): Plan next community meal
DECIDED[coords](consensus): Approve space rental for event
```

## Getting Started

1. **Add commit template** to your repository
2. **Configure Git** to use the template
3. **Install validation hook** to ensure compliance
4. **Train members** on the format
5. **Set up automation** based on your needs

Remember: This isn't bureaucracy - it's encoding democracy into daily practice.

---

*Every commit is a collective decision. Every push advances the revolution.*
