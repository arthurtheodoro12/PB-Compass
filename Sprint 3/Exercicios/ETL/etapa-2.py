def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    return linhas

def calcular_media_receita(dados):
    soma_gross = 0
    contador_filmes = 0

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

        gross = float(campos[5]) 
        soma_gross += gross
        contador_filmes += 1

    media_gross = soma_gross / contador_filmes if contador_filmes > 0 else 0
    return media_gross

caminho_arquivo = "C:/Users/arthu/OneDrive/Desktop/Programa de Bolsas/PB-Compass/Sprint 3/Exercicios/ETL/actors.csv"

dados = ler_arquivo(caminho_arquivo)

media_receita = calcular_media_receita(dados)

caminho_saida = "C:/Users/arthu/OneDrive/Desktop/Programa de Bolsas/PB-Compass/Sprint 3/Exercicios/ETL/etapa-2.txt"
with open(caminho_saida, 'w', encoding='utf-8') as arquivo_saida:
    arquivo_saida.write(f"A média da receita de bilheteria é: {media_receita:.2f}\n")