from typing import Dict, Any
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from models import Report, Figure, EvidenceType
from content import DiagramGenerator
import os as os_module

class EvidenceBinder:
    """Bind evidence (diagrams, tables, figures) to report"""
    
    def __init__(self):
        self.diagram_gen = DiagramGenerator()
        os_module.makedirs('diagrams', exist_ok=True)
    
    def bind(self, report: Report) -> Report:
        """Generate and bind evidence to report"""
        
        # Generate diagrams for algorithms
        for section in report.sections:
            if section.type.value == "algorithm":
                algo_name = section.metadata.get('algorithm')
                if algo_name:
                    self._generate_algorithm_diagram(algo_name, section, report)
            
            # Recursively process subsections
            for subsection in section.subsections:
                if subsection.type.value == "algorithm":
                    algo_name = subsection.metadata.get('algorithm')
                    if algo_name:
                        self._generate_algorithm_diagram(algo_name, subsection, report)
        
        return report
    
    def _generate_algorithm_diagram(self, algo_name: str, section, report: Report):
        """Generate diagram for algorithm"""
        diagram_map = {
            'DFS': 'create_maze_example',
            'BFS': 'create_bfs_visualization',
            'A*': 'create_astar_comparison',
            'Dijkstra': 'create_dijkstra_cost_map',
            'CSP': 'create_csp_example'
        }
        
        if algo_name not in diagram_map:
            return
        
        try:
            method = getattr(self.diagram_gen, diagram_map[algo_name])
            img_buffer = method()
            
            # Save diagram
            safe_name = algo_name.lower().replace('*', 'star').replace('/', '_')
            img_path = f'diagrams/{safe_name}_diagram.png'
            with open(img_path, 'wb') as f:
                f.write(img_buffer.read())
            
            # Create figure evidence
            figure = Figure(
                id=f"fig_{safe_name}",
                type=EvidenceType.FIGURE,
                title=f"Minh họa thuật toán {algo_name}",
                file_path=img_path,
                caption=f"Hình: Minh họa thuật toán {algo_name}",
                position=section.id
            )
            
            report.add_evidence(figure)
            
        except Exception as e:
            print(f"Warning: Could not generate diagram for {algo_name}: {e}")
