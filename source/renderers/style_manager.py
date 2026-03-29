"""
Style Manager for DOCX Documents
Centralized style configuration and management
"""

from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from typing import Dict, Any


class StyleManager:
    """Manage document styles and formatting"""
    
    # Default style configurations
    DEFAULT_STYLES = {
        'page': {
            'width': Cm(21),
            'height': Cm(29.7),
            'left_margin': Cm(3),
            'right_margin': Cm(2),
            'top_margin': Cm(2),
            'bottom_margin': Cm(2)
        },
        'normal': {
            'font_name': 'Times New Roman',
            'font_size': Pt(13),
            'line_spacing': 1.5,
            'alignment': WD_ALIGN_PARAGRAPH.JUSTIFY
        },
        'heading1': {
            'font_name': 'Times New Roman',
            'font_size': Pt(16),
            'bold': True,
            'alignment': WD_ALIGN_PARAGRAPH.CENTER,
            'space_before': Pt(12),
            'space_after': Pt(6)
        },
        'heading2': {
            'font_name': 'Times New Roman',
            'font_size': Pt(14),
            'bold': True,
            'alignment': WD_ALIGN_PARAGRAPH.LEFT,
            'space_before': Pt(10),
            'space_after': Pt(6)
        },
        'heading3': {
            'font_name': 'Times New Roman',
            'font_size': Pt(13),
            'bold': True,
            'alignment': WD_ALIGN_PARAGRAPH.LEFT,
            'space_before': Pt(8),
            'space_after': Pt(4)
        },
        'caption': {
            'font_name': 'Times New Roman',
            'font_size': Pt(11),
            'italic': True,
            'alignment': WD_ALIGN_PARAGRAPH.CENTER,
            'space_before': Pt(6),
            'space_after': Pt(6)
        },
        'code': {
            'font_name': 'Courier New',
            'font_size': Pt(10),
            'background_color': 'F0F0F0',
            'left_indent': Inches(0.5)
        },
        'table': {
            'font_name': 'Times New Roman',
            'font_size': Pt(11),
            'alignment': WD_ALIGN_PARAGRAPH.CENTER
        }
    }
    
    def __init__(self, custom_styles: Dict[str, Any] = None):
        """
        Initialize style manager
        
        Args:
            custom_styles: Custom style overrides
        """
        self.styles = self.DEFAULT_STYLES.copy()
        if custom_styles:
            self._merge_styles(custom_styles)
    
    def apply_to_document(self, doc: Document):
        """
        Apply styles to document
        
        Args:
            doc: Document instance
        """
        self._setup_page_layout(doc)
        self._setup_text_styles(doc)
    
    def _setup_page_layout(self, doc: Document):
        """Setup page layout"""
        page_style = self.styles['page']
        
        for section in doc.sections:
            section.page_width = page_style['width']
            section.page_height = page_style['height']
            section.left_margin = page_style['left_margin']
            section.right_margin = page_style['right_margin']
            section.top_margin = page_style['top_margin']
            section.bottom_margin = page_style['bottom_margin']
    
    def _setup_text_styles(self, doc: Document):
        """Setup text styles"""
        styles = doc.styles
        
        # Normal style
        self._apply_style(styles['Normal'], self.styles['normal'])
        
        # Heading styles
        for i in range(1, 4):
            style_name = f'Heading {i}'
            config_name = f'heading{i}'
            if style_name in styles and config_name in self.styles:
                self._apply_style(styles[style_name], self.styles[config_name])
    
    def _apply_style(self, style, config: Dict[str, Any]):
        """Apply configuration to style"""
        if 'font_name' in config:
            style.font.name = config['font_name']
        
        if 'font_size' in config:
            style.font.size = config['font_size']
        
        if 'bold' in config:
            style.font.bold = config['bold']
        
        if 'italic' in config:
            style.font.italic = config['italic']
        
        if 'alignment' in config:
            style.paragraph_format.alignment = config['alignment']
        
        if 'line_spacing' in config:
            style.paragraph_format.line_spacing = config['line_spacing']
        
        if 'space_before' in config:
            style.paragraph_format.space_before = config['space_before']
        
        if 'space_after' in config:
            style.paragraph_format.space_after = config['space_after']
    
    def _merge_styles(self, custom_styles: Dict[str, Any]):
        """Merge custom styles with defaults"""
        for key, value in custom_styles.items():
            if key in self.styles and isinstance(value, dict):
                self.styles[key].update(value)
            else:
                self.styles[key] = value
    
    def get_style(self, style_name: str) -> Dict[str, Any]:
        """Get style configuration"""
        return self.styles.get(style_name, {})
