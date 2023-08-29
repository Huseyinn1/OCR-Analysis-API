from ocr_analysis.cache.redis_config import redis_client

def cache_result(key,result):
    """
    Creates a cache using the specified key and result.

    Args:
        key (str): Cache key used to determine the result.
        result: Result data to be cached.

    Returns:
        None
    """

    redis_client.set(key,result)

def get_cached_result(key):
    """
    Retrieves the result from the cache using the specified key.

    Args:
        key (str): Cache key used to determine the result to retrieve.

    Returns:
        str: The result data from the cache, decoded using UTF-8 encoding. Returns None if there is no result in the cache.
    """
    cached_result = redis_client.get(key)
    return cached_result.decode("utf-8") if cached_result is not None else None