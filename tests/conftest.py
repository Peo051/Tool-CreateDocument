"""
Pytest Fixtures
Shared test fixtures for all tests
"""

import pytest
import os
import tempfile
from pathlib import Path


@pytest.fixture
def sample_metadata():
    """Sample report metadata"""
    return {
        'title': 'Test Report',
        'organization': 'Test University',
        'faculty': 'Computer Science',
        'students': [
            {'name': 'John Doe', 'id': '123456'},
            {'name': 'Jane Smith', 'id': '123457'}
        ],
        'advisor': 'Dr. Test Advisor',
        'class_name': 'CS101',
        'report_type': 'project_report'
    }


@pytest.fixture
def sample_sections():
    """Sample report sections"""
    return [
        {
            'type': 'cover',
            'title': 'Cover Page'
        },
        {
            'type': 'toc',
            'title': 'Table of Contents'
        },
        {
            'type': 'chapter',
            'title': 'INTRODUCTION',
            'level': 1,
            'content': 'This is the introduction section with sufficient content for testing purposes.',
            'subsections': [
                {
                    'id': 'intro_background',
                    'title': 'Background',
                    'level': 2,
                    'content': 'Background information about the project and its context.'
                }
            ]
        },
        {
            'type': 'conclusion',
            'title': 'CONCLUSION',
            'level': 1,
            'content': 'This is the conclusion section summarizing the key findings and results.'
        },
        {
            'type': 'references',
            'title': 'REFERENCES',
            'references': [
                'Reference 1: Test Reference',
                'Reference 2: Another Reference'
            ]
        }
    ]


@pytest.fixture
def sample_evidence():
    """Sample evidence data"""
    return {
        'figures': [
            {
                'section_id': 'intro_background',
                'path': 'test_image.png',
                'caption': 'Test Figure Caption'
            }
        ],
        'tables': [
            {
                'section_id': 'intro_background',
                'headers': ['Column 1', 'Column 2'],
                'rows': [['A', 'B'], ['C', 'D']],
                'caption': 'Test Table Caption'
            }
        ]
    }


@pytest.fixture
def sample_report_data(sample_metadata, sample_sections, sample_evidence):
    """Complete sample report data"""
    return {
        'metadata': sample_metadata,
        'sections': sample_sections,
        'evidence': sample_evidence
    }


@pytest.fixture
def temp_output_dir():
    """Temporary output directory"""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def sample_chart_data():
    """Sample chart data"""
    return {
        'categories': ['A', 'B', 'C'],
        'values': [10, 20, 30]
    }


@pytest.fixture
def sample_config_dict():
    """Sample configuration dictionary"""
    return {
        'project_info': {
            'title': 'Test Project',
            'description': 'Test project description',
            'students': [
                {'name': 'Test Student', 'id': '123456'}
            ],
            'university': 'Test University',
            'faculty': 'Test Faculty'
        },
        'report_profile': {
            'report_type': 'project_report',
            'language': 'vi'
        },
        'content_requirements': {
            'include_cover': True,
            'include_toc': True,
            'include_references': True
        },
        'technical_data': {
            'algorithms': ['BFS', 'DFS'],
            'technologies': ['Python', 'pytest']
        },
        'evidence': {
            'charts': [],
            'tables': [],
            'figures': [],
            'references': []
        },
        'format_rules': {
            'font_size': 13,
            'line_spacing': 1.5
        }
    }
