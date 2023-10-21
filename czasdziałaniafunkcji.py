import time
from time import sleep


#dekorator
def timeit(fn):
    def wrapper(*args,**kwargs):  # args daje ddowloną możliwość arguemntów,(argument pozycyjyn) to krotka, kwargs z dwiema gwiazdkami pozwala przekazywać dowloną ilość nazwanych argumentów to słownik, argument nazwany

        start = time.time()
        result = fn(*args,**kwargs) # teraz możęmy udekorowac dowoloną funckję a nie jak wcześniej tylko z orrkeślnoną iloscia arguemntó
        end = time.time()
        print(f"Duration {end - start}")
        return result
    return wrapper

@timeit
def greeting():
    print("Hellow rold")
    sleep(3)




greeting()

@timeit
def div(a ,b):
    sleep(3)
    return a/b

div(2 ,4)