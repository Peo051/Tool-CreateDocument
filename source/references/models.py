"""
Reference data models
"""

from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class ReferenceEntry:
    """Unified reference entry"""
    id: str
    authors: List[str]
    title: str
    year: int
    
    # Optional fields
    source: Optional[str] = None  # journal, conference, publisher
    volume: Optional[str] = None
    issue: Optional[str] = None
    pages: Optional[str] = None
    doi: Optional[str] = None
    url: Optional[str] = None
    publisher: Optional[str] = None
    type: str = "article"  # article, book, conference, website
    
    def __post_init__(self):
        """Validate and normalize"""
        if not self.authors:
            raise ValueError("At least one author required")
        if self.year < 1900 or self.year > 2100:
            raise ValueError(f"Invalid year: {self.year}")
    
    @classmethod
    def from_config_model(cls, ref) -> "ReferenceEntry":
        """Create from config_models.Reference"""
        return cls(
            id=ref.id,
            authors=ref.authors,
            title=ref.title,
            year=ref.year,
            source=ref.source,
            url=str(ref.url) if ref.url else None
        )
    
    @classmethod
    def from_schema_model(cls, ref) -> "ReferenceEntry":
        """Create from schema.Reference"""
        return cls(
            id=ref.id,
            authors=ref.authors,
            title=ref.title,
            year=ref.year,
            source=ref.journal or ref.conference or ref.publisher,
            volume=ref.volume,
            pages=ref.pages,
            doi=ref.doi,
            url=str(ref.url) if ref.url else None,
            publisher=ref.publisher,
            type=ref.type
        )
