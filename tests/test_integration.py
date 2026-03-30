"""
Integration tests
"""

import pytest
from pathlib import Path


@pytest.mark.integration
def test_full_pipeline_minimal(sample_config_dict, temp_output_dir):
    """Test full pipeline with minimal config"""
    from source.orchestrator import ReportOrchestrator
    import json
    
    # Write config to file
    config_path = temp_output_dir / 'test_config.json'
    with open(config_path, 'w') as f:
        json.dump(sample_config_dict, f)
    
    orchestrator = ReportOrchestrator(str(config_path), verbose=False)
    output_path = temp_output_dir / 'integration_test.docx'
    
    success = orchestrator.execute(str(output_path))
    
    assert success is True
    assert output_path.exists()


@pytest.mark.integration
def test_config_to_output_flow(sample_config_dict, temp_output_dir):
    """Test complete flow from config to output"""
    from source.config_models import ReportConfig
    from source.orchestrator import ReportOrchestrator
    import json
    
    # Validate config
    config = ReportConfig(**sample_config_dict)
    assert config is not None
    
    # Write config to file
    config_path = temp_output_dir / 'flow_config.json'
    with open(config_path, 'w') as f:
        json.dump(sample_config_dict, f)
    
    # Generate report
    orchestrator = ReportOrchestrator(str(config_path), verbose=False)
    output_path = temp_output_dir / 'flow_test.docx'
    
    success = orchestrator.execute(str(output_path))
    assert success is True
    assert output_path.exists()


@pytest.mark.integration
@pytest.mark.slow
def test_multiple_report_types(sample_config_dict, temp_output_dir):
    """Test generating different report types"""
    from source.orchestrator import ReportOrchestrator
    import json
    
    report_types = ['project_report', 'technical_report', 'thesis']
    
    for report_type in report_types:
        config = sample_config_dict.copy()
        config['report_profile']['report_type'] = report_type
        
        # Write config to file
        config_path = temp_output_dir / f'{report_type}_config.json'
        with open(config_path, 'w') as f:
            json.dump(config, f)
        
        orchestrator = ReportOrchestrator(str(config_path), verbose=False)
        output_path = temp_output_dir / f'{report_type}_test.docx'
        
        success = orchestrator.execute(str(output_path))
        assert success is True
        assert output_path.exists()
