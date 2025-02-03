import sys
from pyspark.sql import SparkSession
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import current_date, date_format, col, when

# Parâmetros do Job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Inicializando Spark e GlueContext
spark = SparkSession.builder.appName(args['JOB_NAME']).getOrCreate()
glueContext = GlueContext(spark.sparkContext)
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Definindo os caminhos
path_raw = 's3://data-lake-arthur-theodoro/Raw/TMDB/JSON/2025/02/02/'
path_de_base = 's3://data-lake-arthur-theodoro/Trusted/TMDB/JSON/'

#Lendo os arquivos JSON
df = spark.read.option("multiline", "true").json(path_raw)

# Obtendo a data de processamento para subir posteriormente no S3
data_processamento = df.select(date_format(current_date(), "yy/MM/dd")).collect()[0][0]

# Defininido o caminho de saída
path_saida = f"{path_de_base}{data_processamento}/"


# TRATAMENTO DOS DADOS

#Selecionando colunas relevantes
df = df.select("genre_ids", "id", "original_language", "original_title", "overview", "popularity", "release_date", "title", "vote_average", "vote_count")

#Tratamento de valores nulos
df = df.fillna(0)

#TRANSFORMANDO JSON EM PARQUET E SUBINDO PARA O S3

# Convertendo para DynamicFrame
dynamic_frame = DynamicFrame.fromDF(df, glueContext, "dynamic_frame")

# Upando para o S3
glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame,
    connection_type="s3",
    connection_options={"path": path_saida},
    format="parquet"
)

job.commit()