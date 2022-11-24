"""Test Query for Repo."""
import timeit

import pytest

from blastoise.parquet import Repo
from blastoise.fs import FileInfo


# pylint: disable = unused-argument
@pytest.mark.parametrize("path", [("/home/kratos/python_projects/x-extract/datasets/mock_data/")])
def test_repo_query(path):
    """Test Query for Repo."""
    count_dict = {}
    # for i in range(50):
    #     time_cost, pot_size = test_roll_query(path, i + 1)
    #     _tup = count_dict.get(pot_size)
    #     if _tup is None:
    #         total_cost = 0
    #         size_count = 0
    #     else:
    #         total_cost, size_count = _tup
    #     total_cost += time_cost
    #     size_count += 1
    #     count_dict[pot_size] = (total_cost, size_count)

    # for key, val in count_dict.items():
        # count_dict[key] = (val[0] / 50, val[1])
    print(count_dict)

    assert False

def test_single_query(path):
    """Func for time cost test."""
    repo = Repo(path)

    start = timeit.default_timer()
    # pylint: disable = unused-variable
    table = repo.query("mock_stocks_wtf")
    end = timeit.default_timer()
    time_cost = end - start

    return time_cost

def test_roll_query(path, round_i):
    """Rolling the test"""
    print(f"=======Round {round_i}=======")
    min_time = 1000000
    pot_size = 0
    for i in range(1, 41):
        FileInfo.buf = i * 10
        time_cost = test_single_query(path)
        print(FileInfo.buf, time_cost)
        if min_time > time_cost:
            min_time = time_cost
            pot_size = FileInfo.buf
    print(min_time, pot_size)
    return min_time, pot_size
