#!/usr/bin/env python3
"""
Shared utility functions for MkDocs tests
"""

import re
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml


def run_command(cmd: str, cwd: Optional[Path] = None) -> Tuple[bool, str, str]:
    """
    Run a command and return success status and output
    
    Args:
        cmd: Command to run
        cwd: Working directory
        
    Returns:
        Tuple of (success, stdout, stderr)
    """
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, cwd=cwd
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)


def extract_frontmatter(content: str) -> Tuple[Optional[Dict], Optional[str]]:
    """
    Extract frontmatter and content from a markdown file
    
    Args:
        content: Raw markdown content
        
    Returns:
        Tuple of (frontmatter dict, remaining content) or (None, None) if invalid
    """
    if not content.strip().startswith("---"):
        return None, content
    
    try:
        parts = content.split("---", 2)
        if len(parts) < 3:
            return None, None
            
        frontmatter_str = parts[1]
        body = parts[2]
        
        frontmatter = yaml.safe_load(frontmatter_str)
        return frontmatter, body
    except yaml.YAMLError:
        return None, None


def find_markdown_links(content: str) -> List[Dict[str, str]]:
    """
    Find all markdown links in content
    
    Args:
        content: Markdown content
        
    Returns:
        List of dicts with 'text' and 'url' keys
    """
    # Regex for markdown links [text](url)
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    links = []
    
    for match in re.finditer(link_pattern, content):
        links.append({
            'text': match.group(1),
            'url': match.group(2)
        })
    
    return links


def find_markdown_images(content: str) -> List[Dict[str, str]]:
    """
    Find all markdown images in content
    
    Args:
        content: Markdown content
        
    Returns:
        List of dicts with 'alt' and 'src' keys
    """
    # Regex for markdown images ![alt](src)
    image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    images = []
    
    for match in re.finditer(image_pattern, content):
        images.append({
            'alt': match.group(1),
            'src': match.group(2)
        })
    
    return images


def validate_internal_link(link: str, current_file: Path, docs_dir: Path) -> bool:
    """
    Validate an internal link
    
    Args:
        link: Link URL
        current_file: Path to the file containing the link
        docs_dir: Documentation root directory
        
    Returns:
        True if link is valid
    """
    # Skip external links
    if link.startswith(('http://', 'https://', 'mailto:', '#')):
        return True
    
    # Remove anchor if present
    if '#' in link:
        link = link.split('#')[0]
    
    # Skip empty links
    if not link:
        return True
    
    # Resolve the link relative to the current file
    link_path = (current_file.parent / link).resolve()
    
    # Check if it's a directory (should have index.md)
    if link_path.is_dir():
        link_path = link_path / "index.md"
    
    # Add .md extension if not present
    if not link_path.suffix and not link_path.exists():
        link_path = link_path.with_suffix('.md')
    
    # Check if the file exists
    return link_path.exists()


