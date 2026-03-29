# Review Engine Guide

Automated quality review for generated reports.

## Overview

The ReviewEngine validates report quality by running a series of checks and returning structured results with severity levels (error, warning, info).

## Quick Start

```python
from source.review import ReviewEngine, ReviewReport

# Create engine
engine = ReviewEngine()

# Review report
result = engine.review(report_data)

# Display results
print(ReviewReport.format_text(result))

# Check if passed
if result.passed:
    print("Report is ready!")
else:
    print(f"Found {result.errors} errors")
```

## Components

### 1. Review Models

**Severity Levels**:
- `ERROR` - Must be fixed
- `WARNING` - Should be reviewed
- `INFO` - Informational

**CheckType**:
- `STRUCTURE` - Document structure
- `CONTENT` - Content quality
- `FORMATTING` - Formatting issues
- `REFERENCES` - Reference problems
- `EVIDENCE` - Evidence issues

**ReviewIssue**:
```python
issue = ReviewIssue(
    check_type=CheckType.CONTENT,
    severity=Severity.ERROR,
    message="Section is empty",
    section_id="intro",
    section_title="Introduction",
    details={'length': 0}
)
```

**ReviewResult**:
```python
result = ReviewResult(
    passed=False,
    total_issues=5,
    errors=2,
    warnings=2,
    infos=1,
    issues=[...],
    metadata={...}
)
```

### 2. Built-in Checks

**RequiredSectionsCheck**:
- Validates required sections by report type
- Severity: ERROR
- Report types: thesis, technical_report, project_report, business_report

**HeadingNumberingCheck**:
- Checks chapter numbering consistency
- Severity: WARNING
- Validates "CHƯƠNG X" or "CHAPTER X" format

**MissingCaptionsCheck**:
- Checks for missing figure/table captions
- Severity: WARNING
- Validates all evidence items

**UnusedReferencesCheck**:
- Detects potentially unused references
- Severity: INFO
- Heuristic: checks for [1], (1) in text

**EmptySectionsCheck**:
- Finds empty or too-short sections
- Severity: ERROR (empty), WARNING (short)
- Minimum length: 50 characters

**DuplicateSectionsCheck**:
- Detects duplicate section titles
- Severity: WARNING
- Case-insensitive comparison

**ConclusionResultsMismatchCheck**:
- Checks if conclusion references results
- Severity: INFO
- Heuristic: word overlap analysis

### 3. Review Engine

```python
from source.review import ReviewEngine

# Default checks
engine = ReviewEngine()

# Custom checks
engine = ReviewEngine(checks=[
    RequiredSectionsCheck,
    EmptySectionsCheck
])

# Add check
engine.add_check(CustomCheck)

# Remove check
engine.remove_check(EmptySectionsCheck)

# List checks
print(engine.get_checks())

# Run review
result = engine.review(report_data)
```

### 4. Review Report

```python
from source.review import ReviewReport

# Text format
text = ReviewReport.format_text(result)
print(text)

# JSON format
json_data = ReviewReport.format_json(result)
```

## Usage Examples

### Example 1: Basic Review

```python
from source.review import ReviewEngine, ReviewReport

report_data = {
    'metadata': {
        'title': 'My Report',
        'report_type': 'project_report'
    },
    'sections': [
        {'type': 'cover', 'title': 'Cover'},
        {'type': 'chapter', 'title': 'Introduction', 'content': 'Text here'}
    ],
    'evidence': {'figures': [], 'tables': []}
}

engine = ReviewEngine()
result = engine.review(report_data)

print(result.summary())
# Output: Review FAILED: 3 issues (2 errors, 1 warnings, 0 infos)

print(ReviewReport.format_text(result))
```

### Example 2: Custom Check

```python
from source.review import BaseCheck, ReviewIssue, Severity, CheckType

class TitleLengthCheck(BaseCheck):
    """Check if title is appropriate length"""
    
    def check(self, report_data):
        issues = []
        title = report_data.get('metadata', {}).get('title', '')
        
        if len(title) < 10:
            issues.append(ReviewIssue(
                check_type=CheckType.CONTENT,
                severity=Severity.WARNING,
                message=f"Title too short: '{title}'",
                details={'length': len(title)}
            ))
        
        if len(title) > 200:
            issues.append(ReviewIssue(
                check_type=CheckType.CONTENT,
                severity=Severity.WARNING,
                message=f"Title too long: {len(title)} chars",
                details={'length': len(title)}
            ))
        
        return issues

# Use custom check
engine = ReviewEngine()
engine.add_check(TitleLengthCheck)
result = engine.review(report_data)
```

### Example 3: Integration with Pipeline

```python
from source.review import ReviewEngine, ReviewReport
from source.renderers import ReportRenderer

# Generate report data
report_data = {...}

# Review before rendering
engine = ReviewEngine()
result = engine.review(report_data)

if result.passed:
    # Render if passed
    renderer = ReportRenderer()
    renderer.render(report_data, 'output/report.docx')
    print("✓ Report rendered successfully")
else:
    # Show issues
    print(ReviewReport.format_text(result))
    print(f"✗ Fix {result.errors} errors before rendering")
```

### Example 4: Selective Checks

```python
from source.review import (
    ReviewEngine,
    RequiredSectionsCheck,
    EmptySectionsCheck,
    MissingCaptionsCheck
)

# Run only specific checks
engine = ReviewEngine(checks=[
    RequiredSectionsCheck,
    EmptySectionsCheck,
    MissingCaptionsCheck
])

result = engine.review(report_data)
```

## Review Result API

### ReviewResult Methods

