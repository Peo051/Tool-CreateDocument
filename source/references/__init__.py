"""
References Engine
Citation formatting and bibliography generation
"""

from .formatter import CitationFormatter, APAFormatter, IEEEFormatter
from .bibliography import BibliographyGenerator
from .models import ReferenceEntry

__all__ = [
    'CitationFormatter',
    'APAFormatter',
    'IEEEFormatter',
    'BibliographyGenerator',
    'ReferenceEntry'
]
