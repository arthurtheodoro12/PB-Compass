import boto3

AWS_ACCESS_KEY_ID="key1"
AWS_SECRET_ACCESS_KEY="key2"
AWS_SESSION_TOKEN = "key3"

s3 = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    aws_session_token = AWS_SESSION_TOKEN
)

#s3.upload_file(r"C:\Users\arthu\OneDrive\Desktop\Programa de Bolsas\PB-Compass\Sprint 5\Desafio\PALAS_OPERACOES_2023_07.csv", "operacoes-policia-federal-julho-2023", "dataBase")
s3.upload_file(r"C:\Users\arthu\OneDrive\Desktop\Programa de Bolsas\PB-Compass\Sprint 5\Desafio\PALAS_OPERACOES_2023_07-TRATADO.csv", "operacoes-policia-federal-julho-2023", "dataBase-tratada")