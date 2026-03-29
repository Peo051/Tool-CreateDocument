# 📐 Schema Design Documentation

## 📚 Tài liệu

### 1. INPUT_SCHEMA_DESIGN.md
**Thiết kế schema input chuyên nghiệp**

Nội dung:
- Design principles
- Detailed schema documentation
- Example inputs (minimal, full, business)
- Usage examples (Python, CLI)
- Future extensibility notes
- Schema comparison
- Benefits và next steps

### 2. source/schema.py
**Implementation với Pydantic**

Nội dung:
- Enums (ReportType, AudienceType, Language, ...)
- Sub-models (Author, ProjectInfo, Algorithm, ...)
- Main model (ReportInput)
- Helper functions (load_from_json, save_to_json, generate_template)
- Validation helpers
- Template generators

### 3. examples/
**Example JSON files**

Files:
- `minimal_project_report.json` - Minimal input
- `full_project_report.json` - Full input với tất cả fields

## 🚀 Quick Start

### 1. Cài đặt dependencies

```bash
pip install pydantic
```

### 2. Sử dụng schema

```python
from source.schema import ReportInput, generate_template, save_to_json

# Generate template
report = generate_template(ReportType.PROJECT_REPORT)

# Customize
report.project_info.title = "My Project"
report.project_info.authors[0].name = "John Doe"

# Save
save_to_json(report, "my_config.json")
```

### 3. Load và validate

```python
from source.schema import load_from_json, validate_report_input

# Load
report = load_from_json("my_config.json")

# Validate
is_valid, errors = validate_report_input(report.dict())
if not is_valid:
    print("Errors:", errors)
```

## 📊 Schema Overview

```
ReportInput (Main)
├── project_info          # Thông tin dự án
│   ├── title, subtitle
│   ├── authors[]
│   ├── organization, supervisor
│   └── github_repo, demo_url
│
├── report_profile        # Đặc điểm báo cáo
│   ├── report_type (thesis|technical|business|project)
│   ├── audience (lecturer|manager|client|...)
│   ├── language (vi|en)
│   └── tone (formal|semi_formal|casual|technical)
│
├── content_requirements  # Yêu cầu nội dung
│   ├── must_have_sections[]
│   ├── optional_sections[]
│   ├── custom_outline[]
│   └── include_abstract, include_acknowledgment
│
├── technical_data        # Dữ liệu kỹ thuật
│   ├── technologies[]
│   ├── algorithms[]
│   ├── datasets[]
│   ├── experiments[]
│   └── metrics[]
│
├── evidence              # Bằng chứng
│   ├── charts[]
│   ├── tables[]
│   ├── figures[]
│   └── references[]
│
├── format_rules          # Quy tắc định dạng
│   ├── citation_style (APA|IEEE|MLA|...)
│   ├── heading_style
│   ├── font_name, font_size
│   ├── margins
│   └── include_toc, include_list_of_figures
│
└── generation_options    # Tùy chọn sinh
    ├── auto_generate_content
    ├── auto_generate_diagrams
    ├── output_format[] (docx|pdf|html|markdown)
    └── use_ai_enhancement
```

## 💡 Key Features

### 1. Type Safety
- Pydantic models với auto-validation
- Type hints đầy đủ
- Error messages rõ ràng

### 2. Flexibility
- Hỗ trợ 4+ loại báo cáo
- Optional fields cho customization
- Custom outline support

### 3. Extensibility
- Dễ thêm fields mới
- Dễ thêm report types mới
- Schema versioning support

### 4. User-Friendly
- Template generators
- Load/save JSON
- Rich documentation

## 📖 Examples

### Minimal Input

```json
{
  "project_info": {
    "title": "My Project",
    "domain": "AI",
    "description": "Description",
    "authors": [{"name": "John", "student_id": "001"}],
    "organization": "University"
  },
  "report_profile": {
    "report_type": "project_report",
    "audience": "lecturer",
    "language": "vi"
  }
}
```

### Full Input

Xem `examples/full_project_report.json`

## 🔧 Integration

### Với auto_report_pro_main.py

```python
from source.schema import load_from_json
from source.auto_report_pro_main import ProReportGenerator

# Load config
config = load_from_json("config.json")

# Generate report
generator = ProReportGenerator(config)
generator.generate_full_report()
```

### Với CLI

```bash
# Generate template
python source/schema.py --generate-template project_report > config.json

# Generate report
python source/auto_report_pro_main.py --input config.json
```

## 🎯 Next Steps

1. **Update auto_report_pro_main.py** để sử dụng schema mới
2. **Add more templates** cho các loại báo cáo khác
3. **Add validators** cho business logic
4. **Add tests** cho schema validation
5. **Add CLI** để generate templates dễ dàng
6. **Add AI integration** để enhance content

## 📚 Tài liệu liên quan

- [INPUT_SCHEMA_DESIGN.md](INPUT_SCHEMA_DESIGN.md) - Thiết kế chi tiết
- [source/schema.py](../../source/schema.py) - Implementation
- [examples/](../../examples/) - Example files

---

**Version**: 1.0.0  
**Status**: ✅ Ready for Implementation
