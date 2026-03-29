#!/usr/bin/env python3
"""
Migration script to convert legacy config to new Pydantic format
"""

import json
import sys
import os
import argparse

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'source'))

from config_models import ReportConfig, save_config


def migrate_config(input_path: str, output_path: str = None):
    """
    Migrate legacy config to new format
    
    Args:
        input_path: Path to legacy config file
        output_path: Path to save new config (optional, defaults to input_path with .new.json)
    """
    
    # Load legacy config
    print(f"📖 Reading legacy config: {input_path}")
    with open(input_path, 'r', encoding='utf-8') as f:
        legacy_config = json.load(f)
    
    # Convert to new format
    print("🔄 Converting to new format...")
    try:
        new_config = ReportConfig.from_legacy_config(legacy_config)
        print("✅ Conversion successful!")
    except Exception as e:
        print(f"❌ Conversion failed: {e}")
        return False
    
    # Determine output path
    if output_path is None:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}.new{ext}"
    
    # Save new config
    print(f"💾 Saving new config: {output_path}")
    save_config(new_config, output_path)
    
    # Show summary
    print("\n" + "="*60)
    print("Migration Summary")
    print("="*60)
    print(f"Title: {new_config.project_info.title}")
    print(f"Type: {new_config.report_profile.report_type}")
    print(f"Authors: {len(new_config.project_info.students)}")
    print(f"Algorithms: {len(new_config.technical_data.algorithms)}")
    print(f"Technologies: {len(new_config.technical_data.technologies)}")
    print("="*60)
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description='Migrate legacy config to new Pydantic format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Migrate report_config.json to report_config.new.json
  python migrate_config.py report_config.json
  
  # Migrate with custom output path
  python migrate_config.py old_config.json new_config.json
  
  # Migrate all configs in a directory
  python migrate_config.py configs/*.json
        """
    )
    
    parser.add_argument('input', help='Input legacy config file')
    parser.add_argument('output', nargs='?', help='Output new config file (optional)')
    
    args = parser.parse_args()
    
    try:
        success = migrate_config(args.input, args.output)
        return 0 if success else 1
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    exit(main())
