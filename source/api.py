#!/usr/bin/env python3
"""
FastAPI Backend for Report Generator
Reuses existing orchestrator, config models, and renderers
"""

import os
import sys
import json
import uuid
from typing import Dict, Any, Optional
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

sys.path.insert(0, os.path.dirname(__file__))

from config_models import ReportConfig, validate_config
from orchestrator import ReportOrchestrator
from pipeline import OutlinePlanner, InputValidator


# ============================================================================
# API MODELS
# ============================================================================

class ValidationRequest(BaseModel):
    """Request for config validation"""
    config: Dict[str, Any]


class ValidationResponse(BaseModel):
    """Response for validation"""
    valid: bool
    errors: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


class PreviewRequest(BaseModel):
    """Request for outline preview"""
    config: Dict[str, Any]


class PreviewResponse(BaseModel):
    """Response for outline preview"""
    outline: Dict[str, Any]
    section_count: int
    estimated_pages: Optional[int] = None


class GenerateRequest(BaseModel):
    """Request for report generation"""
    config: Dict[str, Any]


class JobStatus(BaseModel):
    """Job status response"""
    job_id: str
    status: str  # pending, running, completed, failed
    progress: int  # 0-100
    message: str
    file_id: Optional[str] = None
    error: Optional[str] = None
    created_at: str
    updated_at: str


class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    version: str
    timestamp: str


# ============================================================================
# JOB STORAGE (in-memory for MVP)
# ============================================================================

JOBS: Dict[str, Dict[str, Any]] = {}
OUTPUT_DIR = Path("output/api")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def create_job(config: Dict[str, Any]) -> str:
    """Create a new generation job"""
    job_id = str(uuid.uuid4())
    now = datetime.now().isoformat()
    
    JOBS[job_id] = {
        "job_id": job_id,
        "status": "pending",
        "progress": 0,
        "message": "Job created",
        "file_id": None,
        "error": None,
        "config": config,
        "created_at": now,
        "updated_at": now
    }
    
    return job_id


def update_job(job_id: str, **kwargs):
    """Update job status"""
    if job_id in JOBS:
        JOBS[job_id].update(kwargs)
        JOBS[job_id]["updated_at"] = datetime.now().isoformat()


def get_job(job_id: str) -> Optional[Dict[str, Any]]:
    """Get job by ID"""
    return JOBS.get(job_id)


# ============================================================================
# BACKGROUND TASKS
# ============================================================================

def generate_report_task(job_id: str, config: Dict[str, Any]):
    """Background task for report generation"""
    try:
        update_job(job_id, status="running", progress=10, message="Validating config")
        
        # Save config to temp file
        config_path = OUTPUT_DIR / f"{job_id}_config.json"
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        
        update_job(job_id, progress=20, message="Planning outline")
        
        # Generate report
        output_path = OUTPUT_DIR / f"{job_id}_report.docx"
        orchestrator = ReportOrchestrator(str(config_path), verbose=False)
        
        update_job(job_id, progress=40, message="Generating content")
        success = orchestrator.execute(str(output_path))
        
        # Check if file was actually created (orchestrator might return False due to review warnings)
        if output_path.exists() and output_path.stat().st_size > 1000:
            update_job(
                job_id,
                status="completed",
                progress=100,
                message="Report generated successfully",
                file_id=job_id
            )
        elif success:
            update_job(
                job_id,
                status="completed",
                progress=100,
                message="Report generated successfully",
                file_id=job_id
            )
        else:
            update_job(
                job_id,
                status="failed",
                progress=0,
                message="Generation failed",
                error="Orchestrator execution failed - no output file created"
            )
        
        # Cleanup temp config
        if config_path.exists():
            config_path.unlink()
            
    except Exception as e:
        import traceback
        error_detail = f"{str(e)}\n{traceback.format_exc()}"
        print(f"Generation error for job {job_id}: {error_detail}")
        update_job(
            job_id,
            status="failed",
            progress=0,
            message="Generation failed",
            error=str(e)
        )


# ============================================================================
# FASTAPI APP
# ============================================================================

