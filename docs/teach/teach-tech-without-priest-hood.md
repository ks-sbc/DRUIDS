---
title: "How to Teach Tech Without Being a Tech Priest"
description: "Practical guide for transferring technical knowledge without maintaining hierarchy"
created: 2025-07-04
updated: 2025-07-04
type: "docs/how-to"
security: "L0"
version: "1.0.0"
document_id: "HOW-EDU-2025-001-L0"
tags: ["how-to", "education", "teaching", "anti-hierarchy", "knowledge-transfer"]
draft: true
author: ["Comrade 47"]
---

# How to Teach Tech Without Being a Tech Priest

*A practical guide for tech workers who want to transfer knowledge, not maintain hierarchy*

## The Problem You're Solving

You know things that could help revolutionary movements. But every time you try to help, you accidentally:
- Become "the tech person" everyone depends on
- Use jargon that excludes rather than educates
- Build tools FOR people instead of WITH them
- Maintain the very hierarchy you want to destroy

This guide helps you break that pattern.

## Pre-Teaching Preparation

### 1. Check Your Assumptions

Before teaching anything, examine your beliefs:

**Tech Priest Assumes:**
- "They won't understand the real explanation"
- "I need to simplify this for non-technical people"
- "They just need to know enough to use it"
- "Teaching properly takes too long"

**Liberatory Teacher Assumes:**
- "They understand complex organizing - they can understand this"
- "I need to translate jargon, not simplify concepts"
- "They need to understand WHY, not just HOW"
- "Teaching properly saves time long-term"

### 2. Learn Their Context

Before teaching Git to organizers, understand:
- What tools do they currently use?
- What problems do they actually face?
- What language do they use for their work?
- What are their actual fears about technology?

**Bad**: "Let me teach you version control"  
**Good**: "Show me how you currently share meeting notes"

**Ready for a concrete example?** See our [[git-through-campaign-template|Git Through Campaign Workshop Template]] for how to teach Git using organizing scenarios.

### 3. Prepare Liberatory Materials

Your teaching materials should:
- Use examples from their work, not abstract concepts
- Include the "why" not just the "how"
- Provide multiple learning paths
- Be available for future reference
- Include troubleshooting for real scenarios

## During Teaching: Anti-Hierarchy Practices

### 1. Start with Shared Language

**Tech Priest**: "Git uses a directed acyclic graph to store commits"  
**Liberatory**: "Git is like tracking changes in a document, but more powerful"

Always start with concepts they know, then build bridges:
- "You know how Google Docs shows edit history? Git is like that but..."
- "Remember doing security culture trainings? Git commits are like that..."
- "Think of branches like working groups that merge their work..."

### 2. Teach Concepts Before Commands

**Tech Priest Approach:**
```
"Type these commands:
git add .
git commit -m 'message'
git push"
```

**Liberatory Approach:**
```
"Let's understand what we're doing:
1. We're selecting which changes to save (like choosing which notes matter)
2. We're creating a permanent record with context (like meeting minutes)
3. We're sharing with comrades (like posting to Signal)

Now let's see how Git does this..."
```

### 3. Make Mistakes Publicly

Tech priests never make mistakes. Liberatory teachers do:

```bash
$ git pish
git: 'pish' is not a git command. See 'git --help'.

"Oops, I meant 'push'. See? Git tells you when something's wrong. 
You literally cannot break anything permanently."
```

This shows:
- Everyone makes typos
- Errors aren't scary
- Git is forgiving
- You're learning together

### 4. Rotate the Keyboard

**Tech Priest**: Types everything while others watch  
**Liberatory**: "Who wants to drive? I'll navigate."

Physical control matters. When they type:
- They embody the knowledge
- They overcome fear through action
- They own the process
- You become guide, not guru

### 5. Connect to Political Work

Every technical concept has a political parallel:

| Tech Concept | Political Parallel |
|--------------|-------------------|
| Commits | Meeting minutes that can't be lost |
| Branches | Working groups developing proposals |
| Merging | Democratic consolidation of ideas |
| Conflicts | Competing proposals needing synthesis |
| History | Institutional memory preserved |

### 6. Acknowledge Multiple Paths

**Tech Priest**: "This is the right way"  
**Liberatory**: "Here are three ways - pick what works"

