import functools

def pre(cond,message):
    """Пред условие для функции"""
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args,**kwargs):
            assert cond(*args,**kwargs),message
            return func(*args,**kwargs)
        return inner
    return wrapper


@pre(lambda x:x>=0,"x should be >=0")
def log(x):
    """Вычисляем логарифм"""

log(1)
log(-1)
