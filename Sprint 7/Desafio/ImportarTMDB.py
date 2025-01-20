import requests 
import boto3    
import json     
import datetime as dt 

# Configuracoes iniciais API
api_key = 'api-key'
base_url = 'https://api.themoviedb.org/3/discover/movie'

filtros = {
    'api_key': api_key,
    'language': 'pt-BR',
    'with_genres': '10752', 
    'primary_release_date.gte': '1947-01-01',
    'primary_release_date.lte': '2000-12-31',
    'sort_by': 'vote_count.desc'
}

# Configurações de Acesso AWS
AWS_ACCESS_KEY_ID="Key1"
AWS_SECRET_ACCESS_KEY="Key2"
AWS_SESSION_TOKEN="key3"
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN
)

#Definindo nome das pastas para upar os arquivos e nome do bucket
hoje = dt.datetime.now().strftime("%Y/%m/%d")
estrutura_RAW = f"Raw/TMDB/JSON/{hoje}"
bucket_name = "data-lake-arthur-theodoro"

# Função para enviar dados ao S3
def upload_to_s3(dados, nome_do_bucket, nome_arquivo):
    try:
        dados_json = json.dumps(dados, ensure_ascii=False, indent=4)
        s3_client.put_object(
            Bucket=nome_do_bucket,
            Key=f"{estrutura_RAW}/{nome_arquivo}.json",
            Body=dados_json 
        )
    except Exception as error:
        print(f"Erro ao enviar: {error}")
    else:
        print(f"Arquivo '{nome_arquivo}.json' enviado com sucesso!")


# Função para buscar os filmes da API
def buscar_filmes(limit=300):
    filmes = []
    num_pagina = 1
    while len(filmes) < limit:
        filtros['page'] = num_pagina
        query = requests.get(base_url, params=filtros)
        data = query.json()
        pagina_atual_filmes = data.get('results', [])
        
        # Adicione apenas os filmes necessários para atingir o limite
        filmes.extend(pagina_atual_filmes[:limit - len(filmes)])
        
        # Verifique se atingiu o fim ou atingiu o limite
        if len(pagina_atual_filmes) < 20:
            break  # Less than the max per page indicates end of data

        num_pagina += 1

    return filmes

# Função que separa todos os filmes encontrados em arquivos de no máximo 100 filmes e faz o upload para o S3
def processar_filmes():
    filmes = buscar_filmes()
    if filmes:
        total_filmes_JSON = 100  # Tamanho de cada arquivo JSON
        quantidade_arquivos = (len(filmes) + total_filmes_JSON - 1) // total_filmes_JSON  # Quantidade de arquivos a serem gerados

        for i in range(quantidade_arquivos):
            filmes_do_arquivo = filmes[i * total_filmes_JSON : (i + 1) * total_filmes_JSON]
            nome_arquivo = f"filmes_guerra_{i + 1}"  # Nome único para cada arquivo
            upload_to_s3(filmes_do_arquivo, bucket_name, nome_arquivo)
    else:
        print("Nenhum filme encontrado ou houve um problema com a API.")

# Invocando a função
processar_filmes()

