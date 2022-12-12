"""Util init."""
from .auth import AuthenticationString
from .calculate import Calculate
from .perf import timing
from .str import remove_head


__all__ = [
    "timing",
    "Calculate",
    "AuthenticationString",
    "remove_head"
]
