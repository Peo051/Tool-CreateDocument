"""
Quick LLM Integration Demo
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from source.llm import create_enhancer, EnhancementType
from source.generators import IntroductionGenerator, ConclusionGenerator


def main():
    print("LLM Integration Quick Demo")
    print("=" * 60)
    
    # 1. Create mock enhancer
    enhancer = create_enhancer('mock', prefix='[Enhanced] ')
    print(f"✓ Enhancer created: {type(enhancer).__name__}")
    print(f"✓ Available: {enhancer.is_available()}")
    print()
    
    # 2. Basic enhancement
    text = "This project implements search algorithms."
    enhanced = enhancer.enhance_text(text, EnhancementType.REFINE)
    print(f"Original:  {text}")
    print(f"Enhanced:  {enhanced}")
    print()
    
    # 3. Use with generator
    generator = IntroductionGenerator(use_llm=True, llm_client=enhancer)
    
    section = generator.generate({
        'title': 'Search Algorithm Comparison',
        'domain': 'Artificial Intelligence',
        'objectives': [
            'Compare BFS, DFS, A* algorithms',
            'Analyze performance metrics',
            'Provide implementation examples'
        ]
    })
    
    print(f"✓ Generated section: {section.title}")
    print(f"✓ Subsections: {len(section.subsections)}")
    print()
    
    # 4. Enhance generated content
    enhanced_content = enhancer.enhance_text(
        section.content[:100],
        EnhancementType.EXPAND
    )
    print(f"Enhanced content: {enhanced_content}")
    print()
    
    print("=" * 60)
    print("Demo completed successfully!")


if __name__ == '__main__':
    main()
