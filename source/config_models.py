"""
Robust Input Schema for Professional Report Generator
Production-ready Pydantic models with validation
"""

from typing import List, Optional, Dict, Any, Literal
from pydantic import BaseModel, Field, HttpUrl, field_validator, model_validator
from datetime import date


# ============================================================================
# PROJECT INFO
# ============================================================================

class Author(BaseModel):
    """Author/Student information"""
    name: str = Field(..., min_length=1, description="Full name")
    id: Optional[str] = Field(None, description="Student/Employee ID")
    email: Optional[str] = Field(None, description="Email address")
    role: Optional[str] = Field(None, description="Role (Leader, Member, etc.)")
    
    model_config = {"extra": "forbid"}


class ProjectInfo(BaseModel):
    """Project metadata"""
    title: str = Field(..., min_length=1, description="Project title")
    subtitle: Optional[str] = Field(None, description="Project subtitle")
    description: str = Field(..., min_length=10, description="Project description")
    
    # Authors
    students: List[Author] = Field(..., min_length=1, description="List of authors/students")
    advisor: Optional[str] = Field(None, description="Advisor name")
    
    # Organization
    university: Optional[str] = Field(None, description="University name")
    organization: Optional[str] = Field(None, description="Organization name")
    faculty: Optional[str] = Field(None, description="Faculty/Department")
    class_name: Optional[str] = Field(None, alias="class", description="Class name")
    
    # Links
    github_repo: Optional[HttpUrl] = Field(None, description="GitHub repository URL")
    demo_url: Optional[HttpUrl] = Field(None, description="Demo URL")
    
    # Keywords
    keywords: List[str] = Field(default_factory=list, description="Project keywords")
    
    @model_validator(mode='after')
    def check_organization(self):
        """At least one of university or organization must be provided"""
        if not self.university and not self.organization:
            raise ValueError("Either 'university' or 'organization' must be provided")
        return self
    
    model_config = {"extra": "forbid", "populate_by_name": True}


# ============================================================================
# REPORT PROFILE
# ============================================================================

class ReportProfile(BaseModel):
    """Report characteristics"""
    report_type: Literal["thesis", "technical_report", "project_report", "business_report"] = Field(
        ..., description="Type of report"
    )
    language: Literal["vi", "en"] = Field(default="vi", description="Report language")
    target_pages: Optional[int] = Field(None, ge=1, description="Target page count")
    
    model_config = {"extra": "forbid"}


# ============================================================================
# CONTENT REQUIREMENTS
# ============================================================================

class ContentRequirements(BaseModel):
    """Content structure requirements"""
    include_cover: bool = Field(default=True, description="Include cover page")
    include_acknowledgment: bool = Field(default=True, description="Include acknowledgment")
    include_commitment: bool = Field(default=True, description="Include commitment")
    include_toc: bool = Field(default=True, description="Include table of contents")
    include_references: bool = Field(default=True, description="Include references")
    
    custom_sections: List[str] = Field(default_factory=list, description="Custom section titles")
    
    model_config = {"extra": "forbid"}


# ============================================================================
# TECHNICAL DATA
# ============================================================================

class Algorithm(BaseModel):
    """Algorithm information"""
    name: str = Field(..., min_length=1, description="Algorithm name")
    category: Optional[str] = Field(None, description="Algorithm category")
    complexity: Optional[str] = Field(None, description="Time/space complexity")
    
    model_config = {"extra": "forbid"}


class TechnicalData(BaseModel):
    """Technical project data"""
    algorithms: List[str] = Field(default_factory=list, description="Algorithm names")
    technologies: List[str] = Field(default_factory=list, description="Technologies used")
    datasets: List[str] = Field(default_factory=list, description="Datasets used")
    
    # Detailed algorithm info (optional)
    algorithm_details: List[Algorithm] = Field(default_factory=list, description="Detailed algorithm info")
    
    model_config = {"extra": "forbid"}


# ============================================================================
# EVIDENCE
# ============================================================================

class Chart(BaseModel):
    """Chart/diagram information"""
    id: str = Field(..., min_length=1, description="Unique chart ID")
    title: str = Field(..., min_length=1, description="Chart title")
    type: Literal["bar", "line", "pie", "scatter"] = Field(default="bar", description="Chart type")
    data: Optional[Dict[str, Any]] = Field(None, description="Chart data")
    
    model_config = {"extra": "forbid"}


class Table(BaseModel):
    """Table information"""
    id: str = Field(..., min_length=1, description="Unique table ID")
    title: str = Field(..., min_length=1, description="Table title")
    headers: List[str] = Field(..., min_length=1, description="Column headers")
    rows: List[List[Any]] = Field(..., min_length=1, description="Table rows")
    
    model_config = {"extra": "forbid"}


class Figure(BaseModel):
    """Figure/image information"""
    id: str = Field(..., min_length=1, description="Unique figure ID")
    title: str = Field(..., min_length=1, description="Figure title")
    path: str = Field(..., min_length=1, description="File path")
    caption: Optional[str] = Field(None, description="Figure caption")
    
    model_config = {"extra": "forbid"}


