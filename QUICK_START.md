# Report Generator Web UI - Quick Start

## 🚀 Start in 3 Steps

### 1. Install Backend Dependencies
```bash
pip install -r requirements_api.txt
```

### 2. Start Backend (Terminal 1)
```bash
python run_api.py
```
✅ Backend running on http://localhost:8000

### 3. Start Frontend (Terminal 2)
```bash
cd web
npm install
npm run dev
```
✅ Frontend running on http://localhost:3000

## 🎯 Use the Application

1. Open http://localhost:3000 in your browser
2. Follow the 7-step wizard to create your report
3. Download the generated DOCX file

## 📝 Quick Test

Run the automated test:
```bash
./test_e2e.ps1
```

## 🛠️ Alternative Start Methods

### Windows Batch Files
```bash
# Terminal 1
start_backend.bat

# Terminal 2
start_frontend.bat
```

### PowerShell (Both Servers)
```bash
./start_servers.ps1
```

## ✅ Verify Installation

Backend health check:
```bash
curl http://localhost:8000/api/health
```

Expected response:
```json
{"status":"healthy","version":"1.0.0","timestamp":"..."}
```

## 📚 Full Documentation

See `WEB_UI_IMPLEMENTATION_SUMMARY.md` for complete details.

## 🎉 That's It!

You're ready to generate reports through the web interface!
