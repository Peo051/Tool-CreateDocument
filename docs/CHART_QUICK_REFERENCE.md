# Chart Builder - Quick Reference

## Installation

```python
from source.charts import ChartBuilder, ChartRequest, BarChartData, LineChartData, PieChartData
```

## Basic Usage

```python
builder = ChartBuilder(output_dir="output/charts")

request = ChartRequest(
    id="my_chart",
    title="My Chart Title",
    type="bar",
    data=BarChartData(categories=["A", "B"], values=[10, 20])
)

result = builder.build(request)
print(result.file_path)  # output/charts/my_chart.png
```

## Chart Types

### Bar Chart
```python
ChartRequest(
    id="bar", type="bar",
    data=BarChartData(categories=["A", "B"], values=[10, 20])
)
```

### Line Chart
```python
ChartRequest(
    id="line", type="line",
    data=LineChartData(x_values=[1, 2, 3], y_values=[10, 20, 15])
)
```

### Pie Chart
```python
ChartRequest(
    id="pie", type="pie",
    data=PieChartData(labels=["A", "B"], values=[30, 70])
)
```

### Comparison Table
```python
ChartRequest(
    id="table", type="comparison_table",
    data=ComparisonTableData(
        headers=["Name", "Value"],
        rows=[["A", "10"], ["B", "20"]]
    )
)
```

### Grouped Bar
```python
ChartRequest(
    id="grouped", type="grouped_bar",
    data=MultiSeriesData(
        categories=["X", "Y"],
        series=[
            {"label": "S1", "values": [10, 20]},
            {"label": "S2", "values": [15, 25]}
        ]
    )
)
```

### Stacked Bar
```python
ChartRequest(
    id="stacked", type="stacked_bar",
    data=MultiSeriesData(
        categories=["X", "Y"],
        series=[
            {"label": "S1", "values": [10, 20]},
            {"label": "S2", "values": [15, 25]}
        ]
    )
)
```

## Batch Generation

```python
requests = [request1, request2, request3]
results = builder.build_batch(requests)
```

## From JSON

```python
import json

with open('charts.json') as f:
    data = json.load(f)

requests = [ChartRequest(**c) for c in data['charts']]
results = builder.build_batch(requests)
```

## Customization

```python
ChartRequest(
    id="custom",
    title="Title",
    type="bar",
    data=BarChartData(...),
    x_label="X Axis",
    y_label="Y Axis",
    caption="Custom caption",
    width=12,
    height=8,
    dpi=300
)
```

## Result

```python
result.id          # Chart ID
result.title       # Chart title
result.type        # Chart type
result.file_path   # File path
result.caption     # Caption
result.metadata    # Metadata dict
```

## Examples

```bash
python examples/chart_quick_demo.py
python examples/chart_builder_usage.py
python examples/chart_from_json.py
```

## Common Patterns

### Algorithm Performance
```python
ChartRequest(
    id="algo_perf",
    title="Algorithm Performance",
    type="bar",
    data=BarChartData(
        categories=["BFS", "DFS", "A*"],
        values=[120, 95, 85]
    ),
    y_label="Time (ms)"
)
```

### Training Progress
```python
ChartRequest(
    id="training",
    title="Training Loss",
    type="line",
    data=LineChartData(
        x_values=list(range(1, 11)),
        y_values=[0.9, 0.7, 0.5, 0.4, 0.3, 0.25, 0.2, 0.18, 0.15, 0.12]
    ),
    x_label="Epoch",
    y_label="Loss"
)
```

### Dataset Split
```python
ChartRequest(
    id="split",
    title="Dataset Split",
    type="pie",
    data=PieChartData(
        labels=["Train", "Val", "Test"],
        values=[70, 15, 15]
    )
)
```

## Validation

Data is automatically validated:
- ✅ Length matching (values vs categories)
- ✅ Non-negative values (pie charts)
- ✅ Row consistency (tables)
- ✅ Type safety (Pydantic)

## Error Handling

```python
try:
    request = ChartRequest(...)
    result = builder.build(request)
except ValueError as e:
    print(f"Validation error: {e}")
```

## Tips

1. Use descriptive IDs
2. Always provide axis labels
3. Include captions
4. Batch when possible
5. Validate data first
6. Choose appropriate chart type
