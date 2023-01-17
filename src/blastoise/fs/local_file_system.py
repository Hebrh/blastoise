"""Utils for local file system."""
from pyarrow import fs
from pyarrow.fs import FileType

from .exception import FileInfoNotReasonable
from .hierarchy import Hierarchy


class FileInfo():
    """Simple file info data."""

    # pylint: disable = too-many-arguments
    def __init__(
        self, name: str, size: int=0,
        hierarchy: Hierarchy=Hierarchy.REPO,
        directory: bool=False,
        hadoop: bool=False
        ) -> None:
        """Constructor for FileInfo.

        Args:
            name (str): file or directory path
            hierarchy (Hierarchy): hierarchy
            directory (bool): true if it's directory
            hadoop (bool): is hadoop file system
        """
        if hierarchy == Hierarchy.FILE and directory:
            raise FileInfoNotReasonable()

        # adjust path not to end with slash
        if name.endswith("/"):
            name = name[0: len(name) - 1]
        self.name = name
        if size == 0:
            self.size = 0
        else:
            self.size = size / (1024 * 1024 * 1.0)
        self._hierarchy = hierarchy
        self._directory = directory
        self._hadoop = hadoop
        self._children = []

    @classmethod
    def repo(cls, path: str):
        """Static builder for repo path"""
        local = fs.LocalFileSystem()
        selector = fs.FileSelector(path, allow_not_found=True, recursive=True)
        file_infos = local.get_file_info(selector)
        parent_directory = FileInfo(path, directory=True)
        for file_info in file_infos:
            is_dir = file_info.type == FileType.Directory
            if is_dir:
                size = 0
            else:
                size = file_info.size
            parent_directory.add_child(file_info.path, size, is_dir)
        return parent_directory

    def is_dir(self) -> bool:
        """Whether it's directory."""
        return self._directory

    def hierarchy(self) -> Hierarchy:
        """Getter for hierarchy."""
        return self._hierarchy

    def descend_hierarchy(self, directory: bool) -> Hierarchy:
        """Descend hierarchy."""
        return self._hierarchy.descend(directory=directory, hadoop=self._hadoop)

    def add_child(self, name: str, size: int, directory: bool) -> None:
        """Add child for directory.

        Args:
            name (str): file or directory path
            directory (bool): true if it's directory
        """
        # pass if not a directory
        if not self._directory:
            return

        child_count = len(self._children)
        if child_count > 0:
            tail_child = self._children[child_count - 1]
            # tail add child
            if tail_child.is_dir() and name.startswith(tail_child.name + "/"):
                tail_child.add_child(name, size, directory)
                return

        self._children.append(FileInfo(name,  size, hierarchy=self.descend_hierarchy(directory),
                    directory=directory))

    def list_dir(self) -> list:
        """List the directory.
        Return empty list for file path.
        """
        return self._children

    def __repr__(self) -> str:
        return f"FileInfo:[path={self.name}, id_dir={self._directory}, hier={self._hierarchy}," \
            f"size={self.size}, hadoop={self._hadoop}, child={self._children}]"

    @classmethod
    def list_path(cls, path: str) -> list:
        """List file paths in a parent directory.
        or empty list if 'path' not exists.

        Args:
            path (str): a file path
        """
        return cls.repo(path).list_dir()
