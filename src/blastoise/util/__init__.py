"""Util init."""
from .auth import AuthenticationString
from .calculate import Calculate
from .perf import timing
from .str import remove_head
from .path import dir_to_name


__all__ = [
    "timing",
    "Calculate",
    "AuthenticationString",
    "remove_head",
    'dir_to_name'
]
