# 🏗️ Input Schema Design - Professional Report Generator

> Thiết kế schema input chuyên nghiệp, có khả năng mở rộng cao

## 📋 Design Principles

### 1. Separation of Concerns
- **Metadata**: Thông tin dự án, tác giả
- **Content**: Nội dung, cấu trúc báo cáo
- **Technical**: Dữ liệu kỹ thuật, thuật toán
- **Evidence**: Biểu đồ, bảng, hình ảnh
- **Format**: Quy tắc định dạng

### 2. Flexibility
- Hỗ trợ nhiều loại báo cáo (thesis, technical, business, project)
- Optional fields cho các trường hợp đặc biệt
- Custom sections cho nhu cầu riêng

### 3. Extensibility
- Dễ thêm field mới
- Dễ thêm loại báo cáo mới
- Backward compatible

### 4. Validation
- Type checking với Pydantic
- Required vs Optional rõ ràng
- Default values hợp lý

### 5. User-Friendly
- Tên field dễ hiểu
- Documentation đầy đủ
- Examples cụ thể

## 🎯 Proposed Schema

### Schema Overview

```
ReportInput
├── project_info          # Thông tin dự án
├── report_profile        # Loại và đặc điểm báo cáo
├── content_requirements  # Yêu cầu nội dung
├── technical_data        # Dữ liệu kỹ thuật
├── evidence              # Bằng chứng (charts, tables, figures)
├── format_rules          # Quy tắc định dạng
└── generation_options    # Tùy chọn sinh báo cáo
```



## 📝 Detailed Schema Documentation

### 1. ProjectInfo
**Mục đích**: Thông tin cơ bản về dự án/đề tài

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| title | str | ✅ | Tiêu đề chính | "Maze Duel Game" |
| subtitle | str | ❌ | Tiêu đề phụ | "AI-powered multiplayer game" |
| domain | str | ✅ | Lĩnh vực | "Artificial Intelligence" |
| description | str | ✅ | Mô tả ngắn | "Game with pathfinding algorithms" |
| authors | List[Author] | ✅ | Danh sách tác giả | [{"name": "John", "id": "001"}] |
| organization | str | ✅ | Tổ chức | "MIT University" |
| supervisor | str | ❌ | Người hướng dẫn | "Dr. Smith" |
| keywords | List[str] | ❌ | Từ khóa | ["AI", "Game", "Pathfinding"] |
| github_repo | HttpUrl | ❌ | Link GitHub | "https://github.com/user/repo" |

### 2. ReportProfile
**Mục đích**: Đặc điểm và yêu cầu của báo cáo

| Field | Type | Required | Description | Values |
|-------|------|----------|-------------|--------|
| report_type | ReportType | ✅ | Loại báo cáo | thesis, technical_report, business_report, project_report |
| audience | AudienceType | ✅ | Đối tượng đọc | lecturer, manager, client, internal_team, public |
| language | Language | ✅ | Ngôn ngữ | vi, en |
| tone | ToneStyle | ✅ | Phong cách | formal, semi_formal, casual, technical |
| target_length_pages | int | ❌ | Số trang mục tiêu | 50 |

### 3. ContentRequirements
**Mục đích**: Yêu cầu về nội dung và cấu trúc

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| must_have_sections | List[str] | ❌ | Sections bắt buộc |
| optional_sections | List[str] | ❌ | Sections tùy chọn |
| custom_outline | List[Section] | ❌ | Outline chi tiết tùy chỉnh |
| include_abstract | bool | ❌ | Có abstract không (default: True) |
| include_acknowledgment | bool | ❌ | Có lời cảm ơn không (default: True) |

**Standard sections**:
- `introduction` - Giới thiệu
- `overview` - Tổng quan
- `literature_review` - Tổng quan tài liệu
- `methodology` - Phương pháp
- `implementation` - Triển khai
- `results` - Kết quả
- `discussion` - Thảo luận
- `conclusion` - Kết luận
- `future_work` - Hướng phát triển
- `appendix` - Phụ lục

### 4. TechnicalData
**Mục đích**: Dữ liệu kỹ thuật (thuật toán, công nghệ, metrics)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| technologies | List[str] | ❌ | Công nghệ sử dụng |
| algorithms | List[Algorithm] | ❌ | Thuật toán |
| datasets | List[Dataset] | ❌ | Datasets |
| experiments | List[Experiment] | ❌ | Thực nghiệm |
| metrics | List[Metric] | ❌ | Metrics đo lường |
| system_architecture | str | ❌ | Mô tả kiến trúc |

