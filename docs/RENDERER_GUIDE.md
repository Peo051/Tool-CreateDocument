# DOCX Renderer Guide

Clean, maintainable DOCX renderer for professional report generation.

## Architecture

```
ReportRenderer (High-level)
    ↓
DocumentBuilder (Mid-level utilities)
    ↓
StyleManager (Centralized styling)
    ↓
python-docx (Low-level API)
```

## Components

### 1. StyleManager

Centralized style configuration and management.

```python
from source.renderers import StyleManager

# Default styles
style_manager = StyleManager()

# Custom styles
custom_styles = {
    'normal': {
        'font_size': Pt(12),
        'line_spacing': 1.15
    },
    'heading1': {
        'font_size': Pt(18)
    }
}
style_manager = StyleManager(custom_styles)
```

**Features**:
- Page layout configuration
- Text style management
- Heading styles (1-3)
- Caption styles
- Code block styles
- Table styles

### 2. DocumentBuilder

Low-level document construction utilities.

```python
from source.renderers import DocumentBuilder

builder = DocumentBuilder(doc, style_manager)

# Add elements
builder.add_heading("Title", level=1)
builder.add_paragraph("Content")
builder.add_bullet_list(["Item 1", "Item 2"])
builder.add_image("path/to/image.png", caption="Figure 1")
builder.add_table(headers, rows)
builder.add_code_block("code here")
builder.add_toc()
builder.add_page_break()
```

**Features**:
- Numbered headings
- Styled paragraphs
- Bullet/numbered lists
- Images with captions
- Tables with styling
- Code blocks with syntax highlighting
- Real TOC field
- Page breaks

### 3. ReportRenderer

High-level report rendering.

```python
from source.renderers import ReportRenderer

renderer = ReportRenderer()

report_data = {
    'metadata': {...},
    'sections': [...],
    'evidence': {...}
}

output_path = renderer.render(report_data, 'output/report.docx')
```

**Features**:
- Structured report rendering
- Section type routing
- Automatic numbering
- Evidence integration
- Metadata handling

## Quick Start

### Basic Report

```python
from source.renderers import ReportRenderer

renderer = ReportRenderer()

report_data = {
    'metadata': {
        'title': 'My Report',
        'organization': 'University',
        'faculty': 'Engineering',
        'students': [{'name': 'John Doe', 'id': '123'}]
    },
    'sections': [
        {
            'type': 'cover',
            'title': 'Cover'
        },
        {
            'type': 'chapter',
            'title': 'INTRODUCTION',
            'level': 1,
            'content': 'Introduction text here.'
        }
    ],
    'evidence': {'figures': [], 'tables': []}
}

renderer.render(report_data, 'output/report.docx')
```

## Report Data Structure

### Metadata

```python
{
    'title': str,              # Required
    'subtitle': str,           # Optional
    'organization': str,       # Required (or 'university')
    'faculty': str,            # Required
    'advisor': str,            # Optional
    'students': [              # Required
        {
            'name': str,
            'id': str
        }
    ],
    'class_name': str,         # Optional
    'report_type': str         # 'thesis', 'technical_report', 'project_report'
}
```

### Sections

```python
{
    'type': str,               # Section type
    'title': str,              # Section title
    'level': int,              # Heading level (1-3)
    'content': str,            # Section content
    'subsections': [           # Optional subsections
        {
            'id': str,         # Section ID for evidence
            'title': str,
            'level': int,
            'content': str
        }
    ]
}
```

**Section Types**:
- `cover` - Cover page
- `toc` - Table of contents
- `acknowledgment` - Acknowledgment section
- `commitment` - Commitment/declaration
- `chapter` - Numbered chapter
- `section` - Standard section
- `conclusion` - Conclusion
- `references` - References/bibliography

### Evidence

```python
{
    'figures': [
        {
            'section_id': str,     # Section to insert in
            'path': str,           # Image file path
            'caption': str         # Image caption
        }
    ],
    'tables': [
        {
            'section_id': str,     # Section to insert in
            'headers': [str],      # Column headers
            'rows': [[Any]],       # Table rows
            'caption': str         # Table caption
        }
    ]
}
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
1. First item
2. Second item
3. Third item
"""
```

### Code Blocks

```python
content = """
Here is some code:

```
def hello():
    print("Hello, World!")
```

More text here.
"""
```

## Custom Styling

### Page Layout

```python
custom_styles = {
    'page': {
        'width': Cm(21),
        'height': Cm(29.7),
        'left_margin': Cm(2.5),
        'right_margin': Cm(2.5),
        'top_margin': Cm(2),
        'bottom_margin': Cm(2)
    }
}
```

### Text Styles

```python
custom_styles = {
    'normal': {
        'font_name': 'Arial',
        'font_size': Pt(12),
        'line_spacing': 1.15,
        'alignment': WD_ALIGN_PARAGRAPH.JUSTIFY
    }
}
```

### Heading Styles

```python
custom_styles = {
    'heading1': {
        'font_name': 'Arial',
        'font_size': Pt(18),
        'bold': True,
        'alignment': WD_ALIGN_PARAGRAPH.CENTER
    }
}
```

