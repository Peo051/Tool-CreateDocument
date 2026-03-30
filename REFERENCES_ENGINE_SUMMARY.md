# References Engine Implementation

## Status: ✅ COMPLETE

Implemented practical references engine with APA and IEEE citation formatting, bibliography generation, and pipeline integration.

## New Files

### Core Engine
- `source/references/__init__.py` - Package exports
- `source/references/models.py` - ReferenceEntry data model
- `source/references/formatter.py` - APAFormatter, IEEEFormatter
- `source/references/bibliography.py` - BibliographyGenerator

### Tests
- `tests/test_references.py` - 15 tests (all passing)

### Examples
- `examples/references_usage.py` - Basic usage examples
- `examples/references_integration_demo.py` - Integration with config

## Modified Files

### Integration
- `source/orchestrator.py` - Added `_generate_bibliography()` method in `step_bind_evidence()`
- `source/renderers/docx_renderer.py` - Enhanced `_render_references()` for formatted output

## Features

### Citation Formatters
- **APA 7th Edition**: Author-date style with proper formatting
- **IEEE**: Numbered citations with standard format
- Extensible base class for adding more styles

### Bibliography Generation
- Numbered (IEEE) or unnumbered (APA) lists
- Handles books, articles, conferences, websites
- Optional fields: DOI, URL, volume, issue, pages
- Graceful handling of missing fields

### Data Models
- `ReferenceEntry`: Unified reference model
- Converters from `config_models.Reference` and `schema.Reference`
- Validation: authors required, year 1900-2100

### Integration
- Auto-generates bibliography from config references
- Citation style from `format_rules.citation_style`
- Fallback to IEEE if not specified
- Non-breaking: skips if references module unavailable

## Usage

### Basic Formatting
```python
from references import ReferenceEntry, IEEEFormatter

ref = ReferenceEntry(
    id="1",
    authors=["John Smith"],
    title="Example Article",
    year=2020,
    type="article"
)

formatter = IEEEFormatter()
print(formatter.format_citation(ref))  # Full citation
print(formatter.format_inline(ref))    # [1]
```

### Bibliography Generation
```python
from references import BibliographyGenerator

gen = BibliographyGenerator(style='IEEE')
bib = gen.generate(references)  # Formatted text
section = gen.generate_section(references)  # Section data
```

### Config Integration
```json
{
  "evidence": {
    "references": [
      {
        "id": "1",
        "authors": ["Stuart Russell", "Peter Norvig"],
        "title": "Artificial Intelligence: A Modern Approach",
        "year": 2020,
        "source": "Pearson"
      }
    ]
  },
  "format_rules": {
    "citation_style": "IEEE"
  }
}
```

## Test Coverage

All 15 tests passing:
- Reference entry creation and validation
- APA formatting (single/multiple authors, books)
- IEEE formatting (articles, journals with volume/issue/pages)
- Bibliography generation (IEEE/APA)
- Section data generation
- Inline citations
- URL and DOI handling
- Empty bibliography handling

## Run Tests
```bash
python -m pytest tests/test_references.py -v
```

## Run Examples
```bash
python examples/references_usage.py
python examples/references_integration_demo.py
```

## Architecture

```
Config (references) → ReferenceEntry → Formatter → Bibliography
                                          ↓
                                    Section Data → Renderer → DOCX
```

## Extension Points

Add new citation styles:
```python
class MLAFormatter(CitationFormatter):
    def format_citation(self, ref):
        # MLA formatting logic
        pass
    
    def format_inline(self, ref):
        # MLA inline citation
        pass

# Register
BibliographyGenerator.FORMATTERS['MLA'] = MLAFormatter
```

## Notes

- Non-breaking integration: fails gracefully if references missing
- Deterministic output: same input → same output
- Compact implementation: ~400 lines total
- Reuses existing Reference models from config_models.py
- Ready for production use
