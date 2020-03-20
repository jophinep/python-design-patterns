"""
Flyweight Design Pattern
"""

from functools import wraps

def flyweight(cls):
    """
    flyweight class decorator method
    This is an python implementation of flyweight design pattern
    Ref: https://www.geeksforgeeks.org/flyweight-design-pattern/
    """
    instances = {}
    kwd_mark = object()
    @wraps(cls)
    def getinstance(*args, **kwargs):
        """
        Wapper method
        """
        key = (cls.__name__,) + args + (kwd_mark,) + tuple(sorted(kwargs.items()))
        hash_key = hash(key)
        if hash_key not in instances:
            instances[hash_key] = cls(*args, **kwargs)
        return instances[hash_key]
    return getinstance
