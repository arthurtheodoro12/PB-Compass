a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
c = []


for i in a:
    for num in b:
        if i == num:
            c.append(i)

novoConjunto = set(c)
c = list(novoConjunto)
print(c)