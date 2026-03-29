"""
Methodology Section Generator
"""

from typing import Dict, Any, List
from .base import SectionGenerator, GeneratedSection, Subsection


class MethodologyGenerator(SectionGenerator):
    """Generate methodology section"""
    
    def generate(self, input_data: Dict[str, Any]) -> GeneratedSection:
        """
        Generate methodology section
        
        Expected input_data:
        - approach: Overall approach description
        - methods: List of methods/techniques used
        - tools: Tools and technologies
        - algorithms: Algorithms used
        - data_collection: Data collection methods
        - analysis_methods: Analysis techniques
        - workflow: Development workflow
        """
        approach = input_data.get('approach', '')
        methods = input_data.get('methods', [])
        tools = input_data.get('tools', [])
        algorithms = input_data.get('algorithms', [])
        data_collection = input_data.get('data_collection', '')
        analysis_methods = input_data.get('analysis_methods', [])
        workflow = input_data.get('workflow', [])
        
        # Main content
        if approach:
            content = approach
        else:
            content = (
                "This section describes the methodology employed in this project, "
                "including the approaches, methods, tools, and techniques used."
            )
        
        # Generate subsections
        subsections = []
        
        # Approach
        if approach:
            subsections.append(Subsection(
                title="Approach",
                content=approach,
                level=2
            ))
        
        # Methods
        if methods:
            methods_content = "The following methods were employed:\n\n"
            methods_content += self._build_methods_content(methods)
            
            subsections.append(Subsection(
                title="Methods",
                content=methods_content,
                level=2
            ))
        
        # Tools and Technologies
        if tools:
            tools_content = self._build_tools_content(tools)
            
            subsections.append(Subsection(
                title="Tools and Technologies",
                content=tools_content,
                level=2
            ))
        
        # Algorithms
        if algorithms:
            algo_content = "The following algorithms were utilized:\n\n"
            algo_content += self._build_algorithms_content(algorithms)
            
            subsections.append(Subsection(
                title="Algorithms",
                content=algo_content,
                level=2
            ))
        
        # Data Collection
        if data_collection:
            subsections.append(Subsection(
                title="Data Collection",
                content=data_collection,
                level=2
            ))
        
        # Analysis Methods
        if analysis_methods:
            analysis_content = "Analysis was performed using:\n\n"
            analysis_content += self._format_list(analysis_methods)
            
            subsections.append(Subsection(
                title="Analysis Methods",
                content=analysis_content,
                level=2
            ))
        
        # Workflow
        if workflow:
            workflow_content = "The development workflow consisted of:\n\n"
            workflow_content += self._format_numbered_list(workflow)
            
            subsections.append(Subsection(
                title="Workflow",
                content=workflow_content,
                level=2
            ))
        
        return GeneratedSection(
            title="Methodology",
            content=content,
            subsections=subsections,
            metadata={
                'methods_count': len(methods),
                'tools_count': len(tools),
                'algorithms_count': len(algorithms)
            }
        )
    
    def _build_methods_content(self, methods: List[Any]) -> str:
        """Build content for methods"""
        content_parts = []
        
        for method in methods:
            if isinstance(method, dict):
                name = method.get('name', '')
                description = method.get('description', '')
                content_parts.append(f"**{name}**: {description}")
            else:
                content_parts.append(f"- {method}")
        
        return "\n\n".join(content_parts)
    
    def _build_tools_content(self, tools: List[Any]) -> str:
        """Build content for tools"""
        if not tools:
            return ""
        
        content_parts = []
        
        for tool in tools:
            if isinstance(tool, dict):
                name = tool.get('name', '')
                purpose = tool.get('purpose', '')
                version = tool.get('version', '')
                
                part = f"**{name}**"
                if version:
                    part += f" (v{version})"
                if purpose:
                    part += f": {purpose}"
                
                content_parts.append(part)
            else:
                content_parts.append(f"- {tool}")
        
        return "\n\n".join(content_parts)
    
    def _build_algorithms_content(self, algorithms: List[Any]) -> str:
        """Build content for algorithms"""
        content_parts = []
        
        for algo in algorithms:
            if isinstance(algo, dict):
                name = algo.get('name', '')
                purpose = algo.get('purpose', '')
                complexity = algo.get('complexity', '')
                
                part = f"**{name}**"
                if purpose:
                    part += f"\n\nPurpose: {purpose}"
                if complexity:
                    part += f"\n\nComplexity: {complexity}"
                
                content_parts.append(part)
            else:
                content_parts.append(f"- {algo}")
        
        return "\n\n".join(content_parts)
