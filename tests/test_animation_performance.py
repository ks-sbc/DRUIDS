"""Test CSS animation performance and best practices."""

import re
from pathlib import Path
import pytest
from typing import List, Dict, Set


class TestAnimationPerformance:
    """Test that CSS animations follow performance best practices."""
    
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
    
    def test_animation_properties_performance(self, css_files):
        """Test that animations use performant properties."""
        # Properties that trigger layout (reflow) - expensive
        layout_properties = [
            'width', 'height', 'padding', 'margin',
            'border-width', 'top', 'right', 'bottom', 'left',
            'font-size', 'line-height'
        ]
        
        # Properties that trigger paint - moderate cost
        paint_properties = [
            'color', 'background-color', 'border-color',
            'box-shadow', 'text-shadow'
        ]
        
        # Properties that only trigger composite - cheap
        composite_properties = [
            'transform', 'opacity'
        ]
        
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find all keyframes
            keyframes = re.findall(
                r'@keyframes\s+([a-zA-Z0-9-_]+)\s*{([^}]+(?:{[^}]+}[^}]+)*)}',
                content,
                re.DOTALL
            )
            
            for animation_name, keyframe_content in keyframes:
                # Check what properties are animated
                animated_properties = re.findall(r'([a-zA-Z-]+):\s*[^;]+;', keyframe_content)
                
                # Count expensive animations
                layout_animations = [p for p in animated_properties if p in layout_properties]
                paint_animations = [p for p in animated_properties if p in paint_properties]
                
                # Warn about expensive animations
                if layout_animations:
                    print(f"Warning: Animation '{animation_name}' in {filename} animates layout properties: {set(layout_animations)}")
                    print("  Consider using transform instead for better performance")
                
                if paint_animations and not any(p in composite_properties for p in animated_properties):
                    print(f"Info: Animation '{animation_name}' in {filename} triggers paint: {set(paint_animations)}")
                    print("  Consider adding will-change for frequently animated elements")
    
    def test_transform_animations(self, css_files):
        """Test that transform animations are optimized."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find transform animations
            transforms = re.findall(r'transform:\s*([^;]+);', content)
            
            for transform in transforms:
                # Check for 3D transforms (can enable hardware acceleration)
                if any(func in transform for func in ['translate3d', 'translateZ', 'scale3d', 'rotate3d']):
                    # Good - using 3D transforms
                    pass
                elif any(func in transform for func in ['translateX', 'translateY', 'scale', 'rotate']):
                    # Consider suggesting 3D equivalents for heavy animations
                    if '@keyframes' in content:
                        print(f"Info: Consider using 3D transforms in {filename} for hardware acceleration")
    
    def test_animation_duration(self, css_files):
        """Test that animation durations are reasonable."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find animation/transition durations
            durations = re.findall(r'(?:animation|transition)(?:-duration)?:\s*([^;]*);', content)
            
            for duration_rule in durations:
                # Extract time values
                times = re.findall(r'(\d+(?:\.\d+)?)(s|ms)', duration_rule)
                
                for time_value, unit in times:
                    time_float = float(time_value)
                    
                    # Convert to milliseconds
                    if unit == 's':
                        time_ms = time_float * 1000
                    else:
                        time_ms = time_float
                    
                    # Check for reasonable durations
                    if time_ms > 1000:
                        print(f"Warning: Long animation duration ({time_value}{unit}) in {filename}")
                        print("  Animations over 1s can feel sluggish")
                    
                    if time_ms < 100:
                        print(f"Info: Very short animation ({time_value}{unit}) in {filename}")
                        print("  May not be perceivable")
    
    def test_animation_timing_functions(self, css_files):
        """Test that animations use appropriate timing functions."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find timing functions
            timing_functions = re.findall(
                r'(?:animation|transition)(?:-timing-function)?:\s*([^;]+);',
                content
            )
            
            # Good timing functions for UX
            good_functions = [
                'ease', 'ease-in', 'ease-out', 'ease-in-out',
                'cubic-bezier', 'linear'
            ]
            
            for timing in timing_functions:
                # Check for spring animations (can cause motion sickness)
                if 'spring' in timing:
                    print(f"Warning: Spring animation in {filename} may cause motion sickness")
                
                # Check for steps (usually for sprite animations)
                if 'steps(' in timing:
                    # This is fine for specific use cases
                    pass
    
    def test_will_change_usage(self, css_files):
        """Test that will-change is used appropriately."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find will-change declarations
            will_changes = re.findall(r'will-change:\s*([^;]+);', content)
            
            for will_change in will_changes:
                # Check for appropriate values
                if will_change == 'auto':
                    continue
                
                # Warn about expensive properties
                if any(prop in will_change for prop in ['width', 'height', 'top', 'left']):
                    print(f"Warning: will-change with layout property '{will_change}' in {filename}")
                    print("  This can be expensive. Use transform instead.")
                
                # Check for overuse
                properties = will_change.split(',')
                if len(properties) > 2:
                    print(f"Warning: Too many properties in will-change ({len(properties)}) in {filename}")
                    print("  This can use excessive memory")
    
    def test_reduced_motion_support(self, css_files):
        """Test that animations respect prefers-reduced-motion."""
        all_content = ""
        for file_info in css_files.values():
            all_content += file_info["content"]
        
        # Check if there are animations
        has_animations = any(
            keyword in all_content
            for keyword in ['@keyframes', 'animation:', 'transition:']
        )
        
        if has_animations:
            # Should have reduced motion support
            has_reduced_motion = '@media (prefers-reduced-motion: reduce)' in all_content
            
            assert has_reduced_motion, \
                "CSS contains animations but lacks prefers-reduced-motion support"
            
            # Check that reduced motion actually disables animations
            if has_reduced_motion:
                # Find the reduced motion block
                reduced_blocks = re.findall(
                    r'@media\s*\(prefers-reduced-motion:\s*reduce\)\s*{([^}]+(?:{[^}]+}[^}]+)*)}',
                    all_content,
                    re.DOTALL
                )
                
                # Check that at least one block properly disables animations
                found_proper_reduction = False
                for block in reduced_blocks:
                    # Should disable or reduce animations
                    if any(rule in block for rule in ['animation: none', 'transition: none', 'animation-duration: 0']):
                        found_proper_reduction = True
                        break
                
                assert found_proper_reduction, "Reduced motion media query should actually reduce motion"
    
    def test_animation_performance_hints(self, css_files):
        """Test for performance optimization hints."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Check for GPU-accelerated properties
            if '@keyframes' in content:
                # Look for transforms and opacity (GPU-accelerated)
                gpu_props = content.count('transform:') + content.count('opacity:')
                
                # Look for non-GPU properties in animations
                non_gpu_animated = 0
                keyframes = re.findall(r'@keyframes[^{]+{([^}]+(?:{[^}]+}[^}]+)*)}', content, re.DOTALL)
                
                for keyframe in keyframes:
                    if 'margin' in keyframe or 'padding' in keyframe or 'width' in keyframe or 'height' in keyframe:
                        non_gpu_animated += 1
                
                if non_gpu_animated > 0 and gpu_props == 0:
                    print(f"Performance tip for {filename}: Consider using transform/opacity for animations")
    
    def test_animation_css_containment(self, css_files):
        """Test that animated elements use CSS containment where appropriate."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find elements with animations
            animated_selectors = []
            
            # Find animation declarations
            animations = re.findall(r'([^{]+)\s*{[^}]*animation:[^}]+}', content)
            for selector_block in animations:
                selector = selector_block.strip()
                if selector and not selector.startswith('@'):
                    animated_selectors.append(selector)
            
            # Check if they use containment
            for selector in animated_selectors:
                # Look for contain property for this selector
                pattern = re.escape(selector) + r'\s*{[^}]*contain:[^}]+}'
                if not re.search(pattern, content):
                    # Some selectors benefit from containment
                    if any(keyword in selector for keyword in ['.modal', '.tooltip', '.dropdown', '.card']):
                        print(f"Consider adding 'contain: layout style' to animated element '{selector}' in {filename}")
    
    def test_transition_properties(self, css_files):
        """Test that transitions are specific and optimized."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find transition declarations
            transitions = re.findall(r'transition:\s*([^;]+);', content)
            
            for transition in transitions:
                # Check for 'all' transitions
                if 'all' in transition:
                    print(f"Warning: 'transition: all' found in {filename}")
                    print("  This can cause unexpected animations. Be specific about properties.")
                
                # Check for multiple properties
                properties = transition.split(',')
                if len(properties) > 4:
                    print(f"Info: Many transition properties ({len(properties)}) in {filename}")
                    print("  Consider if all are necessary")
    
    def test_animation_fill_mode(self, css_files):
        """Test that animations use appropriate fill modes."""
        for filename, file_info in css_files.items():
            content = file_info["content"]
            
            # Find animations without fill mode
            animation_rules = re.findall(r'animation:\s*([^;]+);', content)
            
            for rule in animation_rules:
                # Check if fill-mode is specified
                if 'forwards' not in rule and 'backwards' not in rule and 'both' not in rule:
                    # Check if it's a looping animation
                    if 'infinite' not in rule:
                        print(f"Info: Animation in {filename} doesn't specify fill-mode")
                        print("  Consider animation-fill-mode for non-looping animations")