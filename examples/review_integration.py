"""
Review Engine Integration with Report Generation Pipeline
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from source.review import ReviewEngine, Severity
from source.renderers import ReportRenderer, PDFReportRenderer


def generate_and_review_report():
    """Complete workflow: generate, review, render"""
    print("Complete Report Generation with Review")
    print("=" * 60)
    
    # Step 1: Prepare report data
    print("\n1. Preparing report data...")
    report_data = {
        'metadata': {
            'title': 'Search Algorithm Comparison',
            'organization': 'Tech University',
            'faculty': 'Computer Science',
            'advisor': 'Dr. Smith',
            'students': [{'name': 'Alice Johnson', 'id': '2021001'}],
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
                'content': 'We thank our advisor Dr. Smith for guidance and support throughout this project.'
            },
            {
                'type': 'chapter',
                'title': 'INTRODUCTION',
                'level': 1,
                'content': 'This study analyzes and compares three fundamental search algorithms: BFS, DFS, and A*.',
                'subsections': [
                    {
                        'id': 'intro_background',
                        'title': 'Background',
                        'level': 2,
                        'content': 'Search algorithms are essential in computer science for pathfinding, game AI, and optimization problems.'
                    },
                    {
                        'id': 'intro_objectives',
                        'title': 'Objectives',
                        'level': 2,
                        'content': 'The main objectives are to compare algorithm performance, analyze time complexity, and provide implementation examples.'
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
                        'content': 'We conducted experimental analysis on various graph structures with different sizes and complexities.'
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
                        'content': 'Our experiments show that A* achieves 85ms execution time, outperforming BFS (120ms) and DFS (95ms).'
                    }
                ]
            },
            {
                'type': 'conclusion',
                'title': 'CONCLUSION',
                'level': 1,
                'content': 'This study successfully compared three search algorithms. The results demonstrate that A* provides optimal performance with 85ms execution time.'
            },
            {
                'type': 'references',
                'title': 'REFERENCES',
                'references': [
                    'Russell, S., & Norvig, P. (2020). Artificial Intelligence: A Modern Approach.',
                    'Cormen, T. H., et al. (2009). Introduction to Algorithms.'
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
                    'headers': ['Algorithm', 'Time (ms)', 'Memory (MB)'],
                    'rows': [
                        ['BFS', '120', '45'],
                        ['DFS', '95', '30'],
                        ['A*', '85', '50']
                    ],
                    'caption': 'Performance metrics comparison'
                }
            ]
        }
    }
    
    print("✓ Report data prepared")
    
    # Step 2: Review report
    print("\n2. Reviewing report quality...")
    engine = ReviewEngine()
    review_result = engine.review(report_data)
    
    print(f"   {review_result.summary()}")
    
    # Step 3: Check review results
    print("\n3. Checking review results...")
    
    if review_result.errors > 0:
        print("   ❌ ERRORS found - cannot proceed with rendering:")
        for issue in review_result.get_issues_by_severity(Severity.ERROR):
            print(f"      - {issue.message}")
        return False
    
    if review_result.warnings > 0:
        print(f"   ⚠️  {review_result.warnings} WARNINGS found:")
        for issue in review_result.get_issues_by_severity(Severity.WARNING):
            print(f"      - {issue.message}")
        print("   → Proceeding with rendering (warnings are non-blocking)")
    
    if review_result.infos > 0:
        print(f"   ℹ️  {review_result.infos} INFO messages:")
        for issue in review_result.get_issues_by_severity(Severity.INFO):
            print(f"      - {issue.message}")
    
    if review_result.passed and review_result.total_issues == 0:
        print("   ✓ No issues found - report is perfect!")
    
    # Step 4: Render report
    print("\n4. Rendering report...")
    
    # Render DOCX
    docx_renderer = ReportRenderer()
    docx_path = docx_renderer.render(report_data, 'output/reviewed_report.docx')
    print(f"   ✓ DOCX: {docx_path}")
    
    # Render PDF
    pdf_renderer = PDFReportRenderer()
    pdf_path = pdf_renderer.render(report_data, 'output/reviewed_report.pdf')
    print(f"   ✓ PDF:  {pdf_path}")
    
    # Step 5: Save review report
    print("\n5. Saving review report...")
    import json
    review_path = 'output/review_report.json'
    with open(review_path, 'w') as f:
        json.dump(review_result.to_dict(), f, indent=2)
    print(f"   ✓ Review: {review_path}")
    
    print("\n" + "=" * 60)
    print("✓ Complete workflow finished successfully!")
    print("=" * 60)
    
    return True


if __name__ == '__main__':
    generate_and_review_report()
