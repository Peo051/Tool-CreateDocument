"""
Chart Builder Usage Examples
Demonstrates how to generate charts from structured data
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from source.charts import (
    ChartBuilder,
    ChartRequest,
    BarChartData,
    LineChartData,
    PieChartData,
    ComparisonTableData,
    MultiSeriesData
)


def example_1_bar_chart():
    """Example 1: Simple bar chart"""
    print("=" * 60)
    print("Example 1: Bar Chart - Algorithm Performance")
    print("=" * 60)
    
    builder = ChartBuilder(output_dir="output/charts")
    
    request = ChartRequest(
        id="algo_performance",
        title="Algorithm Execution Time Comparison",
        type="bar",
        data=BarChartData(
            categories=["BFS", "DFS", "A*", "Dijkstra"],
            values=[120, 95, 85, 150],
            label="Execution Time (ms)"
        ),
        x_label="Algorithm",
        y_label="Time (ms)",
        caption="Comparison of search algorithm execution times on 1000-node graph"
    )
    
    result = builder.build(request)
    
    print(f"✓ Chart created: {result.file_path}")
    print(f"  Title: {result.title}")
    print(f"  Type: {result.type}")
    print(f"  Caption: {result.caption}")
    print(f"  Data points: {result.metadata['data_points']}")
    print()


def example_2_line_chart():
    """Example 2: Line chart"""
    print("=" * 60)
    print("Example 2: Line Chart - Training Progress")
    print("=" * 60)
    
    builder = ChartBuilder()
    
    request = ChartRequest(
        id="training_loss",
        title="Model Training Loss Over Epochs",
        type="line",
        data=LineChartData(
            x_values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            y_values=[0.95, 0.78, 0.65, 0.52, 0.45, 0.38, 0.32, 0.28, 0.25, 0.23],
            label="Training Loss"
        ),
        x_label="Epoch",
        y_label="Loss",
        caption="Training loss decreases over 10 epochs"
    )
    
    result = builder.build(request)
    
    print(f"✓ Chart created: {result.file_path}")
    print(f"  Caption: {result.caption}")
    print()


def example_3_pie_chart():
    """Example 3: Pie chart"""
    print("=" * 60)
    print("Example 3: Pie Chart - Dataset Distribution")
    print("=" * 60)
    
    builder = ChartBuilder()
    
    request = ChartRequest(
        id="dataset_split",
        title="Dataset Split Distribution",
        type="pie",
        data=PieChartData(
            labels=["Training", "Validation", "Testing"],
            values=[7000, 1500, 1500]
        ),
        caption="Dataset split: 70% training, 15% validation, 15% testing"
    )
    
    result = builder.build(request)
    
    print(f"✓ Chart created: {result.file_path}")
    print(f"  Caption: {result.caption}")
    print()


def example_4_comparison_table():
    """Example 4: Comparison table"""
    print("=" * 60)
    print("Example 4: Comparison Table - Algorithm Metrics")
    print("=" * 60)
    
    builder = ChartBuilder()
    
    request = ChartRequest(
        id="algo_comparison",
        title="Search Algorithm Comparison",
        type="comparison_table",
        data=ComparisonTableData(
            headers=["Algorithm", "Time (ms)", "Space (MB)", "Optimal", "Complete"],
            rows=[
                ["BFS", "120", "45", "Yes", "Yes"],
                ["DFS", "95", "30", "No", "No"],
                ["A*", "85", "50", "Yes", "Yes"],
                ["Dijkstra", "150", "55", "Yes", "Yes"]
            ]
        ),
        caption="Comparison of search algorithms on various metrics",
        width=12,
        height=4
    )
    
    result = builder.build(request)
    
    print(f"✓ Table created: {result.file_path}")
    print(f"  Caption: {result.caption}")
    print()


def example_5_grouped_bar():
    """Example 5: Grouped bar chart"""
    print("=" * 60)
    print("Example 5: Grouped Bar Chart - Multi-Dataset Performance")
    print("=" * 60)
    
    builder = ChartBuilder()
    
    request = ChartRequest(
        id="multi_dataset_perf",
        title="Algorithm Performance Across Datasets",
        type="grouped_bar",
        data=MultiSeriesData(
            categories=["Small", "Medium", "Large"],
            series=[
                {"label": "BFS", "values": [50, 120, 300]},
                {"label": "DFS", "values": [45, 95, 250]},
                {"label": "A*", "values": [40, 85, 220]}
            ]
        ),
        x_label="Dataset Size",
        y_label="Execution Time (ms)",
        caption="Performance comparison across different dataset sizes"
    )
    
    result = builder.build(request)
    
    print(f"✓ Chart created: {result.file_path}")
    print(f"  Caption: {result.caption}")
    print()


def example_6_stacked_bar():
    """Example 6: Stacked bar chart"""
    print("=" * 60)
    print("Example 6: Stacked Bar Chart - Resource Usage")
    print("=" * 60)
    
    builder = ChartBuilder()
    
    request = ChartRequest(
        id="resource_usage",
        title="System Resource Usage by Component",
        type="stacked_bar",
        data=MultiSeriesData(
            categories=["Preprocessing", "Training", "Evaluation"],
            series=[
                {"label": "CPU", "values": [30, 60, 20]},
                {"label": "Memory", "values": [20, 80, 30]},
                {"label": "Disk I/O", "values": [50, 40, 10]}
            ]
        ),
        x_label="Phase",
        y_label="Resource Usage (%)",
        caption="Breakdown of resource usage across pipeline phases"
    )
    
    result = builder.build(request)
    
    print(f"✓ Chart created: {result.file_path}")
    print(f"  Caption: {result.caption}")
    print()


def example_7_batch_generation():
    """Example 7: Batch chart generation"""
    print("=" * 60)
    print("Example 7: Batch Generation - Multiple Charts")
    print("=" * 60)
    
    builder = ChartBuilder()
    
    requests = [
        ChartRequest(
            id="accuracy_chart",
            title="Model Accuracy",
            type="bar",
            data=BarChartData(
                categories=["Model A", "Model B", "Model C"],
                values=[0.92, 0.88, 0.95]
            ),
            y_label="Accuracy"
        ),
        ChartRequest(
            id="precision_recall",
            title="Precision vs Recall",
            type="line",
            data=LineChartData(
                x_values=[0.5, 0.6, 0.7, 0.8, 0.9],
                y_values=[0.95, 0.92, 0.88, 0.82, 0.75],
                label="Precision"
            ),
            x_label="Recall",
            y_label="Precision"
        ),
        ChartRequest(
            id="class_distribution",
            title="Class Distribution",
            type="pie",
            data=PieChartData(
                labels=["Class A", "Class B", "Class C", "Class D"],
                values=[2500, 3000, 1500, 3000]
            )
        )
    ]
    
    results = builder.build_batch(requests)
    
    print(f"✓ Generated {len(results)} charts:")
    for result in results:
        print(f"  - {result.id}: {result.file_path}")
    print()


def example_8_real_experiment_data():
    """Example 8: Real experiment data"""
    print("=" * 60)
    print("Example 8: Real Experiment Data - Search Algorithm Study")
    print("=" * 60)
    
    builder = ChartBuilder()
    
    # Simulated real experiment results
    experiment_data = {
        'algorithms': ['BFS', 'DFS', 'A*', 'Dijkstra', 'Greedy'],
        'time_small': [45, 38, 35, 52, 30],
        'time_medium': [120, 95, 85, 150, 110],
        'time_large': [350, 280, 240, 420, 320],
        'memory': [45, 30, 50, 55, 35],
        'path_quality': [100, 75, 100, 100, 80]
    }
    
    # Chart 1: Execution time comparison
    time_request = ChartRequest(
        id="exp_execution_time",
        title="Execution Time Comparison (Medium Dataset)",
        type="bar",
        data=BarChartData(
            categories=experiment_data['algorithms'],
            values=experiment_data['time_medium']
        ),
        x_label="Algorithm",
        y_label="Time (ms)",
        caption="Execution time on 1000-node graph with 5000 edges"
    )
    
    # Chart 2: Memory usage
    memory_request = ChartRequest(
        id="exp_memory_usage",
        title="Memory Usage Comparison",
        type="bar",
        data=BarChartData(
            categories=experiment_data['algorithms'],
            values=experiment_data['memory']
        ),
        x_label="Algorithm",
        y_label="Memory (MB)",
        caption="Peak memory usage during execution"
    )
    
    # Chart 3: Scalability
    scalability_request = ChartRequest(
        id="exp_scalability",
        title="Algorithm Scalability",
        type="grouped_bar",
        data=MultiSeriesData(
            categories=experiment_data['algorithms'],
            series=[
                {"label": "Small (100 nodes)", "values": experiment_data['time_small']},
                {"label": "Medium (1000 nodes)", "values": experiment_data['time_medium']},
                {"label": "Large (10000 nodes)", "values": experiment_data['time_large']}
            ]
        ),
        x_label="Algorithm",
        y_label="Time (ms)",
        caption="Performance scaling with dataset size"
    )
    
    # Chart 4: Metrics table
    metrics_request = ChartRequest(
        id="exp_metrics_table",
        title="Algorithm Performance Metrics",
        type="comparison_table",
        data=ComparisonTableData(
            headers=["Algorithm", "Time (ms)", "Memory (MB)", "Path Quality (%)", "Optimal"],
            rows=[
                [algo, str(time), str(mem), str(qual), "Yes" if qual == 100 else "No"]
                for algo, time, mem, qual in zip(
                    experiment_data['algorithms'],
                    experiment_data['time_medium'],
                    experiment_data['memory'],
                    experiment_data['path_quality']
                )
            ]
        ),
        caption="Comprehensive performance metrics on medium dataset",
        width=14,
        height=5
    )
    
    results = builder.build_batch([
        time_request,
        memory_request,
        scalability_request,
        metrics_request
    ])
    
    print(f"✓ Generated {len(results)} experiment charts:")
    for result in results:
        print(f"  - {result.id}")
        print(f"    File: {result.file_path}")
        print(f"    Caption: {result.caption}")
    print()


if __name__ == '__main__':
    example_1_bar_chart()
    example_2_line_chart()
    example_3_pie_chart()
    example_4_comparison_table()
    example_5_grouped_bar()
    example_6_stacked_bar()
    example_7_batch_generation()
    example_8_real_experiment_data()
    
    print("=" * 60)
    print("All chart examples completed!")
    print("Check output/charts/ directory for generated images")
    print("=" * 60)
