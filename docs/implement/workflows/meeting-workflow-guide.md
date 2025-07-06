---
title: "Meeting Workflow Guide"
description: "Documentation for Meeting Workflow Guide"
type: "how-to"
security: "L0"
document_id: "HTG-2025-888-L0"
version: "1.0.0"
tags: ["implementation", "workflows"]
---
# Meeting Workflow Guide for DRUIDS

## Introduction

This guide provides comprehensive instructions for managing meetings within the DRUIDS framework, from planning through follow-up. It covers template usage, minute-taking, action item tracking, and integration with democratic centralist principles.

## Prerequisites

- Obsidian vault configured with templates
- Basic familiarity with Markdown
- Understanding of your organization's meeting structure
- Access to appropriate security tier vault (L0 for public, L1 for internal)

## Meeting Types and Templates

### General Meetings (Monthly)

- **Purpose**: Organization-wide updates, voting, general business
- **Security**: Usually L1, announcements can be L0
- **Duration**: 60-90 minutes typically

### Committee Meetings

- **Purpose**: Focused work on specific areas
- **Security**: L1 for internal committees
- **Duration**: 45-60 minutes

### Criticism/Self-Criticism (CSC) Sessions

- **Purpose**: Organizational development and accountability
- **Security**: Always L1 (personal development content)
- **Duration**: 60-90 minutes

### Emergency Meetings

- **Purpose**: Urgent decisions required
- **Security**: Depends on topic
- **Duration**: As needed

## Step-by-Step Meeting Workflow

### 1. Pre-Meeting Preparation (3-7 days before)

#### Time Estimate: 30-45 minutes

**a) Create Meeting Announcement**

1. Open appropriate vault (L0 for public announcements)
2. Create new file: `01-meetings/announcements/YYYY-MM-DD-general-meeting-announcement.md`
3. Use template:

```markdown
---
document_id: EXT-MIN-2024-001-L0
title: "General Meeting - January 2024"
type: announcement
security: L0
date: 2024-01-15
time: "19:00"
location: "Main Hall / Online"
author: "Secretary"
tags: [meeting, announcement, general]
---

# General Meeting - January 2024

**When**: Monday, January 15, 2024 at 7:00 PM
**Where**: Main Hall (123 Main St) or via secure video link
**Who**: All members and invited guests

## Agenda

1. Opening and attendance (5 min)
2. Review of previous minutes (10 min)
3. Committee reports (20 min)
4. Old business (15 min)
5. New business (30 min)
6. Announcements (5 min)
7. Closing (5 min)

## How to Participate

- **In Person**: Arrive 10 minutes early for setup
- **Online**: Link will be sent to member emails 1 hour before
- **Proposals**: Submit via proposal process by January 12

## What to Bring

- Previous meeting minutes (available in shared drive)
- Any proposals or reports you're presenting
- Questions for committee chairs

Contact secretary@organization.org with questions.
```

**b) Prepare Meeting Folder**

In L1 vault:

```bash
01-meetings/minutes/2024/01-january/
├── 2024-01-15-general-meeting/
│   ├── agenda.md
│   ├── attendance.md
│   ├── minutes.md (created during meeting)
│   └── action-items.md (created post-meeting)
```

**c) Pre-populate Agenda**

Create `agenda.md` with details:

```markdown
---
document_id: INT-MIN-2024-001-L1
title: "General Meeting Agenda - January 2024"
type: agenda
security: L1
meeting_date: 2024-01-15
facilitator: "Chairperson"
timekeeper: "Member A"
stack_keeper: "Member B"
---

# General Meeting Agenda
## January 15, 2024

### Roles
- **Facilitator**: Chairperson
- **Timekeeper**: Member A
- **Stack Keeper**: Member B
- **Minutes**: Secretary

### Agenda Items

1. **Opening** (7:00-7:05)
   - Acknowledge land/labor
   - Review meeting agreements
   
2. **Attendance** (7:05-7:10)
   - Roll call
   - Quorum verification
   
3. **Previous Minutes** (7:10-7:20)
   - Review December minutes
   - Corrections/amendments
   - Motion to approve

[Continue with full agenda...]
```

### 2. During the Meeting

#### Time Estimate: Throughout meeting duration

**a) Meeting Minutes Template**

Create `minutes.md` at meeting start:

