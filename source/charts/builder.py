"""
Chart Builder
Generate charts from structured input data
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
from typing import Optional, Dict, Any
from io import BytesIO

from .models import (
    ChartRequest, ChartResult,
    BarChartData, LineChartData, PieChartData,
    ComparisonTableData, MultiSeriesData
)


class ChartBuilder:
    """Build charts from structured data"""
    
    def __init__(self, output_dir: str = "output/charts"):
        """
        Initialize chart builder
        
        Args:
            output_dir: Directory to save chart images
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Configure matplotlib
        plt.rcParams['font.size'] = 10
        plt.rcParams['figure.dpi'] = 150
        plt.rcParams['axes.grid'] = True
        plt.rcParams['grid.alpha'] = 0.3
    
    def build(self, request: ChartRequest) -> ChartResult:
        """
        Build chart from request
        
        Args:
            request: Chart generation request
            
        Returns:
            ChartResult with file path and metadata
        """
        # Route to appropriate builder
        builders = {
            'bar': self._build_bar_chart,
            'line': self._build_line_chart,
            'pie': self._build_pie_chart,
            'comparison_table': self._build_comparison_table,
            'grouped_bar': self._build_grouped_bar,
            'stacked_bar': self._build_stacked_bar,
        }
        
        builder = builders.get(request.type)
        if not builder:
            raise ValueError(f"Unsupported chart type: {request.type}")
        
        # Build chart
        fig = builder(request)
        
        # Save to file
        file_path = self._save_chart(fig, request.id)
        plt.close(fig)
        
        # Generate caption
        caption = self._generate_caption(request)
        
        # Create result
        return ChartResult(
            id=request.id,
            title=request.title,
            type=request.type,
            file_path=str(file_path),
            caption=caption,
            metadata={
                'width': request.width,
                'height': request.height,
                'dpi': request.dpi,
                'data_points': self._count_data_points(request.data)
            }
        )
    
    def _build_bar_chart(self, request: ChartRequest) -> plt.Figure:
        """Build bar chart"""
        data: BarChartData = request.data
        
        fig, ax = plt.subplots(figsize=(request.width, request.height))
        
        x_pos = np.arange(len(data.categories))
        bars = ax.bar(x_pos, data.values, alpha=0.8, edgecolor='black', linewidth=0.5)
        
        # Styling
        ax.set_xlabel(request.x_label or 'Categories')
        ax.set_ylabel(request.y_label or 'Values')
        ax.set_title(request.title, fontweight='bold', fontsize=12)
        ax.set_xticks(x_pos)
        ax.set_xticklabels(data.categories, rotation=45, ha='right')
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}',
                   ha='center', va='bottom', fontsize=8)
        
        if data.label:
            ax.legend([data.label])
        
        plt.tight_layout()
        return fig
    
    def _build_line_chart(self, request: ChartRequest) -> plt.Figure:
        """Build line chart"""
        data: LineChartData = request.data
        
        fig, ax = plt.subplots(figsize=(request.width, request.height))
        
        ax.plot(data.x_values, data.y_values, marker='o', linewidth=2, 
               markersize=6, label=data.label)
        
        # Styling
        ax.set_xlabel(request.x_label or 'X')
        ax.set_ylabel(request.y_label or 'Y')
        ax.set_title(request.title, fontweight='bold', fontsize=12)
        
        if data.label:
            ax.legend()
        
        plt.tight_layout()
        return fig
    
    def _build_pie_chart(self, request: ChartRequest) -> plt.Figure:
        """Build pie chart"""
        data: PieChartData = request.data
        
        fig, ax = plt.subplots(figsize=(request.width, request.height))
        
        # Calculate percentages
        total = sum(data.values)
        percentages = [v/total*100 for v in data.values]
        
        # Create pie chart
        wedges, texts, autotexts = ax.pie(
            data.values,
            labels=data.labels,
            autopct='%1.1f%%',
            startangle=90,
            textprops={'fontsize': 9}
        )
        
        # Make percentage text bold
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        ax.set_title(request.title, fontweight='bold', fontsize=12)
        
        plt.tight_layout()
        return fig
    
    def _build_comparison_table(self, request: ChartRequest) -> plt.Figure:
        """Build comparison table as image"""
        data: ComparisonTableData = request.data
        
        fig, ax = plt.subplots(figsize=(request.width, request.height))
        ax.axis('tight')
        ax.axis('off')
        
        # Create table
        table = ax.table(
            cellText=data.rows,
            colLabels=data.headers,
            cellLoc='center',
            loc='center',
            colWidths=[1.0/len(data.headers)] * len(data.headers)
        )
        
        # Style table
        table.auto_set_font_size(False)
        table.set_fontsize(9)
        table.scale(1, 2)
        
        # Header styling
        for i in range(len(data.headers)):
            cell = table[(0, i)]
            cell.set_facecolor('#4CAF50')
            cell.set_text_props(weight='bold', color='white')
        
        # Alternate row colors
        for i in range(1, len(data.rows) + 1):
            for j in range(len(data.headers)):
                cell = table[(i, j)]
                if i % 2 == 0:
                    cell.set_facecolor('#f0f0f0')
        
        ax.set_title(request.title, fontweight='bold', fontsize=12, pad=20)
        
        plt.tight_layout()
        return fig
    
    def _build_grouped_bar(self, request: ChartRequest) -> plt.Figure:
        """Build grouped bar chart"""
        data: MultiSeriesData = request.data
        
        fig, ax = plt.subplots(figsize=(request.width, request.height))
        
        x = np.arange(len(data.categories))
        width = 0.8 / len(data.series)
        
        for i, series in enumerate(data.series):
            offset = (i - len(data.series)/2 + 0.5) * width
            ax.bar(x + offset, series['values'], width, 
                  label=series['label'], alpha=0.8, edgecolor='black', linewidth=0.5)
        
        ax.set_xlabel(request.x_label or 'Categories')
        ax.set_ylabel(request.y_label or 'Values')
        ax.set_title(request.title, fontweight='bold', fontsize=12)
        ax.set_xticks(x)
        ax.set_xticklabels(data.categories, rotation=45, ha='right')
        ax.legend()
        
        plt.tight_layout()
        return fig
    
    def _build_stacked_bar(self, request: ChartRequest) -> plt.Figure:
        """Build stacked bar chart"""
        data: MultiSeriesData = request.data
        
        fig, ax = plt.subplots(figsize=(request.width, request.height))
        
        x = np.arange(len(data.categories))
        bottom = np.zeros(len(data.categories))
        
        for series in data.series:
            ax.bar(x, series['values'], label=series['label'], 
                  bottom=bottom, alpha=0.8, edgecolor='black', linewidth=0.5)
            bottom += np.array(series['values'])
        
        ax.set_xlabel(request.x_label or 'Categories')
        ax.set_ylabel(request.y_label or 'Values')
        ax.set_title(request.title, fontweight='bold', fontsize=12)
        ax.set_xticks(x)
        ax.set_xticklabels(data.categories, rotation=45, ha='right')
        ax.legend()
        
        plt.tight_layout()
        return fig
    
    def _save_chart(self, fig: plt.Figure, chart_id: str) -> Path:
        """Save chart to file"""
        file_path = self.output_dir / f"{chart_id}.png"
        fig.savefig(file_path, dpi=150, bbox_inches='tight', facecolor='white')
        return file_path
    
    def _generate_caption(self, request: ChartRequest) -> str:
        """Generate caption for chart"""
        if request.caption:
            return request.caption
        
        # Auto-generate caption based on chart type
        captions = {
            'bar': f"Bar chart showing {request.title.lower()}",
            'line': f"Line chart illustrating {request.title.lower()}",
            'pie': f"Pie chart representing {request.title.lower()}",
            'comparison_table': f"Comparison table for {request.title.lower()}",
            'grouped_bar': f"Grouped bar chart comparing {request.title.lower()}",
            'stacked_bar': f"Stacked bar chart showing {request.title.lower()}",
        }
        
        return captions.get(request.type, f"Chart: {request.title}")
    
    def _count_data_points(self, data: Any) -> int:
        """Count number of data points"""
        if isinstance(data, BarChartData):
            return len(data.values)
        elif isinstance(data, LineChartData):
            return len(data.y_values)
        elif isinstance(data, PieChartData):
            return len(data.values)
        elif isinstance(data, ComparisonTableData):
            return len(data.rows) * len(data.headers)
        elif isinstance(data, MultiSeriesData):
            return len(data.categories) * len(data.series)
        return 0
    
    def build_batch(self, requests: list[ChartRequest]) -> list[ChartResult]:
        """
        Build multiple charts in batch
        
        Args:
            requests: List of chart requests
            
        Returns:
            List of chart results
        """
        return [self.build(request) for request in requests]
    
    def to_bytes(self, request: ChartRequest) -> BytesIO:
        """
        Generate chart as bytes (for in-memory use)
        
        Args:
            request: Chart generation request
            
        Returns:
            BytesIO buffer with PNG image
        """
        builders = {
            'bar': self._build_bar_chart,
            'line': self._build_line_chart,
            'pie': self._build_pie_chart,
            'comparison_table': self._build_comparison_table,
            'grouped_bar': self._build_grouped_bar,
            'stacked_bar': self._build_stacked_bar,
        }
        
        builder = builders.get(request.type)
        if not builder:
            raise ValueError(f"Unsupported chart type: {request.type}")
        
        fig = builder(request)
        
        buf = BytesIO()
        fig.savefig(buf, format='png', dpi=request.dpi, bbox_inches='tight', facecolor='white')
        buf.seek(0)
        plt.close(fig)
        
        return buf
