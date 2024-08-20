"""
A Python package for card games.
"""

from pathlib import Path as _Path
import toml as _toml

_data = _toml.load(_Path(__file__).parent.parent / "pyproject.toml")
__version__ = _data["project"]["version"]
