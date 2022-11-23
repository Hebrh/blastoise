"""Utils for local file system."""
from pyarrow import fs
from pyarrow.fs import FileType

from .exception import FileInfoNotReasonable
from .hierarchy import Hierarchy


class FileInfo():
    """Simple file info data."""

    def __init__(
        self, name: str,
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
        self._hierarchy = hierarchy
        self._directory = directory
        self._hadoop = hadoop
        self._children = []

    def is_dir(self) -> bool:
        """Whether it's directory."""
        return self._directory

    def descend_hierarchy(self, directory: bool) -> Hierarchy:
        """Descend hierarchy."""
        return self._hierarchy.descend(directory=directory, hadoop=self._hadoop)

    def add_child(self, name: str, directory: bool) -> None:
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
                tail_child.add_child(name, directory)
                return

        self._children.append(FileInfo(name, hierarchy=self.descend_hierarchy(directory), directory=directory))

    def list_dir(self) -> list:
        """List the directory.
        Return empty list for file path.
        """
        return self._children

    def __repr__(self) -> str:
        return f"FileInfo:[path={self.name}, id_dir={self._directory}, hier={self._hierarchy}," \
            f"hadoop={self._hadoop}, child={self._children}]"


def list_path(path: str) -> list:
    """List file paths in a parent directory.
    or empty list if 'path' not exists.

    Args:
        path (str): a file path
    """
    local = fs.LocalFileSystem()
    selector = fs.FileSelector(path, allow_not_found=True, recursive=True)
    file_infos = local.get_file_info(selector)
    parent_directory = FileInfo(path, directory=True)
    for file_info in file_infos:
        parent_directory.add_child(file_info.path, file_info.type == FileType.Directory)
    return parent_directory.list_dir()
