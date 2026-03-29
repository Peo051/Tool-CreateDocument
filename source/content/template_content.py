"""
Template-based content generator
Replaces hard-coded content with Jinja2 templates
"""

import sys
import os
from typing import Dict, Any, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from template_renderer import ContentRenderer, TemplateRenderer
from models import ReportMetadata


class TemplateContentGenerator:
    """
    Content generator using Jinja2 templates
    Drop-in replacement for ContentTemplates class
    """
    
    def __init__(self):
        """Initialize template-based content generator"""
        self.renderer = ContentRenderer()
    
    def acknowledgment(self, metadata: ReportMetadata, config: Dict[str, Any]) -> str:
        """
        Generate acknowledgment section
        
        Args:
            metadata: Report metadata
            config: Configuration dictionary
            
        Returns:
            Rendered acknowledgment text
        """
        return self.renderer.render_acknowledgment(
            faculty=config.get('faculty', ''),
            advisor=metadata.advisor or config.get('advisor', '')
        )
    
    def commitment(self, metadata: ReportMetadata) -> str:
        """
        Generate commitment section
        
        Args:
            metadata: Report metadata
            
        Returns:
            Rendered commitment text
        """
        return self.renderer.render_commitment()
    
    def introduction_reason(self, config: Dict[str, Any]) -> str:
        """
        Generate introduction reason section
        
        Args:
            config: Configuration dictionary
            
        Returns:
            Rendered introduction reason text
        """
        return self.renderer.render_introduction_reason(
            title=config.get('title', '')
        )
    
    def introduction_objectives(self, config: Dict[str, Any] = None) -> str:
        """
        Generate introduction objectives section
        
        Args:
            config: Configuration dictionary (optional)
            
        Returns:
            Rendered objectives text
        """
        objectives = None
        if config:
            objectives = config.get('objectives')
        
        return self.renderer.render_introduction_objectives(objectives=objectives)
    
    def conclusion(self, config: Dict[str, Any]) -> str:
        """
        Generate conclusion section
        
        Args:
            config: Configuration dictionary
            
        Returns:
            Rendered conclusion text
        """
        return self.renderer.render_conclusion(
            title=config.get('title', ''),
            future_work=config.get('future_work')
        )
    
    def references(self, config: Dict[str, Any]) -> str:
        """
        Generate references section
        
        Args:
            config: Configuration dictionary
            
        Returns:
            Rendered references text
        """
        return self.renderer.render_references(
            github_repo=config.get('github_repo', ''),
            demo_url=config.get('demo_url', ''),
            custom_references=config.get('custom_references')
        )


class AlgorithmContentGenerator:
    """
    Algorithm content generator using templates
    """
    
    def __init__(self):
        """Initialize algorithm content generator"""
        self.renderer = ContentRenderer()
    
    def render_algorithm(self, algorithm_data: Dict[str, Any]) -> str:
        """
        Render algorithm section from data
        
        Args:
            algorithm_data: Algorithm information dictionary
            
        Returns:
            Rendered algorithm content
        """
        return self.renderer.render_algorithm(algorithm_data)
    
    def get_algorithm_content(self, algo_name: str, 
                            algorithms_db: Dict[str, Dict[str, Any]]) -> Optional[str]:
        """
        Get rendered algorithm content by name
        
        Args:
            algo_name: Algorithm name (e.g., 'DFS', 'BFS')
            algorithms_db: Algorithm database dictionary
            
        Returns:
            Rendered algorithm content or None if not found
        """
        algo_data = algorithms_db.get(algo_name)
        if not algo_data:
            return None
        
        return self.render_algorithm(algo_data)


# Backward compatibility: Create instances that match old API
template_content = TemplateContentGenerator()
algorithm_content = AlgorithmContentGenerator()


# Convenience functions
def get_template_content(section_type: str, config: Dict[str, Any], 
                        metadata: Optional[ReportMetadata] = None) -> str:
    """
    Get rendered content for a section
    
    Args:
        section_type: Type of section
        config: Configuration dictionary
        metadata: Report metadata (optional)
        
    Returns:
        Rendered content
    """
    generator = TemplateContentGenerator()
    
    if section_type == 'acknowledgment':
        if metadata is None:
            metadata = ReportMetadata(
                title=config.get('title', ''),
                authors=config.get('students', []),
                advisor=config.get('advisor', ''),
                organization=config.get('university', '')
            )
        return generator.acknowledgment(metadata, config)
    
    elif section_type == 'commitment':
        if metadata is None:
            metadata = ReportMetadata(
                title=config.get('title', ''),
                authors=config.get('students', []),
                organization=config.get('university', '')
            )
        return generator.commitment(metadata)
    
    elif section_type == 'introduction_reason':
        return generator.introduction_reason(config)
    
    elif section_type == 'introduction_objectives':
        return generator.introduction_objectives(config)
    
    elif section_type == 'conclusion':
        return generator.conclusion(config)
    
    elif section_type == 'references':
        return generator.references(config)
    
    else:
        raise ValueError(f"Unknown section type: {section_type}")
