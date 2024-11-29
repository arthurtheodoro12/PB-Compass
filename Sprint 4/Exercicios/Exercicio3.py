from functools import reduce

def calcula_saldo(lancamentos) -> float:
    corrigir_lancamentos = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)

    somar_saldo = reduce(lambda acumulador, x: acumulador + x, corrigir_lancamentos)

    return somar_saldo


lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

somar_saldo = calcula_saldo(lancamentos)

print(somar_saldo)
