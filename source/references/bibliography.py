"""
Bibliography generator
"""

from typing import List, Literal
from .models import ReferenceEntry
from .formatter import CitationFormatter, APAFormatter, IEEEFormatter


class BibliographyGenerator:
    """Generate formatted bibliography"""
    
    FORMATTERS = {
        'APA': APAFormatter,
        'IEEE': IEEEFormatter
    }
    
    def __init__(self, style: Literal['APA', 'IEEE'] = 'IEEE'):
        """Initialize with citation style"""
        self.style = style
        formatter_class = self.FORMATTERS.get(style, IEEEFormatter)
        self.formatter = formatter_class()
    
    def generate(self, references: List[ReferenceEntry], numbered: bool = None) -> str:
        """
        Generate formatted bibliography
        
        Args:
            references: List of reference entries
            numbered: Whether to number entries (auto-detect if None)
        
        Returns:
            Formatted bibliography text
        """
        if not references:
            return ""
        
        # Auto-detect numbering based on style
        if numbered is None:
            numbered = (self.style == 'IEEE')
        
        lines = []
        for i, ref in enumerate(references, 1):
            citation = self.formatter.format_citation(ref)
            
            if numbered:
                lines.append(f"[{i}] {citation}")
            else:
                lines.append(citation)
        
        return "\n\n".join(lines)
    
    def generate_section(self, references: List[ReferenceEntry], title: str = None) -> dict:
        """
        Generate bibliography as section data
        
        Returns:
            Dictionary with section structure
        """
        if title is None:
            title = "References" if self.style == 'APA' else "REFERENCES"
        
        content = self.generate(references)
        
        return {
            'type': 'references',
            'title': title,
            'content': content,
            'references': [
                {
                    'id': ref.id,
                    'citation': self.formatter.format_citation(ref),
                    'inline': self.formatter.format_inline(ref)
                }
                for ref in references
            ],
            'metadata': {
                'style': self.style,
                'count': len(references)
            }
        }
    
    def get_inline_citation(self, ref: ReferenceEntry) -> str:
        """Get inline citation for a reference"""
        return self.formatter.format_inline(ref)
