from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='catapult',
      version=version,
      description="Reading Parquet files with sql using Ballista",
      long_description="""\
Reading Parquet files with sql using Ballista""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='parquet sql Ballista',
      author='zhujw',
      author_email='kratoswittgenstein@gmail.com',
      url='',
      license='Apache',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
