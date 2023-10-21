#KOMPLETNY DEKORATOR


from functools import wraps
def cached(fn):
    cache = {}
    @wraps(fn)
    def wrapper(*args,**kwargs):
        params = (args,tuple(kwargs.items())) #bo kwargs to słowniki i nie można tego słowniki nie możemy ich schaszować i musimy zrobić tupla tupli żebu mieć krokti
        if params not in cache:
            cache[params] = fn(*args,**kwargs)
        return cache[params]

    return wrapper

@cached
def fib(n):
    if n in [0,1]:
        return n
    return fib(n-1) + fib(n-2)

print(fib(60))