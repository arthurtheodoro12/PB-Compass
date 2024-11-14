numeros = []

for i in range(3):
    numeros.append(i + 2)
    if numeros[i] % 2 == 0:
        print("Par: " + str(numeros[i]))
    else:
        print("Ímpar: " + str(numeros[i]))



