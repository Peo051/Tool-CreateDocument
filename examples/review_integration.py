#!/usr/bin/env python3
"""
Example: Review Engine Integration
Demonstrates how the review engine is automatically integrated into the pipeline
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

from orchestrator import ReportOrchestrator

def main():
    """Run report generation with automatic review"""
    
    # Use an existing config
    config_path = os.path.join(os.path.dirname(__file__), 'config_minimal.json')
    output_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'reviewed_report.docx')
    
    print("=" * 60)
    print("Review Engine Integration Example")
    print("=" * 60)
    print()
    print("The review engine is automatically integrated into the")
    print("report generation pipeline. It runs after rendering and")
    print("checks for:")
    print("  - Required sections")
    print("  - Empty sections")
    print("  - Missing captions")
    print("  - Unused references")
    print("  - Heading numbering")
    print("  - Duplicate sections")
    print()
    print("Starting pipeline...")
    print()
    
    # Create orchestrator and run
    orchestrator = ReportOrchestrator(config_path, verbose=True)
    success = orchestrator.execute(output_path)
    
    if success:
        print()
        print("=" * 60)
        print("[OK] Report generated successfully with review!")
        print(f"Output: {output_path}")
        print("=" * 60)
    else:
        print()
        print("=" * 60)
        print("[X] Pipeline failed - check review results above")
        print("=" * 60)
    
    return 0 if success else 1

if __name__ == '__main__':
    sys.exit(main())
