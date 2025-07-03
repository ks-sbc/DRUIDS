# TODO - MkDocs Project

NOTE: If you come across a broken link, fix it. If you come across a missing page, ignore it and remove the link.

## 🐛 Bugs Found During Manual Testing

### Fixed

- [x] **Broken wikilink syntax in tutorials/index.md** - Mixed Obsidian and Markdown syntax `[:text]([[../path]])` corrected to `[:text](../path.md)`
- [x] **Blog tags link** - Fixed path from `[[tags]]` to `[[../tags]]` in blog index

### To Fix

- [x] **Code syntax highlighting not working** - ✅ FALSE ALARM! Pygments IS working, generates proper span elements with classes
- [ ] **Wikilink hash anchors showing in URLs** - pub-obsidian generating hashes like `#39fcfe0df696631025ff0176e29d8413`

## 🚀 Enhancements

### CRITICAL PRIORITY

**UPDATE**: Tested all markdown extensions - most are already working! See test-features.md and test-features-results.md

- [x] **Markdown Extensions** - Most already work:
  - [x] **Mermaid** - ✅ Working via pymdownx.superfences
  - [x] **Admonitions** - ✅ Working (both !!! and > [!note] styles)
  - [ ] **Annotations** - Needs Material CSS/JS setup
  - [ ] **Buttons** - Needs Material CSS classes
  - [x] **Code blocks** - ✅ Working with Pygments highlighting
  - [x] **Content tabs** - ✅ Working via pymdownx.tabbed
  - [x] **Data tables** - ✅ Standard markdown tables work
  - [x] **Diagrams** - ✅ Mermaid works
  - [x] **Footnotes** - ✅ Working
  - [x] **Formatting** - ✅ All formatting works (mark, caret, tilde)
  - [ ] **Grids** - Needs Material CSS classes
  - [x] **Icons, Emojis** - ✅ Emojis work, Material icons need testing
  - [x] **Images** - ✅ Basic images work
  - [x] **Lists** - ✅ All list types work
  - [x] **Math** - ✅ Working with MathJax
  - [ ] **Tooltips** - Needs testing with proper syntax
- [ ] **Plugins** - Critical:
  - [x] **Giscus - material** - ✅ Integrated with custom partial
  - [x] **Footer - material** - ✅ Footer exists for giscus
  - [x] **Complete Giscus integration** - ✅ Script added to comments.html
  - [x] **Add giscus.json** - ✅ Security configuration complete
  - [ ] **Create custom giscus-druids.css** - Basic CSS exists, needs Mandalorian theme
  - [x] **Get real Giscus credentials** - ✅ Using ks-sbc/DRUIDS repo

### High Priority

- [x] **Get real Giscus credentials** - ✅ DONE! Using ks-sbc/DRUIDS repo
- [ ] **Create giscus-druids.css** - Add Mandalorian-themed styling for comments
- [ ] **Caption plugin - material** - for accessibility and SEO
- [ ] **CriticMarkup plugin - Material** - for editing and writing work
- [ ] **Snippets plugin - Material** - for reusable content
- [ ] **SuperFences plugin - Material** - for code blocks and Mermaid
- [ ] **Tasklist plugin - Material** - for task lists
- [ ] \*\*Tabbed p

### Medium Priority

- [ ] **Fix template pages in how-to/mkdocs.md**:
  - [ ] Note Template.md
  - [ ] Tutorial Template.md
  - [ ] Reference Template.md
  - [ ] Project Template.md
- [ ] **Add proper code highlighting configuration**
- [ ] **Theme customization** - Update colors and brandingo
- [ ] **Macros plugin** - Use python to dynamically generate content
- [ ] **Consent plugin** - Pop up for cookies and privacy
- [ ] **MCP plugin** - may make development much easier and faster

### Low Priority

- [ ] **Add more blog posts** to demonstrate features
- [ ] **Plugins** - Nice to have:
  - [ ] **RSS plugin - material**
  - [ ] **Privacy plugin - material**
  - [ ] **Analytics - material**
  - [ ] **Pub-Meta - material**
  - [ ] **Obsidian Vega** - for graphs and charts\*\*
  - [ ] **Versioning - material** - for tracking changes
  - [ ] **Optimized site - material** - for faster loading
- [ ] **Add search configuration** customization
- [ ] **Optimize images** for faster loading

## 🧪 Testing Improvements

- [ ] **Add visual regression tests** for rendered output
- [ ] **Test wikilink rendering** not just configuration
- [ ] **Add accessibility tests**
- [ ] **Test mobile responsiveness**
- [ ] **Check all navigation paths**

## 📚 Documentation

- [ ] **Document wikilink syntax rules** for pub-obsidian
- [ ] **Create contribution guide**
- [ ] **Add deployment guide** for different platforms
- [ ] **Document theme customization** process

## 🔧 Configuration Cleanup

- [ ] **Review and optimize mkdocs.yml** for unused features
- [ ] **Check if all markdown extensions** are needed
- [ ] **Optimize build performance**
- [ ] **Add caching configuration**

## Notes

- Tests pass but don't catch rendering issues
- Manual testing revealed mixed syntax problems
- pub-obsidian plugin has quirks with hash anchors
- Code highlighting might need additional configuration
