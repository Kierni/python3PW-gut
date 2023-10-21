items = [1,2,3,4,5]

pairs = [
         (a, b)
         for a in items
         for b in items
         if a < b
]
print(pairs);