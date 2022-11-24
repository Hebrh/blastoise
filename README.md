# Blastoise: a stream tool that helps you read and query data from parquet files

## Introduction:

Blastoise is a python tool lib that helps reading and querying data from parquet files.
After querying, you can stroe it in Plasma memory map and do some futher calculations.

## Features:

- Multiprocessing: Read parquet files with a process pool if it's necessary.
- Plasma Memory-map: store data into Plasma memory-map.

## Installation

### Source

```bash
$ git clone https://github.com/Hebrh/blastoise.git
$ cd blastoise
$ pip install -e .
```

### Pypi

```bash
$ pip install blastoise
```
