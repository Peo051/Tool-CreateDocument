# Template System Guide - Jinja2 Integration

## Overview

Successfully converted hard-coded content generator into a flexible, template-based system using Jinja2.

## What Was Done

### 1. Template Folder Structure

```
source/templates/
├── sections/                          # Report section templates
│   ├── acknowledgment.j2              # Lời cảm ơn
│   ├── commitment.j2                  # Lời cam đoan
│   ├── introduction_reason.j2         # Lý do chọn đề tài
│   ├── introduction_objectives.j2     # Mục tiêu nghiên cứu
│   ├── conclusion.j2                  # Kết luận
│   └── references.j2                  # Tài liệu tham khảo
│
└── algorithms/                        # Algorithm templates
    └── algorithm_section.j2           # Algorithm content template
```

### 2. Python Template Renderer (`source/template_renderer.py`)

**TemplateRenderer Class:**
- Jinja2 environment setup
- Custom filters (safe_get, join_list, format_list)
- Template rendering with error handling
- Template listing and existence checking

**ContentRenderer Class:**
- High-level API for common sections
- Convenient methods: `render_acknowledgment()`, `render_conclusion()`, etc.
- Algorithm rendering support
- Config-based rendering

### 3. Integration Module (`source/content/template_content.py`)

**TemplateContentGenerator:**
- Drop-in replacement for old `ContentTemplates`
- Same API, template-based implementation
- Backward compatible

**AlgorithmContentGenerator:**
- Renders algorithm sections from data
- Supports algorithm database integration

### 4. Example Templates

#### sections/acknowledgment.j2
```jinja2
Nhóm chúng em xin chân thành cảm ơn quý Thầy/Cô Khoa {{ faculty|default('Công nghệ thông tin') }}, đặc biệt là {{ advisor|default('giảng viên hướng dẫn') }} đã tận tình hướng dẫn...
```

#### sections/introduction_reason.j2
```jinja2
Đề tài "{{ title|default('Ứng dụng thuật toán AI') }}" được nhóm lựa chọn xuất phát từ mong muốn tìm hiểu sâu về cách các thuật toán AI hoạt động...
```

#### algorithms/algorithm_section.j2
```jinja2
{% if purpose %}
{{ purpose }}
{% endif %}

{% if theory %}
{{ theory }}
{% endif %}

**Độ phức tạp:** {{ complexity }}

{% if advantages %}
**Ưu điểm:**
{% for adv in advantages %}
- {{ adv }}
{% endfor %}
{% endif %}
```

## Features

### ✅ Context-Based Rendering

Templates use context variables with fallback defaults:

```python
renderer = ContentRenderer()
content = renderer.render_acknowledgment(
    faculty='Công nghệ thông tin',
    advisor='TS. Trần Việt Hùng'
)
```

### ✅ Fallback Handling

Missing values automatically use defaults:

```jinja2
{{ faculty|default('Công nghệ thông tin') }}
{{ advisor|default('giảng viên hướng dẫn') }}
```

### ✅ Easy to Edit

Templates are plain text files - no Python knowledge needed:

```jinja2
Nhóm xin cảm ơn {{ advisor }} đã hướng dẫn.
```

### ✅ Custom Filters

Built-in filters for common operations:

```jinja2
{{ items|join_list(', ') }}
{{ items|format_list('- ') }}
{{ config|safe_get('key', 'default') }}
```

## Usage

### Basic Usage

```python
from template_renderer import ContentRenderer

renderer = ContentRenderer()

# Render acknowledgment
ack = renderer.render_acknowledgment(
    faculty='Công nghệ thông tin',
    advisor='TS. Trần Việt Hùng'
)

# Render introduction
intro = renderer.render_introduction_reason(
    title='My AI Project'
)

# Render algorithm
algo_data = {
    'name': 'DFS',
    'title': 'DFS - Sinh mê cung',
    'purpose': 'Tạo mê cung ngẫu nhiên',
    'theory': 'DFS là thuật toán...',
    'complexity': 'O(V + E)',
    'advantages': ['Nhanh', 'Đơn giản'],
    'limitations': ['Nhiều ngõ cụt']
}
algo = renderer.render_algorithm(algo_data)
```

### Integration with Existing Code

```python
from content.template_content import TemplateContentGenerator

# Drop-in replacement for old ContentTemplates
generator = TemplateContentGenerator()

# Same API as before
ack = generator.acknowledgment(metadata, config)
intro = generator.introduction_reason(config)
conclusion = generator.conclusion(config)
```

### Quick Rendering

```python
from template_renderer import render_template, render_section

# Render template directly
content = render_template('sections/acknowledgment.j2', {
    'faculty': 'CS',
    'advisor': 'Dr. Smith'
})

# Render section from config
content = render_section('acknowledgment', config)
```

## Template Syntax

### Variables

```jinja2
{{ variable_name }}
{{ config.title }}
{{ metadata.advisor }}
```

### Defaults

```jinja2
{{ variable|default('default value') }}
{{ title|default('Untitled Project') }}
```

### Conditionals

```jinja2
{% if github_repo %}
[1] Repository: {{ github_repo }}
{% endif %}

{% if future_work %}
Hướng phát triển: {{ future_work|join(', ') }}
{% else %}
Hướng phát triển: tối ưu hiệu năng, thêm ML
{% endif %}
```

### Loops

```jinja2
{% for objective in objectives %}
- {{ objective }}
{% endfor %}

{% for adv in advantages %}
- {{ adv }}
{% endfor %}
```

### Filters

```jinja2
{{ items|join(', ') }}
{{ text|upper }}
{{ text|lower }}
{{ text|capitalize }}
{{ list|length }}
```

## Creating New Templates

### Step 1: Create Template File

Create `.j2` file in `source/templates/sections/`:

