"""
LLM Helper for Generators
Provides easy integration between generators and LLM enhancers
"""

from typing import Optional, Dict, Any, Type
from .base import SectionGenerator, GeneratedSection


def create_generator_with_llm(
    generator_class: Type[SectionGenerator],
    llm_config: Optional[Dict[str, Any]] = None,
    **generator_kwargs
) -> SectionGenerator:
    """
    Create generator with optional LLM enhancement
    
    Args:
        generator_class: Generator class to instantiate
        llm_config: LLM configuration dict with keys:
            - enabled: bool (default False)
            - provider: str ('openai', 'anthropic', 'mock', None)
            - api_key: str (optional)
            - model: str (optional)
            - **other provider-specific config
        **generator_kwargs: Additional kwargs for generator
        
    Returns:
        Configured generator instance
        
    Example:
        >>> from source.generators import IntroductionGenerator
        >>> from source.generators.llm_helper import create_generator_with_llm
        >>> 
        >>> llm_config = {
        ...     'enabled': True,
        ...     'provider': 'mock',
        ...     'prefix': '[Enhanced] '
        ... }
        >>> 
        >>> generator = create_generator_with_llm(
        ...     IntroductionGenerator,
        ...     llm_config=llm_config
        ... )
    """
    llm_config = llm_config or {}
    
    use_llm = llm_config.get('enabled', False)
    
    if not use_llm:
        return generator_class(use_llm=False, **generator_kwargs)
    
    # Import LLM components
    try:
        from source.llm import create_enhancer
        
        provider = llm_config.get('provider')
        api_key = llm_config.get('api_key')
        
        # Extract provider-specific config
        provider_config = {
            k: v for k, v in llm_config.items()
            if k not in ['enabled', 'provider', 'api_key']
        }
        
        # Create enhancer
        enhancer = create_enhancer(provider, api_key=api_key, **provider_config)
        
        return generator_class(
            use_llm=True,
            llm_client=enhancer,
            **generator_kwargs
        )
        
    except ImportError:
        # LLM module not available, fallback to no LLM
        return generator_class(use_llm=False, **generator_kwargs)


def enhance_section_post_generation(
    section: GeneratedSection,
    llm_config: Optional[Dict[str, Any]] = None
) -> GeneratedSection:
    """
    Enhance already-generated section with LLM
    
    Args:
        section: Generated section to enhance
        llm_config: LLM configuration (same format as create_generator_with_llm)
        
    Returns:
        Enhanced section or original if LLM not available
        
    Example:
        >>> section = generator.generate(input_data)
        >>> enhanced = enhance_section_post_generation(
        ...     section,
        ...     llm_config={'enabled': True, 'provider': 'mock'}
        ... )
    """
    llm_config = llm_config or {}
    
    if not llm_config.get('enabled', False):
        return section
    
    try:
        from source.llm import create_enhancer
        from source.generators.base import Subsection
        
        provider = llm_config.get('provider')
        api_key = llm_config.get('api_key')
        
        provider_config = {
            k: v for k, v in llm_config.items()
            if k not in ['enabled', 'provider', 'api_key']
        }
        
        enhancer = create_enhancer(provider, api_key=api_key, **provider_config)
        
        if not enhancer.is_available():
            return section
        
        # Enhance content
        enhanced_content = enhancer.enhance_text(section.content)
        
        # Enhance subsections
        enhanced_subsections = []
        for subsec in section.subsections:
            enhanced_subsections.append(Subsection(
                title=subsec.title,
                content=enhancer.enhance_text(subsec.content),
                level=subsec.level
            ))
        
        return GeneratedSection(
            title=section.title,
            content=enhanced_content,
            subsections=enhanced_subsections,
            metadata={**section.metadata, 'enhanced': True}
        )
        
    except Exception:
        # Return original on any error
        return section


def batch_enhance_sections(
    sections: list[GeneratedSection],
    llm_config: Optional[Dict[str, Any]] = None
) -> list[GeneratedSection]:
    """
    Enhance multiple sections in batch
    
    Args:
        sections: List of sections to enhance
        llm_config: LLM configuration
        
    Returns:
        List of enhanced sections
        
    Example:
        >>> sections = [gen1.generate(data1), gen2.generate(data2)]
        >>> enhanced = batch_enhance_sections(
        ...     sections,
        ...     llm_config={'enabled': True, 'provider': 'mock'}
        ... )
    """
    return [
        enhance_section_post_generation(section, llm_config)
        for section in sections
    ]
