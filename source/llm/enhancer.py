"""
LLM Content Enhancer Implementation
"""

from typing import Optional
from .interface import ContentEnhancer, EnhancementRequest, EnhancementResult, EnhancementType, NoOpEnhancer
from .providers import LLMProvider


class LLMContentEnhancer(ContentEnhancer):
    """
    Content enhancer using LLM provider
    Falls back to original content if LLM fails
    """
    
    def __init__(self, provider: Optional[LLMProvider] = None, fallback_to_original: bool = True):
        """
        Initialize enhancer
        
        Args:
            provider: LLM provider (None = no enhancement)
            fallback_to_original: Return original content on failure
        """
        self.provider = provider
        self.fallback_to_original = fallback_to_original
    
    def enhance(self, request: EnhancementRequest) -> EnhancementResult:
        """
        Enhance content using LLM
        
        Args:
            request: Enhancement request
            
        Returns:
            EnhancementResult with enhanced or original content
        """
        # If no provider or not available, return original
        if not self.provider or not self.is_available():
            return EnhancementResult(
                original=request.content,
                enhanced=request.content,
                success=True,
                metadata={'enhancer': 'passthrough', 'reason': 'no_provider'}
            )
        
        try:
            # Build prompt based on enhancement type
            prompt = self._build_prompt(request)
            
            # Generate enhanced content
            enhanced = self.provider.generate(
                prompt=prompt,
                max_tokens=request.max_tokens,
                temperature=request.temperature
            )
            
            return EnhancementResult(
                original=request.content,
                enhanced=enhanced.strip(),
                success=True,
                metadata={
                    'enhancer': 'llm',
                    'provider': type(self.provider).__name__,
                    'enhancement_type': request.enhancement_type.value
                }
            )
            
        except Exception as e:
            # Fallback to original on error
            if self.fallback_to_original:
                return EnhancementResult(
                    original=request.content,
                    enhanced=request.content,
                    success=False,
                    error=str(e),
                    metadata={'enhancer': 'fallback'}
                )
            else:
                raise
    
    def is_available(self) -> bool:
        """Check if LLM provider is available"""
        if not self.provider:
            return False
        
        try:
            return self.provider.is_configured()
        except Exception:
            return False
    
    def _build_prompt(self, request: EnhancementRequest) -> str:
        """
        Build prompt for LLM based on enhancement type
        
        Args:
            request: Enhancement request
            
        Returns:
            Formatted prompt
        """
        content = request.content
        context = request.context
        
        # Base prompts for each enhancement type
        prompts = {
            EnhancementType.EXPAND: (
                f"Expand and elaborate on the following text with more details and examples:\n\n{content}"
            ),
            EnhancementType.REFINE: (
                f"Refine and improve the following text for clarity and professionalism:\n\n{content}"
            ),
            EnhancementType.SUMMARIZE: (
                f"Summarize the following text concisely:\n\n{content}"
            ),
            EnhancementType.REPHRASE: (
                f"Rephrase the following text while maintaining its meaning:\n\n{content}"
            ),
            EnhancementType.TRANSLATE: (
                f"Translate the following text to {context.get('target_language', 'English')}:\n\n{content}"
            )
        }
        
        base_prompt = prompts.get(request.enhancement_type, content)
        
        # Add context if provided
        if context:
            context_str = "\n".join(f"{k}: {v}" for k, v in context.items() if k != 'target_language')
            if context_str:
                base_prompt = f"Context:\n{context_str}\n\n{base_prompt}"
        
        return base_prompt


def create_enhancer(provider_name: Optional[str] = None, 
                   api_key: Optional[str] = None,
                   **kwargs) -> ContentEnhancer:
    """
    Factory function to create content enhancer
    
    Args:
        provider_name: Provider name ('openai', 'anthropic', 'mock', None)
        api_key: API key for provider
        **kwargs: Provider-specific configuration
        
    Returns:
        ContentEnhancer instance
    """
    if not provider_name:
        return NoOpEnhancer()
    
    provider_name = provider_name.lower()
    
    if provider_name == 'openai':
        from .providers import OpenAIProvider
        provider = OpenAIProvider(api_key=api_key, **kwargs)
        return LLMContentEnhancer(provider=provider)
    
    elif provider_name == 'anthropic':
        from .providers import AnthropicProvider
        provider = AnthropicProvider(api_key=api_key, **kwargs)
        return LLMContentEnhancer(provider=provider)
    
    elif provider_name == 'mock':
        from .providers import MockProvider
        provider = MockProvider(api_key=api_key, **kwargs)
        return LLMContentEnhancer(provider=provider)
    
    else:
        # Unknown provider, return no-op
        return NoOpEnhancer()