```markdown
---
document_id: INT-MIN-2024-002-L1
title: "General Meeting Minutes - January 2024"
type: minutes
security: L1
meeting_date: 2024-01-15
start_time: "19:00"
end_time: ""
attendees: []
apologies: []
facilitator: "Chairperson"
minutes_taker: "Secretary"
status: draft
tags: [meeting, minutes, general, 2024-01]
---

# General Meeting Minutes
## January 15, 2024

### Meeting Details
- **Called to Order**: 7:00 PM
- **Adjourned**: [Fill at end]
- **Location**: Main Hall / Online Hybrid
- **Quorum**: Yes (15/20 members present)

### Attendance

**Present** (15):
- Member A (Chair)
- Member B 
- Member C (Online)
[Continue list...]

**Apologies** (3):
- Member X (traveling)
- Member Y (illness)
- Member Z (work conflict)

**Guests** (2):
- Guest 1 (invited speaker)
- Guest 2 (prospective member)

### Minutes

#### 1. Opening (7:00 PM)
- Chairperson opened meeting
- Land acknowledgment read
- Meeting agreements reviewed

#### 2. Previous Minutes
**Motion**: "To approve the December 2023 minutes as distributed"
- Moved: Member D
- Seconded: Member E
- Discussion: Correction to attendance count
- **Vote**: 14-0-1 (Yes-No-Abstain)
- **Result**: PASSED

#### 3. Committee Reports

##### Education Committee (Member F reporting)
- Completed orientation for 3 new members
- Upcoming workshop on "Digital Security" scheduled for Jan 28
- Request for $200 budget for materials
- Full report attached as Appendix A

##### Tech Committee (Member G reporting)
- DRUIDS implementation 60% complete
- Need 2 more volunteers for documentation
- Next sprint planning Feb 1

[Continue with detailed notes...]
```

**b) Real-time Note-taking Best Practices**

1. **Focus on Decisions and Actions**
   - Record all motions verbatim
   - Note who moved and seconded
   - Record exact vote counts
   - Capture assigned actions with deadlines

2. **Summarize Discussions**
   - Key points raised, not every word
   - Significant disagreements or concerns
   - Rationale for decisions

3. **Use Shortcuts During Meeting**

   ```
   M: = Motion
   S: = Seconded by
   AI: = Action Item
   Q: = Question raised
   ```

4. **Clean Up Immediately After**
   - Expand shortcuts
   - Fix formatting
   - Add missed details while fresh

### 3. Post-Meeting Processing

#### Time Estimate: 45-60 minutes (within 24 hours)

**a) Extract Action Items**

Create `action-items.md`:

```markdown
---
document_id: INT-MIN-2024-003-L1
title: "Action Items - General Meeting January 2024"
type: action-items
security: L1
source_meeting: "2024-01-15"
created: 2024-01-16
status: active
---

# Action Items from General Meeting
## January 15, 2024

### High Priority (Due within 1 week)

- [ ] **Submit grant application**
  - Assigned to: Member H
  - Due: January 22, 2024
  - Details: Complete and submit Form 990 to Foundation X
  - Approved budget: $5,000 request

- [ ] **Send new member welcome packets**
  - Assigned to: Education Committee
  - Due: January 20, 2024
  - Details: Prepare and send to 3 new members approved tonight

### Medium Priority (Due within 2 weeks)

- [ ] **Update website with meeting minutes**
  - Assigned to: Tech Committee
  - Due: January 29, 2024
  - Details: Post public portions of minutes to website

[Continue with all items...]

### Tracking

| Item | Assigned | Due Date | Status | Completed |
|------|----------|----------|---------|-----------|
| Grant application | Member H | 2024-01-22 | In Progress | |
| Welcome packets | Ed Comm | 2024-01-20 | Not Started | |
| Website update | Tech Comm | 2024-01-29 | Not Started | |
```

**b) Create Follow-up Tasks**

In your task management system:

```markdown
---
kanban-plugin: basic
---

## To Do

- [ ] Email Member H re: grant application support
- [ ] Schedule check-in with Education Committee
- [ ] Add action items to next meeting agenda

## In Progress

- [ ] Clean up meeting minutes for distribution

## Done

- [x] Created action items document
- [x] Updated attendance records
```

### 4. Distribution and Archival

