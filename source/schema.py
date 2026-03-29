"""
Professional Report Input Schema
Pydantic models for type-safe report generation
"""

from typing import List, Optional, Dict, Any, Literal
from pydantic import BaseModel, Field, HttpUrl, validator
from datetime import date
from enum import Enum


# ============================================================================
# ENUMS - Định nghĩa các giá trị cố định
# ============================================================================

class ReportType(str, Enum):
    """Loại báo cáo"""
    THESIS = "thesis"                    # Luận văn
    TECHNICAL_REPORT = "technical_report"  # Báo cáo kỹ thuật
    BUSINESS_REPORT = "business_report"    # Báo cáo kinh doanh
    PROJECT_REPORT = "project_report"      # Báo cáo đồ án


class AudienceType(str, Enum):
    """Đối tượng đọc"""
    LECTURER = "lecturer"        # Giảng viên
    MANAGER = "manager"          # Quản lý
    CLIENT = "client"            # Khách hàng
    INTERNAL_TEAM = "internal_team"  # Nội bộ
    PUBLIC = "public"            # Công chúng


class Language(str, Enum):
    """Ngôn ngữ"""
    VI = "vi"  # Tiếng Việt
    EN = "en"  # English


class ToneStyle(str, Enum):
    """Phong cách văn"""
    FORMAL = "formal"            # Trang trọng
    SEMI_FORMAL = "semi_formal"  # Bán trang trọng
    CASUAL = "casual"            # Thân mật
    TECHNICAL = "technical"      # Kỹ thuật


class CitationStyle(str, Enum):
    """Chuẩn trích dẫn"""
    APA = "APA"
    IEEE = "IEEE"
    MLA = "MLA"
    CHICAGO = "Chicago"
    HARVARD = "Harvard"


class HeadingStyle(str, Enum):
    """Kiểu đánh số heading"""
    NUMERIC = "1-1.1-1.1.1"           # 1, 1.1, 1.1.1
    ROMAN = "I-A-1"                   # I, A, 1
    MIXED = "Chapter 1-1.1-1.1.1"     # Chapter 1, 1.1, 1.1.1


# ============================================================================
# SUB-MODELS - Các model con
# ============================================================================

class Author(BaseModel):
    """Thông tin tác giả"""
    name: str = Field(..., description="Họ tên đầy đủ")
    student_id: Optional[str] = Field(None, description="Mã số sinh viên/nhân viên")
    email: Optional[str] = Field(None, description="Email liên hệ")
    role: Optional[str] = Field(None, description="Vai trò (Leader, Member, ...)")
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Trần Dương Gia Bảo",
                "student_id": "2001240039",
                "email": "tranduonggiabao0501@gmail.com",
                "role": "Team Leader"
            }
        }


class ProjectInfo(BaseModel):
    """Thông tin dự án/đề tài"""
    title: str = Field(..., description="Tiêu đề chính")
    subtitle: Optional[str] = Field(None, description="Tiêu đề phụ")
    domain: str = Field(..., description="Lĩnh vực (AI, Web, Mobile, ...)")
    description: str = Field(..., description="Mô tả ngắn gọn về dự án")
    
    authors: List[Author] = Field(..., min_items=1, description="Danh sách tác giả")
    organization: str = Field(..., description="Tổ chức (trường, công ty)")
    department: Optional[str] = Field(None, description="Khoa/phòng ban")
    
    supervisor: Optional[str] = Field(None, description="Người hướng dẫn")
    supervisor_title: Optional[str] = Field(None, description="Chức danh (TS., PGS., ...)")
    
    start_date: Optional[date] = Field(None, description="Ngày bắt đầu")
    end_date: Optional[date] = Field(None, description="Ngày kết thúc")
    
    keywords: List[str] = Field(default_factory=list, description="Từ khóa")
    
    # Links
    github_repo: Optional[HttpUrl] = Field(None, description="Link GitHub")
    demo_url: Optional[HttpUrl] = Field(None, description="Link demo")
    documentation_url: Optional[HttpUrl] = Field(None, description="Link tài liệu")
    
    class Config:
        schema_extra = {
            "example": {
                "title": "Maze Duel - BO3 / Gemini_Game",
                "subtitle": "Ứng dụng thuật toán AI trong game mê cung đối kháng",
                "domain": "Artificial Intelligence",
                "description": "Game 2D multiplayer với AI sử dụng nhiều thuật toán",
                "authors": [{"name": "Trần Dương Gia Bảo", "student_id": "2001240039"}],
                "organization": "Đại học Công Thương TP. HCM",
                "department": "Khoa Công nghệ thông tin",
                "supervisor": "Trần Việt Hùng",
                "supervisor_title": "TS.",
                "keywords": ["AI", "Game", "Pathfinding", "CSP"]
            }
        }


