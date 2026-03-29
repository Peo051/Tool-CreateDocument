from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List
from enum import Enum

class EvidenceType(Enum):
    CHART = "chart"
    TABLE = "table"
    FIGURE = "figure"
    REFERENCE = "reference"

@dataclass
class Evidence:
    id: str
    type: EvidenceType
    title: str
    caption: Optional[str] = None
    position: Optional[str] = None  # section_id
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Chart(Evidence):
    chart_type: str = "bar"  # bar, line, pie, scatter
    data: Dict[str, Any] = field(default_factory=dict)
    file_path: Optional[str] = None
    
    def __post_init__(self):
        if self.type != EvidenceType.CHART:
            self.type = EvidenceType.CHART

@dataclass
class Table(Evidence):
    headers: List[str] = field(default_factory=list)
    rows: List[List[Any]] = field(default_factory=list)
    
    def __post_init__(self):
        if self.type != EvidenceType.TABLE:
            self.type = EvidenceType.TABLE

@dataclass
class Figure(Evidence):
    file_path: str = ""
    width: Optional[float] = None
    
    def __post_init__(self):
        if self.type != EvidenceType.FIGURE:
            self.type = EvidenceType.FIGURE

@dataclass
class Reference(Evidence):
    authors: List[str] = field(default_factory=list)
    year: int = 2024
    source: str = ""
    url: Optional[str] = None
    
    def __post_init__(self):
        if self.type != EvidenceType.REFERENCE:
            self.type = EvidenceType.REFERENCE