### 5. Evidence
**Mục đích**: Bằng chứng (biểu đồ, bảng, hình, tài liệu)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| charts | List[Chart] | ❌ | Biểu đồ |
| tables | List[Table] | ❌ | Bảng |
| figures | List[Figure] | ❌ | Hình ảnh |
| references | List[Reference] | ❌ | Tài liệu tham khảo |

### 6. FormatRules
**Mục đích**: Quy tắc định dạng văn bản

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| citation_style | CitationStyle | ❌ | APA | Chuẩn trích dẫn |
| heading_style | HeadingStyle | ❌ | 1-1.1-1.1.1 | Kiểu đánh số |
| font_name | str | ❌ | Times New Roman | Font chữ |
| font_size | int | ❌ | 13 | Cỡ chữ |
| line_spacing | float | ❌ | 1.5 | Giãn dòng |
| include_toc | bool | ❌ | True | Có mục lục không |

### 7. GenerationOptions
**Mục đích**: Tùy chọn sinh báo cáo

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| auto_generate_content | bool | ❌ | True | Tự động sinh nội dung |
| auto_generate_diagrams | bool | ❌ | True | Tự động tạo biểu đồ |
| output_format | List[str] | ❌ | ["docx"] | Format đầu ra |
| output_filename | str | ❌ | None | Tên file output |
| use_ai_enhancement | bool | ❌ | False | Dùng AI cải thiện |

## 💡 Example Inputs

### Example 1: Minimal Input (Project Report)

```json
{
  "project_info": {
    "title": "Maze Duel - AI Game",
    "domain": "Artificial Intelligence",
    "description": "Multiplayer game with AI algorithms",
    "authors": [
      {
        "name": "Trần Dương Gia Bảo",
        "student_id": "2001240039"
      }
    ],
    "organization": "Đại học Công Thương TP. HCM",
    "supervisor": "TS. Trần Việt Hùng"
  },
  "report_profile": {
    "report_type": "project_report",
    "audience": "lecturer",
    "language": "vi",
    "tone": "formal"
  }
}
```

### Example 2: Full Input (Technical Report)

