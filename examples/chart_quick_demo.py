"""
Quick Chart Builder Demo
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from source.charts import ChartBuilder, ChartRequest, BarChartData, PieChartData


def main():
    print("Chart Builder Quick Demo")
    print("=" * 60)
    
    builder = ChartBuilder(output_dir="output/charts")
    
    # 1. Bar chart
    bar_request = ChartRequest(
        id="demo_bar",
        title="Algorithm Performance",
        type="bar",
        data=BarChartData(
            categories=["BFS", "DFS", "A*"],
            values=[120, 95, 85]
        ),
        y_label="Time (ms)"
    )
    
    bar_result = builder.build(bar_request)
    print(f"✓ Bar chart: {bar_result.file_path}")
    
    # 2. Pie chart
    pie_request = ChartRequest(
        id="demo_pie",
        title="Dataset Split",
        type="pie",
        data=PieChartData(
            labels=["Train", "Val", "Test"],
            values=[70, 15, 15]
        )
    )
    
    pie_result = builder.build(pie_request)
    print(f"✓ Pie chart: {pie_result.file_path}")
    
    print("\n" + "=" * 60)
    print("Demo completed! Check output/charts/ directory")


if __name__ == '__main__':
    main()
