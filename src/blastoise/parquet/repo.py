"""Repository of ParuqetLoader, map to table name"""
from blastoise.parquet import ParquetLoader
from blastoise.parse import parse_select


# pylint: disable = too-few-public-methods
class Repo:
    """Repository of ParuqetLoader."""

    def __init__(self, path: str) -> None:
        """Constructor."""
        loaders = ParquetLoader.load_path(path)
        loader_mapper = {}
        for loader in loaders:
            loader_mapper[loader.ds_name] = loader

        self._loaders = loaders
        self._loader_mapper = loader_mapper

    # pylint: disable = dangerous-default-value
    def query(self, table: str, columns=[], filter_expr=None):
        """Query func.

            Args:
                table (str): table name or sql statement
                columns (list of str): select table column name list
                filter_expr (Expression): Expression that filter the result (where)
        """
        if table is None:
            return None
        table_describer, select_fields, where_expr = parse_select(table)
        if table_describer is not None:
            table = table_describer.name
            columns = [f.name for f in select_fields]
            filter_expr = where_expr
        _loader = self._loader_mapper[table]
        if _loader is None:
            return None
        return _loader.query(columns=columns, filter_expr=filter_expr)
