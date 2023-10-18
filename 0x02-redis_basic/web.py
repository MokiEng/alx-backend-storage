#!/usr/bin/env python3
"""A  module to obtain the HTML content of a
particular URL and returns it.
"""

import requests
import redis
from functools import wraps


def cache_page(fn):
    """a decorator cache_page"""
    @wraps(fn)
    def decorated(*args, **kwargs):
        url = args[0]
        cache_key = f'count:{url}'
        cached_result = cache.get(cache_key)

        if cached_result:
            cache.incr(cache_key)
            return cached_result

        response = fn(*args, **kwargs)
        cache.setex(cache_key, 10, response)
        return response
    return decorated


cache = redis.Redis(host='localhost', port=6379, db=0)


@cache_page
def get_page(url):
    """automatically cache the result and track the
    number of times the URL was accessed.
    """
    response = requests.get(url)
    return response.text
