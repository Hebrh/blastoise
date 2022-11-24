"""Repository of ParuqetLoader, map to table name"""
from pyarrow.dataset import Expression

from .loader import ParquetLoader


# pylint: disable = too-few-public-methods
class Repo:
    """Repository of ParuqetLoader"""

    def __init__(self, path: str) -> None:
        """Constructor."""
        loaders = ParquetLoader.load_path(path)
        loader_mapper = {}
        for loader in loaders:
            loader_mapper[loader.ds_name] = loader

        self._loaders = loaders
        self._loader_mapper = loader_mapper

    # pylint: disable = dangerous-default-value
    def query(self, table: str, columns=[], filter_expr: Expression=None):
        """Query func."""
        if table is None:
            return None
        _loader = self._loader_mapper[table]
        if _loader is None:
            return None
        return _loader.query(columns=columns, filter_expr=filter_expr)
