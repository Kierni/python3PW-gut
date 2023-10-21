def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    for d in range(2, x):
        if x % d == 0:
            return False
    return True


def primes(n):
    x = 0
    cnt = 0
    while cnt < n:
        while not is_prime(x):
            x += 1
        yield x
        x += 1
        cnt += 1


for prime in primes(20):
    print(prime)