## Advanced Features

### Table of Contents

The renderer adds a real TOC field that updates in Word:

```python
{
    'type': 'toc',
    'title': 'TABLE OF CONTENTS'
}
```

**Note**: Right-click and select "Update Field" in Word to generate TOC.

### Numbered Chapters

Chapters are automatically numbered:

```python
{
    'type': 'chapter',
    'title': 'INTRODUCTION',  # Becomes "CHƯƠNG 1. INTRODUCTION"
    'level': 1
}
```

### Images with Captions

```python
evidence = {
    'figures': [
        {
            'section_id': 'results',
            'path': 'charts/performance.png',
            'caption': 'Performance comparison'
        }
    ]
}
```

### Tables with Styling

```python
evidence = {
    'tables': [
        {
            'section_id': 'results',
            'headers': ['Algorithm', 'Time', 'Memory'],
            'rows': [
                ['BFS', '120ms', '45MB'],
                ['DFS', '95ms', '30MB']
            ],
            'caption': 'Performance metrics'
        }
    ]
}
```

## Integration Example

### With Chart Builder

```python
from source.charts import ChartBuilder, ChartRequest, BarChartData
from source.renderers import ReportRenderer

# Generate chart
chart_builder = ChartBuilder()
chart_request = ChartRequest(
    id="perf_chart",
    title="Performance",
    type="bar",
    data=BarChartData(categories=["A", "B"], values=[10, 20])
)
chart_result = chart_builder.build(chart_request)

# Render report with chart
renderer = ReportRenderer()
report_data = {
    'metadata': {...},
    'sections': [
        {
            'type': 'chapter',
            'title': 'RESULTS',
            'subsections': [
                {
                    'id': 'results_perf',
                    'title': 'Performance',
                    'content': 'See chart below.'
                }
            ]
        }
    ],
    'evidence': {
        'figures': [
            {
                'section_id': 'results_perf',
                'path': chart_result.file_path,
                'caption': chart_result.caption
            }
        ]
    }
}

renderer.render(report_data, 'output/report.docx')
```

### With Generators

```python
from source.generators import IntroductionGenerator
from source.renderers import ReportRenderer

# Generate content
generator = IntroductionGenerator()
section = generator.generate({
    'title': 'My Project',
    'domain': 'AI',
    'objectives': ['Objective 1', 'Objective 2']
})

# Convert to report format
report_data = {
    'metadata': {...},
    'sections': [
        {
            'type': 'chapter',
            'title': section.title,
            'content': section.content,
            'subsections': [
                {
                    'title': sub.title,
                    'content': sub.content,
                    'level': sub.level
                }
                for sub in section.subsections
            ]
        }
    ],
    'evidence': {'figures': [], 'tables': []}
}

renderer = ReportRenderer()
renderer.render(report_data, 'output/report.docx')
```

## Examples

### Example 1: Basic Report

```bash
python examples/renderer_quick_demo.py
```

### Example 2: Complete Report

```bash
python examples/renderer_usage.py
```

## Dependencies

```bash
pip install python-docx>=0.8.11
```

Or:

```bash
pip install -r requirements_renderer.txt
```

## Best Practices

1. **Separate Concerns**: Keep content generation separate from rendering
2. **Use Section IDs**: Link evidence to sections via IDs
3. **Centralize Styles**: Use StyleManager for consistent styling
4. **Validate Data**: Ensure report_data structure is correct
5. **Test Incrementally**: Test each section type separately
6. **Handle Missing Files**: Check image paths exist before rendering

## Troubleshooting

### TOC Not Showing

Right-click the TOC field in Word and select "Update Field".

### Images Not Appearing

Check that image paths are correct and files exist.

### Styling Not Applied

Ensure StyleManager is passed to ReportRenderer:

```python
style_manager = StyleManager(custom_styles)
renderer = ReportRenderer(style_manager)
```

### Section Numbering Issues

Ensure section type is 'chapter' for automatic numbering.

## API Reference

### StyleManager

```python
StyleManager(custom_styles: Dict[str, Any] = None)
    .apply_to_document(doc: Document)
    .get_style(style_name: str) -> Dict[str, Any]
```

### DocumentBuilder

```python
DocumentBuilder(doc: Document, style_manager: StyleManager)
    .add_heading(text, level, numbered, number)
    .add_paragraph(text, style, alignment, bold, italic)
    .add_bullet_list(items)
    .add_numbered_list(items)
    .add_image(path, width, caption)
    .add_caption(text, prefix)
    .add_table(headers, rows, style)
    .add_code_block(code)
    .add_toc()
    .add_page_break()
    .add_centered_text(text, size, bold)
```

### ReportRenderer

```python
ReportRenderer(style_manager: StyleManager = None)
    .render(report_data: Dict[str, Any], output_path: str) -> str
```

## Summary

The DOCX renderer provides:
- ✅ Clean separation of concerns
- ✅ Centralized style management
- ✅ Support for all document elements
- ✅ Real TOC field generation
- ✅ Automatic section numbering
- ✅ Evidence integration
- ✅ Maintainable code structure

Perfect for professional report generation.
