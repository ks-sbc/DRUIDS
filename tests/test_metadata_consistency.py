#!/usr/bin/env python3
"""
Test DRUIDS metadata consistency across all documentation files.
Following TDD principles: behavior-focused, isolated, fast, meaningful.
"""

import pytest
from pathlib import Path
import yaml
import re
from datetime import datetime
from typing import Dict, List, Set, Optional, Tuple


class TestMetadataConsistency:
    """Test that all DRUIDS documents follow metadata standards."""
    
    @pytest.fixture
    def docs_path(self) -> Path:
        """Provide the documentation root path."""
        return Path(__file__).parent.parent / "docs"
    
    @pytest.fixture
    def required_metadata_fields(self) -> Set[str]:
        """Define required metadata fields per DRUIDS standards."""
        return {
            "title",
            "description", 
            "created",
            "updated",
            "type",
            "security",
            "version",
            "document_id",
            "tags",
            "draft",
            "author"
        }
    
    @pytest.fixture
    def valid_security_levels(self) -> Set[str]:
        """Define valid security classification levels."""
        return {"L0", "L1", "L2"}
    
    @pytest.fixture
    def valid_document_types(self) -> Set[str]:
        """Define valid DRUIDS document types."""
        return {
            "docs/how-to",
            "docs/tutorial", 
            "docs/reference",
            "docs/explanation",
            "blog/post",
            "blog/announcement"
        }
    
    @pytest.fixture
    def document_id_pattern(self) -> re.Pattern:
        """Define the DRUIDS document ID format pattern."""
        return re.compile(r'^[A-Z]{3}-[A-Z]{2,4}-\d{4}-\d{3}-L[0-2]$')
    
    def test_all_markdown_files_have_frontmatter(self, docs_path: Path):
        """Every markdown file should have YAML frontmatter."""
        files_without_frontmatter = []
        
        for md_file in docs_path.rglob("*.md"):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if not content.startswith('---\n'):
                    files_without_frontmatter.append(str(md_file.relative_to(docs_path)))
        
        assert not files_without_frontmatter, \
            f"Files missing frontmatter: {files_without_frontmatter}"
    
    def test_all_documents_have_required_metadata(self, docs_path: Path, required_metadata_fields: Set[str]):
        """Every document should have all required metadata fields."""
        incomplete_metadata = {}
        
        for md_file in docs_path.rglob("*.md"):
            metadata = self._extract_metadata(md_file)
            if metadata:
                missing_fields = required_metadata_fields - set(metadata.keys())
                if missing_fields:
                    incomplete_metadata[str(md_file.relative_to(docs_path))] = list(missing_fields)
        
        assert not incomplete_metadata, \
            f"Documents with missing metadata fields: {incomplete_metadata}"
    
    def test_security_levels_are_valid(self, docs_path: Path, valid_security_levels: Set[str]):
        """All documents should use valid security classification levels."""
        invalid_security = {}
        
        for md_file in docs_path.rglob("*.md"):
            metadata = self._extract_metadata(md_file)
            if metadata and 'security' in metadata:
                if metadata['security'] not in valid_security_levels:
                    invalid_security[str(md_file.relative_to(docs_path))] = metadata['security']
        
        assert not invalid_security, \
            f"Documents with invalid security levels: {invalid_security}"
    
    def test_document_types_are_valid(self, docs_path: Path, valid_document_types: Set[str]):
        """All documents should use valid DRUIDS document types."""
        invalid_types = {}
        
        for md_file in docs_path.rglob("*.md"):
            metadata = self._extract_metadata(md_file)
            if metadata and 'type' in metadata:
                if metadata['type'] not in valid_document_types:
                    invalid_types[str(md_file.relative_to(docs_path))] = metadata['type']
        
        assert not invalid_types, \
            f"Documents with invalid types: {invalid_types}"
    
    def test_document_ids_follow_pattern(self, docs_path: Path, document_id_pattern: re.Pattern):
        """All document IDs should follow the DRUIDS naming convention."""
        invalid_ids = {}
        
        for md_file in docs_path.rglob("*.md"):
            metadata = self._extract_metadata(md_file)
            if metadata and 'document_id' in metadata:
                if not document_id_pattern.match(metadata['document_id']):
                    invalid_ids[str(md_file.relative_to(docs_path))] = metadata['document_id']
        
        assert not invalid_ids, \
            f"Documents with invalid ID format: {invalid_ids}"
    
    def test_dates_are_valid_iso_format(self, docs_path: Path):
        """Created and updated dates should be valid ISO format dates."""
        invalid_dates = {}
        
        for md_file in docs_path.rglob("*.md"):
            metadata = self._extract_metadata(md_file)
            if metadata:
                date_errors = []
                for field in ['created', 'updated']:
                    if field in metadata:
                        try:
                            datetime.fromisoformat(str(metadata[field]))
                        except (ValueError, TypeError):
                            date_errors.append(f"{field}: {metadata[field]}")
                
                if date_errors:
                    invalid_dates[str(md_file.relative_to(docs_path))] = date_errors
        
        assert not invalid_dates, \
            f"Documents with invalid date formats: {invalid_dates}"
    
    def test_updated_date_not_before_created_date(self, docs_path: Path):
        """Updated date should never be before created date."""
        temporal_violations = {}
        
        for md_file in docs_path.rglob("*.md"):
            metadata = self._extract_metadata(md_file)
            if metadata and 'created' in metadata and 'updated' in metadata:
                try:
                    created = datetime.fromisoformat(str(metadata['created']))
                    updated = datetime.fromisoformat(str(metadata['updated']))
                    if updated < created:
                        temporal_violations[str(md_file.relative_to(docs_path))] = {
                            'created': metadata['created'],
                            'updated': metadata['updated']
                        }
                except (ValueError, TypeError):
                    pass  # Invalid dates caught by other test
        
        assert not temporal_violations, \
            f"Documents with updated date before created date: {temporal_violations}"
    
    def test_tags_are_lowercase_with_hyphens(self, docs_path: Path):
        """All tags should be lowercase with hyphens for consistency."""
        invalid_tags = {}
        tag_pattern = re.compile(r'^[a-z0-9-]+$')
        
        for md_file in docs_path.rglob("*.md"):
            metadata = self._extract_metadata(md_file)
            if metadata and 'tags' in metadata and isinstance(metadata['tags'], list):
                bad_tags = [tag for tag in metadata['tags'] if not tag_pattern.match(tag)]
                if bad_tags:
                    invalid_tags[str(md_file.relative_to(docs_path))] = bad_tags
        
        assert not invalid_tags, \
            f"Documents with invalid tag format: {invalid_tags}"
    
    def test_draft_status_is_boolean(self, docs_path: Path):
        """Draft status should be a boolean value."""
        invalid_draft_status = {}
        
        for md_file in docs_path.rglob("*.md"):
            metadata = self._extract_metadata(md_file)
            if metadata and 'draft' in metadata:
                if not isinstance(metadata['draft'], bool):
                    invalid_draft_status[str(md_file.relative_to(docs_path))] = metadata['draft']
        
        assert not invalid_draft_status, \
            f"Documents with non-boolean draft status: {invalid_draft_status}"
    
    def test_version_follows_semver(self, docs_path: Path):
        """Version should follow semantic versioning format."""
        invalid_versions = {}
        semver_pattern = re.compile(r'^\d+\.\d+\.\d+(-[a-zA-Z0-9-]+)?$')
        
        for md_file in docs_path.rglob("*.md"):
            metadata = self._extract_metadata(md_file)
            if metadata and 'version' in metadata:
                if not semver_pattern.match(str(metadata['version'])):
                    invalid_versions[str(md_file.relative_to(docs_path))] = metadata['version']
        
        assert not invalid_versions, \
            f"Documents with invalid version format: {invalid_versions}"
    
    def test_no_duplicate_document_ids(self, docs_path: Path):
        """Document IDs should be unique across the entire documentation."""
        id_to_files: Dict[str, List[str]] = {}
        
        for md_file in docs_path.rglob("*.md"):
            metadata = self._extract_metadata(md_file)
            if metadata and 'document_id' in metadata:
                doc_id = metadata['document_id']
                if doc_id not in id_to_files:
                    id_to_files[doc_id] = []
                id_to_files[doc_id].append(str(md_file.relative_to(docs_path)))
        
        duplicates = {doc_id: files for doc_id, files in id_to_files.items() if len(files) > 1}
        
        assert not duplicates, \
            f"Duplicate document IDs found: {duplicates}"
    
    def test_security_level_matches_document_id(self, docs_path: Path):
        """Security level in metadata should match the level in document ID."""
        mismatches = {}
        
        for md_file in docs_path.rglob("*.md"):
            metadata = self._extract_metadata(md_file)
            if metadata and 'security' in metadata and 'document_id' in metadata:
                security_level = metadata['security']
                doc_id = metadata['document_id']
                if doc_id.endswith(f"-{security_level}"):
                    continue  # Matches correctly
                else:
                    mismatches[str(md_file.relative_to(docs_path))] = {
                        'security': security_level,
                        'document_id': doc_id
                    }
        
        assert not mismatches, \
            f"Security level mismatches between metadata and document ID: {mismatches}"
    
    def _extract_metadata(self, file_path: Path) -> Optional[Dict]:
        """Extract YAML frontmatter from a markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if content.startswith('---\n'):
                    end_index = content.find('\n---\n', 4)
                    if end_index != -1:
                        yaml_content = content[4:end_index]
                        return yaml.safe_load(yaml_content)
        except Exception:
            pass
        return None


class TestMetadataIntegration:
    """Integration tests for metadata consistency across the system."""
    
    def test_blog_posts_have_consistent_metadata_structure(self, docs_path: Path):
        """All blog posts should follow the same metadata structure."""
        blog_path = docs_path / "blog" / "posts"
        if not blog_path.exists():
            pytest.skip("No blog directory found")
        
        metadata_structures = {}
        for md_file in blog_path.glob("*.md"):
            metadata = self._extract_metadata(md_file)
            if metadata:
                structure = tuple(sorted(metadata.keys()))
                if structure not in metadata_structures:
                    metadata_structures[structure] = []
                metadata_structures[structure].append(str(md_file.name))
        
        assert len(metadata_structures) <= 1, \
            f"Inconsistent blog metadata structures: {metadata_structures}"
    
    def test_tutorial_documents_have_navigation_order(self, docs_path: Path):
        """Tutorial documents should have navigation_order for proper sequencing."""
        tutorials_path = docs_path / "tutorials"
        if not tutorials_path.exists():
            pytest.skip("No tutorials directory found")
        
        missing_nav_order = []
        for md_file in tutorials_path.rglob("*.md"):
            metadata = self._extract_metadata(md_file)
            if metadata and 'navigation_order' not in metadata:
                missing_nav_order.append(str(md_file.relative_to(docs_path)))
        
        assert not missing_nav_order, \
            f"Tutorial documents missing navigation_order: {missing_nav_order}"
    
    def _extract_metadata(self, file_path: Path) -> Optional[Dict]:
        """Extract YAML frontmatter from a markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if content.startswith('---\n'):
                    end_index = content.find('\n---\n', 4)
                    if end_index != -1:
                        yaml_content = content[4:end_index]
                        return yaml.safe_load(yaml_content)
        except Exception:
            pass
        return None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])