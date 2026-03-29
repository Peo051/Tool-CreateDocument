# LLM Integration Guide

Complete guide for using LLM enhancement with the report generator.

## Overview

The LLM integration layer provides optional content enhancement without coupling core logic to any specific model provider. The system works perfectly without LLM and gracefully falls back when LLM is unavailable.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Core System                          │
│  (Works independently, no LLM required)                 │
│                                                         │
│  ┌──────────────┐      ┌──────────────┐               │
│  │  Generators  │      │   Pipeline   │               │
│  └──────┬───────┘      └──────────────┘               │
│         │                                              │
└─────────┼──────────────────────────────────────────────┘
          │
          │ Optional Enhancement
          ▼
┌─────────────────────────────────────────────────────────┐
│              LLM Integration Layer                      │
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │         ContentEnhancer Interface                │  │
│  │  (Provider-agnostic enhancement API)             │  │
│  └────────────────┬─────────────────────────────────┘  │
│                   │                                     │
│       ┌───────────┼───────────┬──────────────┐         │
│       ▼           ▼           ▼              ▼         │
│  ┌────────┐ ┌─────────┐ ┌─────────┐   ┌─────────┐    │
│  │ OpenAI │ │Anthropic│ │  Mock   │   │  NoOp   │    │
│  │Provider│ │Provider │ │Provider │   │Enhancer │    │
│  └────────┘ └─────────┘ └─────────┘   └─────────┘    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Key Features

1. **Core Independence**: System works without LLM
2. **Provider Agnostic**: Support OpenAI, Anthropic, or custom providers
3. **Automatic Fallback**: Returns original content if LLM fails
4. **Easy Integration**: Simple API for generators
5. **Testing Support**: Mock provider for development

## Quick Start

### 1. Basic Enhancement

```python
from source.llm import create_enhancer, EnhancementType

# Create enhancer (mock for testing)
enhancer = create_enhancer('mock', prefix='[Enhanced] ')

# Enhance text
text = "This project implements search algorithms."
enhanced = enhancer.enhance_text(text, EnhancementType.REFINE)

print(f"Original:  {text}")
print(f"Enhanced:  {enhanced}")
```

### 2. Use with Generator

```python
from source.llm import create_enhancer
from source.generators import IntroductionGenerator

# Create enhancer
enhancer = create_enhancer('mock')

# Create generator with LLM support
generator = IntroductionGenerator(use_llm=True, llm_client=enhancer)

# Generate section (will use LLM if available)
section = generator.generate({
    'title': 'AI Report Generator',
    'domain': 'Natural Language Processing',
    'objectives': ['Automate reports', 'Support multiple types']
})
```

### 3. Helper Functions

```python
from source.generators import IntroductionGenerator
from source.generators.llm_helper import create_generator_with_llm

# Easy configuration
llm_config = {
    'enabled': True,
    'provider': 'mock',
    'prefix': '[Pro] '
}

generator = create_generator_with_llm(
    IntroductionGenerator,
    llm_config=llm_config
)

section = generator.generate(input_data)
```

## Enhancement Types

The system supports 5 enhancement types:

1. **REFINE**: Improve clarity and professionalism
2. **EXPAND**: Add more details and examples
3. **SUMMARIZE**: Create concise version
4. **REPHRASE**: Rewrite while maintaining meaning
5. **TRANSLATE**: Translate to another language

```python
from source.llm import EnhancementType

# Different enhancements
refined = enhancer.enhance_text(text, EnhancementType.REFINE)
expanded = enhancer.enhance_text(text, EnhancementType.EXPAND)
summary = enhancer.enhance_text(text, EnhancementType.SUMMARIZE)
```

## Provider Configuration

### Mock Provider (Testing)

```python
enhancer = create_enhancer('mock', prefix='[Test] ')
```

### OpenAI Provider

```python
# Requires: pip install openai
# Set environment variable: OPENAI_API_KEY

enhancer = create_enhancer(
    'openai',
    api_key='sk-...',  # or use env var
    model='gpt-3.5-turbo'
)
```

### Anthropic Provider

```python
# Requires: pip install anthropic
# Set environment variable: ANTHROPIC_API_KEY

enhancer = create_enhancer(
    'anthropic',
    api_key='sk-ant-...',  # or use env var
    model='claude-3-sonnet-20240229'
)
```

### No Enhancement

```python
# Returns original content unchanged
enhancer = create_enhancer(None)
```

## Integration Patterns

### Pattern 1: Generator-Level Enhancement

Enhance during generation:

```python
from source.generators import IntroductionGenerator
from source.llm import create_enhancer

enhancer = create_enhancer('mock')
generator = IntroductionGenerator(use_llm=True, llm_client=enhancer)

section = generator.generate(input_data)
# Content is enhanced during generation
```

### Pattern 2: Post-Generation Enhancement

Generate first, enhance later:

```python
from source.generators import IntroductionGenerator
from source.generators.llm_helper import enhance_section_post_generation

# Generate without LLM
generator = IntroductionGenerator()
section = generator.generate(input_data)

# Enhance afterwards
llm_config = {'enabled': True, 'provider': 'mock'}
enhanced_section = enhance_section_post_generation(section, llm_config)
```

### Pattern 3: Batch Enhancement

Enhance multiple sections:

```python
from source.generators.llm_helper import batch_enhance_sections

sections = [
    intro_gen.generate(intro_data),
    method_gen.generate(method_data),
    conclusion_gen.generate(conclusion_data)
]

llm_config = {'enabled': True, 'provider': 'mock'}
enhanced_sections = batch_enhance_sections(sections, llm_config)
```

