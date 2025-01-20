import boto3
import datetime as dt

#Credenciais de Acesso
AWS_ACCESS_KEY_ID="Key1"
AWS_SECRET_ACCESS_KEY="Key2"
AWS_SESSION_TOKEN="key3"

#Criando Cliente Boto3
s3 = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    aws_session_token = AWS_SESSION_TOKEN
)


#Função para criar bucket
def create_bucket(bucket_name):
    try:
        s3.create_bucket(Bucket= bucket_name)
    except Exception as error:
        print(f"Não foi possível criar o Bucket: {error}")
    else:
        print(f"Bucket {bucket_name} criado com sucesso!")

#Função de upar para o S3
def upload_to_s3(path, bucket_name, file_name):
    try:
        s3.upload_file(path, bucket_name, file_name)
    except Exception as error:
        print(f"Erro ao upar arquivo: {error}")
    else:
        print(f"Arquivo '{file_name}' upado para o bucket '{bucket_name}' com sucesso!")


#Criando Bucket
bucket_name = "data-lake-arthur-theodoro"
create_bucket(bucket_name)


#Definindo nome das pastas para upar os arquivos
hoje = dt.datetime.now().strftime("%Y/%m/%d")
pastas_movies = f"Raw/Local/CSV/Movies/{hoje}"
pastas_series = f"Raw/Local/CSV/Series/{hoje}"

#Upando arquivo movies.csv
upload_to_s3(r"/app/data/movies.csv", bucket_name, f"{pastas_movies}/movies.csv")

#Upando arquivo series.csv
upload_to_s3(r"/app/data/series.csv", bucket_name, f"{pastas_series}/series.csv")