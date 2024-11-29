def conta_vogais(texto:str)-> int:
    vogais = ["a", "e", "i", "o", "u"]

    achar_vogais = filter(lambda x: x in vogais, texto.lower())
    return len(list(achar_vogais))

print(conta_vogais("ate logo caique"))