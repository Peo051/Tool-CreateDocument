"""
Document Renderers Package
"""

# DOCX Renderers
from .style_manager import StyleManager
from .document_builder import DocumentBuilder
from .report_renderer import ReportRenderer

# PDF Renderers
from .pdf_styles import PDFStyleManager
from .pdf_builder import PDFBuilder
from .pdf_renderer import PDFReportRenderer

# Keep old renderer for backward compatibility
from .docx_renderer import DocxRenderer

__all__ = [
    # DOCX
    'StyleManager',
    'DocumentBuilder',
    'ReportRenderer',
    'DocxRenderer',  # Legacy
    
    # PDF
    'PDFStyleManager',
    'PDFBuilder',
    'PDFReportRenderer',
]
