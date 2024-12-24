import pandas as pd
import S3 

#Criando bucket
S3.create_bucket("operacoes-policia-federal-julho-2023")

#Subindo para o S3 o arquivo CSV original
S3.upload_to_s3(r"C:\Users\arthu\OneDrive\Desktop\Programa de Bolsas\PB-Compass\Sprint 5\Desafio\PALAS_OPERACOES_2023_07.csv",  "operacoes-policia-federal-julho-2023", "dataBase")


#Tratamento

#Criando o DataFrame
dados = pd.read_csv(r"C:\Users\arthu\OneDrive\Desktop\Programa de Bolsas\PB-Compass\Sprint 5\Desafio\PALAS_OPERACOES_2023_07.csv", delimiter=";")

#Percebi que algumas colunas do DataFrame possuem alguns espaços desnecessários, então decidi usar o str.strip() para tira-los e além disso, substitui todos os vazios e nulos por 0
dados["Area"] = dados["Area"].str.strip()
dados["Sigla Unidade Institucional"] = dados["Sigla Unidade Institucional"].str.strip()
dados["Atuacao em Territorio de Fronteira"] = dados["Atuacao em Territorio de Fronteira"].str.strip()

dados.replace("", "0", inplace=True)
dados.fillna(0, inplace=True)

# Substituição de "0" por "Nao" na coluna "Atuacao em Territorio de Fronteira"
dados["Atuacao em Territorio de Fronteira"] = dados["Atuacao em Territorio de Fronteira"].astype(str)
dados["Atuacao em Territorio de Fronteira"] = dados["Atuacao em Territorio de Fronteira"].replace("0", "Nao")

#Exportando DataFrame tratado
dados.to_csv(r"C:\Users\arthu\OneDrive\Desktop\Programa de Bolsas\PB-Compass\Sprint 5\Desafio\PALAS_OPERACOES_2023_07-TRATADO.csv", index=False, encoding='utf-8')

#Subindo para o S3 o arquivo CSV tratado
S3.upload_to_s3(r"C:\Users\arthu\OneDrive\Desktop\Programa de Bolsas\PB-Compass\Sprint 5\Desafio\PALAS_OPERACOES_2023_07-TRATADO.csv", "operacoes-policia-federal-julho-2023", "dataBase-tratada")


#Manipuação

#Clausula que filtra dados usando ao menos dois operadores lógicos
resultado = dados[(dados["Qtd Prisao em Flagrante"] != 0) & (dados["Qtd Mandado de Busca e Apreesao"] != 0)]

#Função de String + Função de Conversão 
resultado.loc[:, "Qtd Valores Apreendidos"] = resultado["Qtd Valores Apreendidos"].astype(str).str.replace("R$", "").str.replace(".", "").str.replace(",", ".").str.strip()
resultado.loc[:,"Qtd Valores Apreendidos"] = pd.to_numeric(resultado["Qtd Valores Apreendidos"], errors='coerce', downcast='float')

#Uma função condicional
resultado = resultado.query('`Qtd Valores Apreendidos` > 0')

#Função de Data
resultado["Data da Deflagracao"] = pd.to_datetime(resultado["Data da Deflagracao"], dayfirst=True)
data_limite = pd.to_datetime('2023-07-16')
resultado = resultado[resultado["Data da Deflagracao"] < data_limite]

#Duas Funções de Agregação
total_operacoes = resultado["Id Operacao"].count()
total_valores_apreendidos = resultado["Qtd Valores Apreendidos"].sum()
total_valores_apreendidos_formatado = f"{total_valores_apreendidos:,.1f}"

#Saída final
totais = [[total_operacoes, f"R${total_valores_apreendidos_formatado}"]]

#Exportando saída final para um CSV
dados_final = pd.DataFrame(totais, columns=["Quantidade Total de Operações", "Valor Total Apreendido"])
dados_final.to_csv(r"C:\Users\arthu\OneDrive\Desktop\Programa de Bolsas\PB-Compass\Sprint 5\Desafio\PALAS_OPERACOES_2023_07-Final.csv", index=False, encoding='utf-8')

#Subindo para o S3 o CSV final
S3.upload_to_s3(r"C:\Users\arthu\OneDrive\Desktop\Programa de Bolsas\PB-Compass\Sprint 5\Desafio\PALAS_OPERACOES_2023_07-Final.csv", "operacoes-policia-federal-julho-2023", "dataBase-final")