class ReportProfile(BaseModel):
    """Đặc điểm báo cáo"""
    report_type: ReportType = Field(..., description="Loại báo cáo")
    audience: AudienceType = Field(..., description="Đối tượng đọc")
    language: Language = Field(Language.VI, description="Ngôn ngữ")
    tone: ToneStyle = Field(ToneStyle.FORMAL, description="Phong cách")
    
    target_length_pages: Optional[int] = Field(None, ge=1, description="Số trang mục tiêu")
    abstract_max_words: Optional[int] = Field(250, description="Số từ tối đa cho abstract")
    
    class Config:
        schema_extra = {
            "example": {
                "report_type": "project_report",
                "audience": "lecturer",
                "language": "vi",
                "tone": "formal",
                "target_length_pages": 50
            }
        }


class Section(BaseModel):
    """Định nghĩa một section"""
    id: str = Field(..., description="ID duy nhất")
    title: str = Field(..., description="Tiêu đề section")
    level: int = Field(..., ge=1, le=4, description="Cấp độ (1=Chapter, 2=Section, ...)")
    content: Optional[str] = Field(None, description="Nội dung có sẵn")
    auto_generate: bool = Field(True, description="Tự động sinh nội dung")
    subsections: List['Section'] = Field(default_factory=list, description="Các section con")
    
    class Config:
        schema_extra = {
            "example": {
                "id": "chapter_1",
                "title": "Tổng quan",
                "level": 1,
                "auto_generate": True,
                "subsections": [
                    {"id": "1.1", "title": "Giới thiệu", "level": 2}
                ]
            }
        }


Section.update_forward_refs()  # Cho phép self-reference


class ContentRequirements(BaseModel):
    """Yêu cầu nội dung"""
    must_have_sections: List[str] = Field(
        default_factory=list,
        description="Các section bắt buộc (introduction, methodology, ...)"
    )
    optional_sections: List[str] = Field(
        default_factory=list,
        description="Các section tùy chọn"
    )
    custom_outline: List[Section] = Field(
        default_factory=list,
        description="Outline tùy chỉnh chi tiết"
    )
    
    include_abstract: bool = Field(True, description="Có abstract không")
    include_acknowledgment: bool = Field(True, description="Có lời cảm ơn không")
    include_commitment: bool = Field(True, description="Có lời cam đoan không")
    
    class Config:
        schema_extra = {
            "example": {
                "must_have_sections": ["introduction", "methodology", "results", "conclusion"],
                "optional_sections": ["future_work", "appendix"],
                "include_abstract": True
            }
        }


class Algorithm(BaseModel):
    """Thông tin thuật toán"""
    name: str = Field(..., description="Tên thuật toán")
    category: str = Field(..., description="Loại (Search, Optimization, ...)")
    purpose: str = Field(..., description="Mục đích sử dụng")
    complexity: Optional[str] = Field(None, description="Độ phức tạp (O(n), O(n log n), ...)")
    implementation_language: Optional[str] = Field(None, description="Ngôn ngữ triển khai")
    
    class Config:
        schema_extra = {
            "example": {
                "name": "A*",
                "category": "Pathfinding",
                "purpose": "Tìm đường ngắn nhất với heuristic",
                "complexity": "O(E log V)"
            }
        }


