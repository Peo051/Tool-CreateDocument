# Academic Report Generator

> Automated report generation system with modular pipeline architecture, template-based content, and multiple output formats

## Overview

This tool generates structured academic reports (thesis, technical reports, project reports) from JSON configuration files. It features a modular pipeline architecture with validation, content generation, evidence binding, and rendering stages.

## Current Capabilities

### Core Features
- **4 Report Types**: thesis, technical_report, project_report, business_report
- **Modular Pipeline**: 7-stage orchestration (load → validate → plan → generate → bind → render → review)
- **Template System**: Jinja2-based content templates
- **Multiple Renderers**: DOCX (stable), PDF (requires optional dependencies)
- **Input Validation**: Pydantic v2 models with type checking
- **Content Generators**: 7 section generators (introduction, methodology, conclusion, etc.)
- **Optional LLM Integration**: Provider-agnostic enhancement layer (OpenAI, Anthropic, Mock)
- **Chart Generation**: Bar, line, pie charts with matplotlib
- **Review Engine**: 7 quality checks for generated reports
- **References Engine**: APA and IEEE citation formatting with bibliography generation

### Supported Languages
- Vietnamese (vi)
- English (en)

## Current Status & Limitations

### Working
- ✅ Report generation pipeline (DOCX output)
- ✅ Config validation with Pydantic
- ✅ Template-based content generation
- ✅ Chart/diagram generation
- ✅ Review engine with quality checks
- ✅ References and bibliography (APA, IEEE)
- ✅ 56 tests passing (97% pass rate)

### Known Issues
- ⚠️ PDF renderer requires optional dependencies (reportlab)
- ⚠️ Integration tests may fail on systems without matplotlib/tcl properly configured
- ⚠️ Chart generation depends on matplotlib backend configuration

### Not Production-Ready
This is a functional development tool. Use with caution for critical work:
- Test coverage is good but not comprehensive
- Error handling is present but may not cover all edge cases
- Performance has not been optimized for large reports

## Installation

### Requirements
- Python 3.8+
- pip

### Basic Installation
```bash
pip install -r requirements_pro.txt
```

### Optional: PDF Support
```bash
pip install -r requirements_pdf.txt
```

## Quick Start

### 1. Create Configuration

Create `my_config.json`:
```json
{
  "project_info": {
    "title": "My Project Title",
    "description": "A detailed description of the project",
    "students": [
      {"name": "Student Name", "id": "123456"}
    ],
    "university": "University Name"
  },
  "report_profile": {
    "report_type": "project_report",
    "language": "en"
  },
  "technical_data": {
    "algorithms": ["BFS", "DFS"],
    "technologies": ["Python"]
  }
}
```

### 2. Generate Report

```bash
python source/main.py --config my_config.json --output output/report.docx
```

### 3. Check Output

Open `output/report.docx` in Microsoft Word or LibreOffice.

## Configuration

### Recommended: Pydantic Format

Use the structured format with validation:

```json
{
  "project_info": {
    "title": "Project Title",
    "description": "Project description (min 10 chars)",
    "students": [{"name": "Name", "id": "ID"}],
    "university": "University Name",
    "advisor": "Advisor Name"
  },
  "report_profile": {
    "report_type": "project_report",
    "language": "vi"
  },
  "technical_data": {
    "algorithms": ["DFS", "BFS", "A*"],
    "technologies": ["Python", "NetworkX"]
  },
  "evidence": {
    "references": [
      {
        "id": "1",
        "authors": ["Author Name"],
        "title": "Paper Title",
        "year": 2020,
        "source": "Journal/Conference"
      }
    ]
  },
  "format_rules": {
    "citation_style": "IEEE",
    "font_size": 13,
    "line_spacing": 1.5
  }
}
```

See `examples/config_full.json` for complete example.

### Legacy Format (Compatibility)

Flat structure still supported:
```json
{
  "title": "Project Title",
  "students": [{"name": "Name", "id": "ID"}],
  "university": "University",
  "algorithms": ["DFS", "BFS"]
}
```

Convert legacy to new format:
```bash
python migrate_config.py old_config.json
```

## Usage

### Basic Command
```bash
python source/main.py --config config.json
```

### Options
```bash
# Specify output path
python source/main.py --config config.json --output reports/my_report.docx

# Quiet mode (minimal output)
python source/main.py --quiet

# Help
python source/main.py --help
```

### Pipeline Stages
The orchestrator runs 7 stages:
1. **Load Config** - Read and parse configuration
2. **Validate** - Validate with Pydantic models
3. **Plan Outline** - Generate report structure
4. **Generate Content** - Create section content
5. **Bind Evidence** - Attach charts, references
6. **Render** - Create DOCX file
7. **Review** - Quality checks

## Examples

### Run Examples
```bash
# Outline planner
python examples/outline_planner_usage.py

# Section generators
python examples/generators_usage.py

# Chart generation
python examples/chart_quick_demo.py

# LLM integration
python examples/llm_quick_demo.py

# References
python examples/references_usage.py

# Review engine
python examples/review_engine_demo.py

# Full renderer
python examples/renderer_quick_demo.py
```

