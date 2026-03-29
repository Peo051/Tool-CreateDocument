"""
PDF Document Builder
Low-level PDF construction utilities
"""

from reportlab.lib.units import inch, cm
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    Paragraph, Spacer, PageBreak, Image, Table, TableStyle,
    ListFlowable, ListItem
)
from reportlab.lib.enums import TA_CENTER
from typing import List, Any, Optional
import os


class PDFBuilder:
    """Build PDF document elements"""
    
    def __init__(self, style_manager):
        """
        Initialize PDF builder
        
        Args:
            style_manager: PDFStyleManager instance
        """
        self.style_manager = style_manager
        self.story = []
    
    def add_heading(self, text: str, level: int = 1, numbered: bool = False,
                   number: str = None) -> None:
        """
        Add heading
        
        Args:
            text: Heading text
            level: Heading level (1-3)
            numbered: Whether to add numbering
            number: Custom number
        """
        if numbered and number:
            text = f"{number}. {text}"
        
        style_name = f'CustomHeading{level}'
        style = self.style_manager.get_style(style_name)
        
        para = Paragraph(text, style)
        self.story.append(para)
    
    def add_paragraph(self, text: str, style_name: str = 'CustomNormal') -> None:
        """
        Add paragraph
        
        Args:
            text: Paragraph text
            style_name: Style name
        """
        if not text.strip():
            return
        
        style = self.style_manager.get_style(style_name)
        para = Paragraph(text, style)
        self.story.append(para)
    
    def add_bullet_list(self, items: List[str]) -> None:
        """
        Add bullet list
        
        Args:
            items: List items
        """
        style = self.style_manager.get_style('CustomBullet')
        
        list_items = []
        for item in items:
            para = Paragraph(item, style)
            list_items.append(ListItem(para, bulletColor='black'))
        
        bullet_list = ListFlowable(
            list_items,
            bulletType='bullet',
            start='•'
        )
        self.story.append(bullet_list)
    
    def add_numbered_list(self, items: List[str]) -> None:
        """
        Add numbered list
        
        Args:
            items: List items
        """
        style = self.style_manager.get_style('CustomBullet')
        
        for i, item in enumerate(items, 1):
            text = f"{i}. {item}"
            para = Paragraph(text, style)
            self.story.append(para)
    
    def add_image(self, image_path: str, width: Optional[float] = None,
                 caption: Optional[str] = None) -> None:
        """
        Add image with optional caption
        
        Args:
            image_path: Path to image file
            width: Image width (default: 5.5 inches)
            caption: Image caption
        """
        if not os.path.exists(image_path):
            return
        
        width = width or 5.5*inch
        
        try:
            # Get image dimensions first
            from PIL import Image as PILImage
            pil_img = PILImage.open(image_path)
            img_width, img_height = pil_img.size
            
            # Calculate height maintaining aspect ratio
            aspect = img_height / img_width
            height = width * aspect
            
            img = Image(image_path, width=width, height=height)
            self.story.append(Spacer(1, 0.2*inch))
            self.story.append(img)
            
            if caption:
                self.add_caption(caption)
        except Exception as e:
            # Skip image if error
            pass
    
    def add_caption(self, text: str, prefix: str = "Figure") -> None:
        """
        Add caption
        
        Args:
            text: Caption text
            prefix: Caption prefix
        """
        caption_text = f"{prefix}: {text}"
        style = self.style_manager.get_style('Caption')
        para = Paragraph(caption_text, style)
        self.story.append(para)
        self.story.append(Spacer(1, 0.1*inch))
    
    def add_table(self, headers: List[str], rows: List[List[Any]]) -> None:
        """
        Add table
        
        Args:
            headers: Column headers
            rows: Table rows
        """
        # Prepare data
        data = [headers] + rows
        
        # Create table
        table = Table(data, repeatRows=1)
        
        # Style table
        table.setStyle(TableStyle([
            # Header styling
            ('BACKGROUND', (0, 0), (-1, 0), HexColor('#4CAF50')),
            ('TEXTCOLOR', (0, 0), (-1, 0), HexColor('#FFFFFF')),
            ('FONTNAME', (0, 0), (-1, 0), 'Times-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            
            # Body styling
            ('FONTNAME', (0, 1), (-1, -1), 'Times-Roman'),
            ('FONTSIZE', (0, 1), (-1, -1), 11),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor('#FFFFFF'), HexColor('#F0F0F0')]),
            
            # Grid
            ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#000000')),
            ('BOX', (0, 0), (-1, -1), 1, HexColor('#000000')),
            
            # Padding
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ]))
        
        self.story.append(Spacer(1, 0.2*inch))
        self.story.append(table)
        self.story.append(Spacer(1, 0.2*inch))
    
    def add_code_block(self, code: str) -> None:
        """
        Add code block
        
        Args:
            code: Code text
        """
        style = self.style_manager.get_style('CustomCode')
        
        # Escape HTML characters
        code = code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        
        para = Paragraph(f'<pre>{code}</pre>', style)
        self.story.append(para)
    
    def add_page_break(self) -> None:
        """Add page break"""
        self.story.append(PageBreak())
    
    def add_spacer(self, height: float = 0.2) -> None:
        """
        Add vertical space
        
        Args:
            height: Height in inches
        """
        self.story.append(Spacer(1, height*inch))
    
    def add_centered_text(self, text: str, size: int = 13, bold: bool = False) -> None:
        """
        Add centered text
        
        Args:
            text: Text content
            size: Font size
            bold: Bold text
        """
        font = 'Times-Bold' if bold else 'Times-Roman'
        style = self.style_manager.get_style('Centered')
        
        # Override font
        from reportlab.lib.styles import ParagraphStyle
        custom_style = ParagraphStyle(
            'TempCentered',
            parent=style,
            fontName=font,
            fontSize=size
        )
        
        para = Paragraph(text, custom_style)
        self.story.append(para)
    
    def get_story(self) -> List[Any]:
        """Get the story (list of flowables)"""
        return self.story
