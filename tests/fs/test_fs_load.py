"""Test flow."""
import pytest

from catapult.fs import list_path


@pytest.mark.parametrize("dir_path",
    [("/home/kratos/python_projects/x-extract/datasets/mock_data/")])
def test_file_system(dir_path):
    """Test Whole flow."""
    my_li = list_path(dir_path)
    print(my_li)
    assert len(my_li) == 27