### Pattern 4: Conditional Enhancement

Enable LLM based on configuration:

```python
from source.generators.llm_helper import create_generator_with_llm

# Load from config file
config = load_config('report_config.json')

llm_config = {
    'enabled': config.get('use_llm', False),
    'provider': config.get('llm_provider', 'mock'),
    'api_key': config.get('llm_api_key')
}

generator = create_generator_with_llm(
    IntroductionGenerator,
    llm_config=llm_config
)
```

## Fallback Behavior

The system gracefully handles failures:

```python
from source.llm import create_enhancer

# Provider not configured
enhancer = create_enhancer('openai')  # No API key

# Check availability
if enhancer.is_available():
    enhanced = enhancer.enhance_text(text)
else:
    enhanced = text  # Use original

# Or rely on automatic fallback
result = enhancer.enhance_text(text)
# Returns original if enhancement fails
```

## Advanced Usage

### Custom Context

```python
from source.llm.interface import EnhancementRequest, EnhancementType

request = EnhancementRequest(
    content="The algorithm performs well.",
    enhancement_type=EnhancementType.EXPAND,
    context={
        'domain': 'AI',
        'audience': 'technical',
        'tone': 'formal'
    },
    temperature=0.7,
    max_tokens=500
)

result = enhancer.enhance(request)
```

### Section Enhancement

```python
# Enhance complete section with subsections
enhanced = enhancer.enhance_section(
    title='Introduction',
    content='Main content here...',
    subsections=[
        {'title': 'Background', 'content': 'Background text...'},
        {'title': 'Motivation', 'content': 'Motivation text...'}
    ]
)
```

### Generator Base Methods

All generators inherit enhancement methods:

```python
class MyGenerator(SectionGenerator):
    def generate(self, input_data):
        # Generate content
        content = self._create_content(input_data)
        
        # Optionally enhance
        if self.use_llm:
            content = self._enhance_text(content, 'refine')
        
        section = GeneratedSection(
            title='My Section',
            content=content
        )
        
        # Or enhance complete section
        return self._enhance_section(section)
```

## Testing

### Unit Tests

```python
import unittest
from source.llm import create_enhancer, EnhancementType

class TestLLMIntegration(unittest.TestCase):
    def test_mock_enhancement(self):
        enhancer = create_enhancer('mock', prefix='[Test] ')
        result = enhancer.enhance_text('Hello', EnhancementType.REFINE)
        self.assertTrue(result.startswith('[Test]'))
    
    def test_fallback(self):
        enhancer = create_enhancer(None)
        text = 'Original'
        result = enhancer.enhance_text(text)
        self.assertEqual(text, result)
```

### Integration Tests

```python
def test_generator_with_llm():
    enhancer = create_enhancer('mock')
    generator = IntroductionGenerator(use_llm=True, llm_client=enhancer)
    
    section = generator.generate({
        'title': 'Test',
        'domain': 'Testing',
        'objectives': ['Test LLM integration']
    })
    
    assert section.title == 'Introduction'
    assert len(section.content) > 0
```

## Configuration File Format

Add LLM config to your report configuration:

```json
{
  "project_info": {
    "title": "My Report"
  },
  "llm_config": {
    "enabled": true,
    "provider": "openai",
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "max_tokens": 1000
  }
}
```

## Best Practices

1. **Start with Mock**: Test integration with mock provider first
2. **Check Availability**: Always check `is_available()` before relying on LLM
3. **Handle Failures**: Use automatic fallback or handle errors explicitly
4. **Cost Awareness**: LLM calls cost money, use judiciously
5. **Cache Results**: Consider caching enhanced content
6. **Test Without LLM**: Ensure core system works without LLM

## Troubleshooting

### LLM Not Available

```python
enhancer = create_enhancer('openai')
if not enhancer.is_available():
    print("OpenAI not configured. Set OPENAI_API_KEY environment variable.")
```

### Import Errors

```python
try:
    from source.llm import create_enhancer
except ImportError:
    print("LLM module not available. Using fallback.")
    enhancer = None
```

### Enhancement Failures

```python
from source.llm.interface import EnhancementRequest

request = EnhancementRequest(content=text, enhancement_type=EnhancementType.REFINE)
result = enhancer.enhance(request)

if not result.success:
    print(f"Enhancement failed: {result.error}")
    print(f"Using original: {result.original}")
```

## Examples

See complete examples in:
- `examples/llm_integration_usage.py` - 8 comprehensive examples
- `examples/llm_quick_demo.py` - Quick demonstration

Run examples:
```bash
python examples/llm_integration_usage.py
python examples/llm_quick_demo.py
```

## API Reference

### create_enhancer()

```python
def create_enhancer(
    provider_name: Optional[str] = None,
    api_key: Optional[str] = None,
    **kwargs
) -> ContentEnhancer
```

Factory function to create enhancer.

### ContentEnhancer.enhance_text()

```python
def enhance_text(
    text: str,
    enhancement_type: EnhancementType = EnhancementType.REFINE,
    context: Optional[Dict[str, Any]] = None
) -> str
```

Enhance text and return result.

### create_generator_with_llm()

```python
def create_generator_with_llm(
    generator_class: Type[SectionGenerator],
    llm_config: Optional[Dict[str, Any]] = None,
    **generator_kwargs
) -> SectionGenerator
```

Create generator with LLM support.

## Summary

The LLM integration provides:
- ✅ Optional enhancement without coupling
- ✅ Multiple provider support
- ✅ Automatic fallback
- ✅ Easy testing with mock provider
- ✅ Simple integration API
- ✅ Production-ready error handling

The core system remains independent and fully functional without LLM.
