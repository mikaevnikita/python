import functools
import math

def post(cond,message):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args,**kwargs):
            result=func(*args,**kwargs)
            assert cond(result),message
            return result
        return inner
    return wrapper


@post(lambda x:x>=0,"x should be >=0")
def some_function(x):
    "Very hard logic"
    return x

some_function(-1)