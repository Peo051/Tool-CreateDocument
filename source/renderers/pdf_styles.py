"""
PDF Style Manager
Centralized styling for PDF documents
"""

from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.lib.units import cm, inch
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, black
from typing import Dict, Any


class PDFStyleManager:
    """Manage PDF document styles"""
    
    def __init__(self, custom_styles: Dict[str, Any] = None):
        """
        Initialize PDF style manager
        
        Args:
            custom_styles: Custom style overrides
        """
        self.styles = getSampleStyleSheet()
        self._setup_default_styles()
        
        if custom_styles:
            self._apply_custom_styles(custom_styles)
    
    def _setup_default_styles(self):
        """Setup default styles"""
        # Normal style
        self.styles.add(ParagraphStyle(
            name='CustomNormal',
            parent=self.styles['Normal'],
            fontName='Times-Roman',
            fontSize=13,
            leading=19.5,  # 1.5 line spacing
            alignment=TA_JUSTIFY,
            spaceAfter=6
        ))
        
        # Heading 1
        self.styles.add(ParagraphStyle(
            name='CustomHeading1',
            parent=self.styles['Heading1'],
            fontName='Times-Bold',
            fontSize=16,
            leading=20,
            alignment=TA_CENTER,
            spaceAfter=12,
            spaceBefore=12
        ))
        
        # Heading 2
        self.styles.add(ParagraphStyle(
            name='CustomHeading2',
            parent=self.styles['Heading2'],
            fontName='Times-Bold',
            fontSize=14,
            leading=18,
            alignment=TA_LEFT,
            spaceAfter=10,
            spaceBefore=10
        ))
        
        # Heading 3
        self.styles.add(ParagraphStyle(
            name='CustomHeading3',
            parent=self.styles['Heading3'],
            fontName='Times-Bold',
            fontSize=13,
            leading=16,
            alignment=TA_LEFT,
            spaceAfter=8,
            spaceBefore=8
        ))
        
        # Caption
        self.styles.add(ParagraphStyle(
            name='Caption',
            parent=self.styles['Normal'],
            fontName='Times-Italic',
            fontSize=11,
            leading=14,
            alignment=TA_CENTER,
            spaceAfter=6,
            spaceBefore=6
        ))
        
        # Code
        self.styles.add(ParagraphStyle(
            name='CustomCode',
            parent=self.styles['Normal'],
            fontName='Courier',
            fontSize=10,
            leading=12,
            alignment=TA_LEFT,
            leftIndent=0.5*inch,
            backColor=HexColor('#F0F0F0'),
            spaceAfter=6,
            spaceBefore=6
        ))
        
        # Bullet
        self.styles.add(ParagraphStyle(
            name='CustomBullet',
            parent=self.styles['Normal'],
            fontName='Times-Roman',
            fontSize=13,
            leading=19.5,
            leftIndent=0.5*inch,
            bulletIndent=0.25*inch,
            spaceAfter=3
        ))
        
        # Centered
        self.styles.add(ParagraphStyle(
            name='Centered',
            parent=self.styles['Normal'],
            fontName='Times-Roman',
            fontSize=13,
            alignment=TA_CENTER,
            spaceAfter=6
        ))
    
    def _apply_custom_styles(self, custom_styles: Dict[str, Any]):
        """Apply custom style overrides"""
        for style_name, config in custom_styles.items():
            if style_name in self.styles:
                style = self.styles[style_name]
                for key, value in config.items():
                    setattr(style, key, value)
    
    def get_style(self, name: str) -> ParagraphStyle:
        """Get style by name"""
        return self.styles.get(name, self.styles['Normal'])
    
    @staticmethod
    def get_page_config() -> Dict[str, Any]:
        """Get page configuration"""
        return {
            'pagesize': A4,
            'leftMargin': 3*cm,
            'rightMargin': 2*cm,
            'topMargin': 2*cm,
            'bottomMargin': 2*cm
        }
