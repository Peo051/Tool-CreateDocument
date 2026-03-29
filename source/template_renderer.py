#!/usr/bin/env python3
"""
Jinja2 Template Renderer for Report Generation
Converts hard-coded content to template-based system
"""

import os
import sys
from typing import Dict, Any, Optional
from pathlib import Path

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape, TemplateNotFound
except ImportError:
    print("❌ Jinja2 not installed. Install with: pip install jinja2")
    sys.exit(1)


class TemplateRenderer:
    """
    Template-based content renderer using Jinja2
    
    Features:
    - Context-based rendering
    - Fallback handling for missing values
    - Easy-to-edit templates
    - Support for multiple template directories
    """
    
    def __init__(self, template_dir: Optional[str] = None):
        """
        Initialize template renderer
        
        Args:
            template_dir: Path to template directory (default: source/templates)
        """
        if template_dir is None:
            # Default to source/templates
            template_dir = os.path.join(
                os.path.dirname(__file__),
                'templates'
            )
        
        self.template_dir = Path(template_dir)
        
        # Ensure template directory exists
        if not self.template_dir.exists():
            raise FileNotFoundError(f"Template directory not found: {self.template_dir}")
        
        # Initialize Jinja2 environment
        self.env = Environment(
            loader=FileSystemLoader(str(self.template_dir)),
            autoescape=select_autoescape(['html', 'xml']),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True
        )
        
        # Add custom filters
        self._register_filters()
    
    def _register_filters(self):
        """Register custom Jinja2 filters"""
        
        def safe_get(obj, key, default=''):
            """Safely get value from dict with default"""
            if isinstance(obj, dict):
                return obj.get(key, default)
            return default
        
        def join_list(items, separator=', '):
            """Join list items with separator"""
            if not items:
                return ''
            return separator.join(str(item) for item in items)
        
        def format_list(items, bullet='- '):
            """Format list with bullets"""
            if not items:
                return ''
            return '\n'.join(f"{bullet}{item}" for item in items)
        
        # Register filters
        self.env.filters['safe_get'] = safe_get
        self.env.filters['join_list'] = join_list
        self.env.filters['format_list'] = format_list
    
    def render(self, template_name: str, context: Dict[str, Any]) -> str:
        """
        Render template with context
        
        Args:
            template_name: Template file name (e.g., 'sections/acknowledgment.j2')
            context: Context dictionary for template
            
        Returns:
            Rendered content as string
            
        Raises:
            TemplateNotFound: If template doesn't exist
        """
        try:
            template = self.env.get_template(template_name)
            return template.render(**context)
        except TemplateNotFound:
            raise TemplateNotFound(f"Template not found: {template_name}")
        except Exception as e:
            raise RuntimeError(f"Error rendering template {template_name}: {e}")
    
    def render_safe(self, template_name: str, context: Dict[str, Any], 
                    fallback: str = '') -> str:
        """
        Render template with fallback on error
        
        Args:
            template_name: Template file name
            context: Context dictionary
            fallback: Fallback content if rendering fails
            
        Returns:
            Rendered content or fallback
        """
        try:
            return self.render(template_name, context)
        except Exception as e:
            print(f"⚠️  Warning: Failed to render {template_name}: {e}")
            return fallback
    
    def list_templates(self, pattern: str = '*.j2') -> list:
        """
        List available templates
        
        Args:
            pattern: Glob pattern for templates
            
        Returns:
            List of template paths
        """
        templates = []
        for path in self.template_dir.rglob(pattern):
            rel_path = path.relative_to(self.template_dir)
            templates.append(str(rel_path))
        return sorted(templates)
    
    def template_exists(self, template_name: str) -> bool:
        """Check if template exists"""
        template_path = self.template_dir / template_name
        return template_path.exists()


