---
title: "Git in 7 Commands"
description: "Learn the only 7 Git commands you need for 90% of organizing work"
created: 2025-07-03
updated: 2025-07-03
type: "docs/tutorial"
security: "L0"
version: "1.0.0"
document_id: "TUT-GIT-2025-002-L0"
tags: ["tutorial", "git", "essential", "commands", "beginner"]
draft: true
author: ["Comrade 47"]
---

# Git in 7 Commands

*90% of organizing work needs only these 7 commands. Master these, ignore the rest until you need them.*

## The Magnificent Seven

1. `git status` - What's happening?
2. `git add` - Include this
3. `git commit` - Save forever
4. `git push` - Share with comrades
5. `git pull` - Get updates
6. `git log` - See history
7. `git init` - Start new project

That's it. Let's learn each one through real organizing work.

## Command 1: `git status` - What's Happening?

**Think of it as**: Asking "What's going on?"

**When to use**:

- Before starting work
- When confused
- Before committing
- Literally anytime you're unsure

### Try It Now

```bash
git status
```

**What you might see**:

```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

**Translation**: "Everything's saved and up to date. You're good!"

**Or you might see**:

```
Changes not staged for commit:
  modified:   meetings/2025-07-03-notes.md

Untracked files:
  proposals/rent-strike-plan.md
```

**Translation**: "You've got unsaved work. Time to commit!"

### Practice Exercise

1. Create a new file called `practice.md`
2. Run `git status`
3. See how Git notices your new file?

**Real Organizing Use**: Before every meeting, run `git status` to make sure you have the latest notes.

## Command 2: `git add` - Include This

**Think of it as**: Putting documents in an envelope before mailing

**When to use**:

- After creating new files
- After editing files
- Before committing

### The Two Ways

**Add everything** (most common):

```bash
git add .
```

The dot means "everything in this folder"

**Add specific file**:

```bash
git add meetings/2025-07-03-notes.md
```

### Try It Now

Using the practice file from before:

```bash
git add practice.md
git status
```

**What you'll see**:

```
Changes to be committed:
  new file:   practice.md
```

**Translation**: "This file is ready to be saved permanently"

### Practice Exercise

1. Create two files: `todo.md` and `ideas.md`
2. Add just `todo.md` with `git add todo.md`
3. Run `git status` - see how only one is staged?
4. Add the other with `git add ideas.md`

**Real Organizing Use**: After taking meeting notes, `git add meetings/` to include all meeting files.

## Command 3: `git commit` - Save Forever

**Think of it as**: Taking a permanent snapshot with a note attached

**When to use**:

- After completing meaningful work
- Before switching tasks
- At end of work session
- After meetings

### The Command

```bash
git commit -m "Your message here"
```

The `-m` means "message follows"

### Good Commit Messages

**Bad** ❌:

```bash
git commit -m "stuff"
git commit -m "updates"
git commit -m "asdfasdf"
```

**Good** ✅:

```bash
git commit -m "Add July 3 general meeting minutes"
git commit -m "Update rent strike proposal with legal concerns"
git commit -m "Document security protocol for protests"
```

### Try It Now

```bash
git commit -m "Add practice files for Git learning"
```

**What you'll see**:

```
[main a4f3d21] Add practice files for Git learning
 2 files changed, 10 insertions(+)
 create mode 100644 practice.md
 create mode 100644 todo.md
```

### Practice Exercise

1. Edit your `practice.md` file
2. Add it: `git add practice.md`
3. Commit with descriptive message
4. Run `git log` to see your commit

**Real Organizing Use**: After every meeting: `git commit -m "Add March 15 tenant union meeting minutes - approved rent strike timeline"`

## Command 4: `git push` - Share with Comrades

**Think of it as**: Uploading to shared drive

**When to use**:

- After committing important work
- End of work session
- Before meetings (so others have latest)
- When you want backup

### The Command

```bash
git push
```

That's it! If it's your first push on a new branch:

```bash
git push -u origin branch-name
```

### Try It Now

```bash
git push
```

**What you might see**:

```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Writing objects: 100% (3/3), 424 bytes | 424.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To github.com:org/repo.git
   a4f3d21..b5e6f32  main -> main
```

**Translation**: "Your work is now shared with everyone!"

### Practice Exercise

1. Make another commit
2. Push it
3. Ask a comrade to pull and see your changes

**Real Organizing Use**: After documenting important decisions: `git push` so absent comrades can review.

## Command 5: `git pull` - Get Updates

**Think of it as**: Downloading latest changes from comrades

**When to use**:

- Start of every work session
- Before meetings
- When comrade says they pushed changes
- If push fails with "behind" message

### The Command

`git pull`

**What you might see**:

```git
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
Updating a4f3d21..c6d7e43
Fast-forward
 meetings/2025-07-03-emergency.md | 45 ++++++++++++
 1 file changed, 45 insertions(+)
