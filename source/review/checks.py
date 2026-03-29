"""
Review Checks
Individual check implementations
"""

from typing import Dict, Any, List, Set
from .models import ReviewIssue, Severity, CheckType


class BaseCheck:
    """Base class for checks"""
    
    def check(self, report_data: Dict[str, Any]) -> List[ReviewIssue]:
        """
        Run check on report data
        
        Args:
            report_data: Report data dictionary
            
        Returns:
            List of issues found
        """
        raise NotImplementedError


class RequiredSectionsCheck(BaseCheck):
    """Check for missing required sections"""
    
    REQUIRED_SECTIONS = {
        'thesis': ['cover', 'acknowledgment', 'toc', 'chapter', 'conclusion', 'references'],
        'technical_report': ['cover', 'toc', 'chapter', 'conclusion', 'references'],
        'project_report': ['cover', 'toc', 'chapter', 'conclusion', 'references'],
        'business_report': ['cover', 'chapter', 'conclusion']
    }
    
    def check(self, report_data: Dict[str, Any]) -> List[ReviewIssue]:
        issues = []
        
        metadata = report_data.get('metadata', {})
        report_type = metadata.get('report_type', 'project_report')
        
        required = self.REQUIRED_SECTIONS.get(report_type, self.REQUIRED_SECTIONS['project_report'])
        
        sections = report_data.get('sections', [])
        section_types = {s.get('type') for s in sections}
        
        for req_type in required:
            if req_type not in section_types:
                issues.append(ReviewIssue(
                    check_type=CheckType.STRUCTURE,
                    severity=Severity.ERROR,
                    message=f"Missing required section: {req_type}",
                    details={'required_type': req_type, 'report_type': report_type}
                ))
        
        return issues


class HeadingNumberingCheck(BaseCheck):
    """Check heading numbering consistency"""
    
    def check(self, report_data: Dict[str, Any]) -> List[ReviewIssue]:
        issues = []
        
        sections = report_data.get('sections', [])
        chapter_num = 0
        
        for section in sections:
            if section.get('type') == 'chapter':
                chapter_num += 1
                title = section.get('title', '')
                
                # Check if chapter has proper numbering in title
                if 'CHƯƠNG' in title.upper() or 'CHAPTER' in title.upper():
                    # Already has numbering, check if correct
                    if f"CHƯƠNG {chapter_num}" not in title and f"CHAPTER {chapter_num}" not in title:
                        issues.append(ReviewIssue(
                            check_type=CheckType.FORMATTING,
                            severity=Severity.WARNING,
                            message=f"Chapter numbering may be incorrect: expected {chapter_num}",
                            section_title=title,
                            details={'expected_number': chapter_num}
                        ))
        
        return issues


class MissingCaptionsCheck(BaseCheck):
    """Check for missing captions on tables/figures"""
    
    def check(self, report_data: Dict[str, Any]) -> List[ReviewIssue]:
        issues = []
        
        evidence = report_data.get('evidence', {})
        
        # Check figures
        figures = evidence.get('figures', [])
        for i, figure in enumerate(figures):
            if not figure.get('caption') and not figure.get('title'):
                issues.append(ReviewIssue(
                    check_type=CheckType.EVIDENCE,
                    severity=Severity.WARNING,
                    message=f"Figure {i+1} is missing a caption",
                    section_id=figure.get('section_id'),
                    details={'figure_index': i, 'path': figure.get('path')}
                ))
        
        # Check tables
        tables = evidence.get('tables', [])
        for i, table in enumerate(tables):
            if not table.get('caption') and not table.get('title'):
                issues.append(ReviewIssue(
                    check_type=CheckType.EVIDENCE,
                    severity=Severity.WARNING,
                    message=f"Table {i+1} is missing a caption",
                    section_id=table.get('section_id'),
                    details={'table_index': i}
                ))
        
        return issues


class UnusedReferencesCheck(BaseCheck):
    """Check for unused references"""
    
    def check(self, report_data: Dict[str, Any]) -> List[ReviewIssue]:
        issues = []
        
        # Get all references
        sections = report_data.get('sections', [])
        references = []
        
        for section in sections:
            if section.get('type') == 'references':
                refs = section.get('references', [])
                if refs:
                    references = refs
                else:
                    content = section.get('content', '')
                    references = [r.strip() for r in content.split('\n') if r.strip()]
        
        if not references:
            return issues
        
        # Collect all content
        all_content = []
        for section in sections:
            content = section.get('content', '')
            if content:
                all_content.append(content)
            
            for subsection in section.get('subsections', []):
                sub_content = subsection.get('content', '')
                if sub_content:
                    all_content.append(sub_content)
        
        full_text = ' '.join(all_content).lower()
        
        # Check each reference
        for i, ref in enumerate(references):
            # Simple heuristic: check if reference number appears in text
            if f'[{i+1}]' not in full_text and f'({i+1})' not in full_text:
                issues.append(ReviewIssue(
                    check_type=CheckType.REFERENCES,
                    severity=Severity.INFO,
                    message=f"Reference {i+1} may be unused",
                    details={'reference': ref[:100], 'index': i+1}
                ))
        
        return issues


