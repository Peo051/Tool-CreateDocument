"""
Review Integration Demo
Shows how to integrate review engine with report generation pipeline
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from source.review import ReviewEngine, ReviewReport
from source.generators import IntroductionGenerator, ConclusionGenerator


def example_integration():
    """Example: Integrate review with generation pipeline"""
    print("=" * 60)
    print("Review Integration with Pipeline")
    print("=" * 60)
    
    # Step 1: Generate content
    print("\n1. Generating content...")
    
    intro_gen = IntroductionGenerator()
    intro_section = intro_gen.generate({
        'title': 'Algorithm Performance Study',
        'domain': 'Computer Science',
        'context': 'Search algorithms are fundamental to many applications.',
        'objectives': [
            'Compare BFS, DFS, and A* algorithms',
            'Analyze time and space complexity',
            'Provide implementation examples'
        ]
    })
    
    conclusion_gen = ConclusionGenerator()
    conclusion_section = conclusion_gen.generate({
        'summary': 'We compared three search algorithms',
        'findings': [
            'A* provides optimal paths',
            'BFS guarantees shortest path',
            'DFS uses less memory'
        ],
        'future_work': [
            'Test on larger graphs',
            'Implement bidirectional search'
        ]
    })
    
    print("✓ Content generated")
    
    # Step 2: Build report data
    print("\n2. Building report structure...")
    
    report_data = {
        'metadata': {
            'title': 'Algorithm Performance Study',
            'organization': 'Tech University',
            'faculty': 'Computer Science',
            'students': [{'name': 'John Doe', 'id': '123456'}],
            'report_type': 'project_report'
        },
        'sections': [
            {'type': 'cover', 'title': 'Cover'},
            {'type': 'toc', 'title': 'Table of Contents'},
            {
                'type': 'chapter',
                'title': intro_section.title,
                'content': intro_section.content,
                'subsections': [
                    {
                        'id': f'intro_{i}',
                        'title': sub.title,
                        'content': sub.content,
                        'level': sub.level
                    }
                    for i, sub in enumerate(intro_section.subsections)
                ]
            },
            {
                'type': 'chapter',
                'title': 'METHODOLOGY',
                'content': 'We conducted experimental analysis on various graph structures.',
                'subsections': [
                    {
                        'id': 'method_1',
                        'title': 'Experimental Setup',
                        'content': 'Tests were run on graphs with 100 to 10000 nodes.'
                    }
                ]
            },
            {
                'type': 'chapter',
                'title': 'RESULTS',
                'content': 'The experimental results are presented below.',
                'subsections': [
                    {
                        'id': 'results_perf',
                        'title': 'Performance Metrics',
                        'content': 'A* achieved 85ms, BFS 120ms, and DFS 95ms execution time.'
                    }
                ]
            },
            {
                'type': 'conclusion',
                'title': conclusion_section.title,
                'content': conclusion_section.content
            },
            {
                'type': 'references',
                'title': 'REFERENCES',
                'references': [
                    'Russell, S., & Norvig, P. (2020). Artificial Intelligence.',
                    'Cormen, T. H., et al. (2009). Introduction to Algorithms.'
                ]
            }
        ],
        'evidence': {
            'figures': [
                {
                    'section_id': 'results_perf',
                    'path': 'output/charts/algo_performance.png',
                    'caption': 'Algorithm execution time comparison'
                }
            ],
            'tables': [
                {
                    'section_id': 'results_perf',
                    'headers': ['Algorithm', 'Time (ms)', 'Memory (MB)'],
                    'rows': [
                        ['BFS', '120', '45'],
                        ['DFS', '95', '30'],
                        ['A*', '85', '50']
                    ],
                    'caption': 'Performance comparison'
                }
            ]
        }
    }
    
    print("✓ Report structure built")
    
    # Step 3: Review report
    print("\n3. Reviewing report quality...")
    
    engine = ReviewEngine()
    result = engine.review(report_data)
    
    print(f"✓ Review completed: {result.summary()}")
    
    # Step 4: Display results
    print("\n4. Review Results:")
    print("-" * 60)
    print(ReviewReport.format_text(result))
    
    # Step 5: Decision based on review
    print("\n5. Decision:")
    if result.passed:
        print("✓ Report passed review - ready for rendering")
        print("  Next steps:")
        print("  - Render to DOCX: renderer.render(report_data, 'output.docx')")
        print("  - Render to PDF: pdf_renderer.render(report_data, 'output.pdf')")
    else:
        print("✗ Report failed review - fix errors before rendering")
        print(f"  Found {result.errors} errors that must be fixed")
        print("  Review the issues above and update report data")
    
    print()


if __name__ == '__main__':
    example_integration()
    
    print("=" * 60)
    print("Integration demo completed!")
    print("=" * 60)
