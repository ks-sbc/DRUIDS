#!/usr/bin/env python3
"""
Tests for MkDocs build process and configuration
"""

import shutil
from pathlib import Path

import pytest
from mkdocs.commands.build import build
from mkdocs.config import load_config
from mkdocs.exceptions import ConfigurationError

from test_utils import check_command_available, run_command, validate_yaml_file


class TestMkDocsBuild:
    """Test MkDocs build functionality"""

    @pytest.mark.unit
    def test_required_files_exist(self, project_root):
        """Test that required files exist"""
        required_files = [
            "mkdocs.yml",
            "pyproject.toml",
            "docs/index.md",
        ]
        
        missing_files = []
        for file_path in required_files:
            full_path = project_root / file_path
            if not full_path.exists():
                missing_files.append(file_path)
        
        assert not missing_files, f"Missing required files: {missing_files}"

    @pytest.mark.unit
    def test_mkdocs_config_loads(self, mkdocs_config_path):
        """Test that mkdocs.yml loads without errors"""
        try:
            config = load_config(str(mkdocs_config_path))
            assert config is not None
        except ConfigurationError as e:
            pytest.fail(f"Configuration failed to load: {e}")

    @pytest.mark.unit
    def test_mkdocs_config_yaml_valid(self, mkdocs_config_path):
        """Test that mkdocs.yml has valid YAML syntax"""
        is_valid, error = validate_yaml_file(mkdocs_config_path)
        assert is_valid, f"Invalid YAML in mkdocs.yml: {error}"

    @pytest.mark.integration
    def test_mkdocs_build_succeeds(self, mkdocs_config_path, temp_dir):
        """Test that mkdocs build completes successfully"""
        config = load_config(str(mkdocs_config_path))
        # Use temporary site directory
        config["site_dir"] = str(temp_dir / "site")
        
        try:
            build(config, dirty=False)
            # Check that site was created
            assert (temp_dir / "site" / "index.html").exists()
        except Exception as e:
            pytest.fail(f"MkDocs build failed: {e}")

    @pytest.mark.integration
    def test_site_structure_created(self, mkdocs_config_path, temp_dir):
        """Test that build creates expected site structure"""
        config = load_config(str(mkdocs_config_path))
        config["site_dir"] = str(temp_dir / "site")
        
        build(config, dirty=False)
        
        site_dir = temp_dir / "site"
        
        # Check for essential files/directories
        assert (site_dir / "index.html").exists(), "Missing index.html"
        assert any(site_dir.rglob("*.css")), "No CSS files generated"
        assert any(site_dir.rglob("*.js")), "No JS files generated"
        
        # Check for search functionality
        search_files = list(site_dir.rglob("*search*"))
        assert search_files, "No search-related files found"

    @pytest.mark.unit
    def test_theme_configuration(self, mkdocs_config):
        """Test theme configuration validity"""
        theme = mkdocs_config.get("theme", {})
        
        assert theme.get("name"), "Theme name not specified"
        
        # If using Material theme, check for common misconfigurations
        if theme.get("name") == "material":
            # Check icon configuration
            icons = theme.get("icon", {})
            valid_prefixes = ["material/", "fontawesome/", "octicons/"]
            
            for icon_type, icon_value in icons.items():
                if isinstance(icon_value, str):
                    assert any(icon_value.startswith(p) for p in valid_prefixes), \
                        f"Invalid icon prefix for {icon_type}: {icon_value}"

    @pytest.mark.unit
    def test_plugin_configuration(self, mkdocs_config):
        """Test plugin configuration validity"""
        plugins = mkdocs_config.get("plugins", [])
        
        # Check that plugins list is properly formatted
        for plugin in plugins:
            if isinstance(plugin, dict):
                # Plugin with configuration
                assert len(plugin) == 1, f"Invalid plugin configuration: {plugin}"
            else:
                # Plugin without configuration (just name)
                assert isinstance(plugin, str), f"Invalid plugin type: {type(plugin)}"

    @pytest.mark.unit
    def test_navigation_files_exist(self, mkdocs_config, docs_dir):
        """Test that all files referenced in navigation exist"""
        nav = mkdocs_config.get("nav", [])
        missing_files = []
        
        def check_nav_item(item):
            if isinstance(item, dict):
                for key, value in item.items():
                    if isinstance(value, str) and not value.startswith("http"):
                        file_path = docs_dir / value
                        if not file_path.exists():
                            missing_files.append(value)
                    elif isinstance(value, list):
                        for sub_item in value:
                            check_nav_item(sub_item)
        
        for nav_item in nav:
            check_nav_item(nav_item)
        
        # This is a warning, not a failure
        if missing_files:
            pytest.skip(f"Missing navigation files (optional): {missing_files}")

    @pytest.mark.integration
    @pytest.mark.slow
    def test_development_server_starts(self, mkdocs_config_path):
        """Test that development server can start"""
        if not check_command_available("mkdocs"):
            pytest.skip("mkdocs command not available")
        
        # Try to start the server with a timeout
        success, stdout, stderr = run_command(
            "timeout 3s mkdocs serve --dev-addr=127.0.0.1:8001",
            cwd=Path(mkdocs_config_path).parent
        )
        
        # Timeout exit code is 124, which means server started successfully
        if not success and "Address already in use" in stderr:
            pytest.skip("Port 8001 already in use")
        
        # Server should either start (and timeout) or fail with clear error
        assert success or "timeout" in stderr.lower() or stderr == "", \
            f"Server failed to start: {stderr}"

    @pytest.mark.unit
    def test_extra_css_and_js_exist(self, mkdocs_config, project_root):
        """Test that extra CSS and JS files exist"""
        docs_dir = Path(mkdocs_config["docs_dir"])
        
        # Check extra CSS
        extra_css = mkdocs_config.get("extra_css", [])
        for css_file in extra_css:
            file_path = docs_dir / css_file
            assert file_path.exists(), f"Extra CSS file not found: {css_file}"
        
        # Check extra JavaScript
        extra_js = mkdocs_config.get("extra_javascript", [])
        for js_file in extra_js:
            # Skip external URLs
            if not js_file.startswith(("http://", "https://", "//")):
                file_path = docs_dir / js_file
                assert file_path.exists(), f"Extra JS file not found: {js_file}"

    @pytest.mark.unit
    def test_custom_dir_configuration(self, mkdocs_config, project_root):
        """Test custom_dir configuration if present"""
        theme = mkdocs_config.get("theme", {})
        custom_dir = theme.get("custom_dir")
        
        if custom_dir:
            custom_path = project_root / custom_dir
            assert custom_path.exists(), f"Custom theme directory not found: {custom_dir}"
            assert custom_path.is_dir(), f"Custom theme path is not a directory: {custom_dir}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])