def check_command_available(command: str) -> bool:
    """
    Check if a command is available in the system
    
    Args:
        command: Command to check
        
    Returns:
        True if command is available
    """
    try:
        subprocess.run(
            f"which {command}", 
            shell=True, 
            capture_output=True, 
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        return False


def get_all_markdown_files(directory: Path, exclude_patterns: Optional[List[str]] = None) -> List[Path]:
    """
    Get all markdown files in a directory recursively
    
    Args:
        directory: Directory to search
        exclude_patterns: List of glob patterns to exclude
        
    Returns:
        List of markdown file paths
    """
    exclude_patterns = exclude_patterns or []
    markdown_files = []
    
    for md_file in directory.rglob("*.md"):
        # Check if file should be excluded
        should_exclude = False
        for pattern in exclude_patterns:
            if md_file.match(pattern):
                should_exclude = True
                break
        
        if not should_exclude:
            markdown_files.append(md_file)
    
    return markdown_files


def validate_yaml_file(yaml_path: Path) -> Tuple[bool, Optional[str]]:
    """
    Validate a YAML file
    
    Args:
        yaml_path: Path to YAML file
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    try:
        with open(yaml_path, 'r') as f:
            yaml.safe_load(f)
        return True, None
    except yaml.YAMLError as e:
        return False, str(e)
    except Exception as e:
        return False, f"Failed to read file: {e}"


def parse_mkdocs_output(output: str) -> Dict[str, List[Dict[str, str]]]:
    """
    Parse MkDocs build output to extract warnings and errors
    
    Args:
        output: Combined stdout and stderr from mkdocs build
        
    Returns:
        Dict with 'warnings', 'errors', 'info' keys containing parsed messages
    """
    result = {
        'warnings': [],
        'errors': [],
        'info': []
    }
    
    lines = output.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Parse WARNING messages
        if line.startswith('WARNING'):
            # Extract the warning message after "WARNING - "
            match = re.match(r'WARNING\s*-\s*(.+)', line)
            if match:
                warning_text = match.group(1)
                parsed_warning = parse_warning_message(warning_text)
                if parsed_warning:
                    result['warnings'].append(parsed_warning)
                    
        # Parse ERROR messages
        elif line.startswith('ERROR'):
            match = re.match(r'ERROR\s*-\s*(.+)', line)
            if match:
                result['errors'].append({
                    'type': 'error',
                    'message': match.group(1)
                })
                
        # Parse INFO messages (especially for absolute links)
        elif line.startswith('INFO') and 'absolute link' in line:
            match = re.match(r'INFO\s*-\s*(.+)', line)
            if match:
                info_text = match.group(1)
                parsed_info = parse_info_message(info_text)
                if parsed_info:
                    result['info'].append(parsed_info)
    
    return result


def parse_warning_message(warning_text: str) -> Optional[Dict[str, str]]:
    """
    Parse a warning message to extract structured information
    
    Args:
        warning_text: The warning text after "WARNING - "
        
    Returns:
        Dict with warning details or None if not parseable
    """
    # Pattern: "A reference to 'X' is included in the 'nav' configuration, which is not found"
    nav_pattern = r"A reference to '([^']+)' is included in the 'nav' configuration, which is not found"
    match = re.match(nav_pattern, warning_text)
    if match:
        return {
            'type': 'nav_reference_not_found',
            'severity': 'critical',
            'file': match.group(1),
            'message': warning_text
        }
    
    # Pattern: "Doc file 'X' contains a link 'Y', but the target is not found"
    link_pattern = r"Doc file '([^']+)' contains a link '([^']+)', but the target (?:'([^']+)' )?is not found"
    match = re.match(link_pattern, warning_text)
    if match:
        return {
            'type': 'broken_link',
            'severity': 'high',
            'source_file': match.group(1),
            'link': match.group(2),
            'target': match.group(3) or match.group(2),
            'message': warning_text
        }
    
    # Pattern: "Doc file 'X' contains a link 'Y', but the target 'Z' is not found. Did you mean 'W'?"
    suggestion_pattern = r"Doc file '([^']+)' contains a link '([^']+)', but the target '([^']+)' is not found.*Did you mean '([^']+)'\?"
    match = re.match(suggestion_pattern, warning_text)
    if match:
        return {
            'type': 'broken_link_with_suggestion',
            'severity': 'high',
            'source_file': match.group(1),
            'link': match.group(2),
            'target': match.group(3),
            'suggestion': match.group(4),
            'message': warning_text
        }
    
    # Generic warning
    return {
        'type': 'generic',
        'severity': 'medium',
        'message': warning_text
    }


def parse_info_message(info_text: str) -> Optional[Dict[str, str]]:
    """
    Parse an info message to extract structured information
    
    Args:
        info_text: The info text after "INFO - "
        
    Returns:
        Dict with info details or None if not parseable
    """
    # Pattern: "Doc file 'X' contains an absolute link 'Y', it was left as is. Did you mean 'Z'?"
    absolute_pattern = r"Doc file '([^']+)' contains an absolute link '([^']+)', it was left as is\.(?:\s*Did you mean '([^']+)'\?)?"
    match = re.match(absolute_pattern, info_text)
    if match:
        return {
            'type': 'absolute_link',
            'severity': 'medium',
            'source_file': match.group(1),
            'link': match.group(2),
            'suggestion': match.group(3) if match.group(3) else None,
            'message': info_text
        }
    
    return None


def categorize_warnings(parsed_output: Dict[str, List[Dict[str, str]]]) -> Dict[str, List[Dict[str, str]]]:
    """
    Categorize warnings by severity
    
    Args:
        parsed_output: Output from parse_mkdocs_output
        
    Returns:
        Dict with 'critical', 'high', 'medium', 'low' severity categories
    """
    categorized = {
        'critical': [],
        'high': [],
        'medium': [],
        'low': []
    }
    
    # Categorize warnings
    for warning in parsed_output.get('warnings', []):
        severity = warning.get('severity', 'medium')
        categorized[severity].append(warning)
    
    # All errors are critical
    for error in parsed_output.get('errors', []):
        error['severity'] = 'critical'
        categorized['critical'].append(error)
    
    # Info messages are usually medium severity
    for info in parsed_output.get('info', []):
        severity = info.get('severity', 'medium')
        categorized[severity].append(info)
    
    return categorized


def format_warning_report(categorized_warnings: Dict[str, List[Dict[str, str]]]) -> str:
    """
    Format warnings into a readable report
    
    Args:
        categorized_warnings: Output from categorize_warnings
        
    Returns:
        Formatted report string
    """
    report_lines = []
    
    # Count totals
    total_critical = len(categorized_warnings['critical'])
    total_high = len(categorized_warnings['high'])
    total_medium = len(categorized_warnings['medium'])
    total_low = len(categorized_warnings['low'])
    total_all = total_critical + total_high + total_medium + total_low
    
    if total_all == 0:
        return "No warnings or errors found!"
    
    report_lines.append(f"\nMkDocs Build Quality Report")
    report_lines.append("=" * 50)
    report_lines.append(f"Total issues: {total_all}")
    report_lines.append(f"  Critical: {total_critical}")
    report_lines.append(f"  High:     {total_high}")
    report_lines.append(f"  Medium:   {total_medium}")
    report_lines.append(f"  Low:      {total_low}")
    report_lines.append("")
    
    # Format each severity level
    for severity in ['critical', 'high', 'medium', 'low']:
        warnings = categorized_warnings[severity]
        if warnings:
            report_lines.append(f"\n{severity.upper()} Severity Issues:")
            report_lines.append("-" * 40)
            
            # Group by type
            by_type = {}
            for warning in warnings:
                warning_type = warning.get('type', 'unknown')
                if warning_type not in by_type:
                    by_type[warning_type] = []
                by_type[warning_type].append(warning)
            
            for warning_type, items in by_type.items():
                report_lines.append(f"\n  {warning_type.replace('_', ' ').title()} ({len(items)} issues):")
                
                for item in items[:5]:  # Show first 5 of each type
                    if warning_type == 'nav_reference_not_found':
                        report_lines.append(f"    - Missing nav file: {item['file']}")
                    elif warning_type in ['broken_link', 'broken_link_with_suggestion']:
                        report_lines.append(f"    - {item['source_file']}: Link '{item['link']}' → target '{item.get('target', item['link'])}' not found")
                        if 'suggestion' in item and item['suggestion']:
                            report_lines.append(f"      Suggestion: {item['suggestion']}")
                    elif warning_type == 'absolute_link':
                        report_lines.append(f"    - {item['source_file']}: Absolute link '{item['link']}'")
                        if item.get('suggestion'):
                            report_lines.append(f"      Should be: {item['suggestion']}")
                    else:
                        report_lines.append(f"    - {item.get('message', 'Unknown issue')}")
                
                if len(items) > 5:
                    report_lines.append(f"    ... and {len(items) - 5} more")
    
    return "\n".join(report_lines)