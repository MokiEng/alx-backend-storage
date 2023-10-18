#!/usr/bin/env python3
"""exercise file"""
import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


def count_calls(method: Callable) -> Callable:
    """
    a system to count how many times methods of the Cache class are called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Get the qualified name of the method."""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """a call_history decorator to store the history of
    inputs and outputs for a particular function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Get the qualified name of the method."""
        in_key = '{}:inputs'.format(method.__qualname__)
        out_key = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)
        return output
    return wrapper

def replay(fn: Callable) -> None:
    '''Displays the call history of a Cache class' method.
    '''
    if fn is None or not hasattr(fn, '__self__'):
        return
    redis_store = getattr(fn.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return
    fxn_name = fn.__qualname__
    in_key = '{}:inputs'.format(fxn_name)
    out_key = '{}:outputs'.format(fxn_name)
    fxn_call_count = 0
    if redis_store.exists(fxn_name) != 0:
        fxn_call_count = int(redis_store.get(fxn_name))
    print('{} was called {} times:'.format(fxn_name, fxn_call_count))
    fxn_inputs = redis_store.lrange(in_key, 0, -1)
    fxn_outputs = redis_store.lrange(out_key, 0, -1)
    for fxn_input, fxn_output in zip(fxn_inputs, fxn_outputs):
        print('{}(*{}) -> {}'.format(
            fxn_name,
            fxn_input.decode("utf-8"),
            fxn_output,
        ))
class Cache:
    """cache class"""
    def __init__(self) -> None:
        """ Create a Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)
    @call_history
    @count_calls
    
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
