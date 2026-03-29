"""
Quick Renderer Demo
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from source.renderers import ReportRenderer


def main():
    print("Report Renderer Quick Demo")
    print("=" * 60)
    
    renderer = ReportRenderer()
    
    report_data = {
        'metadata': {
            'title': 'Quick Demo Report',
            'organization': 'Demo University',
            'faculty': 'Computer Science',
            'students': [{'name': 'Demo Student', 'id': '123456'}]
        },
        'sections': [
            {
                'type': 'cover',
                'title': 'Cover'
            },
            {
                'type': 'toc',
                'title': 'TABLE OF CONTENTS'
            },
            {
                'type': 'chapter',
                'title': 'INTRODUCTION',
                'level': 1,
                'content': 'This is a quick demonstration of the report renderer.',
                'subsections': [
                    {
                        'id': 'intro_purpose',
                        'title': 'Purpose',
                        'level': 2,
                        'content': 'To demonstrate basic rendering capabilities.'
                    }
                ]
            },
            {
                'type': 'conclusion',
                'title': 'CONCLUSION',
                'level': 1,
                'content': 'The renderer works as expected.'
            }
        ],
        'evidence': {'figures': [], 'tables': []}
    }
    
    output_path = 'output/quick_demo_report.docx'
    result = renderer.render(report_data, output_path)
    
    print(f"✓ Report generated: {result}")
    print("\n" + "=" * 60)
    print("Demo completed!")


if __name__ == '__main__':
    main()