class Dataset(BaseModel):
    """Thông tin dataset"""
    name: str = Field(..., description="Tên dataset")
    source: Optional[str] = Field(None, description="Nguồn")
    size: Optional[str] = Field(None, description="Kích thước (1000 samples, 10GB, ...)")
    description: Optional[str] = Field(None, description="Mô tả")
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Custom Maze Dataset",
                "source": "Generated",
                "size": "1000 mazes",
                "description": "Randomly generated mazes for testing"
            }
        }


class Experiment(BaseModel):
    """Thông tin thực nghiệm"""
    name: str = Field(..., description="Tên thực nghiệm")
    objective: str = Field(..., description="Mục tiêu")
    setup: Optional[str] = Field(None, description="Thiết lập")
    results_summary: Optional[str] = Field(None, description="Tóm tắt kết quả")
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Algorithm Benchmark",
                "objective": "So sánh hiệu năng 3 thuật toán",
                "setup": "100 test cases, Intel i7, 16GB RAM"
            }
        }


class Metric(BaseModel):
    """Thông tin metric"""
    name: str = Field(..., description="Tên metric")
    value: Optional[float] = Field(None, description="Giá trị")
    unit: Optional[str] = Field(None, description="Đơn vị (ms, %, MB, ...)")
    description: Optional[str] = Field(None, description="Mô tả")
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Average Response Time",
                "value": 32.5,
                "unit": "ms",
                "description": "Thời gian phản hồi trung bình"
            }
        }


class TechnicalData(BaseModel):
    """Dữ liệu kỹ thuật"""
    technologies: List[str] = Field(default_factory=list, description="Công nghệ sử dụng")
    algorithms: List[Algorithm] = Field(default_factory=list, description="Thuật toán")
    datasets: List[Dataset] = Field(default_factory=list, description="Datasets")
    experiments: List[Experiment] = Field(default_factory=list, description="Thực nghiệm")
    metrics: List[Metric] = Field(default_factory=list, description="Metrics")
    
    system_architecture: Optional[str] = Field(None, description="Mô tả kiến trúc hệ thống")
    
    class Config:
        schema_extra = {
            "example": {
                "technologies": ["HTML5", "JavaScript", "Canvas API", "MQTT"],
                "algorithms": [
                    {"name": "A*", "category": "Pathfinding", "purpose": "Tìm đường"}
                ],
                "metrics": [
                    {"name": "Response Time", "value": 32.5, "unit": "ms"}
                ]
            }
        }




class Chart(BaseModel):
    """Thông tin biểu đồ"""
    id: str = Field(..., description="ID duy nhất")
    title: str = Field(..., description="Tiêu đề biểu đồ")
    type: str = Field(..., description="Loại (bar, line, pie, scatter, ...)")
    data: Optional[Dict[str, Any]] = Field(None, description="Dữ liệu biểu đồ")
    data_file: Optional[str] = Field(None, description="Đường dẫn file dữ liệu")
    caption: Optional[str] = Field(None, description="Chú thích")
    position: Optional[str] = Field(None, description="Vị trí trong báo cáo (section_id)")
    
    class Config:
        schema_extra = {
            "example": {
                "id": "chart_1",
                "title": "So sánh hiệu năng thuật toán",
                "type": "bar",
                "data": {
                    "labels": ["DFS", "BFS", "A*"],
                    "values": [50, 80, 32]
                },
                "caption": "Thời gian chạy trung bình (ms)"
            }
        }


class Table(BaseModel):
    """Thông tin bảng"""
    id: str = Field(..., description="ID duy nhất")
    title: str = Field(..., description="Tiêu đề bảng")
    headers: List[str] = Field(..., description="Tiêu đề cột")
    rows: List[List[Any]] = Field(..., description="Dữ liệu hàng")
    caption: Optional[str] = Field(None, description="Chú thích")
    position: Optional[str] = Field(None, description="Vị trí trong báo cáo")
    
    class Config:
        schema_extra = {
            "example": {
                "id": "table_1",
                "title": "Kết quả benchmark",
                "headers": ["Algorithm", "Time (ms)", "Memory (MB)"],
                "rows": [
                    ["DFS", 50, 12],
                    ["BFS", 80, 15],
                    ["A*", 32, 18]
                ],
                "caption": "Kết quả đo trên 100 test cases"
            }
        }


