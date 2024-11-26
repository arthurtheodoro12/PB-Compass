def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    return linhas

def ordenar_atores_por_receita(dados):
    atores_receitas = []

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

        ator = campos[0] 
        receita_total_bruta = float(campos[1]) 

        atores_receitas.append((ator, receita_total_bruta))

    atores_ordenados = sorted(atores_receitas, key=lambda x: -x[1])

    return atores_ordenados

caminho_arquivo = "C:/Users/arthu/OneDrive/Desktop/Programa de Bolsas/PB-Compass/Sprint 3/Exercicios/ETL/actors.csv"

dados = ler_arquivo(caminho_arquivo)

atores_ordenados = ordenar_atores_por_receita(dados)

caminho_saida = "C:/Users/arthu/OneDrive/Desktop/Programa de Bolsas/PB-Compass/Sprint 3/Exercicios/ETL/etapa-5.txt"
with open(caminho_saida, 'w', encoding='utf-8') as arquivo_saida:
    for ator, receita in atores_ordenados:
        arquivo_saida.write(f"{ator} - {receita:.2f}\n")