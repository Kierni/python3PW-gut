items = [1,2,3,4,5]

pairs = (
         x ** 2  # wystarczyło zmienic nawiasy kwadratowe en aokrągłe
         for x in items
)



 # "leniwa lista" , tworzy się obiekt w tym obieckie jest napisane w jaki sposób generować listy, ale w pamięci nie wgrwywamt na raz wszystkich lelemtnów
for pair in pairs:
    print(pair)
for pair in pairs:
    print(pair)   # zadziała tylko pierwsza pętla, jest jakby jednorazowy

print(next(pairs))