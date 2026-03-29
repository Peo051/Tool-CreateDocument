# PDF Export Guide

PDF export support for the report generator using ReportLab.

## Overview

The PDF renderer provides direct PDF generation from the same document structure used by the DOCX renderer. It uses an intermediate representation approach for stability and maintainability.

## Architecture

```
Report Data (Dict)
    ↓
PDFReportRenderer
    ↓
PDFBuilder (Flowables)
    ↓
PDFStyleManager (Styles)
    ↓
ReportLab (PDF Generation)
```

## Installation

```bash
pip install reportlab>=3.6.0
```

Or:

```bash
pip install -r requirements_pdf.txt
```

## Quick Start

### Basic PDF Generation

```python
from source.renderers import PDFReportRenderer

renderer = PDFReportRenderer()

report_data = {
    'metadata': {
        'title': 'My Report',
        'organization': 'University',
        'faculty': 'Engineering',
        'students': [{'name': 'John Doe', 'id': '123'}]
    },
    'sections': [
        {'type': 'cover', 'title': 'Cover'},
        {'type': 'chapter', 'title': 'INTRODUCTION', 'level': 1, 'content': 'Text'}
    ],
    'evidence': {'figures': [], 'tables': []}
}

renderer.render(report_data, 'output/report.pdf')
```

### Generate Both DOCX and PDF

```python
from source.renderers import ReportRenderer, PDFReportRenderer

# Same report data for both formats
report_data = {...}

# Generate DOCX
docx_renderer = ReportRenderer()
docx_renderer.render(report_data, 'output/report.docx')

# Generate PDF
pdf_renderer = PDFReportRenderer()
pdf_renderer.render(report_data, 'output/report.pdf')
```

## Components

### 1. PDFStyleManager

Centralized PDF styling configuration.

```python
from source.renderers import PDFStyleManager

# Default styles
style_manager = PDFStyleManager()

# Custom styles
custom_styles = {
    'CustomNormal': {
        'fontSize': 12,
        'leading': 18
    }
}
style_manager = PDFStyleManager(custom_styles)
```

**Available Styles**:
- `CustomNormal` - Normal text
- `CustomHeading1` - Heading level 1
- `CustomHeading2` - Heading level 2
- `CustomHeading3` - Heading level 3
- `Caption` - Image/table captions
- `CustomCode` - Code blocks
- `CustomBullet` - Bullet lists
- `Centered` - Centered text

### 2. PDFBuilder

Low-level PDF element construction.

```python
from source.renderers import PDFBuilder

builder = PDFBuilder(style_manager)

# Add elements
builder.add_heading("Title", level=1)
builder.add_paragraph("Content")
builder.add_bullet_list(["Item 1", "Item 2"])
builder.add_image("path/to/image.png", caption="Figure 1")
builder.add_table(headers, rows)
builder.add_code_block("code here")
builder.add_page_break()

# Get flowables
story = builder.get_story()
```

### 3. PDFReportRenderer

High-level PDF report rendering.

```python
from source.renderers import PDFReportRenderer

renderer = PDFReportRenderer()
renderer.render(report_data, 'output/report.pdf')
```

## Data Structure

The PDF renderer uses the **same data structure** as the DOCX renderer:

```python
report_data = {
    'metadata': {
        'title': str,
        'organization': str,
        'faculty': str,
        'students': [{'name': str, 'id': str}],
        'advisor': str,
        'class_name': str,
        'report_type': str
    },
    'sections': [
        {
            'type': str,  # cover, toc, chapter, etc.
            'title': str,
            'level': int,
            'content': str,
            'subsections': [...]
        }
    ],
    'evidence': {
        'figures': [
            {
                'section_id': str,
                'path': str,
                'caption': str
            }
        ],
        'tables': [
            {
                'section_id': str,
                'headers': [str],
                'rows': [[Any]],
                'caption': str
            }
        ]
    }
}
```

## Features

### Supported Elements

✅ **Cover Page** - With metadata
✅ **Headings** - Levels 1-3 with numbering
✅ **Paragraphs** - Justified text
✅ **Bullet Lists** - Bulleted items
✅ **Numbered Lists** - Numbered items
✅ **Images** - With captions
✅ **Tables** - Styled tables with headers
✅ **Code Blocks** - Monospace with background
✅ **Page Breaks** - Section separation
✅ **Chapter Numbering** - Automatic

### Section Types

Same as DOCX renderer:
- `cover` - Cover page
- `toc` - Table of contents
- `acknowledgment` - Acknowledgment
- `commitment` - Commitment/declaration
- `chapter` - Numbered chapter
- `section` - Standard section
- `conclusion` - Conclusion
- `references` - References

## Examples

### Example 1: Basic PDF

```bash
python examples/pdf_renderer_demo.py
```

### Example 2: Dual Format

```bash
python examples/dual_format_demo.py
```

## Integration

### With Chart Builder

