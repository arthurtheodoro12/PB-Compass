CREATE EXTERNAL TABLE IF NOT EXISTS meubanco.nomes (
  nome string,
  sexo string,
  total integer,
  ano integer
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
 'serialization.format' = ',',
 'field.delim' = ','
)
LOCATION 's3://siteestaticosprint06/dados/' 