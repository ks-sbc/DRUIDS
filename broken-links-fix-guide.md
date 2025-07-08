# Broken Links Fix Guide

## Overview

This guide provides a comprehensive mapping of all broken links in the DRUIDS documentation and their correct replacements.

- **Total Broken Links**: 177
- **Unique Broken Files**: 46
- **Files Needing Fixes**: 39
- **Deleted Files**: 7

## Quick Fix Commands

Use these commands to systematically fix broken links:

### 1. Git-Related Files

```bash
# Fix git-isnt-programming.md references
sed -i 's|git-isnt-programming\.md|../../learn/git-basics/git-isnt-programming.md|g' docs/implement/git/*.md
sed -i 's|git-isnt-programming\.md|../git-basics/git-isnt-programming.md|g' docs/learn/druids-fundamentals/*.md
sed -i 's|git-isnt-programming\.md|../learn/git-basics/git-isnt-programming.md|g' docs/reference/*.md docs/teach/*.md

# Fix git-in-7-commands.md references
sed -i 's|git-in-7-commands\.md|../../learn/git-basics/git-in-7-commands.md|g' docs/implement/git/*.md
sed -i 's|git-in-7-commands\.md|../git-basics/git-in-7-commands.md|g' docs/learn/core-concepts/*.md
sed -i 's|git-in-7-commands\.md|../learn/git-basics/git-in-7-commands.md|g' docs/start/*.md docs/reference/*.md docs/teach/*.md

# Fix your-first-revolutionary-commit.md references
sed -i 's|your-first-revolutionary-commit\.md|../../learn/tutorials/your-first-revolutionary-commit.md|g' docs/implement/git/*.md
sed -i 's|your-first-revolutionary-commit\.md|../tutorials/your-first-revolutionary-commit.md|g' docs/learn/core-concepts/*.md docs/learn/druids-fundamentals/*.md docs/learn/git-basics/*.md
```

### 2. Core Concepts Files

```bash
# Fix democratic-centralism.md references
sed -i 's|democratic-centralism\.md|../../learn/core-concepts/democratic-centralism.md|g' docs/implement/workflows/*.md
sed -i 's|democratic-centralism\.md|../core-concepts/democratic-centralism.md|g' docs/learn/druids-fundamentals/*.md docs/learn/git-basics/*.md
sed -i 's|democratic-centralism\.md|../learn/core-concepts/democratic-centralism.md|g' docs/start/*.md

# Fix druids-security-implementation.md references
sed -i 's|druids-security-implementation\.md|../../learn/core-concepts/druids-security-implementation.md|g' docs/implement/workflows/*.md
sed -i 's|druids-security-implementation\.md|../core-concepts/druids-security-implementation.md|g' docs/learn/druids-fundamentals/*.md
sed -i 's|druids-security-implementation\.md|../learn/core-concepts/druids-security-implementation.md|g' docs/reference/*.md docs/start/*.md

# Fix institutional-memory.md references
sed -i 's|institutional-memory\.md|../core-concepts/institutional-memory.md|g' docs/learn/druids-fundamentals/*.md
sed -i 's|institutional-memory\.md|../learn/core-concepts/institutional-memory.md|g' docs/reference/*.md docs/start/*.md
```

## Detailed Mapping by File

### Files in `implement/git/`

#### git-command-reference-card.md
- `git-isnt-programming.md` → `../../learn/git-basics/git-isnt-programming.md`
- `git-in-7-commands.md` → `../../learn/git-basics/git-in-7-commands.md`
- `visual-git-workflows.md` → `../../learn/git-basics/visual-git-workflows.md`
- `your-first-revolutionary-commit.md` → `../../learn/tutorials/your-first-revolutionary-commit.md`
- `git-through-campaign-template.md` → `../../teach/workshops/git-through-campaign-template.md`

#### git-quick-reference.md
- Same mappings as git-command-reference-card.md

### Files in `learn/core-concepts/`

#### institutional-memory.md
- `quick-demo.md` → `../../start/quick-demo.md`
- `your-first-revolutionary-commit.md` → `../tutorials/your-first-revolutionary-commit.md`
- `git-in-7-commands.md` → `../git-basics/git-in-7-commands.md`
- `from-google-docs.md` → `../../implement/getting-started/migration-guides/from-google-docs.md`
- `from-discord.md` → `../../implement/getting-started/migration-guides/from-discord.md`

#### democratic-centralism.md
- `proposal-process.md` → `../../implement/workflows/proposal-process.md`