app = FastAPI(
    title="Report Generator API",
    description="API for generating professional reports",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        version="1.0.0",
        timestamp=datetime.now().isoformat()
    )


@app.post("/api/validate", response_model=ValidationResponse)
async def validate_config_endpoint(request: ValidationRequest):
    """Validate report configuration"""
    try:
        is_valid, errors = validate_config(request.config)
        
        warnings = []
        # Check for optional fields
        if not request.config.get("project_info", {}).get("advisor"):
            warnings.append("No advisor specified")
        
        return ValidationResponse(
            valid=is_valid,
            errors=errors,
            warnings=warnings
        )
    except Exception as e:
        return ValidationResponse(
            valid=False,
            errors=[str(e)]
        )


@app.post("/api/preview", response_model=PreviewResponse)
async def preview_outline(request: PreviewRequest):
    """Preview report outline without generating content"""
    try:
        # Validate first
        is_valid, errors = validate_config(request.config)
        if not is_valid:
            raise HTTPException(status_code=400, detail={"errors": errors})
        
        # Normalize config to legacy format for planner
        validator = InputValidator()
        normalized_config = validator.normalize(request.config)
        
        # Generate outline
        planner = OutlinePlanner()
        report = planner.plan(normalized_config)
        
        # Convert to dict
        outline = {
            "title": report.metadata.title,
            "sections": [
                {
                    "id": section.id,
                    "title": section.title,
                    "type": section.type.value if hasattr(section.type, 'value') else str(section.type),
                    "subsections": [
                        {
                            "id": sub.id,
                            "title": sub.title,
                            "type": sub.type.value if hasattr(sub.type, 'value') else str(sub.type)
                        }
                        for sub in section.subsections
                    ]
                }
                for section in report.sections
            ]
        }
        
        section_count = len(report.sections)
        estimated_pages = request.config.get("report_profile", {}).get("target_pages")
        
        return PreviewResponse(
            outline=outline,
            section_count=section_count,
            estimated_pages=estimated_pages
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/migrate-config", response_model=Dict[str, Any])
async def migrate_config_endpoint(request: Dict[str, Any]):
    """Migrate legacy config to v2 format"""
    try:
        # Try to load as v2 format first
        try:
            config = ReportConfig(**request)
            return {
                "migrated": False,
                "message": "Config is already in v2 format",
                "config": config.model_dump(mode='json', exclude_none=True)
            }
        except Exception:
            # Try legacy migration
            config = ReportConfig.from_legacy_config(request)
            return {
                "migrated": True,
                "message": "Config migrated from legacy format to v2",
                "config": config.model_dump(mode='json', exclude_none=True)
            }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Migration failed: {str(e)}")


@app.post("/api/generate", response_model=JobStatus)
async def generate_report(request: GenerateRequest, background_tasks: BackgroundTasks):
    """Start report generation job"""
    try:
        # Validate first
        is_valid, errors = validate_config(request.config)
        if not is_valid:
            raise HTTPException(status_code=400, detail={"errors": errors})
        
        # Create job
        job_id = create_job(request.config)
        
        # Start background task
        background_tasks.add_task(generate_report_task, job_id, request.config)
        
        job = get_job(job_id)
        return JobStatus(**job)
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/jobs/{job_id}", response_model=JobStatus)
async def get_job_status(job_id: str):
    """Get job status"""
    job = get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    return JobStatus(**job)


@app.get("/api/download/{file_id}")
async def download_report(file_id: str):
    """Download generated report"""
    file_path = OUTPUT_DIR / f"{file_id}_report.docx"
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(
        path=str(file_path),
        filename="report.docx",
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )


@app.post("/api/import-config", response_model=Dict[str, Any])
async def import_config(request: Dict[str, Any]):
    """Import and normalize config (supports legacy format)"""
    try:
        # Try to load as v2 format
        config = ReportConfig(**request)
        return config.model_dump(mode='json', exclude_none=True)
    except Exception:
        # Try legacy migration
        try:
            config = ReportConfig.from_legacy_config(request)
            return config.model_dump(mode='json', exclude_none=True)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid config format: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
