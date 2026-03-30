# Contributing to Academic Report Generator

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 14+ (for web UI)
- Git

### Setup Development Environment

1. Clone the repository
```bash
git clone <repository-url>
cd CreateDocument
```

2. Install Python dependencies
```bash
pip install -r requirements_pro.txt
pip install -r requirements_test.txt
```

3. Install web UI dependencies (optional)
```bash
cd web
npm install
cd ..
```

4. Run tests to verify setup
```bash
python -m pytest tests/ -v
```

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
│   ├── references/              # Citations
│   ├── charts/                  # Charts
│   ├── review/                  # Quality checks
│   ├── renderers/               # Output renderers
│   └── templates/               # Jinja2 templates
│
├── web/                         # Web UI
├── tests/                       # Test suite
├── examples/                    # Examples
├── docs/                        # Documentation
└── output/                      # Generated reports
```

## Development Workflow

### Making Changes

1. Create a feature branch
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes

3. Run tests
```bash
python -m pytest tests/ -v
```

4. Run linting (optional)
```bash
ruff check source/
```

5. Commit your changes
```bash
git add .
git commit -m "Description of changes"
```

### Testing

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_generators.py -v

# Run with coverage
python -m pytest tests/ --cov=source --cov-report=html
```

### Adding New Features

#### Adding a New Section Generator

1. Create generator in `source/generators/`
2. Inherit from `BaseGenerator`
3. Implement `generate()` method
4. Add tests in `tests/test_generators.py`
5. Update documentation

#### Adding a New Report Type

1. Update `ReportType` enum in `source/config_models.py`
2. Add outline builder in `source/outline_planner.py`
3. Add tests
4. Update documentation

#### Adding a New Citation Style

1. Add formatter in `source/references/formatter.py`
2. Update `CitationStyle` enum
3. Add tests in `tests/test_references.py`
4. Update documentation

## Code Style

- Follow PEP 8
- Use type hints where possible
- Write docstrings for public functions/classes
- Keep functions focused and small
- Add tests for new features

## Documentation

- Update README.md for user-facing changes
- Update relevant guides in `docs/`
- Add examples in `examples/` for new features
- Update CHANGELOG.md

## Entry Points

### Official Entry Points
- **CLI**: `source/main.py` - Use this for command-line interface
- **API**: `source/api.py` - Use this for REST API

### Deprecated (Do Not Use)
- `source/main_v2.py` - Compatibility wrapper only
- `source/legacy_main.py` - Compatibility wrapper only

Always use the official entry points for new development.

## Questions?

- Check existing documentation in `docs/`
- Look at examples in `examples/`
- Review tests in `tests/` for usage patterns

## License

MIT License - See LICENSE file for details
