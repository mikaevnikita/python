import functools

def memoized(func,cache={}):
    """По возможности кэширует значения"""
    @functools.wraps(func)
    def inner(*args,**kwargs):
        key=tuple(args)+tuple(sorted(kwargs.items()))
        if key not in cache:
            cache[key]=func(*args,**kwargs)
        return cache[key]
    return inner

@memoized
def foo(n):
    if n == 1:
        return 1
    return foo(n-1)*n

print(foo(5))
