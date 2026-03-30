"""
Test config validation
"""

import pytest
from pydantic import ValidationError
from source.config_models import ReportConfig, ProjectInfo, ReportProfile


def test_minimal_config(sample_config_dict):
    """Test minimal valid config"""
    config = ReportConfig(**sample_config_dict)
    assert config.project_info.title == 'Test Project'
    assert config.report_profile.report_type == 'project_report'


def test_missing_required_fields():
    """Test validation fails on missing required fields"""
    with pytest.raises(ValidationError):
        ReportConfig(project_info={}, report_profile={})


def test_invalid_report_type():
    """Test validation fails on invalid report type"""
    with pytest.raises(ValidationError):
        ReportProfile(report_type='invalid_type', language='vi')


def test_valid_report_types():
    """Test all valid report types"""
    valid_types = ['thesis', 'technical_report', 'project_report', 'business_report']
    for report_type in valid_types:
        profile = ReportProfile(report_type=report_type, language='vi')
        assert profile.report_type == report_type


def test_university_organization_compatibility(sample_config_dict):
    """Test both university and organization fields work"""
    # Test with university
    config1 = ReportConfig(**sample_config_dict)
    assert config1.project_info.university == 'Test University'
    
    # Test with organization
    config_dict = sample_config_dict.copy()
    config_dict['project_info']['organization'] = 'Test Org'
    del config_dict['project_info']['university']
    config2 = ReportConfig(**config_dict)
    assert config2.project_info.organization == 'Test Org'


def test_default_values(sample_config_dict):
    """Test default values are applied"""
    config = ReportConfig(**sample_config_dict)
    assert config.format_rules.font_size == 13
    assert config.format_rules.line_spacing == 1.5
    assert config.content_requirements.include_cover is True


def test_config_to_dict(sample_config_dict):
    """Test config can be exported to dict"""
    config = ReportConfig(**sample_config_dict)
    config_dict = config.model_dump()
    assert isinstance(config_dict, dict)
    assert config_dict['project_info']['title'] == 'Test Project'
