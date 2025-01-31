"""Importando Bibliotecas"""

from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import when, rand, lit, floor
import random

"""Lendo arquivo + criando dataframe"""

spark = SparkSession \
.builder \
.master ("local[*]") \
.appName("Exercicio Intro") \
.getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)

df_nomes.show(5)

"""Coluna nomes"""

df_nomes = df_nomes.withColumnRenamed(df_nomes.columns[0], "nomes")

df_nomes.printSchema()

df_nomes.show(10)

"""Criando coluna Escolaridade e populando aleatoriamente"""

df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(rand() < 0.33, "Fundamental")
    .when(rand() < 0.66, "Médio")
    .otherwise("Superior")
)

df_nomes.show(10)

"""Criando coluna Pais e populando aleatoriamente com paises da américa do Sul"""

paises_america_sul = ["Argentina", "Brasil", "Chile", "Colômbia", "Equador", "Paraguai", "Peru",
    "Uruguai", "Bolívia", "Venezuela", "Suriname", "Guiana", "Guiana Francesa"
]

df_nomes = df_nomes.withColumn(
    "Pais",
    when(rand() < 0.0769, lit(random.choice(paises_america_sul)))
    .when(rand() < 0.1538, lit(random.choice(paises_america_sul)))
    .when(rand() < 0.2308, lit(random.choice(paises_america_sul)))
    .when(rand() < 0.3077, lit(random.choice(paises_america_sul)))
    .when(rand() < 0.3846, lit(random.choice(paises_america_sul)))
    .when(rand() < 0.4615, lit(random.choice(paises_america_sul)))
    .when(rand() < 0.5384, lit(random.choice(paises_america_sul)))
    .when(rand() < 0.6154, lit(random.choice(paises_america_sul)))
    .when(rand() < 0.6923, lit(random.choice(paises_america_sul)))
    .when(rand() < 0.7692, lit(random.choice(paises_america_sul)))
    .when(rand() < 0.8462, lit(random.choice(paises_america_sul)))
    .when(rand() < 0.9231, lit(random.choice(paises_america_sul)))
    .otherwise(lit(random.choice(paises_america_sul)))
)

df_nomes.show(10)

"""Criando coluna anoNascimento e populando aleatoriamente com anos entre 1945 e 2010"""

df_nomes = df_nomes.withColumn("AnoNascimento", (rand() * (2010 - 1945) + 1945).cast("int"))

df_nomes.show(10)

"""Filtrando todas as pessoas que nasceram no século 21 e armazenando no dataFrame "df_select"


"""

df_select = df_nomes.filter((df_nomes.AnoNascimento >= 2000) & (df_nomes.AnoNascimento <= 2099)).select("nomes")

df_select.show(10)

"""Filtrando todas as pessoas que nasceram no século 21 e armazenando no dataFrame "df_select", agora usando SparkSQL


"""

df_nomes.createOrReplaceTempView("df_select")

spark.sql("SELECT nomes FROM df_select WHERE AnoNascimento >= 2000 AND AnoNascimento <= 2099").show(10)

"""Contando o número de pessoas nascidos entre 1980 e 1994 (geração millennials) usando o método filter


"""

df_nomes.filter((df_nomes.AnoNascimento >= 1980) & (df_nomes.AnoNascimento <= 1994)).count()

"""Contando o número de pessoas nascidos entre 1980 e 1994 (geração millennials), agora usando o SparkSQL


"""

df_nomes.createOrReplaceTempView("count_millennials")

spark.sql("SELECT COUNT(*) as NumeroMillennials FROM count_millennials WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994").show()

"""Utilizando SparkSQL para obter a quantidade de pessoas de cada país para cada uma das gerações"""

df_nomes.createOrReplaceTempView("pessoas")

df_geracoes = spark.sql("""
    SELECT
        Pais,
        CASE
            WHEN AnoNascimento >= 1944 AND AnoNascimento <= 1964 THEN 'Baby Boomers'
            WHEN AnoNascimento >= 1965 AND AnoNascimento <= 1979 THEN 'Geração X'
            WHEN AnoNascimento >= 1980 AND AnoNascimento <= 1994 THEN 'Millennials'
            WHEN AnoNascimento >= 1995 AND AnoNascimento <= 2015 THEN 'Geração Z'
        END AS Geracao,
        COUNT(*) AS Quantidade
    FROM pessoas
    GROUP BY Pais, Geracao
    ORDER BY Pais, Geracao, Quantidade
""")

df_geracoes.show(42)