#### Time Estimate: 15-20 minutes

**a) Prepare Distribution Version**

1. Remove sensitive discussions from public version
2. Create summary for members who missed meeting
3. Highlight key decisions and next steps

**b) Distribution Checklist**

- [ ] Minutes reviewed by second person
- [ ] Action items sent to assignees
- [ ] Public summary created (if needed)
- [ ] Files committed to repository
- [ ] Email sent to members list
- [ ] Calendar updated with next meeting

### Meeting Templates Library

#### Basic Meeting Template

Save as `templates/meeting-minutes-template.md`:

```markdown
---
document_id: {{document_id}}
title: "{{title}}"
type: minutes
security: {{security_level}}
meeting_date: {{date}}
start_time: "{{time}}"
end_time: ""
attendees: []
apologies: []
facilitator: ""
minutes_taker: "{{author}}"
status: draft
---

# {{title}}
## {{date}}

### Meeting Details
- **Called to Order**: 
- **Adjourned**: 
- **Location**: 
- **Quorum**: Yes/No (XX/XX members present)

### Attendance

**Present** (X):
- 

**Apologies** (X):
- 

**Guests** (X):
- 

### Minutes

#### 1. Opening
- 

#### 2. Previous Minutes
**Motion**: "To approve the [MONTH YEAR] minutes as distributed"
- Moved: 
- Seconded: 
- Discussion: 
- **Vote**: X-X-X (Yes-No-Abstain)
- **Result**: PASSED/FAILED

### Action Items
- [ ] 

### Next Meeting
- Date: 
- Time: 
- Location: 

### Adjournment
Meeting adjourned at XX:XX PM

---
*Minutes prepared by: {{author}}*
*Minutes approved: [DATE]*
```

## Automated GitHub Workflow

### What the Meeting Minutes Workflow Does

The Meeting Minutes workflow is a GitHub Action that **automatically creates a discussion thread for your meeting notes**. This automation complements the manual process by providing consistent, pre-formatted templates.

#### The Simple Version

When you trigger this workflow, it creates a new GitHub Discussion post with a pre-formatted template for meeting minutes, ready for someone to fill in with actual meeting notes.

#### Step-by-Step Process

1. **You trigger the workflow** by providing:
   - Meeting date (like "2024-12-28")
   - Meeting type (general, committee, executive, working-group)
   - Security level (L0 for public, L1 for member-only)

2. **The workflow validates your inputs**:
   - Checks the date is in YYYY-MM-DD format
   - Ensures the meeting type is valid
   - Confirms the security level is appropriate

3. **It finds the right discussion category**:
   - Dynamically looks for a category called "meeting-minutes" in your GitHub Discussions
   - If it can't find it, it tells you to create one
   - No more hardcoded category IDs!

4. **It generates a formatted discussion post** with:
   - A title like: "2024-12-28 General Meeting Minutes"
   - A pre-filled template including:
     - Meeting metadata (date, type, who attended)
     - Sections for agenda, discussions, decisions, action items
     - Security classification notice
     - Proper document ID following DRUIDS standards

5. **It creates the discussion** in your repository's Discussions tab

#### Why Use the Automated Workflow

- **Consistency**: Every meeting gets the same professional template
- **Speed**: No manual copying or formatting needed
- **Organization**: All meetings automatically go to the correct category
- **Security-aware**: Includes proper security classifications
- **Trackable**: Creates a permanent, searchable record in GitHub
- **Error-free**: No typos in dates or document IDs

#### Real Example

If you run it with:

- Date: "2024-12-28"
- Type: "general"
- Security: "L0"

It creates a discussion titled "2024-12-28 General Meeting Minutes" with a complete template ready for the secretary to fill in during or after the meeting.

#### How to Use the Workflow

1. **From GitHub Actions page**:
   - Go to Actions tab in your repository
   - Find "Meeting Minutes" workflow
   - Click "Run workflow"
   - Fill in the date, type, and security level
   - Click "Run workflow" button

2. **From GitHub CLI**:

   ```bash
   gh workflow run meeting-minutes.yml \
     -f meeting_date=2024-12-28 \
     -f meeting_type=general \
     -f security_level=L0
   ```

3. **Check the results**:
   - Go to Discussions tab
   - Find your new meeting minutes discussion
   - Start adding the actual meeting content

