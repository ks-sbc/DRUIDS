---
title: "Proposal Template"
description: "Standard format for organizational proposals using tactical-operational-strategic framework"
created: 2025-07-02
updated: 2025-07-02
type: "docs/reference"
security: "L0"
version: "1.0.0"
document_id: "TMP-REF-2025-002-L0"
tags: ["template", "proposals", "decision-making", "reference", "tukhachevsky"]
draft: false
author: ["Comrade 47"]
---

# Proposal Template

*For all organizational proposals. This template enforces the tactical-operational-strategic thinking that prevents failure.*

```markdown
# Proposal: [Clear, Specific Title]

**Submitted by**: [Pseudonym(s)]
**Date**: [YYYY-MM-DD]
**Proposal ID**: [YEAR-NUMBER]
**Status**: [Draft/Under Discussion/Approved/Rejected]
**Security Level**: [L0/L1/L2]

## Executive Summary
[2-3 sentences maximum. What are we doing and why?]

## Strategic Alignment

### How This Advances Revolution
[Connect to long-term revolutionary goals. Be specific about power building.]

### Theoretical Framework
[What Marxist-Leninist principles guide this? How does it build dual power?]

### Success Definition
[What does victory look like strategically? Not just task completion.]

## Operational Planning

### Campaign Integration
[How does this fit with ongoing campaigns? What operational capacity does it build?]

### Resource Analysis
- **People**: [Number needed, skills required, time commitment]
- **Money**: [Budget breakdown, funding sources]
- **Time**: [Timeline with milestones]
- **Infrastructure**: [What DRUIDS features needed]

### Risk Assessment
- **State Repression**: [Likely responses and mitigation]
- **Internal Risks**: [Burnout, conflict, capacity]
- **Failure Points**: [What could go wrong]

## Tactical Implementation

### Concrete Steps
1. [First specific action]
2. [Second specific action]
3. [Continue with all steps]

### Task Assignments
| Task | Skills Needed | Time Estimate | Deadline |
|------|---------------|---------------|----------|
| [Task] | [Skills] | [Hours] | [Date] |

### Success Metrics
- [ ] [Measurable outcome 1]
- [ ] [Measurable outcome 2]
- [ ] [Continue for all metrics]

## Democratic Centralism Considerations

### Points of Unity Required
[What must we agree on to proceed?]

### Spaces for Tactical Flexibility
[Where can comrades adapt based on conditions?]

### Minority Positions
[Document any dissenting views for historical record]

## Timeline

### Phase 1: [Name] (Weeks 1-X)
- Objective: [What completes this phase]
- Key tasks: [Main activities]
- Decision point: [What determines moving forward]

### Phase 2: [Name] (Weeks X-Y)
[Continue for all phases]

## Budget (if applicable)

| Item | Cost | Justification |
|------|------|---------------|
| [Item] | $[Amount] | [Why needed] |
| **Total** | $[Sum] | |

Funding source: [Where money comes from]

## Evaluation Criteria

### Immediate (1 month)
- [ ] [Short-term success metric]

### Medium (3 months)
- [ ] [Medium-term impact]

### Long-term (6+ months)
- [ ] [Strategic advancement]

## Appendices

### A. Related Proposals
- [Link to connected proposals]

### B. Research/Background
- [Supporting documentation]

### C. Community Input
- [Feedback from affected communities]

---

## Proposal History
- [YYYY-MM-DD]: Draft submitted
- [YYYY-MM-DD]: Discussion at meeting
- [YYYY-MM-DD]: Revisions based on feedback
- [YYYY-MM-DD]: Decision made
```

## How to Use This Template

### The Three Levels MUST Connect

**Strategic** → **Operational** → **Tactical**

Every proposal must show how daily tasks (tactical) build organizational capacity (operational) toward revolutionary goals (strategic).

### Common Failure Patterns to Avoid

1. **Tactical Without Strategy**: "Let's do a food drive" without connecting to power building
2. **Strategic Without Tactics**: "Overthrow capitalism" without concrete steps
3. **Operational Gaps**: Good ideas that don't build lasting capacity

### Proposal Workflow in Git

```bash
# Create proposal branch
git checkout -b proposals/2025-01-rent-strike

# Write proposal using template
cp templates/proposal-template.md proposals/2025-01-rent-strike.md
# Edit with your content

# Commit and push
git add proposals/
git commit -m "Add rent strike proposal

- Strategic: Challenges property relations
- Operational: Builds tenant union infrastructure
- Tactical: 50 buildings, 6-month timeline"

git push origin proposals/2025-01-rent-strike
```

### Decision Making Process

1. **Draft**: Author creates on branch
2. **Discussion**: Comments via merge request
3. **Revision**: Updates based on feedback
4. **Decision**: Vote at meeting (record in minutes)
5. **Merge**: If approved, merge to main

### Security Considerations

**L0 Proposals**: Public campaigns, mutual aid
- Remove specific addresses
- Use regional descriptions
- Focus on public-facing elements

**L1 Proposals**: Internal organizing
- Can include member resources
- Tactical details allowed
- Pseudonyms required

**L2 Proposals**: Sensitive operations
- Maximum compartmentalization
- Limited access branch
- Separate security protocols

### Why This Framework Matters

Most organizing fails at the operational level:
- Good tactics without strategy = burnout
- Good strategy without tactics = armchair revolution
- Both without operations = no lasting power

This template forces operational thinking - the bridge between daily work and revolutionary goals.

### Examples of Each Level

**Tactical**: "Distribute food Saturday 2pm at People's Park"
**Operational**: "Build neighborhood survival program with weekly distributions"
**Strategic**: "Create dual power structure replacing state welfare with community care"

All three must be present in every proposal.

### Adapting the Template

Your organization might add:
- **Cultural Work**: How this builds revolutionary culture
- **Coalition Building**: External organization involvement
- **Political Education**: Learning opportunities created
- **Sustainability**: How this work continues beyond initial push

Keep the three-level analysis. Everything else can adapt to your conditions.

---

See also:
- [[meeting-minutes-template|Meeting Minutes Template]]
- [[security-incident-template|Security Incident Template]]
- [[../learn/core-concepts/tukhachevsky-bridge|Understanding Tukhachevsky]]