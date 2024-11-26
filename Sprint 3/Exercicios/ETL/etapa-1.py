def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    return linhas

def ator_mais_filmes(dados):
    maior_num_filmes = 0
    ator_mais_filmes = ""
    
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
        num_filmes = int(campos[2]) 

        if num_filmes > maior_num_filmes:
            maior_num_filmes = num_filmes
            ator_mais_filmes = ator

    return ator_mais_filmes, maior_num_filmes

caminho_arquivo = "C:/Users/arthu/OneDrive/Desktop/Programa de Bolsas/PB-Compass/Sprint 3/Exercicios/ETL/actors.csv"

dados = ler_arquivo(caminho_arquivo)

ator, num_filmes = ator_mais_filmes(dados)

with open("C:/Users/arthu/OneDrive/Desktop/Programa de Bolsas/PB-Compass/Sprint 3/Exercicios/ETL/etapa-1.txt", 'w', encoding='utf-8') as arquivo_saida:
    arquivo_saida.write(f"O ator/atriz com o maior número de filmes é: {ator}\n")
    arquivo_saida.write(f"O número de filmes desse(a) ator/atriz é: {num_filmes}\n")