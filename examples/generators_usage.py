#!/usr/bin/env python3
"""
Section Generators Usage Examples
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

from generators import (
    IntroductionGenerator,
    ProblemStatementGenerator,
    MethodologyGenerator,
    ImplementationGenerator,
    ExperimentsGenerator,
    ResultsAnalysisGenerator,
    ConclusionGenerator
)


def example_introduction():
    """Generate introduction section"""
    print("="*60)
    print("1. Introduction Generator")
    print("="*60)
    
    gen = IntroductionGenerator()
    
    input_data = {
        'title': 'AI-Powered Maze Game',
        'domain': 'Artificial Intelligence',
        'context': 'Game AI has become increasingly important in modern game development.',
        'motivation': 'This project explores practical AI algorithms in a game environment.',
        'objectives': [
            'Implement pathfinding algorithms',
            'Create intelligent AI opponents',
            'Evaluate algorithm performance'
        ],
        'scope': 'The project focuses on 2D maze navigation with multiple AI agents.'
    }
    
    section = gen.generate(input_data)
    
    print(f"\nTitle: {section.title}")
    print(f"Subsections: {len(section.subsections)}")
    for sub in section.subsections:
        print(f"  - {sub.title}")
    print(f"\nContent preview:\n{section.content[:200]}...")


def example_problem_statement():
    """Generate problem statement section"""
    print("\n" + "="*60)
    print("2. Problem Statement Generator")
    print("="*60)
    
    gen = ProblemStatementGenerator()
    
    input_data = {
        'problem': 'Traditional game AI often uses simple heuristics that are predictable.',
        'challenges': [
            'Creating challenging but fair AI opponents',
            'Balancing performance with intelligence',
            'Handling dynamic game states'
        ],
        'current_solutions': [
            {
                'name': 'Rule-based AI',
                'description': 'Uses predefined rules',
                'limitations': ['Predictable', 'Not adaptive']
            }
        ],
        'gaps': [
            'Lack of learning capabilities',
            'Poor performance in complex scenarios'
        ]
    }
    
    section = gen.generate(input_data)
    
    print(f"\nTitle: {section.title}")
    print(f"Subsections: {len(section.subsections)}")
    print(f"Content preview:\n{section.content[:200]}...")


def example_methodology():
    """Generate methodology section"""
    print("\n" + "="*60)
    print("3. Methodology Generator")
    print("="*60)
    
    gen = MethodologyGenerator()
    
    input_data = {
        'approach': 'We employ a multi-algorithm approach combining search and optimization.',
        'algorithms': [
            {
                'name': 'A*',
                'purpose': 'Pathfinding',
                'complexity': 'O(E log V)'
            },
            {
                'name': 'Minimax',
                'purpose': 'Decision making',
                'complexity': 'O(b^d)'
            }
        ],
        'tools': ['Python', 'NetworkX', 'Pygame'],
        'workflow': [
            'Design algorithms',
            'Implement core logic',
            'Test and optimize',
            'Evaluate performance'
        ]
    }
    
    section = gen.generate(input_data)
    
    print(f"\nTitle: {section.title}")
    print(f"Subsections: {len(section.subsections)}")
    for sub in section.subsections:
        print(f"  - {sub.title}")


def example_implementation():
    """Generate implementation section"""
    print("\n" + "="*60)
    print("4. Implementation Generator")
    print("="*60)
    
    gen = ImplementationGenerator()
    
    input_data = {
        'overview': 'The system is implemented using modular architecture.',
        'components': [
            {
                'name': 'PathFinder',
                'description': 'Handles pathfinding algorithms',
                'responsibilities': ['A* search', 'Path optimization']
            },
            {
                'name': 'AIAgent',
                'description': 'Controls AI behavior',
                'responsibilities': ['Decision making', 'State management']
            }
        ],
        'features': [
            'Real-time pathfinding',
            'Multiple AI difficulty levels',
            'Performance monitoring'
        ],
        'technologies': ['Python 3.10', 'Pygame 2.0', 'NumPy']
    }
    
    section = gen.generate(input_data)
    
    print(f"\nTitle: {section.title}")
    print(f"Components: {section.metadata['components_count']}")
    print(f"Features: {section.metadata['features_count']}")


def example_experiments():
    """Generate experiments section"""
    print("\n" + "="*60)
    print("5. Experiments Generator")
    print("="*60)
    
    gen = ExperimentsGenerator()
    
    input_data = {
        'overview': 'We conducted experiments to evaluate algorithm performance.',
        'environment': {
            'hardware': 'Intel i7, 16GB RAM',
            'software': 'Python 3.10',
            'os': 'Windows 11'
        },
        'metrics': [
            {
                'name': 'Execution Time',
                'description': 'Time to find path',
                'formula': 't_end - t_start'
            },
            'Path Length',
            'Memory Usage'
        ],
        'experiments': [
            {
                'name': 'Algorithm Comparison',
                'description': 'Compare A* vs Dijkstra',
                'results': 'A* was 30% faster'
            }
        ]
    }
    
    section = gen.generate(input_data)
    
    print(f"\nTitle: {section.title}")
    print(f"Experiments: {section.metadata['experiments_count']}")
    print(f"Metrics: {section.metadata['metrics_count']}")


def example_results():
    """Generate results analysis section"""
    print("\n" + "="*60)
    print("6. Results Analysis Generator")
    print("="*60)
    
    gen = ResultsAnalysisGenerator()
    
    input_data = {
        'overview': 'Results show significant improvements over baseline.',
        'findings': [
            'A* outperforms Dijkstra by 30%',
            'Memory usage is acceptable',
            'AI difficulty scales well'
        ],
        'performance': {
            'avg_time': '15ms',
            'max_time': '50ms',
            'memory': '120MB'
        },
        'comparisons': [
            {
                'baseline': 'Dijkstra',
                'our_approach': 'A*',
                'metric': 'Execution time',
                'improvement': '30% faster'
            }
        ]
    }
    
    section = gen.generate(input_data)
    
    print(f"\nTitle: {section.title}")
    print(f"Findings: {section.metadata['findings_count']}")
    print(f"Comparisons: {section.metadata['comparisons_count']}")


def example_conclusion():
    """Generate conclusion section"""
    print("\n" + "="*60)
    print("7. Conclusion Generator")
    print("="*60)
    
    gen = ConclusionGenerator()
    
    input_data = {
        'summary': 'This project successfully implemented AI algorithms for game navigation.',
        'achievements': [
            'Implemented 5 pathfinding algorithms',
            'Created scalable AI system',
            'Achieved real-time performance'
        ],
        'contributions': [
            'Comparative analysis of algorithms',
            'Optimized implementation'
        ],
        'future_work': [
            'Add machine learning',
            'Implement multiplayer',
            'Optimize for mobile'
        ]
    }
    
    section = gen.generate(input_data)
    
    print(f"\nTitle: {section.title}")
    print(f"Achievements: {section.metadata['achievements_count']}")
    print(f"Future work: {section.metadata['future_work_count']}")


def example_export():
    """Export section to dict"""
    print("\n" + "="*60)
    print("8. Export to Dictionary")
    print("="*60)
    
    gen = IntroductionGenerator()
    
    input_data = {
        'title': 'Test Project',
        'domain': 'AI',
        'objectives': ['Objective 1', 'Objective 2']
    }
    
    section = gen.generate(input_data)
    data = section.to_dict()
    
    print(f"\nExported keys: {list(data.keys())}")
    print(f"Subsections: {len(data['subsections'])}")


def main():
    print("\nSection Generators Usage Examples\n")
    
    example_introduction()
    example_problem_statement()
    example_methodology()
    example_implementation()
    example_experiments()
    example_results()
    example_conclusion()
    example_export()
    
    print("\n" + "="*60)
    print("✅ All examples completed!")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
