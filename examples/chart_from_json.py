"""
Load and Generate Charts from JSON Input
"""

import sys
import os
import json
sys.path.insert(0, os.path.abspath('.'))

from source.charts import ChartBuilder, ChartRequest


def load_charts_from_json(json_file: str):
    """Load chart requests from JSON file"""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    requests = []
    for chart_data in data.get('charts', []):
        try:
            request = ChartRequest(**chart_data)
            requests.append(request)
        except Exception as e:
            print(f"⚠️  Error loading chart {chart_data.get('id', 'unknown')}: {e}")
    
    return requests


def main():
    print("Chart Generation from JSON Input")
    print("=" * 60)
    
    # Load chart requests from JSON
    json_file = "examples/chart_input_example.json"
    
    if not os.path.exists(json_file):
        print(f"❌ File not found: {json_file}")
        return
    
    print(f"Loading charts from: {json_file}")
    requests = load_charts_from_json(json_file)
    print(f"✓ Loaded {len(requests)} chart requests")
    print()
    
    # Build all charts
    builder = ChartBuilder(output_dir="output/charts")
    results = builder.build_batch(requests)
    
    print(f"✓ Generated {len(results)} charts:")
    print()
    
    for result in results:
        print(f"Chart: {result.id}")
        print(f"  Title: {result.title}")
        print(f"  Type: {result.type}")
        print(f"  File: {result.file_path}")
        print(f"  Caption: {result.caption}")
        print(f"  Data points: {result.metadata['data_points']}")
        print()
    
    print("=" * 60)
    print("All charts generated successfully!")
    print("Check output/charts/ directory")


if __name__ == '__main__':
    main()
