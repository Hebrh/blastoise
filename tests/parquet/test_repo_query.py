"""Test Query for Repo."""
import timeit

import pytest
# from pyarrow import dataset as ds

from blastoise.parquet import Repo


@pytest.mark.parametrize("path", [("/home/kratos/python_projects/x-extract/datasets/mock_data/")])
def test_repo_query(path):
    """Test Query for Repo."""
    repo = Repo(path)

    # dataset = ds\
    #     .dataset("/home/kratos/python_projects/x-extract/datasets/mock_data/mock_stocks_wtf", \
    #     format="parquet")

    start = timeit.default_timer()
    df1 = repo.query("mock_stocks_wtf")
    end = timeit.default_timer()
    time1 = end - start

    # start = timeit.default_timer()
    # df2 = dataset.to_table().to_pandas()
    # end = timeit.default_timer()
    # time2 = end - start

    print(time1)
    # print(time2)

    assert len(df1.index) == 20480000
    # assert len(df2.index) == 20480000
    # assert time1 < time2
    assert  time1 < 0.5
