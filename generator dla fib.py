def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        yield a#to słowo kluczowe ma cechę charakteesyzną returna, też zwraca, jak spotka yield to wyrzuci coś z funkcji ale bedzie kontynuował działanie i nie musi być na końców
        a, b = b, a + b # jeśli występuje vield to mamy generator
    return a


def fib_items(n):
    return (
        fib(x) for x in range(n)
    )

i =0
for n in fib(10):
    print(i, n)
    i+=1

print(list(fib(10)))