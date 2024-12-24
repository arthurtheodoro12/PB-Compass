import boto3

AWS_ACCESS_KEY_ID="key1"
AWS_SECRET_ACCESS_KEY="key2"
AWS_SESSION_TOKEN= "key3"

s3 = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    aws_session_token = AWS_SESSION_TOKEN
)

#Criando Bucket

def create_bucket(bucket_name):
    s3.create_bucket(
        Bucket= bucket_name,
    )

def upload_to_s3(path, bucket_name, file_name):
    s3.upload_file(path, bucket_name, file_name)
