# Chart Builder Guide

Complete guide for generating charts from structured data.

## Overview

The Chart Builder module provides a clean API for generating professional charts from structured input data. It replaces mock/demo data with real, validated input.

## Features

✅ **Structured Input**: Pydantic models with validation
✅ **Multiple Chart Types**: Bar, line, pie, comparison table, grouped bar, stacked bar
✅ **Data Validation**: Automatic validation of columns and data types
✅ **Caption Generation**: Auto-generated or custom captions
✅ **Batch Processing**: Generate multiple charts efficiently
✅ **Clean Output**: Organized file paths and metadata
✅ **Simple API**: Easy to use and integrate

## Quick Start

### Basic Usage

```python
from source.charts import ChartBuilder, ChartRequest, BarChartData

# Create builder
builder = ChartBuilder(output_dir="output/charts")

# Create chart request
request = ChartRequest(
    id="my_chart",
    title="Algorithm Performance",
    type="bar",
    data=BarChartData(
        categories=["BFS", "DFS", "A*"],
        values=[120, 95, 85]
    ),
    y_label="Time (ms)"
)

# Generate chart
result = builder.build(request)
print(f"Chart saved to: {result.file_path}")
```

## Chart Types

### 1. Bar Chart

Simple bar chart for categorical data.

```python
from source.charts import BarChartData, ChartRequest

request = ChartRequest(
    id="bar_example",
    title="Algorithm Execution Time",
    type="bar",
    data=BarChartData(
        categories=["BFS", "DFS", "A*", "Dijkstra"],
        values=[120, 95, 85, 150],
        label="Execution Time (ms)"
    ),
    x_label="Algorithm",
    y_label="Time (ms)",
    caption="Comparison of search algorithm execution times"
)
```

**Features**:
- Value labels on bars
- Automatic grid
- Custom axis labels
- Legend support

### 2. Line Chart

Line chart for continuous data or trends.

```python
from source.charts import LineChartData, ChartRequest

request = ChartRequest(
    id="line_example",
    title="Training Loss Over Epochs",
    type="line",
    data=LineChartData(
        x_values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        y_values=[0.95, 0.78, 0.65, 0.52, 0.45, 0.38, 0.32, 0.28, 0.25, 0.23],
        label="Training Loss"
    ),
    x_label="Epoch",
    y_label="Loss"
)
```

**Features**:
- Markers on data points
- Smooth lines
- Legend support
- Grid overlay

### 3. Pie Chart

Pie chart for proportional data.

```python
from source.charts import PieChartData, ChartRequest

request = ChartRequest(
    id="pie_example",
    title="Dataset Split Distribution",
    type="pie",
    data=PieChartData(
        labels=["Training", "Validation", "Testing"],
        values=[7000, 1500, 1500]
    )
)
```

**Features**:
- Automatic percentage calculation
- Bold percentage labels
- Color-coded slices
- Clean layout

### 4. Comparison Table

Table rendered as image for reports.

```python
from source.charts import ComparisonTableData, ChartRequest

request = ChartRequest(
    id="table_example",
    title="Algorithm Comparison",
    type="comparison_table",
    data=ComparisonTableData(
        headers=["Algorithm", "Time (ms)", "Space (MB)", "Optimal"],
        rows=[
            ["BFS", "120", "45", "Yes"],
            ["DFS", "95", "30", "No"],
            ["A*", "85", "50", "Yes"]
        ]
    ),
    width=12,
    height=4
)
```

**Features**:
- Styled headers (green background)
- Alternating row colors
- Auto-sized columns
- Clean borders

### 5. Grouped Bar Chart

Multiple series side-by-side.

```python
from source.charts import MultiSeriesData, ChartRequest

request = ChartRequest(
    id="grouped_example",
    title="Performance Across Datasets",
    type="grouped_bar",
    data=MultiSeriesData(
        categories=["Small", "Medium", "Large"],
        series=[
            {"label": "BFS", "values": [50, 120, 300]},
            {"label": "DFS", "values": [45, 95, 250]},
            {"label": "A*", "values": [40, 85, 220]}
        ]
    ),
    x_label="Dataset Size",
    y_label="Time (ms)"
)
```

**Features**:
- Multiple series
- Color-coded bars
- Legend
- Grouped layout

### 6. Stacked Bar Chart

Cumulative data visualization.

```python
from source.charts import MultiSeriesData, ChartRequest

request = ChartRequest(
    id="stacked_example",
    title="Resource Usage by Component",
    type="stacked_bar",
    data=MultiSeriesData(
        categories=["Preprocessing", "Training", "Evaluation"],
        series=[
            {"label": "CPU", "values": [30, 60, 20]},
            {"label": "Memory", "values": [20, 80, 30]},
            {"label": "Disk I/O", "values": [50, 40, 10]}
        ]
    ),
    y_label="Resource Usage (%)"
)
```

**Features**:
- Stacked layout
- Color-coded segments
- Legend
- Total visualization

## Data Models

### BarChartData

```python
class BarChartData(BaseModel):
    categories: List[str]  # X-axis labels
    values: List[Union[int, float]]  # Y-axis values
    label: Optional[str]  # Series label
```

**Validation**: Values length must match categories length.

### LineChartData

```python
class LineChartData(BaseModel):
    x_values: List[Union[int, float, str]]  # X-axis values
    y_values: List[Union[int, float]]  # Y-axis values
    label: Optional[str]  # Line label
```

