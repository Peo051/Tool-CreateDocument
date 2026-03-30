#!/usr/bin/env python3
"""
Run FastAPI server
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "source.api:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
