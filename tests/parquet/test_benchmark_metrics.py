"""Test Query for Repo.
        Run: py.test --benchmark-only --benchmark-save-data ./tests/parquet/test_benchmark.py
"""
import pytest

from blastoise.parquet import Repo


repo = Repo('/home/kratos/delibird_mock/data/')

@pytest.mark.benchmark(
    group='Read 10 times'
)
def test_benchmark_metrics(benchmark):
    """Test Query for Repo."""

    benchmark.pedantic(repo.query,
    args=("SELECT SRC_SECU_CODE, PRICE_DATE, F_NAV_ADJUSTED"\
        " FROM T02_FUND_NAV_QUOTATION WHERE PRICE_DATE >= 20180329"\
            " AND  PRICE_DATE <=  20180329",),
            kwargs={}, iterations=500, rounds=1)
