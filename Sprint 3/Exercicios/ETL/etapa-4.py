def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    return linhas

def contar_aparicoes_filmes(dados):
    contagem_filmes = {}

    for linha in dados[1:]:
        campos = []
        campo_atual = []
        dentro_aspas = False

        for char in linha:
            if char == '"':
                dentro_aspas = not dentro_aspas
            elif char == ',' and not dentro_aspas:
                campos.append(''.join(campo_atual).strip())
                campo_atual = []
            else:
                campo_atual.append(char)
        
        if campo_atual:
            campos.append(''.join(campo_atual).strip())

        filme = campos[4]  

        if filme in contagem_filmes:
            contagem_filmes[filme] += 1
        else:
            contagem_filmes[filme] = 1

    filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: (-x[1], x[0]))

    return filmes_ordenados

caminho_arquivo = "C:/Users/arthu/OneDrive/Desktop/Programa de Bolsas/PB-Compass/Sprint 3/Exercicios/ETL/actors.csv"

dados = ler_arquivo(caminho_arquivo)

filmes_ordenados = contar_aparicoes_filmes(dados)

caminho_saida = "C:/Users/arthu/OneDrive/Desktop/Programa de Bolsas/PB-Compass/Sprint 3/Exercicios/ETL/etapa-4.txt"
with open(caminho_saida, 'w', encoding='utf-8') as arquivo_saida:
    for filme, quantidade in filmes_ordenados:
        arquivo_saida.write(f"O filme {filme} aparece {quantidade} vez(es) no dataset.\n")