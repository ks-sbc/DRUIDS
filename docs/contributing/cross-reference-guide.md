---
title: "Cross-Reference Guide for Revolutionary Documentation"
description: "How to create meaningful connections between documents that support the user journey"
created: 2025-07-05
updated: 2025-07-05
type: "docs/how-to"
security: "L0"
version: "1.0.0"
document_id: "HOWTO-CROSSREF-2025-187-L0"
tags: ["documentation", "cross-references", "user-journey", "navigation", "collective-knowledge"]
draft: false
author: ["KSBC Tech Committee"]
navigation_order: 4
---

# Cross-Reference Guide for Revolutionary Documentation

## Material Problem This Solves

Organizers waste precious time hunting through disconnected documents. Without clear connections between theory and practice, comrades:
- Struggle to find the "how" after understanding the "why"
- Miss crucial prerequisites before attempting complex tasks
- Can't see how different pieces fit into their organizing journey
- Duplicate work because they can't find related efforts

This guide ensures every document connects meaningfully to the collective knowledge base.

## Political Framing

Knowledge hoarding is a tool of oppression. By creating clear pathways between documents, we:
- **Democratize access** to technical knowledge
- **Build collective intelligence** rather than individual expertise
- **Connect theory to practice** - the essence of praxis
- **Reduce barriers** for new organizers joining the struggle

## Cross-Reference Patterns

### 1. Journey Progression Links

These links move comrades forward in their DRUIDS journey:

```markdown
<!-- After explaining a concept -->
**Ready to put this into practice?** See [Installation Guide](../implement/getting-started/druids-installation-guide.md)

<!-- After a tutorial -->
**Understand the theory behind this?** Explore [Institutional Memory](../learn/core-concepts/institutional-memory.md)

<!-- After implementation -->
**Ready to teach others?** Check out [Teaching Without Hierarchy](../teach/teach-tech-without-priest-hood.md)
```

**[EXPAND HERE: Add more journey progression examples from your organizing context]**

### 2. Material Prerequisites

Help comrades build necessary capacity before attempting tasks:

```markdown
<!-- At document start -->
> **Prerequisites**: Before diving in, make sure you understand:
> - [Git in 7 Commands](../learn/git-basics/git-in-7-commands.md) - Basic Git literacy
> - [DRUIDS Security Implementation](../learn/core-concepts/druids-security-implementation.md) - Our security philosophy

<!-- Inline prerequisites -->
This workflow assumes you've completed [Your First Revolutionary Commit](../learn/tutorials/your-first-revolutionary-commit.md).
```

**[EXPAND HERE: Create prerequisite chains for your specific workflows]**

### 3. Theory-to-Practice Connections

Every theoretical concept should link to its practical application:

```markdown
<!-- In theory documents -->
## Applying This Principle
See how democratic centralism works in practice:
- [Git Workflow Guide](../implement/workflows/git-workflow-guide.md) - Branches as working groups
- [Proposal Process](../implement/workflows/proposal-process.md) - PRs as democratic proposals

<!-- In practical guides -->
## Revolutionary Theory Behind This
This practice embodies:
- [Democratic Centralism](../learn/core-concepts/democratic-centralism.md) - Unity in action
- [Tech Democratization](../learn/core-concepts/tech-democratization-as-class-struggle.md) - Breaking knowledge hierarchies
```

**[EXPAND HERE: Map your organization's principles to concrete practices]**

### 4. Problem-Solution Mappings

Connect pain points to their solutions:

```markdown
<!-- In problem descriptions -->
### Experiencing This Issue?
- **Lost knowledge when comrades leave?** → [Institutional Memory](../learn/core-concepts/institutional-memory.md)
- **Burnout from repeated onboarding?** → [Onboarding Without Burnout](../learn/tutorials/onboarding-without-burnout.md)
- **Security concerns about surveillance?** → [Security Playbook](../implement/security/security-playbook.md)
```

**[EXPAND HERE: Add your organization's specific challenges and solutions]**

### 5. Alternative Paths

Recognize different organizing contexts need different approaches:

```markdown
## Choose Your Path
Depending on your organizing context:

**For Labor Organizing:**
- Focus on [Meeting Workflows](../implement/workflows/meeting-workflow-guide.md)
- Prioritize [Security Audits](../implement/security/security-audits-for-organizers.md)

**For Tenant Unions:**
- Start with [Migration from Google](../implement/getting-started/migration-guides/from-google-docs.md)
- Emphasize <!-- [Pseudonym Discipline](../../implement/security/security-playbook.md) - Content to be created -->

**For Community Groups:**
- Begin with [Quick Demo](../start/quick-demo.md)
- Build towards [Proposal Process](../implement/workflows/proposal-process.md)
```

**[EXPAND HERE: Add paths specific to your movement's sectors]**

## Anti-Patterns to Avoid

### ❌ Academic Language
```markdown
<!-- Wrong -->
See also: Related theoretical frameworks in appendix B

<!-- Right -->
Put this into practice with: [Git Through Campaign](../teach/workshops/git-through-campaign.md)
```

### ❌ Circular References
```markdown
<!-- Wrong -->
For security, see Security Guide. (Security Guide: For basics, see this document)

<!-- Right -->
Build security knowledge progressively:
1. Start: [Why Security Matters](link1)
2. Learn: [Security Principles](link2)
3. Implement: [Security Playbook](link3)
```

### ❌ Dead-End Documents
Every document should link somewhere - no organizer left behind!

**[EXPAND HERE: Add anti-patterns you've observed in your organizing]**

## Implementation Checklist

When adding cross-references to any document:

- [ ] **Entry Point**: How do comrades arrive here? Link back to their likely source
- [ ] **Prerequisites**: What capacity must they have built? Link to foundations
- [ ] **Next Steps**: Where do they go after this? Link forward in journey
- [ ] **Alternatives**: What if this doesn't fit their context? Link to options
- [ ] **Problems Solved**: What organizing challenges does this address? Link to solutions
- [ ] **Theory Connection**: How does this embody our principles? Link to concepts

## Cross-Reference Phrases That Work

Replace corporate/academic language with revolutionary framing:

| ❌ Avoid | ✅ Use Instead |
|----------|----------------|
| "See also" | "Apply this in practice with..." |
| "Related documents" | "Build on this knowledge with..." |
| "For more information" | "Deepen your understanding through..." |
| "Refer to" | "Put this to work in..." |
| "As described in" | "Learn the foundation in..." |

**[EXPAND HERE: Add phrases that resonate with your organizing culture]**

## Maintaining the Web

Cross-references are living connections that need tending:

1. **Regular Audits**: Check links monthly during documentation sprints
2. **Journey Testing**: Have new comrades follow reference paths
3. **Feedback Loops**: Track which links comrades actually use
4. **Continuous Improvement**: Update based on organizing needs

## Remember

Every cross-reference is a bridge between isolation and collective power. Make them:
- **Clear**: Comrades know exactly what they'll find
- **Purposeful**: Each link serves the journey
- **Accessible**: Language that includes, not excludes
- **Revolutionary**: Reinforcing our values with every connection

---

**Ready to see this in action?** Check out [Visual Learning Paths](../learn/visual-roadmaps.md) for how these connections create complete journeys.

**Want to contribute?** Follow our [Revolutionary Style Guide](../contributing/revolutionary-style-guide.md) to maintain consistency.