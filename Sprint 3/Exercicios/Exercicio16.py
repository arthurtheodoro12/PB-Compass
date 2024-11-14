def somarString(string):
    listaNumeros = string.split(",")
    soma = 0
    for numero in listaNumeros:
        soma += int(numero)
    return soma
  
print(somarString("1,3,4,6,10,76"))