class Reference(BaseModel):
    """Reference information"""
    id: str = Field(..., min_length=1, description="Reference ID")
    authors: List[str] = Field(..., min_length=1, description="Author names")
    title: str = Field(..., min_length=1, description="Reference title")
    year: int = Field(..., ge=1900, le=2100, description="Publication year")
    source: Optional[str] = Field(None, description="Source (journal, conference, etc.)")
    url: Optional[HttpUrl] = Field(None, description="URL")
    
    model_config = {"extra": "forbid"}


class Evidence(BaseModel):
    """Evidence collection"""
    charts: List[Chart] = Field(default_factory=list, description="Charts")
    tables: List[Table] = Field(default_factory=list, description="Tables")
    figures: List[Figure] = Field(default_factory=list, description="Figures")
    references: List[Reference] = Field(default_factory=list, description="References")
    
    model_config = {"extra": "forbid"}


# ============================================================================
# FORMAT RULES
# ============================================================================

class FormatRules(BaseModel):
    """Document formatting rules"""
    citation_style: Literal["APA", "IEEE", "MLA", "Chicago"] = Field(
        default="IEEE", description="Citation style"
    )
    font_name: str = Field(default="Times New Roman", description="Font name")
    font_size: int = Field(default=13, ge=8, le=20, description="Font size")
    line_spacing: float = Field(default=1.5, ge=1.0, le=3.0, description="Line spacing")
    
    # Margins (in cm)
    margin_left: float = Field(default=3.0, ge=1.0, le=5.0, description="Left margin (cm)")
    margin_right: float = Field(default=2.0, ge=1.0, le=5.0, description="Right margin (cm)")
    margin_top: float = Field(default=2.0, ge=1.0, le=5.0, description="Top margin (cm)")
    margin_bottom: float = Field(default=2.0, ge=1.0, le=5.0, description="Bottom margin (cm)")
    
    model_config = {"extra": "forbid"}


# ============================================================================
# MAIN CONFIG
# ============================================================================

class ReportConfig(BaseModel):
    """Complete report configuration"""
    
    # Core sections
    project_info: ProjectInfo = Field(..., description="Project information")
    report_profile: ReportProfile = Field(..., description="Report profile")
    
    # Optional sections
    content_requirements: ContentRequirements = Field(
        default_factory=ContentRequirements, description="Content requirements"
    )
    technical_data: TechnicalData = Field(
        default_factory=TechnicalData, description="Technical data"
    )
    evidence: Evidence = Field(
        default_factory=Evidence, description="Evidence (charts, tables, etc.)"
    )
    format_rules: FormatRules = Field(
        default_factory=FormatRules, description="Format rules"
    )
    
    # Metadata
    version: str = Field(default="1.0", description="Config version")
    created_at: Optional[date] = Field(None, description="Creation date")
    
    model_config = {"extra": "forbid"}
    
    @classmethod
    def from_legacy_config(cls, legacy: Dict[str, Any]) -> "ReportConfig":
        """Convert legacy config format to new schema"""
        
        # Map legacy fields to new structure
        project_info = ProjectInfo(
            title=legacy["title"],
            subtitle=legacy.get("subtitle"),
            description=legacy.get("description", ""),
            students=[
                Author(name=s["name"], id=s.get("id"))
                for s in legacy.get("students", [])
            ],
            advisor=legacy.get("advisor"),
            university=legacy.get("university"),
            organization=legacy.get("organization"),
            faculty=legacy.get("faculty"),
            class_name=legacy.get("class"),
            github_repo=legacy.get("github_repo"),
            demo_url=legacy.get("demo_url"),
            keywords=legacy.get("keywords", [])
        )
        
        report_profile = ReportProfile(
            report_type=cls._map_report_type(legacy.get("report_type", "project_report")),
            language=legacy.get("language", "vi"),
            target_pages=legacy.get("target_pages")
        )
        
        technical_data = TechnicalData(
            algorithms=legacy.get("algorithms", []),
            technologies=legacy.get("technologies", []),
            datasets=legacy.get("datasets", [])
        )
        
        return cls(
            project_info=project_info,
            report_profile=report_profile,
            technical_data=technical_data
        )
    
    @staticmethod
    def _map_report_type(legacy_type: str) -> str:
        """Map legacy report type to new format"""
        mapping = {
            "ttnt": "project_report",
            "thesis": "thesis",
            "technical": "technical_report",
            "business": "business_report"
        }
        return mapping.get(legacy_type, "project_report")


# ============================================================================
# VALIDATION HELPERS
# ============================================================================

def validate_config(config_dict: Dict[str, Any]) -> tuple[bool, List[str]]:
    """
    Validate configuration dictionary
    Returns: (is_valid, error_messages)
    """
    try:
        ReportConfig(**config_dict)
        return True, []
    except Exception as e:
        return False, [str(e)]


def load_config(file_path: str) -> ReportConfig:
    """Load and validate config from JSON file"""
    import json
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return ReportConfig(**data)


def save_config(config: ReportConfig, file_path: str):
    """Save config to JSON file"""
    import json
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(
            config.model_dump(mode='json', exclude_none=True),
            f,
            indent=2,
            ensure_ascii=False
        )
