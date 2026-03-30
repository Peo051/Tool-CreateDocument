# Integration Guide: Pydantic Config Models

This guide explains how the new Pydantic-based configuration system integrates with the existing pipeline.

## Overview

The project now supports both legacy and new configuration formats:

- **Legacy Format**: Flat JSON structure (backward compatible)
- **New Format**: Nested Pydantic models with validation

## Key Features

✅ **Type Safety**: Pydantic models provide runtime type checking  
✅ **Validation**: Automatic validation of required fields and data types  
✅ **Backward Compatible**: Existing configs continue to work  
✅ **Auto-Migration**: Legacy configs are automatically converted  
✅ **Better Defaults**: Sensible defaults for optional fields  

## File Structure

```
source/
├── config_models.py       # New Pydantic models
├── main.py               # Updated pipeline entry point
└── pipeline/
    └── validator.py      # Updated validator with Pydantic integration

examples/
├── config_minimal.json   # Minimal new format example
├── config_full.json      # Full new format example
└── usage_example.py      # Usage examples

migrate_config.py         # Migration script
```

## Configuration Formats

### Legacy Format (Still Supported)

```json
{
  "title": "My Project",
  "description": "Project description",
  "students": [{"name": "Student Name", "id": "001"}],
  "university": "University Name",
  "algorithms": ["DFS", "BFS"],
  "technologies": ["Python"]
}
```

### New Format (Recommended)

```json
{
  "project_info": {
    "title": "My Project",
    "description": "Project description",
    "students": [{"name": "Student Name", "id": "001"}],
    "university": "University Name"
  },
  "report_profile": {
    "report_type": "project_report",
    "language": "vi"
  },
  "technical_data": {
    "algorithms": ["DFS", "BFS"],
    "technologies": ["Python"]
  }
}
```

## Usage

### 1. Using Existing Pipeline (Automatic)

The pipeline automatically detects and converts config formats:

```bash
# Works with legacy format
python source/main.py --config report_config.json

# Works with new format
python source/main.py --config examples/config_minimal.json
```

### 2. Migrating Legacy Config

Convert your existing config to the new format:

```bash
# Creates report_config.new.json
python migrate_config.py report_config.json

# Custom output path
python migrate_config.py old_config.json new_config.json
```

### 3. Creating Config Programmatically

```python
from config_models import ReportConfig, ProjectInfo, Author, ReportProfile

config = ReportConfig(
    project_info=ProjectInfo(
        title="My Project",
        description="A detailed description",
        students=[Author(name="Student Name", id="001")],
        university="University Name"
    ),
    report_profile=ReportProfile(
        report_type="project_report",
        language="vi"
    )
)

# Save to file
from config_models import save_config
save_config(config, "my_config.json")
```

### 4. Loading and Validating Config

```python
from config_models import load_config, validate_config

# Load from file
config = load_config("config.json")

# Validate dictionary
is_valid, errors = validate_config(config_dict)
if not is_valid:
    print(f"Validation errors: {errors}")
```

## Validation Rules

### Required Fields

- `project_info.title` (min 1 character)
- `project_info.description` (min 10 characters)
- `project_info.students` (at least 1 student)
- `project_info.university` OR `project_info.organization`
- `report_profile.report_type` (thesis|technical_report|project_report|business_report)

### Optional Fields with Defaults

- `report_profile.language` (default: "vi")
- `report_profile.target_pages` (optional)
- `format_rules.font_name` (default: "Times New Roman")
- `format_rules.font_size` (default: 13)
- `format_rules.line_spacing` (default: 1.5)

## Report Types

The system supports 4 report types:

1. **thesis**: Academic thesis
2. **technical_report**: Technical documentation
3. **project_report**: Project report (default for legacy "ttnt")
4. **business_report**: Business report

## Integration Details

### How It Works

1. **Input**: User provides config (legacy or new format)
2. **Validation**: `InputValidator` validates using Pydantic
3. **Normalization**: Config is normalized to flat legacy format
4. **Pipeline**: Existing pipeline stages work unchanged
5. **Output**: DOCX report is generated

### Backward Compatibility

The `InputValidator` provides a compatibility layer:

```python
# Validates both formats
is_valid, errors = validator.validate(config_dict)

# Normalizes to flat format for existing pipeline
normalized = validator.normalize(config_dict)

# Loads as Pydantic model for type safety
model = validator.load_config(config_dict)
```

## Examples

See `examples/usage_example.py` for comprehensive examples:

```bash
cd examples
python usage_example.py
```

Examples include:
- Creating config programmatically
- Loading from JSON file
- Validation
- Legacy conversion
- Saving config
- Accessing nested fields
- Error handling

## Migration Checklist

If you want to migrate to the new format:

- [ ] Run migration script: `python migrate_config.py report_config.json`
- [ ] Review generated `report_config.new.json`
- [ ] Test with pipeline: `python source/main.py --config report_config.new.json`
- [ ] Update your config creation scripts to use new format
- [ ] Optionally replace old config with new one

## Benefits of New Format

1. **Type Safety**: Catch errors at config load time, not runtime
2. **Better Validation**: Comprehensive validation rules
3. **Documentation**: Self-documenting with field descriptions
4. **IDE Support**: Better autocomplete and type hints
5. **Extensibility**: Easy to add new fields and validation rules
6. **Maintainability**: Cleaner separation of concerns

## Troubleshooting

### Validation Errors

If you get validation errors, check:

1. Required fields are present
2. Field types match (string, list, etc.)
3. String fields meet minimum length requirements
4. Report type is one of the 4 valid types

### Migration Issues

If migration fails:

1. Check that legacy config has required fields
2. Ensure JSON is valid
3. Check for special characters in strings
4. Verify student list is not empty

### Pipeline Errors

If pipeline fails after migration:

1. Verify config loads: `python -c "from config_models import load_config; load_config('config.json')"`
2. Check validation: `python examples/usage_example.py`
3. Test with minimal config first: `python source/main.py --config examples/config_minimal.json`

## Future Enhancements

Planned improvements:

- [ ] Support for custom validation rules
- [ ] Config templates for different report types
- [ ] Interactive config builder CLI
- [ ] Config diff and merge tools
- [ ] Schema versioning and auto-upgrade

## Support

For issues or questions:

1. Check examples: `examples/usage_example.py`
2. Review this guide
3. Check validation errors carefully
4. Test with minimal config first
