"""Test ParquetLoader."""
import pytest

from catapult.fs import list_path
from catapult.parquet import ParquetLoader


@pytest.mark.parametrize("dir_path",
    [("/home/kratos/python_projects/x-extract/datasets/mock_data/")])
def test_load_parquet(dir_path):
    """Test loading parquet."""
    my_li = list_path(dir_path)
    loaders = ParquetLoader.load(my_li)
    assert len(loaders) == 27
    assert len(loaders[len(loaders) - 1].dataset) > 15
