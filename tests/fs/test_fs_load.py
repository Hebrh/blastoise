"""Test flow."""
import pytest

from blastoise.fs import FileInfo


@pytest.mark.parametrize("dir_path",
    [("/home/kratos/python_projects/x-extract/datasets/mock_data/")])
def test_file_system(dir_path):
    """Test Whole flow."""
    my_li = FileInfo.list_path(dir_path)
    assert len(my_li) == 27
