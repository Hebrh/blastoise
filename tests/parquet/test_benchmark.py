"""Test Query for Repo.
        Run: py.test --benchmark-only --benchmark-save-data ./tests/parquet/test_benchmark.py
"""
import pytest

from blastoise.parquet import Repo


repo = Repo('./datasets/mock_data/')

@pytest.mark.benchmark(
    group='Read 1000 times'
)
def test_benchmark_one(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_one",), kwargs={}, iterations=1000, rounds=100)


@pytest.mark.benchmark(
    group='Read 1000 times'
)
def test_benchmark_two(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_two",), kwargs={}, iterations=1000, rounds=100)


@pytest.mark.benchmark(
    group='Read 1000 times'
)
def test_benchmark_three(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_three",), kwargs={}, iterations=1000, rounds=100)


@pytest.mark.benchmark(
    group='Read 1000 times'
)
def test_benchmark_five(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_five",), kwargs={}, iterations=1000, rounds=100)


@pytest.mark.benchmark(
    group='Read 5000 times'
)
def test_bench_one(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_one",), kwargs={}, iterations=5000, rounds=100)


@pytest.mark.benchmark(
    group='Read 5000 times'
)
def test_bench_two(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_two",), kwargs={}, iterations=5000, rounds=100)


@pytest.mark.benchmark(
    group='Read 5000 times'
)
def test_bench_three(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_three",), kwargs={}, iterations=5000, rounds=100)


@pytest.mark.benchmark(
    group='Read 5000 times'
)
def test_bench_five(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_five",), kwargs={}, iterations=5000, rounds=100)
