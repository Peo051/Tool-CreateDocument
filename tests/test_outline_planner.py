#!/usr/bin/env python3
"""
Unit tests for OutlinePlanner
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

import unittest
from outline_planner import OutlinePlanner, ReportType, OutlineSection, ReportOutline


class TestOutlinePlanner(unittest.TestCase):
    
    def setUp(self):
        self.planner = OutlinePlanner()
    
    def test_thesis_outline(self):
        """Test thesis outline generation"""
        outline = self.planner.plan('thesis')
        self.assertEqual(outline.report_type, ReportType.THESIS)
        self.assertGreater(len(outline.sections), 0)
        self.assertIn('cover', [s.id for s in outline.sections])
    
    def test_technical_outline(self):
        """Test technical report outline"""
        outline = self.planner.plan('technical_report')
        self.assertEqual(outline.report_type, ReportType.TECHNICAL_REPORT)
        self.assertGreater(len(outline.sections), 0)
    
    def test_project_outline(self):
        """Test project report outline"""
        outline = self.planner.plan('project_report')
        self.assertEqual(outline.report_type, ReportType.PROJECT_REPORT)
        self.assertGreater(len(outline.sections), 0)
    
    def test_business_outline(self):
        """Test business report outline"""
        outline = self.planner.plan('business_report')
        self.assertEqual(outline.report_type, ReportType.BUSINESS_REPORT)
        self.assertGreater(len(outline.sections), 0)
    
    def test_with_algorithms(self):
        """Test project outline with algorithms"""
        config = {'algorithms': ['DFS', 'BFS', 'A*']}
        outline = self.planner.plan('project_report', config)
        
        # Find algorithms section
        algo_section = next((s for s in outline.sections if s.id == 'algorithms'), None)
        self.assertIsNotNone(algo_section)
        self.assertEqual(len(algo_section.subsections), 3)
    
    def test_custom_sections(self):
        """Test custom sections"""
        config = {
            'custom_sections': [
                {
                    'id': 'custom1',
                    'title': 'Custom Section',
                    'level': 1
                }
            ]
        }
        outline = self.planner.plan('thesis', config)
        
        # Check custom section exists
        custom = next((s for s in outline.sections if s.id == 'custom1'), None)
        self.assertIsNotNone(custom)
        self.assertEqual(custom.title, 'Custom Section')
    
    def test_to_dict(self):
        """Test conversion to dictionary"""
        outline = self.planner.plan('thesis')
        outline_dict = outline.to_dict()
        
        self.assertIn('report_type', outline_dict)
        self.assertIn('sections', outline_dict)
        self.assertIsInstance(outline_dict['sections'], list)
    
    def test_invalid_type(self):
        """Test invalid report type"""
        with self.assertRaises(ValueError):
            self.planner.plan('invalid_type')
    
    def test_subsections(self):
        """Test subsections are created"""
        outline = self.planner.plan('thesis')
        
        # Find introduction chapter
        intro = next((s for s in outline.sections if s.id == 'ch1'), None)
        self.assertIsNotNone(intro)
        self.assertGreater(len(intro.subsections), 0)


if __name__ == '__main__':
    unittest.main()