### Integration with Manual Process

The automated workflow creates the initial discussion, then you follow the manual process:

1. **Before the meeting**: Run the workflow to create the discussion
2. **During the meeting**: Open the discussion and fill in the template in real-time
3. **After the meeting**: Extract action items and create follow-ups as documented above

This hybrid approach gives you the best of both worlds - automation for consistency and manual flexibility for content.

### Integration with Democratic Processes

#### Proposal Tracking

During meetings, track proposals through their lifecycle:

```markdown
### Proposal: Implement New Security Protocols

**Submitted by**: Member J
**Submitted**: January 8, 2024
**First Reading**: January 15, 2024
**Status**: Tabled for further discussion

**Discussion Points**:
- Cost concerns raised by Member K
- Support from Tech Committee
- Request for detailed implementation plan

**Next Steps**:
- Tech Committee to prepare detailed plan
- Budget impact analysis by Treasurer
- Second reading at February meeting
```

#### Voting Records

Maintain clear voting records:

```markdown
### Motion: Allocate $500 for Workshop Series

**Motion Text**: "To allocate $500 from the education budget for a three-part workshop series on digital security"

**Process**:
- Moved by: Member L
- Seconded by: Member M
- Discussion: 10 minutes
- Amendment: Increase to $600 (accepted as friendly)

**Vote**:
- Yes: 12 (Members A, B, C, D, E, F, G, H, I, J, K, L)
- No: 2 (Members M, N)
- Abstain: 1 (Member O - conflict of interest declared)

**Result**: PASSED (12-2-1)
```

### Common Issues and Solutions

**Issue**: "Minutes are too detailed/not detailed enough"

- **Solution**: Focus on decisions, actions, and key discussion points
- **Guideline**: Someone absent should understand what happened and what they need to do

**Issue**: "Can't keep up during fast discussions"

- **Solution**: Ask for clarification or to slow down
- **Alternative**: Record meeting (with consent) for reference
- **Pro tip**: Use abbreviations during meeting, expand after

**Issue**: "Action items get lost"

- **Solution**: Dedicated action items document
- **Tool**: Use Obsidian Tasks plugin for tracking
- **Automation**: Set up reminder system

**Issue**: "Multiple people editing minutes simultaneously"

- **Solution**: Designate single minute-taker
- **Alternative**: Use collaborative editor during meeting, single person cleans up
- **Git Solution**: Create branch for meeting, merge after

**Issue**: "Attendance tracking is tedious"

- **Solution**: Pre-meeting check-in form
- **Automation**: QR code sign-in that updates attendance file

**Issue**: "Meeting runs over time"

- **Solution**: Strict timekeeper role
- **Tool**: Visual timer visible to all
- **Process**: Parking lot for items that need more time

### Advanced Automation Scripts

#### Meeting Setup Automation

```bash
#!/bin/bash
# setup-meeting.sh - Automate meeting preparation

MEETING_DATE=$1
MEETING_TYPE=$2
VAULT_PATH="~/Documents/druids-vault"

# Create meeting structure
create_meeting_structure() {
    local date=$1
    local type=$2
    local year=$(date -d "$date" +%Y)
    local month=$(date -d "$date" +%m-%B | tr '[:upper:]' '[:lower:]')
    
    # Create directories
    mkdir -p "$VAULT_PATH/01-meetings/minutes/$year/$month/$date-$type-meeting"
    
    # Copy templates
    cp "$VAULT_PATH/templates/meeting-agenda-template.md" \
       "$VAULT_PATH/01-meetings/minutes/$year/$month/$date-$type-meeting/agenda.md"
    
    cp "$VAULT_PATH/templates/meeting-minutes-template.md" \
       "$VAULT_PATH/01-meetings/minutes/$year/$month/$date-$type-meeting/minutes.md"
    
    # Update dates in templates
    sed -i "s/{{date}}/$date/g" "$VAULT_PATH/01-meetings/minutes/$year/$month/$date-$type-meeting/*.md"
    sed -i "s/{{type}}/$type/g" "$VAULT_PATH/01-meetings/minutes/$year/$month/$date-$type-meeting/*.md"
    
    echo "✓ Meeting structure created for $date $type meeting"
}

# Send reminders
send_reminders() {
    local date=$1
    local days_before=$2
    
    # Calculate reminder date
    local reminder_date=$(date -d "$date - $days_before days" +%Y-%m-%d)
    
    # Create reminder task
    echo "- [ ] Send meeting reminder @due($reminder_date)" >> "$VAULT_PATH/tasks.md"
}

# Main execution
create_meeting_structure "$MEETING_DATE" "$MEETING_TYPE"
send_reminders "$MEETING_DATE" 3
send_reminders "$MEETING_DATE" 1

# Create calendar event
echo "Meeting created! Don't forget to:"
echo "1. Add to shared calendar"
echo "2. Book meeting space"
echo "3. Test tech setup if hybrid"
```

