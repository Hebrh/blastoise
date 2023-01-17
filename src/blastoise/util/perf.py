"""Performance calculate."""
from functools import wraps
from time import time


def timing(func):
    """Calcuate function execute time."""

    @wraps(func)
    def wrap(*args, **kw):
        start = time()
        result = func(*args, **kw)
        end = time()
        print(f"func:{func.__name__} took: {end-start:.4f} sec")
        return result

    return wrap