class EmptySectionsCheck(BaseCheck):
    """Check for empty or too-short sections"""
    
    MIN_CONTENT_LENGTH = 50
    
    def check(self, report_data: Dict[str, Any]) -> List[ReviewIssue]:
        issues = []
        
        sections = report_data.get('sections', [])
        
        for section in sections:
            section_type = section.get('type')
            title = section.get('title', 'Untitled')
            content = section.get('content', '')
            subsections = section.get('subsections', [])
            
            # Skip certain types
            if section_type in ['cover', 'toc']:
                continue
            
            # Check if section has content or subsections
            if not content and not subsections:
                issues.append(ReviewIssue(
                    check_type=CheckType.CONTENT,
                    severity=Severity.ERROR,
                    message=f"Section '{title}' is empty",
                    section_title=title,
                    details={'section_type': section_type}
                ))
            elif content and len(content.strip()) < self.MIN_CONTENT_LENGTH and not subsections:
                issues.append(ReviewIssue(
                    check_type=CheckType.CONTENT,
                    severity=Severity.WARNING,
                    message=f"Section '{title}' has very short content ({len(content)} chars)",
                    section_title=title,
                    details={'content_length': len(content), 'min_length': self.MIN_CONTENT_LENGTH}
                ))
            
            # Check subsections
            for subsection in subsections:
                sub_title = subsection.get('title', 'Untitled')
                sub_content = subsection.get('content', '')
                
                if not sub_content:
                    issues.append(ReviewIssue(
                        check_type=CheckType.CONTENT,
                        severity=Severity.WARNING,
                        message=f"Subsection '{sub_title}' is empty",
                        section_title=title,
                        details={'subsection_title': sub_title}
                    ))
        
        return issues


class DuplicateSectionsCheck(BaseCheck):
    """Check for duplicate section titles"""
    
    def check(self, report_data: Dict[str, Any]) -> List[ReviewIssue]:
        issues = []
        
        sections = report_data.get('sections', [])
        seen_titles = {}
        
        for section in sections:
            title = section.get('title', '').strip().lower()
            section_type = section.get('type')
            
            if not title:
                continue
            
            if title in seen_titles:
                issues.append(ReviewIssue(
                    check_type=CheckType.STRUCTURE,
                    severity=Severity.WARNING,
                    message=f"Duplicate section title: '{section.get('title')}'",
                    section_title=section.get('title'),
                    details={
                        'first_occurrence': seen_titles[title],
                        'current_type': section_type
                    }
                ))
            else:
                seen_titles[title] = section_type
        
        return issues


class ConclusionResultsMismatchCheck(BaseCheck):
    """Check for conclusion/results mismatch heuristic"""
    
    def check(self, report_data: Dict[str, Any]) -> List[ReviewIssue]:
        issues = []
        
        sections = report_data.get('sections', [])
        
        # Find results and conclusion sections
        results_content = []
        conclusion_content = []
        
        for section in sections:
            title = section.get('title', '').lower()
            content = section.get('content', '')
            
            if 'result' in title or 'kết quả' in title:
                results_content.append(content)
                for subsection in section.get('subsections', []):
                    results_content.append(subsection.get('content', ''))
            
            if section.get('type') == 'conclusion' or 'conclusion' in title or 'kết luận' in title:
                conclusion_content.append(content)
                for subsection in section.get('subsections', []):
                    conclusion_content.append(subsection.get('content', ''))
        
        if not results_content or not conclusion_content:
            return issues
        
        results_text = ' '.join(results_content).lower()
        conclusion_text = ' '.join(conclusion_content).lower()
        
        # Extract key terms from results (simple heuristic)
        results_words = set(results_text.split())
        conclusion_words = set(conclusion_text.split())
        
        # Check if conclusion mentions results
        if len(results_words) > 50 and len(conclusion_words) > 20:
            # Check for common important words
            important_words = results_words & conclusion_words
            overlap_ratio = len(important_words) / min(len(results_words), len(conclusion_words))
            
            if overlap_ratio < 0.1:
                issues.append(ReviewIssue(
                    check_type=CheckType.CONTENT,
                    severity=Severity.INFO,
                    message="Conclusion may not adequately reference results",
                    details={
                        'overlap_ratio': round(overlap_ratio, 2),
                        'suggestion': 'Ensure conclusion summarizes key findings from results'
                    }
                ))
        
        return issues
