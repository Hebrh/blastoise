"""Test Query for Repo.
        Run: py.test ./tests/parquet/test_where_one.py --benchmark-histogram --benchmark-sort='name'
"""
import pytest

from blastoise.parquet import Repo


repo = Repo('/home/kratos/delibird_mock/mock_data/')

@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_00(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one",), kwargs={}, iterations=1, rounds=10)



@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_01_0(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount >= 0",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_02_10(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount >= 10",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_03_20(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount >= 20",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_04_30(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount >= 30",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_05_40(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount >= 40",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_06_50(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount >= 50",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_07_60(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount >= 60",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_08_70(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount >= 70",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_09_80(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount >= 80",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_10_90(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount >= 90",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_11_100(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount >= 100",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_12_0(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount <= 0",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_13_10(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount <= 10",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_14_20(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount <= 20",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_15_30(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount <= 30",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_16_40(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount <= 40",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_17_50(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount <= 50",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_18_60(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount <= 60",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_19_70(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount <= 70",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_20_80(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount <= 80",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_21_90(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount <= 90",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_22_100(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount <= 100",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_23_0(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount = 0",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_24_30(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount = 30",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_25_70(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount = 70",), kwargs={}, iterations=1, rounds=10)


@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_26_100(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query, args=("select * from mock_dir_one where amount = 100",), kwargs={}, iterations=1, rounds=10)
