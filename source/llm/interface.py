"""
LLM Interface - Provider-agnostic content enhancement
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List
from enum import Enum


class EnhancementType(str, Enum):
    """Types of content enhancement"""
    EXPAND = "expand"
    REFINE = "refine"
    SUMMARIZE = "summarize"
    REPHRASE = "rephrase"
    TRANSLATE = "translate"


@dataclass
class EnhancementRequest:
    """Request for content enhancement"""
    content: str
    enhancement_type: EnhancementType
    context: Dict[str, Any] = field(default_factory=dict)
    max_tokens: Optional[int] = None
    temperature: float = 0.7
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'content': self.content,
            'enhancement_type': self.enhancement_type.value,
            'context': self.context,
            'max_tokens': self.max_tokens,
            'temperature': self.temperature
        }


@dataclass
class EnhancementResult:
    """Result from content enhancement"""
    original: str
    enhanced: str
    success: bool
    error: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'original': self.original,
            'enhanced': self.enhanced,
            'success': self.success,
            'error': self.error,
            'metadata': self.metadata
        }


class ContentEnhancer(ABC):
    """
    Abstract interface for content enhancement
    Core system doesn't depend on this - it's purely optional
    """
    
    @abstractmethod
    def enhance(self, request: EnhancementRequest) -> EnhancementResult:
        """
        Enhance content based on request
        
        Args:
            request: Enhancement request
            
        Returns:
            EnhancementResult with enhanced content or fallback
        """
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        """Check if enhancer is available"""
        pass
    
    def enhance_text(self, text: str, enhancement_type: EnhancementType = EnhancementType.REFINE,
                     context: Optional[Dict[str, Any]] = None) -> str:
        """
        Convenience method to enhance text and return result
        
        Args:
            text: Text to enhance
            enhancement_type: Type of enhancement
            context: Optional context
            
        Returns:
            Enhanced text or original if enhancement fails
        """
        request = EnhancementRequest(
            content=text,
            enhancement_type=enhancement_type,
            context=context or {}
        )
        
        result = self.enhance(request)
        return result.enhanced if result.success else result.original
    
    def enhance_section(self, title: str, content: str, 
                       subsections: Optional[List[Dict[str, str]]] = None) -> Dict[str, Any]:
        """
        Enhance a complete section
        
        Args:
            title: Section title
            content: Section content
            subsections: Optional subsections
            
        Returns:
            Dictionary with enhanced content
        """
        enhanced_content = self.enhance_text(content, EnhancementType.REFINE)
        
        enhanced_subsections = []
        if subsections:
            for subsec in subsections:
                enhanced_subsections.append({
                    'title': subsec['title'],
                    'content': self.enhance_text(subsec['content'], EnhancementType.REFINE)
                })
        
        return {
            'title': title,
            'content': enhanced_content,
            'subsections': enhanced_subsections
        }


class NoOpEnhancer(ContentEnhancer):
    """
    No-op enhancer that returns original content
    Used as fallback when LLM is unavailable
    """
    
    def enhance(self, request: EnhancementRequest) -> EnhancementResult:
        """Return original content unchanged"""
        return EnhancementResult(
            original=request.content,
            enhanced=request.content,
            success=True,
            metadata={'enhancer': 'noop'}
        )
    
    def is_available(self) -> bool:
        """Always available"""
        return True
