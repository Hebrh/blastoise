"""Describe the SELECT sql."""


# pylint: disable = too-few-public-methods
class IdentifierDescriber():
    """Describer of identifiers in the sql."""

    def __init__(self, name, alias=None):
        """Constructor.

            Args:
                name (str): identifier name
                alias (str): alias of identifier name
        """
        self.name = name
        if alias is None or alias == '':
            self.alias = name
        else:
            self.alias = alias

    def __str__(self):
        """To string.

            Return: str
        """
        return f'IdentifierDescriber[name: {self.name}, alias: {self.alias}]'

    def __repr__(self):
        """Repr.

            Return: str
        """
        return self.__str__()

    def wash_alias(self, table_alias):
        """Wash away table alias in the field name.

            Args:
                table_alias (str): table alias
        """
        self.name = self.name.replace(f'{table_alias}.', '')
