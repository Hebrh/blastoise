"""Test Query for Repo."""
import timeit

import pytest
# from pyarrow import dataset as ds

from blastoise.parquet import Repo


@pytest.mark.parametrize("path", [("/home/kratos/delibird_mock/mock_data/")])
def test_repo_query(path):
    """Test Query for Repo."""
    repo = Repo(path)

    start = timeit.default_timer()
    df1 = repo.query("mock_dir_five")
    end = timeit.default_timer()
    time1 = end - start

    start = timeit.default_timer()
    df2 = repo.query("select * from mock_dir_five where amount > 10")
    end = timeit.default_timer()
    time2 = end - start

    print(time1)
    print(time2)

    assert len(df1.index) == 50000000
    assert len(df2.index) < 50000000
    assert  time1 < 0.5
