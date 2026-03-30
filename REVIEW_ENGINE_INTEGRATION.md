# Review Engine Integration

## Summary

The review engine has been successfully integrated into the main report generation pipeline. It now runs automatically after rendering and provides structured quality checks.

## Changes Made

### 1. Modified `source/orchestrator.py`

- Added imports for `ReviewEngine`, `ReviewReport`, and `Severity`
- Enhanced `step_review_output()` to run the review engine
- Added `_report_to_review_data()` helper method to convert Report objects to review-compatible format
- Added Windows console encoding fallback for emoji display
- Review now fails pipeline on critical errors (errors > 0)
- Warnings and info messages are non-blocking

### 2. Created `examples/review_integration.py`

- Demonstrates automatic review integration
- Shows how review results are displayed in the pipeline output

## How It Works

1. After rendering the DOCX file, the orchestrator converts the Report object to a dict format
2. ReviewEngine runs all configured checks (7 by default)
3. Results are formatted and displayed with severity levels:
   - **ERROR**: Critical issues that fail the pipeline
   - **WARNING**: Non-critical issues that don't block generation
   - **INFO**: Informational messages

4. Pipeline fails if any errors are found, continues if only warnings/info

## Review Checks

The following checks run automatically:

1. **RequiredSectionsCheck**: Ensures all required sections exist
2. **HeadingNumberingCheck**: Validates heading numbering consistency
3. **MissingCaptionsCheck**: Checks for figures/tables without captions
4. **UnusedReferencesCheck**: Identifies potentially unused references
5. **EmptySectionsCheck**: Detects sections with no content
6. **DuplicateSectionsCheck**: Finds duplicate section titles
7. **ConclusionResultsMismatchCheck**: Validates conclusion/results alignment

## Example Output

```
🔍 Reviewing generated report...

============================================================
REPORT REVIEW RESULTS
============================================================

Review PASSED: 2 issues (0 errors, 0 warnings, 2 infos)

Report Information:
  report_title: Test Project
  report_type: project_report
  checks_run: 7

INFO (2):
------------------------------------------------------------
  ℹ Reference 1 may be unused
    Details: {'reference': '[3] Stuart Russell...', 'index': 1}
  ℹ Reference 2 may be unused
    Details: {'reference': '[4] Thomas H. Cormen...', 'index': 2}
============================================================
   ✅ Review passed (83.2 KB, 0.00s)
```

## Testing

All tests pass:
- 3 integration tests (test_integration.py)
- 7 review engine tests (test_review_engine.py)
- Total: 10/10 passing

## Usage

No changes needed - review runs automatically:

```python
from source.orchestrator import ReportOrchestrator

orchestrator = ReportOrchestrator('config.json', verbose=True)
success = orchestrator.execute('output.docx')
# Review runs automatically before returning
```

## Configuration

Review checks are currently hardcoded in `ReviewEngine.DEFAULT_CHECKS`. Future enhancement could allow configuration via config file.

## Notes

- Review errors fail the pipeline (return False)
- Review warnings/info are displayed but don't block generation
- Windows console encoding issues are handled with ASCII fallback
- Review data conversion handles both dict and list evidence formats for backward compatibility
