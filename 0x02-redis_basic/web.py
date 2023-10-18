#!/usr/bin/env python3
"""A  module to obtain the HTML content of a
particular URL and returns it.
"""

import requests
import redis
from functools import wraps
from typing import Callable

redis_client = redis.Redis()
"""The module-level Redis instance."""


def data_cacher(method: Callable) -> Callable:
    """Caches the output of fetched data."""
    @wraps(method)
    def wrapper(url) -> str:
        cached_result = redis_client.get(url)
        if cached_result:
            return cached_result.decode('utf-8')
        result = fn(url)
        redis_client.setex(url, timedelta(seconds=10), result)
        return result
    return wrapper


@data_cacher
def get_page(url: str) -> str:
    """ Check if the URL is cached."""
    return requests.get(url).text
