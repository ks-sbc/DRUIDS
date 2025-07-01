"""
MkDocs hooks for shortcodes and custom functionality.
This file can be extended with custom hooks as needed.
"""

def on_page_markdown(markdown, **kwargs):
    """
    Hook to process markdown content before it's converted to HTML.
    Add custom shortcodes or processing here.
    """
    return markdown

def on_page_content(html, **kwargs):
    """
    Hook to process HTML content after markdown conversion.
    Add custom HTML processing here.
    """
    return html