class Figure(BaseModel):
    """Thông tin hình ảnh"""
    id: str = Field(..., description="ID duy nhất")
    title: str = Field(..., description="Tiêu đề hình")
    file_path: str = Field(..., description="Đường dẫn file ảnh")
    caption: Optional[str] = Field(None, description="Chú thích")
    position: Optional[str] = Field(None, description="Vị trí trong báo cáo")
    width: Optional[float] = Field(None, description="Chiều rộng (inches)")
    
    class Config:
        schema_extra = {
            "example": {
                "id": "fig_1",
                "title": "Kiến trúc hệ thống",
                "file_path": "diagrams/architecture.png",
                "caption": "Sơ đồ kiến trúc tổng thể",
                "width": 6.0
            }
        }


class Reference(BaseModel):
    """Thông tin tài liệu tham khảo"""
    id: str = Field(..., description="ID trích dẫn ([1], [Smith2020], ...)")
    type: str = Field(..., description="Loại (book, journal, conference, website, ...)")
    authors: List[str] = Field(..., description="Tác giả")
    title: str = Field(..., description="Tiêu đề")
    year: int = Field(..., description="Năm xuất bản")
    
    # Optional fields tùy loại
    publisher: Optional[str] = Field(None, description="Nhà xuất bản")
    journal: Optional[str] = Field(None, description="Tên journal")
    conference: Optional[str] = Field(None, description="Tên conference")
    volume: Optional[str] = Field(None, description="Volume")
    pages: Optional[str] = Field(None, description="Trang (1-10)")
    doi: Optional[str] = Field(None, description="DOI")
    url: Optional[HttpUrl] = Field(None, description="URL")
    
    class Config:
        schema_extra = {
            "example": {
                "id": "Russell2020",
                "type": "book",
                "authors": ["Stuart Russell", "Peter Norvig"],
                "title": "Artificial Intelligence: A Modern Approach",
                "year": 2020,
                "publisher": "Pearson",
                "pages": "1-1136"
            }
        }


class Evidence(BaseModel):
    """Bằng chứng (biểu đồ, bảng, hình)"""
    charts: List[Chart] = Field(default_factory=list, description="Biểu đồ")
    tables: List[Table] = Field(default_factory=list, description="Bảng")
    figures: List[Figure] = Field(default_factory=list, description="Hình ảnh")
    references: List[Reference] = Field(default_factory=list, description="Tài liệu tham khảo")
    
    class Config:
        schema_extra = {
            "example": {
                "charts": [
                    {"id": "chart_1", "title": "Performance", "type": "bar"}
                ],
                "tables": [
                    {"id": "table_1", "title": "Results", "headers": ["A", "B"], "rows": [[1, 2]]}
                ],
                "figures": [
                    {"id": "fig_1", "title": "Architecture", "file_path": "arch.png"}
                ],
                "references": [
                    {"id": "1", "type": "book", "authors": ["Author"], "title": "Title", "year": 2020}
                ]
            }
        }


class FormatRules(BaseModel):
    """Quy tắc định dạng"""
    citation_style: CitationStyle = Field(CitationStyle.APA, description="Chuẩn trích dẫn")
    heading_style: HeadingStyle = Field(HeadingStyle.NUMERIC, description="Kiểu đánh số heading")
    
    # Page setup
    page_size: str = Field("A4", description="Khổ giấy (A4, Letter, ...)")
    margin_left_cm: float = Field(3.0, description="Lề trái (cm)")
    margin_right_cm: float = Field(2.0, description="Lề phải (cm)")
    margin_top_cm: float = Field(2.0, description="Lề trên (cm)")
    margin_bottom_cm: float = Field(2.0, description="Lề dưới (cm)")
    
    # Font
    font_name: str = Field("Times New Roman", description="Font chữ")
    font_size: int = Field(13, description="Cỡ chữ")
    line_spacing: float = Field(1.5, description="Giãn dòng")
    
    # Structure
    include_toc: bool = Field(True, description="Có mục lục không")
    include_list_of_figures: bool = Field(True, description="Có danh sách hình không")
    include_list_of_tables: bool = Field(True, description="Có danh sách bảng không")
    
    # Numbering
    number_figures: bool = Field(True, description="Đánh số hình")
    number_tables: bool = Field(True, description="Đánh số bảng")
    number_equations: bool = Field(True, description="Đánh số công thức")
    
    class Config:
        schema_extra = {
            "example": {
                "citation_style": "IEEE",
                "heading_style": "1-1.1-1.1.1",
                "font_name": "Times New Roman",
                "font_size": 13,
                "include_toc": True
            }
        }


