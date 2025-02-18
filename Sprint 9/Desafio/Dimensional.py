import sys
from pyspark.context import SparkContext
from pyspark.sql.functions import col, explode, monotonically_increasing_id, when
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext


#Inicializando o GlueContex e o Spark
args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sparkContext = SparkContext()
glueContext = GlueContext(sparkContext)
spark = glueContext.spark_session


#Lendo os dados da camada Trusted e criando dataframe
caminho_trusted = "s3://data-lake-arthur-theodoro/Trusted/TMDB/JSON/25/02/03/"
df_trusted = glueContext.create_dynamic_frame.from_options(
    format="parquet",
    connection_type="s3",
    connection_options={"paths": [caminho_trusted]},
    transformation_ctx="df_trusted"
).toDF()


#Criando as tabelas dimensionais, a tabela fato e a tabela de ligação


#dim_filme
dim_filme = df_trusted.select(
    col("id").alias("id_filme"),
    col("title").alias("titulo"),
    col("original_title").alias("titulo_original"),
    col("overview").alias("sinopse")
).distinct()

dim_filme.write.mode("overwrite").parquet("s3://data-lake-arthur-theodoro/Refined/dim_filme/")


#dim_genero
dim_genero = df_trusted.select(explode(col("genre_ids")).alias("id_genero")).distinct()

dim_genero = dim_genero.withColumn(
    "nome_genero",
    when(col("id_genero") == 10752, "Guerra")
    .when(col("id_genero") == 28, "Ação")
    .when(col("id_genero") == 12, "Aventura")
    .when(col("id_genero") == 878, "Ficção Científica")
    .when(col("id_genero") == 10749, "Romance")
    .when(col("id_genero") == 36, "História")
    .when(col("id_genero") == 99, "Documentário")
    .when(col("id_genero") == 10402, "Musical")
    .when(col("id_genero") == 80, "Crime")
    .when(col("id_genero") == 18, "Drama")
    .when(col("id_genero") == 10770, "Filme de TV")
    .when(col("id_genero") == 27, "Terror")
    .when(col("id_genero") == 35, "Comédia")
    .when(col("id_genero") == 16, "Animação")
    .when(col("id_genero") == 10751, "Familia")
    .when(col("id_genero") == 14, "Fantasia")
    .when(col("id_genero") == 53, "Suspense")
    .when(col("id_genero") == 37, "Velho Oeste")
    .when(col("id_genero") == 9648, "Mistério")
    .otherwise("Desconhecido")
)

dim_genero.write.mode("overwrite").parquet("s3://data-lake-arthur-theodoro/Refined/dim_genero/")


#dim_idioma
dim_idioma = df_trusted.select(col("original_language").alias("codigo_idioma")).distinct().withColumn("id_idioma", monotonically_increasing_id())

dim_idioma.write.mode("overwrite").parquet("s3://data-lake-arthur-theodoro/Refined/dim_idioma/")


#dim_Tempo
dim_tempo = df_trusted.select(col("release_date").alias("data_lancamento")).distinct().withColumn("id_tempo", monotonically_increasing_id())
    
dim_tempo.write.mode("overwrite").parquet("s3://data-lake-arthur-theodoro/Refined/dim_tempo/")


#filme_genero (Tabela de ligação)
filme_genero = df_trusted.select(col("id").alias("id_filme"),explode(col("genre_ids")).alias("id_genero"))

filme_genero.write.mode("overwrite").parquet("s3://data-lake-arthur-theodoro/Refined/filme_genero/")

#fato_filme
fato_filme = df_trusted.join(dim_idioma, df_trusted.original_language == dim_idioma.codigo_idioma).join(dim_tempo, df_trusted.release_date == dim_tempo.data_lancamento) \
    .select(
        monotonically_increasing_id().alias("id_fato_filme"),
        col("id").alias("id_filme"),
        explode(col("genre_ids")).alias("id_genero"),
        col("id_idioma"),
        col("id_tempo"),
        col("popularity").alias("popularidade"),
        col("vote_average").alias("nota_media"),
        col("vote_count").alias("total_votos")
        )
                       
fato_filme.write.mode("overwrite").parquet("s3://data-lake-arthur-theodoro/Refined/fato_filme/")