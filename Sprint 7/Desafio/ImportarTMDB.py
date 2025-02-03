import requests 
import boto3    
import json     
import datetime as dt 

# Configuracão inicial da API
api_key = 'acd287c57f9896a6712fbd67c4a1b06e'
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
AWS_ACCESS_KEY_ID="ASIAZDZTCAPMEFDJ6QKB"
AWS_SECRET_ACCESS_KEY="rJeuAJDb5p2RxH6VQeeb49DoqCYKzXBOQiJke0uf"
AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjEOz//////////wEaCXVzLWVhc3QtMSJHMEUCIQCkofdzS4dwK2JO3qq3OOmpCKAFUmW0jF5QvvC3c2otFgIgL0xgDjzT1UEHEjm0j9id1g+R786yrY+Qyemg5Y2JisYqrAMI9f//////////ARAAGgw2MjY2MzU0NDExMTIiDM90DvyIsRLV6Wo0xyqAA5IMJQA6FsohfDjwVeQq5YBx/ZTsoU9mb+TEiSLBi4wQtvGyczDH8nPTj6SLxemQUpOMY76i//LfFAY7la+XW4gFBqKsh0qh+hqj6zNAOffaSjPDi0ZESyAU8Ni5xJ0hWiTPWMr6Qs7Rf9/MxfXYm7xVU6Ctqu5ZcF5HK33r3XDtUoWQ8ScUlI/oqfHXupno/ybQJjOxBDTFomAU2woIBD1Iix1BSivWZ/YWII2NNna6JaCTiLsG9mLKrOtbR+tFwp2yrbM167CInVdyf3NuExckg+9S+wKyRqWxnwF6FyMhYNHsgzp8SAnF9OW+L1Zqu91sd5NZereB7p0oZT3jL90QUoo8DlFKUehjaB2X6w+h+l1mUef7BDc7U/gJBcYuRjm/BMhZ0K8Ri3eS2Vvqnr0bgYLLK9C22XXYVeFKXnpiIOeMFQz1hxGCLy3R1DJsC2udX86ERL0PLx4YCdComwUgW0TjmPoiW0nZHS+80+I4O+Eus5D3nZet2wMP9h0l7DD1kv+8BjqmAZOMWH8HN+a9Av8dKzII3OWzEC1A9ps058w2dD7n1Y7Eag3laFJg5wqbeNMJ63NywhJ4XJnLklanSu/WBl/I8/76kg5TNf+GmbDqnu5UeHtWBvCupG4ZEqajWtntSpWRRu0fcOBas9DOy6sEcVxzoi2JsCKdSqiwKX9yC/17Cnl/HZGhibVB2lATw/S09o2oFuVUm3PMXZxxmuJnYIIxaoy9/cpPRRE="
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
def buscar_filmes(limit=5000):
    filmes = []
    num_pagina = 1
    while len(filmes) < limit:
        filtros['page'] = num_pagina
        query = requests.get(base_url, params=filtros)
        data = query.json()
        pagina_atual_filmes = data.get('results', [])
        
        filmes.extend(pagina_atual_filmes[:limit - len(filmes)])
        
        if len(pagina_atual_filmes) < 20:
            break 

        num_pagina += 1

    return filmes

# Função que separa todos os filmes encontrados em arquivos de no máximo 100 filmes e faz o upload para o S3
def processar_filmes():
    filmes = buscar_filmes()
    if filmes:
        total_filmes_JSON = 100  # Tamanho de cada arquivo JSON
        quantidade_arquivos = (len(filmes) + total_filmes_JSON - 1) // total_filmes_JSON 

        for i in range(quantidade_arquivos):
            filmes_do_arquivo = filmes[i * total_filmes_JSON : (i + 1) * total_filmes_JSON]
            nome_arquivo = f"filmes_guerra_{i + 1}" 
            upload_to_s3(filmes_do_arquivo, bucket_name, nome_arquivo)
    else:
        print("Nenhum filme encontrado ou houve um problema com a API.")

# Invocando a função
processar_filmes()

