---
title: "Reference Documentation"
description: "Quick reference materials, commands, templates, and technical specifications for DRUIDS"
created: 2025-07-05
updated: 2025-07-05
type: "docs/reference"
security: "L0"
version: "1.0.0"
document_id: "REF-IDX-2025-001-L0"
tags: ["reference", "documentation", "commands", "templates", "quick-guide"]
draft: false
author: ["KSBC Tech Committee"]
navigation_order: 1
---

# Reference Documentation

*Quick access to commands, templates, and technical specifications*

## Quick Navigation

### Commands & Tools
- **[[git-quick-reference|Git Quick Reference]]** - Essential Git commands for revolutionaries
- **[[../learn/git-basics/git-command-reference-card|Git Command Reference Card]]** - Printable reference card
- **[[../learn/git-basics/visual-git-workflows|Visual Git Workflows]]** - Flowcharts and diagrams

### Templates
- **[[../_templates/meeting-minutes-template|Meeting Minutes Template]]** - Standard format for documenting meetings
- **[[../_templates/proposal-template|Proposal Template]]** - Tactical-operational-strategic proposal framework
- **[[../_templates/security-incident-template|Security Incident Template]]** - Crisis response documentation

### Testing & Validation
- **[[testing/test-suite-reference|Test Suite Reference]]** - Comprehensive testing documentation
- **[[../how-to/test-suite-usage|Test Suite Usage Guide]]** - How to run and interpret tests

## By Category

### Git & Version Control
Essential commands and workflows for Git-based organizing:

#### Basic Operations
```bash
git clone [url]              # Get repository
git pull                     # Get updates  
git add [file]               # Stage changes
git commit -m "message"      # Save changes
git push                     # Share changes
git status                   # Check state
```

#### Collaboration
```bash
git branch [name]            # Create branch
git checkout [branch]        # Switch branch
git merge [branch]           # Combine work
git log --oneline            # View history
```

#### Emergency Commands
```bash
git reset --hard HEAD        # Discard all changes
git reflog                   # Recovery history
git clean -fd                # Remove untracked files
```

### Security & Privacy
Key practices for revolutionary organizing:

#### Information Classification
- **L0 (Public)**: General education, public campaigns
- **L1 (Members)**: Internal strategy, member information  
- **L2 (Cadre)**: Sensitive operations, security planning

#### Basic Security Commands
```bash
# Check file permissions
ls -la

# Secure file deletion
shred -vfz -n 3 [file]

# Check git commits for sensitive data
git log --all --grep="password\|secret\|key"
```

### Documentation Standards

#### File Naming Conventions
```
YYYY-MM-DD-meeting-type.md      # Meeting minutes
proposal-YYYY-NN-title.md       # Proposals
guide-topic-name.md             # How-to guides
ref-topic-abbreviation.md       # Reference docs
```

#### Document Metadata
All documents should include:
- Title and description
- Creation and update dates
- Security classification (L0/L1/L2)
- Document ID for tracking
- Relevant tags

#### Commit Message Format
```
TYPE[scope](vote): Description

- Specific change 1
- Specific change 2

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

### Project Management

#### Task States
- **backlog**: Identified but not scheduled
- **todo**: Ready to begin
- **in-progress**: Currently being worked on
- **completed**: Finished successfully

#### Priority Levels
- **critical**: Urgent organizational need
- **high**: Important for current campaigns
- **medium**: Valuable but not time-sensitive
- **low**: Nice to have, future consideration

### MkDocs Configuration

#### Key Settings
```yaml
theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - search.highlight
    
plugins:
  - pub-obsidian
  - search
  - git-revision-date-localized
```

#### Navigation Structure
```yaml
nav:
  - Home: index.md
  - Start: start/
  - Learn: learn/
  - Implement: implement/
  - Teach: teach/
  - Reference: reference/
```

## Quick Start Guides

### New Member Checklist
1. **Read**: [[../start/why-druids|Why DRUIDS?]]
2. **Setup**: [[../implement/getting-started/druids-installation-guide|Installation Guide]]
3. **Learn**: [[../learn/git-basics/git-in-7-commands|Git in 7 Commands]]
4. **Practice**: [[../learn/tutorials/your-first-revolutionary-commit|Your First Commit]]
5. **Contribute**: [[../contributing/revolutionary-style-guide|Style Guide]]

### Emergency Procedures
1. **Security Incident**: Use [[../_templates/security-incident-template|Security Template]]
2. **Git Problems**: Check [[git-quick-reference|Git Reference]]
3. **Site Down**: Follow [[../learn/mkdocs/website-validations|Validation Guide]]
4. **Lost Work**: Use `git reflog` for recovery

### Common Tasks
- **Document a meeting**: Copy [[../_templates/meeting-minutes-template|meeting template]]
- **Make a proposal**: Use [[../_templates/proposal-template|proposal template]]
- **Fix broken links**: Run test suite per [[testing/test-suite-reference|test reference]]
- **Update documentation**: Follow [[../contributing/revolutionary-style-guide|style guide]]

## Technical Specifications

### Supported Formats
- **Markdown**: All content files (.md)
- **YAML**: Configuration and frontmatter
- **JSON**: Data files and configuration
- **CSS/JS**: Theme customization

### File Structure
```
docs/
├── index.md                    # Main page
├── start/                      # Getting started
├── learn/                      # Educational content
├── implement/                  # Installation & setup
├── teach/                      # Training materials
├── reference/                  # This section
├── contributing/               # Contribution guides
└── _templates/                 # Document templates
```

### Build Requirements
- **MkDocs**: Documentation generator
- **Material Theme**: UI framework
- **pub-obsidian plugin**: WikiLinks and backlinks
- **Git**: Version control and revision dates

## Troubleshooting

### Common Issues

**Q: "Page not found" errors**
A: Check navigation in `mkdocs.yml`, ensure file exists

**Q: "WikiLinks not working"**  
A: Verify pub-obsidian plugin is enabled and configured

**Q: "Build failing"**
A: Run `mkdocs build --strict` to see specific errors

**Q: "Links broken after reorganization"**
A: Run link validation tests from [[testing/test-suite-reference|test suite]]

### Getting Help
1. **Check this reference** for quick answers
2. **Search documentation** using site search
3. **Review recent commits** with `git log --oneline`
4. **Ask in tech channel** with specific error messages
5. **Create issue** with reproduction steps

## Contributing to Reference

### Adding New Reference Material
1. Follow [[../contributing/revolutionary-style-guide|style guide]]
2. Use appropriate document templates
3. Include all required frontmatter
4. Test with `mkdocs build --strict`
5. Submit via pull request

### Updating Existing References
1. Check current accuracy
2. Maintain backward compatibility
3. Update modification date
4. Test all examples
5. Document breaking changes

---

**Remember**: Reference documentation should be **accurate**, **concise**, and **immediately useful**. When in doubt, link to more detailed explanations elsewhere.