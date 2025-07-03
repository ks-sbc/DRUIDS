#!/usr/bin/env python3
"""
Pytest configuration and shared fixtures for MkDocs tests
"""

import shutil
import tempfile
from pathlib import Path

import pytest
import yaml
from mkdocs.config import load_config


@pytest.fixture(scope="session")
def project_root():
    """Get the project root directory"""
    return Path(__file__).parent.parent


@pytest.fixture(scope="session")
def mkdocs_config_path(project_root):
    """Path to mkdocs.yml"""
    return project_root / "mkdocs.yml"


@pytest.fixture(scope="session")
def mkdocs_config(mkdocs_config_path):
    """Load MkDocs configuration"""
    if not mkdocs_config_path.exists():
        pytest.skip("mkdocs.yml not found")
    return load_config(str(mkdocs_config_path))


@pytest.fixture(scope="session")
def docs_dir(mkdocs_config):
    """Get the docs directory from config"""
    return Path(mkdocs_config["docs_dir"])


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing"""
    temp_dir = tempfile.mkdtemp()
    yield Path(temp_dir)
    shutil.rmtree(temp_dir)


@pytest.fixture
def sample_markdown_content():
    """Sample markdown content for testing"""
    return {
        "valid": """---
title: Test Document
date: 2024-01-01
---

# Test Document

This is a valid markdown document.

## Section 1

Content with [internal link](../other-page) and [external link](https://example.com).

```python
def hello():
    print("Hello, world!")
```
""",
        "no_frontmatter": """# Test Document

This document has no frontmatter.
""",
        "invalid_frontmatter": """---
title: Test Document
invalid_yaml: [unclosed
---

# Test Document
""",
        "broken_links": """---
title: Test Document
---

# Test Document

This has a [broken link](./nonexistent.md) and [another broken](../missing/file.md).
""",
    }


@pytest.fixture
def create_test_file(temp_dir):
    """Factory fixture to create test files"""

    def _create_file(filename, content):
        file_path = temp_dir / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content)
        return file_path

    return _create_file


def pytest_configure(config):
    """Configure pytest with custom markers"""
    config.addinivalue_line("markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')")
    config.addinivalue_line("markers", "integration: marks tests as integration tests")
    config.addinivalue_line("markers", "unit: marks tests as unit tests")