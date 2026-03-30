# DOCX Renderer - Quick Reference

## Installation

```bash
pip install python-docx>=0.8.11
```

## Basic Usage

```python
from source.renderers import ReportRenderer

renderer = ReportRenderer()

report_data = {
    'metadata': {
        'title': 'Report Title',
        'organization': 'University',
        'faculty': 'Faculty',
        'students': [{'name': 'Name', 'id': 'ID'}]
    },
    'sections': [
        {'type': 'cover', 'title': 'Cover'},
        {'type': 'chapter', 'title': 'CHAPTER', 'level': 1, 'content': 'Text'}
    ],
    'evidence': {'figures': [], 'tables': []}
}

renderer.render(report_data, 'output/report.docx')
```

## Section Types

```python
# Cover page
{'type': 'cover', 'title': 'Cover'}

# Table of contents (with real TOC field)
{'type': 'toc', 'title': 'TABLE OF CONTENTS'}

# Acknowledgment
{'type': 'acknowledgment', 'title': 'ACKNOWLEDGMENT', 'content': 'Text'}

# Commitment
{'type': 'commitment', 'title': 'COMMITMENT', 'content': 'Text'}

# Chapter (auto-numbered)
{'type': 'chapter', 'title': 'TITLE', 'level': 1, 'content': 'Text',
 'subsections': [...]}

# Standard section
{'type': 'section', 'title': 'TITLE', 'level': 1, 'content': 'Text'}

# Conclusion
{'type': 'conclusion', 'title': 'CONCLUSION', 'content': 'Text'}

# References
{'type': 'references', 'title': 'REFERENCES',
 'references': ['Ref 1', 'Ref 2']}
```

## Evidence

### Images

```python
'evidence': {
    'figures': [
        {
            'section_id': 'section_id',
            'path': 'path/to/image.png',
            'caption': 'Figure caption'
        }
    ]
}
```

### Tables

```python
'evidence': {
    'tables': [
        {
            'section_id': 'section_id',
            'headers': ['Col1', 'Col2'],
            'rows': [['A', 'B'], ['C', 'D']],
            'caption': 'Table caption'
        }
    ]
}
```

## Custom Styles

```python
from source.renderers import ReportRenderer, StyleManager
from docx.shared import Pt, Cm

custom_styles = {
    'normal': {
        'font_size': Pt(12),
        'line_spacing': 1.15
    },
    'heading1': {
        'font_size': Pt(18)
    },
    'page': {
        'left_margin': Cm(2.5),
        'right_margin': Cm(2.5)
    }
}

style_manager = StyleManager(custom_styles)
renderer = ReportRenderer(style_manager)
```

## Content Formatting

### Bullet Lists
```python
content = """
- Item 1
- Item 2
- Item 3
"""
```

### Numbered Lists
```python
content = """
1. First
2. Second
3. Third
"""
```

### Code Blocks
```python
content = """
Code example:

```
def hello():
    print("Hello")
```

More text.
"""
```

## Components

### StyleManager
```python
from source.renderers import StyleManager

style_manager = StyleManager(custom_styles)
style_manager.apply_to_document(doc)
```

### DocumentBuilder
```python
from source.renderers import DocumentBuilder

builder = DocumentBuilder(doc, style_manager)
builder.add_heading("Title", level=1)
builder.add_paragraph("Text")
builder.add_image("path.png", caption="Caption")
builder.add_table(headers, rows)
builder.add_toc()
```

### ReportRenderer
```python
from source.renderers import ReportRenderer

renderer = ReportRenderer(style_manager)
renderer.render(report_data, output_path)
```

## Examples

```bash
# Quick demo
python examples/renderer_quick_demo.py

# All examples
python examples/renderer_usage.py
```

## Common Patterns

### Complete Report
```python
report_data = {
    'metadata': {...},
    'sections': [
        {'type': 'cover'},
        {'type': 'toc'},
        {'type': 'acknowledgment', ...},
        {'type': 'chapter', 'title': 'INTRO', ...},
        {'type': 'chapter', 'title': 'METHODS', ...},
        {'type': 'chapter', 'title': 'RESULTS', ...},
        {'type': 'conclusion', ...},
        {'type': 'references', ...}
    ],
    'evidence': {...}
}
```

### Chapter with Subsections
```python
{
    'type': 'chapter',
    'title': 'CHAPTER TITLE',
    'level': 1,
    'content': 'Chapter intro',
    'subsections': [
        {
            'id': 'section_1',
            'title': 'Section 1',
            'level': 2,
            'content': 'Section content'
        },
        {
            'id': 'section_2',
            'title': 'Section 2',
            'level': 2,
            'content': 'Section content'
        }
    ]
}
```

## Tips

1. Use section IDs to link evidence
2. Check image paths exist
3. Right-click TOC in Word to update
4. Test with small reports first
5. Customize styles via StyleManager
6. Separate content generation from rendering
