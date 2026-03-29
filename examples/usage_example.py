#!/usr/bin/env python3
"""
Usage examples for ReportConfig schema
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

from config_models import (
    ReportConfig,
    ProjectInfo,
    Author,
    ReportProfile,
    TechnicalData,
    validate_config,
    load_config,
    save_config
)


# ============================================================================
# Example 1: Create config programmatically
# ============================================================================

def example_create_config():
    """Create config from scratch"""
    print("Example 1: Create config programmatically\n")
    
    config = ReportConfig(
        project_info=ProjectInfo(
            title="My Project",
            description="A detailed project description",
            students=[
                Author(name="Alice Smith", id="001"),
                Author(name="Bob Jones", id="002")
            ],
            university="Tech University",
            advisor="Dr. Jane Doe"
        ),
        report_profile=ReportProfile(
            report_type="project_report",
            language="en",
            target_pages=50
        ),
        technical_data=TechnicalData(
            algorithms=["DFS", "BFS", "A*"],
            technologies=["Python", "TensorFlow"]
        )
    )
    
    print(f"Title: {config.project_info.title}")
    print(f"Type: {config.report_profile.report_type}")
    print(f"Authors: {len(config.project_info.students)}")
    print(f"Algorithms: {', '.join(config.technical_data.algorithms)}")
    print()


# ============================================================================
# Example 2: Load from JSON file
# ============================================================================

def example_load_from_file():
    """Load config from JSON file"""
    print("Example 2: Load from JSON file\n")
    
    try:
        config = load_config('config_minimal.json')
        print(f"✅ Loaded: {config.project_info.title}")
        print(f"   Type: {config.report_profile.report_type}")
        print(f"   Language: {config.report_profile.language}")
        print()
    except Exception as e:
        print(f"❌ Error: {e}\n")


# ============================================================================
# Example 3: Validate config dictionary
# ============================================================================

def example_validate():
    """Validate config dictionary"""
    print("Example 3: Validate config\n")
    
    # Valid config
    valid_config = {
        "project_info": {
            "title": "Test Project",
            "description": "Test description",
            "students": [{"name": "Test User"}],
            "university": "Test University"
        },
        "report_profile": {
            "report_type": "thesis"
        }
    }
    
    is_valid, errors = validate_config(valid_config)
    print(f"Valid config: {is_valid}")
    
    # Invalid config (missing required fields)
    invalid_config = {
        "project_info": {
            "title": "Test"
            # Missing description, students, university
        }
    }
    
    is_valid, errors = validate_config(invalid_config)
    print(f"Invalid config: {is_valid}")
    if errors:
        print(f"Errors: {errors[0][:100]}...")
    print()


# ============================================================================
# Example 4: Convert legacy config
# ============================================================================

def example_legacy_conversion():
    """Convert legacy config format"""
    print("Example 4: Convert legacy config\n")
    
    legacy_config = {
        "report_type": "ttnt",
        "title": "Old Format Project",
        "description": "Using old config format",
        "students": [
            {"name": "Student A", "id": "001"}
        ],
        "university": "University Name",
        "algorithms": ["DFS", "BFS"],
        "technologies": ["Python"]
    }
    
    try:
        config = ReportConfig.from_legacy_config(legacy_config)
        print(f"✅ Converted: {config.project_info.title}")
        print(f"   Old type 'ttnt' → New type '{config.report_profile.report_type}'")
        print(f"   Algorithms: {', '.join(config.technical_data.algorithms)}")
        print()
    except Exception as e:
        print(f"❌ Error: {e}\n")


# ============================================================================
# Example 5: Save config to file
# ============================================================================

def example_save_config():
    """Save config to JSON file"""
    print("Example 5: Save config to file\n")
    
    config = ReportConfig(
        project_info=ProjectInfo(
            title="Saved Project",
            description="This config will be saved",
            students=[Author(name="User")],
            university="University"
        ),
        report_profile=ReportProfile(
            report_type="technical_report"
        )
    )
    
    output_path = 'config_generated.json'
    save_config(config, output_path)
    print(f"✅ Saved to: {output_path}")
    print()


# ============================================================================
# Example 6: Access nested fields
# ============================================================================

def example_access_fields():
    """Access nested configuration fields"""
    print("Example 6: Access nested fields\n")
    
    config = load_config('config_full.json')
    
    # Access project info
    print(f"Title: {config.project_info.title}")
    print(f"First author: {config.project_info.students[0].name}")
    
    # Access technical data
    if config.technical_data.algorithms:
        print(f"Algorithms: {', '.join(config.technical_data.algorithms)}")
    
    # Access evidence
    if config.evidence.charts:
        print(f"Charts: {len(config.evidence.charts)}")
    
    # Access format rules
    print(f"Font: {config.format_rules.font_name} {config.format_rules.font_size}pt")
    print()


# ============================================================================
# Example 7: Validation errors
# ============================================================================

def example_validation_errors():
    """Show validation error handling"""
    print("Example 7: Validation errors\n")
    
    # Missing required field
    try:
        config = ReportConfig(
            project_info=ProjectInfo(
                title="",  # Empty title (invalid)
                description="Test",
                students=[Author(name="User")],
                university="Uni"
            ),
            report_profile=ReportProfile(report_type="thesis")
        )
    except Exception as e:
        print(f"❌ Validation error: {str(e)[:100]}")
    
    # Invalid report type
    try:
        config_dict = {
            "project_info": {
                "title": "Test",
                "description": "Test",
                "students": [{"name": "User"}],
                "university": "Uni"
            },
            "report_profile": {
                "report_type": "invalid_type"  # Invalid
            }
        }
        config = ReportConfig(**config_dict)
    except Exception as e:
        print(f"❌ Validation error: {str(e)[:100]}")
    
    print()


# ============================================================================
# Main
# ============================================================================

def main():
    print("=" * 60)
    print("ReportConfig Usage Examples")
    print("=" * 60)
    print()
    
    example_create_config()
    example_load_from_file()
    example_validate()
    example_legacy_conversion()
    example_save_config()
    example_access_fields()
    example_validation_errors()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
