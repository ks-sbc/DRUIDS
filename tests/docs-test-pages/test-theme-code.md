# Theme Test: Code & Syntax Highlighting

Testing code blocks, syntax highlighting, and inline code.

## Inline Code

Here's some `inline code` within a sentence. We can also use `const variable = "value"` for longer inline snippets.

## Code Blocks

### Python

```python
# Development server with hot reload
def serve():
    """Start the development server."""
    cd repos/druids-wiki
    mkdocs build
    mkdocs serve --dev-addr 127.0.0.1:8001

# Example class
class SecurityManager:
    def __init__(self, level="L0"):
        self.level = level
        self.permissions = self._get_permissions()

    def _get_permissions(self):
        return {
            "L0": ["read"],
            "L1": ["read", "write"],
            "L2": ["read", "write", "admin"]
        }.get(self.level, [])
```

### JavaScript

```javascript
// Initialize Mermaid for diagram rendering
document.addEventListener('DOMContentLoaded', function() {
    if (typeof mermaid !== 'undefined') {
        mermaid.initialize({
            startOnLoad: true,
            theme: 'dark',
            themeVariables: {
                primaryColor: '#228B22',
                primaryTextColor: '#87CEEB'
            }
        });
    }
});

// Example async function
async function fetchData(url) {
    try {
        const response = await fetch(url);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
}
```

### Bash

```bash
#!/bin/bash
# Check for issues in MkDocs build

echo "Building documentation..."
mkdocs build 2>&1 | grep -E "(WARNING|ERROR)"

# Git workflow
git add .
git commit -m "feat: update theme styling"
git push origin main

# Environment setup
export DRUIDS_ENV="development"
source venv/bin/activate
pip install -r requirements.txt
```

### YAML

```yaml
theme:
  name: material
  palette:
    scheme: slate
    primary: custom
    accent: custom
  features:
    - navigation.instant
    - navigation.tracking
    - navigation.tabs
    - navigation.sections
```

### JSON

```json
{
  "name": "druids-wiki",
  "version": "1.0.0",
  "security": {
    "levels": ["L0", "L1", "L2"],
    "defaultLevel": "L0",
    "encryption": {
      "enabled": true,
      "algorithm": "AES-256"
    }
  },
  "features": [
    "documentation",
    "versioning",
    "search"
  ]
}
```

### CSS

```css
/* Custom theme colors */
:root {
  --primary-color: #228B22;
  --accent-color: #CC143C;
  --background: #0A0E27;
  --text-color: #87CEEB;
}

.security-badge {
  display: inline-flex;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-weight: 600;
  text-transform: uppercase;
}

.security-badge.l2 {
  background: rgba(0, 0, 0, 0.2);
  border: 2px solid #000000;
  color: #000000;
}
```

### SQL

```sql
-- Create security levels table
CREATE TABLE security_levels (
    id INTEGER PRIMARY KEY,
    level VARCHAR(10) NOT NULL,
    name VARCHAR(50) NOT NULL,
    permissions TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert default levels
INSERT INTO security_levels (level, name, permissions) VALUES
    ('L0', 'Public', 'read'),
    ('L1', 'Member', 'read,write'),
    ('L2', 'Cadre', 'read,write,admin');

-- Query user permissions
SELECT u.username, s.level, s.permissions
FROM users u
JOIN security_levels s ON u.security_level_id = s.id
WHERE u.active = 1;
```
