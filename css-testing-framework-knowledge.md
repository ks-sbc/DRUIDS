# CSS Testing Framework Knowledge Base

This document contains comprehensive knowledge items for implementing a robust CSS testing framework in the DRUIDS infrastructure project.

## Knowledge Item 1: Comprehensive CSS Testing Framework Architecture

**Domain**: technical  
**Tags**: css, testing, pytest, frontend, quality-assurance  
**Priority**: high

### Title: CSS Testing Framework Architecture Pattern

### Content:
A comprehensive CSS testing framework should be organized into five distinct test categories, each serving a specific quality assurance purpose:

1. **W3C Standards Validation** - Ensures CSS follows official specifications
2. **Design System Compliance** - Validates adherence to design tokens and patterns
3. **Critical CSS Optimization** - Tests performance-critical above-the-fold styles
4. **Animation Performance** - Validates smooth, accessible animations
5. **Cross-Browser Compatibility** - Ensures consistent rendering across browsers

### Implementation Pattern:
```python
# Structure tests by concern
tests/
├── test_w3c_validation.py      # Standards compliance
├── test_design_system.py        # Design token usage
├── test_critical_css.py         # Performance optimization
├── test_animation_perf.py       # Animation best practices
└── test_cross_browser.py        # Compatibility checks
```

### Key Insights:
- Use regex patterns for CSS parsing, but be careful of greedy matching
- Test CSS properties mathematically (e.g., WCAG contrast ratios)
- Allow flexibility for third-party integrations while enforcing standards
- Separate concerns: syntax, semantics, performance, and compatibility

---

## Knowledge Item 2: CSS Accessibility Testing with Mathematical Validation

**Domain**: technical  
**Tags**: accessibility, wcag, css, testing, contrast-ratio  
**Priority**: high

### Title: Mathematical WCAG Contrast Testing Implementation

### Content:
Implement automated WCAG contrast ratio testing using mathematical calculations rather than visual comparison tools. This enables CI/CD integration and consistent validation.

### Implementation:
```python
def _relative_luminance(rgb):
    """Calculate relative luminance per WCAG formula"""
    r, g, b = [x / 255.0 for x in rgb]
    # Apply gamma correction
    r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
    g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
    b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def _contrast_ratio(color1_hex, color2_hex):
    """Calculate WCAG contrast ratio between colors"""
    # Convert and calculate luminance
    lum1 = self._relative_luminance(self._hex_to_rgb(color1_hex))
    lum2 = self._relative_luminance(self._hex_to_rgb(color2_hex))
    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)
    return (lighter + 0.05) / (darker + 0.05)
```

### Success Metrics:
- Normal text: 4.5:1 minimum (AA), 7:1 (AAA)
- Large text: 3:1 minimum (AA), 4.5:1 (AAA)
- UI components: 3:1 minimum

---

## Knowledge Item 3: Test-Driven CSS Development Pattern

**Domain**: process  
**Tags**: tdd, css, testing, workflow, quality-assurance  
**Priority**: high

### Title: TDD Workflow for CSS Implementation

### Content:
Apply Test-Driven Development principles to CSS by writing tests that validate design requirements before implementation.

### Workflow:
1. **Red Phase**: Write tests for design requirements
   - Typography scale adherence
   - Color token usage
   - Spacing consistency
   - Accessibility compliance

2. **Green Phase**: Implement minimal CSS to pass tests
   - Use design tokens instead of hardcoded values
   - Follow naming conventions
   - Ensure accessibility standards

3. **Refactor Phase**: Optimize while maintaining tests
   - Reduce !important usage
   - Consolidate duplicate rules
   - Improve selector efficiency

### Benefits:
- Prevents design drift from established system
- Catches accessibility issues early
- Ensures consistent implementation across team
- Documents design decisions in test form

---

## Knowledge Item 4: CSS Performance Testing Patterns

**Domain**: technical  
**Tags**: performance, css, critical-css, optimization  
**Priority**: medium

### Title: Critical CSS Extraction and Testing

### Content:
Implement automated testing for critical CSS to ensure optimal page load performance.

### Key Patterns:
1. **File Size Limits**:
   - Theme CSS: < 10KB
   - Layout CSS: < 15KB
   - Combined critical: < 14KB (for inlining)

2. **Selector Efficiency**:
   - Avoid universal selectors in critical path
   - Limit selector depth to 3 levels
   - Use CSS containment for complex components

3. **Loading Strategy**:
   - Test that above-fold styles are in critical CSS
   - Verify no @import statements (render-blocking)
   - Ensure proper file loading order

### Testing Approach:
```python
def test_critical_css_size(css_files):
    critical_files = ["theme.css", "layout.css"]
    total_size = sum(get_file_size(f) for f in critical_files)
    assert total_size < 14336  # 14KB limit for inlining
```

---

## Knowledge Item 5: Flexible Test Design for Third-Party Integration

**Domain**: technical  
**Tags**: testing, integration, css, third-party  
**Priority**: medium

### Title: Designing Flexible CSS Tests for Real-World Projects

### Content:
CSS tests must balance strictness with flexibility to accommodate legitimate third-party integrations while maintaining quality standards.

### Strategies:
1. **Allowlists for Known Libraries**:
   - Syntax highlighting: `.highlight`, `.linenos`
   - Icons: `.material-icons`, `.twemoji`
   - Diagrams: `.mermaid`, `.node`
   - UI frameworks: `.md-*` prefixes

2. **Relative Validation**:
   - Allow `em` units for icon sizing
   - Permit `calc()` with design tokens
   - Accept vendor prefixes for compatibility

3. **Context-Aware Rules**:
   - Utilities can use !important
   - Theme files can define non-prefixed variables
   - Different limits for different file types

### Anti-patterns to Avoid:
- Over-zealous regex that matches too broadly
- Tests that break with every library update
- Inflexible rules that prevent legitimate patterns

---

## Knowledge Item 6: CSS Testing Tool Selection Criteria

**Domain**: decision  
**Tags**: tools, testing, css, selection-criteria  
**Priority**: medium

### Title: Choosing CSS Testing Tools and Approaches

### Content:
Selection criteria for CSS testing tools based on project needs and constraints.

### Decision Matrix:
1. **For Syntax Validation**: W3C validators or regex patterns
2. **For Visual Regression**: BackstopJS (OSS) or Percy (commercial)
3. **For Accessibility**: Custom mathematical validation
4. **For Performance**: Custom metrics and thresholds
5. **For Browser Testing**: Real device testing over emulation

### Key Considerations:
- Avoid visual screenshot comparison for CI/CD (flaky)
- Prefer testing CSS specifications over visual output
- Use mathematical validation for objective metrics
- Balance automation with manual review needs

### Recommended Stack:
- pytest for test framework
- regex for CSS parsing
- Mathematical validation for accessibility
- File size/metric validation for performance

---

## Implementation Summary

This knowledge base provides a comprehensive framework for implementing CSS testing in the DRUIDS infrastructure project. The key principles are:

1. **Structured Testing**: Organize tests by concern (validation, design system, performance, accessibility, compatibility)
2. **Mathematical Validation**: Use objective measurements rather than visual comparisons
3. **Flexible Design**: Balance strictness with real-world integration needs
4. **Performance Focus**: Prioritize critical CSS optimization and load performance
5. **Accessibility First**: Implement automated WCAG compliance testing
6. **Tool Selection**: Choose tools based on specific needs and constraints

These knowledge items should be integrated into the project's testing strategy and can serve as a reference for implementing a robust CSS quality assurance framework.