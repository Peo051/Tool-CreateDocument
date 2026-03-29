"""
Review Engine
Main engine for reviewing generated reports
"""

from typing import Dict, Any, List, Type
from .models import ReviewResult, ReviewIssue
from .checks import (
    BaseCheck,
    RequiredSectionsCheck,
    HeadingNumberingCheck,
    MissingCaptionsCheck,
    UnusedReferencesCheck,
    EmptySectionsCheck,
    DuplicateSectionsCheck,
    ConclusionResultsMismatchCheck
)


class ReviewEngine:
    """Engine for reviewing report quality"""
    
    # Default checks to run
    DEFAULT_CHECKS = [
        RequiredSectionsCheck,
        HeadingNumberingCheck,
        MissingCaptionsCheck,
        UnusedReferencesCheck,
        EmptySectionsCheck,
        DuplicateSectionsCheck,
        ConclusionResultsMismatchCheck
    ]
    
    def __init__(self, checks: List[Type[BaseCheck]] = None):
        """
        Initialize review engine
        
        Args:
            checks: List of check classes to run (default: all checks)
        """
        self.checks = checks or self.DEFAULT_CHECKS
        self._check_instances = [check_class() for check_class in self.checks]
    
    def review(self, report_data: Dict[str, Any]) -> ReviewResult:
        """
        Review report data
        
        Args:
            report_data: Report data dictionary
            
        Returns:
            ReviewResult with all issues found
        """
        result = ReviewResult(
            passed=True,
            total_issues=0,
            errors=0,
            warnings=0,
            infos=0
        )
        
        # Add metadata
        metadata = report_data.get('metadata', {})
        result.metadata = {
            'report_title': metadata.get('title', 'Unknown'),
            'report_type': metadata.get('report_type', 'Unknown'),
            'checks_run': len(self._check_instances)
        }
        
        # Run all checks
        for check in self._check_instances:
            issues = check.check(report_data)
            for issue in issues:
                result.add_issue(issue)
        
        return result
    
    def add_check(self, check_class: Type[BaseCheck]) -> None:
        """
        Add a custom check
        
        Args:
            check_class: Check class to add
        """
        self.checks.append(check_class)
        self._check_instances.append(check_class())
    
    def remove_check(self, check_class: Type[BaseCheck]) -> None:
        """
        Remove a check
        
        Args:
            check_class: Check class to remove
        """
        if check_class in self.checks:
            self.checks.remove(check_class)
            self._check_instances = [check_class() for check_class in self.checks]
    
    def get_checks(self) -> List[str]:
        """Get list of check names"""
        return [check.__class__.__name__ for check in self._check_instances]


class ReviewReport:
    """Generate human-readable review report"""
    
    @staticmethod
    def format_text(result: ReviewResult) -> str:
        """
        Format review result as text
        
        Args:
            result: ReviewResult to format
            
        Returns:
            Formatted text report
        """
        lines = []
        
        # Header
        lines.append("=" * 60)
        lines.append("REPORT REVIEW RESULTS")
        lines.append("=" * 60)
        lines.append("")
        
        # Summary
        lines.append(result.summary())
        lines.append("")
        
        # Metadata
        if result.metadata:
            lines.append("Report Information:")
            for key, value in result.metadata.items():
                lines.append(f"  {key}: {value}")
            lines.append("")
        
        # Issues by severity
        if result.errors > 0:
            lines.append(f"ERRORS ({result.errors}):")
            lines.append("-" * 60)
            for issue in result.get_issues_by_severity('error'):
                lines.append(f"  ✗ {issue.message}")
                if issue.section_title:
                    lines.append(f"    Section: {issue.section_title}")
                if issue.details:
                    lines.append(f"    Details: {issue.details}")
                lines.append("")
        
        if result.warnings > 0:
            lines.append(f"WARNINGS ({result.warnings}):")
            lines.append("-" * 60)
            for issue in result.get_issues_by_severity('warning'):
                lines.append(f"  ⚠ {issue.message}")
                if issue.section_title:
                    lines.append(f"    Section: {issue.section_title}")
                if issue.details:
                    lines.append(f"    Details: {issue.details}")
                lines.append("")
        
        if result.infos > 0:
            lines.append(f"INFO ({result.infos}):")
            lines.append("-" * 60)
            for issue in result.get_issues_by_severity('info'):
                lines.append(f"  ℹ {issue.message}")
                if issue.section_title:
                    lines.append(f"    Section: {issue.section_title}")
                if issue.details:
                    lines.append(f"    Details: {issue.details}")
                lines.append("")
        
        if result.total_issues == 0:
            lines.append("✓ No issues found. Report looks good!")
            lines.append("")
        
        lines.append("=" * 60)
        
        return "\n".join(lines)
    
    @staticmethod
    def format_json(result: ReviewResult) -> Dict[str, Any]:
        """
        Format review result as JSON-serializable dict
        
        Args:
            result: ReviewResult to format
            
        Returns:
            Dictionary representation
        """
        return result.to_dict()
