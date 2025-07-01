---
title: Tags
description: Browse content by tags and topics
icon: material/tag-multiple
hide:
  - navigation
---

# 🏷️ Browse by Tags

Explore our content organized by topics and tags. Click on any tag to see related content.

## 📚 Content Categories

### Getting Started

<div class="tag-group">
  <a href="#getting-started" class="tag-link primary">getting-started</a>
  <a href="#tutorial" class="tag-link primary">tutorial</a>
  <a href="#guide" class="tag-link primary">guide</a>
  <a href="#configuration" class="tag-link">configuration</a>
</div>

### Documentation Types

<div class="tag-group">
  <a href="#reference" class="tag-link secondary">reference</a>
  <a href="#api" class="tag-link secondary">api</a>
  <a href="#best-practices" class="tag-link">best-practices</a>
  <a href="#troubleshooting" class="tag-link">troubleshooting</a>
</div>

### Features & Functionality

<div class="tag-group">
  <a href="#customization" class="tag-link accent">customization</a>
  <a href="#theming" class="tag-link accent">theming</a>
  <a href="#navigation" class="tag-link accent">navigation</a>
  <a href="#search" class="tag-link accent">search</a>
  <a href="#blog" class="tag-link accent">blog</a>
  <a href="#comments" class="tag-link accent">comments</a>
</div>

### Technical Topics

<div class="tag-group">
  <a href="#performance" class="tag-link warning">performance</a>
  <a href="#accessibility" class="tag-link warning">accessibility</a>
  <a href="#mobile" class="tag-link warning">mobile</a>
  <a href="#responsive" class="tag-link warning">responsive</a>
  <a href="#seo" class="tag-link warning">seo</a>
</div>

### Development & Deployment

<div class="tag-group">
  <a href="#deployment" class="tag-link info">deployment</a>
  <a href="#ci-cd" class="tag-link info">ci-cd</a>
  <a href="#github" class="tag-link info">github</a>
  <a href="#versioning" class="tag-link info">versioning</a>
  <a href="#migration" class="tag-link info">migration</a>
</div>

### Privacy & Analytics

<div class="tag-group">
  <a href="#analytics" class="tag-link success">analytics</a>
  <a href="#privacy" class="tag-link success">privacy</a>
  <a href="#social" class="tag-link success">social</a>
</div>

### Community & Contribution

<div class="tag-group">
  <a href="#community" class="tag-link purple">community</a>
  <a href="#contribution" class="tag-link purple">contribution</a>
  <a href="#open-source" class="tag-link purple">open-source</a>
  <a href="#advanced" class="tag-link purple">advanced</a>
</div>

## 🔍 Tag Search

Use the search box above to quickly find content, or browse by the tags below.

## 📊 Popular Tags

The most frequently used tags in our documentation:

<div class="popular-tags">
  <a href="#getting-started" class="popular-tag size-large">getting-started</a>
  <a href="#tutorial" class="popular-tag size-large">tutorial</a>
  <a href="#customization" class="popular-tag size-medium">customization</a>
  <a href="#navigation" class="popular-tag size-medium">navigation</a>
  <a href="#configuration" class="popular-tag size-medium">configuration</a>
  <a href="#blog" class="popular-tag size-small">blog</a>
  <a href="#performance" class="popular-tag size-small">performance</a>
  <a href="#accessibility" class="popular-tag size-small">accessibility</a>
  <a href="#deployment" class="popular-tag size-small">deployment</a>
  <a href="#privacy" class="popular-tag size-small">privacy</a>
</div>

## 📖 How to Use Tags

Tags help you discover related content across our documentation:

- **Click any tag** to see all content with that tag
- **Combine searches** with multiple tags to narrow results
- **Follow tag feeds** to stay updated on specific topics
- **Suggest new tags** if you think we're missing important categories

## 🎯 Tag Guidelines

When contributing content, please use these tag guidelines:

### Primary Tags (Required)

- **Content type**: `tutorial`, `guide`, `reference`, `api`
- **Difficulty level**: `getting-started`, `intermediate`, `advanced`
- **Main topic**: `customization`, `navigation`, `deployment`, etc.

### Secondary Tags (Optional)

- **Technology**: `github`, `ci-cd`, `mobile`, `responsive`
- **Purpose**: `performance`, `accessibility`, `seo`, `privacy`
- **Audience**: `community`, `contribution`, `troubleshooting`

### Tag Naming Conventions

- Use **lowercase** with hyphens: `getting-started`, `best-practices`
- Be **specific** but not overly narrow: `navigation` not `nav-tabs`
- Use **established tags** when possible rather than creating new ones
- Keep tags **concise**: prefer `seo` over `search-engine-optimization`

---

_All tags are automatically generated from page metadata. To add tags to a page, include them in the front matter._

<style>
.tag-group {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 1rem 0 2rem 0;
}

.tag-link {
  display: inline-block;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  text-decoration: none;
  font-weight: 500;
  font-size: 0.9rem;
  transition: all 0.2s ease;
  border: 2px solid transparent;
}

.tag-link.primary {
  background: var(--md-primary-fg-color--transparent);
  color: var(--md-primary-fg-color);
  border-color: var(--md-primary-fg-color--light);
}

.tag-link.secondary {
  background: var(--md-default-fg-color--lightest);
  color: var(--md-default-fg-color);
  border-color: var(--md-default-fg-color--lighter);
}

.tag-link.accent {
  background: var(--md-accent-fg-color--transparent);
  color: var(--md-accent-fg-color);
  border-color: var(--md-accent-fg-color);
}

.tag-link.warning {
  background: #fef3c7;
  color: #d97706;
  border-color: #fbbf24;
}

.tag-link.info {
  background: #dbeafe;
  color: #2563eb;
  border-color: #60a5fa;
}

.tag-link.success {
  background: #d1fae5;
  color: #059669;
  border-color: #34d399;
}

.tag-link.purple {
  background: #ede9fe;
  color: #7c3aed;
  border-color: #a78bfa;
}

.tag-link:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.tag-link.primary:hover {
  background: var(--md-primary-fg-color);
  color: white;
}

.tag-link.accent:hover {
  background: var(--md-accent-fg-color);
  color: white;
}

.popular-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin: 2rem 0;
  justify-content: center;
}

.popular-tag {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  background: var(--md-accent-fg-color--transparent);
  color: var(--md-accent-fg-color);
  border: 2px solid var(--md-accent-fg-color);
  border-radius: 25px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
}

.popular-tag.size-large {
  font-size: 1.2rem;
  padding: 1rem 2rem;
}

.popular-tag.size-medium {
  font-size: 1rem;
  padding: 0.75rem 1.5rem;
}

.popular-tag.size-small {
  font-size: 0.9rem;
  padding: 0.5rem 1rem;
}

.popular-tag:hover {
  background: var(--md-accent-fg-color);
  color: white;
  transform: scale(1.05);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}

/* Dark theme adjustments */
[data-md-color-scheme="slate"] .tag-link.warning {
  background: #451a03;
  color: #fbbf24;
}

[data-md-color-scheme="slate"] .tag-link.info {
  background: #1e3a8a;
  color: #60a5fa;
}

[data-md-color-scheme="slate"] .tag-link.success {
  background: #064e3b;
  color: #34d399;
}

[data-md-color-scheme="slate"] .tag-link.purple {
  background: #581c87;
  color: #a78bfa;
}
</style>
