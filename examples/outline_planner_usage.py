#!/usr/bin/env python3
"""
OutlinePlanner Usage Examples
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

from outline_planner import OutlinePlanner, ReportType
import json


def example_basic():
    """Basic usage - generate default outlines"""
    print("="*60)
    print("Example 1: Basic Usage")
    print("="*60)
    
    planner = OutlinePlanner()
    
    # Generate thesis outline
    outline = planner.plan('thesis')
    print(f"\nThesis outline: {len(outline.sections)} sections")
    for section in outline.sections[:5]:
        print(f"  - {section.title}")
    
    # Generate project report outline
    outline = planner.plan('project_report')
    print(f"\nProject report outline: {len(outline.sections)} sections")
    for section in outline.sections[:5]:
        print(f"  - {section.title}")


def example_with_config():
    """With configuration"""
    print("\n" + "="*60)
    print("Example 2: With Configuration")
    print("="*60)
    
    planner = OutlinePlanner()
    
    config = {
        'algorithms': ['DFS', 'BFS', 'A*', 'Dijkstra', 'CSP']
    }
    
    outline = planner.plan('project_report', config)
    
    # Find algorithms section
    for section in outline.sections:
        if section.id == 'algorithms':
            print(f"\n{section.title}:")
            for subsec in section.subsections:
                print(f"  {subsec.title}")


def example_custom_sections():
    """Custom sections override"""
    print("\n" + "="*60)
    print("Example 3: Custom Sections")
    print("="*60)
    
    planner = OutlinePlanner()
    
    config = {
        'custom_sections': [
            {
                'id': 'custom1',
                'title': 'Custom Chapter: AI Ethics',
                'level': 1,
                'position': 5,
                'subsections': [
                    {'title': 'Ethical Considerations'},
                    {'title': 'Privacy Concerns'}
                ]
            }
        ]
    }
    
    outline = planner.plan('technical_report', config)
    
    print(f"\nTechnical report with custom section:")
    for i, section in enumerate(outline.sections):
        print(f"  {i+1}. {section.title}")
        if section.subsections:
            for subsec in section.subsections:
                print(f"      - {subsec.title}")


def example_to_dict():
    """Convert to dictionary"""
    print("\n" + "="*60)
    print("Example 4: Export to Dictionary")
    print("="*60)
    
    planner = OutlinePlanner()
    outline = planner.plan('business_report')
    
    # Convert to dict
    outline_dict = outline.to_dict()
    
    print(f"\nReport type: {outline_dict['report_type']}")
    print(f"Sections: {len(outline_dict['sections'])}")
    print("\nJSON preview:")
    print(json.dumps(outline_dict, indent=2)[:500] + "...")


def example_all_types():
    """Generate all report types"""
    print("\n" + "="*60)
    print("Example 5: All Report Types")
    print("="*60)
    
    planner = OutlinePlanner()
    
    types = ['thesis', 'technical_report', 'project_report', 'business_report']
    
    for rtype in types:
        outline = planner.plan(rtype)
        print(f"\n{rtype}: {len(outline.sections)} sections")


def main():
    print("\nOutlinePlanner Usage Examples\n")
    
    example_basic()
    example_with_config()
    example_custom_sections()
    example_to_dict()
    example_all_types()
    
    print("\n" + "="*60)
    print("✅ All examples completed!")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
