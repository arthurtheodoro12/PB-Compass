CREATE OR REPLACE VIEW "refined-db"."frequencia_palavras_filmes" AS
WITH filmes_filtrados AS (
    SELECT 
        f.id_filme,
        f.sinopse,
        i.codigo_idioma AS pais_producao
    FROM 
        "refined-db"."dim_filme" f
    JOIN 
        "refined-db"."fato_filme" ff ON f.id_filme = ff.id_filme
    JOIN 
        "refined-db"."dim_idioma" i ON ff.id_idioma = i.id_idioma
    JOIN 
        "refined-db"."filme_genero" fg ON f.id_filme = fg.id_filme
    JOIN 
        "refined-db"."dim_genero" g ON fg.id_genero = g.id_genero
    JOIN 
        "refined-db"."dim_tempo" t ON ff.id_tempo = t.id_tempo
    WHERE 
        (g.nome_genero = 'Crime' OR g.nome_genero = 'Guerra')
),
palavras AS (
    SELECT 
        palavra,
        pais_producao
    FROM 
        filmes_filtrados,
        UNNEST(SPLIT(REGEXP_REPLACE(LOWER(sinopse), '[^a-záàâãéèêíïóôõöúçñ]', ' '), ' ')) AS t(palavra)
    WHERE 
        palavra IN (
            'guerra', 'soldados', 'missão', 'exército', 'aliados', 'nazistas', 'batalha', 'campo', 
            'resistencia', 'vietnã', 'misseis', 'cuba', 'mísseis', 'míssil', 'russo', 'eua', 
            'russia', 'estados unidos'
        )
)
SELECT 
    palavra,
    pais_producao,
    COUNT(*) AS frequencia
FROM 
    palavras
GROUP BY 
    palavra,
    pais_producao;