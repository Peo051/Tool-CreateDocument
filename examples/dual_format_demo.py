"""
Dual Format Demo - Generate both DOCX and PDF
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from source.renderers import ReportRenderer, PDFReportRenderer


def main():
    print("Dual Format Demo - DOCX and PDF")
    print("=" * 60)
    
    # Shared report data
    report_data = {
        'metadata': {
            'title': 'Algorithm Performance Study',
            'organization': 'Tech University',
            'faculty': 'Computer Engineering',
            'advisor': 'Prof. Sarah Johnson',
            'students': [
                {'name': 'Charlie Brown', 'id': '2021003'}
            ],
            'class_name': 'CE502',
            'report_type': 'technical_report'
        },
        'sections': [
            {
                'type': 'cover',
                'title': 'Cover'
            },
            {
                'type': 'chapter',
                'title': 'INTRODUCTION',
                'level': 1,
                'content': 'This study analyzes search algorithm performance.',
                'subsections': [
                    {
                        'id': 'intro_scope',
                        'title': 'Scope',
                        'level': 2,
                        'content': 'We focus on BFS, DFS, and A* algorithms.'
                    }
                ]
            },
            {
                'type': 'chapter',
                'title': 'RESULTS',
                'level': 1,
                'subsections': [
                    {
                        'id': 'results_data',
                        'title': 'Experimental Data',
                        'level': 2,
                        'content': 'Performance metrics are shown below.'
                    }
                ]
            },
            {
                'type': 'conclusion',
                'title': 'CONCLUSION',
                'level': 1,
                'content': 'A* algorithm provides optimal performance.'
            }
        ],
        'evidence': {
            'figures': [
                {
                    'section_id': 'results_data',
                    'path': 'output/charts/algo_performance.png',
                    'caption': 'Performance comparison'
                }
            ],
            'tables': [
                {
                    'section_id': 'results_data',
                    'headers': ['Algorithm', 'Time (ms)', 'Memory (MB)'],
                    'rows': [
                        ['BFS', '120', '45'],
                        ['DFS', '95', '30'],
                        ['A*', '85', '50']
                    ],
                    'caption': 'Performance metrics'
                }
            ]
        }
    }
    
    # Generate DOCX
    print("Generating DOCX...")
    docx_renderer = ReportRenderer()
    docx_path = docx_renderer.render(report_data, 'output/dual_format_report.docx')
    print(f"✓ DOCX generated: {docx_path}")
    
    # Generate PDF
    print("\nGenerating PDF...")
    pdf_renderer = PDFReportRenderer()
    pdf_path = pdf_renderer.render(report_data, 'output/dual_format_report.pdf')
    print(f"✓ PDF generated: {pdf_path}")
    
    print("\n" + "=" * 60)
    print("Both formats generated successfully!")
    print(f"DOCX: {docx_path}")
    print(f"PDF:  {pdf_path}")


if __name__ == '__main__':
    main()