#### Action Item Tracker

```python
#!/usr/bin/env python3
# track-action-items.py - Extract and track action items across meetings

import os
import re
from datetime import datetime
import yaml

def extract_action_items(file_path):
    """Extract action items from meeting minutes"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find action items section
    action_items = []
    in_action_section = False
    
    for line in content.split('\n'):
        if 'action items' in line.lower():
            in_action_section = True
            continue
        
        if in_action_section:
            # Match checkbox items
            match = re.match(r'- \[[ x]\] \*\*(.*?)\*\*', line)
            if match:
                item_text = match.group(1)
                # Extract assigned to
                assigned_match = re.search(r'Assigned to: (.*?)(?:\n|$)', content[content.find(item_text):])
                assigned_to = assigned_match.group(1) if assigned_match else 'Unassigned'
                
                # Extract due date
                due_match = re.search(r'Due: (.*?)(?:\n|$)', content[content.find(item_text):])
                due_date = due_match.group(1) if due_match else 'No due date'
                
                action_items.append({
                    'task': item_text,
                    'assigned_to': assigned_to,
                    'due_date': due_date,
                    'source_file': file_path,
                    'status': 'completed' if '[x]' in line else 'pending'
                })
    
    return action_items

def generate_action_report(vault_path):
    """Generate comprehensive action item report"""
    all_actions = []
    
    # Walk through meeting minutes
    for root, dirs, files in os.walk(os.path.join(vault_path, '01-meetings/minutes')):
        for file in files:
            if file == 'action-items.md':
                file_path = os.path.join(root, file)
                actions = extract_action_items(file_path)
                all_actions.extend(actions)
    
    # Generate report
    report = "# Action Items Report\n\n"
    report += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    
    # Group by person
    by_person = {}
    for action in all_actions:
        person = action['assigned_to']
        if person not in by_person:
            by_person[person] = []
        by_person[person].append(action)
    
    # Write report
    for person, actions in sorted(by_person.items()):
        report += f"## {person}\n\n"
        
        pending = [a for a in actions if a['status'] == 'pending']
        completed = [a for a in actions if a['status'] == 'completed']
        
        report += f"**Pending**: {len(pending)} | **Completed**: {len(completed)}\n\n"
        
        if pending:
            report += "### Pending Tasks\n\n"
            for action in sorted(pending, key=lambda x: x['due_date']):
                report += f"- [ ] **{action['task']}**\n"
                report += f"  - Due: {action['due_date']}\n"
                report += f"  - Source: {os.path.basename(os.path.dirname(action['source_file']))}\n\n"
    
    return report

if __name__ == "__main__":
    import sys
    vault_path = sys.argv[1] if len(sys.argv) > 1 else "."
    report = generate_action_report(vault_path)
    
    # Save report
    with open(os.path.join(vault_path, 'action-items-report.md'), 'w') as f:
        f.write(report)
    
    print("✓ Action items report generated")
```

#### Meeting Analytics