### Example Configs
- `examples/config_minimal.json` - Minimal required fields
- `examples/config_full.json` - All available options
- `examples/full_project_report.json` - Complete project report

## Testing

### Run All Tests
```bash
python -m pytest tests/ -v
```

### Run Specific Test Suite
```bash
# Config validation
python -m pytest tests/test_config_validation.py -v

# Generators
python -m pytest tests/test_generators.py -v

# References
python -m pytest tests/test_references.py -v

# Review engine
python -m pytest tests/test_review_engine.py -v
```

### Test Status
- 56 tests total
- 54 passing (97%)
- 2 skipped (PDF dependencies)

## Project Structure

```
.
├── source/                      # Source code
│   ├── main.py                  # Main entry point (recommended)
│   ├── orchestrator.py          # Pipeline orchestrator
│   ├── config_models.py         # Pydantic models
│   ├── schema.py                # Alternative schema
│   ├── outline_planner.py       # Report structure planner
│   ├── pipeline/                # Pipeline stages
│   │   ├── validator.py
│   │   ├── planner.py
│   │   ├── generator.py
│   │   ├── binder.py
│   │   └── renderer.py
│   ├── generators/              # Section generators
│   │   ├── base.py
│   │   ├── introduction.py
│   │   ├── methodology.py
│   │   └── ...
│   ├── llm/                     # Optional LLM integration
│   │   ├── interface.py
│   │   ├── providers.py
│   │   └── enhancer.py
│   ├── references/              # Citation & bibliography
│   │   ├── formatter.py         # APA, IEEE formatters
│   │   ├── bibliography.py
│   │   └── models.py
│   ├── charts/                  # Chart generation
│   │   ├── builder.py
│   │   └── models.py
│   ├── review/                  # Quality checks
│   │   ├── engine.py
│   │   ├── checks.py
│   │   └── models.py
│   ├── renderers/               # Output renderers
│   │   ├── docx_renderer.py
│   │   └── pdf_renderer.py
│   ├── templates/               # Jinja2 templates
│   │   ├── sections/
│   │   └── algorithms/
│   └── legacy_main.py           # Legacy entry point
│
├── tests/                       # Test suite
│   ├── test_config_validation.py
│   ├── test_generators.py
│   ├── test_references.py
│   ├── test_review_engine.py
│   └── ...
│
├── examples/                    # Usage examples
│   ├── config_minimal.json
│   ├── config_full.json
│   ├── outline_planner_usage.py
│   ├── generators_usage.py
│   ├── references_usage.py
│   └── ...
│
├── docs/                        # Documentation
│   └── instruct/
│       ├── DEVELOPER_GUIDE.md
│       ├── QUICK_START.md
│       └── ...
│
├── output/                      # Generated reports
├── diagrams/                    # Generated diagrams
├── README.md                    # This file
├── requirements_pro.txt         # Core dependencies
├── requirements_pdf.txt         # PDF dependencies
└── pytest.ini                   # Test configuration
```

## Documentation

### Guides
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Command reference
- [INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md) - Config integration
- [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) - Legacy migration
- [ORCHESTRATOR_GUIDE.md](ORCHESTRATOR_GUIDE.md) - Pipeline architecture
- [docs/instruct/DEVELOPER_GUIDE.md](docs/instruct/DEVELOPER_GUIDE.md) - Developer guide

### Component Docs
- [OUTLINE_PLANNER.md](OUTLINE_PLANNER.md) - Outline planner
- [GENERATORS_README.md](GENERATORS_README.md) - Section generators
- [LLM_INTEGRATION_GUIDE.md](LLM_INTEGRATION_GUIDE.md) - LLM integration
- [CHART_BUILDER_GUIDE.md](CHART_BUILDER_GUIDE.md) - Chart generation
- [REVIEW_ENGINE_GUIDE.md](REVIEW_ENGINE_GUIDE.md) - Review engine
- [REFERENCES_ENGINE_SUMMARY.md](REFERENCES_ENGINE_SUMMARY.md) - References & citations

## Roadmap

### High Priority
- [ ] Improve test coverage to 100%
- [ ] Fix integration test stability
- [ ] Add comprehensive error messages
- [ ] Performance optimization for large reports

### Medium Priority
- [ ] Web interface for configuration
- [ ] More citation styles (MLA, Chicago)
- [ ] Advanced chart types
- [ ] Template customization UI
- [ ] Batch report generation

### Low Priority
- [ ] HTML output format
- [ ] Markdown output format
- [ ] Real-time collaboration
- [ ] Cloud deployment
- [ ] Plugin system

## Troubleshooting

### ModuleNotFoundError
```bash
pip install -r requirements_pro.txt
```

### Permission Denied
Close the output file if open in Word/LibreOffice.

### Matplotlib/Chart Errors
```bash
pip install --upgrade matplotlib
```

On Windows, ensure tcl/tk is properly installed with Python.

### PDF Generation Fails
Install PDF dependencies:
```bash
pip install -r requirements_pdf.txt
```

## Contributing

This is an academic project. Contributions welcome but no formal process established.

## License

MIT License - Free for educational use

---

**Version**: 1.0  
**Status**: Functional development tool  
**Python**: 3.8+
