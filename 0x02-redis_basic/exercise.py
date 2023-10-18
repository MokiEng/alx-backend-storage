#!/usr/bin/env python3
"""exercise file"""
import redis
import uuid
from typing import Union


class Cache:
    """cache class"""
    def __init__(self):
        """ Create a Redis client"""
        self._redis = redis.Redis()

        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generate a random key using UUID"""
        key = str(uuid.uuid4())

        self._redis.set(key, data)

        return key


if __name__ == "__main__":
    cache = Cache()
