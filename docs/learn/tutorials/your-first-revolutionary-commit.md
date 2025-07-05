---
title: "Your First Revolutionary Commit"
description: "Learn Git by creating your organization's meeting minutes - a hands-on tutorial for absolute beginners"
created: 2025-07-02
updated: 2025-07-02
type: "docs/tutorial"
security: "L0"
version: "1.0.0"
document_id: "TUT-GIT-2025-001-L0"
tags: ["tutorial", "git", "beginners", "meeting-minutes", "hands-on"]
draft: false
author: ["Comrade 47"]
---

# Your First Revolutionary Commit

*A hands-on tutorial for comrades with zero Git experience*

## What We'll Learn

By the end of this tutorial, you will:
- Create your first Git repository
- Write and save meeting minutes
- Make your first commit (a permanent record)
- Understand how this practices democratic centralism
- Feel confident to continue learning

No prior technical knowledge required. Just revolutionary determination.

## What You'll Need

- [ ] A computer (Windows, Mac, or Linux)
- [ ] 30-45 minutes of focused time
- [ ] Meeting notes to transcribe (or we'll create example ones)
- [ ] Patience with yourself - everyone starts here

## Setting Up Your Tools

First, we need to install Git. Don't worry - we'll walk through every step.

### On Ubuntu/Debian Linux

Open a terminal (press `Ctrl+Alt+T`) and type:

```bash
sudo apt update
sudo apt install git
```

When it asks for your password, type it (you won't see characters - that's normal).

### On Mac

1. Open Terminal (find it in Applications → Utilities)
2. Type: `git --version`
3. If Git isn't installed, it will prompt you to install it
4. Click "Install" and wait

### On Windows

1. Download Git from: https://git-scm.com/download/win
2. Run the installer
3. Click "Next" for all default options (they're fine)
4. Open "Git Bash" from your Start menu

### Verify It Worked

In your terminal/Git Bash, type:

```bash
git --version
```

You should see something like: `git version 2.34.1`

**Celebrate!** You just installed revolutionary infrastructure.

## Creating Your First Repository

A repository (or "repo") is like a folder with memory. It remembers every change ever made.

### Step 1: Create a Folder

```bash
# Create a new directory for our organization
mkdir ~/my-organization

# Go into that directory
cd ~/my-organization

# See where we are
pwd
```

You should see something like `/home/yourname/my-organization`

### Step 2: Initialize Git

This is the moment we create revolutionary infrastructure:

```bash
git init
```

You'll see: `Initialized empty Git repository in /home/yourname/my-organization/.git/`

**What just happened?** You created a `.git` folder that will track all changes. This is your organization's memory.

### Step 3: Configure Your Identity

Git needs to know who's making changes. We use pseudonyms for security:

```bash
git config user.name "Comrade Rosa"
git config user.email "rosa@protonmail.com"
```

Replace with your chosen pseudonym. This protects your identity while maintaining accountability.

## Writing Your First Meeting Minutes

Let's create actual organizing documentation.

### Step 1: Create the File

```bash
# Create a meetings folder
mkdir meetings

# Create our first meeting minutes file
touch meetings/2025-07-02-weekly-meeting.md
```

### Step 2: Write the Minutes

Open the file in any text editor. If you're unsure, type:

```bash
# On Linux/Mac
nano meetings/2025-07-02-weekly-meeting.md

# On Windows Git Bash
notepad meetings/2025-07-02-weekly-meeting.md
```

Now type (or paste) these meeting minutes:

```markdown
# Weekly Organizing Meeting
Date: July 2, 2025
Attendees: Rosa, Karl, Vladimir, Clara

## Agenda
1. Review last week's actions
2. Plan upcoming mutual aid
3. Security check-in
4. Next steps

## Discussion

### Last Week's Actions
- Rosa: Completed flyer design ✓
- Karl: Contacted food bank ✓
- Vladimir: Security audit (in progress)

### Mutual Aid Planning
Decision: Saturday July 6, 2pm at People's Park
- Food distribution
- Know Your Rights training
- Childcare provided

### Security Notes
- Reminder: Use Signal for coordination
- New member vetting process working well
- No incidents to report

## Decisions Made
1. Mutual aid event July 6 (unanimous)
2. Create dedicated roles for event (approved)
3. Budget $200 for supplies (approved)

## Action Items
- Clara: Reserve park space
- Rosa: Final flyer + social media
- Karl: Coordinate food pickup
- Vladimir: Complete security audit

## Next Meeting
July 9, 2025 - same time, Clara facilitating
```

Save the file (`Ctrl+X` then `Y` in nano, or just save in notepad).

### Step 3: See What Git Sees

```bash
git status
```

You'll see:
```
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        meetings/

nothing added to commit but untracked files present
```

Git sees our new folder but isn't tracking it yet.

## Making Your First Revolutionary Commit

This is the moment we practice democratic centralism - collective decisions preserved forever.

### Step 1: Stage the Changes

```bash
git add meetings/
```

Run `git status` again:
```
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   meetings/2025-07-02-weekly-meeting.md
```

The file is now "staged" - ready to be committed to history.

### Step 2: Make the Commit

```bash
git commit -m "Add July 2 weekly meeting minutes

- Documented mutual aid planning for July 6
- Recorded security check-in results  
- Assigned action items to comrades
- Practicing democratic centralism through Git"
```

You'll see something like:
```
[main 8a3f2d1] Add July 2 weekly meeting minutes
 1 file changed, 45 insertions(+)
 create mode 100644 meetings/2025-07-02-weekly-meeting.md
```

### Step 3: View Your Revolutionary History

```bash
git log
```

You'll see:
```
commit 8a3f2d1... (HEAD -> main)
Author: Comrade Rosa <rosa@protonmail.com>
Date:   Tue Jul 2 22:30:00 2025 -0500

    Add July 2 weekly meeting minutes
    
    - Documented mutual aid planning for July 6
    - Recorded security check-in results
    - Assigned action items to comrades
    - Practicing democratic centralism through Git
```

**CELEBRATE!** You just created permanent, tamper-proof organizational history!

## Understanding What We Just Did

### This Isn't Just File Storage

What makes this revolutionary:

1. **Permanent Record**: That commit can never be secretly altered
2. **Accountability**: Every change is attributed (to pseudonyms)
3. **Democratic Process**: Decisions are documented and preserved
4. **No Memory Holes**: Can't delete inconvenient history
5. **Collective Ownership**: Not dependent on any individual

### How This Practices Democratic Centralism

- **Freedom of Discussion**: Create branches to propose changes
- **Unity of Action**: Merge approved changes to main branch
- **Minority Positions**: History preserves all proposals, even rejected ones
- **Collective Memory**: Organization's knowledge isn't in one person's head

## Common Problems and Solutions

### "Command not found"

You might be in the wrong terminal. Make sure you're using:
- Terminal (Mac/Linux)
- Git Bash (Windows)

### "Permission denied"

On Linux/Mac, you might need `sudo` for installation:
```bash
sudo apt install git  # Add sudo
```

### "I made a typo in my commit message!"

For your most recent commit:
```bash
git commit --amend -m "New corrected message"
```

### "I committed the wrong file!"

Don't panic. We can fix this:
```bash
git reset HEAD~1  # Undo last commit but keep changes
# Now commit the right files
```

## Your Next Steps

### 1. Practice with Real Work

Next meeting, volunteer to take notes and commit them:
- Take notes during meeting
- Type them up in Markdown
- Commit with descriptive message
- Show comrades the git log

### 2. Learn About Branches

Branches let multiple comrades work without conflict:
```bash
git branch mutual-aid-planning
git checkout mutual-aid-planning
# Make changes here without affecting main
```

### 3. Connect with Comrades

Share your repository:
- Show others your commit history
- Teach someone else their first commit
- Build collective knowledge

## What You've Accomplished

You've just:
- Installed revolutionary infrastructure
- Created organizational memory
- Practiced democratic centralism
- Taken first step toward collective liberation
- Joined the tradition of revolutionary record-keeping

Your meeting minutes are no longer just notes - they're part of permanent revolutionary history.

## Remember

Every commit is a small act of revolution. You're building infrastructure that:
- Can't be controlled by corporations
- Preserves organizational memory
- Practices collective decision-making
- Prepares for state repression

Welcome to the revolutionary infrastructure, comrade.

---

*"The step from theory to practice is the most revolutionary step."*

Next tutorial: [[../git-basics/git-in-7-commands|Git in 7 Commands →]]