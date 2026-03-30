# Report Generator Web UI

Complete FastAPI + React wizard UI for the report generator.

## Architecture

### Backend (FastAPI)
- `source/api.py` - REST API endpoints
- Reuses existing orchestrator, config models, renderers
- In-memory job storage (MVP)
- Background task processing

### Frontend (React + TypeScript)
- 7-step wizard flow
- Zustand state management with localStorage persistence
- Tailwind CSS styling
- Config import/export support

## Setup

### 1. Install Backend Dependencies

```bash
pip install -r requirements_api.txt
```

### 2. Install Frontend Dependencies

```bash
cd web
npm install
```

## Run

### Start Backend (Terminal 1)

```bash
python run_api.py
```

Backend runs on http://localhost:8000

### Start Frontend (Terminal 2)

```bash
cd web
npm run dev
```

Frontend runs on http://localhost:3000

## Usage

1. Open http://localhost:3000
2. Follow the 7-step wizard:
   - Step 1: Select report type and language
   - Step 2: Enter project information
   - Step 3: Add technical data (algorithms, technologies)
   - Step 4: Add references
   - Step 5: Configure format options
   - Step 6: Review and validate configuration
   - Step 7: Generate and download report

## Features

- Wizard-based input (no manual JSON editing)
- Real-time validation
- Config import/export (supports legacy format)
- Background job processing with progress tracking
- Draft persistence in localStorage
- Download generated DOCX files

## API Endpoints

- `GET /api/health` - Health check
- `POST /api/validate` - Validate config
- `POST /api/generate` - Start generation job
- `GET /api/jobs/{job_id}` - Get job status
- `GET /api/download/{file_id}` - Download report
- `POST /api/import-config` - Import config (handles legacy)

## File Structure

```
source/
  api.py                    # FastAPI backend
web/
  src/
    api/
      client.ts             # API client
    components/
      Wizard.tsx            # Main wizard
      StepIndicator.tsx     # Progress indicator
      StepNav.tsx           # Navigation buttons
      ConfigImport.tsx      # Import/export
      steps/
        Step1Type.tsx       # Report type selection
        Step2Info.tsx       # Project info form
        Step3Tech.tsx       # Technical data
        Step4References.tsx # References form
        Step5Format.tsx     # Format options
        Step6Review.tsx     # Validation
        Step7Export.tsx     # Generation & download
    store/
      reportStore.ts        # Zustand state
    types/
      report.ts             # TypeScript types
    App.tsx
    index.tsx
```

## Notes

- Backend saves files to `output/api/`
- Frontend state persists in browser localStorage
- Job storage is in-memory (resets on server restart)
- For production: add database, authentication, file cleanup
