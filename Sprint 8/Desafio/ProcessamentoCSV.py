import sys
from pyspark.sql import SparkSession
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, current_date

#Definindo parâmetros do Job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

#Inicializando Spark e GlueContext
spark = SparkSession.builder.appName(args['JOB_NAME']).getOrCreate()
glueContext = GlueContext(spark.sparkContext)
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#Definindo caminhos
raw_path = 's3://data-lake-arthur-theodoro/Raw/Local/CSV/Movies/2025/01/06/movies.csv'
trusted_path = 's3://data-lake-arthur-theodoro/Trusted/Local/CSV/movie.parquet'
    
#Lendo o arquivo CSV
df = spark.read.option("header", "true").csv(raw_path)

# TRATAMENTO DOS DADOS

#Tratamento de valores nulos
df = df.fillna(0)

#TRANSFORMANDO CSV EM PARQUET E SUBINDO PARA O S3

# Convertendo para DynamicFrame
dynamic_frame = DynamicFrame.fromDF(df, glueContext, "dynamic_frame")
    
#Mudando para Parquet e upando para o S3
glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame,
    connection_type="s3",
    connection_options={"path": trusted_path},
    format="parquet"
)
    
job.commit()