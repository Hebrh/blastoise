py.test ./tests/parquet/test_where_one.py --benchmark-histogram --benchmark-sort='name'
py.test ./tests/parquet/test_where_two.py --benchmark-histogram --benchmark-sort='name'
py.test ./tests/parquet/test_where_three.py --benchmark-histogram --benchmark-sort='name'
py.test ./tests/parquet/test_where_five.py --benchmark-histogram --benchmark-sort='name'
