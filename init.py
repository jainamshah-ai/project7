# utils/__init__.py
"""
Utils Package
A collection of custom modules for file operations and advanced mathematical utilities.
"""
from .file_ops import save_log, read_logs
from .math import calculate_compound_interest, calculate_area_circle

__all__ = ['save_log', 'read_logs', 'calculate_compound_interest', 'calculate_area_circle']