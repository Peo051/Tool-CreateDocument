# Sample Review Result

## Overview

This document shows a sample review result from the ReviewEngine.

## Review Summary

```
Review FAILED: 9 issues (2 errors, 5 warnings, 2 infos)
```

## Issues by Severity

### ERRORS (2)

Critical issues that must be fixed before rendering:

1. **Missing required section: toc**
   - Check Type: structure
   - Details: Required for project_report type
   - Action: Add table of contents section

2. **Missing required section: conclusion**
   - Check Type: structure
   - Details: Required for project_report type
   - Action: Add conclusion section

### WARNINGS (5)

Issues that should be addressed but don't block rendering:

1. **Subsection may be missing numbering: Performance**
   - Check Type: formatting
   - Section: Performance
   - Expected: 2.1
   - Action: Add section numbering

2. **Figure 1 is missing caption**
   - Check Type: evidence
   - Details: Figure at path 'chart.png'
   - Action: Add descriptive caption

3. **Section 'INTRODUCTION' has insufficient content**
   - Check Type: content
   - Content Length: 12 characters
   - Minimum: 50 characters
   - Action: Expand section content

4. **Subsection 'Performance' has insufficient content**
   - Check Type: content
   - Content Length: 25 characters
   - Action: Add more detailed content

5. **Section 'REFERENCES' has insufficient content**
   - Check Type: content
   - Action: Ensure references section has proper content

### INFO (2)

Informational messages for awareness:

1. **Reference [1] may be unused**
   - Check Type: references
   - Reference: "Smith, J. (2020). Paper Title."
   - Action: Verify reference is cited in text

2. **Reference [2] may be unused**
   - Check Type: references
   - Reference: "Jones, A. (2021). Another Paper."
   - Action: Verify reference is cited in text

## JSON Format

```json
{
  "passed": false,
  "total_issues": 9,
  "errors": 2,
  "warnings": 5,
  "infos": 2,
  "issues": [
    {
      "check_type": "structure",
      "severity": "error",
      "message": "Missing required section: toc",
      "section_id": null,
      "section_title": null,
      "details": {
        "required_type": "toc",
        "report_type": "project_report"
      }
    },
    {
      "check_type": "structure",
      "severity": "error",
      "message": "Missing required section: conclusion",
      "section_id": null,
      "section_title": null,
      "details": {
        "required_type": "conclusion",
        "report_type": "project_report"
      }
    },
    {
      "check_type": "formatting",
      "severity": "warning",
      "message": "Subsection may be missing numbering: Performance",
      "section_id": "results_perf",
      "section_title": "Performance",
      "details": {
        "expected_number": "2.1"
      }
    },
    {
      "check_type": "evidence",
      "severity": "warning",
      "message": "Figure 1 is missing caption",
      "section_id": null,
      "section_title": null,
      "details": {
        "figure_index": 1,
        "path": "chart.png"
      }
    },
    {
      "check_type": "content",
      "severity": "warning",
      "message": "Section 'INTRODUCTION' has insufficient content",
      "section_id": null,
      "section_title": "INTRODUCTION",
      "details": {
        "content_length": 12
      }
    },
    {
      "check_type": "content",
      "severity": "warning",
      "message": "Subsection 'Performance' has insufficient content",
      "section_id": "results_perf",
      "section_title": "Performance",
      "details": {
        "content_length": 25
      }
    },
    {
      "check_type": "content",
      "severity": "warning",
      "message": "Section 'REFERENCES' has insufficient content",
      "section_id": null,
      "section_title": "REFERENCES",
      "details": {
        "content_length": 0
      }
    },
    {
      "check_type": "references",
      "severity": "info",
      "message": "Reference [1] may be unused",
      "section_id": null,
      "section_title": null,
      "details": {
        "reference": "Smith, J. (2020). Paper Title."
      }
    },
    {
      "check_type": "references",
      "severity": "info",
      "message": "Reference [2] may be unused",
      "section_id": null,
      "section_title": null,
      "details": {
        "reference": "Jones, A. (2021). Another Paper."
      }
    }
  ],
  "metadata": {
    "checks_run": 7,
    "report_type": "project_report"
  }
}
```

## Recommended Actions

### Priority 1 (Errors - Must Fix)
1. Add table of contents section
2. Add conclusion section

### Priority 2 (Warnings - Should Fix)
1. Add section numbering to subsections
2. Add captions to all figures and tables
3. Expand content in short sections (minimum 50 characters)

### Priority 3 (Info - Nice to Have)
1. Verify all references are cited in text
2. Remove unused references or add citations

## After Fixes

Once all errors are fixed, the report can be rendered. Warnings and info messages are non-blocking but should be addressed for better quality.

Expected result after fixes:
```
Review PASSED: 0 issues (0 errors, 0 warnings, 0 infos)
✓ Report is ready to render
```
