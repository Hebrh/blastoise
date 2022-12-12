"""Parse select."""
import sqlparse
from sqlparse.tokens import Token
from sqlparse.sql import IdentifierList, Identifier

from blastoise.parse import IdentifierDescriber, is_misc_token, parse_where


TYPE_SELECT = 'SELECT'

def parse_select(raw):
    """Parse select sql.

        Args:
            raw (str): raw sql statement.
    """
    if not raw and raw == '':
        return None

    # split multiple sql statements
    statements = sqlparse.split(raw)
    if len(statements) == 0:
        return None

    # only one statement and parse it
    sql = statements[0]
    parsed = sqlparse.parse(sql)

    # Check if parsed to empty Token
    if is_empty_parsed(parsed):
        return None
    single_parsed = parsed[0]

    # Check if this statement is 'SELECT'
    if not is_select_parsed(single_parsed):
        return None

    identifier_count = 0
    select_fields = []
    tokens = list(filter(lambda e: not is_misc_token(e), single_parsed.tokens))
    for token in tokens:
        # Get field and table name
        match = put_identifier_names(token, select_fields)
        if match:
            # count identifier match nums.
            identifier_count += 1
            # when count to 2, means got the table name.
            if identifier_count == 2:
                table_describer = select_fields.pop()
                wash_alias(select_fields, table_describer)
            continue

        where_expr = parse_where(token, table_describer)
        if where_expr is not None:
            break

    return table_describer, select_fields, where_expr

def wash_alias(select_fields, table_describer):
    """Wash away alias in the name of IdentifierDescriber in the list.

        Args:
            select_fields (list of IdentifierDescriber): IdentifierDescriber list
            table_describer (IdentifierDescriber): IdentifierDescriber of Table
    """
    table_alias = table_describer.alias
    for describer in select_fields:
        describer.wash_alias(table_alias)

def put_identifier_names(token, select_fields):
    """Put Indentifier name in the list.

        Args:
            token (Token): Identifier or IdentifierList Token of a Statement
            select_fields (list of IndetifierDescriber): list
        Return:
            bool: if token is Identifier or IdentifierList
    """
    identifiers = token_to_identifers(token)
    # not Identifier or has no child tokens
    if len(identifiers) == 0:
        return False

    for identifier in identifiers:
        describer = get_identifier_name(identifier)
        if describer is not None:
            select_fields.append(describer)
    return True

def get_identifier_name(identifier):
    """Get the name of the Identifier.

        Args:
            identifier (Identifier): Identifier Token of a Statement.
        Return:
            name (str)
    """
    name_tokens = list(filter(lambda t: not is_misc_token(t), identifier.tokens))
    name_len = len(name_tokens)
    # return None for empty Identifier
    if name_len == 0:
        return None
    # only identifier name
    if name_len == 1:
        return IdentifierDescriber(name_tokens[0].value)
    # identifier name and alias
    return IdentifierDescriber(name_tokens[0].value, name_tokens[1].value)

def token_to_identifers(token):
    """Token to IdentiferList.

        Args:
            token (Token): token of a statement
        Return:
            list of Identifier
    """
    if isinstance(token, IdentifierList):
        return list(filter(lambda t: isinstance(t, Identifier), token.tokens))
    if isinstance(token, Identifier):
        return [token]
    return []

def is_empty_parsed(parsed):
    """Check if the parsed statement list is empty.

        Args:
            parse (list of Statement): parsed statement list
        Return:
            bool
    """
    return len(parsed) == 0 or len(parsed[0].tokens) == 0

def is_select_parsed(single_parsed):
    """Check if the input single statement is a SELECT statement.

        Args:
            single_parsed (Statement): single parsed statement
        Return:
            bool
    """
    is_dml = single_parsed.tokens[0].ttype == Token.Keyword.DML
    is_select = single_parsed.get_type() == TYPE_SELECT
    return is_dml and is_select

# if __name__ == '__main__':
#     RAW = '''
#     select t.a as c, t.b from t_test t where t.a > 3 or (t.a<'a' and t.b in (1.2,2,3))
#       and a is null or d is not null and e > date '2022-10-22'
#     '''
#     table, fields, where = parse_select(RAW)
#     print(table)
#     print(fields)
#     print(where)
