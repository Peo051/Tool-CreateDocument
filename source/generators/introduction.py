"""
Introduction Section Generator
"""

from typing import Dict, Any
from .base import SectionGenerator, GeneratedSection, Subsection


class IntroductionGenerator(SectionGenerator):
    """Generate introduction section"""
    
    def generate(self, input_data: Dict[str, Any]) -> GeneratedSection:
        """
        Generate introduction section
        
        Expected input_data:
        - title: Project title
        - domain: Domain/field (e.g., "AI", "Web Development")
        - context: Background context
        - motivation: Why this project matters
        - objectives: List of objectives
        - scope: Project scope
        """
        title = input_data.get('title', 'Project')
        domain = input_data.get('domain', 'software development')
        context = input_data.get('context', '')
        motivation = input_data.get('motivation', '')
        objectives = input_data.get('objectives', [])
        scope = input_data.get('scope', '')
        
        # Main introduction content
        content_parts = []
        
        if context:
            content_parts.append(context)
        else:
            content_parts.append(
                f"This project, titled '{title}', addresses key challenges in {domain}. "
                f"The work presented here explores practical solutions and implementations "
                f"that advance the current state of the field."
            )
        
        if motivation:
            content_parts.append(f"\n{motivation}")
        
        content = "\n\n".join(content_parts)
        
        # Generate subsections
        subsections = []
        
        # Background subsection
        if context:
            subsections.append(Subsection(
                title="Background",
                content=context,
                level=2
            ))
        
        # Motivation subsection
        if motivation:
            subsections.append(Subsection(
                title="Motivation",
                content=motivation,
                level=2
            ))
        
        # Objectives subsection
        if objectives:
            obj_content = "The main objectives of this project are:\n\n"
            obj_content += self._format_numbered_list(objectives)
            
            subsections.append(Subsection(
                title="Objectives",
                content=obj_content,
                level=2
            ))
        
        # Scope subsection
        if scope:
            subsections.append(Subsection(
                title="Scope",
                content=scope,
                level=2
            ))
        
        return GeneratedSection(
            title="Introduction",
            content=content,
            subsections=subsections,
            metadata={'domain': domain, 'title': title}
        )
