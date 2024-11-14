lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def eliminarDuplicados(lista):
    eliminandoDuplicados = set(lista)
    novaLista = list(eliminandoDuplicados)
    return novaLista

print(eliminarDuplicados(lista))

