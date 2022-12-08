"""Test Query for Repo.
        Run: py.test --benchmark-only --benchmark-save-data ./tests/parquet/test_benchmark.py
"""
import pytest

from blastoise.parquet import Repo


repo = Repo('./datasets/mock_data/')

@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_one(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_one",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_two(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_two",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_three(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_three",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_five(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_five",), kwargs={}, iterations=1, rounds=10)
