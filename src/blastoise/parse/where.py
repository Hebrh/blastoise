"""Parse where statements."""
import datetime

import pyarrow.dataset as ds
from sqlparse.tokens import Token
from sqlparse.sql import Identifier, Where, Comparison, Parenthesis, TypedLiteral
from sqlparse.sql import Token as Tok

from blastoise.util import remove_head
from blastoise.parse import is_misc_token
from .logic import LogicExpression

IS_KEY = 'IS'
NULL_KEY = 'NULL'
NOT_NULL_KEY = 'NOT NULL'

LOGIC_MAP = {
    'OR': lambda tup: tup[0] | tup[1],
    'AND': lambda tup: tup[0] & tup[1]
}

MATH_MAP = {
    '>': lambda tup: tup[0] > tup[1],
    '=': lambda tup: tup[0] == tup[1],
    '<': lambda tup: tup[0] < tup[1],
    '>=': lambda tup: tup[0] >= tup[1],
    '<=': lambda tup: tup[0] <= tup[1],
    'in': lambda tup: tup[0].isin(tup[1]),
    IS_KEY: lambda tup: nullable(tup[0], tup[1])
}

VALUE_MAP = {
    Token.Literal.Number.Float: float,
    Token.Literal.Number.Integer: int,
    Token.Literal.String.Single: lambda v: wash_string(v),
    Token.Keyword: lambda v: wash_string(v)
}

# pylint: disable = unnecessary-lambda
TYPE_VALUE_MAP = {
    TypedLiteral: lambda t: parse_type_value(t),
    Parenthesis: lambda t: parse_in_value(t)
}

BUILTIN_MAP = {
    'date': lambda v: datetime.datetime.strptime(v, "'%Y-%m-%d'")
}

COMPARISON_LIST = [
    lambda args: parse_field_name(args[0], args[1]),
    lambda args: args[0].normalized,
    lambda args: parse_right_value(args[0])
]

WHERE_TYPE_MAP = {
    Tok: lambda args: args[0].normalized,
    Comparison: lambda args: parse_comparison(args[0], args[1]),
    Parenthesis: lambda args: parse_parenthesis(args[0], args[1]),
    Identifier: lambda args: parse_comparison_helper(args[0], args[1])
}

def wash_string(val):
    """Wash string value.

        Args:
            val (str): value
        Return:
            washed val
    """
    if not isinstance(val, str):
        return val
    cmp_char = val[0:1]
    while cmp_char == "'" or cmp_char == '"':
        val = val[1:]
        cmp_char = val[0:1]
    s_len = len(val)
    if s_len == 0:
        return val
    cmp_char = val[s_len-1:]
    while cmp_char == "'" or cmp_char == '"':
        val = val[:s_len-1]
        if s_len == 0:
            return val
        cmp_char = val[s_len-1:]
    return val


def nullable(field, key):
    """Field is null or not.

        Args:
            field (Field): Dataset Field
            key (str): key if null
        Return:
            Pyarrow Dataset Expression
    """
    if NULL_KEY == key:
        return field.is_null()
    if NOT_NULL_KEY == key:
        return field.is_valid()
    return None

def parse_field_name(token, table_describer):
    """Get token name.

        Args:
            token (Comparison): Identiifer Token of a Statement
            table_describer (IdentifierDescriber): table describer
        Return:
            Expression: Pyarrow Dataset Expression
    """
    col_name = remove_head(token.normalized, table_describer.alias)
    if col_name is None:
        return None
    return ds.field(col_name)

def parse_right_value(token):
    """Parse right values.

        Args:
            token (Token): Token
        Return:
            value
    """
    ttype = token.ttype
    if ttype is None:
        parse_type = TYPE_VALUE_MAP.get(type(token))
        if parse_type is not None:
            return parse_type(token)
    setter = VALUE_MAP.get(ttype)
    if setter is None:
        return None
    return setter(token.normalized)

def parse_where(token, table_describer):
    """Parse Where Token to Pyarrow Dataset Expression.

        Args:
            token (Where): Where Token of a Statement
            table_describer (IdentifierDescriber): table describer
        Return:
            Expression: Pyarrow Dataset Expression
    """
    if not isinstance(token, Where):
        return None
    tokens = list(filter(lambda e: not e.is_whitespace, token.tokens))[1:]
    return parse_where_helper(tokens, table_describer)

