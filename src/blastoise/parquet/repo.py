"""Repository of ParuqetLoader, map to table name"""
from functools import lru_cache

from pyarrow.dataset import Expression

from blastoise.parquet import ParquetLoader
from blastoise.parse import clean_sql, parse_select
from blastoise.util import map_sql_stamp


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
    def query(self, table_or_sql: str, columns=[], filter_expr: Expression=None, use_cache=True):
        """Query func.

            Args:
                table_or_sql (str): table name or sql statement
                columns (list of str): select table column name list
                filter_expr (Expression): Expression that filter the result (where)
                use_cache (bool): whether use cache
            Return:
                Dataframe
        """
        if table_or_sql is None:
            return None
        table_or_sql = clean_sql(table_or_sql)
        no_selected_columns = columns is None or len(columns) == 0
        no_filter = filter_expr is None
        if no_selected_columns and no_filter and use_cache:
            return self.query_with_cache(table_or_sql, map_sql_stamp(table_or_sql))
        return self.query_helper(table_or_sql, columns, filter_expr)

    def query_helper(self, table_or_sql: str, columns=[], filter_expr: Expression=None):
        """Query func helper.

            Args:
                table_or_sql (str): table name or sql statement
                columns (list of str): select table column name list
                filter_expr (Expression): Expression that filter the result (where)
        """
        table_describer, select_fields, where_expr = parse_select(table_or_sql)
        if table_describer is not None:
            table = table_describer.name
            columns = [f.name for f in select_fields]
            filter_expr = where_expr
        _loader = self._loader_mapper[table]
        if _loader is None:
            return None
        return _loader.query(columns=columns, filter_expr=filter_expr)

    @lru_cache(maxsize=12, typed=True)
    def query_with_cache(self, table_or_sql: str, stamp):
        """Query func helper.

            Args:
                table_or_sql (str): table name or sql statement
                stamp (float): just for cache time strategy
        """
        del stamp
        return self.query_helper(table_or_sql)
