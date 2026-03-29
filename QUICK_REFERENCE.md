# Quick Reference - Report Generator

## Installation

```bash
pip install -r requirements_pro.txt
```

## Basic Usage

```bash
# Generate report with default config
python source/main.py

# Use custom config
python source/main.py --config my_config.json

# Specify output path
python source/main.py --output reports/my_report.docx

# Quiet mode (for scripts)
python source/main.py --quiet
```

## Configuration

### Legacy Format (Flat)

```json
{
  "title": "Project Title",
  "description": "Description",
  "students": [{"name": "Student Name", "id": "001"}],
  "university": "University Name",
  "algorithms": ["DFS", "BFS", "A*"]
}
```

### New Format (Pydantic)

```json
{
  "project_info": {
    "title": "Project Title",
    "description": "Description",
    "students": [{"name": "Student Name"}],
    "university": "University Name"
  },
  "report_profile": {
    "report_type": "project_report",
    "language": "vi"
  },
  "technical_data": {
    "algorithms": ["DFS", "BFS", "A*"]
  }
}
```

## Migration

```bash
# Convert legacy config to new format
python migrate_config.py report_config.json
```

## Pipeline Steps

1. 📖 **Load Config** - Load configuration file
2. ✔️ **Validate Config** - Validate with Pydantic
3. 📋 **Plan Outline** - Create report structure
4. ✍️ **Generate Content** - Generate section content
5. 📊 **Bind Evidence** - Attach diagrams
6. 📄 **Render Output** - Create DOCX file
7. 🔍 **Review Output** - Validate output

## Programmatic Usage

```python
from orchestrator import ReportOrchestrator

# Create and execute
orchestrator = ReportOrchestrator('config.json')
success = orchestrator.execute('output.docx')

# Access results
report = orchestrator.get_report()
config = orchestrator.get_config()
```

## Examples

```bash
# Example configs
python source/main.py --config examples/config_minimal.json
python source/main.py --config examples/config_full.json

# Batch processing
for config in configs/*.json; do
    python source/main.py --config "$config" --output "output/$(basename $config .json).docx"
done
```

## Troubleshooting

| Error | Solution |
|-------|----------|
| Config not found | Check file path |
| Validation failed | Check required fields |
| Permission denied | Close output file |
| Output too small | Check earlier steps |

## Documentation

- `README.md` - Main documentation
- `ORCHESTRATOR_GUIDE.md` - Orchestrator architecture
- `INTEGRATION_GUIDE.md` - Pydantic integration
- `SKILLS_GUIDE.md` - AI skills usage
- `MIGRATION_GUIDE.md` - Pipeline migration

## Help

```bash
python source/main.py --help
```

## Version

```bash
python source/main.py --version
```
