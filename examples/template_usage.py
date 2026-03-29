#!/usr/bin/env python3
"""
Template System Usage Examples
Demonstrates how to use the Jinja2 template system
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

from template_renderer import TemplateRenderer, ContentRenderer
from content.template_content import TemplateContentGenerator, AlgorithmContentGenerator


def example_basic_rendering():
    """Example 1: Basic template rendering"""
    print("\n" + "="*60)
    print("Example 1: Basic Template Rendering")
    print("="*60)
    
    renderer = TemplateRenderer()
    
    # Render acknowledgment
    context = {
        'faculty': 'Công nghệ thông tin',
        'advisor': 'TS. Trần Việt Hùng'
    }
    
    content = renderer.render('sections/acknowledgment.j2', context)
    print(content)


def example_content_renderer():
    """Example 2: Using ContentRenderer"""
    print("\n" + "="*60)
    print("Example 2: ContentRenderer")
    print("="*60)
    
    renderer = ContentRenderer()
    
    # Render introduction reason
    intro = renderer.render_introduction_reason(
        title='Maze Duel - BO3 / Gemini_Game'
    )
    print(intro)


def example_template_content_generator():
    """Example 3: Using TemplateContentGenerator"""
    print("\n" + "="*60)
    print("Example 3: TemplateContentGenerator")
    print("="*60)
    
    generator = TemplateContentGenerator()
    
    config = {
        'title': 'My AI Project',
        'faculty': 'Computer Science',
        'advisor': 'Dr. John Doe',
        'github_repo': 'https://github.com/user/project',
        'demo_url': 'https://demo.example.com'
    }
    
    # Generate multiple sections
    print("Introduction Reason:")
    print("-"*60)
    print(generator.introduction_reason(config))
    
    print("\n\nReferences:")
    print("-"*60)
    print(generator.references(config))


def example_algorithm_rendering():
    """Example 4: Rendering algorithm content"""
    print("\n" + "="*60)
    print("Example 4: Algorithm Rendering")
    print("="*60)
    
    generator = AlgorithmContentGenerator()
    
    # Algorithm data
    algo_data = {
        'name': 'DFS',
        'title': 'DFS - Sinh mê cung procedural',
        'category': 'Tìm kiếm',
        'purpose': 'Tạo ra mê cung ngẫu nhiên cho mỗi ván đấu',
        'theory': 'DFS (Depth-First Search) là thuật toán duyệt đồ thị theo chiều sâu',
        'complexity': 'O(V + E) với V là số ô, E là số cạnh',
        'pseudocode': '''function generateMaze(grid):
    stack = []
    start = randomCell()
    mark start as visited
    stack.push(start)
    while stack not empty:
        current = stack.top()
        neighbors = unvisitedNeighbors(current)
        if neighbors not empty:
            next = random(neighbors)
            removeWall(current, next)
            stack.push(next)
        else:
            stack.pop()''',
        'role': 'Tạo nền móng cho gameplay với bản đồ mới mỗi ván',
        'advantages': [
            'Cực kỳ nhanh O(V)',
            'Đơn giản dễ cài đặt',
            'Tạo mê cung đa dạng'
        ],
        'limitations': [
            'Nhiều ngõ cụt',
            'Ít loops',
            'Cần hậu xử lý'
        ],
        'solution': 'Thêm post-processing để mở loops',
        'application': 'Map generation pipeline'
    }
    
    content = generator.render_algorithm(algo_data)
    print(content)


def example_fallback_handling():
    """Example 5: Fallback handling for missing values"""
    print("\n" + "="*60)
    print("Example 5: Fallback Handling")
    print("="*60)
    
    renderer = ContentRenderer()
    
    # Render with missing values - should use defaults
    print("With empty values (uses defaults):")
    print("-"*60)
    ack = renderer.render_acknowledgment(faculty='', advisor='')
    print(ack)
    
    print("\n\nWith provided values:")
    print("-"*60)
    ack = renderer.render_acknowledgment(
        faculty='Công nghệ thông tin',
        advisor='TS. Trần Việt Hùng'
    )
    print(ack)


def example_custom_objectives():
    """Example 6: Custom objectives"""
    print("\n" + "="*60)
    print("Example 6: Custom Objectives")
    print("="*60)
    
    renderer = ContentRenderer()
    
    # Default objectives
    print("Default objectives:")
    print("-"*60)
    obj1 = renderer.render_introduction_objectives()
    print(obj1)
    
    # Custom objectives
    print("\n\nCustom objectives:")
    print("-"*60)
    custom_obj = [
        'Implement machine learning algorithms',
        'Build web interface',
        'Deploy to cloud',
        'Write comprehensive documentation'
    ]
    obj2 = renderer.render_introduction_objectives(objectives=custom_obj)
    print(obj2)


def example_list_templates():
    """Example 7: List available templates"""
    print("\n" + "="*60)
    print("Example 7: List Available Templates")
    print("="*60)
    
    renderer = TemplateRenderer()
    templates = renderer.list_templates()
    
    print(f"Found {len(templates)} templates:\n")
    for template in templates:
        print(f"  - {template}")


def example_integration_with_config():
    """Example 8: Integration with config file"""
    print("\n" + "="*60)
    print("Example 8: Integration with Config")
    print("="*60)
    
    # Simulate config from report_config.json
    config = {
        'title': 'Maze Duel - BO3 / Gemini_Game',
        'subtitle': 'Ứng dụng thuật toán AI trong game mê cung đối kháng',
        'students': [
            {'name': 'Trần Dương Gia Bảo', 'id': '2001240039'},
            {'name': 'Nguyễn Thế Anh', 'id': '2001240015'}
        ],
        'advisor': 'TS. Trần Việt Hùng',
        'faculty': 'Công nghệ thông tin',
        'university': 'Đại học Công Thương TP. HCM',
        'github_repo': 'https://github.com/GiaBao051/Gemini_Game',
        'demo_url': 'https://giabao051.github.io/Gemini_Game/',
        'algorithms': ['DFS', 'BFS', 'A*', 'Dijkstra', 'CSP']
    }
    
    generator = TemplateContentGenerator()
    
    # Generate all sections
    sections = {
        'Introduction Reason': generator.introduction_reason(config),
        'Introduction Objectives': generator.introduction_objectives(config),
        'Conclusion': generator.conclusion(config),
        'References': generator.references(config)
    }
    
    for section_name, content in sections.items():
        print(f"\n{section_name}:")
        print("-"*60)
        print(content[:200] + "..." if len(content) > 200 else content)


def main():
    """Run all examples"""
    print("\n" + "="*60)
    print("  Template System Usage Examples  ".center(60))
    print("="*60)
    
    examples = [
        example_basic_rendering,
        example_content_renderer,
        example_template_content_generator,
        example_algorithm_rendering,
        example_fallback_handling,
        example_custom_objectives,
        example_list_templates,
        example_integration_with_config
    ]
    
    for example in examples:
        try:
            example()
        except Exception as e:
            print(f"\n❌ Error in {example.__name__}: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "="*60)
    print("✅ All examples completed!")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
