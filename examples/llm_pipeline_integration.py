"""
LLM Pipeline Integration Example
Shows how to integrate LLM enhancement into the full report generation pipeline
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from source.llm import create_enhancer
from source.generators import (
    IntroductionGenerator,
    ProblemStatementGenerator,
    MethodologyGenerator,
    ConclusionGenerator
)
from source.generators.llm_helper import (
    create_generator_with_llm,
    enhance_section_post_generation,
    batch_enhance_sections
)


def example_1_pipeline_with_llm():
    """Example 1: Generate report sections with LLM enhancement"""
    print("=" * 60)
    print("Example 1: Pipeline with LLM Enhancement")
    print("=" * 60)
    
    # Configuration
    llm_config = {
        'enabled': True,
        'provider': 'mock',
        'prefix': '[AI Enhanced] '
    }
    
    # Create generators with LLM
    intro_gen = create_generator_with_llm(IntroductionGenerator, llm_config)
    problem_gen = create_generator_with_llm(ProblemStatementGenerator, llm_config)
    method_gen = create_generator_with_llm(MethodologyGenerator, llm_config)
    conclusion_gen = create_generator_with_llm(ConclusionGenerator, llm_config)
    
    # Generate sections
    intro = intro_gen.generate({
        'title': 'Search Algorithm Comparison',
        'domain': 'Artificial Intelligence',
        'objectives': ['Compare algorithms', 'Analyze performance']
    })
    
    problem = problem_gen.generate({
        'problem': 'Finding optimal paths in graphs',
        'challenges': ['Large search spaces', 'Time complexity'],
        'importance': 'Critical for navigation systems'
    })
    
    method = method_gen.generate({
        'approach': 'Comparative analysis',
        'algorithms': ['BFS', 'DFS', 'A*'],
        'metrics': ['Time', 'Space', 'Optimality']
    })
    
    conclusion = conclusion_gen.generate({
        'summary': 'Compared three search algorithms',
        'findings': ['A* is optimal', 'BFS guarantees shortest path'],
        'future_work': ['Test on larger graphs', 'Implement variants']
    })
    
    print(f"✓ Generated {len([intro, problem, method, conclusion])} sections")
    print(f"✓ Introduction: {len(intro.content)} chars")
    print(f"✓ Problem: {len(problem.content)} chars")
    print(f"✓ Methodology: {len(method.content)} chars")
    print(f"✓ Conclusion: {len(conclusion.content)} chars")
    print()


def example_2_selective_enhancement():
    """Example 2: Generate without LLM, enhance selectively"""
    print("=" * 60)
    print("Example 2: Selective Enhancement")
    print("=" * 60)
    
    # Generate without LLM (faster, cheaper)
    intro_gen = IntroductionGenerator()
    problem_gen = ProblemStatementGenerator()
    
    intro = intro_gen.generate({
        'title': 'Machine Learning Project',
        'domain': 'Data Science',
        'objectives': ['Build model', 'Evaluate performance']
    })
    
    problem = problem_gen.generate({
        'problem': 'Predicting customer churn',
        'challenges': ['Imbalanced data', 'Feature selection'],
        'importance': 'Reduce customer loss'
    })
    
    print(f"✓ Generated sections without LLM")
    print(f"  Original intro: {len(intro.content)} chars")
    print(f"  Original problem: {len(problem.content)} chars")
    
    # Enhance only important sections
    llm_config = {'enabled': True, 'provider': 'mock', 'prefix': '[Enhanced] '}
    
    enhanced_intro = enhance_section_post_generation(intro, llm_config)
    # Don't enhance problem section (keep original)
    
    print(f"✓ Enhanced introduction")
    print(f"  Enhanced intro: {len(enhanced_intro.content)} chars")
    print(f"  Problem unchanged: {len(problem.content)} chars")
    print()


def example_3_batch_enhancement():
    """Example 3: Generate all sections, then batch enhance"""
    print("=" * 60)
    print("Example 3: Batch Enhancement")
    print("=" * 60)
    
    # Generate all sections without LLM
    generators = [
        (IntroductionGenerator(), {
            'title': 'Web Application',
            'domain': 'Software Engineering',
            'objectives': ['Build scalable app']
        }),
        (ProblemStatementGenerator(), {
            'problem': 'Slow page load times',
            'challenges': ['Large assets', 'Database queries'],
            'importance': 'User experience'
        }),
        (ConclusionGenerator(), {
            'summary': 'Optimized web application',
            'findings': ['Reduced load time by 50%'],
            'future_work': ['Add caching', 'Optimize images']
        })
    ]
    
    sections = [gen.generate(data) for gen, data in generators]
    
    print(f"✓ Generated {len(sections)} sections")
    for i, section in enumerate(sections, 1):
        print(f"  {i}. {section.title}: {len(section.content)} chars")
    
    # Batch enhance all sections
    llm_config = {'enabled': True, 'provider': 'mock', 'prefix': '[Pro] '}
    enhanced_sections = batch_enhance_sections(sections, llm_config)
    
    print(f"✓ Enhanced {len(enhanced_sections)} sections")
    for i, section in enumerate(enhanced_sections, 1):
        print(f"  {i}. {section.title}: {len(section.content)} chars")
    print()


def example_4_conditional_enhancement():
    """Example 4: Enable LLM based on configuration"""
    print("=" * 60)
    print("Example 4: Conditional Enhancement")
    print("=" * 60)
    
    # Simulate loading from config file
    configs = [
        {'use_llm': False, 'provider': None},
        {'use_llm': True, 'provider': 'mock', 'prefix': '[AI] '}
    ]
    
    for i, config in enumerate(configs, 1):
        print(f"\nConfiguration {i}: use_llm={config['use_llm']}")
        
        llm_config = {
            'enabled': config['use_llm'],
            'provider': config.get('provider'),
            'prefix': config.get('prefix', '')
        }
        
        generator = create_generator_with_llm(
            IntroductionGenerator,
            llm_config=llm_config
        )
        
        section = generator.generate({
            'title': 'Test Project',
            'domain': 'Testing',
            'objectives': ['Test LLM integration']
        })
        
        print(f"  Generated: {section.title}")
        print(f"  Content length: {len(section.content)} chars")
        print(f"  Enhanced: {section.metadata.get('enhanced', False)}")
    
    print()


def example_5_error_handling():
    """Example 5: Handle LLM failures gracefully"""
    print("=" * 60)
    print("Example 5: Error Handling")
    print("=" * 60)
    
    # Try with unavailable provider
    llm_config = {
        'enabled': True,
        'provider': 'openai',  # Not configured
    }
    
    generator = create_generator_with_llm(
        IntroductionGenerator,
        llm_config=llm_config
    )
    
    # Should still work (fallback to no enhancement)
    section = generator.generate({
        'title': 'Resilient System',
        'domain': 'Software Engineering',
        'objectives': ['Handle failures gracefully']
    })
    
    print(f"✓ Generated section despite LLM unavailable")
    print(f"  Title: {section.title}")
    print(f"  Content: {len(section.content)} chars")
    print(f"  System continued working!")
    print()


def example_6_performance_comparison():
    """Example 6: Compare performance with/without LLM"""
    print("=" * 60)
    print("Example 6: Performance Comparison")
    print("=" * 60)
    
    import time
    
    input_data = {
        'title': 'Performance Test',
        'domain': 'Testing',
        'objectives': ['Measure speed', 'Compare approaches']
    }
    
    # Without LLM
    start = time.time()
    gen_no_llm = IntroductionGenerator()
    section_no_llm = gen_no_llm.generate(input_data)
    time_no_llm = time.time() - start
    
    # With LLM (mock)
    start = time.time()
    llm_config = {'enabled': True, 'provider': 'mock'}
    gen_with_llm = create_generator_with_llm(IntroductionGenerator, llm_config)
    section_with_llm = gen_with_llm.generate(input_data)
    time_with_llm = time.time() - start
    
    print(f"Without LLM: {time_no_llm*1000:.2f}ms")
    print(f"With LLM:    {time_with_llm*1000:.2f}ms")
    print(f"Overhead:    {(time_with_llm - time_no_llm)*1000:.2f}ms")
    print()


if __name__ == '__main__':
    example_1_pipeline_with_llm()
    example_2_selective_enhancement()
    example_3_batch_enhancement()
    example_4_conditional_enhancement()
    example_5_error_handling()
    example_6_performance_comparison()
    
    print("=" * 60)
    print("All pipeline integration examples completed!")
    print("=" * 60)
