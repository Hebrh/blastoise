"""Paruqet metadata loader."""
from itertools import repeat
from multiprocessing import cpu_count
from multiprocessing.pool import Pool

import pandas as pd
from pyarrow import dataset as ds
from pyarrow.dataset import Expression, Dataset

from blastoise.fs import FileInfo, Hierarchy
from blastoise.util import dir_to_name
from .exception import RepoDirectoryCantLoadAloneEception


class ParquetLoader:
    """Load metadata of paruqet files of the same struct in memory."""

    def __init__(self, file_info: FileInfo) -> None:
        """Constructor."""
        if file_info._hierarchy == Hierarchy.REPO:
            raise RepoDirectoryCantLoadAloneEception()

        # file or directory name to dataset name
        _path = file_info.name
        self.path = _path
        self.ds_name = dir_to_name(_path)
        self.size = file_info.size
        self.hierarchy = file_info._hierarchy
        self.directory = file_info._directory
        self.hadoop = file_info._hadoop
        self.dataset = ParquetLoader.load_dataset(file_info)

    @classmethod
    def load_dataset(cls, file_info: FileInfo):
        """Load file to dataset."""
        hier = file_info.hierarchy()
        if hier == Hierarchy.REPO:
            raise RepoDirectoryCantLoadAloneEception()

        return [ds.dataset(file_info.name, format="parquet")]

    @classmethod
    def load_repo(cls, file_info: FileInfo) -> list:
        """Load any parquet path to dataset."""
        if isinstance(file_info, list):
            res = []
            for file in file_info:
                res += cls.load_repo(file)
            return res
        if file_info.hierarchy() == Hierarchy.REPO:
            return [ParquetLoader(f) for f in file_info.list_dir()]
        return [ParquetLoader(file_info)]

    @classmethod
    def load_path(cls, path: str) -> list:
        """Load repo parquet path to dataset."""
        return cls.load_repo(FileInfo.repo(path))

    # pylint: disable = dangerous-default-value
    def query(self, columns=[], filter_expr: Expression=None):
        """Simple Query Helper."""
        ds_group = self.dataset
        group_size = len(ds_group)

        if group_size == 0:
            return None
        if group_size == 1:
            return _query_helper(ds_group[0], columns=columns, filter_expr=filter_expr)

        with Pool(processes=cpu_count()) as pool:
            result = pool.starmap(_query_helper, \
                zip(ds_group, repeat(columns), repeat(filter_expr)))
        return pd.concat(result, axis=0)



# pylint: disable = dangerous-default-value
def _query_helper(dataset: Dataset, columns, filter_expr: Expression):
    """Simple Query Helper."""
    return dataset.to_table(columns=columns, filter=filter_expr).to_pandas()
