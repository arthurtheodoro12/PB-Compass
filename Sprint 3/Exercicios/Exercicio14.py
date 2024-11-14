def funcao(*parametro1, **parametro2):
    for parametro in parametro1:
        print(parametro)
    for chave, parametro in parametro2.items():
        print(parametro)

funcao(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

