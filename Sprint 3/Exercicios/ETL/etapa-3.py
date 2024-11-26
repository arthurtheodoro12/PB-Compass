def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    return linhas

def ator_maior_media_receita(dados):
    maior_media = 0
    ator_maior_media = ""

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
        gross_media = float(campos[3]) 

        if gross_media > maior_media:
            maior_media = gross_media
            ator_maior_media = ator

    return ator_maior_media, maior_media

caminho_arquivo = "C:/Users/arthu/OneDrive/Desktop/Programa de Bolsas/PB-Compass/Sprint 3/Exercicios/ETL/actors.csv"

dados = ler_arquivo(caminho_arquivo)

ator, maior_media = ator_maior_media_receita(dados)

caminho_saida = "C:/Users/arthu/OneDrive/Desktop/Programa de Bolsas/PB-Compass/Sprint 3/Exercicios/ETL/etapa-3.txt"
with open(caminho_saida, 'w', encoding='utf-8') as arquivo_saida:
    arquivo_saida.write(f"O ator/atriz com a maior média de receita de bilheteria bruta por filme é: {ator}\n")
    arquivo_saida.write(f"A média de receita de bilheteria bruta por filme desse ator/atriz é: {maior_media:.2f}\n")