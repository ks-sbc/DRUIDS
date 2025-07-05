---
title: "Proposal Process Workflow"
description: "Step-by-step guide for democratic proposals in DRUIDS using democratic centralist framework"
type: "how-to"
security: "L0"
document_id: "INT-HTG-2025-190-L0"
version: "1.0.0"
tags: ["workflow", "democracy", "decision-making", "proposals"]
---

# Proposal Process Workflow

This guide walks through the complete process of creating, discussing, and implementing proposals using DRUIDS democratic centralist framework.

## Overview

The proposal process embodies democratic centralism by ensuring thorough discussion before unified implementation. Every member can propose ideas, and all members participate in democratic decision-making.

## Process Stages

### Stage 1: Proposal Creation

#### Step 1: Create Proposal Document

Use the proposal template:

```markdown
      ---
      title: "Proposal: [Descriptive Title]"
      date: 2024-01-15
      type: proposal
      status: draft
      author: [Your Name]
      security: L0
      tags:
      - proposal
      - [relevant-topic]
      ---

      # Proposal: [Title]

      ## Summary
      [One paragraph summary of the proposal]

      ## Background
      [Why is this proposal needed? What problem does it solve?]

      ## Proposal Details
      [Detailed description of what you're proposing]

      ## Implementation Plan
      1. [Step 1]
      2. [Step 2]
      3. [Step 3]

      ## Resources Required
      - Human: [Who needs to be involved]
      - Time: [Estimated timeline]
      - Material: [Any material resources needed]

      ## Success Metrics
      - [How will we measure success?]
      - [What are the concrete outcomes?]

      ## Risks and Mitigation
      - Risk: [Potential problem]
      Mitigation: [How to address it]
```

#### Step 2: Develop Your Proposal

1. **Research thoroughly**
   - Check for similar past proposals
   - Gather supporting data
   - Consult affected members

2. **Be specific**
   - Concrete actions, not vague ideas
   - Clear timeline and responsibilities
   - Measurable outcomes

3. **Consider implications**
   - Security impacts
   - Resource requirements
   - Organizational capacity

#### Step 3: Internal Review

Before submission:

- Review with trusted comrades
- Check alignment with principles
- Ensure completeness
- Verify security classification

### Stage 2: Submission

#### Git Workflow (Recommended)

1. **Create proposal branch**

```bash
git checkout -b proposal/your-proposal-name
```

2. **Add your proposal**

```bash
git add proposals/2024-01-your-proposal.md
git commit -m "proposal: Add [proposal name]"
git push origin proposal/your-proposal-name
```

3. **Open Pull Request**

- Title: "Proposal: [Your Proposal Title]"
- Description: Include summary and discussion points
- Label: "proposal", "needs-discussion"

#### Non-Git Workflow

1. Save proposal in `proposals/` folder
2. Share with designated coordinator
3. Request addition to meeting agenda

### Stage 3: Discussion Phase

#### Pre-Meeting Discussion

1. **Announcement**
   - Proposal shared with appropriate security level
   - Minimum 3 days for review
   - Comments collected via:
     - PR comments (Git)
     - Discussion forum
     - Designated channel

2. **Clarification**
   - Author responds to questions
   - Updates proposal if needed
   - Documents concerns raised

#### Meeting Discussion

1. **Presentation** (5-10 minutes)
   - Author presents key points
   - Focus on problem and solution
   - Highlight resource needs

2. **Q&A** (10-15 minutes)
   - Clarifying questions first
   - Then substantive discussion
   - Document all points raised

3. **Debate** (time varies)
   - Arguments for and against
   - Alternative proposals
   - Synthesis attempts

4. **Refinement**
   - Amendments proposed
   - Consensus building
   - Final proposal shape

### Stage 4: Decision

#### Voting Process

1. **Call for Vote**
   - Clear statement of proposal
   - Any final amendments included
   - Voting method announced

2. **Vote Recording**

```markdown
 ## Decision Record
 Date: 2024-01-15
 Proposal: [Title]
 Result: Approved/Rejected
 Vote Count: Y-N-A (Yes-No-Abstain)
```