def parse_where_helper(tokens, table_describer):
    """Parse list of Where Token to Pyarrow Dataset Expression.

        Args:
            tokens (list of Where): list of Where Tokens of a Statement
            table_describer (IdentifierDescriber): table describer
        Return:
            Expression: Pyarrow Dataset Expression
    """
    if len(tokens) == 0:
        return None

    i = 0
    token_num = len(tokens)
    logic_keyword = None
    logic = LogicExpression()
    while i < token_num:
        element = tokens[i]
        ele_type = type(element)
        i += 1

        if ele_type == Identifier:
            ele_arg = [element, tokens[i], tokens[i+1]]
            i += 2
        else:
            ele_arg = element

        parse = WHERE_TYPE_MAP.get(ele_type)
        if parse is None:
            continue
        sub_exp = parse((ele_arg, table_describer))

        if ele_type == Tok:
            logic_keyword = sub_exp
            continue

        if sub_exp is not None:
            logic.logic(sub_exp, logic_keyword)

    return logic.final_expr()

def parse_parenthesis(token, table_describer):
    """Parse Parenthesis Token to Pyarrow Dataset Expression.

        Args:
            token (Parenthesis): Parenthesis Token of a Statement
            table_describer (IdentifierDescriber): table describer
        Return:
            Expression: Pyarrow Dataset Expression
    """
    tokens = list(filter(lambda t: not t.is_whitespace, token.tokens))
    if len(tokens) < 3:
        return None
    tokens = tokens[1:len(tokens)-1]

    return parse_where_helper(tokens, table_describer)

def parse_comparison(token, table_describer):
    """Parse Comparison Token to Pyarrow Dataset Expression.

        Args:
            token (Comparison): Comparison Token of a Statement
            table_describer (IdentifierDescriber): table describer
        Return:
            Expression: Pyarrow Dataset Expression
    """
    tokens = list(filter(lambda t: not is_misc_token(t), token.tokens))

    return parse_comparison_helper(tokens, table_describer)

def parse_comparison_helper(tokens, table_describer):
    """Parse Comparison Token list to Pyarrow Dataset Expression.

        Args:
            tokens (list of Comparison): list of Comparison Token of a Statement
            table_describer (IdentifierDescriber): table describer
        Return:
            Expression: Pyarrow Dataset Expression
    """
    token_count = len(tokens)
    if len(tokens) < 3:
        return None

    i = 0
    ele_list = [None, None, None]
    while i < token_count and i < len(COMPARISON_LIST):
        func = COMPARISON_LIST[i]
        args_tup = (tokens[i], table_describer)
        ele = func(args_tup)
        if ele is None:
            return None
        ele_list[i] = ele
        i += 1

    math_symbol = ele_list[1]
    math_func = MATH_MAP.get(math_symbol)
    if math_func is None:
        return None
    return math_func((ele_list[0], ele_list[2]))

def parse_type_value(token):
    """Parse TypedLiteral right value.

        Args:
            token (TypeLiteral): TypeLiteral Token
        Return:
            value
    """
    tokens = list(filter(lambda t: not is_misc_token(t), token.tokens))
    func = parse_builtin(tokens[0])
    value = parse_right_value(tokens[1])

    if func is None or value is None:
        return None
    return func(value)

def parse_in_value(token):
    """Parse right value for in statement.

        Args:
            token (Parenthesis): Parenthesis Token
        Return:
            value list
    """
    tokens = token.tokens
    if len(tokens) < 3:
        return None
    identifiers = list(filter(lambda t: not is_misc_token(t), tokens[1].tokens))

    value_list = []
    for identifier in identifiers:
        val = parse_right_value(identifier)
        if val is not None:
            value_list.append(val)
    return value_list

def parse_builtin(token):
    """Parse Builtin Token to lambda function.

        Args:
            token (Builtin): Builtin Token
        Return:
            lambda
    """
    if Token.Name.Builtin != token.ttype:
        return None
    return BUILTIN_MAP.get(token.normalized)
