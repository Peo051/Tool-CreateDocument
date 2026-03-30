# Academic Report Generator

> Automated report generation system with modular pipeline architecture

## Overview

Generate structured academic reports (thesis, technical reports, project reports) from JSON configuration files. Features a modular pipeline with validation, content generation, and multiple output formats.

## Quick Start

### Installation
```bash
pip install -r requirements_pro.txt
```

### Generate a Report
```bash
# CLI
python source/main.py --config examples/config_minimal.json --output output/report.docx

# Or as module
python -m source.main --config examples/config_minimal.json
```

### Start Web UI
```bash
# Terminal 1: Backend
python source/api.py

# Terminal 2: Frontend
cd web && npm install && npm run dev
```

Then open http://localhost:3000

## Entry Points

### Official Entry Points
- **CLI**: `source/main.py` - Command-line interface for report generation
- **API**: `source/api.py` - FastAPI REST API for web integration

### Compatibility Wrappers (Deprecated)
- `source/main_v2.py` - Forwards to main.py (deprecated)
- `source/legacy_main.py` - Forwards to main.py (deprecated)

**Note**: Always use `source/main.py` or `source/api.py` for new projects.

## Features

### Core Capabilities
- **4 Report Types**: thesis, technical_report, project_report, business_report
- **7-Stage Pipeline**: load → validate → plan → generate → bind → render → review
- **Multiple Formats**: DOCX (stable), PDF (optional)
- **Input Validation**: Pydantic v2 models with type checking
- **Chart Generation**: Bar, line, pie charts with matplotlib
- **References**: APA and IEEE citation formatting
- **Review Engine**: 7 quality checks for generated reports
- **Web UI**: React + TypeScript wizard interface

### Languages
- Vietnamese (vi)
- English (en)

## Configuration

### Minimal Example
```json
{
  "project_info": {
    "title": "My Project",
    "description": "Project description",
    "students": [{"name": "Student Name", "id": "123"}],
    "university": "University Name"
  },
  "report_profile": {
    "report_type": "project_report",
    "language": "en"
  }
}
```

See `examples/config_full.json` for all options.

### Legacy Format Migration
```bash
python migrate_config.py old_config.json
```

## CLI Usage

```bash
# Basic usage
python source/main.py --config config.json

# Specify output
python source/main.py --config config.json --output reports/my_report.docx

# Quiet mode
python source/main.py --config config.json --quiet

# Help
python source/main.py --help
```

## API Usage

### Start API Server
```bash
python source/api.py
# or
python run_api.py
```

Server runs on http://localhost:8000

### Endpoints
- `GET /api/health` - Health check
- `POST /api/validate` - Validate configuration
- `POST /api/preview` - Preview report outline
- `POST /api/generate` - Generate report (async job)
- `GET /api/jobs/{job_id}` - Check job status
- `GET /api/download/{file_id}` - Download generated report
- `POST /api/migrate-config` - Migrate legacy config

See `docs/WEB_UI_README.md` for full API documentation.

## Project Structure

```
.
├── source/                      # Source code
│   ├── main.py                  # ⭐ Official CLI entry point
│   ├── api.py                   # ⭐ Official API entry point
│   ├── orchestrator.py          # Pipeline orchestrator
│   ├── config_models.py         # Pydantic models
│   ├── pipeline/                # Pipeline stages
│   ├── generators/              # Section generators
│   ├── references/              # Citations & bibliography
│   ├── charts/                  # Chart generation
│   ├── review/                  # Quality checks
│   ├── renderers/               # Output renderers
│   └── templates/               # Jinja2 templates
│
├── web/                         # Web UI (React + TypeScript)
│   ├── src/
│   └── package.json
│
├── tests/                       # Test suite (56 tests, 97% pass)
├── examples/                    # Usage examples & configs
├── docs/                        # Documentation & guides
├── output/                      # Generated reports
│
├── README.md                    # This file
├── CHANGELOG.md                 # Version history
├── QUICK_START.md               # Quick start guide
├── requirements_pro.txt         # Core dependencies
└── requirements_api.txt         # API dependencies
```

## Testing

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific suite
python -m pytest tests/test_generators.py -v

# With coverage
python -m pytest tests/ --cov=source --cov-report=html
```

**Test Status**: 56 tests, 54 passing (97%), 2 skipped (PDF dependencies)

## Documentation

### Essential Docs
- [QUICK_START.md](QUICK_START.md) - Getting started guide
- [CHANGELOG.md](CHANGELOG.md) - Version history
- [CI_SETUP.md](CI_SETUP.md) - CI/CD setup

### Component Guides (in docs/)
- [WEB_UI_README.md](docs/WEB_UI_README.md) - Web UI setup
- [INTEGRATION_GUIDE.md](docs/INTEGRATION_GUIDE.md) - Integration guide
- [MIGRATION_GUIDE.md](docs/MIGRATION_GUIDE.md) - Config migration
- [ORCHESTRATOR_GUIDE.md](docs/ORCHESTRATOR_GUIDE.md) - Pipeline architecture
- [LLM_INTEGRATION_GUIDE.md](docs/LLM_INTEGRATION_GUIDE.md) - LLM integration
- [CHART_BUILDER_GUIDE.md](docs/CHART_BUILDER_GUIDE.md) - Chart generation
- [REVIEW_ENGINE_GUIDE.md](docs/REVIEW_ENGINE_GUIDE.md) - Quality checks

### Developer Docs (in docs/instruct/)
- [DEVELOPER_GUIDE.md](docs/instruct/DEVELOPER_GUIDE.md) - Developer guide
- [PROJECT_SUMMARY.md](docs/instruct/PROJECT_SUMMARY.md) - Project overview

## Examples

```bash
# Outline planner
python examples/outline_planner_usage.py

# Section generators
python examples/generators_usage.py

# Chart generation
python examples/chart_quick_demo.py

# References
python examples/references_usage.py

# Review engine
python examples/review_engine_demo.py
```

## Current Status

### Working ✅
- Report generation pipeline (DOCX)
- Config validation with Pydantic
- Template-based content generation
- Chart/diagram generation
- Review engine with quality checks
- References and bibliography (APA, IEEE)
- Web UI with wizard interface
- REST API with job processing

### Known Issues ⚠️
- PDF renderer requires optional dependencies
- Integration tests may fail without proper matplotlib/tcl setup
- Chart generation depends on matplotlib backend

### Not Production-Ready
This is a functional development tool. Use with caution for critical work:
- Test coverage is good but not comprehensive
- Error handling may not cover all edge cases
- Performance not optimized for large reports

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

### PDF Generation Fails
```bash
pip install -r requirements_pdf.txt
```

## Contributing

This is an academic project. Contributions welcome but no formal process established.

## License

MIT License - Free for educational use

---

**Version**: 2.0  
**Status**: Functional development tool  
**Python**: 3.8+  
**Entry Points**: `source/main.py` (CLI), `source/api.py` (API)
