"""Common helper function for parse."""


def is_misc_token(token):
    """Check if the token is not identifiers.

        Args:
            token (Token): token of a statement
        Return:
            bool
    """
    return token.is_keyword or token.is_whitespace
