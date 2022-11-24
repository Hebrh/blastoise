"""Paruqet metadata loader."""
from pyarrow import dataset as ds

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

        if hier == Hierarchy.SET:
            return [ds.dataset([info.name for info in file_group], format="parquet") \
                    for file_group in file_info.spllit_dir()]

        return [ds.dataset(file_info.name, format="parquet")]

    @classmethod
    def load(cls, file_info: FileInfo | list) -> list:
        """Load any parquet path to dataset."""
        if isinstance(file_info, list):
            res = []
            for file in file_info:
                res += cls.load(file)
            return res
        if file_info.hierarchy() == Hierarchy.REPO:
            return [ParquetLoader(f) for f in file_info.list_dir()]
        return [ParquetLoader(file_info)]
