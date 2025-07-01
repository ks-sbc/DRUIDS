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