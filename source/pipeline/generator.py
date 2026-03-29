from typing import Dict, Any
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from models import Section, SectionType, Report
from content import get_algorithm_content, ContentTemplates

class SectionGenerator:
    """Generate content for sections"""
    
    def __init__(self):
        self.templates = ContentTemplates()
    
    def generate(self, report: Report) -> Report:
        """Generate content for all sections"""
        for section in report.sections:
            self._generate_section(section, report)
        return report
    
    def _generate_section(self, section: Section, report: Report):
        """Generate content for a single section"""
        
        if section.type == SectionType.ACKNOWLEDGMENT:
            section.content = self.templates.acknowledgment(report.metadata, report.config)
        
        elif section.type == SectionType.COMMITMENT:
            section.content = self.templates.commitment(report.metadata)
        
        elif section.type == SectionType.INTRODUCTION:
            for subsection in section.subsections:
                if subsection.id == "intro_reason":
                    subsection.content = self.templates.introduction_reason(report.config)
                elif subsection.id == "intro_objectives":
                    subsection.content = self.templates.introduction_objectives()
        
        elif section.type == SectionType.ALGORITHM:
            algo_name = section.metadata.get('algorithm')
            if algo_name:
                algo_content = get_algorithm_content(algo_name)
                if algo_content:
                    section.content = self._format_algorithm_content(algo_content, section)
        
        elif section.type == SectionType.CONCLUSION:
            section.content = self.templates.conclusion(report.config)
        
        elif section.type == SectionType.REFERENCES:
            section.content = self.templates.references(report.config)
        
        # Recursively generate subsections
        for subsection in section.subsections:
            self._generate_section(subsection, report)
    
    def _format_algorithm_content(self, algo_content: Dict[str, Any], section: Section) -> str:
        """Format algorithm content into text"""
        parts = []
        
        # Purpose
        parts.append(f"**Mục tiêu:** {algo_content['purpose']}")
        parts.append("")
        
        # Theory
        parts.append(f"**Cơ sở lý thuyết:**\n{algo_content['theory']}")
        parts.append("")
        
        # Complexity
        parts.append(f"**Độ phức tạp:** {algo_content['complexity']}")
        parts.append("")
        
        # Pseudocode
        parts.append(f"**Giả mã:**\n```\n{algo_content['pseudocode']}\n```")
        parts.append("")
        
        # Advantages
        parts.append("**Ưu điểm:**")
        for adv in algo_content['advantages']:
            parts.append(f"- {adv}")
        parts.append("")
        
        # Limitations
        parts.append("**Hạn chế:**")
        for lim in algo_content['limitations']:
            parts.append(f"- {lim}")
        
        return "\n".join(parts)
