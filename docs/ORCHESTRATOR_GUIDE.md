# Orchestrator Architecture Guide

This guide explains the refactored orchestration layer for the report generation pipeline.

## Overview

The report generator has been refactored into a clean orchestration pattern that separates concerns and provides better visibility into the generation process.

## Architecture

### Components

```
source/
├── main.py                 # CLI entry point (uses orchestrator)
├── orchestrator.py         # Core orchestration logic
├── config_models.py        # Pydantic configuration models
├── pipeline/               # Pipeline stages
│   ├── validator.py        # Config validation
│   ├── planner.py          # Outline planning
│   ├── generator.py        # Content generation
│   ├── binder.py           # Evidence binding
│   └── renderer.py         # Output rendering
├── models/                 # Data models
├── content/                # Content generators
└── renderers/              # Output renderers
```

### Pipeline Steps

The orchestrator executes 7 distinct steps:

1. **Load Config** 📖 - Load configuration from JSON file
2. **Validate Config** ✔️ - Validate with Pydantic models
3. **Plan Outline** 📋 - Create report structure
4. **Generate Content** ✍️ - Generate section content
5. **Bind Evidence** 📊 - Attach diagrams and evidence
6. **Render Output** 📄 - Create DOCX file
7. **Review Output** 🔍 - Validate generated file

## Usage

### Basic Usage

```bash
# Generate report with default config
python source/main.py

# Use custom config
python source/main.py --config my_config.json

# Specify output path
python source/main.py --output reports/my_report.docx

# Quiet mode (minimal output)
python source/main.py --quiet
```

### Advanced Usage

```bash
# Use new Pydantic config format
python source/main.py --config examples/config_full.json

# Generate multiple reports
python source/main.py --config config1.json --output report1.docx
python source/main.py --config config2.json --output report2.docx

# Batch processing
for config in configs/*.json; do
    python source/main.py --config "$config" --output "output/$(basename $config .json).docx"
done
```

## Orchestrator API

### ReportOrchestrator Class

```python
from orchestrator import ReportOrchestrator

# Create orchestrator
orchestrator = ReportOrchestrator(
    config_path='report_config.json',
    verbose=True  # Enable progress output
)

# Execute complete pipeline
success = orchestrator.execute(output_path='output/report.docx')

# Access generated report
report = orchestrator.get_report()

# Access validated config
config = orchestrator.get_config()
```

### Individual Steps

You can also execute steps individually:

```python
orchestrator = ReportOrchestrator('config.json')

# Execute steps one by one
orchestrator.step_load_config()
orchestrator.step_validate_config()
orchestrator.step_plan_outline()
orchestrator.step_generate_content()
orchestrator.step_bind_evidence()
orchestrator.step_render_output('output.docx')
orchestrator.step_review_output('output.docx')
```

### Progress Tracking

```python
from orchestrator import ProgressTracker

tracker = ProgressTracker()
tracker.start()

# Add and complete steps
step = tracker.add_step("My Step", "🔧", "Doing something")
# ... do work ...
tracker.complete_step(step, duration=1.5)

tracker.finish()
print(tracker.get_summary())
```

## Features

### 1. Clean Separation of Concerns

Each step is isolated and can be tested independently:

```python
# Test validation only
orchestrator = ReportOrchestrator('config.json')
orchestrator.step_load_config()
is_valid = orchestrator.step_validate_config()
```

### 2. Progress Tracking

Detailed progress information with timing:

```
1. ✅ 📖 Load Config (0.00s)
2. ✅ ✔️ Validate Config (0.00s)
3. ✅ 📋 Plan Outline (0.00s)
4. ✅ ✍️ Generate Content (0.00s)
5. ✅ 📊 Bind Evidence (2.40s)
6. ✅ 📄 Render Output (0.27s)
7. ✅ 🔍 Review Output (0.00s)
```

### 3. Error Handling

Clear error messages with step-level granularity:

```
❌ Validation failed: Missing required field: title
```

### 4. Execution Summary

Comprehensive summary after execution:

```
Pipeline Execution Summary
==========================
Total Steps: 7
Completed: 7
Failed: 0
Total Time: 2.70s
```

### 5. Quiet Mode

Minimal output for scripting:

```bash
python source/main.py --quiet
# Only shows errors, no progress
```

## Benefits

### Before (Old main.py)

```python
# Monolithic, hard to test
def generate_report():
    # Load config
    # Validate
    # Generate
    # Render
    # All in one function
```

Problems:
- Hard to test individual steps
- No progress visibility
- Difficult to debug
- Tight coupling

### After (Orchestrator)

```python
# Clean, testable steps
orchestrator.step_load_config()
orchestrator.step_validate_config()
orchestrator.step_plan_outline()
orchestrator.step_generate_content()
orchestrator.step_bind_evidence()
orchestrator.step_render_output()
orchestrator.step_review_output()
```

