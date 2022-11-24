"""Test ParquetLoader."""
import pytest

from blastoise.fs import FileInfo
from blastoise.parquet import ParquetLoader


@pytest.mark.parametrize("dir_path",
    [("/home/kratos/python_projects/x-extract/datasets/mock_data/")])
def test_load_parquet(dir_path):
    """Test loading parquet."""
    repo_info = FileInfo.repo(dir_path)
    loaders = ParquetLoader.load_repo(repo_info)
    assert len(loaders) == 27
    assert len(loaders[len(loaders) - 1].dataset) > 2
