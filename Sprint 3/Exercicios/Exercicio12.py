def my_map(list, f):
    novaLista = []
    for elemento in list:
        aplicacarFunc = f(elemento)
        novaLista.append(aplicacarFunc)
    return novaLista

def quadrado(num):
    return num ** 2

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_map(lista, quadrado))