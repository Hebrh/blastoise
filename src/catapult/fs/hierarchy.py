"""Hierarchy of parquet file system."""
from enum import Enum


class Hierarchy(Enum):
    """Hierarchy enum of parquet file system."""

    REPO, SET, HADOOP_SET, HADDOP_PARTITION, FILE = range(5)

    def descend(self, directory: bool=False,
                hadoop: bool=False) -> Enum:
        """Descend hierarchy.

        Args:
            hierarchy (Hierarchy): ancestor hierarchy
            directory (bool): is dir?
            haddop (bool): is hadoop?
        """
        # not directory, then must be file
        if not directory:
            return Hierarchy.FILE

        hierarchy = self.value
        if hierarchy == Hierarchy.REPO.value:
            if hadoop:
                return Hierarchy.HADOOP_SET
            return Hierarchy.SET
        if hierarchy == Hierarchy.HADOOP_SET.value:
            return Hierarchy.HADDOP_PARTITION
        return Hierarchy.FILE
