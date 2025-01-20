import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import upper, col, desc

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Lendo o arquivo 'nomes.csv' do S3
df = spark.read.csv("s3://exercicio-sprint07-glue/lab-glue/input/nomes.csv", header=True, inferSchema=True)

# Imprimindo o schema do dataframe
df.printSchema()

# Tranformando os valores da coluna 'nome' para maiúsculo
df_maiusculo = df.withColumn('nome', upper(col('nome')))

# Contagem de linhas presentes no dataframe
print(f"Total de linhas no dataframe: {df_maiusculo.count()}")

# Contagem de nomes agrupados por ano e sexo
cont_nomes = df_maiusculo.groupBy('ano', 'sexo').count().orderBy(desc('ano'))
cont_nomes.show()

# Nome feminino com mais registros e em que ano ocorreu
feminino_mais_registros = df_maiusculo.filter(col('sexo') == 'F').groupBy('ano', 'nome').count().orderBy(desc('count'))
if feminino_mais_registros.count() > 0:
    foto_feminino_mais_registros = feminino_mais_registros.first()
    print(f"Nome feminino mais registrado: {foto_feminino_mais_registros['nome']} no ano {foto_feminino_mais_registros['ano']}")

# Nome masculino com mais registros e em que ano ocorreu
masculino_mais_comum = df_maiusculo.filter(col('sexo') == 'M').groupBy('ano', 'nome').count().orderBy(desc('count'))
if masculino_mais_comum.count() > 0:
    foto_masculino_mais_comum = masculino_mais_comum.first()
    print(f"Nome masculino mais registrado: {foto_masculino_mais_comum['nome']} no ano {foto_masculino_mais_comum['ano']}")

# Total de registros masculinos e femininos para cada ano com as primeiras 10 linhas ordenadas por ano
total_por_ano = df_maiusculo.groupBy('ano', 'sexo').count().orderBy('ano').limit(10)
total_por_ano.show()

# Escrever o conteúdo do dataframe com nomes em maiúsculo no S3 (frequencia_registro_nomes_eua)
output_path = "s3://exercicio-sprint07-glue/lab-glue/frequencia_registro_nomes_eua"
df_maiusculo.write.mode("overwrite").partitionBy('sexo', 'ano').json(output_path)

job.commit()