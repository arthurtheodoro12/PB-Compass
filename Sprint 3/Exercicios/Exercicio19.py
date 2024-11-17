import random

random_list = random.sample(range(500), 50)
lista_ordenada = sorted(random_list)
meio_da_lista = len(lista_ordenada)//2

#Calculo Mediana
mediana = 0
if len(lista_ordenada) % 2 == 0:
    mediana = (lista_ordenada[meio_da_lista] + lista_ordenada[meio_da_lista - 1]) / 2 
else:
     mediana = lista_ordenada[meio_da_lista]

media = sum(random_list)/len(random_list)

valor_maximo = max(random_list)

valor_minimo = min(random_list)

print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")