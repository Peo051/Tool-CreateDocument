# OutlinePlanner

Generate structured report outlines by type with support for customization.

## Features

✅ 4 report types: thesis, technical_report, project_report, business_report  
✅ Default outlines for each type  
✅ User override with custom sections  
✅ Structured dataclass objects  
✅ Simple and testable  

## Usage

```python
from outline_planner import OutlinePlanner

planner = OutlinePlanner()

# Basic usage
outline = planner.plan('thesis')

# With config
config = {'algorithms': ['DFS', 'BFS', 'A*']}
outline = planner.plan('project_report', config)

# Custom sections
config = {
    'custom_sections': [{
        'id': 'security',
        'title': 'Security Analysis',
        'level': 1,
        'position': 5
    }]
}
outline = planner.plan('technical_report', config)

# Export to dict
data = outline.to_dict()
```

## Report Types

### Thesis
- Cover, Abstract, Acknowledgment, TOC
- 6 Chapters (Intro, Lit Review, Methodology, Results, Discussion, Conclusion)
- References, Appendices

### Technical Report
- Cover, Executive Summary, TOC
- Introduction, Technical Background, Implementation, Results, Conclusion
- References

### Project Report
- Cover, Acknowledgment, Commitment, TOC
- Introduction, System Overview, Algorithms, Implementation, Results, Conclusion
- References

### Business Report
- Cover, Executive Summary, TOC
- Introduction, Market Analysis, Strategy, Financial Analysis, Recommendations, Conclusion
- Appendices

## Models

```python
@dataclass
class OutlineSection:
    id: str
    title: str
    level: int = 1
    subsections: List['OutlineSection'] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ReportOutline:
    report_type: ReportType
    sections: List[OutlineSection] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
```

## Examples

See `examples/quick_outline_demo.py` for quick demo.  
See `examples/outline_planner_usage.py` for comprehensive examples.

## Tests

```bash
python tests/test_outline_planner.py
```

All 9 tests pass ✅
