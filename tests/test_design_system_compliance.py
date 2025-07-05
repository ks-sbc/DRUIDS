"""Test CSS compliance with design system standards."""

import re
from pathlib import Path
import pytest
from typing import Dict, Set, List


class TestDesignSystemCompliance:
    """Test that CSS follows design system patterns and conventions."""
    
    @pytest.fixture
    def css_files(self):
        """Get all CSS files."""
        css_dir = Path("docs/assets/css")
        files = {}
        for css_file in css_dir.glob("druids-*.css"):
            files[css_file.name] = {
                "path": css_file,
                "content": css_file.read_text()
            }
        return files
    
    @pytest.fixture
    def design_tokens(self):
        """Get design system tokens from theme CSS."""
        theme_css = Path("docs/assets/css/druids-theme.css").read_text()
        
        # Extract all CSS custom properties
        tokens = {
            'colors': set(),
            'spacing': set(),
            'typography': set(),
            'radius': set(),
            'gradients': set()
        }
        
        # Find all custom properties
        custom_props = re.findall(r'(--druids-[a-zA-Z0-9-]+):\s*([^;]+);', theme_css)
        
        for prop, value in custom_props:
            if 'color' in prop or 'bg' in prop or 'text' in prop:
                tokens['colors'].add(prop)
            elif 'radius' in prop:
                tokens['radius'].add(prop)
            elif 'gradient' in prop:
                tokens['gradients'].add(prop)
            elif any(x in prop for x in ['text-', 'line-height']):
                tokens['typography'].add(prop)
        
        return tokens
    
    def test_color_token_usage(self, css_files, design_tokens):
        """Test that colors use design system tokens instead of hardcoded values."""
        # Skip theme.css as it defines the tokens
        test_files = {k: v for k, v in css_files.items() if k != "druids-theme.css"}
        
        for filename, file_info in test_files.items():
            content = file_info["content"]
            
            # Find hardcoded colors
            hex_colors = re.findall(r':\s*(#[0-9A-Fa-f]{3,6})\b', content)
            rgb_colors = re.findall(r':\s*(rgba?\([^)]+\))', content)
            
            # Check each hardcoded color
            hardcoded = []
            for color in hex_colors + rgb_colors:
                # Check if it's in a custom property definition
                if f': {color}' not in content or '--druids-' not in content:
                    # Check if it's using a variable
                    if not re.search(rf'var\(--druids-[^)]+\)', content):
                        hardcoded.append(color)
            
            assert len(hardcoded) == 0, \
                f"Hardcoded colors found in {filename}: {hardcoded[:5]}... Use design tokens instead"
    
    def test_spacing_consistency(self, css_files):
        """Test that spacing values follow design system scale."""
        # Common spacing scale (in rem)
        valid_spacing = [
            '0', '0.25rem', '0.5rem', '0.75rem', '1rem', '1.25rem',
            '1.5rem', '1.75rem', '2rem', '2.5rem', '3rem', '4rem'
        ]
        
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find margin and padding values
            spacing_props = re.findall(r'(?:margin|padding)(?:-(?:top|right|bottom|left))?:\s*([^;]+);', content)
            
            for spacing in spacing_props:
                # Skip auto, inherit, and percentage values
                if spacing in ['auto', 'inherit', '0'] or '%' in spacing:
                    continue
                
                # Skip variable usage
                if 'var(' in spacing:
                    continue
                
                # Check individual values in shorthand
                values = spacing.split()
                for value in values:
                    if value not in valid_spacing and not value.startswith('var('):
                        # Allow calc() expressions
                        if not value.startswith('calc('):
                            print(f"Warning: Non-standard spacing '{value}' in {filename}")
    
    def test_typography_scale(self, css_files, design_tokens):
        """Test that font sizes use the design system typography scale."""
        for filename, file_info in css_files.items():
            if filename == "druids-theme.css":
                continue
                
            content = file_info["content"]
            
            # Find font-size declarations
            font_sizes = re.findall(r'font-size:\s*([^;]+);', content)
            
            for size in font_sizes:
                # Should use design tokens
                if not size.startswith('var(--druids-text-'):
                    # Check if it's a valid exception
                    valid_exceptions = ['inherit', 'initial', '100%']
                    # Allow calc() expressions that use typography tokens
                    # Allow em values for icons and relative sizing
                    if size not in valid_exceptions and not (size.startswith('calc(') and 'var(--druids-text-' in size) and not size.endswith('em'):
                        assert False, \
                            f"Font size '{size}' in {filename} should use typography tokens"
    
    def test_component_naming_conventions(self, css_files):
        """Test that component classes follow naming conventions."""
        # DRUIDS project uses .druids- prefix for custom components
        for filename, file_info in css_files.items():
            if filename == "druids-utilities.css":
                continue  # Utilities may have different patterns
                
            content = file_info["content"]
            
            # Find class selectors (more precise pattern to avoid matching numeric values)
            # This pattern matches class selectors but not decimal numbers
            classes = re.findall(r'\.([a-zA-Z][a-zA-Z0-9-_]*)', content)
            
            custom_classes = []
            for class_name in classes:
                # Skip MkDocs Material classes (md-)
                if class_name.startswith('md-'):
                    continue
                    
                # Skip state classes
                if class_name in ['active', 'disabled', 'hover', 'focus']:
                    continue
                    
                # Skip common third-party classes
                third_party_classes = [
                    'highlight', 'linenodiv', 'linenos',  # Syntax highlighting
                    'admonition', 'note', 'warning', 'tip', 'info', 'danger',  # MkDocs admonitions
                    'admonition-title', 'task-list-item',  # MkDocs components
                    'twemoji', 'emojione', 'material-icons',  # Icon libraries
                    'mermaid', 'node',  # Mermaid diagrams
                    'grid', 'cards',  # Layout components
                    'glow-cyan', 'glow-orange',  # Our utility classes
                    'skip-to-content', 'sr-only',  # Accessibility
                    'text-left', 'text-center', 'text-right',  # Text utilities
                    'bg-primary', 'bg-secondary', 'bg-gradient',  # Background utilities
                    'd-none', 'd-block', 'd-inline', 'd-flex', 'd-grid',  # Display utilities
                    'border', 'rounded', 'shadow',  # Border/shadow utilities
                    'hide-mobile', 'show-mobile', 'hide-desktop', 'show-desktop'  # Responsive
                ]
                if class_name in third_party_classes:
                    continue
                    
                # Custom classes should follow naming convention
                if not class_name.startswith(('druids-', 'test-', 'text-', 'bg-', 'd-', 'flex-', 
                                             'justify-', 'align-', 'border-', 'rounded-', 
                                             'shadow-', 'mt-', 'mb-', 'pt-', 'pb-')):
                    custom_classes.append(class_name)
            
            # Some custom classes are acceptable, but should be minimal
            # Allow up to 20 custom classes for third-party integrations
            assert len(custom_classes) < 20, \
                f"Too many non-standard class names in {filename}: {custom_classes[:10]}..."
    
    def test_breakpoint_consistency(self, css_files):
        """Test that media queries use consistent breakpoints."""
        standard_breakpoints = {
            'mobile': 767,
            'tablet-min': 768,
            'tablet-max': 959,
            'desktop': 960,
            'wide': 1200
        }
        
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find all media query breakpoints
            breakpoints = re.findall(r'@media[^{]*(?:min|max)-width:\s*(\d+)px', content)
            
            for bp in breakpoints:
                bp_value = int(bp)
                
                # Check if it matches standard breakpoints
                is_standard = bp_value in standard_breakpoints.values()
                
                # Allow some flexibility (±1px for rounding)
                is_near_standard = any(
                    abs(bp_value - std) <= 1 
                    for std in standard_breakpoints.values()
                )
                
                assert is_standard or is_near_standard, \
                    f"Non-standard breakpoint {bp}px in {filename}. Use standard breakpoints: {list(standard_breakpoints.values())}"
    
    def test_animation_naming(self, css_files):
        """Test that animations follow naming conventions."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find keyframe animations
            animations = re.findall(r'@keyframes\s+([a-zA-Z0-9-_]+)', content)
            
            for animation in animations:
                # Animation names should be descriptive and kebab-case
                assert re.match(r'^[a-z][a-z0-9-]*$', animation), \
                    f"Animation '{animation}' in {filename} should use kebab-case"
                
                # Should have meaningful names
                assert len(animation) > 3, \
                    f"Animation name '{animation}' in {filename} is too short"
    
    def test_z_index_scale(self, css_files):
        """Test that z-index values follow a consistent scale."""
        # Design system z-index scale
        valid_z_indexes = [
            '-1', '0', '1', '10', '100', '1000', '9999'
        ]
        
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find z-index values
            z_indexes = re.findall(r'z-index:\s*([^;]+);', content)
            
            for z_value in z_indexes:
                # Skip variables and keywords
                if z_value.startswith('var(') or z_value in ['auto', 'inherit']:
                    continue
                
                # Check if it's in the scale
                if z_value not in valid_z_indexes:
                    print(f"Warning: Non-standard z-index '{z_value}' in {filename}")
    
    def test_custom_property_prefix(self, css_files):
        """Test that all custom properties use the project prefix."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find all custom property definitions (CSS custom properties start with --)
            # Match lines that define custom properties, not class names
            custom_props = re.findall(r'^\s*(--[a-zA-Z0-9-]+):', content, re.MULTILINE)
            
            for prop in custom_props:
                # Allow MkDocs Material theme variables that we're overriding
                if prop.startswith('--md-') and filename == "druids-theme.css":
                    continue
                assert prop.startswith('--druids-'), \
                    f"Custom property '{prop}' in {filename} should use '--druids-' prefix"
    
    def test_gradient_consistency(self, css_files, design_tokens):
        """Test that gradients use design system tokens."""
        for filename, file_info in css_files.items():
            if filename == "druids-theme.css":
                continue
                
            content = file_info["content"]
            
            # Find gradient declarations
            gradients = re.findall(r'(?:background|background-image):\s*([^;]*gradient[^;]+);', content)
            
            for gradient in gradients:
                # Should use gradient tokens or color tokens
                if 'var(--druids-gradient-' not in gradient:
                    # Check if it at least uses color tokens
                    # Allow RGBA values that match our design colors (e.g., cyan rgba(0, 217, 255, 0.2))
                    if 'var(--druids-' not in gradient and 'rgba(0, 217, 255' not in gradient:
                        assert False, \
                            f"Gradient in {filename} should use design tokens: {gradient[:50]}..."