from typing import Dict, Any
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from models import Report
from renderers import DocxRenderer

class ReportRenderer:
    """Render report to output format"""
    
    def __init__(self, output_format: str = "docx"):
        self.output_format = output_format
        self.renderer = self._get_renderer()
    
    def _get_renderer(self):
        """Get appropriate renderer"""
        if self.output_format == "docx":
            return DocxRenderer()
        else:
            raise ValueError(f"Unsupported format: {self.output_format}")
    
    def render(self, report: Report, output_path: str) -> str:
        """Render report to file"""
        return self.renderer.render(report, output_path)
