import boto3
import datetime as dt

#Credenciais de Acesso
AWS_ACCESS_KEY_ID="ASIAZDZTCAPMMAAMA5F2"
AWS_SECRET_ACCESS_KEY="6uF+E/Dz231tzwWd5aIzfLvVCsGXCr86cGmC2ERn"
AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjEGEaCXVzLWVhc3QtMSJIMEYCIQDS5uvHDfvRSzN5TREhLyGjsybV9pFMAMpa6hn8g1habQIhAN0R36VgQBuHQ7fjXSw9lS4TBKGENsq9va5vWodv3bbqKqMDCEkQABoMNjI2NjM1NDQxMTEyIgz1k35tON6dtdPZmuYqgAOKZ/DL6bmd9/eucvr1kxTsaNPP+126B988tAtFo+0alThMgMQzE/HFStU7Ujw+V9W7WvvqI9glooPLv+udyhog2p/e3rbwfYmAUmYjYH7GIpX6V5yJPhA8lDfpQ6AEEa8cmnGx1zScKWP8aEBXrkM3cuITsw0eowMSHEigF6YrUu9FUYIy2amIEsa7z/l/hm6mWfLn8xfdbwAKWi6Z7yzCpc9VqjrhNHXMwIoBhpT+X9R1vFy7uvlvyy8zvtvhl7/dP5mBq7YaeNrG9kAeA2G/uPXSems87t/01qVpe9fEG7+cNsn+a9993dpfpKboJjR7hLl6DtdUSA8eidrWVNxtjwZRwiIoThCQRCOSAKoVeW0bnI03hfRiguq5EflNuMd246WQ0UBvkpg3/iUArwyr/4Je0xhIYZhTSs6ml051x9OwOEwbsz5AxJT729DqJw9zYAZ0wr9dnC9vbBqytqsQCM24VITlEHyqJBTEcFE5T0+efmAEl24lI9EVNHHNAbkwuoHwuwY6pQHKVZID4wtzJO0nstfa3I+zJbLFlAk0Ru2VQ6EfmmVY0wpiJN8OyEu534u9zOed5woNQCr5TUW0pnVBPjKtDir7qyGmmLB7KH7WKqhCTWB9afghq1rjzAIgIlqpugo0tkvla+Ftd5+Fbe/emWpzDUBLx/K8ZUfSPMX+yy5i/j9BY3za5N/pF53SHFF55k03XDc31quA4Epzmvsb1INi78NritSsCws="


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