```python
# Get issues by severity
errors = result.get_issues_by_severity(Severity.ERROR)
warnings = result.get_issues_by_severity(Severity.WARNING)
infos = result.get_issues_by_severity(Severity.INFO)

# Get issues by type
structure_issues = result.get_issues_by_type(CheckType.STRUCTURE)
content_issues = result.get_issues_by_type(CheckType.CONTENT)

# Summary
print(result.summary())

# Convert to dict
data = result.to_dict()
```

### ReviewIssue Properties

```python
issue.check_type      # CheckType enum
issue.severity        # Severity enum
issue.message         # Human-readable message
issue.section_id      # Section ID (optional)
issue.section_title   # Section title (optional)
issue.details         # Additional details dict
```

## Extending the Engine

### Create Custom Check

```python
from source.review import BaseCheck, ReviewIssue, Severity, CheckType

class MyCustomCheck(BaseCheck):
    """Description of what this check does"""
    
    def check(self, report_data):
        """
        Run check on report data
        
        Args:
            report_data: Report data dictionary
            
        Returns:
            List of ReviewIssue objects
        """
        issues = []
        
        # Your check logic here
        sections = report_data.get('sections', [])
        for section in sections:
            # Check something
            if condition:
                issues.append(ReviewIssue(
                    check_type=CheckType.CONTENT,
                    severity=Severity.WARNING,
                    message="Issue description",
                    section_title=section.get('title'),
                    details={'key': 'value'}
                ))
        
        return issues
```

### Register Custom Check

```python
# Method 1: At initialization
engine = ReviewEngine(checks=[
    RequiredSectionsCheck,
    MyCustomCheck
])

# Method 2: Add later
engine = ReviewEngine()
engine.add_check(MyCustomCheck)
```

## Check Guidelines

When creating custom checks:

1. **Inherit from BaseCheck**
2. **Implement check() method**
3. **Return List[ReviewIssue]**
4. **Choose appropriate severity**:
   - ERROR: Must fix (blocks rendering)
   - WARNING: Should review (quality issue)
   - INFO: Informational (suggestion)
5. **Provide clear messages**
6. **Include helpful details**
7. **Keep checks focused** (single responsibility)

## Integration Patterns

### Pattern 1: Pre-Render Validation

```python
# Generate → Review → Render
report_data = generate_report()
result = engine.review(report_data)

if result.passed:
    render_report(report_data)
else:
    show_issues(result)
```

### Pattern 2: Continuous Validation

```python
# Review during generation
for section in sections:
    report_data['sections'].append(section)
    result = engine.review(report_data)
    if not result.passed:
        fix_issues(result)
```

### Pattern 3: Quality Gate

```python
# Block rendering on errors
result = engine.review(report_data)

if result.errors > 0:
    raise ValueError(f"Report has {result.errors} errors")

if result.warnings > 5:
    print(f"Warning: {result.warnings} quality issues")

render_report(report_data)
```

## Output Formats

### Text Format

```
============================================================
REPORT REVIEW RESULTS
============================================================

Review FAILED: 5 issues (2 errors, 2 warnings, 1 infos)

Report Information:
  report_title: My Report
  report_type: project_report
  checks_run: 7

ERRORS (2):
------------------------------------------------------------
  ✗ Missing required section: toc
    Details: {'required_type': 'toc'}

  ✗ Section 'Chapter 1' is empty
    Section: Chapter 1
    Details: {'section_type': 'chapter'}

WARNINGS (2):
------------------------------------------------------------
  ⚠ Figure 1 is missing a caption
    Details: {'figure_index': 0}

  ⚠ Section 'Intro' has very short content (25 chars)
    Section: Intro
    Details: {'content_length': 25}

INFO (1):
------------------------------------------------------------
  ℹ Reference 1 may be unused
    Details: {'reference': 'Smith et al. (2020)'}

============================================================
```

### JSON Format

```json
{
  "passed": false,
  "total_issues": 5,
  "errors": 2,
  "warnings": 2,
  "infos": 1,
  "issues": [
    {
      "check_type": "structure",
      "severity": "error",
      "message": "Missing required section: toc",
      "section_id": null,
      "section_title": null,
      "details": {"required_type": "toc"}
    }
  ],
  "metadata": {
    "report_title": "My Report",
    "report_type": "project_report",
    "checks_run": 7
  }
}
```

## Best Practices

1. **Review Early**: Check during generation, not just at the end
2. **Fix Errors First**: Address errors before warnings
3. **Use Custom Checks**: Add domain-specific validation
4. **Log Results**: Save review results for tracking
5. **Automate**: Integrate into CI/CD pipeline
6. **Iterate**: Review → Fix → Review again

## Examples

Run examples:
```bash
python examples/review_engine_demo.py
python examples/review_integration_demo.py
```

## API Reference

### ReviewEngine

```python
ReviewEngine(checks: List[Type[BaseCheck]] = None)
    .review(report_data: Dict[str, Any]) -> ReviewResult
    .add_check(check_class: Type[BaseCheck])
    .remove_check(check_class: Type[BaseCheck])
    .get_checks() -> List[str]
```

### ReviewReport

```python
ReviewReport.format_text(result: ReviewResult) -> str
ReviewReport.format_json(result: ReviewResult) -> Dict[str, Any]
```

### ReviewResult

```python
ReviewResult(passed, total_issues, errors, warnings, infos)
    .add_issue(issue: ReviewIssue)
    .get_issues_by_severity(severity: Severity) -> List[ReviewIssue]
    .get_issues_by_type(check_type: CheckType) -> List[ReviewIssue]
    .summary() -> str
    .to_dict() -> Dict[str, Any]
```

## Summary

The ReviewEngine provides:
- ✅ Structured review results
- ✅ Severity levels (error, warning, info)
- ✅ Easy to extend with custom checks
- ✅ 7 built-in checks
- ✅ Multiple output formats
- ✅ Pipeline integration

Perfect for ensuring report quality before rendering.