**Validation**: Y values length must match X values length.

### PieChartData

```python
class PieChartData(BaseModel):
    labels: List[str]  # Slice labels
    values: List[Union[int, float]]  # Slice values
```

**Validation**: 
- Values length must match labels length
- All values must be non-negative

### ComparisonTableData

```python
class ComparisonTableData(BaseModel):
    headers: List[str]  # Column headers
    rows: List[List[Any]]  # Table rows
```

**Validation**: All rows must have same length as headers.

### MultiSeriesData

```python
class MultiSeriesData(BaseModel):
    categories: List[str]  # Category labels
    series: List[Dict[str, Any]]  # Data series
```

**Series format**:
```python
{
    "label": "Series Name",
    "values": [1, 2, 3, ...]
}
```

**Validation**: All series values must match categories length.

## ChartRequest

Complete chart specification:

```python
class ChartRequest(BaseModel):
    id: str  # Unique chart ID
    title: str  # Chart title
    type: Literal["bar", "line", "pie", "comparison_table", "grouped_bar", "stacked_bar"]
    data: Union[BarChartData, LineChartData, ...]  # Chart data
    
    # Optional
    x_label: Optional[str]  # X-axis label
    y_label: Optional[str]  # Y-axis label
    caption: Optional[str]  # Chart caption
    width: int = 10  # Figure width (inches)
    height: int = 6  # Figure height (inches)
    dpi: int = 150  # Resolution
```

## ChartResult

Result from chart generation:

```python
@dataclass
class ChartResult:
    id: str  # Chart ID
    title: str  # Chart title
    type: str  # Chart type
    file_path: str  # Output file path
    caption: str  # Generated caption
    metadata: Dict[str, Any]  # Additional metadata
```

**Metadata includes**:
- `width`: Figure width
- `height`: Figure height
- `dpi`: Resolution
- `data_points`: Number of data points

## Advanced Usage

### Batch Generation

Generate multiple charts efficiently:

```python
requests = [
    ChartRequest(id="chart1", ...),
    ChartRequest(id="chart2", ...),
    ChartRequest(id="chart3", ...)
]

results = builder.build_batch(requests)
```

### In-Memory Generation

Generate chart as bytes (no file):

```python
buffer = builder.to_bytes(request)
# buffer is BytesIO with PNG image
```

### Custom Output Directory

```python
builder = ChartBuilder(output_dir="custom/path/charts")
```

### Custom Styling

```python
request = ChartRequest(
    id="styled_chart",
    title="My Chart",
    type="bar",
    data=BarChartData(...),
    width=12,  # Wider chart
    height=8,  # Taller chart
    dpi=300,  # Higher resolution
    x_label="Custom X Label",
    y_label="Custom Y Label",
    caption="Custom caption text"
)
```

## JSON Input

Load charts from JSON file:

```json
{
  "charts": [
    {
      "id": "chart1",
      "title": "My Chart",
      "type": "bar",
      "data": {
        "categories": ["A", "B", "C"],
        "values": [10, 20, 30]
      },
      "x_label": "Category",
      "y_label": "Value"
    }
  ]
}
```

```python
import json
from source.charts import ChartBuilder, ChartRequest

# Load from JSON
with open('charts.json') as f:
    data = json.load(f)

requests = [ChartRequest(**chart) for chart in data['charts']]
results = builder.build_batch(requests)
```

## Integration with Report Generator

```python
from source.charts import ChartBuilder, ChartRequest, BarChartData

# Generate charts
builder = ChartBuilder(output_dir="output/charts")

chart_request = ChartRequest(
    id="algo_perf",
    title="Algorithm Performance",
    type="bar",
    data=BarChartData(
        categories=["BFS", "DFS", "A*"],
        values=[120, 95, 85]
    )
)

result = builder.build(chart_request)

# Use in report
# Add image to document: result.file_path
# Add caption: result.caption
```

## Error Handling

The module validates all input:

```python
try:
    request = ChartRequest(
        id="invalid",
        title="Test",
        type="bar",
        data=BarChartData(
            categories=["A", "B"],
            values=[1, 2, 3]  # Length mismatch!
        )
    )
except ValueError as e:
    print(f"Validation error: {e}")
```

## Examples

See comprehensive examples:
- `examples/chart_quick_demo.py` - Quick demonstration
- `examples/chart_builder_usage.py` - 8 detailed examples
- `examples/chart_from_json.py` - Load from JSON
- `examples/chart_input_example.json` - Example JSON input

Run examples:
```bash
python examples/chart_quick_demo.py
python examples/chart_builder_usage.py
python examples/chart_from_json.py
```

## Best Practices

1. **Use Descriptive IDs**: Chart IDs should be unique and descriptive
2. **Provide Captions**: Always include meaningful captions
3. **Validate Data**: Let Pydantic validate your data
4. **Batch When Possible**: Use `build_batch()` for multiple charts
5. **Choose Appropriate Types**: Match chart type to data
6. **Label Axes**: Always provide axis labels
7. **Consider Size**: Adjust width/height for readability

## Summary

The Chart Builder provides:
- ✅ Clean, validated input
- ✅ 6 chart types
- ✅ Automatic caption generation
- ✅ Batch processing
- ✅ Simple API
- ✅ Production-ready output

Replace mock data with real structured input for professional charts.