```

**Translation**: "You got updates! Here's what's new."

**Or**:

`Already up to date.`

**Translation**: "You already have everything."

### Practice Exercise

1. Ask comrade to push a change
2. Pull their change
3. Read what they added
4. Feel the magic of collaboration

**Real Organizing Use**: Before every meeting: `git pull` to ensure you have latest agenda and notes.

## Command 6: `git log` - See History

**Think of it as**: Reading the organization's diary

**When to use**:

- Finding past decisions
- Understanding changes
- Seeing who did what
- Learning from history

### The Commands

**Basic** (full details):

```bash
git log
```

**Condensed** (one line each):

```bash
git log --oneline
```

**Search** (find specific commits):

```bash
git log --grep="rent strike"
```

### Try It Now

`git log --oneline -5`

**What you'll see**:

```
b5e6f32 Add emergency meeting notes
a4f3d21 Update rent strike timeline
d3c2b1a Document legal consultation results
f9e8d7c Add March general meeting minutes
c6b5a4d Initial security protocols
```

### Practice Exercise

1. Make 3 different commits
2. Use `git log` to see full details
3. Use `git log --oneline` to see summary
4. Search for one with `git log --grep="keyword"`

**Real Organizing Use**: `git log --grep="DECISION"` to find all formal decisions made by the organization.

## Command 7: `git init` - Start New Project

**Think of it as**: Creating a new filing cabinet

**When to use**:

- Starting new campaign
- Beginning new organization
- Creating new vault
- ONE TIME at project start

### The Command

```bash
git init
```

### Try It Now

```bash
mkdir new-campaign
cd new-campaign
git init
```

**What you'll see**:

```
Initialized empty Git repository in /path/to/new-campaign/.git/
```

**Translation**: "New Git project ready for your revolutionary work!"

### Practice Exercise

1. Create a new folder for a project
2. Navigate into it
3. Run `git init`
4. Create first file and commit it

**Real Organizing Use**: Starting new campaign: `git init` in the campaign folder to track everything from day one.

## Your Daily Workflow

Here's how these 7 commands flow together:

### Morning Start

```bash
git pull                  # Get latest updates
git status               # See what's happening
```

### During Work

```bash
# Edit files, take notes, write proposals
git add .                # Stage changes
git commit -m "Clear message about work"
```

### Before Break

```bash
git push                 # Share with comrades
```

### Checking History

```bash
git log --oneline       # Review recent work
```

## Common Scenarios

### Scenario: Taking Meeting Notes

```bash
git pull                              # Get latest
# Take notes during meeting
git add meetings/2025-07-03-notes.md
git commit -m "Add July 3 general meeting notes"
git push                             # Share immediately
```

### Scenario: Proposing Something

```bash
git pull                              # Get latest
# Write proposal
git add proposals/new-idea.md
git commit -m "Propose new organizing strategy"
git push                             # Share for review
```

### Scenario: Finding Old Decision

```bash
git log --grep="phone tree"          # Search history
# Found it! Read the old discussion
```

## Practice Project: Your First Week

### Day 1

- Learn `git status` - use it 10 times
- Learn `git add` - add 3 files
- Learn `git commit` - make 3 commits

### Day 2

- Learn `git push` - share your work
- Learn `git pull` - get updates
- Practice the pull-add-commit-push cycle

### Day 3

- Learn `git log` - explore history
- Search for specific commits
- Read others' commit messages

### Day 4

- Use all commands in real work
- Take actual meeting notes
- Share with comrades

### Day 5

- Help another comrade learn one command
- Do entire workflow without referring to notes
- Celebrate!

## Troubleshooting

### "Git says I need to pull first"

```bash
git pull
# Then try your push again
```

### "I committed the wrong thing"

```bash
git log --oneline        # Find the commit
# Don't panic - ask for help
```

### "I'm lost"

```bash
git status              # Always start here
```

## The Truth About Git

You just learned 90% of what you need. Yes, there are dozens more commands. You'll learn them if/when you need them. But these 7 commands will carry you through nearly all organizing work.

## What You've Accomplished

You can now:

- ✅ Check project status
- ✅ Save work permanently
- ✅ Share with comrades
- ✅ Get others' updates
- ✅ Search history
- ✅ Start new projects

That's not "basic" - that's revolutionary infrastructure.

## Your Next Steps

1. **Today**: Practice these 7 commands
2. **This Week**: Use them for real work
3. **Next Week**: Learn [Branching Isn't Scary](/tutorials/branching-basics.md)
4. **This Month**: Teach another comrade

## Remember

- These 7 commands are enough
- Use `git status` when confused
- Commit messages matter
- Pull before push
- Help others learn

---

*"From each command according to ability, to each comrade according to need"*

Ready for more? Try [Git Through a Campaign →](/tutorials/git-through-campaign.md)
