"""
Problem Statement Section Generator
"""

from typing import Dict, Any, List
from .base import SectionGenerator, GeneratedSection, Subsection


class ProblemStatementGenerator(SectionGenerator):
    """Generate problem statement section"""
    
    def generate(self, input_data: Dict[str, Any]) -> GeneratedSection:
        """
        Generate problem statement section
        
        Expected input_data:
        - problem: Main problem description
        - challenges: List of specific challenges
        - current_solutions: Existing solutions and their limitations
        - gaps: Research/implementation gaps
        - impact: Impact of the problem
        """
        problem = input_data.get('problem', '')
        challenges = input_data.get('challenges', [])
        current_solutions = input_data.get('current_solutions', [])
        gaps = input_data.get('gaps', [])
        impact = input_data.get('impact', '')
        
        # Main content
        content_parts = []
        
        if problem:
            content_parts.append(problem)
        
        if challenges:
            content_parts.append(
                "\nThe key challenges include:\n\n" +
                self._format_list(challenges)
            )
        
        content = "\n\n".join(content_parts) if content_parts else (
            "This section outlines the core problem addressed by this project, "
            "including the challenges faced and gaps in existing solutions."
        )
        
        # Generate subsections
        subsections = []
        
        # Problem definition
        if problem:
            subsections.append(Subsection(
                title="Problem Definition",
                content=problem,
                level=2
            ))
        
        # Challenges
        if challenges:
            challenges_content = "The following challenges must be addressed:\n\n"
            challenges_content += self._format_list(challenges)
            
            subsections.append(Subsection(
                title="Key Challenges",
                content=challenges_content,
                level=2
            ))
        
        # Current solutions
        if current_solutions:
            solutions_content = self._build_solutions_content(current_solutions)
            
            subsections.append(Subsection(
                title="Existing Solutions",
                content=solutions_content,
                level=2
            ))
        
        # Gaps
        if gaps:
            gaps_content = "Current approaches have the following limitations:\n\n"
            gaps_content += self._format_list(gaps)
            
            subsections.append(Subsection(
                title="Research Gaps",
                content=gaps_content,
                level=2
            ))
        
        # Impact
        if impact:
            subsections.append(Subsection(
                title="Impact",
                content=impact,
                level=2
            ))
        
        return GeneratedSection(
            title="Problem Statement",
            content=content,
            subsections=subsections,
            metadata={'challenges_count': len(challenges)}
        )
    
    def _build_solutions_content(self, solutions: List[Any]) -> str:
        """Build content for existing solutions"""
        if not solutions:
            return ""
        
        content_parts = []
        
        for i, solution in enumerate(solutions, 1):
            if isinstance(solution, dict):
                name = solution.get('name', f'Solution {i}')
                description = solution.get('description', '')
                limitations = solution.get('limitations', [])
                
                part = f"**{name}**\n\n{description}"
                
                if limitations:
                    part += "\n\nLimitations:\n" + self._format_list(limitations)
                
                content_parts.append(part)
            else:
                content_parts.append(f"{i}. {solution}")
        
        return "\n\n".join(content_parts)
