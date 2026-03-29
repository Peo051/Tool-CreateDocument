"""
Experiments Section Generator
"""

from typing import Dict, Any, List
from .base import SectionGenerator, GeneratedSection, Subsection


class ExperimentsGenerator(SectionGenerator):
    """Generate experiments section"""
    
    def generate(self, input_data: Dict[str, Any]) -> GeneratedSection:
        """
        Generate experiments section
        
        Expected input_data:
        - overview: Experiments overview
        - setup: Experimental setup
        - datasets: Datasets used
        - metrics: Evaluation metrics
        - experiments: List of experiments
        - parameters: Parameters tested
        - environment: Testing environment
        """
        overview = input_data.get('overview', '')
        setup = input_data.get('setup', '')
        datasets = input_data.get('datasets', [])
        metrics = input_data.get('metrics', [])
        experiments = input_data.get('experiments', [])
        parameters = input_data.get('parameters', {})
        environment = input_data.get('environment', {})
        
        # Main content
        if overview:
            content = overview
        else:
            content = (
                "This section describes the experiments conducted to evaluate "
                "the system, including setup, datasets, metrics, and results."
            )
        
        # Generate subsections
        subsections = []
        
        # Experimental Setup
        if setup:
            subsections.append(Subsection(
                title="Experimental Setup",
                content=setup,
                level=2
            ))
        
        # Environment
        if environment:
            env_content = self._build_environment_content(environment)
            
            subsections.append(Subsection(
                title="Testing Environment",
                content=env_content,
                level=2
            ))
        
        # Datasets
        if datasets:
            datasets_content = self._build_datasets_content(datasets)
            
            subsections.append(Subsection(
                title="Datasets",
                content=datasets_content,
                level=2
            ))
        
        # Metrics
        if metrics:
            metrics_content = "The following metrics were used:\n\n"
            metrics_content += self._build_metrics_content(metrics)
            
            subsections.append(Subsection(
                title="Evaluation Metrics",
                content=metrics_content,
                level=2
            ))
        
        # Parameters
        if parameters:
            params_content = self._build_parameters_content(parameters)
            
            subsections.append(Subsection(
                title="Parameters",
                content=params_content,
                level=2
            ))
        
        # Experiments
        if experiments:
            for i, exp in enumerate(experiments, 1):
                exp_content = self._build_experiment_content(exp)
                
                exp_title = exp.get('name', f'Experiment {i}') if isinstance(exp, dict) else f'Experiment {i}'
                
                subsections.append(Subsection(
                    title=exp_title,
                    content=exp_content,
                    level=2
                ))
        
        return GeneratedSection(
            title="Experiments",
            content=content,
            subsections=subsections,
            metadata={
                'experiments_count': len(experiments),
                'metrics_count': len(metrics)
            }
        )
    
    def _build_environment_content(self, environment: Dict[str, Any]) -> str:
        """Build content for testing environment"""
        parts = []
        
        if 'hardware' in environment:
            parts.append(f"**Hardware**: {environment['hardware']}")
        
        if 'software' in environment:
            parts.append(f"**Software**: {environment['software']}")
        
        if 'os' in environment:
            parts.append(f"**Operating System**: {environment['os']}")
        
        for key, value in environment.items():
            if key not in ['hardware', 'software', 'os']:
                parts.append(f"**{key.replace('_', ' ').title()}**: {value}")
        
        return "\n\n".join(parts) if parts else "Standard testing environment was used."
    
    def _build_datasets_content(self, datasets: List[Any]) -> str:
        """Build content for datasets"""
        content_parts = []
        
        for dataset in datasets:
            if isinstance(dataset, dict):
                name = dataset.get('name', '')
                description = dataset.get('description', '')
                size = dataset.get('size', '')
                source = dataset.get('source', '')
                
                part = f"**{name}**"
                if description:
                    part += f"\n\n{description}"
                if size:
                    part += f"\n\nSize: {size}"
                if source:
                    part += f"\n\nSource: {source}"
                
                content_parts.append(part)
            else:
                content_parts.append(f"- {dataset}")
        
        return "\n\n".join(content_parts)
    
    def _build_metrics_content(self, metrics: List[Any]) -> str:
        """Build content for metrics"""
        content_parts = []
        
        for metric in metrics:
            if isinstance(metric, dict):
                name = metric.get('name', '')
                description = metric.get('description', '')
                formula = metric.get('formula', '')
                
                part = f"**{name}**"
                if description:
                    part += f": {description}"
                if formula:
                    part += f"\n\nFormula: {formula}"
                
                content_parts.append(part)
            else:
                content_parts.append(f"- {metric}")
        
        return "\n\n".join(content_parts)
    
    def _build_parameters_content(self, parameters: Dict[str, Any]) -> str:
        """Build content for parameters"""
        parts = []
        
        for key, value in parameters.items():
            param_name = key.replace('_', ' ').title()
            parts.append(f"**{param_name}**: {value}")
        
        return "\n\n".join(parts)
    
    def _build_experiment_content(self, experiment: Any) -> str:
        """Build content for a single experiment"""
        if isinstance(experiment, dict):
            parts = []
            
            if 'description' in experiment:
                parts.append(experiment['description'])
            
            if 'hypothesis' in experiment:
                parts.append(f"**Hypothesis**: {experiment['hypothesis']}")
            
            if 'procedure' in experiment:
                parts.append(f"**Procedure**: {experiment['procedure']}")
            
            if 'results' in experiment:
                parts.append(f"**Results**: {experiment['results']}")
            
            return "\n\n".join(parts)
        else:
            return str(experiment)