class ContentRenderer:
    """
    High-level content renderer for report sections
    Provides convenient methods for common content types
    """
    
    def __init__(self, template_renderer: Optional[TemplateRenderer] = None):
        """
        Initialize content renderer
        
        Args:
            template_renderer: TemplateRenderer instance (creates new if None)
        """
        self.renderer = template_renderer or TemplateRenderer()
    
    def render_acknowledgment(self, faculty: str = '', advisor: str = '') -> str:
        """
        Render acknowledgment section
        
        Args:
            faculty: Faculty name
            advisor: Advisor name
            
        Returns:
            Rendered acknowledgment text
        """
        context = {
            'faculty': faculty,
            'advisor': advisor
        }
        return self.renderer.render('sections/acknowledgment.j2', context)
    
    def render_commitment(self) -> str:
        """
        Render commitment section
        
        Returns:
            Rendered commitment text
        """
        return self.renderer.render('sections/commitment.j2', {})
    
    def render_introduction_reason(self, title: str = '') -> str:
        """
        Render introduction reason section
        
        Args:
            title: Project title
            
        Returns:
            Rendered introduction reason text
        """
        context = {'title': title}
        return self.renderer.render('sections/introduction_reason.j2', context)
    
    def render_introduction_objectives(self, objectives: Optional[list] = None) -> str:
        """
        Render introduction objectives section
        
        Args:
            objectives: List of objectives (uses default if None)
            
        Returns:
            Rendered objectives text
        """
        context = {'objectives': objectives}
        return self.renderer.render('sections/introduction_objectives.j2', context)
    
    def render_conclusion(self, title: str = '', future_work: Optional[list] = None) -> str:
        """
        Render conclusion section
        
        Args:
            title: Project title
            future_work: List of future work items
            
        Returns:
            Rendered conclusion text
        """
        context = {
            'title': title,
            'future_work': future_work
        }
        return self.renderer.render('sections/conclusion.j2', context)
    
    def render_references(self, github_repo: str = '', demo_url: str = '',
                         custom_references: Optional[list] = None) -> str:
        """
        Render references section
        
        Args:
            github_repo: GitHub repository URL
            demo_url: Demo URL
            custom_references: List of custom references
            
        Returns:
            Rendered references text
        """
        context = {
            'github_repo': github_repo,
            'demo_url': demo_url,
            'custom_references': custom_references
        }
        return self.renderer.render('sections/references.j2', context)
    
    def render_algorithm(self, algorithm_data: Dict[str, Any]) -> str:
        """
        Render algorithm section
        
        Args:
            algorithm_data: Dictionary with algorithm information
                - name: Algorithm name
                - title: Algorithm title
                - category: Algorithm category
                - purpose: Purpose description
                - theory: Theoretical background
                - complexity: Time/space complexity
                - pseudocode: Pseudocode
                - role: Role in system
                - advantages: List of advantages
                - limitations: List of limitations
                - solution: Solution to limitations
                - application: Application description
                
        Returns:
            Rendered algorithm section text
        """
        return self.renderer.render('algorithms/algorithm_section.j2', algorithm_data)
    
    def render_from_config(self, section_type: str, config: Dict[str, Any]) -> str:
        """
        Render section from config dictionary
        
        Args:
            section_type: Type of section (acknowledgment, commitment, etc.)
            config: Configuration dictionary
            
        Returns:
            Rendered content
        """
        method_map = {
            'acknowledgment': lambda: self.render_acknowledgment(
                faculty=config.get('faculty', ''),
                advisor=config.get('advisor', '')
            ),
            'commitment': lambda: self.render_commitment(),
            'introduction_reason': lambda: self.render_introduction_reason(
                title=config.get('title', '')
            ),
            'introduction_objectives': lambda: self.render_introduction_objectives(
                objectives=config.get('objectives')
            ),
            'conclusion': lambda: self.render_conclusion(
                title=config.get('title', ''),
                future_work=config.get('future_work')
            ),
            'references': lambda: self.render_references(
                github_repo=config.get('github_repo', ''),
                demo_url=config.get('demo_url', ''),
                custom_references=config.get('custom_references')
            )
        }
        
        if section_type in method_map:
            return method_map[section_type]()
        else:
            raise ValueError(f"Unknown section type: {section_type}")


# Convenience functions for quick usage

def render_template(template_name: str, context: Dict[str, Any]) -> str:
    """
    Quick template rendering
    
    Args:
        template_name: Template file name
        context: Context dictionary
        
    Returns:
        Rendered content
    """
    renderer = TemplateRenderer()
    return renderer.render(template_name, context)


def render_section(section_type: str, config: Dict[str, Any]) -> str:
    """
    Quick section rendering
    
    Args:
        section_type: Section type
        config: Configuration dictionary
        
    Returns:
        Rendered content
    """
    content_renderer = ContentRenderer()
    return content_renderer.render_from_config(section_type, config)


# Example usage
if __name__ == '__main__':
    print("Template Renderer - Example Usage\n")
    print("="*60)
    
    # Initialize renderer
    renderer = ContentRenderer()
    
    # Example 1: Render acknowledgment
    print("\n1. Acknowledgment:")
    print("-"*60)
    ack = renderer.render_acknowledgment(
        faculty='Công nghệ thông tin',
        advisor='TS. Trần Việt Hùng'
    )
    print(ack)
    
    # Example 2: Render introduction reason
    print("\n2. Introduction Reason:")
    print("-"*60)
    intro = renderer.render_introduction_reason(
        title='Maze Duel - BO3 / Gemini_Game'
    )
    print(intro)
    
    # Example 3: Render algorithm
    print("\n3. Algorithm Section:")
    print("-"*60)
    algo_data = {
        'name': 'DFS',
        'title': 'DFS - Sinh mê cung procedural',
        'purpose': 'Tạo ra mê cung ngẫu nhiên',
        'theory': 'DFS là thuật toán duyệt đồ thị theo chiều sâu',
        'complexity': 'O(V + E)',
        'advantages': ['Nhanh', 'Đơn giản', 'Hiệu quả'],
        'limitations': ['Nhiều ngõ cụt', 'Ít loops']
    }
    algo = renderer.render_algorithm(algo_data)
    print(algo)
    
    print("\n" + "="*60)
    print("✅ Template rendering examples completed!")
