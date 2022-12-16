"""Cache utils."""
import time


SQL_STAMP_MAPPER = {}
CACHE_TTL = 600

def map_sql_stamp(sql: str):
    """Map sql to c stamp.

        Args:
            sql (str): sql key
        Return:
            stamp
    """
    current_stamp = SQL_STAMP_MAPPER.get(sql)
    if current_stamp is None:
        return map_helper(sql)
    now_stamp = time.time()
    if (now_stamp - current_stamp) > CACHE_TTL:
        SQL_STAMP_MAPPER.pop(sql, None)
        return map_helper(sql)
    return current_stamp


def map_helper(sql: str):
    """Helper func for mapping sql to timestamp.

        Args:
            sql (str): sql key
        Return:
            stamp
    """
    current_stamp = time.time()
    SQL_STAMP_MAPPER[sql] = current_stamp
    return current_stamp
