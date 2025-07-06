# Documentation Migration Manifest

## Overview
This manifest coordinates the migration of new DRUIDS documentation structure between two repositories/instances.

**Source**: `/home/percy/Desktop/KSBC/repos/druids-wiki/` (ai-convo branch)
**Target**: `/home/percy/Documents/mkdocs/mkdocs/` (user/191 branch)

## Migration Strategy

### Phase 1: Preparation (This Instance)
1. Create this manifest with complete file inventory
2. Document any dependencies or cross-references
3. Note any files that need special handling
4. Create a migration checklist

### Phase 2: Execution (Other Instance)
1. Read this manifest
2. Copy files according to the plan
3. Update internal links as needed
4. Test the new structure
5. Update this manifest with completion status

## Files to Migrate

### New Structure Directories
All files in these directories are NEW and should be copied as-is:
- `docs/start/` (3 files)
- `docs/learn/` (14 files including subdirectories)
- `docs/implement/` (5 files)
- `docs/teach/` (2 files)
- `docs/meta/` (2 files)

### Complete File List

#### Start Section (Entry Point for New Users)
```
docs/start/index.md                 - Overview with decision tree
docs/start/why-druids.md           - Value proposition (FIXED: removed false testimonials)
docs/start/quick-demo.md           - 5-minute demonstration
```

#### Learn Section (Progressive Education)
```
docs/learn/index.md                                           - Learning path overview
docs/learn/git-learning-path.md                              - Progressive Git guide
docs/learn/core-concepts/index.md                            - Core concepts overview
docs/learn/core-concepts/institutional-memory.md             - Memory as capacity
docs/learn/core-concepts/security-as-revolutionary-practice.md - Security principles
docs/learn/core-concepts/druids-security-implementation.md   - Technical security
docs/learn/core-concepts/tech-democratization-as-class-struggle.md - Breaking tech hierarchy
docs/learn/git-basics/why-revolutionaries-need-git.md        - Git for organizing
docs/learn/git-basics/git-isnt-programming.md               - Demystifying Git
docs/learn/git-basics/git-through-campaign.md               - Campaign-based learning
docs/learn/git-basics/git-in-7-commands.md                  - Essential commands
docs/learn/git-basics/daily-git-workflows.md                - Daily practice
docs/learn/druids-fundamentals/revolutionary-commit-conventions.md - Commit format
```

#### Implement Section (Practical Deployment)
```
docs/implement/index.md                                      - Implementation overview
docs/implement/getting-started/druids-installation-guide.md  - Installation
docs/implement/advanced/custom-tails-image-technical-guide.md - Tails customization
docs/implement/advanced/druids-tails-deployment.md          - Tails deployment
docs/implement/advanced/druids-tails-bootstrap-scripts.md    - Bootstrap scripts
```

#### Teach Section (Knowledge Transfer)
```
docs/teach/index.md                        - Teaching overview
docs/teach/teach-tech-without-priest-hood.md - Democratizing knowledge
```

#### Meta Section (Theory/Reference)
```
docs/meta/philosophy.md - Theoretical foundation
docs/meta/glossary.md   - Terms for organizers
```

### Modified Files
These files were modified and contain important navigation updates:

1. **mkdocs.yml** - CRITICAL: Contains complete new navigation structure
   - Lines 97-210 contain the new nav structure
   - Must be carefully merged with existing config

2. **docs/index.md** - Updated homepage to reference new structure

### Moved Files (Already Handled)
These renames are already tracked in git:
```
docs/guides/migration/escaping-google-surveillance.md → docs/implement/getting-started/migration-guides/from-google-docs.md
docs/how-to/breaking-discord-chains.md → docs/implement/getting-started/migration-guides/from-discord.md
docs/reference/git-quick-reference.md → docs/reference/commands/git-commands.md
```

## Special Considerations

### 1. Cross-References
Many documents reference each other. Common patterns:
- `See [Institutional Memory](../core-concepts/institutional-memory.md)`
- `Learn more in [Git Through Campaign](../git-basics/git-through-campaign.md)`

These may need updating based on final directory structure.

### 2. Frontmatter Standards
All new documents use consistent frontmatter:
```yaml
---
title: "Title"
description: "Description"
created: 2025-07-04
updated: 2025-07-04
type: "docs/[tutorial|how-to|reference|explanation]"
security: "L0"
version: "1.0.0"
document_id: "[TYPE]-[NAME]-YYYY-DDD-L[LEVEL]"
tags: [...]
draft: false
author: ["KSBC Tech Committee"]
navigation_order: N
---
```

### 3. Navigation Philosophy
The new structure abandons Diátaxis physical directories in favor of user journey:
- Start → Learn → Implement → Teach
- Diátaxis types are now metadata, not directories
- This matches how people actually discover and use documentation

### 4. Files NOT to Migrate
These are work-in-progress or AI-specific:
- Anything in `ai-discourses/` (except docs/ subdirectory if needed)
- Test pages in `tests/docs-test-pages/`

## Migration Checklist

For the other Claude instance:

- [ ] Read this manifest completely
- [ ] Check target directory is on correct branch (user/191)
- [ ] Create directories: start/, learn/, implement/, teach/, meta/
- [ ] Copy all files listed above
- [ ] Merge mkdocs.yml navigation changes carefully
- [ ] Update docs/index.md
- [ ] Run `mkdocs serve` to test
- [ ] Check for broken links
- [ ] Update this manifest with any issues found

## Coordination Notes

- This instance is on branch: ai-convo
- Other instance should be on: user/191
- Use `/tmp/druids-wiki/migration-status.json` for status updates if needed

## Status

- **Prepared by**: Claude (ai-convo branch)
- **Date**: 2025-07-05
- **Ready for migration**: YES
- **Migration completed**: [ ] (update when done)

---

*This is a living document. Update as migration progresses.*