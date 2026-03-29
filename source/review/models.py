"""
Review Models
Data structures for report review results
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum


class Severity(str, Enum):
    """Issue severity levels"""
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


class CheckType(str, Enum):
    """Types of checks"""
    STRUCTURE = "structure"
    CONTENT = "content"
    FORMATTING = "formatting"
    REFERENCES = "references"
    EVIDENCE = "evidence"


@dataclass
class ReviewIssue:
    """Single review issue"""
    check_type: CheckType
    severity: Severity
    message: str
    section_id: Optional[str] = None
    section_title: Optional[str] = None
    details: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'check_type': self.check_type.value,
            'severity': self.severity.value,
            'message': self.message,
            'section_id': self.section_id,
            'section_title': self.section_title,
            'details': self.details
        }


@dataclass
class ReviewResult:
    """Complete review result"""
    passed: bool
    total_issues: int
    errors: int
    warnings: int
    infos: int
    issues: List[ReviewIssue] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def add_issue(self, issue: ReviewIssue) -> None:
        """Add issue to result"""
        self.issues.append(issue)
        self.total_issues += 1
        
        if issue.severity == Severity.ERROR:
            self.errors += 1
            self.passed = False
        elif issue.severity == Severity.WARNING:
            self.warnings += 1
        else:
            self.infos += 1
    
    def get_issues_by_severity(self, severity: Severity) -> List[ReviewIssue]:
        """Get issues by severity"""
        return [issue for issue in self.issues if issue.severity == severity]
    
    def get_issues_by_type(self, check_type: CheckType) -> List[ReviewIssue]:
        """Get issues by check type"""
        return [issue for issue in self.issues if issue.check_type == check_type]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'passed': self.passed,
            'total_issues': self.total_issues,
            'errors': self.errors,
            'warnings': self.warnings,
            'infos': self.infos,
            'issues': [issue.to_dict() for issue in self.issues],
            'metadata': self.metadata
        }
    
    def summary(self) -> str:
        """Get summary string"""
        status = "PASSED" if self.passed else "FAILED"
        return (
            f"Review {status}: {self.total_issues} issues "
            f"({self.errors} errors, {self.warnings} warnings, {self.infos} infos)"
        )