```python
from source.charts import ChartBuilder, ChartRequest, BarChartData
from source.renderers import PDFReportRenderer

# Generate chart
chart_builder = ChartBuilder()
chart_result = chart_builder.build(ChartRequest(...))

# Render PDF with chart
renderer = PDFReportRenderer()
report_data = {
    'sections': [...],
    'evidence': {
        'figures': [
            {
                'section_id': 'results',
                'path': chart_result.file_path,
                'caption': chart_result.caption
            }
        ]
    }
}
renderer.render(report_data, 'output/report.pdf')
```

### With Generators

```python
from source.generators import IntroductionGenerator
from source.renderers import PDFReportRenderer

# Generate content
generator = IntroductionGenerator()
section = generator.generate({...})

# Convert to report format
report_data = {
    'sections': [
        {
            'type': 'chapter',
            'title': section.title,
            'content': section.content,
            'subsections': [...]
        }
    ]
}

# Render to PDF
renderer = PDFReportRenderer()
renderer.render(report_data, 'output/report.pdf')
```

## Styling

### Page Configuration

```python
from source.renderers import PDFStyleManager

style_manager = PDFStyleManager()
page_config = style_manager.get_page_config()

# Returns:
{
    'pagesize': A4,
    'leftMargin': 3*cm,
    'rightMargin': 2*cm,
    'topMargin': 2*cm,
    'bottomMargin': 2*cm
}
```

### Custom Styles

```python
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_JUSTIFY

custom_styles = {
    'CustomNormal': {
        'fontSize': 12,
        'leading': 18,
        'alignment': TA_JUSTIFY
    },
    'CustomHeading1': {
        'fontSize': 18,
        'leading': 22
    }
}

style_manager = PDFStyleManager(custom_styles)
renderer = PDFReportRenderer(style_manager)
```

## Comparison: DOCX vs PDF

| Feature | DOCX | PDF |
|---------|------|-----|
| Editable | ✅ Yes | ❌ No |
| TOC Field | ✅ Real field | ⚠️ Static |
| File Size | Smaller | Larger |
| Fonts | System fonts | Embedded |
| Images | Linked/embedded | Embedded |
| Tables | Editable | Fixed |
| Portability | Medium | High |
| Print-ready | Medium | High |

## Best Practices

1. **Use Same Data Structure**: Both renderers use identical input
2. **Test with Small Reports**: Start small, then scale up
3. **Check Image Paths**: Ensure images exist before rendering
4. **Handle Errors**: PDF generation can fail on invalid images
5. **Consider File Size**: PDFs with many images can be large
6. **Use Appropriate Format**: DOCX for editing, PDF for distribution

## Troubleshooting

### Images Not Appearing

Check that:
- Image file exists
- Path is correct
- Image format is supported (PNG, JPG)
- Pillow is installed

### Table Formatting Issues

- Ensure all rows have same column count
- Keep cell content reasonable length
- Use appropriate table width

### Font Issues

ReportLab uses standard fonts:
- Times-Roman
- Times-Bold
- Times-Italic
- Courier (for code)

### Large File Size

- Compress images before adding
- Use appropriate image resolution
- Consider splitting into multiple PDFs

## Advanced Usage

### Custom Page Size

```python
from reportlab.lib.pagesizes import letter, A4, legal

# Modify page config in PDFStyleManager
```

### Custom Colors

```python
from reportlab.lib.colors import HexColor

# Use in table styling or text
```

### Multiple Columns

ReportLab supports multi-column layouts (advanced).

## API Reference

### PDFStyleManager

```python
PDFStyleManager(custom_styles: Dict[str, Any] = None)
    .get_style(name: str) -> ParagraphStyle
    .get_page_config() -> Dict[str, Any]
```

### PDFBuilder

```python
PDFBuilder(style_manager: PDFStyleManager)
    .add_heading(text, level, numbered, number)
    .add_paragraph(text, style_name)
    .add_bullet_list(items)
    .add_numbered_list(items)
    .add_image(path, width, caption)
    .add_caption(text, prefix)
    .add_table(headers, rows)
    .add_code_block(code)
    .add_page_break()
    .add_spacer(height)
    .add_centered_text(text, size, bold)
    .get_story() -> List[Flowable]
```

### PDFReportRenderer

```python
PDFReportRenderer(style_manager: PDFStyleManager = None)
    .render(report_data: Dict[str, Any], output_path: str) -> str
```

## Dependencies

```
reportlab>=3.6.0
Pillow>=9.0.0  # For image handling
```

## Run Instructions

```bash
# Install dependencies
pip install reportlab Pillow

# Run PDF demo
python examples/pdf_renderer_demo.py

# Run dual format demo
python examples/dual_format_demo.py

# Check output
ls output/*.pdf
```

## Summary

The PDF renderer provides:
- ✅ Direct PDF generation
- ✅ Same data structure as DOCX
- ✅ Stable implementation with ReportLab
- ✅ All document elements supported
- ✅ Easy integration
- ✅ Production-ready

Perfect for generating print-ready, distributable reports.
