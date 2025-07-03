# DRUIDS Wiki Documentation System

## ‼️UNDER CONSTRUCTION‼️

We're working on troubleshooting a java error among other things, it's 95% there

## Introduction

> Democratic Revolutionary Unified Information & Documentation System

A secure, privacy-respecting documentation system built with MkDocs Material, featuring a Mandalorian tactical aesthetic and GitHub Discussions-based commenting.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/ks-sbc/DRUIDS.git
cd DRUIDS

# Install dependencies
pip install -r requirements.txt

# Run development server
mkdocs build

# Build for production
mkdocs serve
```

Visit <localhost:8000> to see your documentation.

## 📋 Features

### Core Features

- **MkDocs Material Theme**: Modern, responsive documentation
- **Mandalorian Aesthetic**: Custom tactical theme with industrial design
- **Giscus Comments**: Privacy-respecting comments via GitHub Discussions
- **Three-Tier Security**: Visual indicators for L0/L1/L2 content
- **Democratic Centralist Workflow**: Git-based proposal and review system

### Technical Features

- **Full-Text Search**: Built-in search with highlighting
- **Mermaid Diagrams**: Flowcharts and diagrams from text
- **Code Highlighting**: Syntax highlighting for multiple languages
- **Dark Mode**: Automatic theme switching
- **Mobile Responsive**: Works on all devices
- **GDPR Compliant**: Privacy plugin for asset localization

## 🏗️ Project Structure

```text
druids-wiki
├── assets
│   ├── fonts
│   ├── images
│   │   ├── diagrams
│   ├── javascripts
│   ├── js
│   └── stylesheets
├── data
├── docs
├── scripts
├── templates
└── tests
```

```text
druids-wiki/docs
├── community
├── core-concepts
├── getting-started
├── guides
├── implementation
│   ├── obsidian-setup
│   └── workflows
├── operations
│   └── security
├── technical-reference
│   └── architecture
├── configuration
├── deployment
├── development
│   └── testing
├── graphic-design
│   ├── obsidian
│   ├── plugins
│   └── workflows
└── why-druids
```

## 🎨 Mandalorian Theme

The documentation uses a custom Mandalorian tactical aesthetic:

- **Deep Space Black** (#0A0E27): Background
- **Beskar Steel Gray** (#7F8C8D): Primary elements
- **Mandalorian Red** (#C0392B): Accents and highlights
- **Terminal Green** (#00FF41): Code blocks
- **Clean White** (#ECF0F1): Text

### Visual Security Indicators

Content is marked with visual security levels:

- 🟢 **L0 (Public)**: Green - Public content
- 🟠 **L1 (Member)**: Orange - Member-only content
- 🔴 **L2 (Cadre)**: Red - Restricted content

## 💬 Comments System

Comments are powered by Giscus, which uses GitHub Discussions:

- Privacy-respecting (no tracking)
- Stored in GitHub Discussions
- Themed to match the site
- Moderated through GitHub

## 🚀 Deployment

### GitHub Pages

```yaml
# .github/workflows/deploy.yml
name: Deploy to GitHub Pages
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: 3.x
      - run: pip install -r requirements.txt
      - run: mkdocs gh-deploy --force
```

### Cloudflare Pages

1. Connect GitHub repository
2. Build settings:
   - Build command: `pip install -r requirements.txt && mkdocs build`
   - Build output: `site`
   - Environment: `PYTHON_VERSION = 3.11`

## 🛠️ Development

### Prerequisites

- Python 3.8+
- pip
- Git

### Setup Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install test dependencies
pip install -r tests/requirements-test.txt

# Run tests
pytest tests/
```

## 🔒 Security

### Content Security

- All content is version controlled
- Changes require pull request review
- Automated security scanning in CI/CD
- Visual security level indicators

## 🤝 Contributing

1. Clone the repository
2. Create your feature branch
3. Make your changes
4. Add tests if applicable
5. Ensure all tests pass
6. Submit a pull request

See [CONTRIBUTING.md](docs/community/contribute.md) for detailed guidelines.

## 📄 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: <https://github.com/ks-sbc/DRUIDS/issues>
- **Discussions**: <https://github.com/ks-sbc/DRUIDS/discussions>

## 🙏 Acknowledgments

- MkDocs Material by squidfunk
- Giscus by laymonage
- The Mandalorian for aesthetic inspiration
- KSBC community for feedback and testing
