"""
PDF Renderer Demo
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from source.renderers import PDFReportRenderer


def main():
    print("PDF Renderer Demo")
    print("=" * 60)
    
    renderer = PDFReportRenderer()
    
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
                'title': 'TABLE OF CONTENTS'
            },
            {
                'type': 'acknowledgment',
                'title': 'ACKNOWLEDGMENT',
                'level': 1,
                'content': 'We would like to thank our advisor for guidance and support.'
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
                        'content': 'Search algorithms are fundamental to computer science and are used in various applications.'
                    },
                    {
                        'id': 'intro_objectives',
                        'title': 'Objectives',
                        'level': 2,
                        'content': 'The main objectives are:\n- Compare algorithm performance\n- Analyze time complexity\n- Provide implementation examples'
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
                        'content': 'The experimental results show significant differences between algorithms.'
                    }
                ]
            },
            {
                'type': 'conclusion',
                'title': 'CONCLUSION',
                'level': 1,
                'content': 'This study successfully compared three search algorithms and identified their strengths and weaknesses. A* algorithm showed the best overall performance.'
            },
            {
                'type': 'references',
                'title': 'REFERENCES',
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
                    'caption': 'Algorithm execution time comparison'
                }
            ],
            'tables': [
                {
                    'section_id': 'results_performance',
                    'headers': ['Algorithm', 'Time (ms)', 'Memory (MB)', 'Optimal'],
                    'rows': [
                        ['BFS', '120', '45', 'Yes'],
                        ['DFS', '95', '30', 'No'],
                        ['A*', '85', '50', 'Yes']
                    ],
                    'caption': 'Performance comparison metrics'
                }
            ]
        }
    }
    
    output_path = 'output/demo_report.pdf'
    result = renderer.render(report_data, output_path)
    
    print(f"✓ PDF report generated: {result}")
    print("\n" + "=" * 60)
    print("Demo completed!")


if __name__ == '__main__':
    main()
