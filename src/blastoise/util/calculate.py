"""Calculate context manager."""
from timeit import default_timer as timer


class Calculate:
    """Calculate class."""

    def __init__(self, name=None):
        """Init time record."""
        self._name = name
        self._start_time = None
        self._end_time = None

    def __enter__(self):
        """Enter."""
        self._start_time = timer()
        return self

    def __exit__(self, *args):
        """Exit."""
        self._end_time = timer()
        if self._name:
            print(
                f"{self._name} elapsed time: {self._end_time - self._start_time:.4f} sec"
            )
        else:
            print(f"elapsed time: {self._end_time - self._start_time:.4f} sec")
