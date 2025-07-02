#!/usr/bin/env python3
"""
Simplified deployment readiness test - single file, no complex imports
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd):
    """Run a command and return success status and output"""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)


def test_mkdocs_build():
    """Test if MkDocs can build successfully"""
    print("🏗️  Testing MkDocs build...")
    success, stdout, stderr = run_command("mkdocs build --clean --strict")
    
    if success:
        print("✅ MkDocs build successful")
        return True
    else:
        print("❌ MkDocs build failed")
        print("STDOUT:", stdout)
        print("STDERR:", stderr)
        return False


def test_mkdocs_serve():
    """Test if MkDocs serve starts (quick check)"""
    print("🚀 Testing MkDocs serve...")
    # Use timeout to prevent hanging
    cmd = "timeout 2 mkdocs serve -a localhost:8002"
    success, stdout, stderr = run_command(cmd)
    
    # Timeout exit code is 124, which is expected
    if "Serving on" in stdout or "Serving on" in stderr:
        print("✅ MkDocs serve can start")
        return True
    else:
        print("❌ MkDocs serve failed to start")
        return False


def test_yaml_valid():
    """Test if mkdocs.yml is valid YAML"""
    print("📝 Testing YAML validity...")
    success, stdout, stderr = run_command("python -c 'import yaml; yaml.safe_load(open(\"mkdocs.yml\"))'")
    
    if success:
        print("✅ YAML is valid")
        return True
    else:
        print("❌ YAML is invalid")
        print("Error:", stderr)
        return False


def test_required_files():
    """Test if required files exist"""
    print("📁 Checking required files...")
    required_files = [
        "mkdocs.yml",
        "docs/index.md",
        "requirements.txt",
        "package.json"
    ]
    
    all_exist = True
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path} not found")
            all_exist = False
    
    return all_exist


def test_obsidian_compatibility():
    """Test basic Obsidian compatibility"""
    print("🔗 Testing Obsidian compatibility...")
    
    # Check if any markdown files have wikilinks
    docs_dir = Path("docs")
    has_wikilinks = False
    
    for md_file in docs_dir.rglob("*.md"):
        content = md_file.read_text(encoding='utf-8')
        if "[[" in content and "]]" in content:
            has_wikilinks = True
            print(f"  Found wikilinks in: {md_file}")
    
    if has_wikilinks:
        # Test if build still works with wikilinks
        success, _, _ = run_command("mkdocs build --clean")
        if success:
            print("✅ Wikilinks don't break build")
            return True
        else:
            print("❌ Wikilinks break build")
            return False
    else:
        print("ℹ️  No wikilinks found to test")
        return True


def main():
    """Run all deployment tests"""
    print("🎯 Running deployment readiness tests...\n")
    
    tests = [
        ("YAML Validity", test_yaml_valid),
        ("Required Files", test_required_files),
        ("MkDocs Build", test_mkdocs_build),
        ("MkDocs Serve", test_mkdocs_serve),
        ("Obsidian Compatibility", test_obsidian_compatibility),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            passed = test_func()
            results.append((test_name, passed))
        except Exception as e:
            print(f"❌ {test_name} errored: {e}")
            results.append((test_name, False))
        print()  # Empty line between tests
    
    # Summary
    print("\n" + "="*50)
    print("📊 DEPLOYMENT READINESS SUMMARY")
    print("="*50)
    
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{test_name}: {status}")
        if not passed:
            all_passed = False
    
    print("="*50)
    
    if all_passed:
        print("✅ All tests passed! Ready for deployment.")
        return 0
    else:
        print("❌ Some tests failed. Fix issues before deployment.")
        return 1


if __name__ == "__main__":
    sys.exit(main())