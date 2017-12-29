import functools

def singleton(cls):
    instance = None


    @functools.wraps(cls)
    def inner(*args,**kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args,**kwargs)
        return instance
    return inner

@singleton
class Noop:
    pass


a=Noop()
b=Noop()
print(id(a),id(b))