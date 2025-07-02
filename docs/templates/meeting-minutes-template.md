---
title: "Meeting Minutes Template"
description: "Standard format for documenting organizational meetings in Git"
created: 2025-07-02
updated: 2025-07-02
type: "docs/reference"
security: "L0"
version: "1.0.0"
document_id: "TMP-REF-2025-001-L0"
tags: ["template", "meetings", "documentation", "reference"]
draft: false
author: ["Comrade 47"]
---

# Meeting Minutes Template

*Copy this template for each meeting. Replace placeholder text with actual content.*

```markdown
# [Meeting Type] Meeting
Date: [YYYY-MM-DD]
Time: [Start] - [End]
Location: [Physical location or "Virtual"]
Facilitator: [Comrade name]
Note-taker: [Comrade name]
Attendees: [List all present]
Absent: [Note excused absences]

## Agenda
1. [First agenda item]
2. [Second agenda item]
3. [Continue as needed]

## Opening
- [Land acknowledgment if applicable]
- [Review of community agreements]
- [Security check/reminder]

## Discussion

### [Agenda Item 1]
**Presenter**: [Name]
**Time allotted**: [X minutes]

**Key Points**:
- [Main point discussed]
- [Supporting information]
- [Concerns raised]

**Decisions**:
- [Any decisions made]
- [Vote count if applicable: (Y-N-A)]

### [Agenda Item 2]
[Repeat format for each agenda item]

## Proposals Presented

### Proposal: [Title]
**Submitted by**: [Comrade name]
**Type**: [Tactical/Operational/Strategic]

**Summary**:
[Brief description]

**Resource Requirements**:
- Time: [Estimated hours]
- Money: [Budget needed]
- People: [Number of comrades]

**Decision**: [Approved/Tabled/Rejected]
**Vote**: [Y-N-A if formal vote]
**Implementation Timeline**: [If approved]

## Action Items
| Task | Assigned To | Deadline | Priority |
|------|------------|----------|----------|
| [Specific task] | [Comrade] | [Date] | [High/Med/Low] |
| [Continue for all tasks] | | | |

## Announcements
- [General announcements]
- [Upcoming events]
- [Important dates]

## Next Meeting
- **Date**: [YYYY-MM-DD]
- **Time**: [Start time]
- **Facilitator**: [Next facilitator]
- **Agenda items to carry forward**: [List]

## Security Notes
- [Any security concerns]
- [Reminders about operational security]
- [DO NOT include sensitive information in L0 docs]

## Closing
- [Evaluation of meeting process]
- [Appreciations]
- Meeting adjourned at [time]

---
*Committed to Git by [note-taker pseudonym] on [date]*
```

## Template Usage Guidelines

### File Naming Convention
```
meetings/YYYY-MM-DD-meeting-type.md
```

Examples:
- `meetings/2025-07-02-weekly-general.md`
- `meetings/2025-07-02-security-committee.md`
- `meetings/2025-07-02-campaign-planning.md`

### Security Classifications

**L0 (Public)**: General meetings, public campaigns
- No real names without consent
- No home addresses
- No tactical details of actions

**L1 (Members)**: Internal organizing
- Pseudonyms required
- Can include internal strategy
- Store in encrypted repositories

**L2 (Cadre)**: Sensitive planning
- Maximum security protocols
- Limited access
- Never in main branch

### Commit Message Format
```
Add [date] [meeting type] minutes

- [Key decision 1]
- [Key decision 2]
- Attendance: X comrades
- Next meeting: [date]
```

### Democratic Centralism in Practice

1. **During Meeting**: Free discussion, all views recorded
2. **In Minutes**: Document dissenting opinions
3. **After Decision**: Record unified action plan
4. **In Git**: History preserves the process

### Common Sections to Add

Depending on your organization:
- **Political Education**: Summary of study session
- **Finance Report**: Budget updates (general figures only in L0)
- **Campaign Updates**: Progress on ongoing work
- **Solidarity Statements**: Support for other struggles
- **Self-Criticism**: Reflecting on mistakes

### Integration with Git Workflow

1. Create branch for meeting: `git checkout -b meetings/2025-07-02`
2. Write minutes during/immediately after
3. Commit with descriptive message
4. Push branch for review
5. Merge after verification

### Why This Format Works

- **Searchable**: Git grep finds decisions across history
- **Accountable**: Who decided what, when
- **Actionable**: Clear task assignments
- **Historical**: Builds organizational memory
- **Flexible**: Adapt sections to your needs

Remember: Meeting minutes are political documents. They shape organizational memory and culture.

---

See also:
- [Proposal Template](/templates/proposal-template.md)
- [Your First Revolutionary Commit](/tutorials/your-first-revolutionary-commit.md)