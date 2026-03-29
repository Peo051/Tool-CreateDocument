"""
Conclusion Section Generator
"""

from typing import Dict, Any, List
from .base import SectionGenerator, GeneratedSection, Subsection


class ConclusionGenerator(SectionGenerator):
    """Generate conclusion section"""
    
    def generate(self, input_data: Dict[str, Any]) -> GeneratedSection:
        """
        Generate conclusion section
        
        Expected input_data:
        - summary: Project summary
        - achievements: Key achievements
        - contributions: Main contributions
        - limitations: Project limitations
        - future_work: Future work suggestions
        - lessons_learned: Lessons learned
        - final_remarks: Final remarks
        """
        summary = input_data.get('summary', '')
        achievements = input_data.get('achievements', [])
        contributions = input_data.get('contributions', [])
        limitations = input_data.get('limitations', [])
        future_work = input_data.get('future_work', [])
        lessons_learned = input_data.get('lessons_learned', [])
        final_remarks = input_data.get('final_remarks', '')
        
        # Main content
        content_parts = []
        
        if summary:
            content_parts.append(summary)
        else:
            content_parts.append(
                "This project successfully addressed the stated objectives and "
                "delivered a functional solution. The work demonstrates practical "
                "applications and provides insights for future development."
            )
        
        if achievements:
            content_parts.append(
                "\nKey achievements include:\n\n" +
                self._format_list(achievements)
            )
        
        content = "\n\n".join(content_parts)
        
        # Generate subsections
        subsections = []
        
        # Summary
        if summary:
            subsections.append(Subsection(
                title="Summary",
                content=summary,
                level=2
            ))
        
        # Achievements
        if achievements:
            ach_content = "The project achieved the following:\n\n"
            ach_content += self._format_numbered_list(achievements)
            
            subsections.append(Subsection(
                title="Achievements",
                content=ach_content,
                level=2
            ))
        
        # Contributions
        if contributions:
            contrib_content = "Main contributions:\n\n"
            contrib_content += self._format_list(contributions)
            
            subsections.append(Subsection(
                title="Contributions",
                content=contrib_content,
                level=2
            ))
        
        # Limitations
        if limitations:
            lim_content = "The following limitations were identified:\n\n"
            lim_content += self._format_list(limitations)
            
            subsections.append(Subsection(
                title="Limitations",
                content=lim_content,
                level=2
            ))
        
        # Future Work
        if future_work:
            future_content = self._build_future_work_content(future_work)
            
            subsections.append(Subsection(
                title="Future Work",
                content=future_content,
                level=2
            ))
        
        # Lessons Learned
        if lessons_learned:
            lessons_content = "Key lessons learned:\n\n"
            lessons_content += self._format_list(lessons_learned)
            
            subsections.append(Subsection(
                title="Lessons Learned",
                content=lessons_content,
                level=2
            ))
        
        # Final Remarks
        if final_remarks:
            subsections.append(Subsection(
                title="Final Remarks",
                content=final_remarks,
                level=2
            ))
        
        return GeneratedSection(
            title="Conclusion",
            content=content,
            subsections=subsections,
            metadata={
                'achievements_count': len(achievements),
                'future_work_count': len(future_work)
            }
        )
    
    def _build_future_work_content(self, future_work: List[Any]) -> str:
        """Build content for future work"""
        content_parts = []
        
        for item in future_work:
            if isinstance(item, dict):
                title = item.get('title', '')
                description = item.get('description', '')
                priority = item.get('priority', '')
                
                part = f"**{title}**"
                if priority:
                    part += f" (Priority: {priority})"
                if description:
                    part += f"\n\n{description}"
                
                content_parts.append(part)
            else:
                content_parts.append(f"- {item}")
        
        return "\n\n".join(content_parts)
