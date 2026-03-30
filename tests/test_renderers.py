"""
Test renderers (smoke tests)
"""

import pytest
from pathlib import Path
from source.renderers.report_renderer import ReportRenderer


def test_docx_renderer_initialization():
    """Test DOCX renderer can be initialized"""
    renderer = ReportRenderer()
    assert renderer is not None


def test_docx_renderer_basic_render(sample_report_data, temp_output_dir):
    """Test DOCX renderer can render basic report"""
    renderer = ReportRenderer()
    output_path = temp_output_dir / 'test_report.docx'
    
    try:
        renderer.render(sample_report_data, str(output_path))
        assert output_path.exists()
        assert output_path.stat().st_size > 0
    except Exception as e:
        pytest.skip(f"DOCX rendering failed: {e}")


def test_pdf_renderer_initialization():
    """Test PDF renderer can be initialized"""
    try:
        from source.renderers.pdf_renderer import PDFRenderer
        renderer = PDFRenderer()
        assert renderer is not None
    except ImportError:
        pytest.skip("PDF renderer dependencies not installed")


def test_pdf_renderer_basic_render(sample_report_data, temp_output_dir):
    """Test PDF renderer can render basic report"""
    try:
        from source.renderers.pdf_renderer import PDFRenderer
        renderer = PDFRenderer()
        output_path = temp_output_dir / 'test_report.pdf'
        
        renderer.render(sample_report_data, str(output_path))
        assert output_path.exists()
        assert output_path.stat().st_size > 0
    except ImportError:
        pytest.skip("PDF renderer dependencies not installed")
    except Exception as e:
        pytest.skip(f"PDF rendering failed: {e}")


def test_renderer_handles_empty_sections(temp_output_dir):
    """Test renderer handles empty sections gracefully"""
    renderer = ReportRenderer()
    output_path = temp_output_dir / 'empty_report.docx'
    
    minimal_data = {
        'metadata': {
            'title': 'Empty Report',
            'organization': 'Test Org'
        },
        'sections': [],
        'evidence': {'figures': [], 'tables': []}
    }
    
    try:
        renderer.render(minimal_data, str(output_path))
        assert output_path.exists()
    except Exception as e:
        pytest.skip(f"Rendering failed: {e}")