```json
{
  "project_info": {
    "title": "Maze Duel - BO3 / Gemini_Game",
    "subtitle": "Ứng dụng thuật toán AI trong game mê cung đối kháng",
    "domain": "Artificial Intelligence",
    "description": "Game 2D multiplayer với AI sử dụng nhiều thuật toán tìm kiếm và CSP",
    "authors": [
      {
        "name": "Trần Dương Gia Bảo",
        "student_id": "2001240039",
        "email": "bao@example.com",
        "role": "Team Leader"
      },
      {
        "name": "Nguyễn Thế Anh",
        "student_id": "2001240015",
        "role": "Developer"
      }
    ],
    "organization": "Đại học Công Thương TP. HCM",
    "department": "Khoa Công nghệ thông tin",
    "supervisor": "Trần Việt Hùng",
    "supervisor_title": "TS.",
    "keywords": ["AI", "Game", "Pathfinding", "CSP", "Multiplayer"],
    "github_repo": "https://github.com/GiaBao051/Gemini_Game",
    "demo_url": "https://giabao051.github.io/Gemini_Game/"
  },
  
  "report_profile": {
    "report_type": "project_report",
    "audience": "lecturer",
    "language": "vi",
    "tone": "formal",
    "target_length_pages": 60
  },
  
  "content_requirements": {
    "must_have_sections": [
      "introduction",
      "overview",
      "methodology",
      "implementation",
      "results",
      "conclusion"
    ],
    "optional_sections": ["future_work", "appendix"],
    "include_abstract": true,
    "include_acknowledgment": true,
    "include_commitment": true
  },
  
  "technical_data": {
    "technologies": [
      "HTML5",
      "JavaScript",
      "Canvas API",
      "MQTT",
      "WebSocket"
    ],
    "algorithms": [
      {
        "name": "DFS",
        "category": "Graph Traversal",
        "purpose": "Sinh mê cung procedural",
        "complexity": "O(V + E)"
      },
      {
        "name": "BFS",
        "category": "Pathfinding",
        "purpose": "Distance map và fairness check",
        "complexity": "O(V + E)"
      },
      {
        "name": "A*",
        "category": "Pathfinding",
        "purpose": "Tìm đường tối ưu với heuristic",
        "complexity": "O(E log V)"
      },
      {
        "name": "Dijkstra",
        "category": "Pathfinding",
        "purpose": "Đường đi an toàn theo chi phí",
        "complexity": "O(E log V)"
      },
      {
        "name": "CSP",
        "category": "Constraint Satisfaction",
        "purpose": "Đặt nội dung bản đồ theo ràng buộc",
        "complexity": "O(d^n)"
      }
    ],
    "metrics": [
      {
        "name": "Average Response Time",
        "value": 32.5,
        "unit": "ms",
        "description": "Thời gian phản hồi trung bình của A*"
      },
      {
        "name": "Map Generation Time",
        "value": 50,
        "unit": "ms",
        "description": "Thời gian sinh mê cung bằng DFS"
      }
    ]
  },
  
  "evidence": {
    "charts": [
      {
        "id": "chart_performance",
        "title": "So sánh hiệu năng thuật toán",
        "type": "bar",
        "data": {
          "labels": ["DFS", "BFS", "A*", "Dijkstra"],
          "values": [50, 80, 32, 45]
        },
        "caption": "Thời gian chạy trung bình (ms) trên 100 test cases",
        "position": "results"
      }
    ],
    "tables": [
      {
        "id": "table_comparison",
        "title": "Bảng so sánh thuật toán",
        "headers": ["Algorithm", "Time (ms)", "Memory (MB)", "Optimal"],
        "rows": [
          ["DFS", 50, 12, "No"],
          ["BFS", 80, 15, "Yes"],
          ["A*", 32, 18, "Yes"],
          ["Dijkstra", 45, 20, "Yes"]
        ],
        "caption": "Kết quả benchmark trên Intel i7, 16GB RAM"
      }
    ],
    "figures": [
      {
        "id": "fig_architecture",
        "title": "Kiến trúc hệ thống",
        "file_path": "diagrams/architecture.png",
        "caption": "Sơ đồ kiến trúc tổng thể của Maze Duel",
        "width": 6.0
      }
    ],
    "references": [
      {
        "id": "Russell2020",
        "type": "book",
        "authors": ["Stuart Russell", "Peter Norvig"],
        "title": "Artificial Intelligence: A Modern Approach",
        "year": 2020,
        "publisher": "Pearson",
        "pages": "1-1136"
      },
      {
        "id": "Cormen2009",
        "type": "book",
        "authors": ["Thomas H. Cormen", "Charles E. Leiserson"],
        "title": "Introduction to Algorithms",
        "year": 2009,
        "publisher": "MIT Press"
      }
    ]
  },
  
  "format_rules": {
    "citation_style": "IEEE",
    "heading_style": "1-1.1-1.1.1",
    "font_name": "Times New Roman",
    "font_size": 13,
    "line_spacing": 1.5,
    "margin_left_cm": 3.0,
    "margin_right_cm": 2.0,
    "include_toc": true,
    "include_list_of_figures": true,
    "include_list_of_tables": true
  },
  
  "generation_options": {
    "auto_generate_content": true,
    "auto_generate_diagrams": true,
    "output_format": ["docx", "pdf"],
    "output_filename": "Bao_Cao_Do_An_TTNT",
    "output_directory": "output",
    "verbose": true
  }
}
```

### Example 3: Business Report

```json
{
  "project_info": {
    "title": "Q4 2024 Performance Analysis",
    "domain": "Business Analytics",
    "description": "Quarterly performance report with KPI analysis",
    "authors": [
      {
        "name": "Jane Smith",
        "role": "Business Analyst",
        "email": "jane@company.com"
      }
    ],
    "organization": "Tech Corp Inc."
  },
  
  "report_profile": {
    "report_type": "business_report",
    "audience": "manager",
    "language": "en",
    "tone": "semi_formal",
    "target_length_pages": 20
  },
  
  "evidence": {
    "charts": [
      {
        "id": "revenue_chart",
        "title": "Revenue Growth",
        "type": "line",
        "data": {
          "labels": ["Q1", "Q2", "Q3", "Q4"],
          "values": [100, 120, 150, 180]
        }
      }
    ]
  },
  
  "format_rules": {
    "citation_style": "APA",
    "font_name": "Arial",
    "font_size": 11,
    "include_toc": false
  }
}
```

## 🔧 Usage Examples

### Python Usage

```python
from source.schema import ReportInput, generate_template, save_to_json, load_from_json

# Method 1: Generate from template
report = generate_template(ReportType.PROJECT_REPORT)
report.project_info.title = "My Project"
report.project_info.authors[0].name = "John Doe"

# Method 2: Create from scratch
report = ReportInput(
    project_info=ProjectInfo(
        title="My Project",
        domain="AI",
        description="Description",
        authors=[Author(name="John", student_id="001")],
        organization="University"
    ),
    report_profile=ReportProfile(
        report_type=ReportType.PROJECT_REPORT,
        audience=AudienceType.LECTURER,
        language=Language.VI
    )
)

# Method 3: Load from JSON
report = load_from_json("my_report_config.json")

# Save to JSON
save_to_json(report, "output_config.json")

# Validate
is_valid, errors = validate_report_input(report.dict())
if not is_valid:
    print("Errors:", errors)
```

