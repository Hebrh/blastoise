# -*- coding: utf-8 -*-
try:
    from setuptools import find_packages, setup
except ImportError:
    import distribute_setup

    distribute_setup.use_setuptools()
    from setuptools import setup, find_packages

import os
import sys
from distutils import log

long_desc = """Blastoise is a python tool lib that helps reading and querying data from parquet files. After querying, you can stroe it in Plasma memory map and do some futher calculations."""

requires = ["pyarrow", "pandas"]

setup(
    name="blastoise",
    version="0.0.1",
    url="https://github.com/Hebrh/blastoise",
    license="MIT License",
    author="zhujw",
    author_email="kratoswittgenstein@gmail.com",
    description="a stream tool that helps you read and query data from parquet files",
    long_description=long_desc,
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
