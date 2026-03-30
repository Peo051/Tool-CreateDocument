"""
Test review engine
"""

import pytest
from source.review.engine import ReviewEngine
from source.review.checks import (
    RequiredSectionsCheck,
    HeadingNumberingCheck,
    MissingCaptionsCheck,
    EmptySectionsCheck
)
from source.review.models import Severity


def test_review_engine_initialization():
    """Test review engine can be initialized"""
    engine = ReviewEngine()
    assert engine is not None
    assert len(engine.checks) > 0


def test_required_sections_check(sample_report_data):
    """Test required sections check"""
    check = RequiredSectionsCheck()
    issues = check.check(sample_report_data)
    
    # Sample data has introduction and conclusion
    assert len(issues) == 0


def test_missing_required_sections():
    """Test detection of missing required sections"""
    check = RequiredSectionsCheck()
    
    incomplete_data = {
        'metadata': {'title': 'Test', 'report_type': 'project_report'},
        'sections': [
            {'type': 'chapter', 'title': 'INTRODUCTION', 'content': 'Intro'}
        ],
        'evidence': {'figures': [], 'tables': []}
    }
    
    issues = check.check(incomplete_data)
    assert len(issues) > 0
    assert any('conclusion' in issue.message.lower() for issue in issues)


def test_empty_sections_check():
    """Test empty sections detection"""
    check = EmptySectionsCheck()
    
    data_with_empty = {
        'metadata': {'title': 'Test'},
        'sections': [
            {'type': 'chapter', 'title': 'INTRODUCTION', 'content': ''},
            {'type': 'chapter', 'title': 'METHODS', 'content': 'Good content here with enough text to pass minimum length check'}
        ],
        'evidence': {'figures': [], 'tables': []}
    }
    
    issues = check.check(data_with_empty)
    assert len(issues) > 0
    assert issues[0].severity == Severity.ERROR


def test_missing_captions_check():
    """Test missing captions detection"""
    check = MissingCaptionsCheck()
    
    data_with_uncaptioned = {
        'metadata': {'title': 'Test'},
        'sections': [],
        'evidence': {
            'figures': [
                {'path': 'test.png', 'caption': ''},
                {'path': 'test2.png', 'caption': 'Good caption'}
            ],
            'tables': [
                {'headers': ['A'], 'rows': [['1']], 'caption': ''}
            ]
        }
    }
    
    issues = check.check(data_with_uncaptioned)
    assert len(issues) == 2  # One figure and one table without caption


def test_review_engine_full_report(sample_report_data):
    """Test full review engine run"""
    engine = ReviewEngine()
    report = engine.review(sample_report_data)
    
    assert report is not None
    assert hasattr(report, 'issues')
    assert hasattr(report, 'summary')
    assert isinstance(report.issues, list)


def test_review_severity_levels():
    """Test different severity levels"""
    check = EmptySectionsCheck()
    
    data = {
        'metadata': {'title': 'Test'},
        'sections': [
            {'type': 'chapter', 'title': 'TEST', 'content': 'ab'}  # Too short
        ],
        'evidence': {'figures': [], 'tables': []}
    }
    
    issues = check.check(data)
    assert len(issues) > 0
    assert issues[0].severity in [Severity.ERROR, Severity.WARNING, Severity.INFO]
