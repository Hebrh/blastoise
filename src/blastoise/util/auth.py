"""Connection authentication."""


class AuthenticationString(bytes):
    """Subclass bytes to avoid accidental transmission of auth keys over network."""

    def __reduce__(self):
        """Reduce."""
        # pylint: disable = import-outside-toplevel
        from multiprocessing.context import get_spawning_popen

        if get_spawning_popen() is None:
            raise TypeError(
                "Pickling an AuthenticationString object is "
                "disallowed for security reasons"
            )
        return AuthenticationString, (bytes(self),)
