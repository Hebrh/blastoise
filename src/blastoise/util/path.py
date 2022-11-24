"""Path utils."""
import os


def dir_to_name(dir_path: str) -> str:
    """full file path to a simple name"""
    _split = dir_path.split(os.sep)
    _full_name = _split[len(_split) - 1]
    _dot_index = _full_name.find(".")
    if _dot_index > -1:
        _full_name = _full_name[0: _dot_index]
    return _full_name
