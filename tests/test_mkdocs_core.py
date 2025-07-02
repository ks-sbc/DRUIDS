#!/usr/bin/env python3
"""
Consolidated MkDocs core functionality tests.
Combines tests from test_mkdocs_config.py and test_build.py
"""

import subprocess
from pathlib import Path
import yaml
import pytest
from test_utils import get_project_root, check_command_available, run_command


class TestMkDocsCore:
    """Core MkDocs functionality tests"""
    
    @pytest.fixture(scope="class")
    def project_root(self):
        """Get project root directory"""
        return get_project_root()
    
    @pytest.fixture(scope="class")
    def mkdocs_config_path(self, project_root):
        """Path to mkdocs.yml"""
        return project_root / "mkdocs.yml"
    
    @pytest.fixture(scope="class")
    def docs_dir(self, project_root):
        """Path to docs directory"""
        return project_root / "docs"
    
    @pytest.fixture(scope="class")
    def mkdocs_config(self, mkdocs_config_path):
        """Load and return MkDocs configuration"""
        if not mkdocs_config_path.exists():
            pytest.skip("mkdocs.yml not found")
        
        # Use mkdocs config loader
        import mkdocs.config
        import mkdocs.plugins
        
        config = mkdocs.config.load_config(str(mkdocs_config_path))
        return config
    
    # Essential Tests - Must Pass
    
    @pytest.mark.unit
    def test_mkdocs_yml_exists(self, mkdocs_config_path):
        """Test that mkdocs.yml exists"""
        assert mkdocs_config_path.exists(), "mkdocs.yml not found"
    
    @pytest.mark.unit
    def test_mkdocs_yml_is_valid_yaml(self, mkdocs_config_path):
        """Test that mkdocs.yml is valid YAML"""
        with open(mkdocs_config_path, 'r') as f:
            try:
                config = yaml.safe_load(f)
                assert isinstance(config, dict), "mkdocs.yml should be a dictionary"
                assert 'site_name' in config, "mkdocs.yml must have site_name"
            except yaml.YAMLError as e:
                pytest.fail(f"Invalid YAML: {e}")
    
    @pytest.mark.unit
    def test_required_files_exist(self, project_root, docs_dir):
        """Test that all required files exist"""
        required_files = [
            project_root / "mkdocs.yml",
            project_root / "requirements.txt",
            docs_dir / "index.md",
        ]
        
        for file_path in required_files:
            assert file_path.exists(), f"Required file missing: {file_path}"
    
    @pytest.mark.unit
    def test_config_loads_successfully(self, mkdocs_config):
        """Test that MkDocs config loads without errors"""
        assert mkdocs_config is not None
        assert hasattr(mkdocs_config, 'site_name')
        assert mkdocs_config['site_name']
    
    @pytest.mark.integration
    def test_mkdocs_build_succeeds(self, project_root):
        """Test that mkdocs build --clean succeeds"""
        if not check_command_available("mkdocs"):
            pytest.skip("mkdocs command not available")
        
        success, stdout, stderr = run_command(
            "mkdocs build --clean --site-dir test_site",
            cwd=project_root
        )
        
        # Clean up
        test_site = project_root / "test_site"
        if test_site.exists():
            import shutil
            shutil.rmtree(test_site)
        
        assert success, f"MkDocs build failed:\nSTDOUT: {stdout}\nSTDERR: {stderr}"
    
    @pytest.mark.unit
    def test_site_structure_created(self, project_root):
        """Test that build creates expected structure"""
        # Run a quick build
        if not check_command_available("mkdocs"):
            pytest.skip("mkdocs command not available")
        
        success, _, _ = run_command(
            "mkdocs build --clean --site-dir test_site",
            cwd=project_root
        )
        
        if success:
            site_dir = project_root / "test_site"
            assert site_dir.exists(), "Site directory not created"
            assert (site_dir / "index.html").exists(), "index.html not generated"
            
            # Clean up
            if site_dir.exists():
                import shutil
                shutil.rmtree(site_dir)
    
    @pytest.mark.unit
    def test_theme_configuration(self, mkdocs_config):
        """Test theme configuration validity"""
        theme = mkdocs_config.get("theme", {})
        assert theme.get("name"), "Theme name not specified"
        
        # If using Material theme, check basic config
        if theme.get("name") == "material":
            # Just ensure theme loads, don't check specific icons
            assert isinstance(theme, dict)
    
    @pytest.mark.unit
    def test_plugin_configuration(self, mkdocs_config):
        """Test that required plugins are configured"""
        plugins = mkdocs_config.get("plugins", {})
        
        # Check for essential plugins
        plugin_names = []
        if isinstance(plugins, list):
            plugin_names = [p if isinstance(p, str) else list(p.keys())[0] for p in plugins]
        elif isinstance(plugins, dict):
            plugin_names = list(plugins.keys())
        
        # At minimum, search should be present
        assert any("search" in name for name in plugin_names), "Search plugin not configured"
    
    @pytest.mark.unit
    def test_obsidian_wikilinks_supported(self, mkdocs_config):
        """Test that Obsidian wikilinks are supported"""
        plugins = mkdocs_config.get("plugins", {})
        
        # Check for wikilink-supporting plugin
        has_wikilink_support = False
        plugin_names = []
        
        if isinstance(plugins, dict):
            plugin_names = list(plugins.keys())
        elif isinstance(plugins, list):
            for plugin in plugins:
                if isinstance(plugin, str):
                    plugin_names.append(plugin)
                elif isinstance(plugin, dict):
                    plugin_names.extend(plugin.keys())
        
        wikilink_plugins = ['ezlinks', 'roamlinks', 'wikilinks', 'pub-obsidian']
        for plugin in plugin_names:
            if any(wp in plugin for wp in wikilink_plugins):
                has_wikilink_support = True
                break
        
        assert has_wikilink_support, "No wikilink plugin found in configuration"