class GenerationOptions(BaseModel):
    """Tùy chọn sinh báo cáo"""
    auto_generate_content: bool = Field(True, description="Tự động sinh nội dung")
    auto_generate_diagrams: bool = Field(True, description="Tự động tạo biểu đồ")
    
    output_format: List[str] = Field(
        default=["docx"],
        description="Format đầu ra (docx, pdf, html, markdown)"
    )
    output_filename: Optional[str] = Field(None, description="Tên file output")
    output_directory: str = Field("output", description="Thư mục output")
    
    # AI options
    use_ai_enhancement: bool = Field(False, description="Dùng AI cải thiện nội dung")
    ai_model: Optional[str] = Field(None, description="Model AI (gpt-4, claude, ...)")
    
    # Debug
    verbose: bool = Field(False, description="Hiển thị log chi tiết")
    save_intermediate: bool = Field(False, description="Lưu file trung gian")
    
    class Config:
        schema_extra = {
            "example": {
                "auto_generate_content": True,
                "output_format": ["docx", "pdf"],
                "output_filename": "Bao_Cao_Final",
                "verbose": True
            }
        }


# ============================================================================
# MAIN MODEL - Schema chính
# ============================================================================

class ReportInput(BaseModel):
    """
    Schema đầu vào hoàn chỉnh cho hệ thống sinh báo cáo
    
    Hỗ trợ:
    - Nhiều loại báo cáo (thesis, technical, business, project)
    - Tự động sinh nội dung hoặc custom
    - Biểu đồ, bảng, hình ảnh
    - Trích dẫn và tài liệu tham khảo
    - Quy tắc định dạng linh hoạt
    """
    
    # Required
    project_info: ProjectInfo = Field(..., description="Thông tin dự án")
    report_profile: ReportProfile = Field(..., description="Đặc điểm báo cáo")
    
    # Optional
    content_requirements: ContentRequirements = Field(
        default_factory=ContentRequirements,
        description="Yêu cầu nội dung"
    )
    technical_data: TechnicalData = Field(
        default_factory=TechnicalData,
        description="Dữ liệu kỹ thuật"
    )
    evidence: Evidence = Field(
        default_factory=Evidence,
        description="Bằng chứng (charts, tables, figures, references)"
    )
    format_rules: FormatRules = Field(
        default_factory=FormatRules,
        description="Quy tắc định dạng"
    )
    generation_options: GenerationOptions = Field(
        default_factory=GenerationOptions,
        description="Tùy chọn sinh báo cáo"
    )
    
    # Metadata
    schema_version: str = Field("1.0.0", description="Phiên bản schema")
    created_at: Optional[date] = Field(None, description="Ngày tạo")
    updated_at: Optional[date] = Field(None, description="Ngày cập nhật")
    
    class Config:
        schema_extra = {
            "example": {
                "project_info": {
                    "title": "Maze Duel Game",
                    "domain": "AI",
                    "description": "Game with AI algorithms",
                    "authors": [{"name": "John Doe", "student_id": "001"}],
                    "organization": "University"
                },
                "report_profile": {
                    "report_type": "project_report",
                    "audience": "lecturer",
                    "language": "vi"
                }
            }
        }
    
    @validator('created_at', 'updated_at', pre=True, always=True)
    def set_dates(cls, v):
        """Auto-set dates if not provided"""
        return v or date.today()


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def load_from_json(json_file: str) -> ReportInput:
    """Load schema from JSON file"""
    import json
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return ReportInput(**data)


