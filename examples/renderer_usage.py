"""
Report Renderer Usage Examples
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from source.renderers import ReportRenderer, StyleManager
from docx.shared import Pt, Cm


def example_1_basic_report():
    """Example 1: Basic report rendering"""
    print("=" * 60)
    print("Example 1: Basic Report")
    print("=" * 60)
    
    renderer = ReportRenderer()
    
    report_data = {
        'metadata': {
            'title': 'Search Algorithm Comparison',
            'subtitle': 'BFS, DFS, and A* Analysis',
            'organization': 'University of Technology',
            'faculty': 'Computer Science',
            'advisor': 'Dr. John Smith',
            'students': [
                {'name': 'Alice Johnson', 'id': '2021001'},
                {'name': 'Bob Williams', 'id': '2021002'}
            ],
            'class_name': 'CS401',
            'report_type': 'project_report'
        },
        'sections': [
            {
                'type': 'cover',
                'title': 'Cover Page'
            },
            {
                'type': 'toc',
                'title': 'MỤC LỤC'
            },
            {
                'type': 'chapter',
                'title': 'INTRODUCTION',
                'level': 1,
                'content': 'This report presents a comprehensive analysis of search algorithms.',
                'subsections': [
                    {
                        'id': 'intro_background',
                        'title': 'Background',
                        'level': 2,
                        'content': 'Search algorithms are fundamental to computer science.'
                    },
                    {
                        'id': 'intro_objectives',
                        'title': 'Objectives',
                        'level': 2,
                        'content': '- Compare algorithm performance\n- Analyze time complexity\n- Provide implementation examples'
                    }
                ]
            },
            {
                'type': 'conclusion',
                'title': 'CONCLUSION',
                'level': 1,
                'content': 'This study successfully compared three search algorithms.'
            }
        ],
        'evidence': {
            'figures': [],
            'tables': []
        }
    }
    
    output_path = 'output/basic_report.docx'
    result = renderer.render(report_data, output_path)
    
    print(f"✓ Report generated: {result}")
    print()


def example_2_with_images():
    """Example 2: Report with images"""
    print("=" * 60)
    print("Example 2: Report with Images")
    print("=" * 60)
    
    renderer = ReportRenderer()
    
    report_data = {
        'metadata': {
            'title': 'Algorithm Visualization Study',
            'organization': 'Tech University',
            'faculty': 'Engineering',
            'students': [{'name': 'Charlie Brown', 'id': '2021003'}],
            'report_type': 'technical_report'
        },
        'sections': [
            {
                'type': 'cover',
                'title': 'Cover'
            },
            {
                'type': 'chapter',
                'title': 'ALGORITHM ANALYSIS',
                'level': 1,
                'subsections': [
                    {
                        'id': 'algo_performance',
                        'title': 'Performance Comparison',
                        'level': 2,
                        'content': 'The following chart shows algorithm execution times.'
                    }
                ]
            }
        ],
        'evidence': {
            'figures': [
                {
                    'section_id': 'algo_performance',
                    'path': 'output/charts/algo_performance.png',
                    'caption': 'Algorithm execution time comparison'
                }
            ],
            'tables': []
        }
    }
    
    output_path = 'output/report_with_images.docx'
    result = renderer.render(report_data, output_path)
    
    print(f"✓ Report generated: {result}")
    print()


def example_3_with_tables():
    """Example 3: Report with tables"""
    print("=" * 60)
    print("Example 3: Report with Tables")
    print("=" * 60)
    
    renderer = ReportRenderer()
    
    report_data = {
        'metadata': {
            'title': 'Performance Metrics Study',
            'organization': 'Research Institute',
            'faculty': 'Computer Science',
            'students': [{'name': 'David Lee', 'id': '2021004'}]
        },
        'sections': [
            {
                'type': 'cover',
                'title': 'Cover'
            },
            {
                'type': 'chapter',
                'title': 'RESULTS',
                'level': 1,
                'subsections': [
                    {
                        'id': 'results_metrics',
                        'title': 'Performance Metrics',
                        'level': 2,
                        'content': 'The following table summarizes the results.'
                    }
                ]
            }
        ],
        'evidence': {
            'figures': [],
            'tables': [
                {
                    'section_id': 'results_metrics',
                    'headers': ['Algorithm', 'Time (ms)', 'Memory (MB)', 'Optimal'],
                    'rows': [
                        ['BFS', '120', '45', 'Yes'],
                        ['DFS', '95', '30', 'No'],
                        ['A*', '85', '50', 'Yes']
                    ],
                    'caption': 'Algorithm performance comparison'
                }
            ]
        }
    }
    
    output_path = 'output/report_with_tables.docx'
    result = renderer.render(report_data, output_path)
    
    print(f"✓ Report generated: {result}")
    print()


def example_4_custom_styles():
    """Example 4: Report with custom styles"""
    print("=" * 60)
    print("Example 4: Custom Styles")
    print("=" * 60)
    
    # Custom style configuration
    custom_styles = {
        'normal': {
            'font_size': Pt(12),
            'line_spacing': 1.15
        },
        'heading1': {
            'font_size': Pt(18)
        },
        'page': {
            'left_margin': Cm(2.5),
            'right_margin': Cm(2.5)
        }
    }
    
    style_manager = StyleManager(custom_styles)
    renderer = ReportRenderer(style_manager)
    
    report_data = {
        'metadata': {
            'title': 'Custom Styled Report',
            'organization': 'Design Institute',
            'faculty': 'Visual Arts',
            'students': [{'name': 'Emma Wilson', 'id': '2021005'}]
        },
        'sections': [
            {
                'type': 'cover',
                'title': 'Cover'
            },
            {
                'type': 'section',
                'title': 'INTRODUCTION',
                'level': 1,
                'content': 'This report uses custom styling.'
            }
        ],
        'evidence': {'figures': [], 'tables': []}
    }
    
    output_path = 'output/custom_styled_report.docx'
    result = renderer.render(report_data, output_path)
    
    print(f"✓ Report generated: {result}")
    print()


def example_5_complete_report():
    """Example 5: Complete report with all features"""
    print("=" * 60)
    print("Example 5: Complete Report")
    print("=" * 60)
    
    renderer = ReportRenderer()
    
    report_data = {
        'metadata': {
            'title': 'Comprehensive Search Algorithm Study',
            'subtitle': 'Analysis and Implementation',
            'organization': 'National University',
            'faculty': 'Computer Engineering',
            'advisor': 'Prof. Sarah Johnson',
            'students': [
                {'name': 'Frank Miller', 'id': '2021006'},
                {'name': 'Grace Davis', 'id': '2021007'}
            ],
            'class_name': 'CE502',
            'report_type': 'thesis'
        },
        'sections': [
            {
                'type': 'cover',
                'title': 'Cover Page'
            },
            {
                'type': 'acknowledgment',
                'title': 'LỜI CẢM ƠN',
                'level': 1,
                'content': 'We would like to thank our advisor and colleagues for their support.'
            },
            {
                'type': 'commitment',
                'title': 'LỜI CAM ĐOAN',
                'content': 'We declare that this work is our own and has not been submitted elsewhere.'
            },
            {
                'type': 'toc',
                'title': 'MỤC LỤC'
            },
            {
                'type': 'chapter',
                'title': 'INTRODUCTION',
                'level': 1,
                'content': 'Search algorithms are essential tools in computer science.',
                'subsections': [
                    {
                        'id': 'intro_motivation',
                        'title': 'Motivation',
                        'level': 2,
                        'content': 'Understanding search algorithms is crucial for:\n- Pathfinding applications\n- Game AI development\n- Route optimization'
                    },
                    {
                        'id': 'intro_scope',
                        'title': 'Scope',
                        'level': 2,
                        'content': 'This study focuses on three main algorithms: BFS, DFS, and A*.'
                    }
                ]
            },
            {
                'type': 'chapter',
                'title': 'METHODOLOGY',
                'level': 1,
                'subsections': [
                    {
                        'id': 'method_approach',
                        'title': 'Research Approach',
                        'level': 2,
                        'content': 'We conducted experimental analysis on various graph structures.'
                    },
                    {
                        'id': 'method_metrics',
                        'title': 'Performance Metrics',
                        'level': 2,
                        'content': 'Key metrics include execution time, memory usage, and path optimality.'
                    }
                ]
            },
            {
                'type': 'chapter',
                'title': 'RESULTS',
                'level': 1,
                'subsections': [
                    {
                        'id': 'results_performance',
                        'title': 'Performance Analysis',
                        'level': 2,
                        'content': 'The experimental results are presented below.'
                    }
                ]
            },
            {
                'type': 'conclusion',
                'title': 'CONCLUSION',
                'level': 1,
                'content': 'This study successfully compared three search algorithms and identified their strengths and weaknesses.'
            },
            {
                'type': 'references',
                'title': 'TÀI LIỆU THAM KHẢO',
                'references': [
                    'Russell, S., & Norvig, P. (2020). Artificial Intelligence: A Modern Approach.',
                    'Cormen, T. H., et al. (2009). Introduction to Algorithms.',
                    'Hart, P. E., et al. (1968). A Formal Basis for the Heuristic Determination of Minimum Cost Paths.'
                ]
            }
        ],
        'evidence': {
            'figures': [
                {
                    'section_id': 'results_performance',
                    'path': 'output/charts/algo_performance.png',
                    'caption': 'Algorithm execution time comparison on medium dataset'
                }
            ],
            'tables': [
                {
                    'section_id': 'results_performance',
                    'headers': ['Algorithm', 'Time (ms)', 'Memory (MB)', 'Path Quality'],
                    'rows': [
                        ['BFS', '120', '45', '100%'],
                        ['DFS', '95', '30', '75%'],
                        ['A*', '85', '50', '100%']
                    ],
                    'caption': 'Comprehensive performance metrics'
                }
            ]
        }
    }
    
    output_path = 'output/complete_report.docx'
    result = renderer.render(report_data, output_path)
    
    print(f"✓ Complete report generated: {result}")
    print()


if __name__ == '__main__':
    example_1_basic_report()
    example_2_with_images()
    example_3_with_tables()
    example_4_custom_styles()
    example_5_complete_report()
    
    print("=" * 60)
    print("All renderer examples completed!")
    print("Check output/ directory for generated reports")
    print("=" * 60)
