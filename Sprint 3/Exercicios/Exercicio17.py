def dividirLista(lista):
    tamanho = len(lista)
    parte = tamanho//3
    lista1 = lista[0:parte]
    lista2 = lista[parte:parte * 2]
    lista3 = lista[parte*2:]
    return lista1, lista2, lista3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
l1, l2, l3 = dividirLista(lista)
print(l1, l2, l3)