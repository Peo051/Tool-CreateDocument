from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

@dataclass
class ReportMetadata:
    title: str
    subtitle: Optional[str] = None
    authors: List[Dict[str, str]] = field(default_factory=list)
    advisor: Optional[str] = None
    organization: str = ""
    faculty: str = ""
    class_name: str = ""
    github_repo: Optional[str] = None
    demo_url: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)

@dataclass
class Report:
    metadata: ReportMetadata
    sections: List['Section'] = field(default_factory=list)
    evidence: List['Evidence'] = field(default_factory=list)
    config: Dict[str, Any] = field(default_factory=dict)
    
    def add_section(self, section: 'Section'):
        self.sections.append(section)
    
    def add_evidence(self, evidence: 'Evidence'):
        self.evidence.append(evidence)
    
    def get_section_by_id(self, section_id: str) -> Optional['Section']:
        for section in self.sections:
            if section.id == section_id:
                return section
        return None
