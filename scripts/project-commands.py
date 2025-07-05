#!/usr/bin/env python3
"""
Project slash commands - Unified interface for project automation

This script provides a unified interface for all project slash commands:
- /project:act-test
- /project:deployment-ready  
- /project:test-debug

Usage: python project-commands.py <command> [arguments]
"""

import argparse
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Project automation commands",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Available Commands:

  act-test [workflow] [--mode MODE]
    Execute comprehensive local GitHub Actions workflow testing using Act
    
    Examples:
      python project-commands.py act-test
      python project-commands.py act-test deploy.yml --mode debug
      python project-commands.py act-test --mode dry-run

  deployment-ready [--env ENV] [--auto-fix]
    Validate complete deployment readiness with automated checks
    
    Examples:
      python project-commands.py deployment-ready
      python project-commands.py deployment-ready --env staging
      python project-commands.py deployment-ready --auto-fix

  test-debug <test_pattern> [--verbose] [--auto-fix]
    Intelligent debugging for failing tests with context-aware troubleshooting
    
    Examples:
      python project-commands.py test-debug test_act_integration.py
      python project-commands.py test-debug test_*deployment* --verbose
      python project-commands.py test-debug tests/ --auto-fix

Slash Command Style:
  /project:act-test deploy.yml debug
  /project:deployment-ready production --auto-fix
  /project:test-debug test_act_integration.py --verbose
        """
    )
    
    parser.add_argument(
        "command",
        choices=["act-test", "deployment-ready", "test-debug"],
        help="Command to execute"
    )
    
    parser.add_argument(
        "args",
        nargs="*",
        help="Arguments to pass to the command"
    )
    
    args = parser.parse_args()
    
    # Get the script directory
    script_dir = Path(__file__).parent
    
    # Map commands to their scripts
    command_scripts = {
        "act-test": script_dir / "project-act-test.py",
        "deployment-ready": script_dir / "project-deployment-ready.py", 
        "test-debug": script_dir / "project-test-debug.py"
    }
    
    # Build command to execute
    script_path = command_scripts[args.command]
    cmd = [sys.executable, str(script_path)] + args.args
    
    # Execute the command
    try:
        result = subprocess.run(cmd, cwd=script_dir.parent)
        sys.exit(result.returncode)
    except KeyboardInterrupt:
        print("\n⚠️ Command interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error executing command: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()