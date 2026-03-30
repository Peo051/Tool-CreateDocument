"""
Test section generators
"""

import pytest
from source.generators.base import GeneratedSection
from source.generators.introduction import IntroductionGenerator
from source.generators.problem_statement import ProblemStatementGenerator
from source.generators.methodology import MethodologyGenerator
from source.generators.conclusion import ConclusionGenerator


def test_introduction_generator():
    """Test introduction generator"""
    gen = IntroductionGenerator()
    input_data = {
        'project_title': 'Test Project',
        'project_description': 'A test project for validation',
        'objectives': ['Objective 1', 'Objective 2'],
        'scope': 'Project scope description'
    }
    result = gen.generate(input_data)
    
    assert isinstance(result, GeneratedSection)
    assert result.title == 'Introduction'
    assert len(result.content) > 0
    assert len(result.subsections) > 0


def test_problem_statement_generator():
    """Test problem statement generator"""
    gen = ProblemStatementGenerator()
    input_data = {
        'problem_description': 'The problem we are solving',
        'current_situation': 'Current state analysis',
        'challenges': ['Challenge 1', 'Challenge 2']
    }
    result = gen.generate(input_data)
    
    assert isinstance(result, GeneratedSection)
    assert result.title == 'Problem Statement'
    assert len(result.content) > 0


def test_methodology_generator():
    """Test methodology generator"""
    gen = MethodologyGenerator()
    input_data = {
        'approach': 'Our approach to solving the problem',
        'algorithms': ['BFS', 'DFS', 'A*'],
        'technologies': ['Python', 'pytest'],
        'development_process': 'Agile methodology'
    }
    result = gen.generate(input_data)
    
    assert isinstance(result, GeneratedSection)
    assert result.title == 'Methodology'
    assert len(result.subsections) > 0


def test_conclusion_generator():
    """Test conclusion generator"""
    gen = ConclusionGenerator()
    input_data = {
        'achievements': ['Achievement 1', 'Achievement 2'],
        'limitations': ['Limitation 1'],
        'future_work': ['Future work 1', 'Future work 2']
    }
    result = gen.generate(input_data)
    
    assert isinstance(result, GeneratedSection)
    assert result.title == 'Conclusion'
    assert len(result.subsections) > 0


def test_generator_with_empty_input():
    """Test generators handle empty input gracefully"""
    gen = IntroductionGenerator()
    result = gen.generate({})
    
    assert isinstance(result, GeneratedSection)
    assert result.title == 'Introduction'
    # Should still generate something, even if minimal


def test_generated_section_structure():
    """Test generated section has correct structure"""
    gen = IntroductionGenerator()
    input_data = {
        'project_title': 'Test',
        'objectives': ['Obj 1']
    }
    result = gen.generate(input_data)
    
    assert hasattr(result, 'title')
    assert hasattr(result, 'content')
    assert hasattr(result, 'subsections')
    assert isinstance(result.subsections, list)
