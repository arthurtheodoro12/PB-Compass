numeros = open("C:/Users/arthu/OneDrive/Desktop/Programa de Bolsas/PB-Compass/Sprint 4/Exercicios/arquivos-utilizados/number.txt", 'r', encoding='utf-8')

numeros_ordenados = list(sorted((line.strip() for line in numeros), key=int, reverse=True))

maiores_pares = list(filter(lambda num: int(num) % 2 == 0, numeros_ordenados))

maiores_pares_int = list(map(int, maiores_pares))

somar_maiores_pares = sum(map(lambda x: x, maiores_pares_int[:5]))

print(maiores_pares_int[:5])
print(somar_maiores_pares)

