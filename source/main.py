#!/usr/bin/env python3
"""
Report Generator - Main Entry Point
Clean orchestration layer with step-by-step execution
"""

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from orchestrator import ReportOrchestrator


def print_banner():
    """Print application banner"""
    banner = """
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║        📄 Professional Report Generator v2.0 📄          ║
║                                                          ║
║     Automated report generation with AI algorithms      ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
"""
    print(banner)


def main():
    """Main entry point"""
    
    parser = argparse.ArgumentParser(
        description='Professional Report Generator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate report with default config
  python main.py
  
  # Use custom config and output
  python main.py --config my_config.json --output reports/my_report.docx
  
  # Quiet mode (minimal output)
  python main.py --quiet
  
  # Use new Pydantic config format
  python main.py --config examples/config_full.json
        """
    )
    
    parser.add_argument(
        '--config',
        default='report_config.json',
        help='Configuration file path (default: report_config.json)'
    )
    
    parser.add_argument(
        '--output',
        default='output/report.docx',
        help='Output file path (default: output/report.docx)'
    )
    
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Quiet mode - minimal output'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='Report Generator v2.0'
    )
    
    args = parser.parse_args()
    
    # Print banner unless quiet
    if not args.quiet:
        print_banner()
    
    try:
        # Create orchestrator
        orchestrator = ReportOrchestrator(
            config_path=args.config,
            verbose=not args.quiet
        )
        
        # Execute pipeline
        success = orchestrator.execute(output_path=args.output)
        
        if success:
            if not args.quiet:
                print(f"\n✅ Success! Report saved to: {args.output}")
                print(f"\n💡 Open the file with Microsoft Word or LibreOffice\n")
            return 0
        else:
            if not args.quiet:
                print(f"\n❌ Failed to generate report")
                print(f"💡 Check the error messages above for details\n")
            return 1
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        return 130
        
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        
        if not args.quiet:
            import traceback
            print("\nFull traceback:")
            traceback.print_exc()
        
        return 1


if __name__ == '__main__':
    sys.exit(main())
