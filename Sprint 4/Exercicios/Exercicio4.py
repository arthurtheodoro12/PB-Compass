def calcular_valor_maximo(operadores,operandos) -> float:
    lista_completa = list(zip(operadores, operandos))

    def aplicar_operacao(operador, operando):
        if operador == "+":
            return operando[0] + operando[1]
        elif operador == "-":
            return operando[0] - operando[1]
        elif operador == "/":
            if operando[1] != 0:
                return operando[0] / operando[1]
            else:
                return 0
        elif operador == "*":
            return operando[0] * operando[1]
        elif operador == "%":
            return operando[0] % operando[1]
        else:
            return 0

    
    resultados = map(lambda x: aplicar_operacao(x[0], x[1]), lista_completa)
    
    maior_resultado = max(resultados)

    return maior_resultado

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

maior_valor = calcular_valor_maximo(operadores, operandos)

print(maior_valor)