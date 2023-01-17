"""Singleton Parquet Repo."""
from threading import Lock

from blastoise.parquet import Repo

class RepoSingleton(Repo):
    """Singleton class for Repo."""

    _instance = None
    lock = Lock()

    #pylint: disable = unused-argument
    def __new__(cls, *args, **kwargs):
        """Rewrite __new__ for singleton."""
        if cls._instance:
            return cls._instance
        else:
            with cls.lock:
                if cls._instance:
                    return cls._instance
                cls._instance = super().__new__(cls)
                return cls._instance

    def __init__(self):
        """Constructor."""
        path = '/home/kratos/delibird_mock/data'
        super(RepoSingleton, self).__init__(path)
