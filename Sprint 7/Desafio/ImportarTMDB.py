import requests
import boto3
import json
import datetime as dt

# Configuração inicial da API TMDB
api_key = 'acd287c57f9896a6712fbd67c4a1b06e'
base_url_movies = 'https://api.themoviedb.org/3/discover/movie'
base_url_credits = 'https://api.themoviedb.org/3/movie/{movie_id}/credits'

filtros = {
    'api_key': api_key,
    'language': 'pt-BR',
    'with_genres': '10752',
    'primary_release_date.gte': '1947-01-01',
    'primary_release_date.lte': '2000-12-31',
    'sort_by': 'vote_count.desc'
}

# Configurações AWS
AWS_ACCESS_KEY_ID = "ASIAZDZTCAPMEFDJ6QKB"
AWS_SECRET_ACCESS_KEY = "rJeuAJDb5p2RxH6VQeeb49DoqCYKzXBOQiJke0uf"
AWS_SESSION_TOKEN = "IQoJb3JpZ2luX2VjEOz//////////wEaCXVzLWVhc3QtMS..."

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN
)

# Definição do nome das pastas no S3
hoje = dt.datetime.now().strftime("%Y/%m/%d")
estrutura_RAW = f"Raw/TMDB/JSON/{hoje}"
bucket_name = "data-lake-arthur-theodoro"

# Função para upload no S3
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

# Função para buscar filmes
def buscar_filmes(limit=5000):
    filmes = []
    num_pagina = 1
    while len(filmes) < limit:
        filtros['page'] = num_pagina
        query = requests.get(base_url_movies, params=filtros)
        data = query.json()
        pagina_atual_filmes = data.get('results', [])
        filmes.extend(pagina_atual_filmes[:limit - len(filmes)])
        if len(pagina_atual_filmes) < 20:
            break
        num_pagina += 1
    return filmes

# Função para buscar atores e diretores de um filme
def buscar_atores_diretores(movie_id):
    url = base_url_credits.format(movie_id=movie_id)
    response = requests.get(url, params={'api_key': api_key})
    data = response.json()
    
    atores = [
        {'id': ator['id'], 'nome': ator['name'], 'personagem': ator.get('character', '')}
        for ator in data.get('cast', [])
    ]
    
    diretores = [
        {'id': crew['id'], 'nome': crew['name'], 'departamento': crew['department']}
        for crew in data.get('crew', []) if crew.get('job') == 'Director'
    ]
    
    return {'atores': atores, 'diretores': diretores}

# Função para processar todos os filmes e coletar dados de atores e diretores
def processar_atores_diretores():
    filmes = buscar_filmes()
    dados_atores_diretores = []
    
    for filme in filmes:
        movie_id = filme['id']
        creditos = buscar_atores_diretores(movie_id)
        dados_atores_diretores.append({
            'filme_id': movie_id,
            'titulo': filme['title'],
            'atores': creditos['atores'],
            'diretores': creditos['diretores']
        })
    
    if dados_atores_diretores:
        upload_to_s3(dados_atores_diretores, bucket_name, "atores_diretores")
    else:
        print("Nenhum dado de atores/diretores encontrado.")

# Invocar a função
processar_atores_diretores()
