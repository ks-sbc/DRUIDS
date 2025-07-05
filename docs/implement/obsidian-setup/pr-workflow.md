---
title: "Obsidian to GitHub PR Workflow"
description: "Secure workflow for creating pull requests from Obsidian using Meta Bind buttons, templates, and GitHub Actions."
type: "how-to"
security: "L0"
document_id: "INT-HTG-2025-236-L0"
version: "1.0.0"
tags: ["obsidian", "github", "pull-requests", "workflow", "automation"]
---

# Obsidian to GitHub PR Workflow

## Overview

This document describes the secure workflow for creating pull requests starting from Obsidian and ending in GitHub, using a combination of Meta Bind buttons, templates, and GitHub Actions.

## Architecture

```mermaid
graph LR
    A[Obsidian PR Draft] -->|Meta Bind Export| B[PR Queue Folder]
    B -->|Obsidian-Git Sync| C[GitHub Repo]
    C -->|GitHub Action| D[Draft PR Created]
    D -->|Manual Review| E[PR Submitted]
```

## Security Model

### What We DON'T Do

- ❌ Direct GitHub API calls from Obsidian (credential exposure risk)
- ❌ Automatic PR creation without review (security bypass risk)
- ❌ JavaScript execution with system access (code injection risk)

### What We DO

- ✅ Use Meta Bind for safe UI interactions and data collection
- ✅ Export to monitored folder for GitHub Action processing
- ✅ Maintain security tier separation and validation
- ✅ Require manual review before final submission

## Step-by-Step Workflow

### 1. Create PR Draft in Obsidian

1. Create new note from `OBSIDIAN_PR_DRAFT.md` template
2. Fill in all metadata fields using Meta Bind inputs
3. Write PR description, changes, and testing details

### 2. Validate and Export

1. Click "Validate PR" button to check completeness
2. Review the validation results
3. Click "Export to GitHub" to create queue file

### 3. Automated Processing

The `.github/pr-queue/` folder is monitored by a GitHub Action that:

1. Detects new PR draft files
2. Validates security classifications
3. Creates a draft PR with the content
4. Adds appropriate labels and reviewers
5. Notifies the author

### 4. Manual Review and Submission

1. Author reviews the draft PR on GitHub
2. Makes any final adjustments
3. Marks PR as "Ready for Review"
4. Democratic process begins

## Meta Bind Button Configuration

### Safe Button Actions

```yaml
# Copy to Clipboard - SAFE
- type: copyToClipboard
  text: "formatted content"

# Create Note - SAFE
- type: createNote
  folderPath: ".github/pr-queue"
  
# Run Command - SAFE (if command is trusted)
- type: command
  command: "druids:validate-pr"

# Update Metadata - SAFE
- type: updateMetadata
  bindTarget: "status"
  value: "ready"
```

### Unsafe Actions to Avoid

```yaml
# Run JavaScript - RISKY
- type: runInlineJS
  code: "arbitrary code execution"

# Run JS File - RISKY  
- type: runJSFile
  file: "could access system"
```

## GitHub Action for PR Creation

```yaml
name: Process PR Queue

on:
  push:
    paths:
      - '.github/pr-queue/*.md'

jobs:
  create-pr:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Parse PR Draft
        id: parse
        run: |
          # Extract metadata and content from PR draft file
          
      - name: Validate Security
        run: |
          # Ensure security classifications are appropriate
          
      - name: Create Draft PR
        uses: peter-evans/create-pull-request@v5
        with:
          draft: true
          title: ${{ steps.parse.outputs.title }}
          body: ${{ steps.parse.outputs.body }}
          branch: ${{ steps.parse.outputs.branch }}
```

## Best Practices

### For Users

1. **Always validate** before exporting
2. **Review draft PRs** before marking ready
3. **Don't store credentials** in Obsidian
4. **Use templates** for consistency

### For Admins

1. **Monitor the pr-queue** folder
2. **Audit GitHub Actions** regularly  
3. **Restrict Meta Bind JS** execution
4. **Maintain secure templates**

## Advantages of This Approach

1. **Security**: No credentials in Obsidian, validated workflow
2. **Flexibility**: Draft in familiar environment
3. **Automation**: Reduces manual steps while maintaining control
4. **Traceability**: Clear audit trail from draft to PR
5. **Democratic**: Supports DRUIDS principles

## Future Enhancements

1. **Templater Integration**: Auto-generate PR content
2. **Dataview Queries**: Show PR status in Obsidian
3. **QuickAdd Macros**: Streamline common PR types
4. **Status Sync**: Update Obsidian when PR status changes

## Related Documentation

- [Obsidian Git Workflow Guide](../../implement/workflows/git-workflow-guide.md)
- [Merge Request Process](../../implement/obsidian-setup/merge-request-process.md)
- [Proposal Process Workflow](../../implement/workflows/proposal-process.md)
