"""
Results Analysis Section Generator
"""

from typing import Dict, Any, List
from .base import SectionGenerator, GeneratedSection, Subsection


class ResultsAnalysisGenerator(SectionGenerator):
    """Generate results analysis section"""
    
    def generate(self, input_data: Dict[str, Any]) -> GeneratedSection:
        """
        Generate results analysis section
        
        Expected input_data:
        - overview: Results overview
        - findings: Key findings
        - performance: Performance results
        - comparisons: Comparisons with baselines
        - visualizations: Charts/graphs descriptions
        - discussion: Discussion of results
        - limitations: Limitations of results
        """
        overview = input_data.get('overview', '')
        findings = input_data.get('findings', [])
        performance = input_data.get('performance', {})
        comparisons = input_data.get('comparisons', [])
        visualizations = input_data.get('visualizations', [])
        discussion = input_data.get('discussion', '')
        limitations = input_data.get('limitations', [])
        
        # Main content
        if overview:
            content = overview
        else:
            content = (
                "This section presents and analyzes the results obtained from "
                "the experiments, including performance metrics, comparisons, and key findings."
            )
        
        # Generate subsections
        subsections = []
        
        # Key Findings
        if findings:
            findings_content = "The main findings are:\n\n"
            findings_content += self._format_numbered_list(findings)
            
            subsections.append(Subsection(
                title="Key Findings",
                content=findings_content,
                level=2
            ))
        
        # Performance Results
        if performance:
            perf_content = self._build_performance_content(performance)
            
            subsections.append(Subsection(
                title="Performance Results",
                content=perf_content,
                level=2
            ))
        
        # Comparisons
        if comparisons:
            comp_content = self._build_comparisons_content(comparisons)
            
            subsections.append(Subsection(
                title="Comparative Analysis",
                content=comp_content,
                level=2
            ))
        
        # Visualizations
        if visualizations:
            viz_content = self._build_visualizations_content(visualizations)
            
            subsections.append(Subsection(
                title="Visualizations",
                content=viz_content,
                level=2
            ))
        
        # Discussion
        if discussion:
            subsections.append(Subsection(
                title="Discussion",
                content=discussion,
                level=2
            ))
        
        # Limitations
        if limitations:
            lim_content = "The following limitations were identified:\n\n"
            lim_content += self._format_list(limitations)
            
            subsections.append(Subsection(
                title="Limitations",
                content=lim_content,
                level=2
            ))
        
        return GeneratedSection(
            title="Results and Analysis",
            content=content,
            subsections=subsections,
            metadata={
                'findings_count': len(findings),
                'comparisons_count': len(comparisons)
            }
        )
    
    def _build_performance_content(self, performance: Dict[str, Any]) -> str:
        """Build content for performance results"""
        parts = []
        
        for metric, value in performance.items():
            metric_name = metric.replace('_', ' ').title()
            
            if isinstance(value, dict):
                # Detailed metric with multiple values
                part = f"**{metric_name}**\n"
                for key, val in value.items():
                    part += f"\n- {key.replace('_', ' ').title()}: {val}"
                parts.append(part)
            else:
                # Simple metric
                parts.append(f"**{metric_name}**: {value}")
        
        return "\n\n".join(parts)
    
    def _build_comparisons_content(self, comparisons: List[Any]) -> str:
        """Build content for comparisons"""
        content_parts = []
        
        for comparison in comparisons:
            if isinstance(comparison, dict):
                baseline = comparison.get('baseline', '')
                our_approach = comparison.get('our_approach', '')
                metric = comparison.get('metric', '')
                improvement = comparison.get('improvement', '')
                
                part = f"**Comparison with {baseline}**\n"
                
                if metric:
                    part += f"\nMetric: {metric}"
                
                if our_approach:
                    part += f"\nOur approach: {our_approach}"
                
                if improvement:
                    part += f"\nImprovement: {improvement}"
                
                content_parts.append(part)
            else:
                content_parts.append(f"- {comparison}")
        
        return "\n\n".join(content_parts)
    
    def _build_visualizations_content(self, visualizations: List[Any]) -> str:
        """Build content for visualizations"""
        content_parts = []
        
        for viz in visualizations:
            if isinstance(viz, dict):
                title = viz.get('title', '')
                description = viz.get('description', '')
                figure_ref = viz.get('figure_ref', '')
                
                part = f"**{title}**"
                
                if figure_ref:
                    part += f" (Figure {figure_ref})"
                
                if description:
                    part += f"\n\n{description}"
                
                content_parts.append(part)
            else:
                content_parts.append(f"- {viz}")
        
        return "\n\n".join(content_parts)
