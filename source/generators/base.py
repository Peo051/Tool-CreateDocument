"""
Base interface for section generators
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional


@dataclass
class Subsection:
    """Represents a subsection"""
    title: str
    content: str
    level: int = 2


@dataclass
class GeneratedSection:
    """Output from a section generator"""
    title: str
    content: str
    subsections: List[Subsection] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'title': self.title,
            'content': self.content,
            'subsections': [
                {'title': s.title, 'content': s.content, 'level': s.level}
                for s in self.subsections
            ],
            'metadata': self.metadata
        }


class SectionGenerator(ABC):
    """Base class for section generators"""
    
    def __init__(self, use_llm: bool = False, llm_client: Optional[Any] = None):
        """
        Initialize generator
        
        Args:
            use_llm: Whether to use LLM for generation
            llm_client: Optional LLM client (ContentEnhancer instance)
        """
        self.use_llm = use_llm
        self.llm_client = llm_client
        self._enhancer = llm_client if use_llm else None
    
    @abstractmethod
    def generate(self, input_data: Dict[str, Any]) -> GeneratedSection:
        """
        Generate section content
        
        Args:
            input_data: Structured input data for generation
            
        Returns:
            GeneratedSection with title, content, and subsections
        """
        pass
    
    def _enhance_text(self, text: str, enhancement_type: str = 'refine', 
                     context: Optional[Dict[str, Any]] = None) -> str:
        """
        Enhance text using LLM if available
        
        Args:
            text: Text to enhance
            enhancement_type: Type of enhancement ('refine', 'expand', etc.)
            context: Optional context for enhancement
            
        Returns:
            Enhanced text or original if LLM not available
        """
        if not self._enhancer or not self.use_llm:
            return text
        
        try:
            # Import here to avoid circular dependency
            from source.llm.interface import EnhancementType
            
            # Map string to enum
            type_map = {
                'refine': EnhancementType.REFINE,
                'expand': EnhancementType.EXPAND,
                'summarize': EnhancementType.SUMMARIZE,
                'rephrase': EnhancementType.REPHRASE
            }
            
            enh_type = type_map.get(enhancement_type.lower(), EnhancementType.REFINE)
            
            return self._enhancer.enhance_text(text, enh_type, context)
        except Exception:
            # Fallback to original on any error
            return text
    
    def _enhance_section(self, section: GeneratedSection) -> GeneratedSection:
        """
        Enhance complete section using LLM if available
        
        Args:
            section: Generated section to enhance
            
        Returns:
            Enhanced section or original if LLM not available
        """
        if not self._enhancer or not self.use_llm:
            return section
        
        try:
            # Enhance main content
            enhanced_content = self._enhance_text(section.content, 'refine')
            
            # Enhance subsections
            enhanced_subsections = []
            for subsec in section.subsections:
                enhanced_subsections.append(Subsection(
                    title=subsec.title,
                    content=self._enhance_text(subsec.content, 'refine'),
                    level=subsec.level
                ))
            
            return GeneratedSection(
                title=section.title,
                content=enhanced_content,
                subsections=enhanced_subsections,
                metadata={**section.metadata, 'enhanced': True}
            )
        except Exception:
            # Fallback to original on any error
            return section
    
    def _format_list(self, items: List[str], bullet: str = "-") -> str:
        """Format list of items"""
        return "\n".join(f"{bullet} {item}" for item in items)
    
    def _format_numbered_list(self, items: List[str]) -> str:
        """Format numbered list"""
        return "\n".join(f"{i}. {item}" for i, item in enumerate(items, 1))
