def pares_ate(n:int):
    for numero in range(2, n+1):
        if numero % 2 == 0:
            yield numero

resultados = pares_ate(12)

for resultado in resultados:
    print(resultado)