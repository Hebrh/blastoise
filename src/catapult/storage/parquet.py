from pathlib import Path

from pyarrow import dataset as ds







if __name__ == "__main__":
    directory = Path("/home/kratos/python_projects/x-extract/datasets/mock_data/mock_stocks_wtf")
    parquet_files = [par for par in directory.iterdir() if par.is_file() and par.suffix == ".parquet"]

    file_count = len(parquet_files)

    dataset = ds.dataset(parquet_files[0: min(10, file_count)], format="parquet")

    print(dataset.count_rows())
    print(dataset.to_table(filter=(ds.field("amount") == 33)).to_pandas())
