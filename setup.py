# -*- coding: utf-8 -*-
try:
    from setuptools import find_packages, setup
except ImportError:
    import distribute_setup

    distribute_setup.use_setuptools()
    from setuptools import setup, find_packages

import os
import sys
import sysconfig
from distutils import log
from setuptools.command.build_py import build_py as _build_py

import numpy as np
from Cython.Build import cythonize


EXCLUDE_FILES = []


def get_ext_paths(root_dir, exclude_files):
    """get filepaths for compilation"""
    paths = []

    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            if os.path.splitext(filename)[1] != '.py':
                continue

            file_path = os.path.join(root, filename)
            if file_path in exclude_files:
                continue

            paths.append(file_path)
        for sub_dir in dirs:
            sub_paths = get_ext_paths(sub_dir, exclude_files)
            for d in sub_paths:
                paths.append(d)
    return paths


# noinspection PyPep8Naming
class build_py(_build_py):

    def find_package_modules(self, package, package_dir):
        ext_suffix = sysconfig.get_config_var('EXT_SUFFIX')
        modules = super().find_package_modules(package, package_dir)
        filtered_modules = []
        for (pkg, mod, filepath) in modules:
            if os.path.exists(filepath.replace('.py', ext_suffix)):
                continue
            filtered_modules.append((pkg, mod, filepath, ))
        return filtered_modules

long_desc = """Blastoise is a python tool lib that helps reading and querying data from parquet files. After querying, you can stroe it in Plasma memory map and do some futher calculations."""

requires = [
    'pyarrow==10.0.0',
    'pandas==1.5.2',
    'sqlparse==0.4.3'
]

setup(
    name="blastoise",
    version="0.1.0",
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
    include_dirs=np.get_include(),
    install_requires=requires,
    ext_modules=cythonize(
        get_ext_paths('blastoise', EXCLUDE_FILES),
        compiler_directives={'language_level': 3}
    ),
    # cmdclass={
    #     'build_py': build_py
    # }
)
