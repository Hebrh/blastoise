"""Test memory usage of loader."""
import time

import pytest

from blastoise.parquet import Repo


@pytest.mark.benchmark(
    group='loaded and idle'
)
def test_mem_loader1(benchmark):
    """Test memory usage of loader."""
    repo = Repo('/home/kratos/delibird_mock/mock_data/')
    benchmark.pedantic(time.sleep, args=(5,), iterations=1, rounds=1)


@pytest.mark.benchmark(
    group='loaded and idle'
)
def test_mem_loader2(benchmark):
    """Test memory usage of loader."""
    repo = Repo('/home/kratos/delibird_mock/mock_data/')
    benchmark.pedantic(nothing, args=(repo,), iterations=1, rounds=1)

def nothing(repo):
    """Noting to do."""
    time.sleep(5)
    return repo
