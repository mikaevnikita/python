import functools
def profiled(func):
    """Декоратор работающий как счетчик вызовов"""
    @functools.wraps(func)
    def inner(*args,**kwargs):
        inner.ncalls+=1
        return func(*args,**kwargs)
    inner.ncalls=0
    return inner

@profiled
def some_function(x):
    print(x)

some_function(42)
some_function(3)
print(some_function.ncalls)
