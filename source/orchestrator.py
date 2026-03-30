#!/usr/bin/env python3
"""
Report Generation Orchestrator
Clean orchestration layer with step-by-step execution
"""

import json
import os
import sys
from typing import Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))

from pipeline import (
    InputValidator,
    OutlinePlanner,
    SectionGenerator,
    EvidenceBinder,
    ReportRenderer
)
from config_models import ReportConfig
from models import Report
from review.engine import ReviewEngine, ReviewReport
from review.models import Severity


@dataclass
class PipelineStep:
    """Represents a pipeline step"""
    name: str
    emoji: str
    description: str
    completed: bool = False
    error: Optional[str] = None
    duration: float = 0.0


class ProgressTracker:
    """Track pipeline progress"""
    
    def __init__(self):
        self.steps = []
        self.start_time = None
        self.end_time = None
    
    def add_step(self, name: str, emoji: str, description: str) -> PipelineStep:
        """Add a new step"""
        step = PipelineStep(name=name, emoji=emoji, description=description)
        self.steps.append(step)
        return step
    
    def start(self):
        """Start tracking"""
        self.start_time = datetime.now()
    
    def complete_step(self, step: PipelineStep, duration: float):
        """Mark step as completed"""
        step.completed = True
        step.duration = duration
    
    def fail_step(self, step: PipelineStep, error: str):
        """Mark step as failed"""
        step.error = error
    
    def finish(self):
        """Finish tracking"""
        self.end_time = datetime.now()
    
    def get_summary(self) -> str:
        """Get execution summary"""
        if not self.start_time or not self.end_time:
            return "Pipeline not completed"
        
        total_time = (self.end_time - self.start_time).total_seconds()
        completed = sum(1 for s in self.steps if s.completed)
        failed = sum(1 for s in self.steps if s.error)
        
        summary = [
            "\n" + "="*60,
            "Pipeline Execution Summary",
            "="*60,
            f"Total Steps: {len(self.steps)}",
            f"Completed: {completed}",
            f"Failed: {failed}",
            f"Total Time: {total_time:.2f}s",
            ""
        ]
        
        for i, step in enumerate(self.steps, 1):
            status = "✅" if step.completed else ("❌" if step.error else "⏸️")
            summary.append(f"{i}. {status} {step.emoji} {step.name} ({step.duration:.2f}s)")
            if step.error:
                summary.append(f"   Error: {step.error}")
        
        summary.append("="*60)
        return "\n".join(summary)


