dados = open("C:/Users/arthu/OneDrive/Desktop/Programa de Bolsas/PB-Compass/Sprint 4/Exercicios/arquivos-utilizados/estudantes.csv", 'r', encoding='utf-8')

linhas = dados.readlines()
print(linhas)
linhas = list(map(lambda linha: linha.strip(), linhas))
print(linhas)
lista_aluno_nota= list(map(lambda linha: linha.split(","), linhas))
print(linhas)

nomes_estudantes = list(map(lambda x: x[0], lista_aluno_nota))

lista_notas = list(map(lambda x: x[1:6], lista_aluno_nota))

lista_notas_ordenada = list(map(lambda nota: nota.sort(reverse = True, key = float) or nota, lista_notas))

top_3_notas = list(map(lambda x: [int(x[0]), int(x[1]), int(x[2])], lista_notas_ordenada))

lista_medias = list(map(lambda x: round(sum(x)/3, 2), top_3_notas))

resultado = sorted(zip(nomes_estudantes, top_3_notas, lista_medias), key=lambda x: x[0])

for nome, nota, media in resultado:
    print(f"Nome: {nome} Notas: {nota} Média: {media}")


