"""
config.py
~~~~~~~~~

Project configuration data.
"""
from collections import namedtuple
from pathlib import Path


def _project_path() -> Path:
    """Return file system path for current project."""
    return Path(__file__).parent.parent


DataPaths = namedtuple('DataPaths', ['raw', 'interim', 'processed'])
DATA_PATHS = DataPaths(
    raw=_project_path() / 'data/raw',
    interim=_project_path() / 'data/interim',
    processed=_project_path() / 'data/processed',
)

ReportPaths = namedtuple('ReportPaths', ['reports', 'figures'])
REPORT_PATHS = ReportPaths(
    reports=_project_path() / 'reports',
    figures=_project_path() / 'reports/figures',
)
