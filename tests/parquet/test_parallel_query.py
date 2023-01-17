"""Test Query for Repo."""
import timeit
from multiprocessing import cpu_count
from multiprocessing.pool import Pool

import pytest
import pandas as pd
from pyarrow import dataset as ds
# from pyarrow import dataset as ds

from blastoise.parquet import Repo


@pytest.mark.parametrize("path", [("/home/kratos/mock_data/")])
def test_repo_query(path):
    """Test Query for Repo."""
    repo = Repo(path)

    start = timeit.default_timer()
    df_set = []
    for i in range(100):
        df_set.append(query(repo, "mock_stocks_dir", ds.field("amount") == i + 30))
    end = timeit.default_timer()
    time1 = end - start

    start = timeit.default_timer()
    total_data = pd.concat(df_set, axis=0)
    end = timeit.default_timer()
    time2 = end - start

    start = timeit.default_timer()
    with Pool(processes=cpu_count()) as pool:
        df_set = pool.starmap(query, zip([repo for i in range(100)],
                                         ["mock_stocks_dir" for j in range(100)],
                                         [(ds.field("amount") == k) for k in range(30, 130)]))
    end = timeit.default_timer()
    time3 = end - start

    start = timeit.default_timer()
    total_data = pd.concat(df_set, axis=0)
    end = timeit.default_timer()
    time4 = end - start

    print("res: ====")
    print(time1)
    print(time2)
    print(time3)
    print(time4)

    for data in df_set:
        assert len(data.index) <= 20480000
    assert len(total_data.index) <= 204800000
    assert  time1 < 5
    assert time2 < 0.5
    assert  time3 < 5
    assert time4 < 0.5

def query(repo: Repo, table: str, filter_expr=None):
    """Helper query."""
    return repo.query(table, filter_expr=filter_expr)
