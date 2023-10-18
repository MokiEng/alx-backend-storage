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

    def get(self, key: str, fn: Callable = None,
           ) -> Union[str, bytes, int, float]:
        """ Retrieve data from Redis."""
        data = self._redis.get(key)

        return fn(data) if fn is not None else data
    def get_str(self, key: str) -> str:
        """Retrieves a string value from a Redis."""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Retrieves an integer value from a Redis."""
        return self.get(key, lambda x: int(x))


if __name__ == "__main__":
    cache = Cache()
