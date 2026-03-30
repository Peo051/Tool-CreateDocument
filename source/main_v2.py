#!/usr/bin/env python3
"""
COMPATIBILITY WRAPPER - DEPRECATED
This file is kept for backward compatibility only.
Please use source/main.py instead.

This wrapper simply forwards all calls to the official main.py entry point.
"""

import sys
import warnings
from pathlib import Path

# Show deprecation warning
warnings.warn(
    "main_v2.py is deprecated. Please use 'python source/main.py' or 'python -m source.main' instead.",
    DeprecationWarning,
    stacklevel=2
)

# Add source to path
sys.path.insert(0, str(Path(__file__).parent))

# Import and run the official main
from main import main

if __name__ == "__main__":
    main()
