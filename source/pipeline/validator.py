from typing import Dict, Any, List, Tuple
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from config_models import ReportConfig, validate_config as pydantic_validate

class InputValidator:
    """Validate input configuration using Pydantic models"""
    
    def validate(self, config: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate configuration using Pydantic
        Returns: (is_valid, error_messages)
        """
        # Try new Pydantic validation first
        is_valid, errors = pydantic_validate(config)
        if is_valid:
            return True, []
        
        # If validation fails, try legacy format conversion
        try:
            ReportConfig.from_legacy_config(config)
            return True, []
        except Exception as e:
            return False, [str(e)]
    
    def normalize(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Normalize configuration with defaults
        Returns flat dict for backward compatibility with existing pipeline
        """
        try:
            # Try loading as new format
            report_config = ReportConfig(**config)
        except:
            # Fall back to legacy conversion
            report_config = ReportConfig.from_legacy_config(config)
        
        # Convert to flat legacy format for backward compatibility
        return self._to_legacy_format(report_config)
    
    def load_config(self, config: Dict[str, Any]) -> ReportConfig:
        """
        Load and validate config, return Pydantic model
        """
        try:
            return ReportConfig(**config)
        except:
            return ReportConfig.from_legacy_config(config)
    
    def _to_legacy_format(self, config: ReportConfig) -> Dict[str, Any]:
        """Convert Pydantic model to flat legacy format"""
        legacy = {
            # Project info (flattened)
            'title': config.project_info.title,
            'subtitle': config.project_info.subtitle or '',
            'description': config.project_info.description,
            'students': [
                {'name': s.name, 'id': s.id, 'email': s.email, 'role': s.role}
                for s in config.project_info.students
            ],
            'advisor': config.project_info.advisor or '',
            'university': config.project_info.university or config.project_info.organization or '',
            'organization': config.project_info.organization or config.project_info.university or '',
            'faculty': config.project_info.faculty or '',
            'class': config.project_info.class_name or '',
            'github_repo': str(config.project_info.github_repo) if config.project_info.github_repo else '',
            'demo_url': str(config.project_info.demo_url) if config.project_info.demo_url else '',
            'keywords': config.project_info.keywords,
            
            # Report profile
            'report_type': config.report_profile.report_type,
            'language': config.report_profile.language,
            'target_pages': config.report_profile.target_pages,
            
            # Technical data
            'algorithms': config.technical_data.algorithms,
            'technologies': config.technical_data.technologies,
            'datasets': config.technical_data.datasets,
        }
        
        return legacy
