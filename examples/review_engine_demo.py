"""
Review Engine Demo
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from source.review import ReviewEngine, ReviewReport


def example_1_good_report():
    """Example 1: Review a good report"""
    print("=" * 60)
    print("Example 1: Good Report")
    print("=" * 60)
    
    report_data = {
        'metadata': {
            'title': 'Search Algorithm Comparison',
            'report_type': 'project_report'
        },
        'sections': [
            {'type': 'cover', 'title': 'Cover'},
            {'type': 'toc', 'title': 'Table of Contents'},
            {
                'type': 'chapter',
                'title': 'CHƯƠNG 1. INTRODUCTION',
                'content': 'This report presents a comprehensive analysis of search algorithms including BFS, DFS, and A*.',
                'subsections': [
                    {
                        'id': 'intro_background',
                        'title': 'Background',
                        'content': 'Search algorithms are fundamental to computer science and have wide applications.'
                    }
                ]
            },
            {
                'type': 'chapter',
                'title': 'CHƯƠNG 2. RESULTS',
                'content': 'The experimental results show that A* algorithm performs best.',
                'subsections': [
                    {
                        'id': 'results_data',
                        'title': 'Performance Data',
                        'content': 'We tested three algorithms: BFS achieved 120ms, DFS 95ms, and A* 85ms execution time.'
                    }
                ]
            },
            {
                'type': 'conclusion',
                'title': 'CONCLUSION',
                'content': 'Based on the results, A* algorithm provides the best performance with 85ms execution time. The findings show significant improvements over traditional approaches.'
            },
            {
                'type': 'references',
                'title': 'REFERENCES',
                'references': [
                    'Russell, S., & Norvig, P. (2020). Artificial Intelligence [1].',
                    'Cormen, T. H., et al. (2009). Introduction to Algorithms [2].'
                ]
            }
        ],
        'evidence': {
            'figures': [
                {
                    'section_id': 'results_data',
                    'path': 'charts/performance.png',
                    'caption': 'Algorithm performance comparison'
                }
            ],
            'tables': [
                {
                    'section_id': 'results_data',
                    'headers': ['Algorithm', 'Time'],
                    'rows': [['BFS', '120ms'], ['DFS', '95ms']],
                    'caption': 'Performance metrics'
                }
            ]
        }
    }
    
    engine = ReviewEngine()
    result = engine.review(report_data)
    
    print(ReviewReport.format_text(result))
    print()


def example_2_problematic_report():
    """Example 2: Review a problematic report"""
    print("=" * 60)
    print("Example 2: Problematic Report")
    print("=" * 60)
    
    report_data = {
        'metadata': {
            'title': 'Incomplete Report',
            'report_type': 'thesis'
        },
        'sections': [
            {'type': 'cover', 'title': 'Cover'},
            # Missing: acknowledgment, toc
            {
                'type': 'chapter',
                'title': 'Introduction',  # Missing chapter number
                'content': 'Short.',  # Too short
                'subsections': []
            },
            {
                'type': 'chapter',
                'title': 'Introduction',  # Duplicate title
                'content': '',  # Empty
                'subsections': []
            },
            {
                'type': 'conclusion',
                'title': 'Conclusion',
                'content': 'The end.'  # No reference to results
            }
            # Missing: references
        ],
        'evidence': {
            'figures': [
                {
                    'section_id': 'intro',
                    'path': 'chart.png'
                    # Missing caption
                }
            ],
            'tables': []
        }
    }
    
    engine = ReviewEngine()
    result = engine.review(report_data)
    
    print(ReviewReport.format_text(result))
    print()


def example_3_custom_check():
    """Example 3: Add custom check"""
    print("=" * 60)
    print("Example 3: Custom Check")
    print("=" * 60)
    
    from source.review import BaseCheck, ReviewIssue, Severity, CheckType
    
    class CustomTitleCheck(BaseCheck):
        """Check if title is too short"""
        def check(self, report_data):
            issues = []
            title = report_data.get('metadata', {}).get('title', '')
            if len(title) < 10:
                issues.append(ReviewIssue(
                    check_type=CheckType.CONTENT,
                    severity=Severity.WARNING,
                    message=f"Report title is too short: '{title}'",
                    details={'title_length': len(title)}
                ))
            return issues
    
    report_data = {
        'metadata': {
            'title': 'Short',
            'report_type': 'project_report'
        },
        'sections': [
            {'type': 'cover', 'title': 'Cover'},
            {'type': 'toc', 'title': 'TOC'},
            {'type': 'chapter', 'title': 'Chapter 1', 'content': 'Content here.'},
            {'type': 'conclusion', 'title': 'Conclusion', 'content': 'Done.'},
            {'type': 'references', 'title': 'References', 'references': ['Ref 1']}
        ],
        'evidence': {'figures': [], 'tables': []}
    }
    
    engine = ReviewEngine()
    engine.add_check(CustomTitleCheck)
    
    print(f"Running {len(engine.get_checks())} checks:")
    for check_name in engine.get_checks():
        print(f"  - {check_name}")
    print()
    
    result = engine.review(report_data)
    print(ReviewReport.format_text(result))
    print()


def example_4_json_output():
    """Example 4: JSON output"""
    print("=" * 60)
    print("Example 4: JSON Output")
    print("=" * 60)
    
    import json
    
    report_data = {
        'metadata': {
            'title': 'Test Report',
            'report_type': 'project_report'
        },
        'sections': [
            {'type': 'cover', 'title': 'Cover'},
            {'type': 'chapter', 'title': 'Chapter', 'content': ''},  # Empty
        ],
        'evidence': {'figures': [], 'tables': []}
    }
    
    engine = ReviewEngine()
    result = engine.review(report_data)
    
    json_output = ReviewReport.format_json(result)
    print(json.dumps(json_output, indent=2))
    print()


if __name__ == '__main__':
    example_1_good_report()
    example_2_problematic_report()
    example_3_custom_check()
    example_4_json_output()
    
    print("=" * 60)
    print("All review examples completed!")
    print("=" * 60)
