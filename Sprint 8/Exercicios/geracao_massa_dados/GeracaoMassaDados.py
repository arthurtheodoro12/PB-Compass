import random
import time
import os
import names

#Etapa 1

numeros = []

for i in range(0, 250):
    numeros.append(random.randint(0, 250))

numeros.reverse()
#print(numeros)

#Etapa 2
animais = [
    "gato", "cachorro", "elefante", "tigre", "leão", "girafa", "rinoceronte", 
    "urso", "panda", "cavalo", "lobo", "zebra", "camelo", "porco", "canguru", 
    "jacaré", "coelho", "raposa", "arara", "tartaruga"]

animais.sort()

#[print(animal) for animal in animais]

#with open(r"C:\Users\arthu\OneDrive\Desktop\Programa de Bolsas\PB-Compass\Sprint 8\Exercicios\animais.csv", "w") as arquivo:
    #arquivo.writelines([f"{animal}\n" for animal in animais])

#Etapa 3
random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = []

for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios.")

dados = []
for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

with open(r'C:\Users\arthu\OneDrive\Desktop\Programa de Bolsas\PB-Compass\Sprint 8\Exercicios\nomes_aleatorios.txt', 'w') as arquivo_nomes:
    for nome in dados:
        arquivo_nomes.write(nome + '\n')