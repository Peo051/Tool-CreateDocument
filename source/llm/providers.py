"""
LLM Provider Adapters
Isolated provider-specific code
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import os


class LLMProvider(ABC):
    """Abstract LLM provider interface"""
    
    def __init__(self, api_key: Optional[str] = None, **kwargs):
        """
        Initialize provider
        
        Args:
            api_key: API key (can be None, will try env var)
            **kwargs: Provider-specific configuration
        """
        self.api_key = api_key
        self.config = kwargs
    
    @abstractmethod
    def generate(self, prompt: str, max_tokens: Optional[int] = None, 
                temperature: float = 0.7, **kwargs) -> str:
        """
        Generate text from prompt
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            **kwargs: Provider-specific parameters
            
        Returns:
            Generated text
            
        Raises:
            Exception: If generation fails
        """
        pass
    
    @abstractmethod
    def is_configured(self) -> bool:
        """Check if provider is properly configured"""
        pass


class OpenAIProvider(LLMProvider):
    """
    OpenAI provider adapter
    Placeholder - requires openai package
    """
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo", **kwargs):
        super().__init__(api_key, **kwargs)
        self.model = model
        self.client = None
        
        # Try to initialize client
        if self.is_configured():
            try:
                import openai
                self.client = openai.OpenAI(api_key=self.api_key or os.getenv('OPENAI_API_KEY'))
            except ImportError:
                pass  # openai package not installed
            except Exception:
                pass  # Configuration error
    
    def generate(self, prompt: str, max_tokens: Optional[int] = None,
                temperature: float = 0.7, **kwargs) -> str:
        """Generate text using OpenAI API"""
        if not self.client:
            raise RuntimeError("OpenAI client not initialized")
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature,
                **kwargs
            )
            return response.choices[0].message.content
        except Exception as e:
            raise RuntimeError(f"OpenAI generation failed: {e}")
    
    def is_configured(self) -> bool:
        """Check if OpenAI is configured"""
        return bool(self.api_key or os.getenv('OPENAI_API_KEY'))


class AnthropicProvider(LLMProvider):
    """
    Anthropic (Claude) provider adapter
    Placeholder - requires anthropic package
    """
    
    def __init__(self, api_key: Optional[str] = None, model: str = "claude-3-sonnet-20240229", **kwargs):
        super().__init__(api_key, **kwargs)
        self.model = model
        self.client = None
        
        # Try to initialize client
        if self.is_configured():
            try:
                import anthropic
                self.client = anthropic.Anthropic(api_key=self.api_key or os.getenv('ANTHROPIC_API_KEY'))
            except ImportError:
                pass  # anthropic package not installed
            except Exception:
                pass  # Configuration error
    
    def generate(self, prompt: str, max_tokens: Optional[int] = None,
                temperature: float = 0.7, **kwargs) -> str:
        """Generate text using Anthropic API"""
        if not self.client:
            raise RuntimeError("Anthropic client not initialized")
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens or 1024,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}],
                **kwargs
            )
            return response.content[0].text
        except Exception as e:
            raise RuntimeError(f"Anthropic generation failed: {e}")
    
    def is_configured(self) -> bool:
        """Check if Anthropic is configured"""
        return bool(self.api_key or os.getenv('ANTHROPIC_API_KEY'))


class MockProvider(LLMProvider):
    """
    Mock provider for testing
    Returns enhanced version of input with prefix
    """
    
    def __init__(self, api_key: Optional[str] = None, **kwargs):
        super().__init__(api_key, **kwargs)
        self.prefix = kwargs.get('prefix', '[Enhanced] ')
    
    def generate(self, prompt: str, max_tokens: Optional[int] = None,
                temperature: float = 0.7, **kwargs) -> str:
        """Return mock enhanced text"""
        # Simple mock: add prefix and capitalize
        return f"{self.prefix}{prompt.strip()}"
    
    def is_configured(self) -> bool:
        """Always configured"""
        return True