Example with Git:
- "Visual people might prefer GitHub Desktop"
- "Command line gives more control"
- "VS Code has Git built in"
- "All valid - let's try each"

## Common Teaching Scenarios

### Scenario 1: "I Could Never Learn That"

**Tech Priest Response**: "Don't worry, I'll handle the technical stuff"  
**Liberatory Response**: "You organize workers against capital. This is easier."

Then prove it:
1. Start with something they succeeded at
2. Show the parallel to tech concept
3. Let them do one small thing successfully
4. Build confidence through repetition

### Scenario 2: "Just Set It Up For Me"

**Tech Priest Response**: Sets it up, maintains dependency  
**Liberatory Response**: "Let's set it up together so you can do it next time"

Process:
1. "I'll do first step while you watch"
2. "You do second step while I guide"
3. "You do third step while I watch"
4. "You teach someone else tomorrow"

### Scenario 3: "What If I Break Something?"

**Tech Priest Response**: "Don't worry, I'll fix it"  
**Liberatory Response**: "Let's break it on purpose and fix it together"

Create safe failure:
```bash
# Make a test repository
mkdir test-break-things
cd test-break-things
git init

# Now mess it up!
# Delete files, make mistakes, experiment
# Show how to recover everything
```

### Scenario 4: "I Don't Have Time to Learn"

**Tech Priest Response**: "I'll just do it for you"  
**Liberatory Response**: "Learning saves time within a week"

Show the math:
- "How long to wait for me each time? 2 days?"
- "How many times per month? 5?"
- "That's 10 days waiting vs 2 hours learning"

## Post-Teaching: Ensuring Independence

### 1. Create Documentation Together

Don't write docs FOR them. Write WITH them:
- They describe the problem in their words
- You provide technical solution
- They write the steps as they understand them
- You review for accuracy, not style

### 2. Establish Peer Learning

**Tech Priest**: Remains sole source of knowledge  
**Liberatory**: Creates learning networks

Actions:
- Connect learners with each other
- Create practice groups
- Celebrate when they teach others
- Step back as they step up

### 3. Regular Check-ins Without Solving

Schedule follow-ups where you:
- Ask what they've accomplished
- Celebrate their independence
- Refuse to solve problems directly
- Guide them to solutions instead

### 4. Document Patterns, Not Just Solutions

Help them recognize patterns:
- "Notice how Git errors usually tell you what to do?"
- "See how the workflow is always: change, stage, commit, share?"
- "Pattern: When stuck, check status first"

## Anti-Patterns to Avoid

### The Humble Brag
"Oh this? It's super easy once you understand the underlying Merkle tree structure..."

### The Overwhelm
Teaching everything about Git instead of the 7 commands they need

### The Rescue
Jumping in to fix things instead of guiding them to fix it

### The Gatekeeper
"You're not ready for that advanced feature" (Let them decide!)

### The Priest's Tools
Using your special aliases, custom setup, or advanced tools while teaching

## Success Metrics

You're succeeding when:
- They stop asking you for help
- They start teaching others
- They propose technical solutions you hadn't considered
- They correct your mistakes
- You become unnecessary

## A Personal Practice

Before each teaching session, remind yourself:
- "I am transferring power, not demonstrating it"
- "Their struggle context matters more than my technical context"
- "Every question is legitimate"
- "My goal is my own obsolescence"

## Example: Teaching Git in 1 Hour

**0-10 min**: Their current workflow and pain points  
**10-20 min**: Git solves these specific problems (demos)  
**20-40 min**: They drive, you navigate through basics  
**40-50 min**: They do it solo with you watching  
**50-60 min**: Plan their practice and next steps  

## The Revolutionary Teaching Moment

The moment you know you've succeeded isn't when they thank you for your help. It's when they say:

"Wait, that's it? I thought it would be harder."

That's when you know you've taught without priesthood - when the mystery dissolves and only capability remains.

## Final Thought

Every time you're tempted to just "fix it real quick," remember: maintaining their dependency maintains hierarchy. Your revolutionary duty is to transfer knowledge so completely that they forget they ever needed you.

The revolution doesn't need more tech priests. It needs more teachers who make themselves unnecessary.

---

*"Teach a comrade to fish, and you feed them for a day. Teach a comrade to learn fishing from documentation, and you've broken the role of master forever."*