import functools

def once(func):
    """Выполняет код только один раз, удобен для инициализации настроек и тд"""
    @functools.wraps(func)
    def inner(*args,**kwargs):
        if not inner.called:
            func(*args,**kwargs)
            inner.called=True
    inner.called=False
    return inner

@once
def some_function(x):
    print(x)

some_function(42)
some_function(3)
