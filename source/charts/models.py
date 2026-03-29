"""
Chart Data Models
Structured input for chart generation
"""

from typing import List, Dict, Any, Optional, Literal, Union
from pydantic import BaseModel, Field, field_validator
from dataclasses import dataclass


# ============================================================================
# CHART DATA MODELS
# ============================================================================

class ChartColumn(BaseModel):
    """Column definition for chart data"""
    name: str = Field(..., min_length=1, description="Column name")
    type: Literal["string", "number", "category"] = Field(
        default="string", description="Data type"
    )
    label: Optional[str] = Field(None, description="Display label")
    
    model_config = {"extra": "forbid"}


class BarChartData(BaseModel):
    """Bar chart data structure"""
    categories: List[str] = Field(..., min_length=1, description="Category labels (x-axis)")
    values: List[Union[int, float]] = Field(..., min_length=1, description="Values (y-axis)")
    label: Optional[str] = Field(None, description="Data series label")
    
    @field_validator('values')
    @classmethod
    def validate_values(cls, v, info):
        categories = info.data.get('categories', [])
        if len(v) != len(categories):
            raise ValueError(f"Values length ({len(v)}) must match categories length ({len(categories)})")
        return v
    
    model_config = {"extra": "forbid"}


class LineChartData(BaseModel):
    """Line chart data structure"""
    x_values: List[Union[int, float, str]] = Field(..., min_length=2, description="X-axis values")
    y_values: List[Union[int, float]] = Field(..., min_length=2, description="Y-axis values")
    label: Optional[str] = Field(None, description="Line label")
    
    @field_validator('y_values')
    @classmethod
    def validate_values(cls, v, info):
        x_values = info.data.get('x_values', [])
        if len(v) != len(x_values):
            raise ValueError(f"Y values length ({len(v)}) must match X values length ({len(x_values)})")
        return v
    
    model_config = {"extra": "forbid"}


class PieChartData(BaseModel):
    """Pie chart data structure"""
    labels: List[str] = Field(..., min_length=1, description="Slice labels")
    values: List[Union[int, float]] = Field(..., min_length=1, description="Slice values")
    
    @field_validator('values')
    @classmethod
    def validate_values(cls, v, info):
        labels = info.data.get('labels', [])
        if len(v) != len(labels):
            raise ValueError(f"Values length ({len(v)}) must match labels length ({len(labels)})")
        if any(val < 0 for val in v):
            raise ValueError("Pie chart values must be non-negative")
        return v
    
    model_config = {"extra": "forbid"}


class ComparisonTableData(BaseModel):
    """Comparison table data structure"""
    headers: List[str] = Field(..., min_length=2, description="Column headers")
    rows: List[List[Any]] = Field(..., min_length=1, description="Table rows")
    
    @field_validator('rows')
    @classmethod
    def validate_rows(cls, v, info):
        headers = info.data.get('headers', [])
        for i, row in enumerate(v):
            if len(row) != len(headers):
                raise ValueError(
                    f"Row {i} length ({len(row)}) must match headers length ({len(headers)})"
                )
        return v
    
    model_config = {"extra": "forbid"}


class MultiSeriesData(BaseModel):
    """Multi-series data for grouped/stacked charts"""
    categories: List[str] = Field(..., min_length=1, description="Category labels")
    series: List[Dict[str, Any]] = Field(..., min_length=1, description="Data series")
    
    @field_validator('series')
    @classmethod
    def validate_series(cls, v, info):
        categories = info.data.get('categories', [])
        for i, s in enumerate(v):
            if 'label' not in s:
                raise ValueError(f"Series {i} must have 'label' field")
            if 'values' not in s:
                raise ValueError(f"Series {i} must have 'values' field")
            if len(s['values']) != len(categories):
                raise ValueError(
                    f"Series {i} values length must match categories length"
                )
        return v
    
    model_config = {"extra": "forbid"}


# ============================================================================
# CHART REQUEST
# ============================================================================

class ChartRequest(BaseModel):
    """Complete chart generation request"""
    id: str = Field(..., min_length=1, description="Unique chart ID")
    title: str = Field(..., min_length=1, description="Chart title")
    type: Literal["bar", "line", "pie", "comparison_table", "grouped_bar", "stacked_bar"] = Field(
        ..., description="Chart type"
    )
    data: Union[BarChartData, LineChartData, PieChartData, ComparisonTableData, MultiSeriesData] = Field(
        ..., description="Chart data"
    )
    
    # Optional styling
    x_label: Optional[str] = Field(None, description="X-axis label")
    y_label: Optional[str] = Field(None, description="Y-axis label")
    caption: Optional[str] = Field(None, description="Chart caption")
    
    # Output options
    width: int = Field(default=10, ge=4, le=20, description="Figure width in inches")
    height: int = Field(default=6, ge=3, le=15, description="Figure height in inches")
    dpi: int = Field(default=150, ge=72, le=300, description="Resolution (DPI)")
    
    model_config = {"extra": "forbid"}


# ============================================================================
# CHART RESULT
# ============================================================================

@dataclass
class ChartResult:
    """Result from chart generation"""
    id: str
    title: str
    type: str
    file_path: str
    caption: str
    metadata: Dict[str, Any]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'type': self.type,
            'file_path': self.file_path,
            'caption': self.caption,
            'metadata': self.metadata
        }
