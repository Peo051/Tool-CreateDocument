"""
Implementation Section Generator
"""

from typing import Dict, Any, List
from .base import SectionGenerator, GeneratedSection, Subsection


class ImplementationGenerator(SectionGenerator):
    """Generate implementation section"""
    
    def generate(self, input_data: Dict[str, Any]) -> GeneratedSection:
        """
        Generate implementation section
        
        Expected input_data:
        - overview: Implementation overview
        - architecture: System architecture description
        - components: List of components
        - features: Key features implemented
        - technologies: Technologies used
        - challenges: Implementation challenges
        - code_structure: Code organization
        """
        overview = input_data.get('overview', '')
        architecture = input_data.get('architecture', '')
        components = input_data.get('components', [])
        features = input_data.get('features', [])
        technologies = input_data.get('technologies', [])
        challenges = input_data.get('challenges', [])
        code_structure = input_data.get('code_structure', '')
        
        # Main content
        if overview:
            content = overview
        else:
            content = (
                "This section details the implementation of the system, "
                "including architecture, components, and key features."
            )
        
        # Generate subsections
        subsections = []
        
        # Architecture
        if architecture:
            subsections.append(Subsection(
                title="System Architecture",
                content=architecture,
                level=2
            ))
        
        # Components
        if components:
            components_content = self._build_components_content(components)
            
            subsections.append(Subsection(
                title="Components",
                content=components_content,
                level=2
            ))
        
        # Features
        if features:
            features_content = "The following features were implemented:\n\n"
            features_content += self._build_features_content(features)
            
            subsections.append(Subsection(
                title="Key Features",
                content=features_content,
                level=2
            ))
        
        # Technologies
        if technologies:
            tech_content = "Technologies used:\n\n"
            tech_content += self._format_list(technologies)
            
            subsections.append(Subsection(
                title="Technologies",
                content=tech_content,
                level=2
            ))
        
        # Code Structure
        if code_structure:
            subsections.append(Subsection(
                title="Code Structure",
                content=code_structure,
                level=2
            ))
        
        # Implementation Challenges
        if challenges:
            challenges_content = "Key challenges encountered:\n\n"
            challenges_content += self._build_challenges_content(challenges)
            
            subsections.append(Subsection(
                title="Implementation Challenges",
                content=challenges_content,
                level=2
            ))
        
        return GeneratedSection(
            title="Implementation",
            content=content,
            subsections=subsections,
            metadata={
                'components_count': len(components),
                'features_count': len(features)
            }
        )
    
    def _build_components_content(self, components: List[Any]) -> str:
        """Build content for components"""
        content_parts = []
        
        for component in components:
            if isinstance(component, dict):
                name = component.get('name', '')
                description = component.get('description', '')
                responsibilities = component.get('responsibilities', [])
                
                part = f"**{name}**\n\n{description}"
                
                if responsibilities:
                    part += "\n\nResponsibilities:\n"
                    part += self._format_list(responsibilities)
                
                content_parts.append(part)
            else:
                content_parts.append(f"- {component}")
        
        return "\n\n".join(content_parts)
    
    def _build_features_content(self, features: List[Any]) -> str:
        """Build content for features"""
        content_parts = []
        
        for feature in features:
            if isinstance(feature, dict):
                name = feature.get('name', '')
                description = feature.get('description', '')
                status = feature.get('status', '')
                
                part = f"**{name}**"
                if status:
                    part += f" ({status})"
                if description:
                    part += f"\n\n{description}"
                
                content_parts.append(part)
            else:
                content_parts.append(f"- {feature}")
        
        return "\n\n".join(content_parts)
    
    def _build_challenges_content(self, challenges: List[Any]) -> str:
        """Build content for challenges"""
        content_parts = []
        
        for challenge in challenges:
            if isinstance(challenge, dict):
                problem = challenge.get('problem', '')
                solution = challenge.get('solution', '')
                
                part = f"**Challenge**: {problem}"
                if solution:
                    part += f"\n\n**Solution**: {solution}"
                
                content_parts.append(part)
            else:
                content_parts.append(f"- {challenge}")
        
        return "\n\n".join(content_parts)
