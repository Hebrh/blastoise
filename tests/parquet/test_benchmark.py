"""Test Query for Repo."""
import pytest

from blastoise.parquet import Repo


repo = Repo('./datasets/mock_data/')

@pytest.mark.benchmark(
    group='read_1000'
)
def test_benchmark_one(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_one",), kwargs={}, iterations=1000, rounds=100)


@pytest.mark.benchmark(
    group='read_1000'
)
def test_benchmark_two(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_two",), kwargs={}, iterations=1000, rounds=100)


@pytest.mark.benchmark(
    group='read_1000'
)
def test_benchmark_three(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_three",), kwargs={}, iterations=1000, rounds=100)


@pytest.mark.benchmark(
    group='read_1000'
)
def test_benchmark_five(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_five",), kwargs={}, iterations=1000, rounds=100)


@pytest.mark.benchmark(
    group='read_5000'
)
def test_bench_one(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_one",), kwargs={}, iterations=5000, rounds=100)


@pytest.mark.benchmark(
    group='read_5000'
)
def test_bench_two(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_two",), kwargs={}, iterations=5000, rounds=100)


@pytest.mark.benchmark(
    group='read_5000'
)
def test_bench_three(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_three",), kwargs={}, iterations=5000, rounds=100)


@pytest.mark.benchmark(
    group='read_5000'
)
def test_bench_five(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("mock_dir_five",), kwargs={}, iterations=5000, rounds=100)
