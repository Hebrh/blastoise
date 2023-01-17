"""Test clean sql."""
from blastoise.parse import clean_sql


def test_clean_table():
    """Test clean table name."""
    table_name = 't_user'
    clean = clean_sql(table_name)

    assert clean == table_name
