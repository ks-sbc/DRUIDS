---
title: "DRUIDS Task Status Guide"
description: "Guide to task status symbols and workflow states used in DRUIDS democratic centralist processes."
type: "reference"
security: "L0"
document_id: "INT-REF-2025-217-L0"
version: "1.0.0"
tags: ["tasks", "workflow", "status-management", "democratic-centralism", "project-management"]
---

# DRUIDS Task Status Guide

## Overview

The Tasks plugin in DRUIDS uses an expanded set of status types to support democratic centralist workflows. This guide explains each status and when to use them.

## Standard Task Statuses

### ` ` Todo

- **Symbol**: Space (empty checkbox)
- **Meaning**: Task not yet started
- **Next Status**: `/` (In Progress)
- **Usage**: Default state for new tasks

### `/` In Progress

- **Symbol**: Forward slash
- **Meaning**: Actively being worked on
- **Next Status**: `x` (Done)
- **Usage**: Mark when you begin work

### `x` Done

- **Symbol**: x
- **Meaning**: Task completed
- **Next Status**: ` ` (Todo)
- **Usage**: Mark when work is finished

### `-` Cancelled

- **Symbol**: Hyphen
- **Meaning**: Task no longer needed
- **Next Status**: ` ` (Todo)
- **Usage**: For obsolete or rejected tasks

## Democratic Workflow Statuses

### `⏸️` Blocked

- **Symbol**: Pause emoji
- **Meaning**: Cannot proceed due to dependency
- **Next Status**: `/` (In Progress)
- **Usage**:
  - Waiting for another task to complete
  - Needs approval or resources
  - External dependencies

**Example**:

```markdown
- [⏸️] Implement new feature (blocked by #123)
```

### `🔄` Under Review

- **Symbol**: Cycle arrows emoji
- **Meaning**: Submitted for democratic review
- **Next Status**: `x` (Done)
- **Usage**:
  - Proposal under discussion
  - Code review pending
  - Awaiting collective feedback

**Example**:

```markdown
- [🔄] Security policy update (review ends 2025-07-01)
```

### `📋` Agenda Item

- **Symbol**: Clipboard emoji
- **Meaning**: Scheduled for meeting discussion
- **Next Status**: `/` (In Progress)
- **Usage**:
  - Added to meeting agenda
  - Requires group decision
  - Needs collective input

**Example**:

```markdown
- [📋] Discuss budget allocation (July meeting)
```

### `🗳️` Voting

- **Symbol**: Ballot box emoji
- **Meaning**: Active democratic vote
- **Next Status**: `x` (Done)
- **Usage**:
  - Formal vote in progress
  - Decision pending member input
  - Time-sensitive democratic process

**Example**:

```markdown
- [🗳️] Vote on new member application (closes 2025-07-05)
```

### `⚡` Urgent

- **Symbol**: Lightning bolt emoji
- **Meaning**: High priority, needs immediate attention
- **Next Status**: `/` (In Progress)
- **Usage**:
  - Security issues
  - Time-critical tasks
  - Blocking other work

**Example**:

```markdown
- [⚡] Fix security vulnerability in public site
```

### `🎯` Decision Made

- **Symbol**: Target emoji
- **Meaning**: Democratic decision reached, awaiting implementation
- **Next Status**: `/` (In Progress)
- **Usage**:
  - Vote completed, decision recorded
  - Approved but not yet implemented
  - Clear mandate for action

**Example**:

```markdown
- [🎯] Implement approved proposal #456
```

## Additional Statuses

### `>` Forwarded

- **Symbol**: Greater than
- **Meaning**: Delegated to someone else
- **Usage**: Task reassigned

### `<` Scheduled

- **Symbol**: Less than
- **Meaning**: Planned for future date
- **Usage**: Deferred tasks

### `?` Question

- **Symbol**: Question mark
- **Meaning**: Needs clarification
- **Usage**: Unclear requirements

## Status Workflows

### Proposal Workflow

```
Todo → Agenda Item → Under Review → Voting → Decision Made → In Progress → Done
```

### Blocked Task Workflow

```
In Progress → Blocked → (dependency resolved) → In Progress → Done
```

### Urgent Task Workflow

```
Todo → Urgent → In Progress → Done
```

## Using Task Statuses

### In Obsidian

1. **Create task with status**:

   ```markdown
   - [ ] Regular todo
   - [/] Task in progress
   - [⏸️] Blocked task
   ```

2. **Change status**:
   - Click the checkbox to cycle through statuses
   - Or use command palette: "Tasks: Toggle task done"

3. **Filter by status**:

   ```tasks
   not done
   status.name includes "Blocked"
   status.name includes "Under Review"
   ```

### Task Queries

**Show all blocked tasks**:

```markdown
```tasks
status.symbol includes "⏸️"
```

```

**Show items for next meeting**:
```markdown
```tasks
status.symbol includes "📋"
group by heading
```

```

**Show urgent tasks**:
```markdown
```tasks
status.symbol includes "⚡"
sort by priority
```

```

## Best Practices

### DO's
- ✅ Update status as work progresses
- ✅ Add context when blocking tasks
- ✅ Set deadlines for voting tasks
- ✅ Link related tasks and proposals
- ✅ Use urgent sparingly

### DON'Ts
- ❌ Leave tasks in "In Progress" indefinitely
- ❌ Skip democratic review when required
- ❌ Mark everything as urgent
- ❌ Change voting results after deadline
- ❌ Use blocked without explanation

## Status Reporting

### Weekly Status Query
```markdown
## This Week's Tasks

### In Progress
```tasks
status.symbol includes "/"
```

### Blocked

```tasks
status.symbol includes "⏸️"
```

### Under Review

```tasks
status.symbol includes "🔄"
```

### Urgent

```tasks
status.symbol includes "⚡"
```

```

### Meeting Preparation Query
```markdown
## Upcoming Meeting Items

### Agenda Items
```tasks
status.symbol includes "📋"
not done
```

### Active Votes

```tasks
status.symbol includes "🗳️"
```

### Decisions to Implement

```tasks
status.symbol includes "🎯"
```

```

## Integration with Democratic Centralism

These task statuses support DRUIDS' democratic centralist principles:

1. **Transparency**: All members can see task status
2. **Accountability**: Clear ownership and progress tracking
3. **Democratic Process**: Review and voting statuses
4. **Collective Decision**: Agenda items and decisions
5. **Urgency Management**: Balanced priorities

## Keyboard Shortcuts

Configure in Obsidian settings:
- `Ctrl+1`: Mark as Todo
- `Ctrl+2`: Mark as In Progress
- `Ctrl+3`: Mark as Done
- `Ctrl+4`: Mark as Blocked
- `Ctrl+5`: Mark as Under Review

## Troubleshooting

**Status not appearing**: 
- Ensure Tasks plugin is updated
- Check data.json has all statuses
- Restart Obsidian

**Can't change status**:
- Verify task format is correct
- Check if status is available as command
- Try clicking checkbox instead

**Emoji not displaying**:
- Ensure Unicode support in font
- Try different emoji variation
- Check Obsidian appearance settings
