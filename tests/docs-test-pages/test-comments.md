---
comments: true
---

# Test Page for Giscus Comments

This page is for testing the Giscus comment integration with the DRUIDS wiki.

## Overview

This test page demonstrates:

1. **Giscus Integration**: Comments powered by GitHub Discussions
2. **Mandalorian Theme**: Custom CSS matching our tactical aesthetic
3. **Theme Synchronization**: Comments adapt to light/dark mode
4. **Security**: Origin restrictions via giscus.json

## How to Test

1. Make sure you have comments enabled in the frontmatter:

   ```yaml
   ---
   comments: true
   ---
   ```

2. Run the local MkDocs server:

   ```bash
   mkdocs serve
   ```

3. Navigate to this page at `http://localhost:8000/test-comments/`

4. You should see:
   - A comments section at the bottom
   - Mandalorian-themed styling
   - Ability to post comments (requires GitHub login)

## Security Features

The Giscus integration includes:

- **Origin Restrictions**: Only allowed domains can embed comments
- **No Tracking**: Giscus is privacy-respecting
- **GitHub Authentication**: Leverages GitHub's security
- **Moderation Tools**: Through GitHub Discussions

## Styling

The comments use our custom Mandalorian theme with:

- Deep space black background (#0A0E27)
- Beskar steel gray accents (#7F8C8D)
- Mandalorian red highlights (#C0392B)
- Terminal green for code (#00FF41)

---

_This is the way._
