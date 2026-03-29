# Template System - Quick Start

## Installation

```bash
pip install jinja2
```

## Basic Usage

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

# Render conclusion
conclusion = renderer.render_conclusion(
    title='My AI Project',
    future_work=['Optimize performance', 'Add ML']
)
```

## Template Files

Located in `source/templates/`:

```
sections/
├── acknowledgment.j2              # Lời cảm ơn
├── commitment.j2                  # Lời cam đoan
├── introduction_reason.j2         # Lý do chọn đề tài
├── introduction_objectives.j2     # Mục tiêu
├── conclusion.j2                  # Kết luận
└── references.j2                  # Tài liệu tham khảo

algorithms/
└── algorithm_section.j2           # Algorithm content
```

## Editing Templates

Just edit the `.j2` files - no Python needed!

**Example (acknowledgment.j2):**
```jinja2
Nhóm xin cảm ơn {{ advisor|default('giảng viên') }} đã hướng dẫn.
```

## Template Syntax

### Variables
```jinja2
{{ variable_name }}
{{ config.title }}
```

### Defaults
```jinja2
{{ variable|default('default value') }}
```

### Conditionals
```jinja2
{% if github_repo %}
Repository: {{ github_repo }}
{% endif %}
```

### Loops
```jinja2
{% for item in items %}
- {{ item }}
{% endfor %}
```

## Integration

Replace old content generator:

```python
# Old
from content.templates import ContentTemplates
generator = ContentTemplates()

# New
from content.template_content import TemplateContentGenerator
generator = TemplateContentGenerator()

# Same API - works exactly the same!
ack = generator.acknowledgment(metadata, config)
```

## Examples

Run examples:

```bash
python examples/template_usage.py
```

## Documentation

- `TEMPLATE_SYSTEM_GUIDE.md` - Complete guide
- `TEMPLATE_SYSTEM_COMPLETION.md` - Implementation details
- `examples/template_usage.py` - 8 examples

## Common Tasks

### Add New Template

1. Create `source/templates/sections/my_section.j2`
2. Add method to `ContentRenderer`
3. Use it!

### Customize Content

1. Edit template file
2. Save
3. Done! (no code changes needed)

### Use Custom Values

```python
renderer.render_acknowledgment(
    faculty='Your Faculty',
    advisor='Your Advisor'
)
```

## Troubleshooting

### Template Not Found
- Check file exists in `source/templates/`
- Check file extension is `.j2`

### Variable Not Found
- Use default filter: `{{ var|default('default') }}`

### Rendering Error
- Check template syntax
- Check context variables

## Quick Reference

| Method | Template | Context Variables |
|--------|----------|-------------------|
| `render_acknowledgment()` | `sections/acknowledgment.j2` | `faculty`, `advisor` |
| `render_commitment()` | `sections/commitment.j2` | None |
| `render_introduction_reason()` | `sections/introduction_reason.j2` | `title` |
| `render_introduction_objectives()` | `sections/introduction_objectives.j2` | `objectives` |
| `render_conclusion()` | `sections/conclusion.j2` | `title`, `future_work` |
| `render_references()` | `sections/references.j2` | `github_repo`, `demo_url`, `custom_references` |
| `render_algorithm()` | `algorithms/algorithm_section.j2` | `name`, `title`, `purpose`, `theory`, `complexity`, `advantages`, `limitations` |

## That's It!

You're ready to use the template system. Edit templates, render content, enjoy!