#### three-tier-system.md
- `security-protocols.md` → `../../implement/security/security-playbook.md`
- `help-committed-sensitive-data.md` → `../../implement/security/help-committed-sensitive-data.md`

### Files in `learn/druids-fundamentals/`

#### philosophy.md
- `quick-demo.md` → `../../start/quick-demo.md`
- `why-druids.md` → `../../start/why-druids.md`
- `git-isnt-programming.md` → `../git-basics/git-isnt-programming.md`
- `git-through-campaign.md` → `../git-basics/git-through-campaign.md`
- `druids-security-implementation.md` → `../core-concepts/druids-security-implementation.md`
- `teach-tech-without-priest-hood.md` → `../../teach/teach-tech-without-priest-hood.md`
- `institutional-memory.md` → `../core-concepts/institutional-memory.md`
- `your-first-revolutionary-commit.md` → `../tutorials/your-first-revolutionary-commit.md`
- `glossary.md` → `../../reference/glossary.md`

#### druids-red-lines.md
- `teach-tech-without-priest-hood.md` → `../../teach/teach-tech-without-priest-hood.md`
- `druids-security-implementation.md` → `../core-concepts/druids-security-implementation.md`
- `revolutionary-style-guide.md` → `revolutionary-commit-conventions.md`

### Files in `start/`

#### index.md
- `institutional-memory.md` → `../learn/core-concepts/institutional-memory.md`
- `tech-democratization-as-class-struggle.md` → `../learn/core-concepts/power-steering-metaphor.md`
- `druids-installation-guide.md` → `../implement/getting-started/druids-installation-guide.md`
- `visual-roadmaps.md` → `../learn/visual-roadmaps.md`
- `git-through-campaign-template.md` → `../teach/workshops/git-through-campaign-template.md`
- `from-google-docs.md` → `../implement/getting-started/migration-guides/from-google-docs.md`
- `from-discord.md` → `../implement/getting-started/migration-guides/from-discord.md`

#### onboarding-yourself-in-3-days.md
Multiple fixes needed - see full mapping in JSON file.

#### why-druids.md
- `visual-roadmaps.md` → `../learn/visual-roadmaps.md`
- `institutional-memory.md` → `../learn/core-concepts/institutional-memory.md`
- `druids-installation-guide.md` → `../implement/getting-started/druids-installation-guide.md`

### Files in `teach/`

#### index.md
- `git-through-campaign-template.md` → `workshops/git-through-campaign-template.md`
- `visual-roadmaps.md` → `../learn/visual-roadmaps.md`
- `revolutionary-style-guide.md` → `../learn/druids-fundamentals/revolutionary-commit-conventions.md`
- `git-isnt-programming.md` → `../learn/git-basics/git-isnt-programming.md`
- `git-in-7-commands.md` → `../learn/git-basics/git-in-7-commands.md`
- `from-google-docs.md` → `../implement/getting-started/migration-guides/from-google-docs.md`
- `why-druids.md` → `../start/why-druids.md`

## Deleted Files and Alternatives

These files no longer exist and should be replaced with alternatives:

1. **tech-democratization-as-class-struggle.md** → `learn/core-concepts/power-steering-metaphor.md`
2. **revolutionary-style-guide.md** → `learn/druids-fundamentals/revolutionary-commit-conventions.md`
3. **getting-started.md** → `start/quick-demo.md`
4. **project-management-guide.md** → `implement/workflows/proposal-process.md`
5. **why-rebase-warps-reality.md** → `learn/git-basics/daily-git-workflows.md#avoiding-rebase`
6. **qm-troubleshooting.md** → `implement/troubleshooting/index.md`
7. **obsidian.md** → Use `#obsidian-setup` anchor in the same file or link to `implement/obsidian-setup/complete-setup-guide.md`

## Special Cases

### Absolute Links in git-learning-path.md
Convert all absolute paths starting with `/` to relative paths:
- `/explanation/` → `explanations/`
- `/reference/` → `../reference/`
- `/tutorials/` → `tutorials/`
- `/how-to/` → `../implement/`

### Directory References
Add `index.md` to directory-only references:
- `./core-concepts/` → `./core-concepts/index.md`
- `./git-basics/` → `./git-basics/index.md`
- `./druids-fundamentals/` → `./druids-fundamentals/index.md`
- `../implement/` → `../implement/index.md`

## Validation

After fixing links, run:
```bash
mkdocs build --strict 2>&1 | grep "WARNING.*contains a link"
```

This should show significantly fewer warnings.