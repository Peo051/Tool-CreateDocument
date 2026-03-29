#!/usr/bin/env python3
"""
OutlinePlanner - Generate structured report outlines by type
"""

from typing import List, Optional, Dict, Any
from dataclasses import dataclass, field
from enum import Enum


class ReportType(str, Enum):
    """Supported report types"""
    THESIS = "thesis"
    TECHNICAL_REPORT = "technical_report"
    PROJECT_REPORT = "project_report"
    BUSINESS_REPORT = "business_report"


@dataclass
class OutlineSection:
    """Represents a section in the outline"""
    id: str
    title: str
    level: int = 1
    subsections: List['OutlineSection'] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def add_subsection(self, section: 'OutlineSection') -> None:
        """Add a subsection"""
        self.subsections.append(section)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'level': self.level,
            'subsections': [s.to_dict() for s in self.subsections],
            'metadata': self.metadata
        }


@dataclass
class ReportOutline:
    """Complete report outline"""
    report_type: ReportType
    sections: List[OutlineSection] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def add_section(self, section: OutlineSection) -> None:
        """Add a top-level section"""
        self.sections.append(section)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'report_type': self.report_type.value,
            'sections': [s.to_dict() for s in self.sections],
            'metadata': self.metadata
        }


class OutlinePlanner:
    """Generate report outlines based on type"""
    
    def __init__(self):
        self.outline_builders = {
            ReportType.THESIS: self._build_thesis_outline,
            ReportType.TECHNICAL_REPORT: self._build_technical_outline,
            ReportType.PROJECT_REPORT: self._build_project_outline,
            ReportType.BUSINESS_REPORT: self._build_business_outline
        }
    
    def plan(self, report_type: str, config: Optional[Dict[str, Any]] = None) -> ReportOutline:
        """
        Generate outline for report type
        
        Args:
            report_type: Type of report (thesis, technical_report, etc.)
            config: Optional config with custom sections
            
        Returns:
            ReportOutline object
        """
        config = config or {}
        
        # Convert string to enum
        try:
            rtype = ReportType(report_type)
        except ValueError:
            raise ValueError(f"Unknown report type: {report_type}")
        
        # Build default outline
        outline = self.outline_builders[rtype](config)
        
        # Apply user overrides
        if 'custom_sections' in config:
            self._apply_custom_sections(outline, config['custom_sections'])
        
        return outline
    
    def _build_thesis_outline(self, config: Dict[str, Any]) -> ReportOutline:
        """Build thesis outline"""
        outline = ReportOutline(report_type=ReportType.THESIS)
        
        # Front matter
        outline.add_section(OutlineSection('cover', 'Cover Page', level=0))
        outline.add_section(OutlineSection('abstract', 'Abstract', level=0))
        outline.add_section(OutlineSection('acknowledgment', 'Acknowledgment', level=0))
        outline.add_section(OutlineSection('toc', 'Table of Contents', level=0))
        
        # Chapter 1: Introduction
        intro = OutlineSection('ch1', 'Chapter 1: Introduction', level=1)
        intro.add_subsection(OutlineSection('ch1.1', 'Background', level=2))
        intro.add_subsection(OutlineSection('ch1.2', 'Problem Statement', level=2))
        intro.add_subsection(OutlineSection('ch1.3', 'Research Objectives', level=2))
        intro.add_subsection(OutlineSection('ch1.4', 'Scope and Limitations', level=2))
        outline.add_section(intro)
        
        # Chapter 2: Literature Review
        lit = OutlineSection('ch2', 'Chapter 2: Literature Review', level=1)
        lit.add_subsection(OutlineSection('ch2.1', 'Theoretical Framework', level=2))
        lit.add_subsection(OutlineSection('ch2.2', 'Related Work', level=2))
        outline.add_section(lit)
        
        # Chapter 3: Methodology
        method = OutlineSection('ch3', 'Chapter 3: Methodology', level=1)
        method.add_subsection(OutlineSection('ch3.1', 'Research Design', level=2))
        method.add_subsection(OutlineSection('ch3.2', 'Data Collection', level=2))
        method.add_subsection(OutlineSection('ch3.3', 'Analysis Methods', level=2))
        outline.add_section(method)
        
        # Chapter 4: Results
        results = OutlineSection('ch4', 'Chapter 4: Results', level=1)
        results.add_subsection(OutlineSection('ch4.1', 'Findings', level=2))
        results.add_subsection(OutlineSection('ch4.2', 'Analysis', level=2))
        outline.add_section(results)
        
        # Chapter 5: Discussion
        disc = OutlineSection('ch5', 'Chapter 5: Discussion', level=1)
        disc.add_subsection(OutlineSection('ch5.1', 'Interpretation', level=2))
        disc.add_subsection(OutlineSection('ch5.2', 'Implications', level=2))
        outline.add_section(disc)
        
        # Chapter 6: Conclusion
        concl = OutlineSection('ch6', 'Chapter 6: Conclusion', level=1)
        concl.add_subsection(OutlineSection('ch6.1', 'Summary', level=2))
        concl.add_subsection(OutlineSection('ch6.2', 'Future Work', level=2))
        outline.add_section(concl)
        
        # Back matter
        outline.add_section(OutlineSection('references', 'References', level=0))
        outline.add_section(OutlineSection('appendices', 'Appendices', level=0))
        
        return outline
    
    def _build_technical_outline(self, config: Dict[str, Any]) -> ReportOutline:
        """Build technical report outline"""
        outline = ReportOutline(report_type=ReportType.TECHNICAL_REPORT)
        
        outline.add_section(OutlineSection('cover', 'Cover Page', level=0))
        outline.add_section(OutlineSection('executive_summary', 'Executive Summary', level=0))
        outline.add_section(OutlineSection('toc', 'Table of Contents', level=0))
        
        # Introduction
        intro = OutlineSection('intro', '1. Introduction', level=1)
        intro.add_subsection(OutlineSection('intro.1', '1.1 Purpose', level=2))
        intro.add_subsection(OutlineSection('intro.2', '1.2 Scope', level=2))
        outline.add_section(intro)
        
        # Technical Background
        tech = OutlineSection('tech', '2. Technical Background', level=1)
        tech.add_subsection(OutlineSection('tech.1', '2.1 Technologies', level=2))
        tech.add_subsection(OutlineSection('tech.2', '2.2 Architecture', level=2))
        outline.add_section(tech)
        
        # Implementation
        impl = OutlineSection('impl', '3. Implementation', level=1)
        impl.add_subsection(OutlineSection('impl.1', '3.1 Design', level=2))
        impl.add_subsection(OutlineSection('impl.2', '3.2 Development', level=2))
        impl.add_subsection(OutlineSection('impl.3', '3.3 Testing', level=2))
        outline.add_section(impl)
        
        # Results
        results = OutlineSection('results', '4. Results', level=1)
        results.add_subsection(OutlineSection('results.1', '4.1 Performance', level=2))
        results.add_subsection(OutlineSection('results.2', '4.2 Evaluation', level=2))
        outline.add_section(results)
        
        # Conclusion
        outline.add_section(OutlineSection('conclusion', '5. Conclusion', level=1))
        outline.add_section(OutlineSection('references', 'References', level=0))
        
        return outline
    
    def _build_project_outline(self, config: Dict[str, Any]) -> ReportOutline:
        """Build project report outline"""
        outline = ReportOutline(report_type=ReportType.PROJECT_REPORT)
        
        outline.add_section(OutlineSection('cover', 'Cover Page', level=0))
        outline.add_section(OutlineSection('acknowledgment', 'Acknowledgment', level=0))
        outline.add_section(OutlineSection('commitment', 'Commitment', level=0))
        outline.add_section(OutlineSection('toc', 'Table of Contents', level=0))
        
        # Introduction
        intro = OutlineSection('intro', 'Introduction', level=1)
        intro.add_subsection(OutlineSection('intro.1', 'Project Motivation', level=2))
        intro.add_subsection(OutlineSection('intro.2', 'Objectives', level=2))
        intro.add_subsection(OutlineSection('intro.3', 'Scope', level=2))
        outline.add_section(intro)
        
        # Overview
        overview = OutlineSection('overview', 'System Overview', level=1)
        overview.add_subsection(OutlineSection('overview.1', 'Architecture', level=2))
        overview.add_subsection(OutlineSection('overview.2', 'Technologies', level=2))
        outline.add_section(overview)
        
        # Algorithms (if specified)
        if config.get('algorithms'):
            algos = OutlineSection('algorithms', 'Algorithms', level=1)
            for i, algo in enumerate(config['algorithms'][:5], 1):
                algos.add_subsection(OutlineSection(
                    f'algo.{i}',
                    f'{i}. {algo}',
                    level=2,
                    metadata={'algorithm': algo}
                ))
            outline.add_section(algos)
        
        # Implementation
        impl = OutlineSection('implementation', 'Implementation', level=1)
        impl.add_subsection(OutlineSection('impl.1', 'Development Process', level=2))
        impl.add_subsection(OutlineSection('impl.2', 'Key Features', level=2))
        outline.add_section(impl)
        
        # Results
        results = OutlineSection('results', 'Results and Evaluation', level=1)
        results.add_subsection(OutlineSection('results.1', 'Testing', level=2))
        results.add_subsection(OutlineSection('results.2', 'Performance', level=2))
        outline.add_section(results)
        
        # Conclusion
        outline.add_section(OutlineSection('conclusion', 'Conclusion and Future Work', level=1))
        outline.add_section(OutlineSection('references', 'References', level=0))
        
        return outline
    
    def _build_business_outline(self, config: Dict[str, Any]) -> ReportOutline:
        """Build business report outline"""
        outline = ReportOutline(report_type=ReportType.BUSINESS_REPORT)
        
        outline.add_section(OutlineSection('cover', 'Cover Page', level=0))
        outline.add_section(OutlineSection('executive_summary', 'Executive Summary', level=0))
        outline.add_section(OutlineSection('toc', 'Table of Contents', level=0))
        
        # Introduction
        intro = OutlineSection('intro', '1. Introduction', level=1)
        intro.add_subsection(OutlineSection('intro.1', '1.1 Background', level=2))
        intro.add_subsection(OutlineSection('intro.2', '1.2 Purpose', level=2))
        outline.add_section(intro)
        
        # Market Analysis
        market = OutlineSection('market', '2. Market Analysis', level=1)
        market.add_subsection(OutlineSection('market.1', '2.1 Market Overview', level=2))
        market.add_subsection(OutlineSection('market.2', '2.2 Competitive Analysis', level=2))
        outline.add_section(market)
        
        # Strategy
        strategy = OutlineSection('strategy', '3. Strategy', level=1)
        strategy.add_subsection(OutlineSection('strategy.1', '3.1 Approach', level=2))
        strategy.add_subsection(OutlineSection('strategy.2', '3.2 Implementation Plan', level=2))
        outline.add_section(strategy)
        
        # Financial Analysis
        finance = OutlineSection('finance', '4. Financial Analysis', level=1)
        finance.add_subsection(OutlineSection('finance.1', '4.1 Budget', level=2))
        finance.add_subsection(OutlineSection('finance.2', '4.2 ROI Projection', level=2))
        outline.add_section(finance)
        
        # Recommendations
        outline.add_section(OutlineSection('recommendations', '5. Recommendations', level=1))
        outline.add_section(OutlineSection('conclusion', '6. Conclusion', level=1))
        outline.add_section(OutlineSection('appendices', 'Appendices', level=0))
        
        return outline
    
    def _apply_custom_sections(self, outline: ReportOutline, custom_sections: List[Dict[str, Any]]) -> None:
        """Apply user-defined custom sections"""
        for custom in custom_sections:
            section = OutlineSection(
                id=custom.get('id', f"custom_{len(outline.sections)}"),
                title=custom['title'],
                level=custom.get('level', 1),
                metadata=custom.get('metadata', {})
            )
            
            # Add subsections if provided
            for subsec in custom.get('subsections', []):
                section.add_subsection(OutlineSection(
                    id=subsec.get('id', f"{section.id}.{len(section.subsections)}"),
                    title=subsec['title'],
                    level=subsec.get('level', 2)
                ))
            
            # Insert at specified position or append
            position = custom.get('position', len(outline.sections))
            if position < len(outline.sections):
                outline.sections.insert(position, section)
            else:
                outline.add_section(section)
