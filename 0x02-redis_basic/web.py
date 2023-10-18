#!/usr/bin/env python3
"""A  module to obtain the HTML content of a
particular URL and returns it.
"""

import requests
import redis
from functools import wraps
from typing import Callable
from datetime import datetime, timedelta

redis_client = redis.Redis()


def get_page(url: str) -> str:
    """ Check if the URL is cached."""
    cached_result = redis_client.get(url)
    if cached_result:
        return cached_result.decode('utf-8')
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
    else:
        content = f"Failed to retrieve the content from {url}"
    redis_client.setex(url, timedelta(seconds=10), content)
    increment_url_count(url)
    return content

def increment_url_count(url: str):
    """Track the number of times the URL is accessed"""
    count_key = f'count:{url}'
    current_count = redis_client.get(count_key)
    if current_count:
        new_count = int(current_count) + 1
    else:
        new_count = 1
    redis_client.set(count_key, new_count)

def cache_result(fn):
    @wraps(fn)
    def wrapper(url):
        cached_result = redis_client.get(url)
        if cached_result:
            return cached_result.decode('utf-8')
        result = fn(url)
        redis_client.setex(url, timedelta(seconds=10), result)
        return result
    return wrapper
get_page = cache_result(get_page)
