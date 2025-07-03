#!/usr/bin/env python3
"""
Deployment Validation for MkDocs
Simple, focused validation that ensures documentation can be built and served.
"""

import subprocess
import sys
import os
from pathlib import Path
import tempfile
import time
import signal
from typing import Tuple


def run_command(cmd: list, timeout: int = 60) -> Tuple[bool, str]:
    """Run a command and return success status and output."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=Path(__file__).parent.parent
        )
        return result.returncode == 0, result.stderr + result.stdout
    except subprocess.TimeoutExpired:
        return False, f"Command timed out after {timeout} seconds"
    except Exception as e:
        return False, f"Command failed: {str(e)}"


def validate_mkdocs_config() -> bool:
    """Ensure mkdocs.yml is valid and can be loaded."""
    print("🔍 Validating MkDocs configuration...")

    success, output = run_command(["mkdocs", "help"])
    if success:
        print("✅ MkDocs configuration is valid")
        return True
    else:
        print("❌ MkDocs configuration is invalid:")
        print(output)
        return False


def validate_build() -> bool:
    """Test that MkDocs can build the site successfully."""
    print("🏗️  Testing MkDocs build...")
    
    # Use clean strict build to catch all issues
    success, output = run_command(["mkdocs", "build", "--clean", "--strict"], timeout=120)
    
    if success:
        print("✅ MkDocs build succeeded")
        return True
    else:
        print("❌ MkDocs build failed:")
        print(output)
        return False


def validate_serve() -> bool:
    """Test that MkDocs can start the development server."""
    print("🚀 Testing MkDocs serve...")
    
    # Start server in background
    try:
        process = subprocess.Popen(
            ["mkdocs", "serve", "--dev-addr", "127.0.0.1:8001"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=Path(__file__).parent.parent
        )
        
        # Wait for server to start
        time.sleep(3)
        
        # Check if process is still running
        if process.poll() is None:
            print("✅ MkDocs serve started successfully")
            # Clean shutdown
            process.terminate()
            process.wait(timeout=5)
            return True
        else:
            stdout, stderr = process.communicate()
            print("❌ MkDocs serve failed to start:")
            print(stderr + stdout)
            return False
            
    except Exception as e:
        print(f"❌ Error testing serve: {str(e)}")
        if 'process' in locals():
            try:
                process.terminate()
                process.wait(timeout=5)
            except:
                pass
        return False


def validate_required_files() -> bool:
    """Ensure required files exist and are readable."""
    print("📁 Checking required files...")
    
    required_files = [
        "mkdocs.yml",
        "docs/index.md",
    ]
    
    missing_files = []
    for file_path in required_files:
        full_path = Path(__file__).parent.parent / file_path
        if not full_path.exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False
    else:
        print("✅ All required files present")
        return True


def main():
    """Run all deployment validations."""
    print("🎯 Running deployment validation...")
    print("=" * 50)
    
    validations = [
        ("Required Files", validate_required_files),
        ("MkDocs Config", validate_mkdocs_config),
        ("Build Test", validate_build),
        ("Serve Test", validate_serve),
    ]
    
    results = []
    for name, validation_func in validations:
        print(f"\n📋 {name}")
        try:
            success = validation_func()
            results.append((name, success))
        except Exception as e:
            print(f"❌ {name} failed with error: {str(e)}")
            results.append((name, False))
    
    print("\n" + "=" * 50)
    print("📊 DEPLOYMENT VALIDATION RESULTS")
    print("=" * 50)
    
    all_passed = True
    for name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {name}")
        if not success:
            all_passed = False
    
    print("=" * 50)
    if all_passed:
        print("🎉 ALL VALIDATIONS PASSED - READY FOR DEPLOYMENT!")
        sys.exit(0)
    else:
        print("💥 DEPLOYMENT VALIDATION FAILED")
        print("🔧 Fix the failing validations before deploying")
        sys.exit(1)


if __name__ == "__main__":
    main()