```jinja2
{# my_section.j2 #}
This is my custom section.

Title: {{ title }}

{% if description %}
Description: {{ description }}
{% endif %}
```

### Step 2: Add Renderer Method

Add method to `ContentRenderer`:

```python
def render_my_section(self, title: str = '', description: str = '') -> str:
    context = {
        'title': title,
        'description': description
    }
    return self.renderer.render('sections/my_section.j2', context)
```

### Step 3: Use It

```python
renderer = ContentRenderer()
content = renderer.render_my_section(
    title='My Title',
    description='My Description'
)
```

## Migration from Hard-Coded Content

### Before (Hard-Coded)

```python
def acknowledgment(self, metadata, config):
    faculty = config.get('faculty', '')
    advisor = metadata.advisor or ''
    
    return f"""Nhóm chúng em xin chân thành cảm ơn quý Thầy/Cô Khoa {faculty}, đặc biệt là {advisor} đã tận tình hướng dẫn..."""
```

### After (Template-Based)

**Template (acknowledgment.j2):**
```jinja2
Nhóm chúng em xin chân thành cảm ơn quý Thầy/Cô Khoa {{ faculty|default('Công nghệ thông tin') }}, đặc biệt là {{ advisor|default('giảng viên hướng dẫn') }} đã tận tình hướng dẫn...
```

**Python:**
```python
def acknowledgment(self, metadata, config):
    return self.renderer.render_acknowledgment(
        faculty=config.get('faculty', ''),
        advisor=metadata.advisor or config.get('advisor', '')
    )
```

## Benefits

### 1. Separation of Concerns
- Content in templates (easy to edit)
- Logic in Python (easy to maintain)

### 2. Easy Customization
- Non-programmers can edit templates
- No Python knowledge required
- Just edit text files

### 3. Reusability
- Templates can be reused across projects
- Share templates between teams
- Version control friendly

### 4. Maintainability
- Changes to content don't require code changes
- Easier to review content changes
- Clear separation of data and presentation

### 5. Flexibility
- Support multiple languages
- Different templates for different report types
- Easy A/B testing

## Advanced Features

### Custom Filters

Add custom filters for specific needs:

```python
def _register_filters(self):
    def format_date(date_obj, format='%Y-%m-%d'):
        return date_obj.strftime(format)
    
    self.env.filters['format_date'] = format_date
```

Use in templates:

```jinja2
{{ report_date|format_date('%d/%m/%Y') }}
```

### Template Inheritance

Create base template:

```jinja2
{# base_section.j2 #}
<section>
    <h1>{{ title }}</h1>
    {% block content %}{% endblock %}
</section>
```

Extend it:

```jinja2
{# my_section.j2 #}
{% extends "base_section.j2" %}

{% block content %}
    <p>{{ description }}</p>
{% endblock %}
```

### Macros

Define reusable components:

```jinja2
{% macro render_list(items, bullet='- ') %}
{% for item in items %}
{{ bullet }}{{ item }}
{% endfor %}
{% endmacro %}

{{ render_list(advantages, '✓ ') }}
{{ render_list(limitations, '✗ ') }}
```

## Testing

### Unit Tests

```python
import unittest
from template_renderer import ContentRenderer

class TestTemplateRenderer(unittest.TestCase):
    def setUp(self):
        self.renderer = ContentRenderer()
    
    def test_acknowledgment(self):
        content = self.renderer.render_acknowledgment(
            faculty='CS',
            advisor='Dr. Smith'
        )
        self.assertIn('CS', content)
        self.assertIn('Dr. Smith', content)
    
    def test_fallback(self):
        content = self.renderer.render_acknowledgment(
            faculty='',
            advisor=''
        )
        # Should use defaults
        self.assertIn('Công nghệ thông tin', content)
```

### Integration Tests

```python
def test_full_report_generation():
    generator = TemplateContentGenerator()
    config = load_config('test_config.json')
    
    sections = {
        'ack': generator.acknowledgment(metadata, config),
        'intro': generator.introduction_reason(config),
        'conclusion': generator.conclusion(config)
    }
    
    for name, content in sections.items():
        assert len(content) > 0, f"{name} is empty"
```

## Troubleshooting

### Template Not Found

```python
TemplateNotFound: sections/my_template.j2
```

**Solution:** Check template path and ensure file exists in `source/templates/`

### Variable Not Found

```jinja2
{{ undefined_variable }}
```

**Solution:** Use default filter:
```jinja2
{{ undefined_variable|default('default value') }}
```

### Rendering Error

```python
RuntimeError: Error rendering template: ...
```

**Solution:** Check template syntax and context variables

## Performance

### Caching

Jinja2 automatically caches compiled templates:

```python
# First render: compiles template
content1 = renderer.render('sections/ack.j2', context)

# Second render: uses cached template (fast)
content2 = renderer.render('sections/ack.j2', context)
```

### Optimization Tips

1. **Reuse renderer instances** - Don't create new renderer for each render
2. **Use template inheritance** - Reduce duplication
3. **Minimize logic in templates** - Keep templates simple
4. **Pre-compile templates** - For production use

## Examples

See `examples/template_usage.py` for comprehensive examples:

```bash
python examples/template_usage.py
```

Examples include:
1. Basic template rendering
2. ContentRenderer usage
3. TemplateContentGenerator
4. Algorithm rendering
5. Fallback handling
6. Custom objectives
7. List available templates
8. Integration with config

## Summary

The template system provides:

✅ Clean separation of content and code  
✅ Easy customization without programming  
✅ Fallback handling for missing values  
✅ Context-based rendering  
✅ Backward compatible with existing code  
✅ Production-ready with error handling  
✅ Comprehensive examples and documentation  

Templates are now the single source of truth for content, making the system more maintainable and flexible.
