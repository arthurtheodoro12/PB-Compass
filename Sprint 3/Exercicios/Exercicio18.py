def pegarValores(dicionario):
    lista = []
    for chave, valor in dicionario.items():
        lista.append(valor)
    excluirDuplicados = set(lista)
    novaLista = list(excluirDuplicados)
    return novaLista

speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 
         'June':53, 'july':54, 'Aug':44, 'Sept':54}   

print(pegarValores(speed))
