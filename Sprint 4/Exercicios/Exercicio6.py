def maiores_que_media(conteudo:dict)->list:
    precos = list(conteudo.values())
    media = sum(precos) / len(precos)
    maior_que_media = filter(lambda x: x[1] > media, conteudo.items())
    return sorted(list(maior_que_media), key=lambda x: x[1])



conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

print(maiores_que_media(conteudo))