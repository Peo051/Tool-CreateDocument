# Refactor Plan: Clean Pipeline Architecture

## Proposed File Tree

```
source/
├── pipeline/
│   ├── __init__.py
│   ├── validator.py          # Input validation
│   ├── planner.py             # Outline planning
│   ├── generator.py           # Section generation
│   ├── binder.py              # Evidence binding
│   └── renderer.py            # DOCX rendering
│
├── models/
│   ├── __init__.py
│   ├── report.py              # Report data models
│   ├── section.py             # Section models
│   └── evidence.py            # Evidence models
│
├── content/
│   ├── __init__.py
│   ├── algorithms.py          # Algorithm content (refactored)
│   ├── templates.py           # Content templates
│   └── diagrams.py            # Diagram generation (refactored)
│
├── renderers/
│   ├── __init__.py
│   ├── docx_renderer.py       # DOCX-specific rendering
│   └── pdf_renderer.py        # PDF rendering (future)
│
├── schema.py                  # Pydantic schemas (existing)
├── main.py                    # New entry point
└── legacy_main.py             # Old auto_report_pro_main.py (renamed)

## Migration Notes

1. **Backward Compatibility**: Old `auto_report_pro_main.py` → `legacy_main.py`
2. **New Entry**: `main.py` uses pipeline
3. **Gradual Migration**: Can use both old and new simultaneously
4. **Config Compatible**: Works with existing `report_config.json`
```
