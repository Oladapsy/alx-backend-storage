#!/usr/bin/env python3
""" Create a Cache class. In the __init__ method, store an instance of the
    Redis client as a private variable named _redis (using redis.Redis())
    and flush the instance using flushdb.

    Create a store method that takes a data argument and returns a string.
    The method should generate a random key (e.g. using uuid), store the
    input data in Redis using the random key and return the key.

    Type-annotate store correctly. Remember that data can be a str, bytes,
    int or float.
"""
import redis
from typing import Callable, Union, Optional
from uuid import uuid4
import functools

"""
    Above Cache define a count_calls decorator that takes a
    single methodCallable argument and returns a Callable.
"""


def count_calls(method: Callable) -> Callable:
    """count all called method in the Cache class"""

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper method to increment call count anytime the
        methods are called"""
        key = method.__qualname__

        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ decorator for a function in the class"""

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
            wrapper function to store inputs and outputs
            for a particular function in the class cache
        """
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, result)
        return result
    return wrapper


class Cache():
    """ a Cache class"""
    def __init__(self):
        """store redis instance and flush it"""
        self._redis = redis.Redis(host="localhost", port=6379, db=0)
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store method takes data and return string"""
        rkey = str(uuid4())
        self._redis.set(rkey, data)
        return rkey

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:  # noqa: E501
        """ get a record based on key or value based on key"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """ get str from cache"""
        return (self.get(key, lambda d: d.decode("utf-8")))

    def get_int(self, key: int) -> Optional[int]:
        """ get int from cache"""
        return self.get(key, int)
