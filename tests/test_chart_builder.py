"""
Test chart builder
"""

import pytest
from pathlib import Path
from source.charts.builder import ChartBuilder
from source.charts.models import BarChartData, LineChartData, PieChartData, ChartColumn


def test_bar_chart_creation(temp_output_dir):
    """Test bar chart creation"""
    from source.charts.models import ChartRequest
    builder = ChartBuilder(output_dir=temp_output_dir)
    
    data = BarChartData(
        categories=['A', 'B', 'C'],
        values=[10, 20, 30]
    )
    
    request = ChartRequest(
        id='test_bar',
        title='Test Bar Chart',
        type='bar',
        data=data,
        x_label='Categories',
        y_label='Values'
    )
    
    result = builder.build(request)
    
    assert result.title == 'Test Bar Chart'
    assert result.file_path is not None
    assert Path(result.file_path).exists()


def test_line_chart_creation(temp_output_dir):
    """Test line chart creation"""
    from source.charts.models import ChartRequest
    builder = ChartBuilder(output_dir=temp_output_dir)
    
    data = LineChartData(
        x_values=[1, 2, 3, 4],
        y_values=[10, 20, 15, 25]
    )
    
    request = ChartRequest(
        id='test_line',
        title='Test Line Chart',
        type='line',
        data=data,
        x_label='X Axis',
        y_label='Y Axis'
    )
    
    result = builder.build(request)
    
    assert result.title == 'Test Line Chart'
    assert result.file_path is not None
    assert Path(result.file_path).exists()


def test_pie_chart_creation(temp_output_dir):
    """Test pie chart creation"""
    from source.charts.models import ChartRequest
    builder = ChartBuilder(output_dir=temp_output_dir)
    
    data = PieChartData(
        labels=['A', 'B', 'C'],
        values=[30, 40, 30]
    )
    
    request = ChartRequest(
        id='test_pie',
        title='Test Pie Chart',
        type='pie',
        data=data
    )
    
    result = builder.build(request)
    
    assert result.title == 'Test Pie Chart'
    assert result.file_path is not None
    assert Path(result.file_path).exists()


def test_invalid_chart_data(temp_output_dir):
    """Test chart builder handles invalid data"""
    builder = ChartBuilder(output_dir=temp_output_dir)
    
    # Mismatched categories and values
    with pytest.raises(ValueError):
        BarChartData(
            categories=['A', 'B'],
            values=[10, 20, 30]  # Too many values
        )


def test_chart_builder_output_directory(temp_output_dir):
    """Test chart builder creates output directory"""
    from source.charts.models import ChartRequest
    output_dir = temp_output_dir / 'charts'
    builder = ChartBuilder(output_dir=output_dir)
    
    data = BarChartData(
        categories=['A'],
        values=[10]
    )
    
    request = ChartRequest(
        id='test_dir',
        title='Test',
        type='bar',
        data=data,
        x_label='X',
        y_label='Y'
    )
    
    result = builder.build(request)
    assert output_dir.exists()
    assert result.file_path is not None


def test_chart_caption_generation(temp_output_dir):
    """Test chart caption is generated correctly"""
    from source.charts.models import ChartRequest
    builder = ChartBuilder(output_dir=temp_output_dir)
    
    data = BarChartData(
        categories=['Method A', 'Method B'],
        values=[85, 92]
    )
    
    request = ChartRequest(
        id='test_caption',
        title='Performance Comparison',
        type='bar',
        data=data,
        x_label='Methods',
        y_label='Accuracy (%)'
    )
    
    result = builder.build(request)
    # Caption is auto-generated and includes the title in lowercase
    assert 'performance comparison' in result.caption.lower()