3. **Documentation**
   - Update proposal status
   - Record in meeting minutes
   - Create decision document

#### Decision Types

- **Consensus**: All agree (preferred)
- **Majority**: Over 50% approve
- **Supermajority**: 2/3 approve (for major changes)
- **Postponed**: Needs more development

### Stage 5: Implementation

#### If Approved

1. **Create Implementation Plan**

```markdown
 ---
 title: "Implementation: [Proposal Title]"
 type: implementation
 status: active
 proposal_ref: <!-- [[../../_templates/proposal-template|Original Proposal]] -->
 owner: [Responsible Person]
 deadline: 2024-02-15
 ---

 # Implementation Plan

 ## Decision Summary
 [What was decided]

 ## Action Items
 - [ ] Task 1 - Owner - Due Date
 - [ ] Task 2 - Owner - Due Date
 - [ ] Task 3 - Owner - Due Date

 ## Progress Updates
 ### 2024-01-16
 - Started work on Task 1
 - Assigned team members
```

2. **Assign Responsibilities**
   - Clear task ownership
   - Concrete deadlines
   - Reporting structure

3. **Track Progress**
   - Regular updates
   - Dashboard monitoring
   - Blocker identification

#### If Rejected

1. **Document Reasons**
   - Why rejected
   - What would need to change
   - Lessons learned

2. **Archive Proposal**
   - Move to `archive/proposals/rejected/`
   - Maintain for future reference
   - Link from decision record

### Stage 6: Evaluation

#### Progress Review

Weekly/Monthly:

- Check implementation status
- Address blockers
- Adjust timeline if needed
- Report to organization

#### Completion

1. **Final Report**
   - Outcomes achieved
   - Metrics comparison
   - Lessons learned
   - Recommendations

2. **Archive**
   - Move to `archive/proposals/completed/`
   - Update all references
   - Extract best practices

## Security Considerations

### Classification Guidelines

- **L0 (Public)**: General organizational improvements
- **L1 (Candidate)**: Internal process changes
- **L2 (Cadre)**: Strategic or sensitive proposals

### Access Control

- Only appropriate security levels in discussion
- Sanitized versions for lower levels if needed
- Compartmentalization of sensitive details

## Best Practices

### For Proposal Authors

1. **Start early**: Don't rush proposals
2. **Seek input**: Talk to affected members first
3. **Be flexible**: Expect modifications
4. **Stay engaged**: Participate throughout process

### For Reviewers

1. **Read thoroughly**: Understand before commenting
2. **Be constructive**: Suggest improvements
3. **Consider broadly**: Think of all implications
4. **Respect process**: Follow democratic procedures

### For Implementation

1. **Act promptly**: Start implementation quickly
2. **Communicate regularly**: Keep organization informed
3. **Document everything**: Maintain clear records
4. **Evaluate honestly**: Report real outcomes

## Common Issues and Solutions

### "Proposal ignored"

- Ensure proper submission process followed
- Check if reached right audience
- Consider timing and priorities
- Resubmit with improvements

### "Discussion dominated by few"

- Facilitator ensures equal participation
- Use written comments option
- Break into smaller groups
- Set speaking time limits

### "Implementation stalls"

- Review resource allocation
- Check if plan was realistic
- Identify and address blockers
- Consider modifications

## Tools and Templates

### Dataview Queries

**Active Proposals:**

```sql
TABLE status, author, date
FROM "proposals"
WHERE type = "proposal" AND status = "active"
SORT date DESC
```

**Implementation Tracking:**

```sql
TASK
FROM "implementation"
WHERE !completed
GROUP BY file.name
```

### Git Commands

```bash
# Create proposal branch
git checkout -b proposal/descriptive-name

# Update proposal
git add proposals/your-proposal.md
git commit -m "proposal: Update based on feedback"

# After approval, merge
git checkout main
git merge proposal/descriptive-name
```

## Next Steps

1. Review existing proposals for examples
2. Draft your first proposal
3. Seek feedback before submission
4. Participate in others' proposals
5. Learn from the process

Remember: The proposal process is how we make collective decisions democratically. Every proposal, whether approved or not, helps develop our collective understanding and unity.
