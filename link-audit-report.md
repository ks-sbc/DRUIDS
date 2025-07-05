# Link Audit Report

Generated on: 2025-07-05

## Summary

Total broken links identified: 72
- Missing target files: 68
- Incorrect anchor links: 2
- Unrecognized relative links: 2

## Broken Links by Category

### 1. Missing Visual Roadmaps
**File:** `learn/visual-roadmaps.md`
- Referenced in: multiple files
- Status: File does not exist

### 2. Missing Git Basics
The following git basics files are missing:
- `learn/git-basics/git-in-7-commands.md`
- `learn/git-basics/git-isnt-programming.md`

### 3. Missing Glossary
**File:** `glossary.md`
- Referenced in: multiple files across the documentation
- Status: File does not exist

### 4. Missing Tutorial Files
- `tutorials/first-week-with-druids.md`
- `tutorials/branching-basics.md`

### 5. Missing How-To Guides
- `how-to/daily-workflows.md`
- `how-to/breaking-discord-chains.md`
- `how-to/pseudonym-discipline.md`

### 6. Missing Reference Documentation
- `reference/security-protocols.md`
- `reference/design/theme-development-guide.md`
- `reference/design/qm-accessibility.md`
- `reference/design/qm-implementation-guide.md`
- `reference/design/qm-troubleshooting.md`
- `reference/troubleshooting.md`

### 7. Missing Explanation Documents
- `explanation/why-discord-democracy-fails.md`

### 8. Missing Community/Support Pages
- `community/support.md`

### 9. Missing Campaign and Workflow Files
- `learn/core-concepts/git-as-democratic-centralism.md`
- `learn/core-concepts/security-as-revolutionary-practice.md`
- `learn/core-concepts/three-tier-system.md`
- `learn/getting-started/setting-up-git.md`
- `implement/workflows/campaign-management.md`
- `teach/running-git-workshop.md`

### 10. Missing MkDocs Documentation
- `learn/mkdocs/features-demo.md`
- `learn/mkdocs/customization-guide.md`

## Files with Most Broken Links

1. **implement/getting-started/druids-installation-guide.md** - 10 broken links
2. **teach/index.md** - 8 broken links
3. **start/onboarding-yourself-in-3-days.md** - 11 broken links
4. **learn/index.md** - Multiple broken links

## Recommended Actions

### Priority 1: Create Missing Core Files
1. Create `glossary.md` - Referenced everywhere
2. Create `learn/visual-roadmaps.md` - Key navigation file
3. Create git basics files in `learn/git-basics/`

### Priority 2: Fix Navigation Structure
1. Update all index files to remove broken links
2. Create placeholder files for missing content
3. Update navigation paths in mkdocs.yml

### Priority 3: Content Migration
1. Check if content exists elsewhere and needs moving
2. Update links to point to correct locations
3. Remove references to non-existent files

## Link Patterns to Fix

### Incorrect Path Patterns
- Links starting with `/guides/` should likely be `/how-to/`
- Links to `/tutorials/` might need to be `/learn/tutorials/`
- Some links use absolute paths that should be relative

### Anchor Links
- `#step-1-inventory-your-digital-prisonmd` - Malformed anchor
- `#weekly-progress-path` - Missing section
- `#bootcamp-path` - Missing section

## Next Steps

1. Run the fix_wiki_links.py script again to catch any remaining wiki-style links
2. Create a script to automatically fix common link patterns
3. Generate stub files for missing content
4. Update navigation configuration in mkdocs.yml
5. Re-run build to verify fixes

## Notes

- Many of these files may have been intentionally removed or renamed
- Some links may be pointing to future content not yet created
- The project appears to be in active reorganization