class ReportOrchestrator:
    """
    Main orchestrator for report generation pipeline
    Coordinates all steps from config loading to final output
    """
    
    def __init__(self, config_path: str = 'report_config.json', verbose: bool = True):
        """
        Initialize orchestrator
        
        Args:
            config_path: Path to configuration file
            verbose: Enable verbose output
        """
        self.config_path = config_path
        self.verbose = verbose
        self.tracker = ProgressTracker()
        
        # Pipeline components (lazy initialization)
        self.validator = None
        self.planner = None
        self.generator = None
        self.binder = None
        self.renderer = None
        
        # Data holders
        self.config_dict = None
        self.config_model = None
        self.report = None
    
    def _log(self, message: str):
        """Log message if verbose"""
        if self.verbose:
            try:
                print(message)
            except UnicodeEncodeError:
                # Fallback for Windows console - replace emojis with ASCII
                import sys
                if sys.platform == 'win32':
                    # Simple emoji to ASCII mapping
                    replacements = {
                        '🚀': '>>', '📖': '[*]', '✔️': '[v]', '📋': '[-]',
                        '✍️': '[~]', '📊': '[#]', '📄': '[=]', '🔍': '[?]',
                        '✅': '[OK]', '❌': '[X]', '⚠️': '[!]', 'ℹ': '[i]',
                        '✗': '[X]', '⏸️': '[-]'
                    }
                    for emoji, ascii_rep in replacements.items():
                        message = message.replace(emoji, ascii_rep)
                print(message)
    
    def _initialize_components(self):
        """Initialize pipeline components"""
        self.validator = InputValidator()
        self.planner = OutlinePlanner()
        self.generator = SectionGenerator()
        self.binder = EvidenceBinder()
        self.renderer = ReportRenderer(output_format="docx")
    
    def step_load_config(self) -> bool:
        """
        Step 1: Load configuration from file
        Returns: True if successful
        """
        step = self.tracker.add_step(
            "Load Config",
            "📖",
            f"Loading configuration from {self.config_path}"
        )
        
        start = datetime.now()
        
        try:
            self._log(f"\n{step.emoji} {step.description}...")
            
            if not os.path.exists(self.config_path):
                raise FileNotFoundError(f"Config file not found: {self.config_path}")
            
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config_dict = json.load(f)
            
            duration = (datetime.now() - start).total_seconds()
            self.tracker.complete_step(step, duration)
            self._log(f"   ✅ Config loaded ({duration:.2f}s)\n")
            return True
            
        except Exception as e:
            duration = (datetime.now() - start).total_seconds()
            self.tracker.fail_step(step, str(e))
            self._log(f"   ❌ Failed to load config: {e}\n")
            return False
    
    def step_validate_config(self) -> bool:
        """
        Step 2: Validate configuration
        Returns: True if valid
        """
        step = self.tracker.add_step(
            "Validate Config",
            "✔️",
            "Validating configuration with Pydantic"
        )
        
        start = datetime.now()
        
        try:
            self._log(f"{step.emoji} {step.description}...")
            
            if self.validator is None:
                self._initialize_components()
            
            # Validate
            is_valid, errors = self.validator.validate(self.config_dict)
            if not is_valid:
                error_msg = "; ".join(errors)
                raise ValueError(f"Validation failed: {error_msg}")
            
            # Load as Pydantic model
            self.config_model = self.validator.load_config(self.config_dict)
            
            # Normalize for backward compatibility
            self.config_dict = self.validator.normalize(self.config_dict)
            
            duration = (datetime.now() - start).total_seconds()
            self.tracker.complete_step(step, duration)
            self._log(f"   ✅ Config validated ({duration:.2f}s)\n")
            return True
            
        except Exception as e:
            duration = (datetime.now() - start).total_seconds()
            self.tracker.fail_step(step, str(e))
            self._log(f"   ❌ Validation failed: {e}\n")
            return False
    
    def step_plan_outline(self) -> bool:
        """
        Step 3: Plan report outline
        Returns: True if successful
        """
        step = self.tracker.add_step(
            "Plan Outline",
            "📋",
            "Planning report structure and sections"
        )
        
        start = datetime.now()
        
        try:
            self._log(f"{step.emoji} {step.description}...")
            
            self.report = self.planner.plan(self.config_dict)
            
            duration = (datetime.now() - start).total_seconds()
            self.tracker.complete_step(step, duration)
            self._log(f"   ✅ Created {len(self.report.sections)} sections ({duration:.2f}s)\n")
            return True
            
        except Exception as e:
            duration = (datetime.now() - start).total_seconds()
            self.tracker.fail_step(step, str(e))
            self._log(f"   ❌ Planning failed: {e}\n")
            return False
    
    def step_generate_content(self) -> bool:
        """
        Step 4: Generate section content
        Returns: True if successful
        """
        step = self.tracker.add_step(
            "Generate Content",
            "✍️",
            "Generating content for all sections"
        )
        
        start = datetime.now()
        
        try:
            self._log(f"{step.emoji} {step.description}...")
            
            self.report = self.generator.generate(self.report)
            
            duration = (datetime.now() - start).total_seconds()
            self.tracker.complete_step(step, duration)
            self._log(f"   ✅ Content generated ({duration:.2f}s)\n")
            return True
            
        except Exception as e:
            duration = (datetime.now() - start).total_seconds()
            self.tracker.fail_step(step, str(e))
            self._log(f"   ❌ Generation failed: {e}\n")
            return False
    
    def step_bind_evidence(self) -> bool:
        """
        Step 5: Bind evidence (diagrams, tables, etc.) and generate bibliography
        Returns: True if successful
        """
        step = self.tracker.add_step(
            "Bind Evidence",
            "📊",
            "Binding diagrams, evidence, and generating bibliography"
        )
        
        start = datetime.now()
        
        try:
            self._log(f"{step.emoji} {step.description}...")
            
            # Bind evidence
            self.report = self.binder.bind(self.report)
            
            # Generate bibliography if references exist
            if self.config_model and hasattr(self.config_model, 'evidence') and self.config_model.evidence.references:
                self._generate_bibliography()
            
            duration = (datetime.now() - start).total_seconds()
            self.tracker.complete_step(step, duration)
            self._log(f"   ✅ Bound {len(self.report.evidence)} evidence items ({duration:.2f}s)\n")
            return True
            
        except Exception as e:
            duration = (datetime.now() - start).total_seconds()
            self.tracker.fail_step(step, str(e))
            self._log(f"   ❌ Evidence binding failed: {e}\n")
            return False
    
    def _generate_bibliography(self):
        """Generate bibliography section from config references"""
        try:
            from references import BibliographyGenerator, ReferenceEntry
            
            # Get citation style from config
            style = 'IEEE'  # default
            if hasattr(self.config_model, 'format_rules') and hasattr(self.config_model.format_rules, 'citation_style'):
                style = self.config_model.format_rules.citation_style
            
            # Convert config references to ReferenceEntry
            ref_entries = []
            for i, ref in enumerate(self.config_model.evidence.references, 1):
                try:
                    entry = ReferenceEntry.from_config_model(ref)
                    # Use index as ID if not set
                    if not entry.id or entry.id == ref.id:
                        entry.id = str(i)
                    ref_entries.append(entry)
                except Exception:
                    # Skip invalid references
                    continue
            
            if ref_entries:
                # Generate bibliography section
                gen = BibliographyGenerator(style=style)
                bib_section = gen.generate_section(ref_entries)
                
                # Add to report sections
                from models import Section, SectionType
                section = Section(
                    id='references',
                    type=SectionType.REFERENCES,
                    title=bib_section['title'],
                    content=bib_section['content'],
                    metadata=bib_section['metadata']
                )
                self.report.sections.append(section)
                
        except ImportError:
            # References module not available, skip
            pass
        except Exception as e:
            # Log but don't fail
            self._log(f"   ⚠️  Bibliography generation warning: {e}\n")
    
    def _report_to_review_data(self) -> Dict[str, Any]:
        """Convert Report object to review engine data format"""
        if not self.report:
            return {}
        
        # Convert metadata
        metadata = {
            'title': self.report.metadata.title,
            'subtitle': self.report.metadata.subtitle,
            'authors': self.report.metadata.authors,
            'report_type': 'project_report'
        }
        
        # Convert sections
        sections = []
        for section in self.report.sections:
            section_dict = {
                'id': section.id,
                'title': section.title,
                'type': section.type.value if hasattr(section.type, 'value') else str(section.type),
                'content': section.content,
                'level': section.level,
                'subsections': []
            }
            
            # Convert subsections
            for subsection in section.subsections:
                subsection_dict = {
                    'id': subsection.id,
                    'title': subsection.title,
                    'type': subsection.type.value if hasattr(subsection.type, 'value') else str(subsection.type),
                    'content': subsection.content,
                    'level': subsection.level
                }
                section_dict['subsections'].append(subsection_dict)
            
            sections.append(section_dict)
        
        # Convert evidence - group by type
        evidence_dict = {
            'figures': [],
            'tables': [],
            'charts': []
        }
        for ev in self.report.evidence:
            ev_dict = {
                'id': ev.id,
                'type': ev.type.value if hasattr(ev.type, 'value') else str(ev.type),
                'caption': getattr(ev, 'caption', ''),
                'path': getattr(ev, 'path', '')
            }
            # Categorize by type
            ev_type = ev_dict['type'].lower()
            if 'figure' in ev_type or 'diagram' in ev_type:
                evidence_dict['figures'].append(ev_dict)
            elif 'table' in ev_type:
                evidence_dict['tables'].append(ev_dict)
            elif 'chart' in ev_type:
                evidence_dict['charts'].append(ev_dict)
            else:
                # Default to figures
                evidence_dict['figures'].append(ev_dict)
        
        # Extract references from config if available
        references = []
        if self.config_dict and 'evidence' in self.config_dict:
            evidence_data = self.config_dict.get('evidence', {})
            if isinstance(evidence_data, dict):
                references = evidence_data.get('references', [])
            elif isinstance(evidence_data, list):
                # Legacy format - evidence is a list
                references = []
        
        return {
            'metadata': metadata,
            'sections': sections,
            'evidence': evidence_dict,
            'references': references
        }
    
    def step_render_output(self, output_path: str) -> bool:
        """
        Step 6: Render final output
        Returns: True if successful
        """
        step = self.tracker.add_step(
            "Render Output",
            "📄",
            f"Rendering to {output_path}"
        )
        
        start = datetime.now()
        
        try:
            self._log(f"{step.emoji} {step.description}...")
            
            # Ensure output directory exists
            os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
            
            output_file = self.renderer.render(self.report, output_path)
            
            duration = (datetime.now() - start).total_seconds()
            self.tracker.complete_step(step, duration)
            self._log(f"   ✅ Rendered to {output_file} ({duration:.2f}s)\n")
            return True
            
        except Exception as e:
            duration = (datetime.now() - start).total_seconds()
            self.tracker.fail_step(step, str(e))
            self._log(f"   ❌ Rendering failed: {e}\n")
            return False
    
    def step_review_output(self, output_path: str) -> bool:
        """
        Step 7: Review and validate output
        Returns: True if successful
        """
        step = self.tracker.add_step(
            "Review Output",
            "🔍",
            "Reviewing generated report"
        )
        
        start = datetime.now()
        
        try:
            self._log(f"{step.emoji} {step.description}...")
            
            # Check file exists
            if not os.path.exists(output_path):
                raise FileNotFoundError(f"Output file not found: {output_path}")
            
            # Check file size
            file_size = os.path.getsize(output_path)
            if file_size < 1000:  # Less than 1KB is suspicious
                raise ValueError(f"Output file too small: {file_size} bytes")
            
            # Run review engine on report
            try:
                review_data = self._report_to_review_data()
                engine = ReviewEngine()
                result = engine.review(review_data)
                
                # Display review results
                self._log("\n" + ReviewReport.format_text(result))
                
                # Fail if critical errors found
                if result.errors > 0:
                    duration = (datetime.now() - start).total_seconds()
                    self.tracker.fail_step(step, f"{result.errors} critical errors found")
                    self._log(f"   ❌ Review failed with {result.errors} errors ({duration:.2f}s)\n")
                    return False
            except Exception as review_error:
                # Log review error but don't fail the pipeline
                self._log(f"   ⚠️  Review engine error (non-critical): {review_error}\n")
            
            # Success (warnings/info are acceptable)
            duration = (datetime.now() - start).total_seconds()
            self.tracker.complete_step(step, duration)
            file_size_kb = file_size / 1024
            self._log(f"   ✅ Review passed ({file_size_kb:.1f} KB, {duration:.2f}s)\n")
            return True
            
        except Exception as e:
            duration = (datetime.now() - start).total_seconds()
            self.tracker.fail_step(step, str(e))
            self._log(f"   ❌ Review failed: {e}\n")
            return False
    
    def execute(self, output_path: str = 'output/report.docx') -> bool:
        """
        Execute complete pipeline
        
        Args:
            output_path: Path for output file
            
        Returns:
            True if successful
        """
        self._log("\n" + "="*60)
        self._log("🚀 Report Generation Pipeline")
        self._log("="*60)
        
        self.tracker.start()
        
        # Execute steps in order
        steps = [
            lambda: self.step_load_config(),
            lambda: self.step_validate_config(),
            lambda: self.step_plan_outline(),
            lambda: self.step_generate_content(),
            lambda: self.step_bind_evidence(),
            lambda: self.step_render_output(output_path),
            lambda: self.step_review_output(output_path)
        ]
        
        for step_func in steps:
            if not step_func():
                self.tracker.finish()
                self._log("\n❌ Pipeline failed!")
                self._log(self.tracker.get_summary())
                return False
        
        self.tracker.finish()
        self._log("✅ Pipeline completed successfully!")
        self._log(self.tracker.get_summary())
        
        return True
    
    def get_report(self) -> Optional[Report]:
        """Get generated report object"""
        return self.report
    
    def get_config(self) -> Optional[ReportConfig]:
        """Get validated config model"""
        return self.config_model