Benefits:
- ✅ Each step is testable
- ✅ Clear progress tracking
- ✅ Easy to debug
- ✅ Loose coupling
- ✅ Better error handling

## Extending the Orchestrator

### Add a New Step

```python
def step_custom_processing(self) -> bool:
    """Custom processing step"""
    step = self.tracker.add_step(
        "Custom Process",
        "🔧",
        "Doing custom processing"
    )
    
    start = datetime.now()
    
    try:
        self._log(f"{step.emoji} {step.description}...")
        
        # Your custom logic here
        
        duration = (datetime.now() - start).total_seconds()
        self.tracker.complete_step(step, duration)
        self._log(f"   ✅ Custom processing done ({duration:.2f}s)\n")
        return True
        
    except Exception as e:
        duration = (datetime.now() - start).total_seconds()
        self.tracker.fail_step(step, str(e))
        self._log(f"   ❌ Custom processing failed: {e}\n")
        return False
```

### Add to Pipeline

```python
def execute(self, output_path: str = 'output/report.docx') -> bool:
    steps = [
        lambda: self.step_load_config(),
        lambda: self.step_validate_config(),
        lambda: self.step_plan_outline(),
        lambda: self.step_generate_content(),
        lambda: self.step_custom_processing(),  # Add here
        lambda: self.step_bind_evidence(),
        lambda: self.step_render_output(output_path),
        lambda: self.step_review_output(output_path)
    ]
    
    for step_func in steps:
        if not step_func():
            return False
    
    return True
```

## Testing

### Unit Testing Steps

```python
import unittest
from orchestrator import ReportOrchestrator

class TestOrchestrator(unittest.TestCase):
    
    def test_load_config(self):
        orch = ReportOrchestrator('test_config.json')
        self.assertTrue(orch.step_load_config())
        self.assertIsNotNone(orch.config_dict)
    
    def test_validate_config(self):
        orch = ReportOrchestrator('test_config.json')
        orch.step_load_config()
        self.assertTrue(orch.step_validate_config())
        self.assertIsNotNone(orch.config_model)
```

### Integration Testing

```python
def test_full_pipeline():
    orch = ReportOrchestrator('test_config.json')
    success = orch.execute('test_output.docx')
    assert success
    assert os.path.exists('test_output.docx')
```

## Performance

### Timing Breakdown

Typical execution times:

- Load Config: < 0.01s
- Validate Config: < 0.01s
- Plan Outline: < 0.01s
- Generate Content: < 0.01s
- Bind Evidence: 2-3s (diagram generation)
- Render Output: 0.2-0.5s
- Review Output: < 0.01s

**Total: ~2-4 seconds**

### Optimization Tips

1. **Cache diagrams**: Reuse generated diagrams
2. **Parallel generation**: Generate sections in parallel
3. **Lazy loading**: Load content only when needed
4. **Incremental rendering**: Render sections as they're ready

## Troubleshooting

### Config Not Found

```
❌ Failed to load config: Config file not found: config.json
```

Solution: Check file path and ensure file exists

### Validation Failed

```
❌ Validation failed: Missing required field: title
```

Solution: Check config has all required fields

### Rendering Failed

```
❌ Rendering failed: Permission denied
```

Solution: Close the output file if it's open

### Output Too Small

```
❌ Review failed: Output file too small: 500 bytes
```

Solution: Check for errors in earlier steps

## Migration from Old Main

### Old Code

```python
pipeline = ReportPipeline(args.config)
output_file = pipeline.run(args.output)
```

### New Code

```python
orchestrator = ReportOrchestrator(args.config)
success = orchestrator.execute(args.output)
```

The API is similar but provides better error handling and progress tracking.

## Best Practices

1. **Always check return values**: Each step returns True/False
2. **Use verbose mode during development**: Helps debug issues
3. **Use quiet mode in production**: Cleaner output for logs
4. **Handle errors gracefully**: Check success before proceeding
5. **Test individual steps**: Don't just test the full pipeline

## Future Enhancements

Planned improvements:

- [ ] Parallel step execution where possible
- [ ] Step retry logic with exponential backoff
- [ ] Checkpoint/resume functionality
- [ ] Dry-run mode (validate without generating)
- [ ] Step profiling and optimization
- [ ] Custom step plugins
- [ ] Web API interface
- [ ] Real-time progress streaming

## Summary

The orchestrator pattern provides:

- ✅ Clean separation of concerns
- ✅ Better testability
- ✅ Clear progress tracking
- ✅ Improved error handling
- ✅ Easy extensibility
- ✅ Professional output

Use `python source/main.py --help` for all available options.
