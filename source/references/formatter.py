"""
Citation formatters for different styles
"""

from abc import ABC, abstractmethod
from typing import List
from .models import ReferenceEntry


class CitationFormatter(ABC):
    """Base citation formatter"""
    
    @abstractmethod
    def format_citation(self, ref: ReferenceEntry) -> str:
        """Format full citation"""
        pass
    
    @abstractmethod
    def format_inline(self, ref: ReferenceEntry) -> str:
        """Format inline citation"""
        pass
    
    def format_authors(self, authors: List[str], max_authors: int = None) -> str:
        """Format author list"""
        if not authors:
            return ""
        
        if max_authors and len(authors) > max_authors:
            return f"{authors[0]} et al."
        
        if len(authors) == 1:
            return authors[0]
        elif len(authors) == 2:
            return f"{authors[0]} and {authors[1]}"
        else:
            return ", ".join(authors[:-1]) + f", and {authors[-1]}"


class APAFormatter(CitationFormatter):
    """APA 7th edition formatter"""
    
    def format_citation(self, ref: ReferenceEntry) -> str:
        """
        Format full APA citation
        Example: Smith, J., & Doe, A. (2020). Title of work. Journal Name, 10(2), 123-145.
        """
        parts = []
        
        # Authors
        authors = self._format_apa_authors(ref.authors)
        parts.append(authors)
        
        # Year
        parts.append(f"({ref.year}).")
        
        # Title
        parts.append(f"{ref.title}.")
        
        # Source details
        if ref.type == "book":
            if ref.publisher:
                parts.append(f"{ref.publisher}.")
        elif ref.type == "article" or ref.type == "journal":
            if ref.source:
                source_part = f"*{ref.source}*"
                if ref.volume:
                    source_part += f", {ref.volume}"
                    if ref.issue:
                        source_part += f"({ref.issue})"
                if ref.pages:
                    source_part += f", {ref.pages}"
                parts.append(source_part + ".")
        elif ref.type == "conference":
            if ref.source:
                parts.append(f"In *{ref.source}*.")
        
        # DOI or URL
        if ref.doi:
            parts.append(f"https://doi.org/{ref.doi}")
        elif ref.url:
            parts.append(ref.url)
        
        return " ".join(parts)
    
    def format_inline(self, ref: ReferenceEntry) -> str:
        """
        Format inline APA citation
        Example: (Smith & Doe, 2020)
        """
        if len(ref.authors) == 1:
            author_part = self._get_last_name(ref.authors[0])
        elif len(ref.authors) == 2:
            author_part = f"{self._get_last_name(ref.authors[0])} & {self._get_last_name(ref.authors[1])}"
        else:
            author_part = f"{self._get_last_name(ref.authors[0])} et al."
        
        return f"({author_part}, {ref.year})"
    
    def _format_apa_authors(self, authors: List[str]) -> str:
        """Format authors in APA style"""
        if not authors:
            return ""
        
        formatted = []
        for author in authors:
            # Try to format as "Last, F. M."
            parts = author.split()
            if len(parts) >= 2:
                last = parts[-1]
                initials = ". ".join([p[0] for p in parts[:-1]]) + "."
                formatted.append(f"{last}, {initials}")
            else:
                formatted.append(author)
        
        if len(formatted) == 1:
            return formatted[0]
        elif len(formatted) == 2:
            return f"{formatted[0]}, & {formatted[1]}"
        else:
            return ", ".join(formatted[:-1]) + f", & {formatted[-1]}"
    
    def _get_last_name(self, author: str) -> str:
        """Extract last name"""
        parts = author.split()
        return parts[-1] if parts else author


class IEEEFormatter(CitationFormatter):
    """IEEE citation formatter"""
    
    def format_citation(self, ref: ReferenceEntry) -> str:
        """
        Format full IEEE citation
        Example: [1] J. Smith and A. Doe, "Title of work," Journal Name, vol. 10, no. 2, pp. 123-145, 2020.
        """
        parts = []
        
        # Authors
        authors = self._format_ieee_authors(ref.authors)
        parts.append(authors + ",")
        
        # Title in quotes
        parts.append(f'"{ref.title},"')
        
        # Source details
        if ref.type == "book":
            if ref.publisher:
                parts.append(f"{ref.publisher},")
        elif ref.type == "article" or ref.type == "journal":
            if ref.source:
                source_part = f"*{ref.source}*"
                if ref.volume:
                    source_part += f", vol. {ref.volume}"
                if ref.issue:
                    source_part += f", no. {ref.issue}"
                if ref.pages:
                    source_part += f", pp. {ref.pages}"
                parts.append(source_part + ",")
        elif ref.type == "conference":
            if ref.source:
                parts.append(f"in *{ref.source}*,")
        
        # Year
        parts.append(f"{ref.year}.")
        
        # DOI or URL
        if ref.doi:
            parts.append(f"doi: {ref.doi}")
        elif ref.url:
            parts.append(f"[Online]. Available: {ref.url}")
        
        return " ".join(parts)
    
    def format_inline(self, ref: ReferenceEntry) -> str:
        """
        Format inline IEEE citation
        Example: [1]
        """
        return f"[{ref.id}]"
    
    def _format_ieee_authors(self, authors: List[str]) -> str:
        """Format authors in IEEE style"""
        if not authors:
            return ""
        
        formatted = []
        for author in authors:
            # Try to format as "F. M. Last"
            parts = author.split()
            if len(parts) >= 2:
                last = parts[-1]
                initials = ". ".join([p[0] for p in parts[:-1]]) + "."
                formatted.append(f"{initials} {last}")
            else:
                formatted.append(author)
        
        if len(formatted) == 1:
            return formatted[0]
        elif len(formatted) == 2:
            return f"{formatted[0]} and {formatted[1]}"
        else:
            return ", ".join(formatted[:-1]) + f", and {formatted[-1]}"
