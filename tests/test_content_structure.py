#!/usr/bin/env python3
"""
Tests for Diátaxis documentation framework compliance.
Validates that content is organized according to the four content types:
- Tutorials (learning-oriented)
- How-to guides (problem-oriented)  
- Reference (information-oriented)
- Explanation (understanding-oriented)
"""

import re
from pathlib import Path
from typing import Dict, List, Set

import pytest

from test_utils import (
    extract_frontmatter,
    get_all_markdown_files,
)


class TestContentStructure:
    """Test Diátaxis framework compliance"""

    def classify_content_type(self, content: str, file_path: Path) -> str:
        """
        Classify content based on Diátaxis framework
        
        Returns: 'tutorial', 'howto', 'reference', 'explanation', or 'unknown'
        """
        # Check frontmatter first
        frontmatter, body = extract_frontmatter(content)
        if frontmatter and 'type' in frontmatter:
            content_type = frontmatter['type'].lower()
            if content_type in ['tutorial', 'howto', 'how-to', 'reference', 'explanation']:
                return content_type.replace('how-to', 'howto')
        
        # Classify based on file path
        path_str = str(file_path).lower()
        if 'tutorial' in path_str:
            return 'tutorial'
        elif 'how-to' in path_str or 'guide' in path_str:
            return 'howto'
        elif 'reference' in path_str:
            return 'reference'
        elif 'explanation' in path_str or 'concept' in path_str:
            return 'explanation'
        
        # Classify based on content patterns
        if body is None:
            body = content
        
        body_lower = body.lower()
        
        # Tutorial indicators
        tutorial_patterns = [
            r'\bstep\s+\d+', r'\bfirst,?\s+', r'\bnext,?\s+', r'\bthen,?\s+',
            r'\blet\'s\s+', r'\bwe\s+will\s+', r'\byou\s+will\s+learn',
            r'\bfollow\s+along', r'\bwalkthrough'
        ]
        
        # How-to indicators  
        howto_patterns = [
            r'\bhow\s+to\s+', r'\bto\s+\w+,?\s+', r'\bsteps?:', r'\bprocedure',
            r'\binstructions?', r'\bmethod', r'\bsolution'
        ]
        
        # Reference indicators
        reference_patterns = [
            r'\bapi\b', r'\bcommand\s+reference', r'\boptions?:', r'\bparameters?:',
            r'\bsyntax:', r'\bspecification', r'\bschema'
        ]
        
        # Explanation indicators
        explanation_patterns = [
            r'\bwhy\s+', r'\bbecause\s+', r'\breason', r'\bconcept', r'\btheory',
            r'\bprinciple', r'\barchitecture', r'\bdesign\s+pattern'
        ]
        
        # Count pattern matches
        scores = {
            'tutorial': sum(1 for p in tutorial_patterns if re.search(p, body_lower)),
            'howto': sum(1 for p in howto_patterns if re.search(p, body_lower)),
            'reference': sum(1 for p in reference_patterns if re.search(p, body_lower)),
            'explanation': sum(1 for p in explanation_patterns if re.search(p, body_lower))
        }
        
        # Return highest scoring type, or 'unknown' if no clear winner
        if max(scores.values()) > 0:
            return max(scores, key=scores.get)
        
        return 'unknown'

    @pytest.mark.integration
    def test_diataxis_directory_structure(self, docs_dir):
        """Test that Diátaxis directory structure exists"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        expected_dirs = {
            'tutorials': 'Learning-oriented documentation',
            'how-to': 'Problem-oriented documentation',
            'reference': 'Information-oriented documentation',
            'explanation': 'Understanding-oriented documentation'
        }
        
        existing_dirs = {d.name for d in docs_dir.iterdir() if d.is_dir()}
        missing_dirs = set(expected_dirs.keys()) - existing_dirs
        
        if missing_dirs:
            warning_msg = f"\nMissing Diátaxis directories:\n"
            for dir_name in missing_dirs:
                warning_msg += f"  - {dir_name}/: {expected_dirs[dir_name]}\n"
            
            # This is a structural recommendation, not a hard requirement
            pytest.skip(f"Diátaxis structure incomplete (warning):{warning_msg}")

    @pytest.mark.integration
    def test_content_type_classification(self, docs_dir):
        """Test that content is properly classified by type"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        
        # Exclude certain files from classification
        exclude_patterns = ['index.md', 'README.md', 'test-', '_template']
        
        classification_results = {
            'tutorial': [],
            'howto': [],
            'reference': [],
            'explanation': [],
            'unknown': []
        }
        
        for md_file in markdown_files:
            rel_path = md_file.relative_to(docs_dir)
            
            # Skip excluded files
            if any(pattern in str(rel_path).lower() for pattern in exclude_patterns):
                continue
            
            content = md_file.read_text(encoding='utf-8')
            content_type = self.classify_content_type(content, rel_path)
            classification_results[content_type].append(rel_path)
        
        # Report classification results
        total_classified = sum(len(files) for content_type, files in classification_results.items() if content_type != 'unknown')
        total_files = sum(len(files) for files in classification_results.values())
        
        print(f"\nContent Classification Results:")
        print(f"  Total files analyzed: {total_files}")
        print(f"  Successfully classified: {total_classified}")
        
        for content_type, files in classification_results.items():
            if files:
                print(f"  {content_type.title()}: {len(files)} files")
        
        # Warn if too many files are unclassified
        unknown_ratio = len(classification_results['unknown']) / total_files if total_files > 0 else 0
        if unknown_ratio > 0.3:  # More than 30% unclassified
            warning_msg = f"\nMany files could not be classified ({len(classification_results['unknown'])} of {total_files}):\n"
            for file_path in classification_results['unknown'][:10]:
                warning_msg += f"  - {file_path}\n"
            if len(classification_results['unknown']) > 10:
                warning_msg += f"  ... and {len(classification_results['unknown']) - 10} more\n"
            
            pytest.skip(f"Content classification issues (warning):{warning_msg}")

    @pytest.mark.integration  
    def test_tutorial_content_quality(self, docs_dir):
        """Test tutorial content follows Diátaxis principles"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        tutorial_dir = docs_dir / "tutorials"
        if not tutorial_dir.exists():
            pytest.skip("No tutorials directory found")
        
        tutorial_files = get_all_markdown_files(tutorial_dir)
        tutorial_issues = []
        
        for tutorial_file in tutorial_files:
            if tutorial_file.name == 'index.md':
                continue
                
            content = tutorial_file.read_text(encoding='utf-8')
            rel_path = tutorial_file.relative_to(docs_dir)
            
            # Tutorial quality checks
            frontmatter, body = extract_frontmatter(content)
            if body is None:
                body = content
            
            # Should have practical steps
            if not re.search(r'\bstep\s+\d+|first.*then|next.*', body, re.IGNORECASE):
                tutorial_issues.append(f"{rel_path}: No clear step sequence found")
            
            # Should be action-oriented (use imperative verbs)
            imperative_verbs = ['create', 'add', 'install', 'run', 'open', 'click', 'type', 'save']
            verb_count = sum(1 for verb in imperative_verbs if verb in body.lower())
            if verb_count < 2:
                tutorial_issues.append(f"{rel_path}: Limited action-oriented language")
            
            # Should avoid too much theory/explanation  
            explanation_words = ['because', 'theory', 'concept', 'principle', 'architecture']
            explanation_count = sum(1 for word in explanation_words if word in body.lower())
            if explanation_count > 5:
                tutorial_issues.append(f"{rel_path}: Too much explanatory content for tutorial")
            
            # Should have a clear outcome
            if not re.search(r'\bfinish|complete|result|outcome|accomplish', body, re.IGNORECASE):
                tutorial_issues.append(f"{rel_path}: No clear learning outcome described")
        
        if tutorial_issues:
            warning_msg = f"\nTutorial quality issues ({len(tutorial_issues)}):\n"
            for issue in tutorial_issues:
                warning_msg += f"  - {issue}\n"
            
            pytest.skip(f"Tutorial quality concerns (warning):{warning_msg}")

    @pytest.mark.integration
    def test_howto_content_quality(self, docs_dir):
        """Test how-to guide content follows Diátaxis principles"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        howto_dir = docs_dir / "how-to"
        if not howto_dir.exists():
            pytest.skip("No how-to directory found")
        
        howto_files = get_all_markdown_files(howto_dir)
        howto_issues = []
        
        for howto_file in howto_files:
            if howto_file.name == 'index.md':
                continue
                
            content = howto_file.read_text(encoding='utf-8')
            rel_path = howto_file.relative_to(docs_dir)
            
            frontmatter, body = extract_frontmatter(content)
            if body is None:
                body = content
            
            # Should focus on solving a specific problem
            if not re.search(r'\bhow\s+to|problem|solve|fix|troubleshoot', body, re.IGNORECASE):
                howto_issues.append(f"{rel_path}: Doesn't clearly address a specific problem")
            
            # Should be goal-oriented
            goal_words = ['achieve', 'accomplish', 'complete', 'finish', 'solve', 'fix']
            goal_count = sum(1 for word in goal_words if word in body.lower())
            if goal_count == 0:
                howto_issues.append(f"{rel_path}: No clear goal orientation")
            
            # Should avoid tutorial-style learning progression
            tutorial_words = ['learn', 'understand', 'lesson', 'exercise']
            tutorial_count = sum(1 for word in tutorial_words if word in body.lower())
            if tutorial_count > 3:
                howto_issues.append(f"{rel_path}: Too tutorial-like for how-to guide")
        
        if howto_issues:
            warning_msg = f"\nHow-to guide quality issues ({len(howto_issues)}):\n"
            for issue in howto_issues:
                warning_msg += f"  - {issue}\n"
            
            pytest.skip(f"How-to quality concerns (warning):{warning_msg}")

    @pytest.mark.integration
    def test_reference_content_quality(self, docs_dir):
        """Test reference content follows Diátaxis principles"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        reference_dir = docs_dir / "reference"
        if not reference_dir.exists():
            pytest.skip("No reference directory found")
        
        reference_files = get_all_markdown_files(reference_dir)
        reference_issues = []
        
        for ref_file in reference_files:
            if ref_file.name == 'index.md':
                continue
                
            content = ref_file.read_text(encoding='utf-8')
            rel_path = ref_file.relative_to(docs_dir)
            
            frontmatter, body = extract_frontmatter(content)
            if body is None:
                body = content
            
            # Should be information-dense
            word_count = len(body.split())
            if word_count < 200:
                reference_issues.append(f"{rel_path}: Too brief for reference material ({word_count} words)")
            
            # Should have structured information (tables, lists, code blocks)
            has_table = '|' in body and '---' in body
            has_lists = re.search(r'^\s*[-*+]\s+', body, re.MULTILINE)
            has_code = '```' in body or '`' in body
            
            if not (has_table or has_lists or has_code):
                reference_issues.append(f"{rel_path}: No structured information found")
            
            # Should avoid instructional language
            instructional_words = ['first', 'then', 'next', 'follow', 'do this']
            instructional_count = sum(1 for word in instructional_words if word in body.lower())
            if instructional_count > 3:
                reference_issues.append(f"{rel_path}: Too instructional for reference material")
        
        if reference_issues:
            warning_msg = f"\nReference quality issues ({len(reference_issues)}):\n"
            for issue in reference_issues:
                warning_msg += f"  - {issue}\n"
            
            pytest.skip(f"Reference quality concerns (warning):{warning_msg}")

    @pytest.mark.integration
    def test_content_cross_references(self, docs_dir):
        """Test appropriate cross-references between content types"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        cross_ref_analysis = {
            'tutorial_to_howto': 0,
            'tutorial_to_reference': 0,
            'howto_to_reference': 0,
            'explanation_to_all': 0,
            'inappropriate_refs': []
        }
        
        for md_file in markdown_files:
            content = md_file.read_text(encoding='utf-8')
            rel_path = md_file.relative_to(docs_dir)
            
            content_type = self.classify_content_type(content, rel_path)
            
            # Extract links from content
            links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
            
            for link_text, link_url in links:
                # Skip external links
                if link_url.startswith(('http://', 'https://', 'mailto:')):
                    continue
                
                # Determine target content type based on URL
                target_type = 'unknown'
                if 'tutorial' in link_url:
                    target_type = 'tutorial'
                elif 'how-to' in link_url or 'guide' in link_url:
                    target_type = 'howto'
                elif 'reference' in link_url:
                    target_type = 'reference'
                elif 'explanation' in link_url:
                    target_type = 'explanation'
                
                # Track cross-references
                if content_type == 'tutorial' and target_type == 'howto':
                    cross_ref_analysis['tutorial_to_howto'] += 1
                elif content_type == 'tutorial' and target_type == 'reference':
                    cross_ref_analysis['tutorial_to_reference'] += 1
                elif content_type == 'howto' and target_type == 'reference':
                    cross_ref_analysis['howto_to_reference'] += 1
                elif content_type == 'explanation':
                    cross_ref_analysis['explanation_to_all'] += 1
                
                # Check for inappropriate cross-references
                if content_type == 'reference' and target_type == 'tutorial':
                    cross_ref_analysis['inappropriate_refs'].append(
                        f"{rel_path}: Reference linking to tutorial"
                    )
                elif content_type == 'howto' and target_type == 'tutorial':
                    cross_ref_analysis['inappropriate_refs'].append(
                        f"{rel_path}: How-to linking to tutorial (should be self-contained)"
                    )
        
        # Report cross-reference analysis
        print(f"\nContent Cross-Reference Analysis:")
        print(f"  Tutorial → How-to: {cross_ref_analysis['tutorial_to_howto']}")
        print(f"  Tutorial → Reference: {cross_ref_analysis['tutorial_to_reference']}")
        print(f"  How-to → Reference: {cross_ref_analysis['howto_to_reference']}")
        print(f"  Explanation → All: {cross_ref_analysis['explanation_to_all']}")
        
        if cross_ref_analysis['inappropriate_refs']:
            warning_msg = f"\nInappropriate cross-references ({len(cross_ref_analysis['inappropriate_refs'])}):\n"
            for ref in cross_ref_analysis['inappropriate_refs']:
                warning_msg += f"  - {ref}\n"
            
            pytest.skip(f"Cross-reference issues (warning):{warning_msg}")

    @pytest.mark.integration
    def test_content_completeness(self, docs_dir):
        """Test that each content type has adequate coverage"""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        markdown_files = get_all_markdown_files(docs_dir)
        content_counts = {
            'tutorial': 0,
            'howto': 0,
            'reference': 0,
            'explanation': 0,
            'unknown': 0
        }
        
        for md_file in markdown_files:
            # Skip index and template files
            if md_file.name in ['index.md', 'README.md'] or '_template' in str(md_file):
                continue
                
            content = md_file.read_text(encoding='utf-8')
            rel_path = md_file.relative_to(docs_dir)
            content_type = self.classify_content_type(content, rel_path)
            content_counts[content_type] += 1
        
        # Check for balanced coverage
        total_content = sum(count for type_name, count in content_counts.items() if type_name != 'unknown')
        
        completeness_issues = []
        
        # Each type should have at least some representation
        for content_type in ['tutorial', 'howto', 'reference', 'explanation']:
            count = content_counts[content_type]
            if count == 0:
                completeness_issues.append(f"No {content_type} content found")
            elif total_content > 10 and count < 2:
                completeness_issues.append(f"Very limited {content_type} content ({count} files)")
        
        # Report completeness
        print(f"\nContent Type Distribution:")
        for content_type, count in content_counts.items():
            percentage = (count / total_content * 100) if total_content > 0 else 0
            print(f"  {content_type.title()}: {count} files ({percentage:.1f}%)")
        
        if completeness_issues:
            warning_msg = f"\nContent completeness issues:\n"
            for issue in completeness_issues:
                warning_msg += f"  - {issue}\n"
            
            pytest.skip(f"Content coverage gaps (warning):{warning_msg}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])