def save_to_json(report_input: ReportInput, json_file: str):
    """Save schema to JSON file"""
    import json
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(report_input.dict(), f, indent=2, ensure_ascii=False, default=str)


def generate_template(report_type: ReportType) -> ReportInput:
    """Generate template for specific report type"""
    templates = {
        ReportType.THESIS: _thesis_template,
        ReportType.TECHNICAL_REPORT: _technical_template,
        ReportType.BUSINESS_REPORT: _business_template,
        ReportType.PROJECT_REPORT: _project_template,
    }
    return templates[report_type]()


def _project_template() -> ReportInput:
    """Template for project report"""
    return ReportInput(
        project_info=ProjectInfo(
            title="[Tên đề tài]",
            domain="[Lĩnh vực]",
            description="[Mô tả]",
            authors=[Author(name="[Tên sinh viên]", student_id="[MSSV]")],
            organization="[Tên trường]",
            supervisor="[Tên GV]"
        ),
        report_profile=ReportProfile(
            report_type=ReportType.PROJECT_REPORT,
            audience=AudienceType.LECTURER,
            language=Language.VI,
            target_length_pages=50
        ),
        content_requirements=ContentRequirements(
            must_have_sections=["introduction", "overview", "methodology", "implementation", "results", "conclusion"],
            include_abstract=True,
            include_acknowledgment=True
        )
    )


def _thesis_template() -> ReportInput:
    """Template for thesis"""
    return ReportInput(
        project_info=ProjectInfo(
            title="[Tên luận văn]",
            domain="[Lĩnh vực]",
            description="[Mô tả]",
            authors=[Author(name="[Tên học viên]")],
            organization="[Tên trường]",
            supervisor="[Tên GV]",
            supervisor_title="PGS.TS."
        ),
        report_profile=ReportProfile(
            report_type=ReportType.THESIS,
            audience=AudienceType.LECTURER,
            language=Language.VI,
            target_length_pages=100
        )
    )


def _technical_template() -> ReportInput:
    """Template for technical report"""
    return ReportInput(
        project_info=ProjectInfo(
            title="[Tên báo cáo kỹ thuật]",
            domain="[Lĩnh vực]",
            description="[Mô tả]",
            authors=[Author(name="[Tên tác giả]")],
            organization="[Tên công ty]"
        ),
        report_profile=ReportProfile(
            report_type=ReportType.TECHNICAL_REPORT,
            audience=AudienceType.INTERNAL_TEAM,
            language=Language.EN,
            tone=ToneStyle.TECHNICAL
        )
    )


def _business_template() -> ReportInput:
    """Template for business report"""
    return ReportInput(
        project_info=ProjectInfo(
            title="[Tên báo cáo kinh doanh]",
            domain="Business",
            description="[Mô tả]",
            authors=[Author(name="[Tên tác giả]", role="Analyst")],
            organization="[Tên công ty]"
        ),
        report_profile=ReportProfile(
            report_type=ReportType.BUSINESS_REPORT,
            audience=AudienceType.MANAGER,
            language=Language.VI,
            tone=ToneStyle.SEMI_FORMAL
        )
    )


# ============================================================================
# VALIDATION HELPERS
# ============================================================================

def validate_report_input(data: dict) -> tuple[bool, list[str]]:
    """
    Validate report input data
    Returns: (is_valid, error_messages)
    """
    try:
        ReportInput(**data)
        return True, []
    except Exception as e:
        return False, [str(e)]


if __name__ == "__main__":
    # Example usage
    print("=" * 60)
    print("REPORT INPUT SCHEMA - Example Usage")
    print("=" * 60)
    
    # Generate template
    template = generate_template(ReportType.PROJECT_REPORT)
    print("\n1. Generated template:")
    print(f"   Title: {template.project_info.title}")
    print(f"   Type: {template.report_profile.report_type}")
    
    # Save to JSON
    save_to_json(template, "template_project.json")
    print("\n2. Saved to: template_project.json")
    
    # Load from JSON
    loaded = load_from_json("template_project.json")
    print(f"\n3. Loaded from JSON: {loaded.project_info.title}")
    
    print("\n✅ Schema is ready to use!")