### CLI Usage

```bash
# Generate template
python source/schema.py --generate-template project_report > config.json

# Validate input
python source/schema.py --validate config.json

# Generate report
python source/auto_report_pro_main.py --input config.json
```

## 🚀 Notes for Future Extensibility

### 1. Adding New Report Types

```python
# In schema.py
class ReportType(str, Enum):
    THESIS = "thesis"
    # ... existing types
    RESEARCH_PAPER = "research_paper"  # NEW

# Add template
def _research_paper_template() -> ReportInput:
    return ReportInput(...)
```

### 2. Adding New Fields

```python
# Add to existing model
class ProjectInfo(BaseModel):
    # ... existing fields
    funding_source: Optional[str] = Field(None, description="Nguồn tài trợ")  # NEW
```

### 3. Adding New Evidence Types

```python
# Add new evidence type
class Video(BaseModel):
    id: str
    title: str
    file_path: str
    duration: Optional[int] = None

class Evidence(BaseModel):
    # ... existing fields
    videos: List[Video] = Field(default_factory=list)  # NEW
```

### 4. Adding AI Integration

```python
class AIConfig(BaseModel):
    provider: str = Field("openai", description="AI provider")
    model: str = Field("gpt-4", description="Model name")
    api_key: Optional[str] = Field(None, description="API key")
    temperature: float = Field(0.7, description="Temperature")

class GenerationOptions(BaseModel):
    # ... existing fields
    ai_config: Optional[AIConfig] = None  # NEW
```

### 5. Adding Localization

```python
class LocalizationConfig(BaseModel):
    language: Language
    date_format: str = Field("%d/%m/%Y", description="Date format")
    number_format: str = Field("1.234,56", description="Number format")
    currency: str = Field("VND", description="Currency")

class ReportInput(BaseModel):
    # ... existing fields
    localization: LocalizationConfig = Field(default_factory=LocalizationConfig)  # NEW
```

### 6. Versioning Strategy

```python
# Schema versioning
class ReportInput(BaseModel):
    schema_version: str = Field("1.0.0")
    
    @validator('schema_version')
    def check_version(cls, v):
        major, minor, patch = map(int, v.split('.'))
        if major > 1:
            raise ValueError("Unsupported schema version")
        return v
```

### 7. Migration Support

```python
def migrate_schema(old_data: dict, from_version: str, to_version: str) -> dict:
    """Migrate schema from old version to new version"""
    migrations = {
        ("1.0.0", "1.1.0"): _migrate_1_0_to_1_1,
        ("1.1.0", "2.0.0"): _migrate_1_1_to_2_0,
    }
    
    migration_func = migrations.get((from_version, to_version))
    if migration_func:
        return migration_func(old_data)
    return old_data
```

## 📊 Schema Comparison

| Feature | Old Schema | New Schema |
|---------|-----------|------------|
| Fields | 10 | 50+ |
| Nested levels | 1 | 3-4 |
| Type safety | ❌ | ✅ Pydantic |
| Validation | ❌ | ✅ Auto |
| Documentation | ❌ | ✅ Full |
| Examples | ❌ | ✅ Multiple |
| Extensibility | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Report types | 1 | 4+ |
| Evidence support | ❌ | ✅ Charts, Tables, Figures |
| Format rules | Basic | Advanced |

## ✅ Benefits

1. **Type Safety**: Pydantic validation tự động
2. **Documentation**: Mỗi field có description và example
3. **Flexibility**: Hỗ trợ nhiều loại báo cáo
4. **Extensibility**: Dễ thêm field/model mới
5. **User-Friendly**: Template generators
6. **Validation**: Auto-validation với error messages
7. **JSON Support**: Load/save từ JSON
8. **Backward Compatible**: Schema versioning

## 🎯 Next Steps

1. **Implement Generator**: Cập nhật `auto_report_pro_main.py` để sử dụng schema mới
2. **Add Templates**: Tạo thêm templates cho các loại báo cáo
3. **Add Validators**: Thêm custom validators cho business logic
4. **Add Tests**: Unit tests cho schema validation
5. **Add CLI**: Command-line interface để generate templates
6. **Add Documentation**: API documentation với Swagger/OpenAPI
7. **Add Examples**: Thêm nhiều examples thực tế

---

**Version**: 1.0.0  
**Last Updated**: 2025-01-XX  
**Status**: ✅ Ready for Implementation
