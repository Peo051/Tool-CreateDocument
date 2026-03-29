from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from enum import Enum

class SectionType(Enum):
    COVER = "cover"
    ACKNOWLEDGMENT = "acknowledgment"
    COMMITMENT = "commitment"
    TOC = "toc"
    INTRODUCTION = "introduction"
    CHAPTER = "chapter"
    ALGORITHM = "algorithm"
    CONCLUSION = "conclusion"
    REFERENCES = "references"

@dataclass
class Section:
    id: str
    title: str
    type: SectionType
    content: str = ""
    level: int = 1
    subsections: List['Section'] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def add_subsection(self, subsection: 'Section'):
        self.subsections.append(subsection)
    
    def get_full_content(self) -> str:
        """Get content including all subsections"""
        parts = [self.content]
        for sub in self.subsections:
            parts.append(sub.get_full_content())
        return "\n\n".join(filter(None, parts))
