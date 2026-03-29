"""
LLM Integration Examples
Demonstrates how to use LLM enhancement with generators
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from source.llm import create_enhancer, EnhancementType
from source.llm.interface import EnhancementRequest
from source.generators import IntroductionGenerator


def example_1_basic_enhancement():
    """Example 1: Basic text enhancement"""
    print("=" * 60)
    print("Example 1: Basic Text Enhancement")
    print("=" * 60)
    
    # Create mock enhancer for testing
    enhancer = create_enhancer('mock', prefix='[Enhanced] ')
    
    original_text = "This is a simple introduction to the project."
    enhanced_text = enhancer.enhance_text(original_text, EnhancementType.REFINE)
    
    print(f"Original: {original_text}")
    print(f"Enhanced: {enhanced_text}")
    print(f"Available: {enhancer.is_available()}")
    print()


def example_2_enhancement_types():
    """Example 2: Different enhancement types"""
    print("=" * 60)
    print("Example 2: Different Enhancement Types")
    print("=" * 60)
    
    enhancer = create_enhancer('mock', prefix='[Improved] ')
    
    text = "The algorithm performs well on large datasets."
    
    for enh_type in [EnhancementType.EXPAND, EnhancementType.REFINE, 
                     EnhancementType.SUMMARIZE, EnhancementType.REPHRASE]:
        result = enhancer.enhance_text(text, enh_type)
        print(f"{enh_type.value}: {result}")
    
    print()


def example_3_enhancement_request():
    """Example 3: Using EnhancementRequest with context"""
    print("=" * 60)
    print("Example 3: Enhancement Request with Context")
    print("=" * 60)
    
    enhancer = create_enhancer('mock')
    
    request = EnhancementRequest(
        content="The system uses machine learning algorithms.",
        enhancement_type=EnhancementType.EXPAND,
        context={
            'domain': 'AI',
            'audience': 'technical',
            'tone': 'formal'
        },
        temperature=0.7
    )
    
    result = enhancer.enhance(request)
    
    print(f"Success: {result.success}")
    print(f"Original: {result.original}")
    print(f"Enhanced: {result.enhanced}")
    print(f"Metadata: {result.metadata}")
    print()


def example_4_section_enhancement():
    """Example 4: Enhance complete section"""
    print("=" * 60)
    print("Example 4: Section Enhancement")
    print("=" * 60)
    
    enhancer = create_enhancer('mock', prefix='[Better] ')
    
    section_data = {
        'title': 'Introduction',
        'content': 'This project explores AI algorithms.',
        'subsections': [
            {'title': 'Background', 'content': 'AI has grown rapidly.'},
            {'title': 'Motivation', 'content': 'We need better solutions.'}
        ]
    }
    
    enhanced = enhancer.enhance_section(
        title=section_data['title'],
        content=section_data['content'],
        subsections=section_data['subsections']
    )
    
    print(f"Title: {enhanced['title']}")
    print(f"Content: {enhanced['content']}")
    for subsec in enhanced['subsections']:
        print(f"  - {subsec['title']}: {subsec['content']}")
    print()


def example_5_generator_with_llm():
    """Example 5: Use generator with LLM enhancer"""
    print("=" * 60)
    print("Example 5: Generator with LLM Enhancement")
    print("=" * 60)
    
    # Create enhancer
    enhancer = create_enhancer('mock', prefix='[AI Enhanced] ')
    
    # Create generator with LLM support
    generator = IntroductionGenerator(use_llm=True, llm_client=enhancer)
    
    input_data = {
        'title': 'AI-Powered Report Generator',
        'domain': 'Natural Language Processing',
        'context': 'Automated report generation is a growing field.',
        'motivation': 'Manual report writing is time-consuming.',
        'objectives': [
            'Automate content generation',
            'Support multiple report types',
            'Integrate LLM capabilities'
        ],
        'scope': 'Focus on academic and technical reports.'
    }
    
    section = generator.generate(input_data)
    
    print(f"Title: {section.title}")
    print(f"Content: {section.content[:200]}...")
    print(f"Subsections: {len(section.subsections)}")
    for subsec in section.subsections:
        print(f"  - {subsec.title}")
    print()


def example_6_fallback_behavior():
    """Example 6: Fallback when LLM unavailable"""
    print("=" * 60)
    print("Example 6: Fallback Behavior")
    print("=" * 60)
    
    # Create enhancer with no provider (fallback mode)
    enhancer = create_enhancer(None)
    
    text = "This text will not be enhanced."
    enhanced = enhancer.enhance_text(text, EnhancementType.REFINE)
    
    print(f"Original: {text}")
    print(f"Enhanced: {enhanced}")
    print(f"Same? {text == enhanced}")
    print(f"Available: {enhancer.is_available()}")
    print()


def example_7_provider_configuration():
    """Example 7: Different provider configurations"""
    print("=" * 60)
    print("Example 7: Provider Configuration")
    print("=" * 60)
    
    # Mock provider
    mock_enhancer = create_enhancer('mock', prefix='[Mock] ')
    print(f"Mock available: {mock_enhancer.is_available()}")
    
    # OpenAI provider (will fail without API key)
    openai_enhancer = create_enhancer('openai')
    print(f"OpenAI available: {openai_enhancer.is_available()}")
    
    # Anthropic provider (will fail without API key)
    anthropic_enhancer = create_enhancer('anthropic')
    print(f"Anthropic available: {anthropic_enhancer.is_available()}")
    
    # No-op provider
    noop_enhancer = create_enhancer(None)
    print(f"NoOp available: {noop_enhancer.is_available()}")
    print()


def example_8_integration_pattern():
    """Example 8: Complete integration pattern"""
    print("=" * 60)
    print("Example 8: Complete Integration Pattern")
    print("=" * 60)
    
    # Step 1: Create enhancer based on config
    config = {
        'use_llm': True,
        'provider': 'mock',
        'provider_config': {'prefix': '[Pro] '}
    }
    
    if config.get('use_llm'):
        enhancer = create_enhancer(
            config['provider'],
            **config.get('provider_config', {})
        )
    else:
        enhancer = create_enhancer(None)
    
    print(f"Enhancer created: {type(enhancer).__name__}")
    print(f"Available: {enhancer.is_available()}")
    
    # Step 2: Use with generator
    generator = IntroductionGenerator(
        use_llm=config.get('use_llm', False),
        llm_client=enhancer
    )
    
    # Step 3: Generate content
    section = generator.generate({
        'title': 'Test Project',
        'domain': 'Software Engineering',
        'objectives': ['Build', 'Test', 'Deploy']
    })
    
    # Step 4: Optionally enhance generated content
    if enhancer.is_available():
        enhanced_content = enhancer.enhance_text(
            section.content,
            EnhancementType.REFINE
        )
        print(f"Original length: {len(section.content)}")
        print(f"Enhanced length: {len(enhanced_content)}")
    
    print()


if __name__ == '__main__':
    example_1_basic_enhancement()
    example_2_enhancement_types()
    example_3_enhancement_request()
    example_4_section_enhancement()
    example_5_generator_with_llm()
    example_6_fallback_behavior()
    example_7_provider_configuration()
    example_8_integration_pattern()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)