```bash
#!/bin/bash
# meeting-analytics.sh - Generate meeting statistics

VAULT_PATH="${1:-$HOME/Documents/druids-vault}"
YEAR="${2:-$(date +%Y)}"

echo "# Meeting Analytics Report - $YEAR"
echo "Generated: $(date)"
echo

# Count meetings by type
echo "## Meetings by Type"
find "$VAULT_PATH/01-meetings/minutes/$YEAR" -name "minutes.md" -type f | while read -r file; do
    grep -h "type: " "$file" 2>/dev/null || true
done | sort | uniq -c | while read count type; do
    echo "- ${type#type: }: $count"
done

echo
echo "## Attendance Trends"

# Average attendance
total_attendance=0
meeting_count=0

find "$VAULT_PATH/01-meetings/minutes/$YEAR" -name "minutes.md" -type f | while read -r file; do
    attendance=$(grep -A1 "Present" "$file" | grep -o "[0-9]*" | head -1)
    if [ -n "$attendance" ]; then
        total_attendance=$((total_attendance + attendance))
        meeting_count=$((meeting_count + 1))
    fi
done

if [ $meeting_count -gt 0 ]; then
    avg_attendance=$((total_attendance / meeting_count))
    echo "Average attendance: $avg_attendance members"
fi

echo
echo "## Action Items Completion Rate"

total_actions=0
completed_actions=0

find "$VAULT_PATH/01-meetings/minutes/$YEAR" -name "action-items.md" -type f | while read -r file; do
    total=$(grep -c "^\- \[[ x]\]" "$file" || true)
    completed=$(grep -c "^\- \[x\]" "$file" || true)
    
    total_actions=$((total_actions + total))
    completed_actions=$((completed_actions + completed))
done

if [ $total_actions -gt 0 ]; then
    completion_rate=$((completed_actions * 100 / total_actions))
    echo "Completion rate: $completion_rate% ($completed_actions/$total_actions)"
fi

echo
echo "## Meeting Duration Analysis"

# Extract meeting durations
find "$VAULT_PATH/01-meetings/minutes/$YEAR" -name "minutes.md" -type f | while read -r file; do
    start_time=$(grep "start_time:" "$file" | cut -d'"' -f2)
    end_time=$(grep "end_time:" "$file" | cut -d'"' -f2)
    
    if [ -n "$start_time" ] && [ -n "$end_time" ]; then
        # Calculate duration (requires date command that supports time math)
        duration=$(( $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) ))
        duration_min=$((duration / 60))
        
        meeting_type=$(grep "type:" "$file" | awk '{print $2}')
        echo "$meeting_type: $duration_min minutes"
    fi
done | sort | awk '{
    type=$1
    duration=$2
    
    count[type]++
    total[type] += duration
}
END {
    for (t in count) {
        avg = total[t] / count[t]
        printf "%s average: %.0f minutes\n", t, avg
    }
}'
```

### Success Metrics

Track your meeting management effectiveness:

- Minutes completed within 24 hours: Target 100%
- Action items completed by deadline: Target 80%
- Member attendance rate: Track trends
- Meeting time efficiency: Stay within scheduled time

### Next Steps

1. Customize templates for your organization
2. Train all potential minute-takers
3. Establish rotation schedule for meeting roles
4. Create meeting archives structure
5. Integrate with project management workflow

Remember: Good meeting management is the backbone of democratic centralist organizations. Clear records enable accountability and collective decision-making.

## Quick Reference Guide

### Meeting Roles Cheatsheet

| Role | Responsibilities | Key Tasks |
|------|-----------------|-----------|
| **Facilitator** | Guide discussion, maintain focus | Follow agenda, manage stack, enforce time |
| **Timekeeper** | Track time per agenda item | Give warnings (5 min, 1 min), suggest moving on |
| **Stack Keeper** | Manage speaking order | Track raised hands, ensure equity |
| **Minutes Taker** | Record decisions and discussions | Focus on actions, decisions, key points |
| **Vibes Watcher** | Monitor group energy | Suggest breaks, note tensions |

### Quick Commands

```bash
# Before meeting
./setup-meeting.sh 2024-01-15 general

# During meeting (in Obsidian)
Ctrl+T: Insert timestamp
Alt+C: Insert checkbox
Ctrl+Shift+M: Meeting template

# After meeting
./track-action-items.py ~/druids-vault
git add meetings/2024/01-january/
git commit -m "Add January general meeting minutes"
git push
```

### Meeting Minute Must-Haves

- [ ] Date, time, location
- [ ] Attendance (present, apologies, guests)  
- [ ] All motions word-for-word
- [ ] Vote counts (Yes-No-Abstain)
- [ ] Action items with assignee and deadline
- [ ] Next meeting date

### Common Motion Language

```markdown
"I move to..."
"I move that we..."
"I move to amend the motion by..."
"I call the question" (end debate)
"I move to table" (postpone)
"Point of order" (procedural issue)
"Point of information" (question)
```
